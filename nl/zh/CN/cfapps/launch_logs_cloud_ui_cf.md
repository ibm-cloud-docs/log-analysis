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

# 导航至 Cloud Foundry 应用程序的日志
{: #launch_logs_cloud_ui_cf}

在 {{site.data.keyword.Bluemix}} UI 中，可以通过为每个 Cloud Foundry 应用程序提供的日志选项卡，或通过 {{site.data.keyword.loganalysisshort}} 服务 UI 来查看、过滤和分析日志。
{:shortdesc}

要查看 CF 应用程序日志，请考虑以下信息： 

<table>
  <caption>有关 {{site.data.keyword.Bluemix_notm}} 中 CF 应用程序日志的信息</caption>
  <tr>
    <th>UI 选项</th>
    <th>信息</th>
  </tr>
  <tr>
    <td>通过 CF 应用程序 UI 提供的“日志”选项卡</td>
    <td>可用于分析的日志包含最近 24 小时的数据。</td>
  </tr>
  <tr>
    <td>{{site.data.keyword.loganalysisshort}} 仪表板 (Kibana)</td>
    <td>可用于分析的日志包含最近 3 天的数据。您还可以指定定制时间段。</td>
  </tr>
</table>


## 通过 CF 应用程序仪表板导航至 CF 应用程序日志 
{: #cfapp_ui}

要查看 Cloud Foundry 应用程序的部署或运行时日志，请完成以下步骤：

1. 在“应用程序”仪表板中，单击 Cloud Foundry 应用程序的名称。 
    
2. 在“应用程序详细信息”页面中，单击**日志**。
    
    在**日志**选项卡中，可以查看应用程序的最近日志或实时跟踪日志。此外，可以按组件（日志类型）、按应用程序实例标识以及按错误来过滤日志。
    
缺省情况下，{{site.data.keyword.Bluemix_notm}} 控制台中可用于分析的日志包含最近 24 小时的数据。


## 通过 {{site.data.keyword.loganalysisshort}} UI 导航至 CF 应用程序日志 
{: #cfapp_la}

要查看 Cloud Foundry 应用程序的部署或运行时日志，请完成以下步骤：

1. 在“应用程序”仪表板中，单击 Cloud Foundry 应用程序的名称。 
    
2. 在“应用程序详细信息”页面中，单击**日志**。
    
3. 单击**在 Kibana 中查看**。

缺省情况下，可用于分析的日志包含最近 15 分钟的数据。

**提示**：要分析定制时间段的数据，请参阅[使用 Kibana 进行高级日志分析](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#analyzing_logs_Kibana)。 


