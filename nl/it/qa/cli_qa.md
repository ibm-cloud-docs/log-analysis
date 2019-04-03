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


# Domande frequenti e risposte relative all'utilizzo della CLI IBM Cloud
{: #cli_qa}

Sono qui di seguito riportate le risposte alle domande comuni sull'utilizzo della CLI {{site.data.keyword.Bluemix}} con il servizio {{site.data.keyword.loganalysisshort}}. 
{:shortdesc}

* [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)
* [Come installo la CLI {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#install_bmx_cli)
* [Come ottengo il GUID di un account](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)
* [Come ottengo il GUID di un'organizzazione](/docs/services/CloudLogAnalysis/qa/cli_qa.html#org_guid)
* [Come ottengo il GUID di uno spazio](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid)

## Come accedo a IBM Cloud?
{: #login}

Esegui questo comando per accedere a una regione in {{site.data.keyword.Bluemix_notm}} in cui è disponibile il servizio {{site.data.keyword.loganalysisshort}}.

```
ibmcloud login -a Endpoint
```
{: codeblock}
	
Dove *Endpoint* è l'URL per eseguire l'accesso a {{site.data.keyword.Bluemix_notm}}. Questo URL è differente per ogni regione.
	
<table>
    <caption>Elenco di endpoint per accedere a {{site.data.keyword.Bluemix_notm}}</caption>
	<tr>
	  <th>Regione</th>
	  <th>URL</th>
	</tr>
	<tr>
	  <td>Germania</td>
	  <td>api.eu-de.bluemix.net</td>
	</tr>
	<tr>
	  <td>Sydney</td>
	  <td>api.au-syd.bluemix.net</td>
	</tr>
	<tr>
	  <td>Stati Uniti Sud</td>
	  <td>api.ng.bluemix.net</td>
	</tr>
	<tr>
	  <td>Regno Unito</td>
	  <td>api.eu-gb.bluemix.net</td>
	</tr>
</table>

Ad esempio, per accedere alla regione Stati Uniti Sud, esegui questo comando:
	
```
ibmcloud login -a https://api.ng.bluemix.net
```
{: codeblock}

Attieniti alle istruzioni. 

Puoi anche configurare un'organizzazione e uno spazio. Esegui il seguente comando:

```
ibmcloud target -o OrgName -s SpaceName
```
{: codeblock}

dove

* OrgName è il nome dell'organizzazione.
* SpaceName è il nome dello spazio.

	
	
## Come installo la CLI IBM Cloud?
{: #install_bmx_cli}

Vedi [Scarica e installa la CLI {{site.data.keyword.Bluemix}}](/docs/cli/index.html#overview).



## Come ottengo il GUID di un account
{: #account_guid}
	
Per ottenere il GUID di un account, completa la seguente procedura:
	
1. Accedi a una regione in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Esegui il comando `ibmcloud iam accounts` per ottenere il GUID di un account.

    ```
	ibmcloud iam accounts
	```
	{: codeblock} 
	
	Ad esempio, per richiamare tutti gli account con i loro GUID corrispondenti per l'utente xxx@yyy.com, esegui il comando:
	
	```
	ibmcloud iam accounts
	Retrieving all accounts of xxx@yyy.com...
    OK
    Account GUID                       Name                               Type    State    Owner User ID   
    12345123451234512345123451234512   A Account                          TRIAL   ACTIVE   xxx@yyy.com   
    23456234562345622456234561234561   B Account                          TRIAL   ACTIVE   zzz@yyy.com   
	```
	{: screen}

	
## Come ottengo il GUID di un'organizzazione?
{: #org_guid}

Completa la seguente procedura per ottenere il GUID di un organizzazione:
	
1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Esegui il comando `ibmcloud iam org` per ottenere il GUID dell'organizzazione. 

    ```
    ibmcloud iam org NAME --guid
    ```
    {: codeblock}
	
    dove NAME è il nome dell'organizzazione {{site.data.keyword.Bluemix_notm}}.        
		
		
		
## Come ottengo il GUID di uno spazio?
{: #space_guid2}
	
Completa la seguente procedura per ottenere il GUID di uno spazio:
	
1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Esegui il comando `ibmcloud iam space` per ottenere il GUID dello spazio. 

    ```
    ibmcloud iam space NAME --guid
    ```
    {: codeblock}
	
    dove NAME è il nome di uno spazio {{site.data.keyword.Bluemix_notm}}. 
	
    Ad esempio, per ottenere il GUID per lo spazio *dev*, immetti il seguente comando:
	
    ```
    ibmcloud iam space dev --guid
    e03afff1-3456-4af6-1234-59treg1b0abc
    ```
    {: screen}




		
		
