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

# Eliminazione dei log
{: #deleting_logs1}

Utilizza il comando [ibmcloud cf logging delete](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#status1) per eliminare i log da Raccolta dei log. 
{:shortdesc}

* Puoi eliminare i log entro uno specifico intervallo di tempo.
* Puoi eliminare i log in base al tipo. Nota: ciascun file di log ha solo un tipo di voci di log.
* Puoi eliminare i log per uno spazio o nel dominio dell'account.


## Eliminazione dei log per uno specifico periodo di tempo
{: #fix_period}

Completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Esegui il comando *status* per visualizzare i log disponibili in Raccolta dei log.

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
	
3. Elimina i log archiviati in uno specifico giorno.

    ```
	ibmcloud cf logging delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	dove
	
	* *-s* imposta la data di inizio in Coordinated Universal Time (UTC): AAAA-MM-GG, ad esempio, 2006-01-02.
    * *-e* imposta la data di fine in Coordinated Universal Time (UTC): AAAA-MM-GG
    	
	Ad esempio, per eliminare i log per il 25 maggio 2017, esegui questo comando:
	
	```
	ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## Eliminazione dei log in base al tipo di log per uno specifico periodo di tempo 
{: #log_type1}

Completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Esegui il comando *status* per visualizzare i log disponibili in Raccolta dei log.

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
	
3. Elimina i log archiviati in uno specifico giorno.

    ```
	ibmcloud cf logging delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	dove
	
	* *-s* imposta la data di inizio in Coordinated Universal Time (UTC): AAAA-MM-GG, ad esempio, 2006-01-02.
    * *-e* imposta la data di fine in Coordinated Universal Time (UTC): AAAA-MM-GG
	* *-t* imposta il tipo di log.
    	
	Ad esempio, per eliminare i log di tipo linux_syslog per il 25 maggio 2017, esegui questo comando:
	
	```
	ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## Eliminazione dei log dell'account in base al tipo di log per uno specifico periodo di tempo 
{: #acc_log_type}

Completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Esegui il comando *status* per visualizzare i log disponibili in Raccolta dei log a livello dell'account.

    ```
    ibmcloud cf logging status  -a
    ```
    {: codeblock}
    
    Ad esempio,
    
    ```
    $ ibmcloud cf logging status -a
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}
	
3. Elimina i log archiviati in uno specifico giorno.

    ```
	ibmcloud cf logging delete -s StartDate -e EndDate -t LogType -a
	```
	{: codeblock}
	
	dove
	
	* *-s* imposta la data di inizio in Coordinated Universal Time (UTC): AAAA-MM-GG, ad esempio, 2006-01-02.
    * *-e* imposta la data di fine in Coordinated Universal Time (UTC): AAAA-MM-GG
	* *-t* imposta il tipo di log.
    	
	Ad esempio, per eliminare i log di tipo linux_syslog per il 25 maggio 2017 archiviati in Raccolta dei log a livello dell'account, esegui questo comando:
	
	```
	ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -a
	```
	{: screen}
	












