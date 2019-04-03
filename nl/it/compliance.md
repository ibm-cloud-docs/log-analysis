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


# Conformità
{: #compliance}

[ {{site.data.keyword.Bluemix}} fornisce una piattaforma cloud e i servizi creati con gli standard di sicurezza più rigorosi di IBM.](/docs/security/compliance.html#compliance). Il servizio {{site.data.keyword.loganalysislong}} è un servizio DevOps creato per {{site.data.keyword.Bluemix_notm}}. 
{:shortdesc}


## Normative sulla protezione dei dati generali (GDPR)

Le normative sulla protezione dei dati generali (GDPR) cercano di creare un quadro giuridico di protezione dei dati armonizzato nella UE e ha lo scopo di ridare ai cittadini il controllo dei propri dati personali, mentre impone regole rigorose a chi ospita e ‘elabora’ questi dati, ovunque nel mondo. Il Regolamento introduce anche regole inerenti la libera circolazione di dati personali all'interno e all'esterno dell'UE. 

**Dichiarazione:** il servizio {{site.data.keyword.loganalysisshort}} archivia e visualizza i record di log dalle risorse cloud in esecuzione nel tuo account in {{site.data.keyword.Bluemix_notm}} e dai log che potresti inviare dall'esterno di {{site.data.keyword.Bluemix_notm}}. Le informazioni personali (PI) non devono essere incluse nelle voci di log archiviate in {{site.data.keyword.loganalysisshort}} poiché questi dati sono accessibili ad altri utenti nella tua azienda, nonché a {{site.data.keyword.IBM_notm}} per poter abilitare il supporto del servizio cloud.

### Regioni
{: #regions}

Il servizio {{site.data.keyword.loganalysisshort}} è conforme al regolamento GDPR nelle regioni di {{site.data.keyword.Bluemix_notm}} pubblico in cui è disponibile il servizio.


### Conservazione di dati
{: #data_retention}

Il servizio {{site.data.keyword.loganalysisshort}} include 2 repository di dati in cui possono essere archiviati i tuoi dati: 

* Ricerca dei log, che ospita i dati di log disponibili per l'analisi tramite Kibana.
* Raccolta dei log, che ospita i dati di log per l'archiviazione a lungo termine.

A seconda del piano di servizio di {{site.data.keyword.loganalysisshort}}, i dati vengono archiviati nella Ricerca dei log o anche nella Raccolta dei log. Il piano lite o standard archivia i dati solo nella Ricerca dei log. I rimanenti piani archiviano i dati nella Ricerca dei log e nella Raccolta dei log.

* I log che vengono archiviati nella Ricerca dei log vengono conservati per 3 giorni.
* I log archiviati in Raccolta dei log vengono conservati finché non configuri una politica di conservazione o finché non li elimini manualmente. Per impostazione predefinita, i log vengono conservati a tempo indefinito nella Raccolta dei log.



### Eliminazione dei dati
{: #data_deletion}

Tieni conto delle seguenti informazioni:

* I log archiviati nella Ricerca dei log vengono eliminati dopo 3 giorni.

* I log archiviati nella Raccolta dei log vengono eliminati dopo alcuni giorni quando configuri una politica di conservazione o quando li elimini manualmente. 

    Puoi configurare una politica di conservazione log per definire il numero di giorni in cui desideri conservare i log nella raccolta di log. Per maggiori informazioni, consulta [Visualizzazione e configurazione della politica di conservazione dei log utilizzando il plugin {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy).

    Puoi utilizzare la [API Raccolta dei log](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} oppure la [CLI Raccolta dei log](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window} per eliminare i log manualmente da Raccolta dei log. 

    Puoi utilizzare la CLI per eliminare i log manualmente dalla Raccolta dei log. Per ulteriori informazioni, vedi [ibmcloud logging log-delete utilizzando il plugin {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs).


Se passi da un piano a pagamento a uno standard o lite, i log nella Raccolta dei log saranno eliminati in circa un giorno.

In qualsiasi momento, puoi aprire un ticket di supporto e richiedere che tutti i tuoi dati siano eliminati dalla Ricerca dei log o dalla Raccolta dei log. Per informazioni su come aprire un ticket di supporto IBM, vedi [Come contattare il supporto](/docs/get-support/howtogetsupport.html#getting-customer-support).



### Ulteriori informazioni
{: #info}

Per ulteriori informazioni, vedi:

[Conformità di sicurezza di {{site.data.keyword.Bluemix_notm}}](/docs/security/compliance.html#compliance)

[GDPR - Pagina ufficiale {{site.data.keyword.IBM_notm}}](https://www.ibm.com/data-responsibility/gdpr/)



