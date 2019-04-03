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

# Passaggio ai log di un'applicazione Cloud Foundry
{: #launch_logs_cloud_ui_cf}

Nella IU {{site.data.keyword.Bluemix}} puoi visualizzare, filtrare e analizzare i log tramite la scheda Log disponibile per ciascuna applicazione Cloud Foundry o tramite la IU del servizio {{site.data.keyword.loganalysisshort}}.
{:shortdesc}

Per visualizzare i log dell'applicazione CF, tieni conto delle seguenti informazioni: 

<table>
  <caption>Informazioni sui log dell'applicazione CF in {{site.data.keyword.Bluemix_notm}}</caption>
  <tr>
    <th>Opzioni IU</th>
    <th>Informazioni</th>
  </tr>
  <tr>
    <td>Scheda Log disponibile tramite la IU dell'applicazione CF </td>
    <td>I log che sono disponibili per l'analisi includono i dati delle ultime 24 ore.</td>
  </tr>
  <tr>
    <td>Dashboard {{site.data.keyword.loganalysisshort}} (Kibana)</td>
    <td>I log che sono disponibili per l'analisi includono i dati degli ultimi 3 giorni. Puoi anche specificare un periodo personalizzato.</td>
  </tr>
</table>


## Passaggio ai log dell'applicazione CF tramite il dashboard dell'applicazione CF. 
{: #cfapp_ui}

Per visualizzare i log di distribuzione o di runtime di un'applicazione Cloud Foundry, completa la seguente procedura:

1. Dal dashboard Applicazioni, fai clic sul nome della tua applicazione Cloud Foundry. 
    
2. Dalla pagina dei dettagli dell'applicazione, fai clic su **Log**.
    
    Dalla scheda **Log**, puoi visualizzare in tempo reale i log recenti riguardanti la tua applicazione o le parti finali dei log. Inoltre, puoi filtrare i log in base al componente (tipo di log), all'ID istanza dell'applicazione e all'errore.
    
Per impostazione predefinita, i log disponibili per l'analisi dalla console {{site.data.keyword.Bluemix_notm}} includono i dati delle ultime 24 ore.


## Passaggio ai log dell'applicazione CF tramite la IU {{site.data.keyword.loganalysisshort}} 
{: #cfapp_la}

Per visualizzare i log di distribuzione o di runtime di un'applicazione Cloud Foundry, completa la seguente procedura:

1. Dal dashboard Applicazioni, fai clic sul nome della tua applicazione Cloud Foundry. 
    
2. Dalla pagina dei dettagli dell'applicazione, fai clic su **Log**.
    
3. Fai clic su **Visualizza in Kibana**.

Per impostazione predefinita, i log disponibili per l'analisi includono i dati degli ultimi 15 minuti.

**Suggerimento:** per analizzare i dati per un periodo personalizzato, consulta [Analisi log avanzata con Kibana](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#analyzing_logs_Kibana). 


