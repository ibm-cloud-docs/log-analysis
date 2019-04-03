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


# Protokolle außerhalb von {{site.data.keyword.Bluemix_notm}} senden
{: #log_ingestion}

Sie können Protokolle außerhalb der {{site.data.keyword.IBM_notm}} Cloud über den Multi-Tenant Logstash Forwarder an den {{site.data.keyword.loganalysisshort}}-Service senden. 
{:shortdesc}

Diese Funktion ist nur für Servicepläne verfügbar, die das Einpflegen von Protokollen (Log Ingestion) zulassen. Weitere Informationen finden Sie unter [Servicepläne](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

Um Protokolle außerhalb der {{site.data.keyword.IBM_notm}} Cloud an den {{site.data.keyword.loganalysisshort}}-Service zu senden, benötigen Sie die folgenden Cloud-Ressourcen:

* Eine {{site.data.keyword.IBM_notm}}ID für die Anmeldung bei {{site.data.keyword.Bluemix_notm}}. Diese Benutzer-ID muss über Berechtigungen für die Arbeit mit dem {{site.data.keyword.loganalysisshort}}-Service in einem Bereich in {{site.data.keyword.Bluemix_notm}} verfügen. Der Bereich ist die Domäne in {{site.data.keyword.Bluemix_notm}}, an den Sie Protokolle für die Analyse senden möchten.
* Ein Protokollierungstoken, das über die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle generiert wird und für die Authentifizierung der lokalen Umgebung mit dem {{site.data.keyword.loganalysisshort}}-Service verwendet wird.  

In der lokalen Umgebung müssen Sie den Multi-Tenant Logstash Forwarder (mt-logstash-forwarder) konfigurieren und die Protokolldateien angeben, die an den {{site.data.keyword.loganalysisshort}}-Service gesendet werden sollen.

Weitere Informationen zum Konfigurieren der lokalen Umgebung zum Senden von Protokollen an den {{site.data.keyword.loganalysisshort}}-Service finden Sie unter [Lokale Daten an einen Bereich in {{site.data.keyword.Bluemix_notm}} senden](/docs/services/CloudLogAnalysis/how-to/send-data/send_data_mt.html#send_data_mt).



## Einpflege-URLs
{: #log_ingestion_urls}

In der folgenden Tabelle sind die URLs aufgeführt, die Sie zum Senden von Protokollen an {{site.data.keyword.Bluemix_notm}} verwenden müssen:

<table>
  <caption>Einpflege-URLs</caption>
    <tr>
      <th>Region</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>Deutschland</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Sydney</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Vereinigtes Königreich</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>USA (Süden)</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


