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

# 查看和分析日志 (Kibana)
{:#analyzing_logs_Kibana}

可以使用 Kibana 5.1（一种开放式源代码分析和可视化平台）通过各种图形（例如，图表和表）来对数据进行监视、搜索、分析和可视化表示。使用 Kibana 可执行高级分析任务。
{:shortdesc}

Kibana 是一种基于浏览器的界面，在其中可以通过交互方式分析数据以及定制仪表板，随后可使用这些仪表板来分析日志数据并执行高级管理任务。有关更多信息，请参阅 [Kibana User Guide ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}。

Kibana 页面显示的数据受搜索约束。缺省数据集由预配置的索引模式进行定义。要过滤信息，可以添加新的搜索查询，并将过滤器应用于缺省数据集。然后，可以保存搜索以供未来复用。 

Kibana 包含可用于分析日志的不同页面：

|Kibana 页面|描述
|
|-------------|-------------|
|发现|使用此页面可定义搜索，并通过表和直方图以交互方式分析日志。|
|可视化|使用此页面可创建可视化项，例如图形和表；可以使用可视化项来分析日志数据并比较结果。|
|仪表板|使用此页面可通过保存的可视化项和搜索的集合来分析日志。|
{: caption="表 1. Kibana 页面" caption-side="top"}

**注**：尽管可以追溯 3 天内的数据，但是通过“可视化”页面或“仪表板”页面一次只能分析一个整天的数据。缺省情况下日志数据会存储 3 天。 

|Kibana 页面|时间段信息|
|-------------|-------------------------|
|发现|分析最长 3 天的数据。|
|可视化|分析 24 小时时间段的数据。<br> 可以过滤长度为 24 小时的定制时间段的日志数据。|
|仪表板|分析 24 小时时间段的数据。<br> 可以过滤长度为 24 小时的定制时间段的日志数据。<br> 设置的时间选取器会应用于仪表板中包含的所有可视化项。|
{: caption="表 2. 时间段信息" caption-side="top"}

例如，下面说明了可以如何使用 Kibana 通过不同页面来显示有关空间中 CF 应用程序或容器的信息：

## 导航至 Kibana 仪表板
{: #launch_Kibana}

您可以使用以下任何一种方法来启动 Kibana：

* 通过 {{site.data.keyword.loganalysisshort}} 服务仪表板

    您可以启动 Kibana，以便您看到的数据从所提供空间内的服务聚集日志。
	
	有关更多信息，请参阅[通过 Log Analysis 服务的仪表板浏览至 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_log_analysis)。

* 从 {{site.data.keyword.Bluemix_notm}}

    可以在特定 CF 应用程序的上下文中，使用 Kibana 显示该 CF 应用程序的日志。有关更多信息，请参阅[通过 CF 应用程序的仪表板浏览至 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app)。
    
    可以在特定 Docker 容器的上下文中，使用 Kibana 显示该 Docker 容器的日志。此功能仅适用于在 {{site.data.keyword.Bluemix_notm}} 管理的基础架构中部署的容器。有关更多信息，请参阅[通过容器的仪表板浏览至 Kibana](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers)。
    
    对于 CF 应用程序，用于过滤可在 Kibana 中进行分析的数据的查询会检索 Cloud Foundry 应用程序的日志条目。Kibana 缺省显示的日志信息全部与单个 Cloud Foundry 应用程序及其所有实例相关联。 
    
    对于容器，用于过滤可在 Kibana 中进行分析的数据的查询会检索容器的所有实例的日志条目。Kibana 缺省显示的日志信息全部与单个容器或容器组及其所有实例相关联。 
    
    

* 通过浏览器链接直接打开

    您可能希望启动 Kibana，以便您看到的数据从所提供空间内的服务聚集日志。
    
    用于过滤仪表板中所显示数据的查询会检索 {{site.data.keyword.Bluemix_notm}} 组织中空间的日志条目。Kibana 显示的日志信息包括在您登录到的 {{site.data.keyword.Bluemix_notm}} 组织空间内部署的所有资源的记录。 
    
    有关更多信息，请参阅[通过 Web 浏览器导航至 Kibana 仪表板](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)。
    
    

## 交互式分析数据
{: #analyze_discover}

在“发现”页面中，可以定义新搜索查询并按查询应用过滤器。日志数据将通过表和直方图显示。可以使用这些可视化项以交互方式分析数据。有关更多信息，请参阅[在 Kibana 中以交互方式分析日志](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#analize_logs_interactively)。

可以通过日志字段（例如，message_type 和 instance_ID）来配置过滤器，并可以设置时间段。您可以动态启用或禁用这些过滤器。表和直方图将显示满足所启用的查询和过滤条件的日志条目。有关更多信息，请参阅[在 Kibana 中过滤日志](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs)。

## 通过可视化项分析数据
{: #analyze_visualize}
    
在“可视化”页面中，可以定义新的搜索查询和可视化项。还可以打开保存的可视化项或者保存可视化项。

要分析数据，可以基于现有搜索或新搜索来创建可视化项。Kibana 包含可用于分析信息的不同类型的可视化项，如表、趋势和直方图。每个可视化项的用途各不相同。一些可视化项组织成行，用于提供一个或多个查询的结果。另一些可视化项则显示文档或定制信息。可视化项中的数据可以是固定的，也可以在更新搜索查询时更改。可以在 Web 页面中嵌入可视化项，也可以共享可视化项。 

有关更多信息，请参阅[使用可视化项分析日志](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#kibana_visualizations)。

## 在仪表板中分析数据
{: #analyze_dashboard}

在“仪表板”页面中，可以同时定制、保存和共享多个可视化项和搜索。 

可以在仪表板中添加、除去和重新排列可视化项。有关更多信息，请参阅[在 Kibana 中通过仪表板分析日志](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#analize_logs_dashboard)。
    
定制 Kibana 仪表板后，可以通过其可视化项对数据进行分析，然后保存以供未来复用。有关更多信息，请参阅[保存 Kibana 仪表板](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save)。

## 定制 Kibana
{: #analyze_management}

您还可以通过**管理**页面来配置和管理 Kibana 资源。 

您可以完成以下任务之一：

* 保存、删除、导出和导入搜索。 
* 保存、删除、导出和导入可视化。
* 保存、删除、导出和导入仪表板。
* [刷新字段列表。](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)

## 限制
{: #limitations}

在 Kibana 中，您仅可以与相同组织或帐户的成员共享可视化或仪表板。

不支持以下 Kibana 功能：

* 共享搜索。
* 创建新索引模式。 


## 用户查看日志所需的角色
{: #roles}

在 {{site.data.keyword.Bluemix_notm}} 中，您可以将一个或多个角色分配给用户。这些角色可定义要启用什么任务以便该用户能够使用 {{site.data.keyword.loganalysisshort}} 服务。
 

下表列出用户查看日志时必须具有的角色：

<table>
  <caption>**帐户所有者**查看日志所需的许可权</caption>
  <tr>
    <th>操作</th>
	<th>CF 空间角色</th>
	<th>CF 组织角色</th>
	<th>IAM 角色</th>
  </tr>
  <tr>
    <td>查看空间域中的日志</td>
	<td>*管理者* </br>*开发者* </br>*审计员*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>查看帐户域中的日志</td>
	<td></td>
	<td></td>
	<td>*管理员*</td>
  </tr>
  <tr>
    <td>查看组织域中的日志</td>
	<td></td>
	<td>*管理者* </br>*记帐管理者*  </br>*审计员*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>**审计员**查看日志所需的许可权</caption>
  <tr>
    <th>操作</th>
	<th>CF 空间角色</th>
	<th>CF 组织角色</th>
	<th>IAM 角色</th>
  </tr>
  <tr>
    <td>查看空间域中的日志</td>
	<td>*审计员*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>查看帐户域中的日志</td>
	<td></td>
	<td></td>
	<td>*查看者*</td>
  </tr>
  <tr>
    <td>查看组织域中的日志</td>
	<td></td>
	<td>*审计员*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>**管理员**查看日志所需的许可权</caption>
  <tr>
    <th>操作</th>
	<th>CF 空间角色</th>
	<th>CF 组织角色</th>
	<th>IAM 角色</th>
  </tr>
  <tr>
    <td>查看空间域中的日志</td>
	<td>*开发者*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>查看帐户域中的日志</td>
	<td></td>
	<td></td>
	<td>*查看者*</td>
  </tr>
  <tr>
    <td>查看组织域中的日志</td>
	<td></td>
	<td>*管理者*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>**开发者**查看日志所需的许可权</caption>
  <tr>
    <th>操作</th>
	<th>CF 空间角色</th>
	<th>CF 组织角色</th>
	<th>IAM 角色</th>
  </tr>
  <tr>
    <td>查看空间域中的日志</td>
	<td>*开发者*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>查看帐户域中的日志</td>
	<td></td>
	<td></td>
	<td>*查看者*</td>
  </tr>
  <tr>
    <td>查看组织域中的日志</td>
	<td></td>
	<td>*审计员*</td>
	<td></td>
  </tr>
</table>



## 用于启动 Kibana 的 URL
{: #urls_kibana}

下表列出用于启动 Kibana 的 URL 以及每个区域的 Kibana 版本：

<table>
    <caption>用于启动 Kibana 的 URL</caption>
    <tr>
      <th>区域</th>
      <th>URL</th>
      <th>Kibana 版本</th>
    </tr>
	<tr>
      <td>法兰克福</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>悉尼</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>英国</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
    <tr>
      <td>美国南部</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
</table>




