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


# 导航至 Kibana 仪表板
{: #launch}

可以通过 {{site.data.keyword.loganalysisshort}} 服务、通过 {{site.data.keyword.Bluemix}} UI 或直接通过 Web 浏览器启动 Kibana。
{:shortdesc}

对于 CF 应用程序和 Docker 容器，您可以从 {{site.data.keyword.Bluemix_notm}} UI 启动 Kibana，并在从中启动 Kibana 的资源的上下文中分析数据。例如，可以在特定 CF 应用程序的上下文中，使用 Kibana 显示该 CF 应用程序的日志。
    
对于任何云资源（例如在 Kubernetes 基础架构中部署的 Docker 容器），可以直接通过浏览器链接或通过 {{site.data.keyword.loganalysisshort}} 服务仪表板来启动 Kibana，以查看从提供的空间内各服务中聚集的日志数据。用于过滤仪表板中所显示数据的查询会检索组织中空间的日志条目。Kibana 显示的日志信息包括在您登录到的组织空间内部署的所有资源的记录。 

下表列出用于启动 Kibana 的某些云资源和受支持导航方法：

<table>
<caption>表 1. 资源和受支持导航方法的列表。</caption>
  <tr>
    <th>资源</th>
	<th>通过 {{site.data.keyword.loganalysisshort}} 服务仪表板导航至 Kibana 仪表板</th>
    <th>通过 Bluemix 仪表板导航至 Kibana 仪表板</th>
    <th>通过 Web 浏览器导航至 Kibana 仪表板</th>
  </tr>
  <tr>
    <td>CF 应用程序</td>
	<td>是</td>
    <td>是</td>
    <td>是</td>
  </tr>  
  <tr>
    <td>在 Kubernetes 集群中部署的容器</td>
	<td>是</td>
    <td>是</td>
    <td>是</td>
  </tr>  
  <tr>
    <td>在 {{site.data.keyword.Bluemix_notm}} 管理的基础架构中部署的容器（已弃用）</td>
	<td>是</td>
    <td>是</td>
    <td>是</td>
  </tr>  
</table>

有关 Kibana 的更多信息，请参阅 [Kibana User Guide ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}。
    

##  通过 Log Analysis 服务的仪表板导航至 Kibana
{: #launch_Kibana_from_log_analysis}

用于过滤 Kibana 中所显示数据的查询会检索组织中该空间的日志条目。 
	
Kibana 显示的日志信息包括在您登录到的组织空间内部署的所有资源的记录。

要通过 {{site.data.keyword.loganalysisshort}} 服务的仪表板启动 Kibana，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}}，然后在 {{site.data.keyword.Bluemix_notm}}“仪表板”中单击 {{site.data.keyword.loganalysisshort}} 服务。 
    
2. 在 {{site.data.keyword.Bluemix_notm}} UI 中选择**受管**选项卡。

3. 单击**启动**。这将打开 Kibana 仪表板。

缺省情况下，**发现**页面会装入所选的缺省索引模式，并将时间过滤器设置为最近 15 分钟。 

如果“发现”页面未显示任何日志条目，请调整时间选取器。有关更多信息，请参阅[设置时间过滤器](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)。

	
	
##  通过 Web 浏览器导航至 Kibana
{: #launch_Kibana_from_browser}

用于过滤 Kibana 中所显示数据的查询会检索组织中该空间的日志条目。 
	
Kibana 显示的日志信息包括在您登录到的组织空间内部署的所有资源的记录。

要通过浏览器启动 Kibana，请完成以下步骤：

1. 打开 Web 浏览器并启动 Kibana。然后，登录到 Kibana 用户界面。

    要查看每个区域的 URL 列表，请参阅[用于启动 Kibana 的 URL](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana)。
    
    这将打开 Kibana 中的“发现”页面。
	
2. 为要查看并分析其中日志数据的空间选择索引模式。

    1. 单击 **default-index**。
	
	2. 为该空间选择索引模式。索引模式的格式如下：
	
	    ```
	    [logstash-Space_ID-]YYYY.MM.DD 
	    ```
        {: screen}
	
	    其中，*Space_ID* 是要查看并分析其中日志数据的空间的 GUID。 
	
如果“发现”页面未显示任何日志条目，请调整时间选取器。有关更多信息，请参阅[设置时间过滤器](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)。


	
##  通过 CF 应用程序的仪表板导航至 Kibana
{: #launch_Kibana_from_cf_app}

用于过滤 Kibana 中所显示数据的查询会检索从中启动 Kibana 的 {{site.data.keyword.Bluemix_notm}} CF 应用程序的日志条目。

要在 Kibana 中查看 Cloud Foundry 应用程序的日志，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 帐户。

    {{site.data.keyword.Bluemix_notm}}“仪表板”位于：[http://bluemix.net![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}。
    
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 在 {{site.data.keyword.Bluemix_notm}}“仪表板”中单击应用程序名称或容器。 
    
3. 在 {{site.data.keyword.Bluemix_notm}} UI 中打开“日志”选项卡。

    对于 CF 应用程序，单击导航栏中的**日志**。这将打开“日志”选项卡。  

4. 单击**在 Kibana 中查看**。这将打开 Kibana 仪表板。

    缺省情况下，**发现**页面会装入所选的缺省索引模式，并将时间过滤器设置为最近 15 分钟。搜索查询会设置为与 CF 应用程序的所有条目相匹配。

    如果“发现”页面未显示任何日志条目，请调整时间选取器。有关更多信息，请参阅[设置时间过滤器](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)。

	
	
##  通过在 Kubernetes 集群中部署的容器的仪表板导航至 Kibana
{: #launch_Kibana_for_containers_kube}

用于过滤 Kibana 中所显示数据的查询会检索从中启动 Kibana 的集群的日志条目。

要在 Kibana 中查看容器的日志，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 帐户。

    {{site.data.keyword.Bluemix_notm}}“仪表板”位于：[http://bluemix.net![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}。
    
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 从菜单中，选择**仪表板**。

3. 在*集群*部分中，选择集群。

4. 在*概述*部分中，选择**查看日志**。

    这将打开 Kibana。




##  通过在 {{site.data.keyword.Bluemix_notm}} 管理的基础架构中部署的容器的仪表板导航至 Kibana（已弃用）
{: #launch_Kibana_for_containers}

此方法仅适用于在 {{site.data.keyword.Bluemix_notm}} 管理的基础架构中部署的容器。

用于过滤 Kibana 中所显示数据的查询会检索从中启动 Kibana 的容器的日志条目。

要在 Kibana 中查看 Docker 容器的日志，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}}，然后在 {{site.data.keyword.Bluemix_notm}}“仪表板”中单击该容器。 
    
2. 在 {{site.data.keyword.Bluemix_notm}} UI 中打开“日志”选项卡。

    对于在 {{site.data.keyword.IBM_notm}} 管理的基础架构中部署的容器，选择导航栏中的**监视和日志**，然后单击**日志记录**选项卡。 
    
    这将打开“日志”选项卡。  

3. 单击**高级视图**。这将打开 Kibana 仪表板。

    缺省情况下，**发现**页面会装入所选的缺省索引模式，并将时间过滤器设置为最近 30 秒。搜索查询会设置为与 Docker 容器的所有条目相匹配。

    如果“发现”页面未显示任何日志条目，请调整时间选取器。有关更多信息，请参阅[设置时间过滤器](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)。

	



