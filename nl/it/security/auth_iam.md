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


# Ottenimento del token IAM
{: #auth_iam1}

Per gestire i log disponibili nel dominio di account utilizzando la API {{site.data.keyword.loganalysisshort}}, devi utilizzare un token di autenticazione. Usa la CLI {{{site.data.keyword.Bluemix_notm}} per ottenere il token IAM. Il token ha un tempo di scadenza. 
{:shortdesc}


## Ottenimento del token IAM
{: #iam_token_cli}

Per ottenere il token di autorizzazione utilizzando la CLI {{site.data.keyword.Bluemix_notm}}, completa la seguente procedura da un terminale:

1. Installa la CLI {{site.data.keyword.Bluemix_notm}}.

   Per ulteriori informazioni, vedi [Scarica e installa la CLI {{site.data.keyword.Bluemix}}](/docs/cli/index.html#overview).
   
   Se la CLI è installata, continua con il passo successivo.
    
2. Accedi a una regione in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
3. Esegui il comando `ibmcloud iam oauth-tokens` per ottenere il token IAM.

    ```
	ibmcloud iam oauth-tokens
	```
	{: codeblock}
	
	L'output restituisce il token IAM che devi usare per autenticare il tuo ID utente in tale spazio e organizzazione. Puoi esportare il token IAM in una variabile shell quale `$iam_token`.



**Nota:** quando usi il token, rimuovi *Bearer* dal valore del token che passi in una chiamata API.

