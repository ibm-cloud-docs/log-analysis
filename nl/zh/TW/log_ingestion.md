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


# 從 {{site.data.keyword.Bluemix_notm}} 外部傳送日誌
{: #log_ingestion}

您可以使用「多方承租戶 Logstash 轉遞程式」，將日誌從 {{site.data.keyword.IBM_notm}} Cloud 外部傳送至 {{site.data.keyword.loganalysisshort}} 服務。
{:shortdesc}

此特性僅適用於容許日誌汲取的服務方案。如需相關資訊，請參閱[服務方案](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。

若要將日誌從 {{site.data.keyword.IBM_notm}} Cloud 外部傳送至 {{site.data.keyword.loganalysisshort}} 服務，您需要下列 Cloud 資源：

* 用來登入 {{site.data.keyword.Bluemix_notm}} 的 {{site.data.keyword.IBM_notm}} ID。此使用者 ID 必須具有在 {{site.data.keyword.Bluemix_notm}} 的空間中使用 {{site.data.keyword.loganalysisshort}} 服務的許可權。空間是 {{site.data.keyword.Bluemix_notm}} 中您計劃傳送及分析日誌的網域。
* 記載記號是使用 {{site.data.keyword.loganalysisshort}} CLI 所產生，並用來向 {{site.data.keyword.loganalysisshort}} 服務鑑別本端環境。  

在本端環境中，您必須配置 mt-logstash-forwarder，並指定您要傳送至 {{site.data.keyword.loganalysisshort}} 服務的日誌檔。

如需配置本端環境以將日誌傳送至 {{site.data.keyword.loganalysisshort}} 服務的相關資訊，請參閱[將內部部署資料傳送至 {{site.data.keyword.Bluemix_notm}} 中的空間](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt)。



## 汲取 URL
{: #log_ingestion_urls}

下表列出您必須用來將日誌傳送至 {{site.data.keyword.Bluemix_notm}} 的 URL：

<table>
  <caption>汲取 URL</caption>
    <tr>
      <th>地區</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>德國</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>雪梨</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>英國</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>美國南部</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


