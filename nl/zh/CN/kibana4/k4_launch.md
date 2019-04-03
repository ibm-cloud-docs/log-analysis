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
{: #k4_launch}

可以通过 {{site.data.keyword.Bluemix}} UI 或直接通过 Web 浏览器启动 Kibana。
{:shortdesc}

通过 {{site.data.keyword.Bluemix_notm}} 启动 Kibana 可在从中启动 Kibana 的资源的上下文中查看和分析数据。例如，可以在特定 CF 应用程序的上下文中，使用 Kibana 显示该 CF 应用程序的日志。

下表列出用于启动 Kibana 的资源和受支持导航方法：

<table>
<caption>表 1. 资源和受支持导航方法的列表。</caption>
  <tr>
    <th>资源</th>
    <th>通过 Bluemix 仪表板导航至 Kibana 仪表板</th>
    <th>通过 Web 浏览器导航至 Kibana 仪表板</th>
  <tr>
  <tr>
    <td>CF 应用程序</td>
    <td>是</td>
    <td>是</td>
  <tr>  
  <tr>
    <td>在 Kubernetes 集群中部署的容器</td>
    <td>是</td>
    <td>是</td>
  <tr>  
</table>

有关 Kibana 的更多信息，请参阅 [Kibana User Guide ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}。
    

##  通过 Bluemix 仪表板导航至 Kibana 仪表板
{: #launch_Kibana_from_bluemix}

用于过滤 Kibana 中所显示数据的查询会检索从中启动 Kibana 的 {{site.data.keyword.Bluemix_notm}} CF 应用程序或 Docker 容器的日志条目。

要在 Kibana 中查看 Cloud Foundry 应用程序或 Docker 容器的日志，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}}，然后在 {{site.data.keyword.Bluemix_notm}}“仪表板”中单击该应用程序名称或容器。 
    
2. 在 {{site.data.keyword.Bluemix_notm}} UI 中打开“日志”选项卡。

    * 对于 CF 应用程序，单击导航栏中的**日志**。 
    * 对于在 {{site.data.keyword.Bluemix_notm}} 管理的基础架构中部署的容器，选择导航栏中的**监视和日志**，然后单击**日志记录**选项卡。 
    
        这将打开“日志”选项卡。  

3. 单击**高级视图**。这将打开 Kibana 仪表板。

    缺省情况下，**发现**页面会装入所选的缺省索引模式，并将时间过滤器设置为最近 30 秒。搜索查询会设置为与 CF 应用程序或 Docker 容器的所有条目相匹配。

    如果“发现”页面未显示任何日志条目，请调整时间选取器。 


##  通过 Web 浏览器导航至 Kibana 仪表板
{: #launch_Kibana_from_browser1}

用于过滤 Kibana 中所显示数据的查询会检索 {{site.data.keyword.Bluemix_notm}} 组织中空间的日志条目。Kibana 显示的日志信息包括在您登录到的 {{site.data.keyword.Bluemix_notm}} 组织空间内部署的所有资源的记录。

要通过浏览器启动 Kibana，请完成以下步骤：

1. 启动 Kibana 用户界面。
    
    例如： 
      
        <table>
          <caption>表 1. 用于启动 Kibana 的 URL</caption>
           <tr>
            <th>区域</th>
            <th>URL</th>
          </tr>
          <tr>
            <td>美国南部</td>
            <td>https://logging.ng.bluemix.net/ </td>
          </tr>
          <tr>
            <td>英国</td>
            <td>https://logging.eu-gb.bluemix.net/ </td>
          </tr>
        </table>

    如果“发现”页面未显示任何日志条目，请调整时间选取器。 

