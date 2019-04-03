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


# {{site.data.keyword.Bluemix_notm}} の外部からのログ送信
{: #log_ingestion}

マルチテナント Logstash Forwarder を使用することによって、ログを {{site.data.keyword.IBM_notm}} Cloud の外部から {{site.data.keyword.loganalysisshort}} サービスに送信できます。 
{:shortdesc}

この機能は、ログ取り込みが許可されるサービス・プランでのみ使用可能です。 詳しくは、『[サービス・プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。

ログを {{site.data.keyword.IBM_notm}} Cloud の外部から {{site.data.keyword.loganalysisshort}} サービスに送信するには、以下のクラウド・リソースが必要です。

* {{site.data.keyword.Bluemix_notm}} にログインするための {{site.data.keyword.IBM_notm}}ID。 このユーザー ID は、{{site.data.keyword.Bluemix_notm}} のスペース内で {{site.data.keyword.loganalysisshort}} サービスと連携できる許可を持っている必要があります。 そのスペースは、ログの送信と分析を行うことを計画している、{{site.data.keyword.Bluemix_notm}} 内のドメインです。
* {{site.data.keyword.loganalysisshort}} CLI を使用して生成され、{{site.data.keyword.loganalysisshort}} サービスに対してローカル環境を認証するために使用される、ロギング・トークン。  

ローカル環境で、mt-logstash-forwarder を構成し、{{site.data.keyword.loganalysisshort}} サービスに送信したいログ・ファイルを指定する必要があります。

{{site.data.keyword.loganalysisshort}} サービスにログを送信するためのローカル環境の構成について詳しくは、『[{{site.data.keyword.Bluemix_notm}} のスペースへのオンプレミス・データの送信](/docs/services/CloudLogAnalysis/how-to/send-data/send_data_mt.html#send_data_mt)』を参照してください。



## 取り込み URL
{: #log_ingestion_urls}

以下の表は、ログを {{site.data.keyword.Bluemix_notm}} に送信するために使用する必要のある URL を示します。

<table>
  <caption>取り込み URL</caption>
    <tr>
      <th>地域</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>ドイツ</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>シドニー</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>英国</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>米国南部</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


