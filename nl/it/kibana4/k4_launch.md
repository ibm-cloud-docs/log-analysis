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
{: #k4_launch}

Puoi avviare Kibana dalla IU {{site.data.keyword.Bluemix}} o direttamente dal browser web.
{:shortdesc}

Avvia Kibana da {{site.data.keyword.Bluemix_notm}} per visualizzare e analizzare i dati nel contesto della risorsa da cui avvii Kibana. Ad esempio, puoi eseguire l'avvio ai log della tua specifica applicazione CF in Kibana, nel contesto di quella specifica applicazione.

La seguente tabella elenca le risorse e il metodo di navigazione supportato per avviare Kibana:

<table>
<caption>Tabella 1. Elenco di risorse e metodi di navigazione supportati. </caption>
  <tr>
    <th>Risorsa</th>
    <th>Passaggio al dashboard Kibana dal dashboard Bluemix</th>
    <th>Passaggio al dashboard Kibana da un browser web</th>
  <tr>
  <tr>
    <td>Applicazione CF</td>
    <td>Sì</td>
    <td>Sì</td>
  <tr>  
  <tr>
    <td>Contenitore distribuito in un cluster Kubernetes</td>
    <td>Sì</td>
    <td>Sì</td>
  <tr>  
</table>

Per ulteriori informazioni sulle applicazioni Kibana, vedi la [ ![Icona link esterno](../../../icons/launch-glyph.svg "Icona link esterno")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}.
    

##  Passaggio al dashboard Kibana dal dashboard Bluemix
{: #launch_Kibana_from_bluemix}

La query che viene utilizzata per filtrare i dati visualizzati in Kibana richiama le voci di log per il contenitore o l'applicazione CF {{site.data.keyword.Bluemix_notm}} da cui avvii Kibana.

Per visualizzare i log di un'applicazione Cloud Foundry o di un contenitore Docker in Kibana, completa la seguente procedura:

1. Accedi a {{site.data.keyword.Bluemix_notm}} e fai clic sul contenitore o sul nome dell'applicazione dal dashboard {{site.data.keyword.Bluemix_notm}}. 
    
2. Apri la scheda di log nella IU {{site.data.keyword.Bluemix_notm}}.

    * Per le applicazioni CF, fai clic su **Log** nella barra di navigazione. 
    * Per i contenitori distribuiti nell'infrastruttura gestita da {{site.data.keyword.Bluemix_notm}}, seleziona **Monitoraggio e log** nella barra di navigazione e quindi fai clic sulla scheda **Registrazione**. 
    
        Viene aperta la scheda dei log.  

3. Fai clic su **Vista avanzata**. Viene aperto il dashboard Kibana.

    Per impostazione predefinita, la pagina **Rileva** viene caricata con il modello di indice predefinito selezionato al momento dell'impostazione del filtro negli ultimi 30 secondi. La query di ricerca è impostata per corrispondere a tutte le voci del tuo contenitore Docker o della tua applicazione CF.

    Se la pagina Rileva non mostra alcuna voce di log, modifica il selezionatore di tempo. 


##  Passaggio al dashboard Kibana da un browser web
{: #launch_Kibana_from_browser1}

La query che viene utilizzata per filtrare i dati visualizzati in Kibana richiama le voci di log per uno spazio nell'organizzazione {{site.data.keyword.Bluemix_notm}}. Le informazioni di log visualizzate da Kibana includono i record per
tutte le risorse che vengono distribuite all'interno dello spazio dell'organizzazione {{site.data.keyword.Bluemix_notm}} a cui sei collegato.

Completa la seguente procedura per avviare Kibana da un browser:

1. Avvia l'interfaccia utente Kibana.
    
    Ad esempio, 
      
        <table>
          <caption>Tabella 1. URL per avviare Kibana  </caption>
           <tr>
            <th>Regione</th>
            <th>URL</th>
          </tr>
          <tr>
            <td>Stati Uniti Sud</td>
            <td>https://logging.ng.bluemix.net/ </td>
          </tr>
          <tr>
            <td>Regno Unito</td>
            <td>https://logging.eu-gb.bluemix.net/ </td>
          </tr>
        </table>

    Se la pagina Rileva non mostra alcuna voce di log, modifica il selezionatore di tempo. 

