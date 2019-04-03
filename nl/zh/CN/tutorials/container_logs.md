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


# 在 Kibana 中分析 Kubernetes 集群中部署的应用程序的日志
{: #container_logs}
使用本教程可了解如何配置集群以将日志转发到 {{site.data.keyword.Bluemix_notm}} 中的 {{site.data.keyword.loganalysisshort}} 服务。
{:shortdesc}


## 目标
{: #objectives}

1. 配置集群中的日志记录配置。 
2. 对部署在 {{site.data.keyword.Bluemix_notm}} 的 Kubernetes 集群中的应用程序的容器日志执行搜索和分析。

本教程将引导您完成要使以下端到端场景在 {{site.data.keyword.Bluemix_notm}} 中正常执行所需的步骤：供应集群、配置集群以将日志发送到 {{site.data.keyword.Bluemix_notm}} 中的 {{site.data.keyword.loganalysisshort}} 服务、在集群中部署应用程序以及使用 Kibana 查看和过滤该集群的容器日志。


**注**：要完成本教程，必须完成不同步骤中链接的先决条件和教程。


## 先决条件
{: #prereq}

1. 成为 {{site.data.keyword.Bluemix_notm}} 帐户的成员或所有者，并具有创建 Kubernetes 标准集群、将应用程序部署至集群，以及查询 {{site.data.keyword.Bluemix_notm}} 中的日志以在 Kibana 中进行高级分析的许可权。

    您的 {{site.data.keyword.Bluemix_notm}} 用户标识必须已分配有以下策略：
    
    * {{site.data.keyword.containershort}} 的 IAM 策略，以及*编辑者*、*操作员*或*管理员*许可权。
    * {{site.data.keyword.loganalysisshort}} 服务供应所在空间的 CF 角色，以及*开发者*许可权。
    
    有关更多信息，请参阅[通过 IBM Cloud UI 向用户分配 IAM 策略](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account)和[使用 IBM Cloud UI 向用户授予查看空间日志的许可权](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space)。

2. 具有终端会话，您可以从中管理 Kubernetes 集群并从命令行部署应用程序。此教程的示例供 Ubuntu Linux 系统使用。

3. 安装 CLI，以在 Ubuntu 系统中使用 {{site.data.keyword.containershort}} 和 {{site.data.keyword.loganalysisshort}}。

    * 安装 {{site.data.keyword.Bluemix_notm}} CLI。安装 {{site.data.keyword.containershort}} CLI，以在 {{site.data.keyword.containershort}} 中创建和管理 Kubernetes 集群，以及将容器化应用程序部署到集群中。有关更多信息，请参阅[安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview)。
    
    * 安装 {{site.data.keyword.loganalysisshort}} CLI。有关更多信息，请参阅[配置 Log Analysis CLI（IBM Cloud 插件）](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli)。
    
4. 有权访问美国南部区域帐户中名为 **dev** 的空间。 

    集群中可用的日志将配置为转发到与此空间关联的空间域。 
    
    在此空间中，将供应 {{site.data.keyword.loganalysisshort}} 服务。
    
    您必须具有此空间的**开发者**许可权，这样您才能供应 {{site.data.keyword.loganalysisshort}} 服务。
    
    在本教程中，所用组织的名称为 **MyOrg**。

    
 

## 步骤 1：供应 Kubernetes 集群
{: #step25}

请完成以下步骤：

1. 创建标准 Kubernetes 集群。

   有关更多信息，请参阅[创建集群](/docs/containers/cs_tutorials.html#cs_cluster_tutorial)。

2. 在终端中设置集群上下文。设置上下文后，您可以管理 Kubernetes 集群并在 Kubernetes 集群中部署应用程序。

    登录到与您所创建的集群相关联的 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

	初始化 {{site.data.keyword.containershort}} 服务插件。

	```
	ibmcloud cs init
	```
	{: codeblock}

    设置集群的终端上下文。
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    运行此命令的输出提供您必须在终端运行的命令，以设置配置文件的路径。例如：

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    复制并粘贴命令以在终端中设置环境变量，然后按 **Enter** 键。



## 步骤 2：配置集群以将日志自动转发到 {{site.data.keyword.loganalysisshort}} 服务
{: #step26}

部署应用程序时，{{site.data.keyword.containershort}} 会自动收集日志。但是，日志不会自动转发到 {{site.data.keyword.loganalysisshort}} 服务。您必须在集群中创建 1 个或多个日志记录配置，用于定义如下内容：

* 日志要转发到的位置。可以将日志转发到帐户域或空间域。
* 要转发到 {{site.data.keyword.loganalysisshort}} 服务以进行分析的日志。


定义日志记录配置之前，请检查集群中的当前日志记录配置定义。运行以下命令：

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

其中，*ClusterName* 是集群的名称。

例如，为集群 *mycluster* 定义的日志记录配置如下： 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

要查看可为其定义日志记录配置的日志源的列表，请参阅[日志源](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_sources)。


### 配置集群以将 stderr 和 stdout 日志转发到 {{site.data.keyword.loganalysisshort}} 服务
{: #containerstd}


完成以下步骤以将 stdout 和 stderr 日志发送到空间域，其中组织名称为 *MyOrg*，空间名称为 *dev*，位于美国南部区域中：

1. 检查用户标识是否具有添加集群配置的许可权。只有具有 {{site.data.keyword.containershort}} 的 IAM 策略且具有管理集群许可权的用户才能启用此功能。需要以下任何角色：*管理员*、*操作员*

    要检查用户标识已分配 IAM 策略来管理集群，请完成以下步骤：
    
    1. 登录到 {{site.data.keyword.Bluemix_notm}} 控制台。打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}。使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

    2. 从菜单栏，单击**管理 > 帐户 > 用户**。*用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
    3. 选择用户标识并验证该用户标识是否具有 {{site.data.keyword.containershort}} 的策略。

    如果需要许可权，请联系帐户所有者或帐户管理员。只有帐户所有者或具有分配策略许可权的用户才能执行此步骤。

2. 创建集群日志记录配置。运行以下命令以将 *stdout* 和 *stderr* 日志文件发送到 {{site.data.keyword.loganalysisshort}} 服务：

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    其中 

    * *ClusterName* 是集群的名称。
    * *EndPoint* 是供应 {{site.data.keyword.loganalysisshort}} 服务的区域中的日志记录服务的 URL。有关端点的列表，请参阅[端点](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls)。
    * *OrgName* 是其中空间可用的组织的名称。
    * *SpaceName* 是供应 {{site.data.keyword.loganalysisshort}} 服务的空间的名称。


例如，要创建日志记录配置，用于将 stdout 和 stderr 日志转发到美国南部区域中的 dev 空间，请运行以下命令：

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### 配置集群以将工作程序日志转发到 {{site.data.keyword.loganalysisshort}} 服务
{: #workerlogs }

完成以下步骤以将工作程序日志发送到空间域，其中组织名称为 *MyOrg*，空间名称为 *dev*，位于美国南部区域中：

1. 检查用户标识是否具有添加集群配置的许可权。只有具有 {{site.data.keyword.containershort}} 的 IAM 策略且具有管理集群许可权的用户才能启用此功能。需要以下任何角色：*管理员*、*操作员*

    要检查用户标识已分配 IAM 策略来管理集群，请完成以下步骤：
    
    1. 登录到 {{site.data.keyword.Bluemix_notm}} 控制台。打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}。使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

    2. 从菜单栏，单击**管理 > 帐户 > 用户**。*用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
    3. 选择用户标识并验证该用户标识是否具有 {{site.data.keyword.containershort}} 的策略。

    如果需要许可权，请联系帐户所有者或帐户管理员。只有帐户所有者或具有分配策略许可权的用户才能执行此步骤。

2. 创建集群日志记录配置。运行以下命令以将 */var/log/syslog* 和 */var/log/auth.log* 日志文件发送到 {{site.data.keyword.loganalysisshort}} 服务：

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    其中 

    * *ClusterName* 是集群的名称。
    * *EndPoint* 是供应 {{site.data.keyword.loganalysisshort}} 服务的区域中的日志记录服务的 URL。有关端点的列表，请参阅[端点](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls)。
    * *OrgName* 是其中空间可用的组织的名称。
    * *SpaceName* 是供应 {{site.data.keyword.loganalysisshort}} 服务的空间的名称。

    
例如，要创建日志记录配置，用于将工作程序日志转发到美国南部区域中的空间域，请运行以下命令：

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## 步骤 3：授予用户查看空间域中日志的许可权
{: #step33}

要授予用户查看空间中日志的许可权，您必须为该用户分配 Cloud Foundry 角色，该角色描述此用户可以在空间中使用 {{site.data.keyword.loganalysisshort}} 服务执行的操作。 

要授予用户使用 {{site.data.keyword.loganalysisshort}} 服务的许可权，请完成以下步骤：



1. 登录到 {{site.data.keyword.Bluemix_notm}} 控制台。

    打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}
	
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 从菜单栏，单击**管理 > 帐户 > 用户**。 

    *用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
3. 如果用户是帐户的成员，请从列表中选择用户名，或者从*操作*菜单中单击**管理用户**。

    如果用户不是帐户的成员，请参阅[邀请用户](/docs/iam/iamuserinv.html#iamuserinv)。

4. 选择 **Cloud Foundry 访问权**，然后选择组织。

    这将列出该组织中可用空间的列表。

5. 选择空间。然后，从菜单操作中，选择**编辑空间角色**。

    如果看不到美国南部的空间，请先创建空间，然后再继续。

6. 选择*开发者*。

    您可以选择 1 个或多个角色。 
    
    有效角色为：*管理者*、*开发者*和*审计员*
	
7. 单击**保存角色**。


## 步骤 4：授予 {{site.data.keyword.containershort_notm}} 密钥所有者许可权
{: #step52}

要将集群日志转发到空间，{{site.data.keyword.containershort_notm}} 密钥所有者必须具有以下许可权：

* {{site.data.keyword.loganalysisshort}} 服务的 IAM 策略，以及*管理员*许可权。
* 要将日志转发到的组织和空间中的 Cloud Foundry (CF) 许可权。容器密钥所有者需要组织的 *orgManager* 角色，以及空间的 *SpaceManager* 和 *Developer* 角色。

请完成以下步骤：

1. 确定帐户中作为 {{site.data.keyword.containershort}} 密钥所有者的用户。在终端中，运行以下命令：

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    其中，*ClusterName* 是集群的名称。

2. 验证身份为 {{site.data.keyword.containershort}} 密钥所有者的用户是否具有组织的 *orgManager* 角色，以及空间的 *SpaceManager* 和 *Developer* 角色。

    登录到 {{site.data.keyword.Bluemix_notm}} 控制台。打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}。使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

    从菜单栏，单击**管理 > 帐户 > 用户**。*用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
    选择用户标识并验证用户是否具有组织的 *orgManager* 角色，以及空间的 *SpaceManager* 和 *Developer* 角色。

    如果用户没有正确的许可权，请授予用户以下许可权：组织的 *orgManager* 角色，以及空间的 *SpaceManager* 和 *Developer* 角色。有关更多信息，请参阅[使用 IBM Cloud UI 向用户授予查看空间日志的许可权](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space)。
    
3. 验证身份为 {{site.data.keyword.containershort}} 密钥所有者的用户是否具有 {{site.data.keyword.loganalysisshort}} 服务的 IAM 策略，以及*管理员*许可权。

    从菜单栏，单击**管理 > 帐户 > 用户**。*用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
    选择用户标识并验证用户是否已设置 IAM 策略。 

    如果用户没有 IAM 策略，请参阅[通过 IBM Cloud UI 将 IAM 策略分配给用户](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account)。

4. 刷新日志记录配置。运行以下命令：
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    其中，*ClusterName* 是集群的名称。
	



## 步骤 5：在 Kubernetes 集群中部署样本应用程序以在 stdout 中生成内容
{: #step53}

在 Kubernetes 集群中部署并运行样本应用程序。完成以下教程中的步骤以部署样本应用程序：[第 1 课：将单实例应用程序部署到 Kubernetes 集群](/docs/containers/cs_tutorials_apps.html#cs_apps_tutorial_lesson1)。

该应用程序是 Hello World Node.js 应用程序：

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

在此样本应用程序中，当您在浏览器中测试应用程序时，应用程序会将以下消息写入 stdout：`Sample app is listening on port 8080.`






## 步骤 6：在 Kibana 中查看日志数据
{: #step6}

请完成以下步骤：

1. 在浏览器中启动 Kibana。 

    有关如何启动 Kibana 的更多信息，请参阅[通过 Web 浏览器导航至 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)。

    要分析集群的日志数据，必须在创建集群的云 Public 区域中访问 Kibana。 
    
    例如，在美国南部区域中，输入以下 URL 以启动 Kibana：
	
	```
	https://logging.ng.bluemix.net/
```
	{: codeblock}
	
    这将打开 Kibana。
    
    **注**：验证是否是在要转发集群日志的区域中启动的 Kibana。有关每个区域的 URL 的相关信息，请参阅[日志记录端点](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana)。
    	
2. 要查看空间域中可用的日志数据，请完成以下步骤：

    1. 在 Kibana 中，单击您的用户标识。这将打开可设置空间的视图。
    
    2. 选择其中空间可用的帐户。 
    
    3. 选择以下域：**空间**
    
    4. 选择其中空间可用的组织 *MyOrg*。
    
    5. 选择空间 *dev*。
    
    
3. 在**发现**页面中，查看显示的事件。 
        
    在*可用字段*部分中，您可以查看可用于定义新查询或过滤页面上所显示表中列出的条目的字段列表。
    
    下表列出分析应用程序日志时可用于定义新搜索查询的一些字段。该表还包括对应于样本应用程序所生成事件的样本值：
 
    <table>
              <caption>表 2. 容器日志的常用字段</caption>
               <tr>
                <th align="center">字段</th>
                <th align="center">描述</th>
                <th align="center">示例</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>此字段的值对应于收集日志条目的 {{site.data.keyword.Bluemix_notm}} 区域。</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>帐户标识</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str*</td>
                <td>集群标识。</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>集群标识</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str*</td>
                <td>名称空间名称</td>
                <td>*default* 是缺省值。</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>容器名称</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>标签字段是可选的。您可以有 0 个或多个标签。每个标签以前缀 `kubernetes.labels.` 开头，后接 *label_name*。</td>
                <td>在样本应用程序中，您可以看到 2 个标签：<br>* *kubernetes.labels.pod-template-hash_str* = 3355293961<br>* *kubernetes.labels.run_str* =	hello-world-deployment</td>
              </tr>
              <tr>
                <td>*stream_str*</td>
                <td>日志的类型。</td>
                <td>*stdout*、*stderr*</td>
              </tr>
        </table>
     
有关与 Kubernetes 集群相关的其他搜索字段的更多信息，请参阅[搜索日志](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_search)。


## 步骤 7：在 Kibana 中按 Kubernetes 集群名称过滤数据
{: #step7}
    
在*发现*页面上显示的表中，可以查看可用于分析的所有条目。所列出的条目对应于在*搜索*栏中显示的搜索查询。使用星号 (*) 可显示为页面所配置的一段时间内的所有条目。
    
例如，要按 Kubernetes 集群名称过滤数据，请修改*搜索*栏查询。根据定制字段 *kubernetes.cluster_name_str* 添加过滤器：
    
1. 在**可用字段**部分中，选择 *kubernetes.cluster_name_str* 字段。这将显示该字段的可用值子集。    
    
2. 选择对应于要分析其日志的集群的值。 
    
    在您选择值后，*搜索*栏中会添加一个过滤器，而该表将仅显示与您刚刚所选条件匹配的条目。     
   

**注：** 

如果看不到您的集群名称，请为任意集群名称添加过滤器。然后，选择过滤器的编辑符号。    
    
以下查询将显示：
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

将集群的名称 (*cluster1*) 替换为要查看其日志数据的集群名称 *mycluster*。
        
如果看不到任何数据，请尝试更改时间过滤器。有关更多信息，请参阅[设置时间过滤器](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter)。

有关更多信息，请参阅[在 Kibana 中过滤日志](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs)。


## {{site.data.keyword.containershort_notm}} 参考资料
{: reference}

CLI 命令：

* [ibmcloud cs api-key-info](/docs/containers/cs_cli_reference.html#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers/cs_cli_reference.html#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers/cs_cli_reference.html#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers/cs_cli_reference.html#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers/cs_cli_reference.html#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers/cs_cli_reference.html#cs_logging_refresh)

