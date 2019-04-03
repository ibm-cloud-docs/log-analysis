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


# Passaggio al dashboard Kibana
{: #launch}

Puoi avviare Kibana dal servizio {{site.data.keyword.loganalysisshort}}, dalla IU {{site.data.keyword.Bluemix}} o direttamente da un browser web.
{:shortdesc}

Per le applicazioni CF e i contenitori Docker, puoi avviare Kibana dalla IU {{site.data.keyword.Bluemix_notm}} per visualizzare e analizzare i dati nel contesto della risorsa da cui avvii Kibana. Ad esempio, puoi eseguire l'avvio ai log della tua specifica applicazione CF in Kibana, nel contesto di quella specifica applicazione.
    
Per tutte le risorse cloud come un contenitore Docker distribuito a un'infrastruttura Kubernetes, puoi avviare Kibana da un link browser diretto o dal dashboard del servizio {{site.data.keyword.loganalysisshort}} per visualizzare i dati di log aggregati dai servizi all'interno di uno spazio fornito. La query che viene utilizzata per filtrare i dati visualizzati nel dashboard richiama le voci di log per uno spazio nell'organizzazione. Le informazioni di log visualizzate da Kibana includono i record per tutte le risorse che vengono distribuite all'interno dello spazio dell'organizzazione a cui sei collegato. 

La seguente tabella elenca alcune risorse cloud e i metodi di navigazione supportati per avviare Kibana:

<table>
<caption>Tabella 1. Elenco di risorse e metodi di navigazione supportati. </caption>
  <tr>
    <th>Risorsa</th>
	<th>Passa al dashboard Kibana dal dashboard del servizio {{site.data.keyword.loganalysisshort}}</th>
    <th>Passa al dashboard Kibana dal dashboard Bluemix</th>
    <th>Passa al dashboard Kibana da un browser web</th>
  </tr>
  <tr>
    <td>Applicazione CF</td>
	<td>Sì</td>
    <td>Sì</td>
    <td>Sì</td>
  </tr>  
  <tr>
    <td>Contenitore distribuito in un cluster Kubernetes</td>
	<td>Sì</td>
    <td>Sì</td>
    <td>Sì</td>
  </tr>  
  <tr>
    <td>Contenitore distribuito in un'infrastruttura gestita da {{site.data.keyword.Bluemix_notm}} (obsoleto)</td>
	<td>Sì</td>
    <td>Sì</td>
    <td>Sì</td>
  </tr>  
</table>

Per ulteriori informazioni sulle applicazioni Kibana, vedi la [ ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.
    

##  Passaggio a Kibana dal dashboard del servizio Analisi di log
{: #launch_Kibana_from_log_analysis}

La query che viene utilizzata per filtrare i dati visualizzati in Kibana richiama le voci di log per tale spazio nell'organizzazione. 
	
Le informazioni di log visualizzate da Kibana includono i record per tutte le risorse che vengono distribuite all'interno dello spazio dell'organizzazione a cui sei collegato.

Completa la seguente procedura per avviare Kibana dal dashboard del servizio {{site.data.keyword.loganalysisshort}}:

1. Accedi a {{site.data.keyword.Bluemix_notm}} e fai clic sul servizio {{site.data.keyword.loganalysisshort}} dal dashboard {{site.data.keyword.Bluemix_notm}}. 
    
2. Seleziona la scheda **Gestito** nella IU {{site.data.keyword.Bluemix_notm}}.

3. Fai clic su **AVVIA**. Viene aperto il dashboard Kibana.

Per impostazione predefinita, la pagina **Rileva** viene caricata con il modello di indice predefinito selezionato al momento dell'impostazione del filtro negli ultimi 15 minuti. 

Se la pagina Rileva non mostra alcuna voce di log, modifica il selezionatore di tempo. Per maggiori informazioni, vedi [Configurazione di un filtro temporale](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	
	
##  Passaggio a Kibana da un browser web.
{: #launch_Kibana_from_browser}

La query che viene utilizzata per filtrare i dati visualizzati in Kibana richiama le voci di log per tale spazio nell'organizzazione. 
	
Le informazioni di log visualizzate da Kibana includono i record per tutte le risorse che vengono distribuite all'interno dello spazio dell'organizzazione a cui sei collegato.

Completa la seguente procedura per avviare Kibana da un browser:

1. Apri un browser Web e avvia Kibana. Accedi quindi all'interfaccia utente Kibana.

    Per visualizzare l'elenco di URL per ogni regione, vedi [URL per avviare Kibana](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana).
    
    Viene aperta la pagina Rileva in Kibana.
	
2. Selezionare il modello di indice per lo spazio da dove vuoi visualizzare e analizzare i dati di log.

    1. Fai clic su **default-index**.
	
	2. Seleziona il modello di indice per lo spazio. Il formato del modello di indice è il seguente:
	
	    ```
	    [logstash-Space_ID-]YYYY.MM.DD 
	    ```
        {: screen}
	
	    dove *Space_ID* è il GUID dello spazio in cui desideri visualizzare e analizzare i dati di log. 
	
Se la pagina Rileva non mostra alcuna voce di log, modifica il selezionatore di tempo. Per maggiori informazioni, vedi [Configurazione di un filtro temporale](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).


	
##  Passaggio a Kibana dal dashboard di una applicazione CF
{: #launch_Kibana_from_cf_app}

La query che viene utilizzata per filtrare i dati visualizzati in Kibana richiama le voci di log per l'applicazione CF {{site.data.keyword.Bluemix_notm}} da cui avvii Kibana.

Per visualizzare i log di un'applicazione Cloud Foundry in Kibana, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.Bluemix_notm}}.

    Il dashboard {{site.data.keyword.Bluemix_notm}} è disponibile in: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}.
    
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Fare clic sul nome dell'applicazione o sul contenitore dal dashboard {{site.data.keyword.Bluemix_notm}}. 
    
3. Apri la scheda di log nella IU {{site.data.keyword.Bluemix_notm}}.

    Per le applicazioni CF, fai clic su **Log** nella barra di navigazione. 
    Viene aperta la scheda dei log.  

4. Fai clic su **Visualizza in Kibana**. Viene aperto il dashboard Kibana.

    Per impostazione predefinita, la pagina **Rileva** viene caricata con il modello di indice predefinito selezionato al momento dell'impostazione del filtro negli ultimi 15 minuti. La query di ricerca è impostata per corrispondere a tutte le voci per l'applicazione CF.

    Se la pagina Rileva non mostra alcuna voce di log, modifica il selezionatore di tempo. Per maggiori informazioni, vedi [Configurazione di un filtro temporale](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	
	
##  Passaggio a Kibana dal dashboard di un contenitore distribuito in un cluster Kubernetes
{: #launch_Kibana_for_containers_kube}

La query che viene utilizzata per filtrare i dati visualizzati in Kibana richiama le voci di log per il cluster da cui avvii Kibana.

Per visualizzare i log di un contenitore in Kibana, completa la seguente procedura:

1. Accedi al tuo account {{site.data.keyword.Bluemix_notm}}.

    Il dashboard {{site.data.keyword.Bluemix_notm}} è disponibile in: [http://bluemix.net ![Icona di link esterno](../../../icons/launch-glyph.svg "Icona di link esterno")](http://bluemix.net){:new_window}.
    
	Dopo che hai eseguito l'accesso con il tuo ID utente e la tua password, viene aperta la IU {{site.data.keyword.Bluemix_notm}}.

2. Dal menu, seleziona **Dashboard**.

3. Nella sezione *Cluster*, seleziona il cluster.

4. Nella sezione *Panoramica*, seleziona **Visualizza log**.

    Viene aperto Kibana.




##  Passaggio a Kibana dal dashboard di un contenitore distribuito nell'infrastruttura gestita da {{site.data.keyword.Bluemix_notm}} (obsoleto)
{: #launch_Kibana_for_containers}

Questo metodo si applica solo ai contenitori distribuiti nell'infrastruttura gestita da {{site.data.keyword.Bluemix_notm}}.

La query che viene utilizzata per filtrare i dati visualizzati in Kibana richiama le voci di log per il contenitore da cui avvii Kibana.

Per visualizzare i log di un contenitore Docker in Kibana, completa la seguente procedura:

1. Accedi a {{site.data.keyword.Bluemix_notm}} e fai clic sul contenitore dal dashboard {{site.data.keyword.Bluemix_notm}}. 
    
2. Apri la scheda di log nella IU {{site.data.keyword.Bluemix_notm}}.

    Per i contenitori distribuiti nell'infrastruttura gestita da {{site.data.keyword.IBM_notm}}, seleziona **Monitoraggio e log** nella barra di navigazione e quindi fai clic sulla scheda **Registrazione**. 
    
    Viene aperta la scheda dei log.  

3. Fai clic su **Vista avanzata**. Viene aperto il dashboard Kibana.

    Per impostazione predefinita, la pagina **Rileva** viene caricata con il modello di indice predefinito selezionato al momento dell'impostazione del filtro negli ultimi 30 secondi. La query di ricerca è impostata per corrispondere a tutte le voci del contenitore Docker.

    Se la pagina Rileva non mostra alcuna voce di log, modifica il selezionatore di tempo. Per maggiori informazioni, vedi [Configurazione di un filtro temporale](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	



