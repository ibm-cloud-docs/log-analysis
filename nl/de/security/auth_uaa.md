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


# UAA-Token abrufen
{: #auth_uaa}

Zum Verwalten der in einer Bereichsdomäne verfügbaren Protokolle über die {{site.data.keyword.loganalysisshort}}-API müssen Sie ein Authentifizierungstoken verwenden.
{:shortdesc}

		
## UAA-Token abrufen
{: #uaa_cli}


Führen Sie die folgenden Schritte aus, um das Berechtigungstoken abzurufen:

1. Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle.

   Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix}}-Befehlszeilenschnittstelle herunterladen und installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview). 
   
   Fahren Sie mit dem nächsten Schritt fort, wenn die Befehlszeilenschnittstelle bereits installiert ist.
    
2. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Um das UAA-Token für {{site.data.keyword.Bluemix_notm}} abzurufen, führen Sie den Befehl `ibmcloud iam oauth-token` aus.

    ```
	ibmcloud iam oauth-token
	```
	{: codeblock}
	
	Die Ausgabe enthält das UAA-Token, das Sie für die Authentifizierung Ihrer Benutzer-ID in diesem Bereich und dieser Organisation benötigen.
	

**Hinweis:** Wenn Sie das Token verwenden, entfernen Sie *Bearer* aus dem Wert des Tokens, den Sie in einem API-Aufruf übergeben.
