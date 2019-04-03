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


# Zum Kibana-Dashboard navigieren
{: #k4_launch}

Sie können Kibana über die {{site.data.keyword.Bluemix}}-Benutzerschnittstelle oder direkt über einen Web-Browser starten.
{:shortdesc}

Sie können Kibana über {{site.data.keyword.Bluemix_notm}} starten, um Daten im Kontext der Ressource anzuzeigen und zu analysieren, von der Sie Kibana starten. Sie können Ihre spezifischen CF-App-Protokolle in Kibana im Kontext dieser spezifischen App starten.

In der folgenden Tabelle sind die Ressourcen und die unterstützten Navigationsmethoden zum Starten von Kibana aufgeführt:

<table>
<caption>Tabelle 1. Liste der Ressourcen und unterstützten Navigationsmethoden. </caption>
  <tr>
    <th>Ressource</th>
    <th>Navigation zum Kibana-Dashboard vom Bluemix-Dashboard</th>
    <th>Navigation zum Kibana-Dashboard von einem Web-Browser</th>
  <tr>
  <tr>
    <td>CF-App</td>
    <td>Ja</td>
    <td>Ja</td>
  <tr>  
  <tr>
    <td>Container in Kubernetes-Cluster</td>
    <td>Ja</td>
    <td>Ja</td>
  <tr>  
</table>

Weitere Informationen zu Kibana finden Sie in der Veröffentlichung [Kibana User Guide ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}.
    

##  Navigation zum Kibana-Dashboard vom Bluemix-Dashboard
{: #launch_Kibana_from_bluemix}

Die Abfrage, durch die die in Kibana angezeigten Daten gefiltert werden, ruft Protokolleinträge für die {{site.data.keyword.Bluemix_notm}}-CF-App oder den Container ab, von der/dem Sie Kibana starten.

Führen Sie die folgenden Schritte aus, um die Protokolle einer Cloud Foundry-Anwendung oder eines Docker-Containers in Kibana anzuzeigen:

1. Melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an und klicken Sie dann im {{site.data.keyword.Bluemix_notm}}-Dashboard auf den App-Namen oder Container. 
    
2. Öffnen Sie die Registerkarte 'Protokoll' in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle.

    * Klicken Sie für CF-Apps in der Navigationsleiste auf **Protokolle**. 
    * Wählen Sie für alle in der von {{site.data.keyword.Bluemix_notm}} verwalteten Infrastruktur bereitgestellten Container die Option **Überwachung und Protokolle** in der Navigationsleiste aus und klicken Sie anschließend auf die Registerkarte **Protokollierung**. 
    
        Die Registerkarte 'Protokolle' wird geöffnet.  

3. Klicken Sie auf **Erweiterte Ansicht**. Das Kibana-Dashboard wird geöffnet.

    Standardmäßig ist beim Laden der Seite **Discover** das Standardindexmuster ausgewählt und ein Zeitfilter auf die letzten 30 Sekunden eingestellt. Die Suchabfrage wird so eingestellt, dass sie allen Einträgen für die CF-App oder den Docker-Container entspricht.

    Wenn auf der Seite 'Discover' nicht alle Protokolleinträge angezeigt werden, passen Sie das Zeitauswahlfeld an. 


##  Navigation zum Kibana-Dashboard von einem Web-Browser
{: #launch_Kibana_from_browser1}

Die Abfrage, durch die die in Kibana angezeigten Daten gefiltert werden, ruft Protokolleinträge für einen Bereich in der {{site.data.keyword.Bluemix_notm}}-Organisation ab. Die Protokollinformationen, die in Kibana angezeigt werden, umfassen Einträge für alle Ressourcen, die innerhalb des Bereichs der {{site.data.keyword.Bluemix_notm}}-Organisation bereitgestellt sind, an der Sie angemeldet sind.

Führen Sie den folgenden Schritt aus, um Kibana über einen Browser zu starten:

1. Starten Sie die Kibana-Benutzerschnittstelle.
    
    Beispiel: 
      
        <table>
          <caption>Tabelle 1. URLs zum Starten von Kibana  </caption>
           <tr>
            <th>Region</th>
            <th>URL</th>
          </tr>
          <tr>
            <td>USA (Süden)</td>
            <td>https://logging.ng.bluemix.net/ </td>
          </tr>
          <tr>
            <td>Vereinigtes Königreich</td>
            <td>https://logging.eu-gb.bluemix.net/ </td>
          </tr>
        </table>

    Wenn auf der Seite 'Discover' nicht alle Protokolleinträge angezeigt werden, passen Sie das Zeitauswahlfeld an. 

