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

# Formati dei log Kibana
{: #kibana_formats}

Puoi configurare Kibana in modo da poter visualizzare nella pagina *Rileva* diversi campi per ogni voce di log.
{:shortdesc}



## Formato dei log Kibana per le applicazioni Cloud Foundry
{: #kibana_log_format_cf}

Puoi configurare Kibana in modo che visualizzi nella pagina *Ricerca* i seguenti campi per ogni voce di log:

| Campo | Descrizione |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> L'ora dell'evento registrato. <br> La data e ora è definita fino al millisecondo. |
| @version | La versione dell'evento. |
| ALCH_TENANT_ID | L'ID dello spazio {{site.data.keyword.Bluemix_notm}}. |
| \_id | L'ID univoco per il tuo documento di log. |
| \_index | L'indice per la voce di log. |
| \_type | Il tipo di log, ad esempio *syslog*. |
| app_name | Il nome della tua applicazione. |
| application_id | L'ID univoco della tua applicazione. |
| host | Il nome della tua applicazione che ha prodotto i dati di log. |
| instance_id | L'ID dell'istanza della tua applicazione che ha prodotto i dati di log. |
| loglevel | La severità dell'evento registrato. |
| message | Il messaggio che viene emesso dal componente. <br> Il messaggio varia a seconda dal contesto. |
| message_type | Il flusso in cui viene scritto il messaggio di log. <br> * **OUT** fa riferimento al flusso stdout <br> * **ERR** fa riferimento al flusso stderr. |
| org_id | L'ID univoco della tua organizzazione {{site.data.keyword.Bluemix_notm}} |
| org_name | Il nome dell'organizzazione {{site.data.keyword.Bluemix_notm}} in cui viene preparata la tua applicazione. |
| origin | Il componente in cui l'evento è stato creato. |
| source_id | Il componente che produce i log. <br> Il seguente elenco descrive i log di ogni componente: <br> * **API**: le risposte registrate per le chiamate API che richiedono una modifica allo stato della tua applicazione. <br> * **APP**: le risposte registrate dalla tua applicazione. <br> * **CELL**: le risposte registrate dalla cella Diego che indicano quando un'applicazione viene avviata, interrotta o arrestata in modo anomalo <br> * **LGR**: le risposte registrate dal loggregator che indicano problemi con il processo di registrazione. <br> * **RTR**: le risposte registrate dal Router quando istrada le richieste HTTP alla tua applicazione. <br> * **SSH**: le risposte registrate dalla cella Diego quando un utente accede a un contenitore applicazioni utilizzando il comando `cf ssh`. <br> * **STG**: le risposte registrate dalla cella Diego o dal DEA (Droplet Execution Agent) quando la tua applicazione viene preparata o ripreparata. |
| space_name | Il nome dello spazio {{site.data.keyword.Bluemix_notm}} in cui viene preparata la tua applicazione. |
| timestamp | L'ora dell'evento registrato. La data e ora è definita fino al millisecondo. |
{: caption="Tabella 1. Campi per le applicazioni CF" caption-side="top"}



## Formato di log Kibana per i contenitori Docker distribuiti in un cluster Kubernetes
{: #kibana_log_format_containers_kubernetes}

Puoi configurare Kibana in modo che visualizzi nella pagina *Ricerca* i seguenti campi per ogni voce di log. Questi campi sono impostati da {{site.data.keyword.IBM}} e includono i tuoi dati messaggio. 

| Campo | Descrizione | Altre informazioni |
|-------|-------------|---------------------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> L'ora dell'evento registrato. <br> La data e ora è definita fino al millisecondo. | |
| @version | La versione dell'evento. | |
| ALCH_TENANT_ID | L'ID dello spazio {{site.data.keyword.Bluemix_notm}}. | |
| \_id | L'ID univoco per il tuo documento di log. | |
| \_index | L'indice per la voce di log. | |
| \_score |  |  |
| \_type | Il tipo di log, ad esempio *logs*. | |
| crn_str | Informazioni sull'origine del log. | Per impostazione predefinita, questo campo è impostato da {{site.data.keyword.IBM_notm}}. <br> **Nota**: se invii il messaggio di log in formato JSON valido, e uno dei campi è denominato `crn`, il valore del campo viene sovrascritto con il valore impostato nel messaggio.  |  
| docker.container_id_str | GUID del contenitore in esecuzione in un pod. | |
| ibm-containers.account_str | GUID dell'account {{site.data.keyword.Bluemix_notm}}.  |  |
| ibm-containers.cluster_id_str | GUID del cluster Kubernetes.  |  |
| ibm-containers.cluster_type_str |  | Valore riservato per uso interno di {{site.data.keyword.IBM_notm}}. |
| ibm-containers.region_str | Regione in {{site.data.keyword.Bluemix_notm}}.  |  |
| kubernetes.container_name_str | Nome del contenitore dove viene distribuita un'applicazione.  |  |
| kubernetes.host | Indirizzo IP pubblico del lavoro dove è in esecuzione il contenitore. |  |
| kubernetes.labels.*example_label_name*\_str | Coppia chiave-valore che colleghi a un oggetto Kubernetes come ad esempio un pod. | Ogni etichetta che colleghi a un oggetto Kubernetes è elencata come un campo nella voce di log visualizzata in Kibana. <br> Puoi avere 0 o più etichette. |
| kubernetes.namespace_name_str | Spazio dei nomi Kubernetes dove viene distribuito il contenitore. |  |
| kubernetes.pod_id_str | GUID del pod dove viene distribuito il contenitore. |  |
| kubernetes.pod_name_str | Nome del pod. |  |
| message | Messaggio completo. | Se invii un messaggio in formato JSON valido, ciascun campo viene analizzato singolarmente e visualizzato in Kibana.  |
| stream_str |  | Valore riservato per uso interno di {{site.data.keyword.IBM_notm}}. |
|tag_str |  | Valore riservato per uso interno di {{site.data.keyword.IBM_notm}}. |
{: caption="Tabella 3. Campi per i contenitori Docker" caption-side="top"}


## Formato dei log Kibana per Message Hub
{: #kibana_log_format_messagehub}

Puoi configurare Kibana in modo che visualizzi nella pagina *Ricerca* i seguenti campi per ogni voce di log:

| Campo | Descrizione |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> L'ora dell'evento registrato. <br> La data e ora è definita fino al millisecondo. |
| @version | La versione dell'evento. |
| ALCH_TENANT_ID | L'ID dello spazio {{site.data.keyword.Bluemix_notm}}. |
| \_id | L'ID univoco per il tuo documento di log. |
| \_index | L'indice per la voce di log. |
| \_type | Il tipo di log, ad esempio *syslog*. |
| loglevel | La severità dell'evento registrato, ad esempio, **Info**. |
| module | Questo campo è impostato su **MessageHub**. |
{: caption="Tabella 4. Campi per gli eventi Message Hub" caption-side="top"}

Esempio di una voce di log:

```
March 8th 2017, 17:15:16.454	

message:
    Creating topic ABC
@version:
    1
@timestamp:
    March 8th 2017, 17:15:16.454
loglevel:
    Info
module:
    MessageHub
ALCH_TENANT_ID:
    3d8d2eae-f3f0-44f6-9717-126113a00b51
&#95;id:
    AVqu6vJl1zcfr8KYMI95
&#95;type:
    logs
&#95;index:
    logstash-2017.03.08
```
{: screen}


