---

copyright:
  years: 2017, 2019

lastupdated: "2019-03-06"

keywords: IBM Cloud, logging

subcollection: cloudloganalysis

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


# 启用集群日志的自动收集
{: #containers_kube_other_logs}

要能够查看和分析 {{site.data.keyword.loganalysisshort}} 服务中的集群日志，您必须配置集群以将那些日志转发到 {{site.data.keyword.loganalysisshort}} 服务。
{:shortdesc}

## 步骤 1：检查用户标识的许可权
{: step1}

您的用户标识必须具有以下许可权，才能向集群添加日志记录配置：

* {{site.data.keyword.containershort}} 的 IAM 策略，以及**查看者**许可权。
* 集群实例的 IAM 策略，以及**管理员**或**操作员**许可权。

要检查您的用户标识是否具有这些 IAM 策略，请完成以下步骤：

**注**：只有帐户所有者或具有分配策略许可权的用户才能执行此步骤。

1. 登录到 {{site.data.keyword.Bluemix_notm}} 控制台。打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}
	
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 从菜单栏，单击**管理 > 帐户 > 用户**。*用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
3. 选择用户标识并验证该用户标识是否具有这两个策略。




## 步骤 2：设置集群上下文。
{: #step2}

请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 初始化 {{site.data.keyword.loganalysisshort}} 服务插件。

	```
	ibmcloud ks init
	```
	{: codeblock}

3. 设置集群的终端上下文。
    
	```
	ibmcloud ks cluster-config ClusterName
	```
	{: codeblock}

    运行此命令的输出提供您必须在终端运行的命令，以设置配置文件的路径。例如，对于名为 *MyCluster* 的集群，运行以下命令：

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

4. 复制并粘贴命令以在终端中设置环境变量，然后按 **Enter** 键。



## 步骤 3：配置集群
{: step3}

您可以选择转发给 {{site.data.keyword.loganalysisshort}} 服务的集群日志。 

* 要启用 stdout 和 stderr 的自动日志收集和转发，请参阅[启用容器日志的自动日志收集和转发](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#containers)。
* 要启用应用程序日志的自动日志收集和转发，请参阅[启用应用程序日志的自动日志收集和转发](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#apps)。
* 要启用工作程序日志的自动日志收集和转发，请参阅[启用工作程序日志的自动日志收集和转发](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#workers)。
* 要启用 Kubernetes 系统组件日志的自动日志收集和转发，请参阅[启用 Kubernetes 系统组件日志的自动日志收集和转发](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#system)。
* 要启用 Kubernetes Ingress 控制器日志的自动日志收集和转发，请参阅[启用 Kubernetes Ingress 控制器日志的自动日志收集和转发](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#controller)。



## 步骤 4：设置 {{site.data.keyword.containershort_notm}} 密钥所有者的许可权
{: #step4}


{{site.data.keyword.containershort}} 密钥所有者需要以下 IAM 策略：

* {{site.data.keyword.containershort}} 的 IAM 策略，以及**管理员**角色。
* {{site.data.keyword.loganalysisshort}} 服务的 IAM 策略，以及**管理员**角色。

请完成以下步骤： 

1. 登录到 {{site.data.keyword.Bluemix_notm}} 控制台。打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}
	
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 从菜单栏，单击**管理 > 帐户 > 用户**。*用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
3. 选择 {{site.data.keyword.containershort_notm}} 密钥所有者的用户标识，然后验证该用户标识是否具有这两个策略。


将日志转发到空间域时，还必须向组织和空间中的 {{site.data.keyword.containershort}} 密钥所有者授予 Cloud Foundry (CF) 许可权。密钥所有者需要组织的 *orgManager* 角色，以及空间的 *SpaceManager* 或 *Developer* 角色。

请完成以下步骤：

1. 确定帐户中作为 {{site.data.keyword.containershort}} 密钥所有者的用户。在终端中，运行以下命令：

    ```
    ibmcloud ks api-key-info ClusterName
    ```
    {: codeblock}
    
    其中，*ClusterName* 是集群的名称。
    
2. 验证身份为 {{site.data.keyword.containershort}} 密钥所有者的用户是否具有组织的 *orgManager* 角色，以及空间的 *SpaceManager* 和 *Developer* 角色。

    登录到 {{site.data.keyword.Bluemix_notm}} 控制台。打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}。使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

    从菜单栏，单击**管理 > 帐户 > 用户**。*用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
    选择用户标识并验证用户是否具有组织的 *orgManager* 角色，以及空间的 *SpaceManager* 或 *Developer* 角色。
 
3. 如果用户没有正确的许可权，请完成以下步骤：

    1. 向用户授予以下许可权：组织的 *orgManager* 角色，以及空间的 *SpaceManager* 和 *Developer* 角色。有关更多信息，请参阅[使用 IBM Cloud UI 向用户授予查看空间日志的许可权](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space)。
    
    2. 刷新日志记录配置。运行以下命令：
    
        ```
        ibmcloud ks logging-config-refresh ClusterName
        ```
        {: codeblock}
        
        其中，*ClusterName* 是集群的名称。
  




## 启用容器日志的自动日志收集和转发 
{: #containers}

运行以下命令以将 *stdout* 和 *stderr* 日志文件发送到 {{site.data.keyword.loganalysisshort}} 服务：

```
ibmcloud ks logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

其中 

* *ClusterName* 是集群的名称。
* *EndPoint* 是供应 {{site.data.keyword.loganalysisshort}} 服务的区域中的日志记录服务的 URL。有关端点的列表，请参阅[端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)。
* *OrgName* 是其中空间可用的组织的名称。
* *SpaceName* 是供应 {{site.data.keyword.loganalysisshort}} 服务的空间的名称。


例如，要创建日志记录配置，用于将 stdout 和 stderr 日志转发到德国区域中的帐户域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}

要创建日志记录配置，用于将 stdout 和 stderr 日志转发到德国区域中的空间域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace
```
{: screen}



## 启用应用程序日志的自动日志收集和转发 
{: #apps}

运行以下命令以将 */var/log/apps/**/.log* 和 */var/log/apps/*/.err* 日志文件发送到 {{site.data.keyword.loganalysisshort}} 服务：

```
ibmcloud ks logging-config-create ClusterName --logsource application --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName --app-containers --app-paths
```
{: codeblock}

其中 

* *ClusterName* 是集群的名称。
* *EndPoint* 是供应 {{site.data.keyword.loganalysisshort}} 服务的区域中的日志记录服务的 URL。有关端点的列表，请参阅[端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)。
* *OrgName* 是其中空间可用的组织的名称。
* *SpaceName* 是供应 {{site.data.keyword.loganalysisshort}} 服务的空间的名称。
* *app-containers* 是可选参数，您可以设置该参数来定义要监视的容器的列表。这些容器就是从中将日志转发到 {{site.data.keyword.loganalysisshort}} 的容器。您可以设置一个或多个容器（用逗号分隔）。
* *app-paths* 定义要监视的容器内部的路径。您可以设置一个或多个路径（用逗号分隔）。可以使用通配符，如“/var/log/*.log”。 

例如，要创建日志记录配置，用于将应用程序日志转发到德国区域中的空间域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace --app-paths /var/log/*.log
```
{: screen}

例如，要创建日志记录配置，用于将应用程序日志转发到德国区域中的帐户域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --app-paths /var/log/*.log
```
{: screen}



## 启用工作程序日志的自动日志收集和转发 
{: #workers}


运行以下命令以将 */var/log/syslog* 和 */var/log/auth.log* 日志文件发送到 {{site.data.keyword.loganalysisshort}} 服务：

```
ibmcloud ks logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

其中 

* *ClusterName* 是集群的名称。
* *EndPoint* 是供应 {{site.data.keyword.loganalysisshort}} 服务的区域中的日志记录服务的 URL。有关端点的列表，请参阅[端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)。
* *OrgName* 是其中空间可用的组织的名称。
* *SpaceName* 是供应 {{site.data.keyword.loganalysisshort}} 服务的空间的名称。



例如，要创建日志记录配置，用于将工作程序日志转发到德国区域中的空间域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

例如，要创建日志记录配置，用于将工作程序日志转发到德国区域中的帐户域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## 启用 Kubernetes 系统组件日志的自动日志收集和转发
{: #system}

运行以下命令以将 */var/log/kubelet.log* 和 */var/log/kube-proxy.log* 日志文件发送到 {{site.data.keyword.loganalysisshort}} 服务：

```
ibmcloud ks logging-config-create ClusterName --logsource kubernetes --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

其中 

* *ClusterName* 是集群的名称。
* *EndPoint* 是供应 {{site.data.keyword.loganalysisshort}} 服务的区域中的日志记录服务的 URL。有关端点的列表，请参阅[端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)。
* *OrgName* 是其中空间可用的组织的名称。
* *SpaceName* 是供应 {{site.data.keyword.loganalysisshort}} 服务的空间的名称。



例如，要创建日志记录配置，用于将 Kubernetes 系统组件日志转发到德国区域中的空间域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

例如，要创建日志记录配置，用于将 Kubernetes 系统组件日志转发到德国区域中的帐户域，请运行以下命令：

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## 启用 Kubernetes Ingress 控制器日志的自动日志收集和转发
{: #controller}

运行以下命令以将 */var/log/alb/ids/.log*、*/var/log/alb/ids/.err*、*/var/log/alb/customerlogs/.log* 和 /var/log/alb/customerlogs/.err* 日志文件发送到 {{site.data.keyword.loganalysisshort}} 服务：

```
ibmcloud ks logging-config-create ClusterName --logsource ingress --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName
```
{: codeblock}

其中 

* *ClusterName* 是集群的名称。
* *EndPoint* 是供应 {{site.data.keyword.loganalysisshort}} 服务的区域中的日志记录服务的 URL。有关端点的列表，请参阅[端点](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)。
* *OrgName* 是其中空间可用的组织的名称。
* *SpaceName* 是供应 {{site.data.keyword.loganalysisshort}} 服务的空间的名称。



例如，要创建日志记录配置，用于将 Ingress 控制器日志转发到德国区域中的空间域，请运行以下命令：

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

例如，要创建日志记录配置，用于将 Ingress 控制器日志转发到德国区域中的帐户域，请运行以下命令：

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091  
```
{: screen}



