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


# Protokollierungstoken abrufen
{: #logging_token}

Rufen Sie ein Protokollierungstoken ab, um Protokolle an den {{site.data.keyword.loganalysisshort}}-Service zu senden. 
{:shortdesc}


## Protokollierungstoken zum Senden von Protokollen an einen Bereich über die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle abrufen 
{: #logging_token_la_cloud_cli}

Führen Sie die folgenden Schritte aus, um das Protokollierungstoken abzurufen, mit dem Sie Protokolle an den {{site.data.keyword.loganalysisshort}}-Service senden können:

1. Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle.

   Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle herunterladen und installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview). 
   
   Fahren Sie mit dem nächsten Schritt fort, wenn die Befehlszeilenschnittstelle bereits installiert ist.
    
2. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Führen Sie den folgenden Befehl aus:

    ```
	ibmcloud logging token-get
	```
	{: codeblock}

Die Ausgabe gibt das Protokollierungstoken zurück.


## Protokollierungstoken zum Senden von Protokollen an einen Bereich über die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle abrufen 
{: #logging_token_cloud_cli}

Führen Sie die folgenden Schritte aus, um das Protokollierungstoken abzurufen, mit dem Sie Protokolle an den {{site.data.keyword.loganalysisshort}}-Service senden können:

1. Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle.

   Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle herunterladen und installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview). 
   
   Fahren Sie mit dem nächsten Schritt fort, wenn die Befehlszeilenschnittstelle bereits installiert ist.
    
2. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Erstellen Sie einen Serviceschlüssel in dem Bereich, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Führen Sie die folgenden Befehle aus:

    Listen Sie die Services auf, um den Namen der {{site.data.keyword.loganalysisshort}}-Instanz im Bereich abzurufen:
	
    ```
	ibmcloud service list
	```
	{: codeblock}
	
	Beispiel:
	
	```
	ibmcloud service list
    Invoking 'cf services'...

    Getting services in org lopezdsr_org / space dev as xxx@yyyy...
    OK

    name              service          plan       bound apps   last operation
    Log Analysis-vg   ibmloganalysis   standard                create succeeded
    ```
	{: screen}
	
	Erstellen Sie einen Schlüssel. Verwenden Sie den Wert **name** als Servicenamen und geben Sie den Namen Ihres Schlüssels ein.
	
	```
	ibmcloud service key-create servicename KeyName 
	```
	{: codeblock}
	
	Beispiel:
	
	```
	ibmcloud service key-create "Log Analysis-vg" mykey2
    Invoking 'cf create-service-key Log Analysis-vg mykey2'...

    Creating service key mykey2 for service instance Log Analysis-vg as xxx@yyyy...
    OK
    ```
	{: screen}
	
4. Rufen Sie das Protokollierungstoken ab. Führen Sie den folgenden Befehl aus:
	
	```
	ibmcloud service key-show name Keyname
	```
	{: codeblock}
	
	Beispiel: 
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" 
    Invoking 'cf service-key Log Analysis-vg mykey2'...

    Getting key mykey2 for service instance Log Analysis-vg as xxx@yyyy...

    {
     "LOG_INGESTION_MTLJ_URL": "https://ingest-eu-fra.logging.bluemix.net:9091",
     "logging_token": "sdtghyrtfde4",
     "space_id": "12345678-avfg-erft-b1f2-2efrtgcb1744"
    }
    ```
	{: screen}
	
	Führen Sie zum Abrufen des Protokollierungstokens den folgenden Befehl aus:
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" | tail -n +4 | jq -r .logging_token
    sdtghyrtfde4
	```
	{: screen}


	
## Protokollierungstoken zum Senden von Protokollen an einen Bereich über die Log Analysis-API abrufen
{: #logging_token_api}


Führen Sie die folgenden Schritte aus, um das Protokollierungstoken abzurufen, mit dem Sie Protokolle an den {{site.data.keyword.loganalysisshort}}-Service senden können:

1. Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle.

   Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle herunterladen und installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview). 
   
   Fahren Sie mit dem nächsten Schritt fort, wenn die Befehlszeilenschnittstelle bereits installiert ist.
    
2. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Rufen Sie das [UAA-Token](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#uaa_cli) ab.

    Führen Sie zum Abrufen des UAA-Tokens beispielsweise den Befehl `ibmcloud cf oauth-token` aus.

    ```
	ibmcloud cf oauth-token
	```
	{: codeblock}
	
	Die Ausgabe enthält das UAA-Token, das Sie für die Authentifizierung Ihrer Benutzer-ID in diesem Bereich und dieser Organisation benötigen.

4. Rufen Sie die GUID für den Bereich ab.

   Weitere Informationen finden Sie unter [Wie rufe ich die GUID eines Bereichs ab?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#space_guid2).  
	
5. Exportieren Sie die folgenden Variablen: TOKEN und SPACEID.

    * *TOKEN* ist das OAuth-Token aus dem vorherigen Schritt mit Ausschluss von 'Bearer'.
	
	* *SPACEID* ist die GUID des Bereichs aus dem vorherigen Schritt. 
		
	Beispiel:
	
	```
	export TOKEN="eyJhbGciOiJI....cGFzc3dvcmQiLCJjZiIsInVhYSIsIm9wZW5pZCJdfQ.JaoaVudG4jqjeXz6q3JQL_SJJfoIFvY8m-rGlxryWS8"
	export SPACEID="667fb895-abcd-defg-aaaa-cf4587341095"
	```
	{: screen}
	
6. Rufen Sie das Protokollierungstoken ab. Führen Sie den folgenden Befehl aus:
 
    ```
	curl -k -X GET  --header "X-Auth-Token: ${TOKEN}"  --header "X-Auth-Project-Id: s-${SPACEID}"  LOGGING_ENDPOINT/token
    ```
    {: codeblock}	
	
	Dabei gilt:
	* SPACEID ist die GUID des Bereichs, in dem der Service ausgeführt wird.
	* TOKEN ist das UAA-Token aus dem vorherigen Schritt ohne das Präfix 'bearer.
	* LOGGING_ENDPOINT ist der {{site.data.keyword.loganalysisshort}}-Endpunkt für die {{site.data.keyword.Bluemix_notm}}-Region, in der sich die Organisation und der Bereich befinden. LOGGING_ENDPOINT ist für jede Region anders. Weitere Informationen zu den URLs für die verschiedenen Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#endpoints).
	
    Der Befehl gibt das Protokollierungstoken zurück, das Sie verwenden müssen, um Protokolle an diesen Bereich senden zu können.
	
