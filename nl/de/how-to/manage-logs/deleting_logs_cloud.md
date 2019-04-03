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

# Protokolle löschen
{: #deleting_logs}

Mit dem Befehl [ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) können Sie Protokolle aus 'Log Collection' löschen. 
{:shortdesc}

* Sie können Protokolle für einen bestimmten Zeitraum löschen.
* Sie können Protokolle nach Typ löschen. Beachten Sie, dass jede Protokolldatei nur über einen Typ von Protokolleintrag verfügt.
* Sie können Protokolle für einen Bereich, eine Organisation oder eine Kontodomäne löschen.


## Alle Protokolle für einen bestimmten Zeitraum löschen
{: #time_range}

Führen Sie die folgenden Schritte aus, um alle Protokolle zu löschen, die in einer Bereichsdomäne für einen bestimmten Zeitraum gespeichert sind:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Führen Sie den folgenden Befehl aus, um die in 'Log Collection' verfügbaren Protokolle anzuzeigen.

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Beispiel:
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-abcd-4193-aere-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. Löschen Sie die Protokolle, die für einen bestimmten Tag gespeichert sind.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	Dabei gilt:
	
	* *-s* legt das Startdatum in koordinierter Weltzeit (UTC) fest: JJJJ-MM-TT, z. B. 2006-01-02.
    * *-e* legt das Enddatum in koordinierter Weltzeit (UTC) fest: JJJJ-MM-TT
    	
	Führen Sie beispielsweise den folgenden Befehl aus, um die Protokolle für den 25. Mai 2017 zu löschen:
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## Protokolle nach Protokolltyp für einen bestimmten Zeitraum löschen 
{: #log_type}

Führen Sie die folgenden Schritte aus, um Protokolle nach Protokolltyp zu löschen, die in einer Bereichsdomäne für einen bestimmten Zeitraum gespeichert sind:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Führen Sie den folgenden Befehl aus, um die in 'Log Collection' verfügbaren Protokolle anzuzeigen.

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Beispiel:
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. Löschen Sie die Protokolle, die für einen bestimmten Tag gespeichert sind.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	Dabei gilt:
	
	* *-s* legt das Startdatum in koordinierter Weltzeit (UTC) fest: JJJJ-MM-TT, z. B. 2006-01-02.
    * *-e* legt das Enddatum in koordinierter Weltzeit (UTC) fest: JJJJ-MM-TT
	* Mit *-t* wird der Protokolltyp festgelegt.
    	
	Führen Sie beispielsweise den folgenden Befehl aus, um die Protokolle des Typs 'linux_syslog' für den 25. Mai 2017 zu löschen:
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## Kontoprotokolle nach Protokolltyp für einen bestimmten Zeitraum löschen 
{: #time_range_acc}

Führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Rufen Sie die Konto-ID ab.

    Weitere Informationen finden Sie unter [Wie rufe ich die GUID eines Kontos ab?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid).
    
3. Führen Sie den folgenden Befehl aus, um die in 'Log Collection' verfügbaren Protokolle auf der Kontoebene anzuzeigen.

    ```
    ibmcloud logging log-show  -r account -i AccountID
    ```
    {: codeblock}
    
    Beispiel:
    
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
	
4. Löschen Sie die Protokolle, die für einen bestimmten Tag gespeichert sind.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType -r account -i AccountID
	```
	{: codeblock}
	
	Dabei gilt:
	
	* *-s* legt das Startdatum in koordinierter Weltzeit (UTC) fest: JJJJ-MM-TT, z. B. 2006-01-02.
    * *-e* legt das Enddatum in koordinierter Weltzeit (UTC) fest: JJJJ-MM-TT
	* Mit *-t* wird der Protokolltyp festgelegt.
    	
	Führen Sie beispielsweise den folgenden Befehl aus, um die Protokolle des Typs 'linux_syslog' für den 25. Mai 2017 zu löschen, die in 'Log Collection' auf der Kontoebene gespeichert sind:
	
	```
	ibmcloud logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -r account -i 123456789123456789567c9c8de6dece
	```
	{: screen}
	












