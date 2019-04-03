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

# Download dei log
{: #downloading_logs}

Puoi scaricare i log in un file locale o inserire i dati in un altro programma. Scarica i log nel contesto di una sessione. Una sessione specifica quali log saranno scaricati. Se lo scaricamento dei log viene interrotto, la sessione abilita il ripristino dello scaricamento dall'interruzione. Dopo aver completato lo scaricamento, devi eliminare la sessione.
{:shortdesc}

Per completare la procedura, devi installare la CLI {{site.data.keyword.loganalysisshort}}. Per ulteriori informazioni, vedi [Configuring the {{site.data.keyword.loganalysisshort}} CLI](https://console.bluemix.net/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli_).


Completa la seguente procedura per scaricare i dati di log disponibili in uno spazio in un file locale:

## Passo 1: accedi a {{site.data.keyword.Bluemix_notm}}
{: #downloading_logs_step1}

Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

## Passo 2: Identifica quali log sono disponibili
{: #step21}

1. Utilizza il comando `ibmcloud logging log-show` per vedere quali log sono disponibili per le ultime 2 settimane. Esegui il seguente comando:

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Ad esempio, l'output per l'esecuzione di questo comando è:
    
    ```
    ibmcloud logging log-show 
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-16   794008   706     All          syslog, default   
	2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}

    **Nota:** il servizio {{site.data.keyword.loganalysisshort}} è un servizio globale che utilizza l'ora Coordinated Universal Time (UTC). I giorni sono definiti come giorni UTC. Per ottenere i log per un giorno/ora locale specifici, potresti dover scaricare più giorni UTC.


## Passo 3: crea una sessione
{: #step3}

Una sessione è obbligatoria per definire l'ambito dei dati di log disponibili per uno scaricamento e per conservare lo stato dello scaricamento. 

Utilizza il comando [ibmcloud logging session-create](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_create) per creare una sessione. Facoltativamente, puoi specificare la data di inizio, di fine e i tipi di log quando crei una sessione:  

* Quando specifici la data di inizio e di fine, la sessione fornisce l'accesso ai log compresi in queste date. 
* Quando specifici il tipo di log (**-t**), la sessione fornisce l'accesso a un tipo di log particolare. Questa funzione è importante quando gestisci i log su larga scala, perché puoi indirizzare una sessione solo su piccole sottoserie di log a cui sei interessato.

**Nota:** per ogni sessione, puoi scaricare i log per un massimo di 15 giorni.

Per creare una sessione che viene utilizzata per scaricare tutti i log disponibili per le ultime 2 settimane, immetti il seguente comando:

```
ibmcloud logging session-create 
```
{: codeblock}

La sessione restituisce le seguenti informazioni:

* L'intervallo di date che deve essere scaricato. Il valore predefinito è la data UTC corrente.
* I tipi di log che devono essere scaricati. Per impostazione predefinita, include tutti i log disponibili per il periodo di tempo che hai specificato quando hai creato la sessione. 
* Le informazioni sull'inclusione dell'account completo o solo dello spazio corrente. Per impostazione predefinita, ottieni i log nello spazio in cui hai eseguito l'accesso.
* L'ID della sessione, obbligatorio per scaricare i log.

Ad esempio,

```
$ ibmcloud logging session-create
Creating session for lopezdsr@uk.ibm.com resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type
944aec4d-61f4-43d1-8f3b-c040195122da   12345678-1234-5678-abcd-378620d6fab5   2017-11-17T14:17:25.611542863Z   2017-11-17T14:17:25.611542863Z   2017-11-04   2017-11-17   ANY_TYPE
Session: 944aec4d-61f4-43d1-8f3b-c040195122da is created
```
{: screen}

**Suggerimento:** per visualizzare l'elenco delle sessioni attive, esegui il comando [ibmcloud logging sessions](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_list).

## Passo 4: scarica i dati di log in un file
{: #step41}

Per scaricare i log specificati dai parametri della sessione, esegui il seguente comando:

```
ibmcloud logging log-download -o Log_File_Name Session_ID
```
{: codeblock}

dove

* Log_File_Name è il nome del file di output.
* Session_ID è il GUID della sessione. Ottieni questi valori nel passo precedente.

Ad esempio,

```
ibmcloud logging log-download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

L'indicatore di avanzamento si muove da 0 a 100% come vengono scaricati i log.

**Nota:** 

* Il formato dei dati scaricati è un JSON compresso. Se decomprimi il file .gz e lo apri, puoi visualizzare i dati nel formato JSON. 
* Il JSON compresso è adatto all'inserimento per ElasticSearch o Logstash. Se non viene fornito -o, i dati saranno instradati a stdout in modo che puoi inserirli direttamente nel tuo proprio stack ELK.
* Puoi anche elaborare i dati con qualsiasi programma che possa analizzare JSON. 

## Passo 5: elimina la sessione
{: #step5}

Al termine del download, devi eliminare la sessione utilizzando il comando [ibmcloud logging session delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete). 

Esegui il seguente comando per eliminare una sessione:

```
ibmcloud logging session-delete Session_ID
```
{: codeblock}

Dove Session_ID è il GUID della sessione che hai creato in un passo precedente.

Ad esempio,

```
ibmcloud logging session-delete -jshdjsunelsssr4566722==
Deleting session: -jshdjsunelsssr4566722== of resource: 12345678-1234-5678-abcd-378620d6fab5 ...
Session: -jshdjsunelsssr4566722== is deleted

```
{: screen}




