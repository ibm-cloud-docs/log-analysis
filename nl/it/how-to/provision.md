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


# Provisioning del servizio Analisi di log
{: #provision}

Puoi eseguire il provisioning del servizio {{site.data.keyword.loganalysisshort}} dalla IU {{site.data.keyword.Bluemix}} o dalla riga di comando.
{:shortdesc}


## Provisioning dalla IU
{: #ui}

Completa la seguente procedura per eseguire il provisioning di un'istanza del servizio {{site.data.keyword.loganalysisshort}} in {{site.data.keyword.Bluemix_notm}}:

1. Accedi al tuo account {{site.data.keyword.Bluemix_notm}}.

    Il dashboard {{site.data.keyword.Bluemix_notm}} è disponibile in: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}.
    
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Fai clic su **Catalogo**. Viene aperto l'elenco dei servizi disponibili in {{site.data.keyword.Bluemix_notm}}.

3. Seleziona la categoria **Strumenti per gli sviluppatori** per filtrare l'elenco di servizi visualizzato.

4. Fai clic sul tile **Analisi di log**.

5. Seleziona un piano di servizio. Per impostazione predefinita, è impostato il piano **Lite**.

    Per ulteriori informazioni sui piani di servizio, vedi [Piani di servizio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).
	
6. Fai clic su **Crea** per eseguire il provisioning del servizio {{site.data.keyword.loganalysisshort}} nello spazio {{site.data.keyword.Bluemix_notm}} in cui hai eseguito l'accesso.
  
 

## Provisioning dalla CLI
{: #cli}

Completa la seguente procedura per eseguire il provisioning di un'istanza del servizio {{site.data.keyword.loganalysisshort}} in {{site.data.keyword.Bluemix_notm}} tramite la riga di comando:

1. [Prerequisito] Installa la CLI {{site.data.keyword.Bluemix_notm}}.

   Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
   Se la CLI è installata, continua con il passo successivo.
    
2. Accedi alla regione, all'organizzazione e allo spazio in {{site.data.keyword.Bluemix_notm}} in cui vuoi eseguire il provisioning del servizio. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
3. Esegui il comando `ibmcloud service create` per eseguire il provisioning di un'istanza.

    ```
	ibmcloud service create service_name service_plan service_instance_name
	```
	{: codeblock}
	
	Dove
	
	* service_name è il nome del servizio, ossia **ibmLogAnalysis**.
	* service_plan è il nome del piano di servizio. Per un elenco dei piani, vedi [Piani di servizio](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).
	* service_instance_name è il nome che vuoi usare per la nuova istanza del servizio che crei.

	Ad esempio, per creare un'istanza del servizio {{site.data.keyword.loganalysisshort}} con il piano Lite, esegui questo comando:
	
	```
	ibmcloud service create ibmLogAnalysis standard my_logging_svc
	```
	{: codeblock}
	
4. Verifica che il servizio venga creato correttamente. Esegui il seguente comando:

    ```	
	ibmcloud service list
	```
	{: codeblock}
	
	L'output dell'esecuzione del comando si presenta così:
	
	```
    Richiamo dei servizi nell'organizzazione MyOrg / space MySpace come xxx@yyy.com in corso...
    OK
    
    name                           service                  plan                   bound apps              last operation
    my_logging_svc                ibmLogAnalysis           standard                                        create succeeded
	```
	{: screen}

	



