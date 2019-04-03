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


# 错误消息
{: #error_msgs}

在 {{site.data.keyword.Bluemix}} 上使用 {{site.data.keyword.loganalysisshort}} 服务时，可能会看到以下错误消息：
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**消息描述**

您已达到分配给 {{site.data.keyword.loganalysisfull}} 实例 {Instance GUID} 的 Bluemix 空间 {Space GUID} 的每日配额。您当前为“日志搜索”存储器分配的每日存储量是 500 MB，数据在“日志搜索”存储器中保留 3 天，在此期间可以在 Kibana 中对其进行搜索。要升级套餐，以便每天可以在“日志搜索”存储器中存储更多数据，同时在“日志收集”存储器中保留所有日志，请升级此空间的 {{site.data.keyword.loganalysisshort}} 服务套餐。有关服务套餐以及如何升级套餐的更多信息，请参阅[套餐](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。


**消息说明** 

达到为 Lite 服务套餐分配的“日志搜索”存储量配额时，会收到标识为 *BXNLG020001W* 的消息。轻量套餐是一种补充性服务套餐，您在空间中供应 {{site.data.keyword.loganalysisshort}} 服务时，缺省情况下会设置此套餐。您当前为“日志搜索”存储器分配的每日存储量是 500 MB，数据在“日志搜索”存储器中保留 3 天，在此期间可以在 Kibana 中对其进行搜索。

**恢复**

要升级套餐，以便每天可以在“日志搜索”存储器中存储更多数据，同时在“日志收集”存储器中保留所有日志，请升级此空间的 {{site.data.keyword.loganalysisshort}} 服务套餐。有关服务套餐以及如何升级套餐的更多信息，请参阅[套餐](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。


## BXNLG020002W 
{: #BXNLG020002W}


**消息描述**

您已达到分配给 {{site.data.keyword.loganalysisfull}} 实例 {Instance GUID} 的 Bluemix 空间 {Space GUID} 的每日配额。您当前为“日志搜索”存储器分配的每日存储量是 XXX，数据会保留 3 天，在此期间可以在 Kibana 中对其进行搜索。这不会影响“日志收集”存储器中的日志保留时间策略。要升级套餐，以便每天可以在“日志搜索”存储器中存储更多数据，请升级此空间的 {{site.data.keyword.loganalysisshort}} 服务套餐。有关服务套餐以及如何升级套餐的更多信息，请参阅[套餐](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。

XXX 表示当前套餐可搜索数据的大小。

**消息说明** 

您已达到分配给 {{site.data.keyword.loganalysisfull}} 实例 {Instance GUID} 的空间 {Space GUID} 的每日配额。您当前为“日志搜索”存储器分配的每日存储量是 500 MB、2 GB、5 GB 或 10 GB，数据会保留 3 天，在此期间可以在 Kibana 中对其进行搜索。这不会影响“日志收集”存储器中的日志保留时间策略。

**恢复**

要升级套餐，以便每天可以在“日志搜索”存储器中存储更多数据，请升级此空间的 {{site.data.keyword.loganalysisshort}} 服务套餐。有关服务套餐以及如何升级套餐的更多信息，请参阅[套餐](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。




