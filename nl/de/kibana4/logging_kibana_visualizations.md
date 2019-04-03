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

# Protokolle in Kibana mit Visualisierungen analysieren 
{:#logging_kibana_visualizations}

Auf der Seite *Visualize* in Kibana können Sie Visualisierungen wie Diagramme und Tabellen erstellen, mit denen Sie Ihre Protokolldaten analysieren und Ergebnisse vergleichen können. 
{:shortdesc}

Sie können eine Visualisierung individuell verwenden, um Ihre Protokolle zu analysieren. 

* Sie können Visualisierungen aus einer Suche erstellen, die Sie auf der Seite *Discover* definieren und speichern, oder aus einer neuen Abfrage, die Sie auf der Seite *Visualize* definieren. Die Suche definiert das Subset von Daten, die durch die Visualisierung angezeigt werden.

* Der Typ der Visualisierung, die Sie auswählen, bestimmt, wie die Daten für die Analyse angezeigt werden.

In der folgenden Tabelle sind die verschiedenen Visualisierungstypen aufgeführt:

| Typ der Visualisierung | Beschreibung |
|-----------------------|-------------|
| Flächendiagramm | Zeigt quantitative Daten in grafischer Form. Verwenden Sie diese Option, um zwei oder mehr Gruppen zusammengefasster Daten zu vergleichen. |
| Datentabelle | Zeigt Rohdaten in tabellarischer Form für eine zusammengesetzte Aggregation. |
| Kurvendiagramm | Zeigt zeitbasierte Daten. Verwenden Sie diese Option, um zwei oder mehr Gruppen zusammengefasster zeitbasierter Daten zu vergleichen. |
| Markdown-Widget | Zeigt Textinformationen an. |
| Metrik | Zeigt eine Trefferzahl oder den genauen Durchschnitt eines numerischen Felds. |
| Kreisdiagramm | Zeigt verschiedene Werte eines Felds. | 
| Vertikales Balkendiagramm | Zeigt zeitbasierte und nicht zeitbasierte Daten. Dient zur Gruppierung von Daten. |
{: caption="Tabelle 1. Visualisierungstypen" caption-side="top"}

Auf der Seite 'Visualize' können Sie eine der folgenden Tasks ausführen:

| Task | Weitere Informationen |
|------|------------------|
| [Neue Visualisierung erstellen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_k4_visualizations_create) | Sie können Visualisierungen aus einer Suche erstellen, die Sie auf der Seite *Discover* definieren und speichern, oder aus einer neuen Abfrage, die Sie auf der Seite *Visualize* definieren. |
| [Visualisierung speichern](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_save) | Sie können Visualisierungen zur späteren Wiederverwendung speichern. |
| [Visualisierung laden](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_reload) | Sie können eine Visualisierung hochladen, um ihre Daten zu aktualisieren, um Änderungen vorzunehmen oder um die Daten zu analysieren. |
| [Visualisierung löschen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_delete) | Nicht benötigte Visualisierungen können gelöscht werden. |
| [Visualisierung exportieren](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_export) | Sie können eine Visualisierung als JSON-Datei exportieren.  |
| [Visualisierung importieren](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_import) | Sie können eine Visualisierung als JSON-Datei importieren.  |
| [Visualisierung freigeben](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_share) | Sie können eine Visualisierung über Ihre HTML-Quelle oder das Kibana-Dashboard freigeben.  |
{: caption="Tabelle 2. Tasks für die Arbeit mit Visualisierungen" caption-side="top"}


## Visualisierungen über Abfragen in Kibana erstellen
{:#logging_k4_visualizations_create}

Führen Sie die folgenden Schritte aus, um eine Visualisierung über die Seite 'Visualize' zu erstellen:

1. Starten Sie Kibana und wählen Sie anschließend die Seite **Visualize** aus.

2. Erstellen Sie eine neue Visualisierung. Klicken Sie in der Symbolleiste auf die Schaltfläche **New Visualization** ![New Visualization](images/k4_visualization_new_icon.jpg "New Visualization").

3. Wählen Sie eine Visualisierung aus.
    
4. Wählen Sie eine Suchquelle aus. Wählen Sie eine der folgenden Optionen aus:

    * Klicken Sie auf **From a new search**.
    * Klicken Sie auf **From a saved search**. 
  
5. Konfigurieren Sie die Abfrage.

    * Bei Auswahl der Option **From a saved search** wählen Sie eine Suchabfrage aus. Die Abfrage wird verwendet, um die Daten abzurufen, die für die Visualisierung verwendet werden. 

        Wenn Sie eine Suche ausgewählt haben, wird der Visualization Builder geöffnet und lädt die Daten für die ausgewählte Abfrage. Die folgende Nachricht wird angezeigt: *This visualization is linked to a saved search: Name_der_Suche*. 
	
	**Hinweis**: Alle Änderungen, die Sie an einer gespeicherten Suche vornehmen, werden automatisch in der Visualisierung nachvollzogen. Zum Inaktivieren der automatischen Aktualisierungen, die Sie an der Abfrage vornehmen, die mit dieser Visualisierung verknüpft ist, klicken Sie doppelt auf die Nachricht *This visualization is linked to a saved search: your_search_name*. 

    * Bei Auswahl der Option **From a new search** definieren Sie eine neue Abfrage. Die Abfrage wird verwendet, um das Subset der Daten zu definieren, die von der Visualisierung abgerufen und verwendet werden.

6. Wählen Sie im Visualization Builder eine Metrikzusammenfassung für die Y-Achse aus.

7. Wählen Sie im Visualization Builder einen Buckettyp aus. Wählen Sie anschließend eine Bucketzusammenfassung aus.
  
8. Fügen Sie Sub-Buckets hinzu, um die Daten aufzugliedern.

Weitere Informationen zu Kibana finden Sie in der Veröffentlichung [Kibana User Guide ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}.

## Visualisierung löschen
{:#logging_kibana_visualizations_delete}

Führen Sie auf der Seite 'Settings' die folgenden Schritte aus, um eine Visualisierung zu löschen:

1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.

2. Wählen Sie in der Registerkarte **Visualizations** die Visualisierung aus, die Sie löschen wollen.

3. Klicken Sie auf **Delete**.


## Visualisierung exportieren
{:#logging_kibana_visualizations_export}

Führen Sie auf der Seite 'Settings' die folgenden Schritte aus, um eine Visualisierung als eine JSON-Datei zu exportieren:

1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.

2. Wählen Sie in der Registerkarte **Visualizations** die Visualisierung aus, die Sie exportieren wollen.

3. Klicken Sie auf **Export**.

4. Speichern Sie die Datei.

## Visualisierung importieren
{:#logging_kibana_visualizations_import}

Führen Sie auf der Seite 'Settings' die folgenden Schritte aus, um eine Visualisierung als eine JSON-Datei zu importieren:

1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.

2. Wählen Sie in der Registerkarte **Visualizations** die Option **Import** aus.

3. Wählen Sie eine Datei aus und klicken Sie auf **Open**.

Die Visualisierung wird zur Liste der Visualisierungen hinzugefügt.


 
## Visualisierung laden
{:#logging_kibana_visualizations_reload}

Führen Sie die folgenden Schritte aus, um eine gespeicherte Visualisierung zu laden:

1. Klicken Sie in der Symbolleiste der Seite 'Visualize' auf die Schaltfläche **Load Saved Visualization** ![Load Saved Visualization](images/k4_visualization_open_icon.jpg "Load Saved Visualization").

2. Wählen Sie die Visualisierung aus, die Sie laden wollen. 


## Visualisierung speichern
{:#logging_kibana_visualizations_save}

Führen Sie die folgenden Schritte aus, um eine Visualisierung auf der Seite 'Visualize' zu speichern:

1. Klicken Sie in der Symbolleiste der Seite 'Visualize' auf die Schaltfläche **Save Visualization** ![Save Visualization](images/k4_visualization_save_icon.jpg "Save Visualization").

2. Geben Sie einen Namen für die Visualisierung ein.

3. Klicken Sie auf 'Save'. 



## Visualisierung gemeinsam nutzen
{:#logging_kibana_visualizations_share}

Führen Sie die folgenden Schritte aus, um eine Visualisierung auf der Seite 'Visualize' gemeinsam zu nutzen:

1. Klicken Sie in der Symbolleiste der Seite 'Visualize' auf die Schaltfläche **Share Visualization** ![Share Visualization](images/k4_visualization_share_icon.jpg "Share Visualization").

2. Wählen Sie eine der folgenden Aktionen aus:

    * **Embed this visualization**: Wählen Sie diese Option aus, um die Visualisierung über die HTML-Quelle gemeinsam zu nutzen. 
    
        Klicken Sie auf die Schaltfläche zum Kopieren ![In Zwischenablage kopieren](images/k4_copy_to_clipboard.jpg "In Zwischenablage kopieren"), um den HTML-Code zu kopieren, den Sie zum Einbetten der Visualisierung in die HTML-Quelle verwenden können. 
	
	**Hinweis**: Um die Visualisierung sehen zu können, müssen Benutzer Zugriff auf Kibana haben.
	
    * **Share a link**: Wählen Sie diese Option aus, um die Visualisierung mit anderen Benutzern in Kibana gemeinsam zu nutzen.



