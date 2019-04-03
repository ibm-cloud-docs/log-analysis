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
{: #downloading_logs1}

Puoi scaricare i log in un file locale o inserire i dati in un altro programma. Scarica i log nel contesto di una sessione. Una sessione specifica quali log saranno scaricati. Se lo scaricamento dei log viene interrotto, la sessione abilita il ripristino dello scaricamento dall'interruzione. Dopo aver completato lo scaricamento, devi eliminare la sessione.
{:shortdesc}

Completa la seguente procedura per scaricare i dati del log disponibili in uno spazio {{site.data.keyword.Bluemix_notm}} in un file locale:

## Passo 1: accedi a IBM Cloud

Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

## Passo 2: Identifica quali log sono disponibili
{: #step31}

1. Utilizza il comando `ibmcloud cf logging status` per vedere quali log sono disponibili per le ultime 2 settimane. Esegui il seguente comando:

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Ad esempio, l'output per l'esecuzione di questo comando è:
    
    ```
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}

    **Nota:** il servizio {{site.data.keyword.loganalysisshort}} è un servizio globale che utilizza l'ora Coordinated Universal Time (UTC). I giorni sono definiti come giorni UTC. Per ottenere i log per un giorno/ora locale specifici, potresti dover scaricare più giorni UTC.


## Passo 3: crea una sessione
{: #step32}

Una sessione è obbligatoria per definire l'ambito dei dati di log disponibili per uno scaricamento e per conservare lo stato dello scaricamento. 

Utilizza il comando [cf logging session create](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) per creare una sessione. Facoltativamente, puoi specificare la data di inizio, di fine e i tipi di log quando crei una sessione:  

* Quando specifici la data di inizio e di fine, la sessione fornisce l'accesso ai log compresi in queste date. 
* Quando specifici il tipo di log (**-t**), la sessione fornisce l'accesso a un tipo di log particolare. Questa funzione è importante quando gestisci i log su larga scala, perché puoi indirizzare una sessione solo su piccole sottoserie di log a cui sei interessato.

**Nota:** per ogni sessione, puoi scaricare i log per un massimo di 15 giorni.

Per creare una sessione che viene utilizzata per scaricare i log del tipo *log*, esegui il seguente comando:

```
ibmcloud cf logging session create -t log
```
{: codeblock}

La sessione restituisce le seguenti informazioni:

* L'intervallo di date che deve essere scaricato. Il valore predefinito è la data UTC corrente.
* I tipi di log che devono essere scaricati. Per impostazione predefinita, include tutti i log disponibili per il periodo di tempo che hai specificato quando hai creato la sessione. 
* Le informazioni sull'inclusione dell'account completo o solo dello spazio corrente. Per impostazione predefinita, ottieni i log nello spazio in cui hai eseguito l'accesso.
* L'ID della sessione, obbligatorio per scaricare i log.

Ad esempio,

```
$ ibmcloud cf logging session create -t log     
+--------------+--------------------------------------+
|     NAME     |                VALUE                 |
+--------------+--------------------------------------+
| Access-Time  | 2017-05-25T18:04:21.743792338Z       |
| Create-Time  | 2017-05-25T18:04:21.743792338Z       |
| Date-Range   | {                                    |
|              |  "End": "2017-05-25T00:00:00Z",      |
|              |  "Start": "2017-05-25T00:00:00Z"     |
|              | }                                    |
| Id           | -jshdjsunelsssr4566722==             |
| Space        | fdgrghg3-b090-4567-vvfg-afbc436902a3 |
| Type-Account | {                                    |
|              |  "Type": "log"                       |
|              | }                                    |
| Username     | xxx@yyy.com                          |
+--------------+--------------------------------------+
```
{: screen}

**Suggerimento:** per visualizzare l'elenco delle sessioni attive, esegui il comando [cf logging session list](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_list1).

## Passo 4: scarica i dati di log in un file
{: #step42}

Per scaricare i log specificati dai parametri della sessione, esegui il seguente comando:

```
ibmcloud cf logging download -o Log_File_Name Session_ID
```
{: codeblock}

dove

* Log_File_Name è il nome del file di output.
* Session_ID è il GUID della sessione. Ottieni questi valori nel passo precedente.

Ad esempio,

```
ibmcloud cf logging download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

L'indicatore di avanzamento si muove da 0 a 100% come vengono scaricati i log.

**Nota:** 

* Il formato dei dati scaricati è un JSON compresso. Se decomprimi il file .gz e lo apri, puoi visualizzare i dati nel formato JSON. 
* Il JSON compresso è adatto all'inserimento per ElasticSearch o Logstash. Se non viene fornito -o, i dati saranno instradati a stdout in modo che puoi inserirli direttamente nel tuo proprio stack ELK.
* Puoi anche elaborare i dati con qualsiasi programma che possa analizzare JSON. 

## Passo 5: elimina la sessione
{: #step51}

Dopo aver completato lo scaricamento, devi eliminare la sessione utilizzando il comando [cf logging session delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_delete1). 

Esegui il seguente comando per eliminare una sessione:

```
ibmcloud cf logging session delete Session_ID
```
{: codeblock}

Dove Session_ID è il GUID della sessione che hai creato in un passo precedente.

Ad esempio,

```
ibmcloud cf logging session delete -jshdjsunelsssr4566722==
+---------+------------------------+
|  NAME   |         VALUE          |
+---------+------------------------+
| Message | Delete session success |
+---------+------------------------+
```
{: screen}




