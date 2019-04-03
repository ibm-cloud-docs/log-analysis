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


# Invio dei log dall'esterno di {{site.data.keyword.Bluemix_notm}}
{: #log_ingestion}

Puoi inviare i log dall'esterno di {{site.data.keyword.IBM_notm}} Cloud nel servizio {{site.data.keyword.loganalysisshort}} utilizzando il Logstash Forwarder a più tenant. 
{:shortdesc}

Questa funzione è disponibile solo per i piani di servizio che consentono l'inserimento di log. Per ulteriori informazioni, vedi [Piani di servizio](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

Per inviare i log dall'esterno di {{site.data.keyword.IBM_notm}} Cloud nel servizio {{site.data.keyword.loganalysisshort}}, hai bisogno delle seguenti risorse Cloud:

* Un ID {{site.data.keyword.IBM_notm}} per accedere a {{site.data.keyword.Bluemix_notm}}. Questo ID utente deve disporre delle autorizzazioni per lavorare con il servizio {{site.data.keyword.loganalysisshort}} in uno spazio in {{site.data.keyword.Bluemix_notm}}. Lo spazio è il dominio in {{site.data.keyword.Bluemix_notm}} in cui intendi inviare e analizzare i log.
* Un token di registrazione generato utilizzando la CLI {{site.data.keyword.loganalysisshort}} e utilizzato per autenticare il tuo ambiente locale con il servizio {{site.data.keyword.loganalysisshort}}.  

Nel tuo ambiente locale, devi configurare l'mt-logstash-forwarder e specificare i file di log che vuoi inviare al servizio {{site.data.keyword.loganalysisshort}}.

Per ulteriori informazioni sulla configurazione del tuo ambiente locale per inviare i log al servizio {{site.data.keyword.loganalysisshort}}, vedi [Invio di dati in loco a uno spazio in {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt).



## URL di inserimento
{: #log_ingestion_urls}

La seguente tabella elenca gli URL che devi usare per inviare i log in {{site.data.keyword.Bluemix_notm}}:

<table>
  <caption>URL di inserimento</caption>
    <tr>
      <th>Regione</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>Germania</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Sydney</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Regno Unito</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Stati Uniti Sud</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


