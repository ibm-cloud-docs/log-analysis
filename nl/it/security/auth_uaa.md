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


# Ottenimento del token UAA
{: #auth_uaa}

Per gestire i log disponibili in un dominio dello spazio tramite l'API {{site.data.keyword.loganalysisshort}}, devi utilizzare un token di autenticazione.
{:shortdesc}

		
## Ottenimento del token UAA
{: #uaa_cli}


Per ottenere il token di autorizzazione, completa la seguente procedura:

1. Installa la CLI {{site.data.keyword.Bluemix_notm}}.

   Per ulteriori informazioni, vedi [Scarica e installa la CLI {{site.data.keyword.Bluemix}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Se la CLI è installata, continua con il passo successivo.
    
2. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Esegui il comando `ibmcloud iam oauth-token` per ottenere il token UAA {{site.data.keyword.Bluemix_notm}}.

    ```
	ibmcloud iam oauth-token
	```
	{: codeblock}
	
	L'output restituisce il token UAA che devi usare per autenticare il tuo ID utente in tale spazio e organizzazione.
	

**Nota:** quando usi il token, rimuovi *Bearer* dal valore del token che passi in una chiamata API.
