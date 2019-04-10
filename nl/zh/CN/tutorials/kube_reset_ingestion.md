---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

subcollection: LogDNA

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}
{:important: .important}
{:note: .note}


# 重置 Kubernetes 集群使用的摄入密钥以将日志转发到 {{site.data.keyword.la_full_notm}} 实例
{: #kube_reset}

如果用于将日志从集群转发到 {{site.data.keyword.cloud_notm}} 中 {{site.data.keyword.la_full_notm}} 实例的摄入密钥已泄露，那么必须重置该密钥并更新 Kubernetes 集群配置，以使用新的摄入密钥。
{:shortdesc}

## 开始之前
{: #kube_reset_prereqs}

在美国南部区域中工作。{{site.data.keyword.la_full_notm}} 实例和 Kubernetes 集群这两种资源都必须在同一帐户中运行。

{{site.data.keyword.la_full_notm}} 实例在 **Default** 资源组中供应。

请阅读有关 {{site.data.keyword.la_full_notm}} 的信息。有关更多信息，请参阅[关于 LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)。

要完成本教程中的步骤，您的 {{site.data.keyword.IBM_notm}} 标识必须分配有对以下每个资源的 IAM 策略： 

|资源|访问策略的作用域|角色|区域|信息|
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
|资源组 **Default**|资源组|查看者|us-south|要允许用户查看 Default 资源组中的服务实例，此策略是必需的。|
|{{site.data.keyword.la_full_notm}} 服务|资源组|编辑者</br>管理者|us-south|要允许用户重置摄入密钥，此策略是必需的。|
|Kubernetes 集群实例|资源|编辑者|us-south|要在 Kubernetes 集群中删除和配置私钥和 LogDNA 代理程序，此策略是必需的。|
{: caption="表 1. 完成教程所需的 IAM 策略的列表" caption-side="top"} 

有关 {{site.data.keyword.containerlong}} IAM 角色的更多信息，请参阅[用户访问许可权](/docs/containers?topic=containers-access_reference#access_reference)。

安装 {{site.data.keyword.cloud_notm}} CLI 和 Kubernetes CLI 插件。有关更多信息，请参阅[安装 {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)。


## 步骤 1：重置摄入密钥
{: #kube_reset_step1}

要使用 {{site.data.keyword.la_full_notm}} Web UI 来更新 {{site.data.keyword.la_full_notm}} 实例的摄入密钥，请完成以下步骤：

1. 启动 {{site.data.keyword.la_full_notm}} Web UI。有关更多信息，请参阅[启动 {{site.data.keyword.la_full_notm}} Web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 选择**配置**图标。然后，选择**组织**。 

3. 选择 **API 密钥**。

    您可以看到已创建的摄入密钥。 

4. 选择**生成摄入密钥**。

    新的密钥会添加到列表中。

5. 删除旧的摄入密钥。单击**删除**。


## 步骤 2：除去集群中使用旧摄入密钥的任何配置
{: #kube_reset_step2}

完成以下步骤：

1. 打开终端。然后，登录到 {{site.data.keyword.cloud_notm}}。运行以下命令并遵循提示进行操作：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    选择已供应 {{site.data.keyword.la_full_notm}} 实例的帐户。

2. 设置集群环境。运行以下命令：

    首先，获取用于设置环境变量的命令，并下载 Kubernetes 配置文件。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置文件下载完成后，会显示一个命令，您可以使用该命令将本地 Kubernetes 配置文件的路径设置为环境变量。

    复制并粘贴终端中显示的命令，以设置 KUBECONFIG 环境变量。

    **注：**每次登录到 {{site.data.keyword.containerlong}} CLI 来使用集群时，都必须运行这些命令以将集群的配置文件的路径设置为会话变量。Kubernetes CLI 使用此变量来查找与 {{site.data.keyword.cloud_notm}} 中的集群连接所必需的本地配置文件和证书。

3. 从 Kubernetes 集群中除去私钥。Kubernetes 私钥包含 LogDNA 摄入密钥。运行以下命令：

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. 除去 Kubernetes 集群的每个工作程序（节点）上的 LogDNA 代理程序。LogDNA 代理程序负责收集和转发日志。运行以下命令：

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. 验证 LogDNA 代理程序是否已成功删除。运行以下命令：

    ```
    kubectl get pods
    ```
    {: codeblock}

    您应该不会看到任何 LogDNA pod。


## 步骤 3：使用新的摄入密钥配置 Kubernetes 集群
{: #kube_reset_step3}

要配置 Kubernetes 集群以将日志转发到 LogDNA 实例，请通过命令行完成以下步骤：

1. 打开终端。然后，登录到 {{site.data.keyword.cloud_notm}}。运行以下命令并遵循提示进行操作：

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    选择已供应 {{site.data.keyword.la_full_notm}} 实例的帐户。

2. 设置集群环境。运行以下命令：

    首先，获取用于设置环境变量的命令，并下载 Kubernetes 配置文件。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置文件下载完成后，会显示一个命令，您可以使用该命令将本地 Kubernetes 配置文件的路径设置为环境变量。

    复制并粘贴终端中显示的命令，以设置 KUBECONFIG 环境变量。

    **注：**每次登录到 {{site.data.keyword.containerlong}} CLI 来使用集群时，都必须运行这些命令以将集群的配置文件的路径设置为会话变量。Kubernetes CLI 使用此变量来查找与 {{site.data.keyword.cloud_notm}} 中的集群连接所必需的本地配置文件和证书。

3. 向 Kubernetes 集群添加私钥。运行以下命令：

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE 显示实例的 LogDNA 摄入密钥。

    Kubernetes 私钥包含 LogDNA 摄入密钥。LogDNA 摄入密钥用于向 {{site.data.keyword.la_full_notm}} 服务认证日志记录代理程序。还用于打开安全 Web 套接字来连接日志记录后端系统上的摄入服务器。

4. 在 Kubernetes 集群的每个工作程序（节点）上配置 LogDNA 代理程序。运行以下命令：

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    LogDNA 代理程序负责收集和转发日志。

    代理程序会自动收集位于 /var/log 下扩展名为 *.log 的日志以及无扩展名的文件。缺省情况下，将从所有名称空间（包括 kube-system）收集日志。

5. 验证 LogDNA 代理程序是否已成功创建并验证其状态。运行以下命令：

    ```
    kubectl get pods
    ```
    {: codeblock}


## 步骤 4：启动 LogDNA Web UI
{: #kube_reset_step4}

要通过 {{site.data.keyword.cloud_notm}} UI 启动 IBM Log Analysis with LogDNA 仪表板，请完成以下步骤：

1. 登录到 {{site.data.keyword.cloud_notm}} 帐户。

    单击 [{{site.data.keyword.cloud_notm}} 仪表板 ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window} 以启动 {{site.data.keyword.cloud_notm}}“仪表板”。

	使用用户标识和密码登录后，{{site.data.keyword.cloud_notm}}“仪表板”即会打开。

2. 在导航菜单中，选择**可观察性**。 

3. 选择**日志记录**。 

    这将显示 {{site.data.keyword.cloud_notm}} 上可用的 {{site.data.keyword.la_full_notm}} 实例的列表。

3. 选择一个实例。然后，单击**查看日志**。

    LogDNA Web UI 将打开并显示集群日志。


## 步骤 5：查看日志
{: #kube_reset_step5}

在 LogDNA Web UI 中，可以在日志通过系统时查看这些日志。您可以使用日志跟踪来查看日志。 

**注：**使用**免费**服务套餐时，只能跟踪最新的日志。



## 后续步骤
{: #kube_reset_next_steps}

  如果要[过滤集群日志](https://docs.logdna.com/docs/filters)、[搜索集群日志](https://docs.logdna.com/docs/search)、[定义视图](https://docs.logdna.com/docs/views)和[配置警报](https://docs.logdna.com/docs/alerts)，那么必须将 {{site.data.keyword.la_full_notm}} 套餐升级为付费套餐。



