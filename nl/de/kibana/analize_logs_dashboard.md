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

# Protokolle in Kibana über ein Dashboard analysieren
{:#analize_logs_dashboard}

Auf der Seite *Dashboard* in Kibana können Sie Visualisierungen anzeigen, die in den Dashboards gruppiert werden. Verwenden Sie die Dashboards, um Ihre Protokolldaten zu analysieren und die Ergebnisse zu vergleichen.
{:shortdesc}

In {{site.data.keyword.Bluemix}} gibt es verschiedene Arten von Dashboards, die Sie definieren und anpassen können, um die Daten zu visualisieren und zu analysieren. In der folgenden Tabelle sind verschiedene Arten von Dashboards aufgelistet:

| Art des Dashboards | Beschreibung |
|-------------------|-------------|
| Dashboard für einzelne CF-App | Dieses Dashboard zeigt Informationen zu einer einzelnen Cloud Foundry-Anwendung an. |
| Dashboard für einzelnen Container  | Dieses Dashboard zeigt Informationen zu einem einzelnen Container an.  |
| Dashboard für Containergruppe  | Dieses Dashboard zeigt Informationen für eine bestimmte Containergruppe an.  |
| Dashboard für mehrere CF-Apps | Dieses Dashboard zeigt Informationen zu allen Cloud Foundry-Anwendungen an, die in demselben Bereich bereitgestellt werden.  | 
| Dashboard für mehrere Container | Dieses Dashboard zeigt Informationen zu allen Containern an, die in demselben Bereich bereitgestellt werden.  |
| Dashboard für einen Bereich | Dieses Dashboard zeigt Protokollierungsdaten an, die in einem Bereich zur Verfügung stehen.  | 
{: caption="Tabelle 1. Beispiele für Dashboardtypen" caption-side="top"}

Konfigurieren Sie die Fensterbereiche, um die Daten in einem Dashboard zu visualisieren. Kibana enthält verschiedene Visualisierungen, wie zum Beispiel Tabellen, Trends und Histogramme, die Sie zur Analyse der Informationen verwenden können. Eine Visualisierung wird einem Dashboard als Fensterbereich hinzugefügt. Sie können Fensterbereiche im Dashboard hinzufügen, entfernen und neu anordnen. Der Zweck jedes Fensterbereichs variiert. Einige Fensterbereiche zeigen zeilenweise die Ergebnisse einer oder mehrerer Abfragen. Andere Fensterbereiche enthalten Dokumente oder angepasste Informationen. Jeder Fensterbereich basiert auf einer Suche. Die Suche definiert das Subset von Daten, die in dem Fensterbereich angezeigt werden. Sie können beispielsweise ein Balkendiagramm, ein Kreisdiagramm oder eine Tabelle konfigurieren, um die Daten zu visualisieren und zu analysieren.  

In der folgenden Tabelle sind die verschiedenen Tasks aufgeführt, die Sie auf der Seite 'Dashboard' ausführen können:

| Task | Weitere Informationen |
|------|------------------|
| [Visualisierung hinzufügen](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#add_visualization) | Sie können eine vorhandene Visualisierung oder Suche zu einem Dashboard hinzufügen.|
| [Neues Dashboard erstellen](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#new) | Sie können mehrere Dashboards erstellen. Jedes Dashboard kann so gestaltet werden, dass es verschiedene Suchen und Visualisierungen oder unterschiedliche Protokolldaten enthält.  |
| [Dashboard löschen](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#delete) | Nicht benötigte Dashboards können gelöscht werden. |
| [Dashboard exportieren](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#export) | Sie können ein Dashboard als JSON-Datei exportieren. |
| [Dashboard importieren](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#import) | Sie können ein Dashboard als JSON-Datei importieren. |
| [Dashboard laden](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#reload3) | Sie können ein Dashboard hochladen, um seine Daten zu aktualisieren, um Änderungen vorzunehmen oder um die Daten zu analysieren. |
| [Dashboard speichern](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save) | Sie können ein Dashboard zur späteren Verwendung speichern. |
{: caption="Tabelle 2. Tasks für die Arbeit mit Dashboards" caption-side="top"}

Weitere Informationen zu Kibana finden Sie in der Veröffentlichung [Kibana User Guide ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Neue Suche oder Visualisierung hinzufügen
{: #add_visualization}

Führen Sie die folgenden Schritte aus, um eine vorhandene Visualisierung oder Suche hinzuzufügen:

1. Klicken Sie in der Symbolleiste der Seite 'Dashboard' auf **Add**. 

    **Hinweis:** Sie können Visualisierungen und Suchen hinzufügen. 

2. Wählen Sie die Registerkarte **Visualizations** aus, um eine Visualisierung hinzufügen, oder wählen Sie die Registerkarte **Searches**, um eine Suche hinzuzufügen.

3. Klicken Sie auf die Suche oder Visualisierung, die Sie hinzufügen wollen.

    Ein Fensterbereich für die Suche oder Visualisierung wird zum Dashboard hinzugefügt.

	
## Neues Kibana-Dashboard erstellen
{: #new}

Führen Sie die folgenden Schritte aus, um ein neues Dashboard zu erstellen:

1. Klicken Sie in der Symbolleiste der Seite 'Dashboard' auf **Add**. 

2. Fügen Sie eine oder mehr Suchen und Visualisierungen hinzu. Weitere Informationen finden Sie unter [Neue Suche oder Visualisierung hinzufügen](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#add_visualization).

    Wenn Sie eine Suche oder eine Visualisierung hinzufügen, wird ein Fensterbereich im Dashboard hinzugefügt.

3. Ziehen Sie einen Fensterbereich und legen Sie ihn in dem Teil des Dashboards ab, in dem Sie ihn positionieren wollen.
 
4. Speichern Sie das Dashboard zur späteren Wiederverwendung. Weitere Informationen finden Sie unter [Kibana-Dashboard speichern](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save).


## Kibana-Dashboard löschen
{: #delete1}

Führen Sie die folgenden Schritte auf der Seite **Management** aus, um ein Dashboard zu löschen:

1. Wählen Sie auf der Seite **Management** die Option **Saved Objects** aus.

2. Wählen Sie in der Registerkarte **Dashboards** das Dashboard aus, das Sie löschen wollen.

3. Klicken Sie auf **Delete**.

## Kibana-Dashboard exportieren
{: #export}

Führen Sie die folgenden Schritte auf der Seite **Management** aus, um ein Dashboard als JSON-Datei zu exportieren:

1. Wählen Sie auf der Seite **Management** die Option **Saved Objects** aus.

2. Wählen Sie in der Registerkarte **Dashboard** das Dashboard aus, das Sie exportieren wollen.

3. Klicken Sie auf **Export**.

4. Speichern Sie die Datei.

## Kibana-Dashboard importieren
{: #import}

Führen Sie die folgenden Schritte auf der Seite **Management** aus, um ein Dashboard als JSON-Datei zu importieren:

1. Wählen Sie auf der Seite **Management** die Option **Saved Objects** aus.

2. Wählen Sie in der Registerkarte **Dashboard** die Option **Import** aus.

3. Wählen Sie eine Datei aus und klicken Sie auf **Open**.

Das Dashboard wird zur Liste der Dashboards hinzugefügt.

## Kibana-Dashboard laden
{: #reload3}

Führen Sie die folgenden Schritte aus, um ein gespeichertes Dashboard zu laden:

1. Klicken Sie in der Symbolleiste der Seite 'Dashboard' auf **Open**.

2. Wählen Sie ein Dashboard aus der Liste der verfügbaren Dashboards aus, die unter dem Feld *Name* angezeigt wird.

Sie können über die Suchleiste auch nach einem Dashboard suchen.

## Kibana-Dashboard speichern
{: #save}

Führen Sie die folgenden Schritte aus, um ein Kibana-Dashboard zu speichern, nachdem Sie es angepasst haben:

1. Klicken Sie in der Symbolleiste auf **Save**.

2. Geben Sie einen Namen für das Dashboard ein.

    **Hinweis:** Der Name darf keine Leerzeichen enthalten.

3. Klicken Sie auf **Save**.




