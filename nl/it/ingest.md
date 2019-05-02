---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

subcollection: LogDNA

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

 
# Invio dei log
{: #ingest}

Puoi inviare i dati di log a un'istanza {{site.data.keyword.la_full_notm}}. 
{:shortdesc}

Per inviare i log in modo programmatico, completa la seguente procedura:

## Passo 1. Ottieni la chiave API di inserimento 
{: #ingest_step1}

**Nota:** per completare questo passo, devi disporre del ruolo **gestore** per il servizio o l'istanza {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi [Concessione delle autorizzazioni per gestire i log e configurare gli avvisi in LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

Per ottenere la chiave di inserimento, completa la seguente procedura:
    
1. Avvia l'IU web {{site.data.keyword.la_full_notm}}. Per ulteriori informazioni, vedi il documento relativo all'[accesso all'IU web {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleziona l'icona **Configuration** ![Icona Configuration](images/admin.png). Seleziona quindi **Organization**. 

3. Seleziona **API keys**.

    Puoi visualizzare le chiavi di inserimento che sono state create. 

4. Utilizza una chiave di inserimento esistente o fai clic su **Generate Ingestion Key** per crearne una nuova.

    Una nuova chiave viene aggiunta all'elenco. Copia la chiave.


## Passo 2. Invia i log
{: #ingest_step2}

Per inviare i log, esegui il seguente comando cURL:

```
curl "ENDPOINT/logs/ingest?PARAMETRI_QUERY" -u CHIAVE_DI_INSERIMENTO: --header "Content-Type: application/json; charset=UTF-8" -d "RIGHE_LOG"
```
{: codeblock}

Dove 

* *ENDPOINT* rappresenta il punto di ingresso del servizio. Ogni regione ha un URL differente.
* PARAMETRI_QUERY sono i parametri che definiscono i criteri di filtro applicati alla richiesta di inserimento.
* RIGHE_LOG descrivono l'insieme di righe di log che desideri inviare. È definito come un array di oggetti.
* CHIAVE_DI_INSERIMENTO è la chiave che hai creato nel passo precedente.

La seguente tabella elenca gli endpoint per ogni regione:

| Regione         | Endpoint                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="Endpoint per ogni regione" caption-side="top"} 


La seguente tabella elenca i parametri di query:

| Parametro di query | Tipo       | Stato     | Descrizione |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | richiesto   | Nome host dell'origine. |
| `mac`           | `string`     | facoltativo   | L'indirizzo mac di rete del computer host.    |
| `ip`            | `string`     | facoltativo   | L'indirizzo IP locale del computer host.  | 
| `now`           | `date-time`  | facoltativo   | La data/ora UNIX di origine in millisecondi al momento della richiesta. Se ne fa uso per calcolare la desincronizzazione temporale.|
| `tags`          | `string`     | facoltativo   | Tag che vengono utilizzate per raggruppare dinamicamente gli host. |
{: caption="Parametri di query" caption-side="top"} 



La seguente tabella elenca i dati richiesti per ogni riga di log:

| Parametri     | Tipo       | Descrizione                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | Data/ora UNIX, compresi i millisecondi, quando è stata registrata la voce di log.       | 
| `line`           | `string`     | Testo della riga di log.                                     |
| `app`            | `string`     | Nome dell'applicazione che genera la riga di log.  |
| `level`          | `string`     | Imposta un valore per il livello. Ad esempio, dei valori di esempio per questo parametro sono `INFO`, `WARNING`, `ERROR`. |
| `meta`           |            | Questo campo è riservato per le informazioni personalizzate associate a una riga di log. Per aggiungere dei metadati ad una chiamata API, specifica il campo meta sotto l'oggetto delle righe. I metadati possono essere visualizzati all'interno del contesto di tale riga.                      |
{: caption="Campi degli oggetti riga" caption-side="top"} 

Ad esempio, il seguente esempio mostra il JSON per una riga di log che desideri inserire:

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00,
      "line":"This is my first log line.",
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## Esempio
{: #ingest_example}

Il seguente esempio mostra il comando cURL per inviare 1 riga di log a un'istanza del servizio {{site.data.keyword.la_full_notm}}: 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

