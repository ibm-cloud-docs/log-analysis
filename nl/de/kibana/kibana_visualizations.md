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
{:#kibana_visualizations}

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
| [Neue Visualisierung erstellen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#create) | Sie können Visualisierungen aus einer Suche erstellen, die Sie auf der Seite *Discover* definieren und speichern, oder aus einer neuen Abfrage, die Sie auf der Seite *Visualize* definieren. |
| [Visualisierung löschen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#delete) | Nicht benötigte Visualisierungen können gelöscht werden. |
| [Visualisierung exportieren](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#export) | Sie können eine Visualisierung als JSON-Datei exportieren.  |
| [Visualisierung importieren](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#import1) | Sie können eine Visualisierung als JSON-Datei importieren.  |
| [Visualisierung laden](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#reload2) | Sie können eine Visualisierung hochladen, um ihre Daten zu aktualisieren, um Änderungen vorzunehmen oder um die Daten zu analysieren. |
| [Visualisierung speichern](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#save2) | Sie können Visualisierungen zur späteren Wiederverwendung speichern. |
{: caption="Tabelle 2. Tasks für die Arbeit mit Visualisierungen" caption-side="top"}


## Visualisierungen über Abfragen in Kibana erstellen
{: #create}

Führen Sie die folgenden Schritte aus, um eine Visualisierung über die Seite 'Visualize' zu erstellen:

1. Starten Sie Kibana und wählen Sie anschließend die Seite **Visualize** aus.

2. Wählen Sie einen Visualisierungstyp aus, z. B. *table*.

3. Wählen Sie eine Visualisierung aus, die Sie zuvor über die Option **Or, From a Saved Search** gespeichert haben, oder wählen Sie einen Index im Abschnitt **From a New Search, Select Index** aus.

4. Konfigurieren Sie die Abfrage.

    * Bei Auswahl der Option **Or, From a Saved Search** wählen Sie eine Suchabfrage aus. Die Abfrage wird verwendet, um die Daten abzurufen, die für die Visualisierung verwendet werden. 
	
	    Wenn Sie eine Suche ausgewählt haben, wird der Visualization Builder geöffnet und lädt die Daten für die ausgewählte Abfrage. 
		
		**Hinweis**: Alle Änderungen, die Sie an einer gespeicherten Suche vornehmen, werden automatisch in der Visualisierung nachvollzogen. Zum Inaktivieren der automatischen Aktualisierungen, die Sie an der Abfrage vornehmen, die mit dieser Visualisierung verknüpft ist, klicken Sie doppelt auf die Nachricht *This visualization is linked to a saved search: your_search_name*. 

    * Bei Auswahl von **From a New Search, Select Index** definieren Sie eine neue Abfrage. Die Abfrage wird verwendet, um das Subset der Daten zu definieren, die von der Visualisierung abgerufen und verwendet werden.

        Weitere Informationen finden Sie unter [Protokolle durch Definieren angepasster Abfragen filtern](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search).

Weitere Informationen zu Kibana finden Sie in der Veröffentlichung [Kibana User Guide ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Visualisierung löschen
{: #delete}

Führen Sie die folgenden Schritte auf der Seite **Management** aus, um eine Visualisierung zu löschen:

1. Wählen Sie auf der Seite **Management** die Option **Saved Objects** aus.

2. Wählen Sie in der Registerkarte **Visualizations** die Visualisierung aus, die Sie löschen wollen.

3. Klicken Sie auf **Delete**.


## Visualisierung exportieren
{: #export1}

Führen Sie die folgenden Schritte auf der Seite **Management** aus, um eine Visualisierung als JSON-Datei zu exportieren:

1. Wählen Sie auf der Seite **Management** die Option **Saved Objects** aus.

2. Wählen Sie in der Registerkarte **Visualizations** die Visualisierung aus, die Sie exportieren wollen.

3. Klicken Sie auf **Export**.

4. Speichern Sie die Datei.

## Visualisierung importieren
{: #import1}

Führen Sie die folgenden Schritte auf der Seite **Management** aus, um eine Visualisierung als JSON-Datei zu importieren:

1. Wählen Sie auf der Seite **Management** die Option **Saved Objects** aus.

2. Wählen Sie in der Registerkarte **Visualizations** die Option **Import** aus.

3. Wählen Sie eine Datei aus und klicken Sie auf **Open**.

Die Visualisierung wird zur Liste der Visualisierungen hinzugefügt.


 
## Visualisierung laden
{: #reload2}

Führen Sie die folgenden Schritte aus, um eine gespeicherte Visualisierung zu laden:

1. Klicken Sie in der Symbolleiste der Seite 'Visualize' auf **Open**.

2. Wählen Sie die Visualisierung aus, die Sie laden wollen. 


## Visualisierung speichern
{: #save2}

Führen Sie die folgenden Schritte aus, um eine Visualisierung auf der Seite 'Visualize' zu speichern:

1. Klicken Sie in der Symbolleiste der Seite 'Visualize' auf **Save**.

2. Geben Sie einen Namen für die Visualisierung ein.

3. Klicken Sie auf 'Save'. 


