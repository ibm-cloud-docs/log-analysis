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

# 虚拟机
{: #logging_vm_ov}

不会自动为虚拟机 (VM) 启用日志记录功能。但是，可以将 VM 配置为将日志发送到“日志收集”中。要从 VM 收集日志数据并将其发送到 {{site.data.keyword.loganalysisshort}} 服务中，您必须配置多租户 Logstash 转发器 (mt-logstash-forwarder)。然后，可以在 Kibana 中查看、过滤和分析日志。
{:shortdesc}


## 日志获取
{: #log_ingestion2}

{{site.data.keyword.loganalysisshort}} 服务提供了不同的套餐。所有套餐（*轻量*套餐除外）都包含将日志发送到“日志收集”的功能。有关套餐的更多信息，请参阅[服务套餐](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。

可以使用 mt-logstash-forwarder 将日志发送到 {{site.data.keyword.loganalysisshort}}。有关更多信息，请参阅[使用多租户 Logstash 转发器 (mt-logstash-forwarder) 发送日志数据](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt)。


## 日志收集
{: #log_collection2}

缺省情况下，{{site.data.keyword.Bluemix_notm}} 会将日志数据最长存储 3 天：   

* 每天每个空间最多存储 500 MB 数据。超过 500 MB 上限的任何日志都会被废弃。每天凌晨 12:30 UTC 会重置分配的上限。
* 可搜索最长 3 天最多 1.5 GB 的数据。日志数据达到 1.5 GB 或超过 3 天后，会对数据进行滚动式覆盖（先进先出）。

{{site.data.keyword.loganalysisshort}} 服务提供了其他套餐，允许您根据自己的需要，将日志在“日志收集”中存储任意长的时间。有关每个套餐价格的更多信息，请参阅[服务套餐](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。

* 可以配置日志保留时间策略，可用于定义您希望日志在“日志收集”中保留的天数。有关更多信息，请参阅[日志保留时间策略](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#log_retention_policy)。
* 您可以使用日志收集 CLI 或 API 手动删除日志。


## 日志搜索
{: #log_search2}

缺省情况下，在 {{site.data.keyword.Bluemix_notm}} 中可以使用 Kibana 每天最多搜索 500 MB 日志。 

{{site.data.keyword.loganalysisshort}} 服务提供了多种套餐。每种套餐有不同的日志搜索功能，例如*日志收集*套餐允许每天最多搜索 1 GB 数据。有关套餐的更多信息，请参阅[服务套餐](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。


## 日志分析
{: #log_analysis}

要分析日志数据，请使用 Kibana 执行高级分析任务。可以使用 Kibana（一种开放式源代码分析和可视化平台）通过各种图形（例如，图表和表）来对数据进行监视、搜索、分析和可视化表示。有关更多信息，请参阅[在 Kibana 中分析日志](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#analyzing_logs_Kibana)。
