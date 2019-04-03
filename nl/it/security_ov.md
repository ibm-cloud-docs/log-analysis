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

# Sicurezza
{: #security_ov}

Per controllare le azioni {{site.data.keyword.loganalysisshort}} che un utente è autorizzato a eseguire, puoi assegnare uno o più ruoli a un utente. 
{:shortdesc}

Per lavorare con la API di servizio {{site.data.keyword.loganalysisshort}}, devi utilizzare un token UAA o un token IAM. Per inviare i log nel servizio {{site.data.keyword.loganalysisshort}}, ti serve un token di registrazione.


## Modelli di autenticazione
{: #auth1}

Per lavorare con il servizio {{site.data.keyword.loganalysisshort}} tramite la CLI o la API, hai bisogno di un token di autenticazione.

Il servizio {{site.data.keyword.loganalysisshort}} supporta i seguenti modelli di autenticazione:

* [Autenticazione UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)

    Puoi utilizzare la CLI solo per gestire i token UAA.
	
* [Autenticazione IAM](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)

    Il modello di autenticazione IAM offre funzionalità di gestione API, CLI o IU. 

**Nota:** un token UAA e un token IAM scadono dopo un periodo di tempo. 

## Ruoli
{: #roles3}

Ci sono due tipi di ruoli in {{site.data.keyword.Bluemix_notm}} che controllano le azioni che gli utenti possono eseguire quando gestiscono il servizio {{site.data.keyword.loganalysisshort}}:

* Ruoli CF (Cloud Foundry): controlli quali azioni {{site.data.keyword.loganalysisshort}} un utente può eseguire assegnando uno o più ruoli CF. Con tali ruoli, controlli le autorizzazioni dell'utente a visualizzare e gestire i log in uno spazio o in un'organizzazione.
* Ruoli IAM: controlli quali azioni {{site.data.keyword.loganalysisshort}} un utente può eseguire assegnando uno o più ruoli IAM. Con tali ruoli, controlli le autorizzazioni dell'utente a visualizzare e gestire i log di account. 


La seguente tabella elenca il tipo dei ruoli e il dominio in {{site.data.keyword.Bluemix_notm}} che controllano:

<table>
  <caption>Tabella 1. Tipo dei ruoli che controllano le azioni per ogni dominio</caption>
  <tr>
    <th></th>
	<th align="right">Account</th>
    <th align="right">Organizzazione</th>
    <th align="right">Spazio</th>	
  </tr>
  <tr>
    <td align="left">Ruoli CF</td>
	<td align="center">No</td>
	<td align="center">Sì</td>
	<td align="center">Sì</td>
  </tr>
  <tr>
    <td align="left">Ruoli IAM</td>
	<td align="center">Sì</td>
	<td align="center">No</td>
	<td align="center">No</td>
  </tr>
</table>


## Ruoli CF
{: #bmx_roles}

La seguente tabella elenca i privilegi di ciascuno dei ruoli CF per lavorare con il servizio {{site.data.keyword.loganalysisshort}}:

<table>
  <caption>Tabella 2. Ruoli e privilegi Cloud Foundry per lavorare con il servizio {{site.data.keyword.loganalysisshort}}.</caption>
  <tr>
    <th>Ruolo</th>
	<th>Dominio</th>
	<th>Privilegi di accesso</th>
  </tr>
  <tr>
    <td>Gestore</td>
	<td>Organizzazione <br>Spazio</td>
	<td>Tutte le API RESTful</td>
  </tr>
  <tr>
    <td>Sviluppatore</td>
	<td>Spazio</td>
	<td>Tutte le API RESTful</td>
  </tr>
  <tr>
    <td>Revisore</td>
	<td>Organizzazione <br>Spazio</td>
	<td>Solo API RESTful che eseguono operazioni di sola lettura, come l'esecuzione di query dei log.</td>
  </tr>
</table>


## Ruoli IAM
{: #iam_roles}

La seguente tabella elenca i privilegi di ciascuno dei ruoli IAM per lavorare con il servizio {{site.data.keyword.loganalysisshort}}:

<table>
  <caption>Tabella 3. Ruoli e privilegi IAM per lavorare con il servizio {{site.data.keyword.loganalysisshort}}.</caption>
  <tr>
    <th>Ruolo</th>
	<th>Privilegi</th>
  </tr>
  <tr>
    <td>Amministratore</td>
	  <td>Visualizza le informazioni sui log in uno spazio o a livello dell'account. <br>Scarica i log in un file locale oppure inviali a un altro programma quale uno stack Elastic. <br>Visualizza il periodo di conservazione per i log disponibili in uno spazio o in un account. <br>Aggiorna il periodo di conservazione per i log disponibili in uno spazio o in un account. <br>Elenca le sessioni attive e i rispettivi ID. <br>Crea una sessione che puoi utilizzare per scaricare i log. <br>Elimina una sessione, specificata dall'ID sessione. <br>Visualizza lo stato di una sola sessione. <br>Elimina i log. </td>
  </tr>
  <tr>
    <td>Editor</td>
	  <td>Visualizza le informazioni sui log in uno spazio o a livello dell'account. <br>Scarica i log in un file locale oppure inviali a un altro programma quale uno stack Elastic. <br>Visualizza il periodo di conservazione per i log disponibili in uno spazio o in un account. <br>Aggiorna il periodo di conservazione per i log disponibili in uno spazio o in un account. <br>Elenca le sessioni attive e i rispettivi ID. <br>Crea una sessione che puoi utilizzare per scaricare i log. <br>Elimina una sessione, specificata dall'ID sessione. <br>Visualizza lo stato di una sola sessione. <br>Elimina i log.  </td>
  </tr>
  <tr>
    <td>Operatore</td>
	  <td>Visualizza le informazioni sui log in uno spazio o a livello dell'account. <br>Visualizza il periodo di conservazione per i log disponibili in uno spazio o in un account. <br>Elenca le sessioni attive e i rispettivi ID. <br>Visualizza lo stato di una sola sessione. <br>Scarica i log in un file locale oppure inviali a un altro programma quale uno stack Elastic.  <br>Crea una sessione che puoi utilizzare per scaricare i log. <br>Elimina una sessione, specificata dall'ID sessione. </td>
  </tr>
  <tr>
    <td>Visualizzatore</td>
	  <td>Visualizza le informazioni sui log in uno spazio o a livello dell'account. <br>Visualizza il periodo di conservazione per i log disponibili in uno spazio o in un account. <br>Elenca le sessioni attive e i rispettivi ID. <br>Visualizza lo stato di una sola sessione. </td>
  </tr>
</table>

La seguente tabella elenca le relazioni tra la API, una azione di servizio e un ruolo IAM che viene utilizzato dal servizio {{site.data.keyword.loganalysisshort}}.

<table>
  <caption>Tabella 4. Relazione tra la API, una azione di servizio e un ruolo IAM. </caption>
  <tr>
    <th>API</th>
	<th>Azione</th>
	<th>Ruolo IAM</th>
	<th>Descrizione</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>Amministratore, Editor</td>
	<td>Elimina i log.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>Amministratore, Editor, Visualizzatore</td>
	<td>Visualizza le informazioni sui log in uno spazio {{site.data.keyword.Bluemix_notm}} o a livello dell'account.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>Amministratore, Editor</td>
	<td>Scarica i log in un file locale oppure inviali a un altro programma quale uno stack Elastic.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>Amministratore, Editor, Visualizzatore</td>
    <td>Visualizza il periodo di conservazione per i log disponibili in un account o in uno spazio {{site.data.keyword.Bluemix_notm}}.</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>Amministratore, Editor</td>
    <td>Aggiorna il periodo di conservazione per i log disponibili in un account o in uno spazio {{site.data.keyword.Bluemix_notm}}.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Amministratore, Editor, Visualizzatore</td>
    <td>Elenca le sessioni attive e i rispettivi ID.</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>Amministratore, Editor</td>
    <td>Crea una sessione che puoi utilizzare per scaricare i log.</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>Amministratore, Editor</td>
    <td>Elimina una sessione, specificata dall'ID sessione.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Amministratore, Editor, Visualizzatore</td>
    <td>Visualizza lo stato di una sola sessione.</td>
  </tr>
</table>

## Ottenimento di un token di autenticazione per gestire i log utilizzando la API
{: #get_token}

Per gestire i log utilizzando la API {{site.data.keyword.loganalysisshort}}, devi utilizzare un token di autenticazione. 

**Gestione dei log disponibili nel dominio dello spazio**

* Utilizza la CLI {{site.data.keyword.loganalysisshort}} per ottenere il token UAA. 
* Il token ha un tempo di scadenza. 

Per ulteriori informazioni, vedi [Ottenimento del token UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

**Gestione dei log disponibili nel dominio dell'account**

* Usa la CLI {{{site.data.keyword.Bluemix_notm}} per ottenere il token IAM. 
* Il token ha un tempo di scadenza. 

Per ulteriori informazioni, vedi [Ottenimento del token IAM](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1).


## Ottenimento del token di registrazione per inviare i log in Analisi dei log
{: #get_logging_token}

Per inviare i log nel servizio {{site.data.keyword.loganalysisshort}}, ti serve un token di registrazione. 

Per inviare i log a un dominio dello spazio, scegli uno dei seguenti metodi:

* [Ottenimento del token di registrazione per inviare i log a uno spazio utilizzando il comando {{site.data.keyword.Bluemix_notm}} ibmcloud service ](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_cloud_cli)
* [Ottenimento del token di registrazione per inviare i log a uno spazio utilizzando la CLI Analisi dei log](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_la_cloud_cli)
* [Ottenimento del token di registrazione per inviare i log a uno spazio utilizzando la API Analisi dei log](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_api)


## Concessione di autorizzazioni a un utente per lavorare con i log
{: #grant_permissions1}

Per consentire a un utente di gestire i log o di visualizzarli, è necessario concedergli le autorizzazioni in {{site.data.keyword.Bluemix_notm}} a lavorare con il servizio {{site.data.keyword.loganalysisshort}}.

* Per informazioni sulle autorizzazioni necessarie per gestire i log, vedi [Ruoli di cui un utente ha bisogno per gestire i log](/docs/services/CloudLogAnalysis/manage_logs.html#roles1).
* Per informazioni sulle autorizzazioni necessarie per visualizzare i log, vedi [Ruoli di cui un utente ha bisogno per visualizzare i log](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#roles).

Per ulteriori informazioni su come concedere le autorizzazioni, vedi:

* [Assegna una politica IAM a un utente tramite la IU {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions).
* [Assegna una politica IAM a un utente utilizzando la riga di comando](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_commandline).
* [Concessione delle autorizzazioni a un utente per visualizzare i log dello spazio utilizzando la IU {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).


