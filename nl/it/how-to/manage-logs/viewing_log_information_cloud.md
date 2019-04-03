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
{: #viewing_log_status1}

Utilizza il comando [ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#status) per ottenere informazioni sui log che vengono raccolti e archiviati in Raccolta dei log. Puoi ottenere informazioni sulla dimensione, sul numero di record, sui tipi di log e sulla disponibilità o meno dei log per l'analisi in Kibana.
{:shortdesc}

## Ottenimento delle informazioni sui log per un periodo di tempo
{: #viewing_logs}

Utilizza il comando `ibmcloud logging log-show` con le opzioni **-s** per impostare il giorno di inizio e **-e** per impostare la data di fine. Ad esempio:

* `ibmcloud logging log-show` fornisce informazioni per le ultime 2 settimane.
* `ibmcloud logging log-show -s 2017-05-03` fornisce informazioni dal 3 maggio 2017 fino alla data corrente.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` fornisce informazioni dal 3 all'8 maggio 2017. 

Completa la seguente procedura per ottenere informazioni sui log archiviati in uno spazio:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Esegui il seguente comando:

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Ad esempio,
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## Ottenimento delle informazioni su un tipo di log per un periodo di tempo
{: #viewing_logs_by_log_type}

Per ottenere informazioni su un tipo di log per un periodo di tempo, utilizza il comando `ibmcloud logging log-show` con le opzioni **-t** per specificare il tipo di log, **-s** per impostare il giorno di inizio e **-e** per impostare la data di fine. Ad esempio,

* `ibmcloud logging log-show -t syslog` fornisce informazioni sui log di tipo *syslog* per le ultime 2 settimane.
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` fornisce informazioni sui log di tipo *syslog* dal 3 maggio 2017 fino alla data corrente.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` fornisce informazioni sui log di tipo *syslog* dal 3 all'8 maggio 2017. 

Completa la seguente procedura per ottenere informazioni su un tipo di log per un periodo di tempo:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Esegui il seguente comando:

    ```
    ibmcloud logging log-show -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    dove
    
    * *-s* viene utilizzata per configurare la data di inizio in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-e* viene utilizzata per configurare la data di fine in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-t* viene utilizzata per configurare il tipo di log.
    
    Puoi specificare più tipi di log sperando ogni tipo con una virgola, ad esempio, **log_type_1,log_type_2,log_type_3**. 
    
    Ad esempio,
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## Ottenimento di informazioni sui log a livello dell'account
{: #viewing_logs_account}

Per ottenere informazioni sui log disponibili a livello di account per un periodo di tempo, utilizza il comando `ibmcloud logging log-show` con l'opzione **-r account** e **-i** per impostare l'ID dell'account. Puoi anche specificare le opzioni **-t** per il tipo di log, **-s** per configurare la data di inizio e **-e** per la data di fine. 

Completa la seguente procedura per ottenere informazioni sull'account relative ai log:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
2. Ottieni l'ID account.

    Per ulteriori informazioni, vedi [Come ottengo il GUID di un account](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Esegui il seguente comando:

    ```
    ibmcloud logging log-show -r account -i AccountID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    dove
    
    * *-r account* viene utilizzata per impostare il dominio in cui vuoi ottenere informazioni sui log.
    * *-i AccountID* viene utilizzata per impostare l'ID dell'account.
    * *-s* viene utilizzata per configurare la data di inizio in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-e* viene utilizzata per configurare la data di fine in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-t* viene utilizzata per configurare il tipo di log.

    Puoi specificare più tipi di log sperando ogni tipo con una virgola, ad esempio, **log_type_1,log_type_2,log_type_3**. 
 
    Ad esempio, per visualizzare le informazioni sui log archiviati per il 17 novembre 2017 nel dominio dell'account per l'account *123456789123456789567c9c8de6dece*, esegui questo comando:
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## Ottenimento di informazioni sui log a livello dell'organizzazione
{: #viewing_logs_org}

Per ottenere informazioni sui log disponibili a livello di organizzazione per un periodo di tempo, utilizza il comando `ibmcloud logging log-show` con l'opzione **-r org** e **-i** per impostare l'ID dell'organizzazione. Puoi anche specificare le opzioni **-t** per il tipo di log, **-s** per configurare la data di inizio e **-e** per la data di fine. 

Completa la seguente procedura per ottenere informazioni sull'account relative ai log:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
2. Ottieni l'ID account.

    Per ulteriori informazioni, vedi [Come ottengo il GUID di un'organizzazione](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#org_guid).
    
3. Esegui il seguente comando:

    ```
    ibmcloud logging log-show -r org -i OrgID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    dove
    
    * *-r org* viene utilizzata per impostare il dominio in cui vuoi ottenere informazioni sui log.
    * *-i OrgID* viene utilizzata per impostare l'ID dell'organizzazione.
    * *-s* viene utilizzata per configurare la data di inizio in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-e* viene utilizzata per configurare la data di fine in UTC (Universal Coordinated Time): *YYYY-MM-DD*
    * *-t* viene utilizzata per configurare il tipo di log.
    
    Puoi specificare più tipi di log sperando ogni tipo con una virgola, ad esempio, **log_type_1,log_type_2,log_type_3**. 
 
    Ad esempio, per visualizzare le informazioni sui log archiviati per il 17 novembre 2017 a livello dell'organizzazione per l'organizzazione con ID *abcd56789123456789567c9c8de6dece*, esegui questo comando:
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








