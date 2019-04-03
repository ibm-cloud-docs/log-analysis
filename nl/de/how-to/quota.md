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


# Suchkontingent und tägliche Nutzung berechnen
{: #quota}

Um das Kontingent und die aktuelle tägliche Nutzung einer Protokolldomäne für den {{site.data.keyword.loganalysisshort}}-Service abzurufen, können Sie einen cURL-Befehl ausführen. 
{:shortdesc}

## Suchkontingent und tägliche Nutzung mit der CLI berechnen
{: #quota_cli}

Führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an.

    Führen Sie zum Beispiel den folgenden Befehl aus, um sich an der Region 'USA (Süden)' anzumelden:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Führen Sie den CLI-Befehl `ibmcloud logging quota-usage-show` aus. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    Dabei gilt: 

    * Gültige RESOURCE_TYPE-Werte sind: Bereich (space), Konto (account)
    * RESOURCE_ID ist die GUID des Kontos oder Bereichs, für die Sie die Kontingentnutzung abrufen möchten.


Um beispielsweise die Kontingentnutzung eines Kontos anzuzeigen, führen Sie den folgenden Befehl aus:

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotment   Current Usage
524288000         0   
```
{: screen}

Um die Kontingentnutzung für einen Bereich anzuzeigen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotment   Current Usage
524288000         6774014   
```
{: screen}


## Suchkontingentverlauf mit der CLI abrufen
{: #quota_history_cli}


Führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an.

    Führen Sie zum Beispiel den folgenden Befehl aus, um sich an der Region 'USA (Süden)' anzumelden:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Führen Sie den CLI-Befehl `ibmcloud logging quota-usage-show` mit dem Parameter `-s` aus. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    Dabei gilt: 

    * Gültige RESOURCE_TYPE-Werte sind: Bereich (space), Konto (account)
    * RESOURCE_ID ist die GUID des Kontos oder Bereichs, für die Sie die Kontingentnutzung abrufen möchten.

Beispiel:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotment   Usage
2018.02.28   524288000   80405926
2018.03.06   524288000   18955540
2018.03.05   524288000   47262944
2018.03.08   524288000   18311338
2018.03.01   524288000   82416831
2018.03.03   524288000   75045462
2018.03.07   524288000   17386278
2018.03.02   524288000   104316444
2018.03.04   524288000   73125223   
```
{: screen}



## Suchkontingent und tägliche Nutzung eines Kontos mit der API berechnen
{: #account}

Führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Rufen Sie die ID des Kontos ab. Führen Sie den folgenden Befehl aus:

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	Es wird eine Liste von Konten mit den jeweiligen GUIDs angezeigt.
	
	Exportieren Sie die Konto-ID in eine Shellvariable. Beispiel:
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. Rufen Sie das UAA-Token ab. 

    Weitere Informationen finden Sie unter [UAA-Token abrufen](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exportieren Sie das UAA-Token in eine Shellvariable. `Bearer` darf nicht mit eingeschlossen werden. Beispiel:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Rufen Sie das Kontingent und die aktuelle Nutzung der Domäne ab. Führen Sie den folgenden Befehl aus:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	Dabei ist *ENDPOINT* für jede Region anders. Eine Liste der Endpunkte pro Region finden Sie unter [Protokollierungsendpunkte](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).
	
	Führen Sie beispielsweise den cURL-Befehl aus, um das Kontingent für das Konto in der Region 'USA (Süden)' abzurufen:
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	Das Ergebnis enthält die Informationen zum täglichen Kontingent und der täglichen Nutzung.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}

	
## Suchkontingent und tägliche Nutzung eines Bereichs mit der API berechnen
{: #space1}

Führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Rufen Sie die ID des Bereichs ab.

    Weitere Informationen finden Sie unter [Wie rufe ich die GUID eines Bereichs ab?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid).
	
	Exportieren Sie die Bereichs-ID in eine Shellvariable. Beispiel:
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. Rufen Sie das UAA-Token ab. 

    Weitere Informationen finden Sie unter [UAA-Token abrufen](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exportieren Sie das UAA-Token in eine Shellvariable. `Bearer` darf nicht mit eingeschlossen werden. Beispiel:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Rufen Sie das Kontingent und die aktuelle Nutzung der Domäne ab. Führen Sie den folgenden Befehl aus:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	Dabei ist *ENDPOINT* für jede Region anders. Eine Liste der Endpunkte pro Region finden Sie unter [Protokollierungsendpunkte](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).

    Führen Sie beispielsweise den folgenden cURL-Befehl aus, um das Kontingent und die Nutzung für eine Bereichsdomäne in der Region 'USA (Süden)' abzurufen:
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	Das Ergebnis enthält die Informationen zum täglichen Kontingent und der täglichen Nutzung.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}



