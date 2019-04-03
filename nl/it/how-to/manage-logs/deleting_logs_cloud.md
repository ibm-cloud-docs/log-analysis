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
{: #deleting_logs}

Utilizza il comando [ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) per eliminare i log da Raccolta dei log. 
{:shortdesc}

* Puoi eliminare i log entro uno specifico intervallo di tempo.
* Puoi eliminare i log in base al tipo. Nota: ciascun file di log ha solo un tipo di voci di log.
* Puoi eliminare i log per uno spazio, per un'organizzazione oppure nel dominio dell'account.


## Eliminazione di tutti i log per uno specifico periodo di tempo
{: #time_range}

Completa la seguente procedura per eliminare tutti i log archiviati in un dominio di spazio per uno specifico periodo di tempo:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Esegui questo comando per visualizzare i log disponibili in Raccolta dei log.

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Ad esempio,
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-abcd-4193-aere-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. Elimina i log archiviati in uno specifico giorno.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	dove
	
	* *-s* imposta la data di inizio in Coordinated Universal Time (UTC): AAAA-MM-GG, ad esempio, 2006-01-02.
    * *-e* imposta la data di fine in Coordinated Universal Time (UTC): AAAA-MM-GG
    	
	Ad esempio, per eliminare i log per il 25 maggio 2017, esegui questo comando:
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## Eliminazione dei log in base al tipo di log per uno specifico periodo di tempo 
{: #log_type}

Completa la seguente procedura per eliminare i log in base al tipo di log archiviati in un dominio dello spazio per uno specifico periodo di tempo:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Esegui questo comando per visualizzare i log disponibili in Raccolta dei log.

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Ad esempio,
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. Elimina i log archiviati in uno specifico giorno.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	dove
	
	* *-s* imposta la data di inizio in Coordinated Universal Time (UTC): AAAA-MM-GG, ad esempio, 2006-01-02.
    * *-e* imposta la data di fine in Coordinated Universal Time (UTC): AAAA-MM-GG
	* *-t* imposta il tipo di log.
    	
	Ad esempio, per eliminare i log di tipo linux_syslog per il 25 maggio 2017, esegui questo comando:
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## Eliminazione dei log dell'account in base al tipo di log per uno specifico periodo di tempo 
{: #time_range_acc}

Completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Ottieni l'ID account.

    Per ulteriori informazioni, vedi [Come ottengo il GUID di un account](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid).
    
3. Esegui questo comando per visualizzare i log disponibili in Raccolta dei log a livello dell'account.

    ```
    ibmcloud logging log-show  -r account -i AccountID
    ```
    {: codeblock}
    
    Ad esempio,
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    All                 default
	2017-05-25   2000       76115   All                 linux_syslog,log
    2017-05-26   195678     17639   All                 default,linux_syslog    
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}
	
4. Elimina i log archiviati in uno specifico giorno.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType -r account -i AccountID
	```
	{: codeblock}
	
	dove
	
	* *-s* imposta la data di inizio in Coordinated Universal Time (UTC): AAAA-MM-GG, ad esempio, 2006-01-02.
    * *-e* imposta la data di fine in Coordinated Universal Time (UTC): AAAA-MM-GG
	* *-t* imposta il tipo di log.
    	
	Ad esempio, per eliminare i log di tipo linux_syslog per il 25 maggio 2017 archiviati in Raccolta dei log a livello dell'account, esegui questo comando:
	
	```
	ibmcloud logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -r account -i 123456789123456789567c9c8de6dece
	```
	{: screen}
	












