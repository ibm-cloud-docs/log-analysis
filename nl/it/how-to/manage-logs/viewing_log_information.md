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

# Visualizzazione delle informazioni sul log
{: #viewing_log_status}

Utilizza il comando [cf logging status](/docs/services/CloudLogAnalysis/reference/logging_cli.html#status1) per ottenere le informazioni sui log che vengono raccolti e archiviati in Raccolta dei log.
{:shortdesc}

## Ottenimento delle informazioni sui log per un periodo di tempo
{: #viewing_logs1}

Utilizza il comando `cf logging status` per visualizzare la dimensione, il numero, i tipi di log e se i log sono disponibili o meno per l'analisi in Kibana dei log archiviati in Raccolta dei log. 

Utilizza il comando `cf logging status` con le opzioni **-s** per configurare il giorno di inizio e **-e** per il giorno di fine. Ad esempio:

* `cf logging status` fornisce le informazioni sulle ultime 2 settimane.
* `cf logging status -s 2017-05-03` fornisce le informazioni dal 3 maggio 2017 fino alla data corrente.
* `cf logging status -s 2017-05-03 -e 2017-05-08` fornisce le informazioni dal 3 all'8 maggio 2017. 

Completa la seguente procedura per ottenere informazioni sui log:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Esegui il comando *status*.

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Ad esempio,
    
    ```
    $ ibmcloud cf logging status
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}


## Ottenimento delle informazioni su un tipo di log per un periodo di tempo
{: #viewing_logs_by_log_type1}

Per ottenere le informazioni su un tipo di log per un periodo di tempo, utilizza il comando `cf logging status` con le opzioni **-t** per specificare il tipo di log, **-s** per configurare la data di inizio e **-e** per la data di fine. Ad esempio,

* `cf logging status -t syslog` fornisce le informazioni sui log del tipo *syslog* per le ultime 2 settimane.
* `cf logging status -s 2017-05-03 -t syslog` fornisce le informazioni sui log del tipo *syslog* dal 3 maggio 2017 fino alla data corrente.
* `cf logging status -s 2017-05-03 -e 2017-05-08 -t syslog` fornisce le informazioni sui log del tipo *syslog* dal 3 al 8 maggio 2017. 

Completa la seguente procedura per ottenere informazioni su un tipo di log per un periodo di tempo:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Esegui il comando *status*.

    ```
    ibmcloud cf logging status -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    dove
    
    * *-s* viene utilizzata per configurare la data di inizio in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-e* viene utilizzata per configurare la data di fine in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-t* viene utilizzata per configurare il tipo di log.
    
    Puoi specificare più tipi di log sperando ogni tipo con una virgola, ad esempio, **log_type_1,log_type_2,log_type_3**. 
    
    Ad esempio,
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}



## Ottenimento delle informazioni sull'account dei log
{: #viewing_logs_account1}

Per ottenere le informazioni sui log per un periodo di tempo in un account {{site.data.keyword.Bluemix_notm}}, utilizza il comando `cf logging status` con l'opzione **-a**. Puoi anche specificare le opzioni **-t** per il tipo di log, **-s** per configurare la data di inizio e **-e** per la data di fine. 

Completa la seguente procedura per ottenere informazioni sull'account relative ai log:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Esegui il comando *status*.

    ```
    ibmcloud cf logging status -a -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    dove
    
    * *-a* viene utilizzata per specificare le informazioni al livello dell'account
    * *-s* viene utilizzata per configurare la data di inizio in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-e* viene utilizzata per configurare la data di fine in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-t* viene utilizzata per configurare il tipo di log.
    

    Puoi specificare più tipi di log sperando ogni tipo con una virgola, ad esempio, **log_type_1,log_type_2,log_type_3**. 
 
    Ad esempio,
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log -a
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}














