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


# Gestione dei log
{: #manage_logs}

Puoi utilizzare la CLI {{site.data.keyword.loganalysisshort}} e la API {{site.data.keyword.loganalysisshort}} per gestire i log archiviati in Raccolta dei log.
{:shortdesc}

Per gestire i log, tieni conto delle seguenti informazioni:

1. L'ID utente deve avere una politica assegnata in {{site.data.keyword.Bluemix_notm}} per {{site.data.keyword.loganalysisshort}} con le autorizzazioni a gestire i log. 

    Per un elenco delle attività e dei ruoli IAM per ogni ruolo, vedi [Ruoli IAM](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles). 
	
	Per ulteriori informazioni su come assegnare una politica, vedi [Assegna una politica IAM a un utente tramite la IU {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account).
	
2. Questa funzione è disponibile solo per i piani di servizio che consentono la conservazione dei log. 

    Per ulteriori informazioni sui piani di servizio, vedi [Piani di servizio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

Il servizio {{site.data.keyword.loganalysisshort}} offre due CLI che puoi utilizzare per gestire i log:

* Un plugin {{site.data.keyword.loganalysisshort}} {{site.data.keyword.Bluemix_notm}}. Per ulteriori informazioni sulla CLI, vedi [CLI {{site.data.keyword.loganalysisshort}} (plugin {{site.data.keyword.Bluemix_notm}})](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli).
* Un plugin CF {{site.data.keyword.loganalysisshort}} (Obsoleto). Per ulteriori informazioni sulla CLI, vedi [Configurazione della CLI Analisi dei log (plugin CF)](/docs/services/CloudLogAnalysis/reference/logging_cli.html#logging_cli).


## Configurazione di una politica di conservazione dei log
{: #log_retention_policy}

Puoi utilizzare la CLI {{site.data.keyword.loganalysisshort}} per visualizzare e configurare una politica di conservazione dei log. La politica specifica il numero di giorni per cui i log vengono conservati in Raccolta dei log. 

* Per impostazione predefinita, quando selezioni un piano pagato, i log vengono racconti e conservati in Raccolta dei log. 
* Quando imposti un periodo di conservazione, al suo scadere i log vengono automaticamente eliminati da Raccolta dei log e non possono essere ripristinati.
* Puoi specificare una periodo di conservazione per un account. Il periodo di conservazione viene automaticamente configurato per tutti gli spazi in tale account. 
* Puoi specificare un periodo di conservazione per uno spazio.
* Puoi modificare in qualsiasi momento la politica di conservazione.
* Puoi disabilitare la politica impostandone il valore su *-1*. 

**Nota:** quando disabiliti la politica di conservazione dei log, devi conservare i log nella Raccolta dei log. Puoi utilizzare il comando CLI [cf logging delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#delete4) per eliminare i log vecchi.

Per ulteriori informazioni, vedi:

* [Visualizzazione e configurazione della politica di conservazione dei log utilizzando il plugin {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy).
* [Visualizzazione e configurazione della politica di conservazione dei log utilizzando il plugin CF](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy.html#configuring_retention_policy).


## Eliminazione dei log
{: #log_deletion}

I log archiviati nella Ricerca dei log vengono eliminati dopo 3 giorni.

I log archiviati in Raccolta dei log vengono conservati finché non configuri una politica di conservazione o finché non li elimini manualmente. 

* Puoi configurare una politica di conservazione log per definire il numero di giorni in cui desideri conservare i log nella raccolta di log. Per maggiori informazioni, consulta [Visualizzazione e configurazione della politica di conservazione dei log utilizzando il plugin {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy).

* Puoi utilizzare la [API Raccolta dei log](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} oppure la [CLI Raccolta dei log](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window} per eliminare i log manualmente da Raccolta dei log. 

* Puoi utilizzare la CLI. Per ulteriori informazioni sull'eliminazione manuale dei log tramite la CLI, vedi [ibmcloud logging log-delete utilizzando il plugin {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs).
    


## Download dei log
{: #download_logs2}

Puoi cercare nei log degli ultimi 3 giorni in Kibana. Per poter analizzare i dati di log più vecchi, puoi scaricare i log in un file locale o inserirli in altri programmi come un Elastic Stack locale. 

Per ulteriori informazioni, vedi:

* [Download dei log utilizzando il plugin {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs_cloud.html#downloading_logs).
* [Download dei log utilizzando il plugin CF](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs.html#downloading_logs1).



## Ottenimento di informazioni sui tuoi log
{: #info_about_logs}

Per ottenere informazioni generali sui tuoi log, usa il comando `ibmcloud logging log-show` oppure il comando `cf logging status`. Per ulteriori informazioni, vedi:

* [Visualizzazione di informazioni sui log utilizzando il plugin {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information_cloud.html#viewing_log_status1)
* [Visualizzazione di informazioni sui log utilizzando il plugin CF](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information.html#viewing_log_status1).

Ad esempio, per mantenere i costi sotto controllo, potresti voler monitorare la dimensione dei log delle tue applicazioni per un periodo di tempo. Ad esempio, potresti voler conoscere la dimensione di ogni tipo di log durante una settimana per uno spazio {{site.data.keyword.Bluemix_notm}} per identificare se un'applicazione o un servizio sta generando più log del previsto. Per controllare la dimensione dei tuoi log, usa il comando `ibmcloud logging log-show` oppure il comando `cf logging status`.

Puoi visualizzare le informazioni sui log archiviati in un dominio dello spazio, un dominio dell'organizzazione o un dominio dell'account.



## Installazione della CLI {{site.data.keyword.loganalysisshort_notm}} (plugin {{site.data.keyword.Bluemix_notm}})
{: #install_cli2}

Per informazioni su come installare la CLI, vedi [Installazione della CLI di registrazione](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli).

Per controllare la versione della CLI, esegui il comando `ibmcloud plugin list`.

Per ottenere supporto su come eseguire i comandi, vedi [Come ottenere supporto per la riga di comando per eseguire i comandi](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#command_cli_help).


## Endpoint registrazione
{: #endpoints}

La seguente tabella elenca gli URL di registrazione per ogni regione:

<table>
    <caption>Endpoint per ogni regione</caption>
    <tr>
      <th>Regione</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>Francoforte</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>Sydney</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td>Regno Unito</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>Stati Uniti Sud</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## Ruoli di cui un utente ha bisogno per gestire i log
{: #roles1}

In {{site.data.keyword.Bluemix_notm}}, puoi assegnare uno o più ruoli agli utenti. Questi ruoli definiscono quali attività sono abilitate per tale utente per lavorare con il servizio {{site.data.keyword.loganalysisshort}}. 

Le seguenti tabelle elencano i ruoli che un utente deve avere per gestire i log:

<table>
  <caption>Autorizzazioni di cui un **proprietario dell'account** ha bisogno per gestire i log</caption>
  <tr>
	<th>Ruolo IAM</th>
	<th>Azioni</th>
  </tr>
  <tr>
    <td>*Amministratore*</td>
    <td>Controlla lo stato dei log </br>Scarica log </br>Elimina log </br>Modifica la politica di conservazione dei log </br>Gestisci sessioni </td>
</table>

<table>
  <caption>Autorizzazioni di cui un **revisore** ha bisogno per gestire i log</caption>
  <tr>
	<th>Ruolo IAM</th>
	<th>Azioni</th>
  </tr>
  <tr>
    <td>*Visualizzatore*</td>
    <td>Ottieni informazioni sui log ospitati in Raccolta dei log. </br>Ottieni informazioni sulla politica di conservazione dei log configurata. </td>
</table>

<table>
  <caption>Autorizzazioni di cui un **amministratore** ha bisogno per gestire i log</caption>
  <tr>
	<th>Ruolo IAM</th>
	<th>Azioni</th>
  </tr>
  <tr>
    <td>*Amministratore*</td>
    <td>Controlla lo stato dei log </br>Scarica log </br>Elimina log </br>Modifica la politica di conservazione dei log </br>Gestisci sessioni </td>
</table>

<table>
  <caption>Autorizzazioni di cui uno **sviluppatore** ha bisogno per gestire i log.</caption>
  <tr>
	<th>Ruolo IAM</th>
	<th>Azioni</th>
  </tr>
  <tr>
    <td>*Editor*</td>
    <td>Controlla lo stato dei log </br>Scarica log </br>Elimina log </br>Modifica la politica di conservazione dei log </br>Gestisci sessioni</td>
</table>

