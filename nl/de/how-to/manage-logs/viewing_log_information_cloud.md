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

# Protokollinformationen anzeigen
{: #viewing_log_status1}

Mit dem Befehl [ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#status) können Sie Informationen zu den Protokollen abrufen, die in 'Log Collection' erfasst und gespeichert werden. Dabei handelt es sich um Informationen zur Größe, Anzahl der Datensätze, zu den Protokolltypen und darüber, ob die Protokolle für die Analyse in Kibana verfügbar sind oder nicht.
{:shortdesc}

## Informationen zu Protokollen über einen Zeitraum abrufen
{: #viewing_logs}

Verwenden Sie den Befehl `ibmcloud logging log-show` mit der Option **-s**, um den Starttag festzulegen, oder mit der Option **-e**, um den Endtag festzulegen. Beispiel:

* `ibmcloud logging log-show` stellt Informationen für die letzten zwei Wochen bereit.
* `ibmcloud logging log-show -s 2017-05-03` stellt Informationen vom 3. Mai 2017 bis zum aktuellen Datum bereit.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` stellt Informationen für den Zeitraum vom 3. Mai 2017 bis zum 8. Mai 2017 bereit. 

Führen Sie die folgenden Schritte aus, um Informationen zu Protokollen abzurufen, die in einem Bereich gespeichert sind:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Beispiel:
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## Informationen zu einem Protokolltyp über einen Zeitraum abrufen
{: #viewing_logs_by_log_type}

Um Informationen zu einem Protokolltyp über einen bestimmten Zeitraum zu erhalten, verwenden Sie den Befehl `ibmcloud logging log-show` und legen Sie die Option **-t** für den Protokolltyp, die Option **-s** für das Startdatum und die Option **-e** für das Enddatum fest. Beispiel:

* `ibmcloud logging log-show -t syslog` stellt Informationen zu Protokollen des Typs *syslog* für die beiden letzten Wochen bereit.
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` stellt Informationen zu Protokollen des Typs *syslog* vom 3. Mai 2017 bis zum aktuellen Datum bereit.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` stellt Informationen zu Protokollen des Typs *syslog* für den Zeitraum vom 3. Mai 2017 bis zum 8. Mai 2017 bereit. 

Führen Sie die folgenden Schritte aus, um Informationen zu einem Protokolltyp über einen Zeitraum abzurufen:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging log-show -s JJJJ-MM-TT -e JJJJ-MM-TT -t *Protokolltyp*
    ```
    {: codeblock}
    
    Dabei gilt:
    
    * *-s* wird verwendet, um das Startdatum in Universal Coordinated Time (UTC) festzulegen: *JJJJ-MM-TT*
    * *-e* wird verwendet, um das Enddatum in Universal Coordinated Time (UTC) festzulegen: *JJJJ-MM-TT*
    * *-t* wird verwendet, um den Protokolltyp festzulegen.
    
    Sie können mehrere Protokolltypen angeben, indem Sie die einzelnen Typen durch Kommas trennen. Beispiel: **Protokolltyp_1,Protokolltyp_2,Protokolltyp_3**. 
    
    Beispiel:
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## Informationen zu Protokollen auf Kontoebene abrufen
{: #viewing_logs_account}

Um Informationen zu Protokollen abzurufen, die auf der Kontoebene über einen bestimmten Zeitraum verfügbar sind, verwenden Sie den Befehl `ibmcloud logging log-show` mit der Option **-r account** und der Option **-i**, um die ID des Kontos anzugeben. Sie können außerdem die Optionen **-t** für den Protokolltyp, **-s** für das Startdatum und **-e** für das Enddatum festlegen. 

Führen Sie die folgenden Schritte aus, um Kontoinformationen zu Protokollen abzurufen:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Rufen Sie die Konto-ID ab.

    Weitere Informationen finden Sie unter [Wie rufe ich die GUID eines Kontos ab?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid).
    
3. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging log-show -r account -i AccountID -s JJJJ-MM-TT -e JJJJ-MM-TT -t *Protokolltyp*
    ```
    {: codeblock}
    
    Dabei gilt:
    
    * *-r account* wird verwendet, um die Domäne festzulegen, aus der Sie Informationen zu den Protokollen abrufen möchten.
    * *-i AccountID* wird verwendet, um die ID des Kontos festzulegen.
    * *-s* wird verwendet, um das Startdatum in Universal Coordinated Time (UTC) festzulegen: *JJJJ-MM-TT*
    * *-e* wird verwendet, um das Enddatum in Universal Coordinated Time (UTC) festzulegen: *JJJJ-MM-TT*
    * *-t* wird verwendet, um den Protokolltyp festzulegen.

    Sie können mehrere Protokolltypen angeben, indem Sie die einzelnen Typen durch Kommas trennen. Beispiel: **Protokolltyp_1,Protokolltyp_2,Protokolltyp_3**. 
 
    Um beispielsweise Informationen zu Protokollen anzuzeigen, die für den 17. November 2107 in der Kontodomäne für das Konto *123456789123456789567c9c8de6dece* gespeichert wurden, führen Sie den folgenden Befehl aus:
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## Informationen zu Protokollen auf Organisationsebene abrufen
{: #viewing_logs_org}

Um Informationen zu Protokollen abzurufen, die auf der Organisationsebene über einen bestimmten Zeitraum verfügbar sind, verwenden Sie den Befehl `ibmcloud logging log-show` mit der Option **-r org** und der Option **-i**, um die ID der Organisation anzugeben. Sie können außerdem die Optionen **-t** für den Protokolltyp, **-s** für das Startdatum und **-e** für das Enddatum festlegen. 

Führen Sie die folgenden Schritte aus, um Kontoinformationen zu Protokollen abzurufen:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Rufen Sie die Konto-ID ab.

    Weitere Informationen finden Sie unter [Wie rufe ich die GUID einer Organisation ab?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#org_guid).
    
3. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging log-show -r org -i OrgID -s JJJJ-MM-TT -e JJJJ-MM-TT -t *Protokolltyp*
    ```
    {: codeblock}
    
    Dabei gilt:
    
    * *-r org* wird verwendet, um die Domäne festzulegen, aus der Sie Informationen zu den Protokollen abrufen möchten.
    * *-i OrgID* wird verwendet, um die ID der Organisation festzulegen.
    * *-s* wird verwendet, um das Startdatum in Universal Coordinated Time (UTC) festzulegen: *JJJJ-MM-TT*
    * *-e* wird verwendet, um das Enddatum in Universal Coordinated Time (UTC) festzulegen: *JJJJ-MM-TT*
    * *-t* wird verwendet, um den Protokolltyp festzulegen.
    
    Sie können mehrere Protokolltypen angeben, indem Sie die einzelnen Typen durch Kommas trennen. Beispiel: **Protokolltyp_1,Protokolltyp_2,Protokolltyp_3**. 
 
    Um beispielsweise Informationen zu Protokollen anzuzeigen, die für den 17. November 2107 in der Organisationsdomäne für die Organisation *abcd56789123456789567c9c8de6dece* gespeichert wurden, führen Sie den folgenden Befehl aus:
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








