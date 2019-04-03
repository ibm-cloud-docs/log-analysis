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


# 从 {{site.data.keyword.Bluemix_notm}} 外部发送日志
{: #log_ingestion}

可以使用多租户 Logstash 转发器将日志从 {{site.data.keyword.IBM_notm}} Cloud 的外部发送到 {{site.data.keyword.loganalysisshort}} 服务。
{:shortdesc}

此功能仅可用于允许日志数据获取的服务套餐。有关更多信息，请参阅[服务套餐](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。

要将日志从 {{site.data.keyword.IBM_notm}} Cloud 的外部发送到 {{site.data.keyword.loganalysisshort}} 服务，您需要以下 Cloud 资源：

* 用于登录到 {{site.data.keyword.Bluemix_notm}} 的 {{site.data.keyword.IBM_notm}} 标识。此用户标识必须具有使用 {{site.data.keyword.Bluemix_notm}} 中空间内的 {{site.data.keyword.loganalysisshort}} 服务的许可权。该空间是 {{site.data.keyword.Bluemix_notm}} 中您计划在其中发送和分析日志的域。
* 使用 {{site.data.keyword.loganalysisshort}} CLI 生成的日志记录令牌，用于向 {{site.data.keyword.loganalysisshort}} 服务认证本地环境。  

在本地环境中，您必须配置 mt-logstash-forwarder，并指定要发送到 {{site.data.keyword.loganalysisshort}} 服务的日志文件。

有关配置本地环境以将日志发送到 {{site.data.keyword.loganalysisshort}} 服务的更多信息，请参阅[将内部部署数据发送到 {{site.data.keyword.Bluemix_notm}} 中的空间](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt)。



## 数据获取 URL
{: #log_ingestion_urls}

下表列出将日志发送到 {{site.data.keyword.Bluemix_notm}} 时必须使用的 URL：

<table>
  <caption>数据获取 URL</caption>
    <tr>
      <th>区域</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>德国</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>悉尼</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>英国</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>美国南部</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


