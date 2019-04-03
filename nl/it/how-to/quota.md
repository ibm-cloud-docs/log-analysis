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


# Calcolo della quota di ricerca e dell'utilizzo giornaliero
{: #quota}

Per ottenere la quota e l'utilizzo giornaliero corrente di un dominio dei log del servizio {{site.data.keyword.loganalysisshort}}, puoi eseguire un comando cURL. 
{:shortdesc}

## Calcolo della quota di ricerca e dell'utilizzo giornaliero con la CLI
{: #quota_cli}

Completa la seguente procedura:

1. Accedi a {{site.data.keyword.Bluemix_notm}}.

    Ad esempio, per accedere alla regione Stati Uniti Sud, immetti il comando:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Esegui il comando della CLI `ibmcloud logging quota-usage-show`. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    dove 

    * I valori RESOURCE_TYPE validi sono i seguenti: space, account
    * RESOURCE_ID è il GUID dell'account o dello spazio per cui vuoi ottenere l'utilizzo della quota.


Ad esempio, per visualizzare l'utilizzo della quota di un account, immetti il seguente comando:

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage   
524288000         0   
```
{: screen}

Per visualizzare l'utilizzo della quota di uno spazio, immetti il seguente comando:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage   
524288000         6774014   
```
{: screen}


## Ottenimento della cronologia della quota di ricerca utilizzando la CLI
{: #quota_history_cli}


Completa la seguente procedura:

1. Accedi a {{site.data.keyword.Bluemix_notm}}.

    Ad esempio, per accedere alla regione Stati Uniti Sud, immetti il comando:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Esegui il comando della CLI `ibmcloud logging quota-usage-show` con il parametro `-s`. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    dove 

    * I valori RESOURCE_TYPE validi sono i seguenti: space, account
    * RESOURCE_ID è il GUID dell'account o dello spazio per cui vuoi ottenere l'utilizzo della quota.

Ad esempio,

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
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



## Calcolo della quota di ricerca e dell'utilizzo giornaliero di un account utilizzando l'API
{: #account}

Completa la seguente procedura:

1. Accedi a {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Ottieni l'ID dell'account. Esegui il seguente comando:

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	Viene visualizzato un elenco di account con i relativi GUID.
	
	Esporta l'ID account in una variabile shell. Ad esempio:
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. Ottieni il token UAA. 

    Per ulteriori informazioni, vedi [Ottenimento del token UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Esporta il token UAA in una variabile shell. Non includere `Bearer`. Ad esempio:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Ottieni la quota del dominio e l'utilizzo corrente. Esegui il seguente comando:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	dove *ENDPOINT* è diverso per ogni regione. Per un elenco di endpoint per ogni regione, vedi [Endpoint registrazione](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).
	
	Ad esempio, esegui il comando cURL per ottenere la quota per l'account nella regione Stati Uniti Sud:
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	Il risultato include le informazioni sulla quota e l'utilizzo giornalieri.
	
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

	
## Calcolo della quota di ricerca e dell'utilizzo giornaliero di uno spazio utilizzando l'API
{: #space1}

Completa la seguente procedura:

1. Accedi a {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Ottieni l'ID dello spazio.

    Per ulteriori informazioni, vedi [Come ottengo il GUID di uno spazio](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid).
	
	Esporta l'ID spazio in una variabile shell. Ad esempio:
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. Ottieni il token UAA. 

    Per ulteriori informazioni, vedi [Ottenimento del token UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Esporta il token UAA in una variabile shell. Non includere `Bearer`. Ad esempio:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Ottieni la quota del dominio e l'utilizzo corrente. Esegui il seguente comando:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	dove *ENDPOINT* è diverso per ogni regione. Per un elenco di endpoint per ogni regione, vedi [Endpoint registrazione](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).

    Ad esempio, esegui questo comando cURL per ottenere la quota e l'utilizzo di uno dominio dello spazio nella regione Stati Uniti Sud:
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	Il risultato include le informazioni sulla quota e l'utilizzo giornalieri.
	
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



