---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# 从实例拆离 LogDNA 代理程序
{: #detach_agent}

从日志记录实例拆离 LogDNA 代理程序可停止收集日志。
{:shortdesc}

## 从 Kubernetes 集群拆离 LogDNA 代理程序
{: #detach_agent_kube}

要使 Kubernetes 集群停止向 {{site.data.keyword.la_full_notm}} 实例发送日志，必须从该集群除去 LogDNA 代理程序。 

要使 Kubernetes 集群停止向 LogDNA 实例转发日志，请通过命令行完成以下步骤：

1. 打开终端。然后，[登录到 {{site.data.keyword.cloud_notm}} ![外部链接图标](../../icons/launch-glyph.svg "外部链接图标")](https://cloud.ibm.com/login){:new_window}，并遵循提示进行操作。

    选择已供应 {{site.data.keyword.la_full_notm}} 实例的帐户。

2. 设置集群环境。运行以下命令：

    首先，获取用于设置环境变量的命令，并下载 Kubernetes 配置文件。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置文件下载完成后，会显示一个命令，您可以使用该命令将本地 Kubernetes 配置文件的路径设置为环境变量。

    然后，复制并粘贴终端中显示的命令，以设置 `KUBECONFIG` 环境变量。

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




