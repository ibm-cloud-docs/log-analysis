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
{: #launch}

Sie können Kibana über den {{site.data.keyword.loganalysisshort}}-Service, über die {{site.data.keyword.Bluemix}}-Benutzerschnittstelle oder direkt über einen Web-Browser starten.
{:shortdesc}

Für CF-Apps und Docker-Container können Sie Kibana über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle starten, um Daten im Kontext der Ressource anzuzeigen und zu analysieren, von der Sie Kibana starten. Sie können Ihre spezifischen CF-App-Protokolle in Kibana im Kontext dieser spezifischen App starten.
    
Bei allen Cloudressourcen - wie z. B. Docker-Container, die in einer Kubernetes-Infrastruktur bereitgestellt sind - können Sie Kibana über einen direkten Browser-Link oder vom Dashboard des {{site.data.keyword.loganalysisshort}}-Service starten, um zusammengefasste Protokolldaten von Services in einem zur Verfügung gestellten Bereich anzuzeigen. Die Abfrage, durch die die im Dashboard angezeigten Daten gefiltert werden, ruft Protokolleinträge für einen Bereich in der Organisation ab. Die Protokollinformationen, die in Kibana angezeigt werden, umfassen Einträge für alle Ressourcen, die innerhalb des Bereichs der Organisation bereitgestellt sind, an der Sie angemeldet sind. 

Die folgende Tabelle listet einige Cloudressourcen und die unterstützten Navigationsmethoden zum Starten von Kibana auf:

<table>
<caption>Tabelle 1. Liste der Ressourcen und unterstützten Navigationsmethoden. </caption>
  <tr>
    <th>Ressource</th>
	<th>Navigation zum Kibana-Dashboard vom {{site.data.keyword.loganalysisshort}}-Service-Dashboard</th>
    <th>Navigation zum Kibana-Dashboard vom Bluemix-Dashboard</th>
    <th>Navigation zum Kibana-Dashboard von einem Web-Browser</th>
  </tr>
  <tr>
    <td>CF-App</td>
	<td>Ja</td>
    <td>Ja</td>
    <td>Ja</td>
  </tr>  
  <tr>
    <td>Container in Kubernetes-Cluster</td>
	<td>Ja</td>
    <td>Ja</td>
    <td>Ja</td>
  </tr>  
  <tr>
    <td>Container in einer {{site.data.keyword.Bluemix_notm}}-verwalteten Infrastruktur (veraltet)</td>
	<td>Ja</td>
    <td>Ja</td>
    <td>Ja</td>
  </tr>  
</table>

Weitere Informationen zu Kibana finden Sie in der Veröffentlichung [Kibana User Guide ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.
    

##  Vom Dashboard des Log Analysis-Service zu Kibana navigieren
{: #launch_Kibana_from_log_analysis}

Mit der Abfrage, durch die die in Kibana angezeigten Daten gefiltert werden, werden Protokolleinträge für den Bereich in der Organisation abgerufen. 
	
Die Protokollinformationen, die in Kibana angezeigt werden, umfassen Einträge für alle Ressourcen, die innerhalb des Bereichs der Organisation bereitgestellt sind, an der Sie angemeldet sind.

Führen Sie die folgenden Schritte aus, um Kibana von dem Dashboard des {{site.data.keyword.loganalysisshort}}-Service zu starten:

1. Melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an und klicken Sie dann im {{site.data.keyword.Bluemix_notm}}-Dashboard auf den {{site.data.keyword.loganalysisshort}}-Service. 
    
2. Wählen Sie die Registerkarte **Managed** in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle aus.

3. Klicken Sie auf **LAUNCH**. Das Kibana-Dashboard wird geöffnet.

Standardmäßig ist beim Laden der Seite **Discover** das Standardindexmuster ausgewählt und ein Zeitfilter auf die letzten 15 Minuten eingestellt. 

Wenn auf der Seite 'Discover' nicht alle Protokolleinträge angezeigt werden, passen Sie das Zeitauswahlfeld an. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	
	
##  Von einem Web-Browser zu Kibana navigieren
{: #launch_Kibana_from_browser}

Mit der Abfrage, durch die die in Kibana angezeigten Daten gefiltert werden, werden Protokolleinträge für den Bereich in der Organisation abgerufen. 
	
Die Protokollinformationen, die in Kibana angezeigt werden, umfassen Einträge für alle Ressourcen, die innerhalb des Bereichs der Organisation bereitgestellt sind, an der Sie angemeldet sind.

Führen Sie die folgenden Schritte aus, um Kibana von einem Browser zu starten:

1. Öffnen Sie einen Web-Browser und starten Sie Kibana. Melden Sie sich anschließend an der Kibana-Benutzerschnittstelle an.

    Eine Liste der URLs nach Region finden Sie unter [URLs zum Starten von Kibana](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana).
    
    Die Seite 'Discover' in Kibana wird geöffnet.
	
2. Wählen Sie das Indexmuster für den Bereich aus, in dem Sie Protokolldaten anzeigen und analysieren wollen.

    1. Klicken Sie auf **default-index**.
	
	2. Wählen Sie das Indexmuster für den Bereich aus. Das Indexmuster hat folgendes Format:
	
	    ```
	    [logstash-Bereichs-ID-]JJJJ.MM.TT 
	    ```
        {: screen}
	
	    Dabei ist *Bereichs-ID* die GUID des Bereichs, in dem Sie Protokolldaten anzeigen und analysieren wollen. 
	
Wenn auf der Seite 'Discover' nicht alle Protokolleinträge angezeigt werden, passen Sie das Zeitauswahlfeld an. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).


	
##  Vom Dashboard einer CF-App zu Kibana navigieren
{: #launch_Kibana_from_cf_app}

Die Abfrage, durch die die in Kibana angezeigten Daten gefiltert werden, ruft Protokolleinträge für die {{site.data.keyword.Bluemix_notm}}-CF-App ab, von der Sie Kibana starten.

Führen Sie die folgenden Schritte aus, um die Protokolle einer Cloud Foundry-Anwendung in Kibana anzuzeigen:

1. Melden Sie sich an Ihrem {{site.data.keyword.Bluemix_notm}}-Konto an.

    Das {{site.data.keyword.Bluemix_notm}}-Dashboard finden Sie unter [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window}.
    
	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

2. Klicken Sie im {{site.data.keyword.Bluemix_notm}}-Dashboard auf den App-Namen oder Container. 
    
3. Öffnen Sie die Registerkarte 'Protokoll' in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle.

    Klicken Sie für CF-Apps in der Navigationsleiste auf **Protokolle**. 
    Die Registerkarte 'Protokolle' wird geöffnet.  

4. Klicken Sie auf die Option zur Anzeige in Kibana. Das Kibana-Dashboard wird geöffnet.

    Standardmäßig ist beim Laden der Seite **Discover** das Standardindexmuster ausgewählt und ein Zeitfilter auf die letzten 15 Minuten eingestellt. Die Suchabfrage wird so eingestellt, dass sie allen Einträgen für der CF-App entspricht.

    Wenn auf der Seite 'Discover' nicht alle Protokolleinträge angezeigt werden, passen Sie das Zeitauswahlfeld an. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	
	
##  Vom Dashboard eines in einem Kubernetes-Cluster bereitgestellten Containers zu Kibana navigieren
{: #launch_Kibana_for_containers_kube}

Die Abfrage, mit der die in Kibana angezeigten Daten gefiltert werden, ruft Protokolleinträge für den Cluster ab, von dem Sie Kibana starten.

Führen Sie die folgenden Schritte aus, um die Protokolle eines Containers in Kibana anzuzeigen:

1. Melden Sie sich an Ihrem {{site.data.keyword.Bluemix_notm}}-Konto an.

    Das {{site.data.keyword.Bluemix_notm}}-Dashboard finden Sie unter [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window}.
    
	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

2. Wählen Sie im Menü die Option **Dashboard** aus.

3. Wählen Sie im Abschnitt *Cluster* den Cluster aus.

4. Wählen Sie im Abschnitt *Übersicht* die Option **Protokolle anzeigen** aus.

    Kibana wird geöffnet.




##  Vom Dashboard eines in der von {{site.data.keyword.Bluemix_notm}} verwalteten Infrastruktur bereitgestellten Containers zu Kibana navigieren (veraltet)
{: #launch_Kibana_for_containers}

Diese Methode gilt nur für Container, die in der {{site.data.keyword.Bluemix_notm}}-verwalteten Infrastruktur bereitgestellt werden.

Die Abfrage, durch die die in Kibana angezeigten Daten gefiltert werden, ruft Protokolleinträge für den Container ab, von dem Sie Kibana starten.

Führen Sie die folgenden Schritte aus, um die Protokolle eines Docker-Containers in Kibana anzuzeigen:

1. Melden Sie sich bei {{site.data.keyword.Bluemix_notm}} an und klicken Sie dann im {{site.data.keyword.Bluemix_notm}}-Dashboard auf den Container. 
    
2. Öffnen Sie die Registerkarte 'Protokoll' in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle.

    Wählen Sie für alle in der von {{site.data.keyword.IBM_notm}} verwalteten Infrastruktur bereitgestellten Container die Option **Überwachung und Protokolle** in der Navigationsleiste aus und klicken Sie anschließend auf die Registerkarte **Protokollierung**. 
    
    Die Registerkarte 'Protokolle' wird geöffnet.  

3. Klicken Sie auf **Erweiterte Ansicht**. Das Kibana-Dashboard wird geöffnet.

    Standardmäßig ist beim Laden der Seite **Discover** das Standardindexmuster ausgewählt und ein Zeitfilter auf die letzten 30 Sekunden eingestellt. Die Suchabfrage wird so eingestellt, dass sie allen Einträgen für den Docker-Container entspricht.

    Wenn auf der Seite 'Discover' nicht alle Protokolleinträge angezeigt werden, passen Sie das Zeitauswahlfeld an. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

	



