---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# 配置 LogDNA 代理程序
{: #config_agent}

LogDNA 代理程序负责收集日志并将其转发到 {{site.data.keyword.la_full_notm}} 实例。供应 {{site.data.keyword.la_full}} 的实例后，必须为要监视的每个日志源配置 LogDNA 代理程序。
{:shortdesc}

* LogDNA 代理程序使用 LogDNA 摄入密钥进行认证，并打开安全 Web 套接字来连接 {{site.data.keyword.la_full_notm}} 摄入服务器。 
* 缺省情况下，代理程序会监视 */var/log/* 下扩展名为 *.log* 的所有文件以及无扩展名的文件。
* 代理程序会跟踪新的日志数据，并查找添加到代理程序监视的日志记录目录的新文件。

可以通过 LogDNA 代理程序配置以下参数： 

|参数|描述|
|-----------|-------------|
|`tags`|定义标记以用于将主机自动分组成动态组。|
|`logdir`|定义希望代理程序监视的定制路径。</br>使用逗号分隔多个路径。可以使用 glob 模式。也可以配置特定文件。使用双引号输入 glob 模式。|
|`exclude`|定义不希望 LogDNA 代理程序监视的文件。**注：**这些文件可以位于通过 logdir 参数定义的任何路径中。</br>使用逗号分隔多个文件。可以使用 glob 模式。也可以配置特定文件。|
|`exclude_regex`|定义正则表达式模式以过滤掉与模式匹配的任何行。不要包含前导和尾部 `/`。|
|`hostname`|定义主机名。此值会覆盖操作系统主机名。|
|`autoupdate`|设置为 `1` 可在更新公共存储库代理程序定义时自动更新代理程序。设置为 `0` 可禁用此功能。|  
{: caption="表 1. 用于定制 LogDNA 代理程序的参数" caption-side="top"} 



## 使用脚本在 Kubernetes 集群上配置 LogDNA 代理程序
{: #config_agent_kube_script}

要配置 Kubernetes 集群以将日志发送到 {{site.data.keyword.la_full_notm}} 实例，必须在集群的每个节点上安装 *logdna-agent* pod。LogDNA 代理程序会从安装了该代理程序的 pod 中读取日志文件，并将日志数据转发到 LogDNA 实例。

要配置 Kubernetes 集群以将日志转发到 LogDNA 实例，请通过命令行完成以下步骤：

1. 打开终端以登录到 {{site.data.keyword.cloud_notm}}。

   ```
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   选择已供应 {{site.data.keyword.la_full_notm}} 实例的帐户。

2. 将要配置日志记录的集群设置为此会话的上下文。

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   配置文件下载完成后，会显示一个命令，您可以使用该命令将本地 Kubernetes 配置文件的路径设置为环境变量。复制并粘贴终端中显示的命令，以设置 `KUBECONFIG` 环境变量。

3. 创建 Kubernetes 私钥来存储服务实例的 logDNA 摄入密钥。LogDNA 摄入密钥用于打开安全 Web 套接字来连接 logDNA 摄入服务器，以及向 {{site.data.keyword.la_full_notm}} 服务认证日志记录代理程序。

   ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
   {: pre}

4. 创建 Kubernetes 守护程序集，以用于在 Kubernetes 集群的每个工作程序节点上部署 LogDNA 代理程序。LogDNA 代理程序会收集在 pod 的 `/var/log` 目录中存储的扩展名为 `*.log` 的日志以及无扩展名的文件。缺省情况下，将从所有名称空间（包括 `kube-system`）收集日志，并自动将日志转发到 {{site.data.keyword.la_full_notm}} 服务。

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. 验证 LogDNA 代理程序是否已成功部署。 

   ```
   kubectl get pods
   ```
   {: pre}
   

当您看到一个或多个 LogDNA pod 时，说明部署成功。
* **LogDNA pod 数等于集群中的工作程序节点数。** 
* 所有 pod 都必须处于 `Running` 状态。
* *Stdout* 和 *stderr* 会自动从所有容器收集日志数据并进行转发。日志数据包括应用程序日志和工作程序日志。 
* 缺省情况下，在工作程序上运行的 LogDNA 代理程序 pod 会从该节点上的所有名称空间收集日志，包括 kube-system 日志。



## 在 Kubernetes 集群上向 LogDNA 代理程序添加标记
{: #config_agent_kube_tags}

要添加标记，请完成以下步骤：

1. 设置集群环境。运行以下命令：

    首先，获取用于设置环境变量的命令，并下载 Kubernetes 配置文件。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    配置文件下载完成后，会显示一个命令，您可以使用该命令将本地 Kubernetes 配置文件的路径设置为环境变量。

    复制并粘贴终端中显示的命令，以设置 KUBECONFIG 环境变量。

2. 检查守护程序集的更新策略。然后，选择是使用 *kubectl apply* 还是 *kubectl edit* 来修改代理程序的配置文件。

    要检查更新策略，请运行以下命令：

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    如果更新策略设置为 *OnDelete*，或者如果您具有通过版本控制系统管理的配置文件，请更新本地配置文件，然后使用 *kubectl apply* 将更改应用于 LogDNA 代理程序。

    如果更新策略设置为 *RollingUpdate*，那么可以使用 *kubectl edit* 进行更新并将更改应用于 LogDNA 代理程序。

3. 编辑 `logdna-agent-configmap.yaml` 文件。 

    通过修改本地副本来更新配置文件。**注：**还可以通过运行以下命令来生成代理程序的配置文件：

    ```
    kubectl get configmap logdna-agent -o=yaml > prod-logdna-agent-configmap.yaml
    ```
    {: codeblock}

    或者，使用 *kubectl edit* 来更新配置文件。

    ```
    kubectl edit configmap logdna-agent
    ```
    {: codeblock}

4. 进行更改。添加 **LOGDNA_TAGS** 部分。

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    例如，以下部分显示了在配置文件中添加标记的位置：

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. 如果是在本地编辑文件，请应用配置更改。 

    ```
    kubectl apply -f logdna-agent-configmap.yaml
    ```
    {: codeblock}
    
    **注：**如果使用的是 *kubectl edit*，那么在保存修改时会自动应用更改。


## 在 Linux Ubuntu 或 Debian 上配置 LogDNA 代理程序
{: #config_agent_linux}

要配置 Ubuntu 服务器以将日志发送到 {{site.data.keyword.la_full_notm}} 实例，必须安装 `logdna-agent`。LogDNA 代理程序会从 */var/log* 中读取日志文件，并将日志数据转发到 LogDNA 实例。

要配置 Ubuntu 服务器以将日志转发到 LogDNA 实例，请通过 Ubuntu 终端完成以下步骤：

1. 安装 LogDNA 代理程序。运行以下命令：

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. 设置 LogDNA 代理程序将日志转发到 {{site.data.keyword.la_full_notm}} 实例时必须使用的摄入密钥。  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    其中，INGESTION_KEY 包含要配置为转发日志的 {{site.data.keyword.la_full_notm}} 实例的有效摄入密钥。

3. 设置认证端点。LogDNA 代理程序使用此主机来认证并获取用于转发日志的令牌。

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. 设置摄入端点。

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. 定义要监视的更多日志路径。运行以下命令： 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    缺省情况下，将监视 **/var/log**。

6. （可选）配置 LogDNA 代理程序以标记主机。 


## 在 Linux Ubuntu 或 Debian 上向 LogDNA 代理程序添加标记
{: #config_agent-linux_tags}
 

要向 LogDNA 代理程序添加更多标记，请完成以下步骤：

1. 验证 LogDNA 代理程序是否在运行。

2. 添加一个或多个标记。

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


还可以编辑 LogDNA 配置文件并添加标记。该配置文件位于 */etc/logdna.conf* 中。

1. 编辑该文件。

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. 添加标记。

3. 重新启动 LogDNA 代理程序。

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














