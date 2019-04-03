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


# Antworten auf häufig gestellte Fragen zur Verwendung der IBM Cloud-Befehlszeilenschnittstelle
{: #cli_qa}

Im Folgenden finden Sie Antworten auf häufig gestellte Fragen zur Verwendung der {{site.data.keyword.Bluemix}}-Befehlszeilenschnittstelle mit dem {{site.data.keyword.loganalysisshort}}-Service. 
{:shortdesc}

* [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an? ](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)
* [Wie installiere ich die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle](/docs/services/CloudLogAnalysis/qa/cli_qa.html#install_bmx_cli)
* [Wie rufe ich die GUID eines Kontos ab?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)
* [Wie rufe ich die GUID einer Organisation ab?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#org_guid)
* [Wie rufe ich die GUID eines Bereichs ab?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid)

## Wie melde ich mich bei IBM Cloud an? 
{: #login}

Führen Sie den folgenden Befehl aus, um sich bei einer Region in {{site.data.keyword.Bluemix_notm}} anzumelden, in der der {{site.data.keyword.loganalysisshort}}-Service verfügbar ist:

```
ibmcloud login -a Endpunkt
```
{: codeblock}
	
Dabei ist *Endpunkt* die URL für die Anmeldung bei {{site.data.keyword.Bluemix_notm}}. Diese URL ist für jede Region anders.
	
<table>
    <caption>Liste der Endpunkte für den Zugriff auf {{site.data.keyword.Bluemix_notm}}</caption>
	<tr>
	  <th>Region</th>
	  <th>URL</th>
	</tr>
	<tr>
	  <td>Deutschland</td>
	  <td>api.eu-de.bluemix.net</td>
	</tr>
	<tr>
	  <td>Sydney</td>
	  <td>api.au-syd.bluemix.net</td>
	</tr>
	<tr>
	  <td>USA (Süden)</td>
	  <td>api.ng.bluemix.net</td>
	</tr>
	<tr>
	  <td>Vereinigtes Königreich</td>
	  <td>api.eu-gb.bluemix.net</td>
	</tr>
</table>

Führen Sie zum Beispiel den folgenden Befehl aus, um sich an der Region 'USA (Süden)' anzumelden:
	
```
ibmcloud login -a https://api.ng.bluemix.net
```
{: codeblock}

Gehen Sie gemäß den Anweisungen vor. 

Sie können auch eine Organisation und einen Bereich festlegen. Führen Sie den folgenden Befehl aus:

```
ibmcloud target -o Organisationsname -s Bereichsname
```
{: codeblock}

Dabei gilt:

* 'Organisationsname' ist der Name der Organisation.
* 'Bereichsname' ist der Name des Bereichs.

	
	
## Wie installiere ich die IBM Cloud-Befehlszeilenschnittstelle?
{: #install_bmx_cli}

Siehe [{{site.data.keyword.Bluemix}}-Befehlszeilenschnittstelle herunterladen und installieren](/docs/cli/index.html#overview).



## Wie rufe ich die GUID eines Kontos ab?
{: #account_guid}
	
Führen Sie die folgenden Schritte aus, um die GUID eines Kontos abzurufen:
	
1. Melden sich bei einer Region in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Führen Sie den Befehl `ibmcloud iam accounts` aus, um die GUID eines Kontos abzurufen.

    ```
	ibmcloud iam accounts
	```
	{: codeblock} 
	
	Um beispielsweise alle Konten mit den entsprechenden GUIDs für Benutzer xxx@yyy.com abzurufen, führen Sie den folgenden Befehl aus:
	
	```
	ibmcloud iam accounts
	Retrieving all accounts of xxx@yyy.com...
    OK
    Account GUID                       Name                               Type    State    Owner User ID   
    12345123451234512345123451234512   A Account                          TRIAL   ACTIVE   xxx@yyy.com   
    23456234562345622456234561234561   B Account                          TRIAL   ACTIVE   zzz@yyy.com   
	```
	{: screen}

	
## Wie rufe ich die GUID einer Organisation ab?
{: #org_guid}

Führen Sie die folgenden Schritte aus, um die GUID einer Organisation abzurufen:
	
1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Führen Sie den Befehl `ibmcloud iam org` aus, um die GUID der Organisation abzurufen. 

    ```
    ibmcloud iam org NAME --guid
    ```
    {: codeblock}
	
    Dabei ist NAME der Name einer {{site.data.keyword.Bluemix_notm}}-Organisation.        
		
		
		
## Wie rufe ich die GUID eines Bereichs ab?
{: #space_guid2}
	
Führen Sie die folgenden Schritte aus, um die GUID eines Bereichs abzurufen:
	
1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Führen Sie den Befehl `ibmcloud iam space` aus, um die GUID des Bereichs abzurufen. 

    ```
    ibmcloud iam space NAME --guid
    ```
    {: codeblock}
	
    Dabei ist NAME der Name eines {{site.data.keyword.Bluemix_notm}}-Bereichs. 
	
    Um beispielsweise die GUID für den Bereich *dev* abzurufen, führen Sie den folgenden Befehl aus:
	
    ```
    ibmcloud iam space dev --guid
    e03afff1-3456-4af6-1234-59treg1b0abc
    ```
    {: screen}




		
		
