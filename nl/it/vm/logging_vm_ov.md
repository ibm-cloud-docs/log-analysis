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

# Macchine virtuali
{: #logging_vm_ov}

Le funzionalità di registrazione non vengono abilitate automaticamente per le macchine virtuali (VM). Tuttavia, puoi configurare la tua VM per inviare i log alla raccolta dei log. Per raccogliere e inviare i dati di log da una VM al servizio {{site.data.keyword.loganalysisshort}}, devi configurare un Logstash Forwarder a più tenant (mt-logstash-forwarder). Quindi, puoi visualizzare, filtrare e analizzare i log in Kibana.
{:shortdesc}


## Inserimento log
{: #log_ingestion2}

Il servizio {{site.data.keyword.loganalysisshort}} offre diversi piani. Tutti i piani, con l'eccezione del piano *Lite*, includono la capacità di inviare log alla raccolta di log. Per ulteriori informazioni sui piani, vedi [Piani di servizio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

Puoi inviare log in {{site.data.keyword.loganalysisshort}} utilizzando mt-logstash-forwarder. Per maggiori informazioni, consulta [Invia dati di log utilizzando un logstash forwarder a più tenant (mt-logstash-forwarder)](/docs/services/CloudLogAnalysis/how-to/send-data/send_data_mt.html#send_data_mt).


## Raccolta di log
{: #log_collection2}

Per impostazione predefinita, {{site.data.keyword.Bluemix_notm}} archivia i dati dei log per un massimo di 3 giorni:   

* Viene archiviato un massimo di 500 MB di dati al giorno. Tutti i log che superano i 500 MB vengono scartati. Le assegnazioni dei limiti vengono
reimpostate ogni giorno alle ore 12:30 UTC.
* Sono ricercabili fino a 1,5 GB di dati per una massimo di 3 giorni. Viene eseguito il rollover (la prima voce inserita è la prima a essere eliminata) dei dati di log quando vengono raggiunti i 1,5 GB di dati o vengono superati i 3 giorni.

Il servizio {{site.data.keyword.loganalysisshort}} fornisce ulteriori piani che ti consentono di archiviare i log nella raccolta di log per quanto tempo desideri. Per ulteriori informazioni sul prezzo di ogni piano, vedi [Piani di servizio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

* Puoi configurare una politica di conservazione log che puoi utilizzare per definire il numero di giorni in cui desideri conservare i log nella raccolta di log. Per maggiori informazioni, vedi [Politica di conservazione log](/docs/services/CloudLogAnalysis/manage_logs.html#log_retention_policy).
* Puoi eliminare i log manualmente utilizzando la API o la CLI Raccolta dei log.


## Ricerca log
{: #log_search2}

Per impostazione predefinita, puoi utilizzare Kibana per ricercare fino a 500 MB di log al giorno in {{site.data.keyword.Bluemix_notm}}. 

Il servizio {{site.data.keyword.loganalysisshort}} fornisce più piani. Ogni piano ha diverse capacità di ricerca log, ad esempio, il piano *Raccolta di log* ti consente di ricercare fino a 1 GB di dati al giorno. Per ulteriori informazioni sui piani, vedi [Piani di servizio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).


## Analisi log
{: #log_analysis}

Per analizzare i dati dei log, usa Kibana per eseguire delle attività di analisi avanzate. Puoi utilizzare Kibana, una piattaforma di analisi e visualizzazione open source, per monitorare, ricercare, analizzare e visualizzare i tuoi dati in una varietà di grafici, ad esempio, diagrammi e tabelle. Per maggiori informazioni, vedi [Analisi dei log in Kibana](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#analyzing_logs_Kibana).
