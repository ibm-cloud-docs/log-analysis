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

# Protokolle in Kibana interaktiv analysieren
{:#kibana_analize_logs_interactively}

Auf der Seite "Discover" können Sie Ihre {{site.data.keyword.Bluemix}}-Protokolle interaktiv anzeigen und analysieren. Sie können Suchabfragen in der Abfragesprache Lucene definieren, um die Daten zu filtern. Für jede Suchabfrage können Sie Filter anwenden, um die Einträge einzugrenzen, die für die Analyse verfügbar sind. Sie können eine Suche zur späteren Verwendung speichern.
{:shortdesc}

In {{site.data.keyword.Bluemix_notm}} ist die Gruppe von Daten, die auf der Seite 'Discover' angezeigt wird, wenn Sie Kibana in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle starten, standardmäßig so konfiguriert, dass nur die Einträge für die Cloud Foundry-Anwendung (CF-Anwendung) oder den Cloud Foundry-Container angezeigt werden, aus der bzw. dem heraus Kibana gestartet wird. 

In der folgenden Tabelle ist die Standardabfrage für jede Ressource beim Starten von Kibana über {{site.data.keyword.Bluemix_notm}} angegeben:

| Ressource | Standard-Kibana-Suchabfrage |
|---------------|---------------|
| CF-Anwendung   | `Anwendungs-ID:<app_GUID>`    |
| Einzelner Docker-Container | `Instanz:<instance_GUID>`    |
| Containergruppe mit zwei Instanzen | `Instanz:<instance_GUID> ODER Instanz:<instance_GUID>` |
{: caption="Tabelle 1. Standardsuchabfragen" caption-side="top"}

**Hinweis:** 
* Jedes Mal, wenn Sie Kibana aus der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle heraus starten, werden Daten angezeigt, die der standardmäßig vordefinierten Abfrage entsprechen und auf dem Indexmuster basieren.
* Auf der Seite 'Discover' werden maximal 500 Einträge angezeigt, die den zuletzt hinzugefügten Einträgen entsprechen. Sie können diesen Wert auf der Seite mit den Einstellungen ändern.

Wenn Sie Kibana über einen Browser starten, umfassen die Daten, die auf der Seite 'Discover' angezeigt werden, alle Protokolldaten, die in dem Bereich verfügbar sind, in dem Sie angemeldet sind. Die Seite wird nicht auf bestimmte Container oder Apps beschränkt.

Die Seite 'Discover' enthält ein Histogramm und eine Tabelle, die Sie anpassen können, sodass Sie die Daten interaktiv analysieren können. 

Zur Anpassung der Tabelle auf der Seite 'Discover' können Sie beliebige der folgenden Tasks ausführen:

| Task | Beschreibung | 
|------|-------------|
| [Feldspalte hinzufügen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_add_fields_to_table) | Sie können Felder hinzufügen, um anstelle der vollständigen Nachricht bestimmte Daten anzuzeigen, die für die Analyse erforderlich sind. |
| [Feldspalte neu anordnen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_rearrange_fields_in_table) | Verschieben Sie die Position eines Felds in der Tabelle auf der Position, an der Sie es wollen. |
| [Eintrag anzeigen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_view_entry_in_table) | Sie können einen Eintrag in der Tabelle erweitern, um die Details des Eintrags nach Feld geparst oder als JSON-Daten anzuzeigen. |
| [Feldspalte entfernen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_remove_fields_from_table) | Sie können ein Feld entfernen, wenn es in der Ansicht für die Analyse nicht erforderlich ist. |
| [Einträge nach Wert eines indexierten Felds anordnen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_sort_by_table) | Sie können die Einträge zur einfacheren Analyse neu sortieren. |
| [Datenansicht automatisch aktualisieren](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_view_refresh_interval) | Sie können die Daten, die in der Tabelle angezeigt werden, mit den neuesten Einträgen aktualisieren. Standardmäßig ist die Aktualisierung inaktiviert (**OFF**). |
{: caption="Tabelle 2. Tasks für die Anpassung einer Tabelle" caption-side="top"}

<br>

Die folgende Abbildung zeigt ein Beispiel für eine Tabelle auf der Seite 'Discover':

![Seite 'Discover' in Kibana](images/k4_discover_page.jpg "Seite 'Discover' in Kibana")

Sie können weitere Suchen definieren. Wenn Sie eine neue Suche definieren, werden die Daten, die im Histogramm und in der Tabelle angezeigt werden, automatisch aktualisiert.

Zum Definieren einer neuen Suche verwenden Sie die Standardsuchabfrage als Ausgangspunkt und grenzen die Suche dann durch folgende Aktionen ein:

* Wenden Sie Feldfilter an, um die Gruppe von Daten einzugrenzen, die angezeigt wird. Sie können jeden Filter umschalten, auf der Seite fixieren, nach Bedarf aktivieren oder inaktivieren und so konfigurieren, dass der Wert eingeschlossen oder ausgeschlossen wird. 

    **Tipp:** Wenn Sie ein Feld nicht in der *Feldliste* finden können, das Sie erwarten, oder wenn einige der Lupensymbole neben den aufgelisteten Feldern auf der Seite 'Discover' inaktiviert sind, laden Sie die Feldliste erneut, indem Sie das Indexmuster auf der Seite 'Settings' aktualisieren. 

    Wenn Ihre CF-App zum Beispiel viele Instanzen hat, möchten Sie möglicherweise die Daten für eine bestimmte Instanz analysieren. Sie können einen Feldfilter für den bestimmten Instanz-ID-Wert definieren, den Sie analysieren wollen. 
    
* Passen Sie das Zeitauswahlfeld (*Timer Picker*) für zeitbasierte Daten an. Sie können einen absoluten Zeitbereich oder einen relativen Zeitbereich für eine Abfrage angeben oder Sie können einen Zeitbereich aus einer Reihe vordefinierter Werte auswählen. 

Wenn Sie die Suche, die das Datensubset definiert, das Sie analysieren wollen, konfiguriert haben, können Sie sie zur späteren Wiederverwendung speichern.

Sie können eine der folgenden Tasks für Suchen ausführen, die Sie auf der Seite 'Discover' definieren:

| Task | Beschreibung |
|------|-------------|
| Eine Suche speichern | Sie können eine Suche zur späteren Verwendung speichern.  |
| Eine Suche löschen | Sie können eine Suche löschen, wenn sie nicht mehr benötigt wird. |
| Eine Suche exportieren | Sie können eine Suche zur gemeinsamen Nutzung exportieren.  |
| Eine Suche neu laden  | Sie können eine vorhandene Suche hochladen, um eine Gruppe von Daten erneut zu analysieren. |
| Die Daten einer Suche aktualisieren | Sie können eine automatische Aktualisierung der Daten, die durch die Suche angezeigt wird, konfigurieren.  |
| Eine Suche importieren | Sie können eine Suche importieren.  |
{: caption="Tabelle 3. Tasks für die Arbeit mit Suchen" caption-side="top"}

<br>

Sie können auch Statistikdaten auf der Seite 'Discover' ansehen:
* Sie können Statistiken pro Feld anzeigen. 
* Sie können Statistiken im Histogramm pro konfigurierter Zeitmarke (`@timestamp`) anzeigen.

Weitere Informationen finden Sie unter [Statistiken zu Felddaten anzeigen](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-kibana_analize_logs_interactively#kibana_discover_view_fields_stats).

**Hinweis:** Die Daten, die in der Tabelle und im Histogramm angezeigt werden, sind statisch. Wenn Sie immer wieder die neuesten Einträge anzeigen wollen, müssen Sie ein Aktualisierungsintervall festlegen. 


## Feldspalte einer Tabelle hinzufügen
{: #kibana_discover_add_fields_to_table}

Die Tabelle, die zur Analyse von Daten auf der Seite 'Discover' verfügbar ist, enthält standardmäßig die folgenden Felder:
* **time:** Dieses Feld gibt an, wann der Eintrag erfasst und in {{site.data.keyword.Bluemix_notm}} aufgezeichnet wurde.
* **_source:** Dieses Feld enthält die Originaldaten des Eintrags.

Sie können der Tabelle durch eine der folgenden Optionen eine Feldspalte hinzufügen:

* Fügen Sie eine Feldspalte aus der Feldliste ('Fields') hinzu, die auf der Seite verfügbar ist.

    1. Suchen Sie auf der Seite 'Discover' das Feld im Abschnitt `Selected Fields`.
    2. Setzen Sie den Mauszeiger auf ein Feld in der Feldliste.
    
        ![Ansicht zum Hinzufügen eines Feldes aus einer Tabelle](images/k4_add_field_column_hover.jpg "Ansicht zum Hinzufügen eines Feldes aus einer Tabelle")
    
    3. Klicken auf **Add**, um ein Feld hinzuzufügen.
    
 * Fügen Sie eine Feldspalte in der Tabellenansicht eines erweiterten Eintrags hinzu.

    1. Erweitern Sie einen Eintrag in der Tabelle.
    2. Suchen Sie in der Tabellenansicht das Feld, das Sie hinzufügen wollen.
    
        ![Ansicht zum Hinzufügen eines Feldes aus einer Tabelle](images/k4_add_field_column.jpg "Ansicht zum Hinzufügen eines Feldes aus einer Tabelle")
    
    3. Klicken Sie auf das Symbol **Toggle Column in table** ![Toggle column in table](images/k4_toggle_field_icon.jpg).
    

**Hinweis:** Wenn Sie der Tabelle zum ersten Mal eine Feldspalte hinzufügen, wird die in der Tabelle angezeigte Feldspalte *_source* ausgeblendet. Das Feld *_source* zeigt den Wert jedes einzelnen Felds für jeden Protokolleintrag. Wenn Sie andere Feldwerte für einen Protokolleintrag in der Tabelle anzeigen wollen, nachdem Sie der Tabelle eine Spalte hinzugefügt haben, zeigen Sie die Registerkarte für die Tabellenansicht ('Table') oder die Registerkarte 'JSON' für den jeweiligen Eintrag an.

Wenn Sie beispielsweise das Feld *application_id* zur Tabelle hinzufügen, sieht die Tabelle nach dieser Änderung folgendermaßen aus:

![Tabellenansicht nach dem Hinzufügen eines neuen Feldes](images/k4_add_field_filter_new_table_look.jpg "Tabellenansicht nach dem Hinzufügen eines neuen Feldes")


## Datenansicht automatisch aktualisieren
{: #kibana_discover_view_refresh_interval}

In {{site.data.keyword.Bluemix_notm}} ist das Zeitintervall für automatisches Aktualisieren (*Auto-refresh*) standardmäßig inaktiviert (**OFF**) und die Daten, die in Kibana angezeigt werden, entsprechen den letzten 15 Minuten seit dem Start von Kibana. Die 15 Minuten entsprechen dem Zeitfilter, der vorkonfiguriert ist. Sie können diesen Zeitfilter ändern, indem Sie ein anderes Zeitintervall festlegen. 

Führen Sie die folgenden Schritte aus, um ein Zeitintervall für automatisches Aktualisieren (*Auto-refresh*) festzulegen:

1. Klicken Sie in der Menüleiste der Seite 'Discover' auf das Zeitauswahlfeld (Time Picker) ![Time Picker](images/k4_time_picker_icon.jpg "Time Picker").

2. Wählen Sie die Schaltfläche für automatisches Aktualisieren ![Schaltfläche für automatisches Aktualisieren](images/k4_auto_refresh_icon.jpg "Schaltfläche für automatisches Aktualisieren") aus.

3. Wählen Sie ein Aktualisierungsintervall aus.

    ![Optionen zum Festlegen eines automatischen Aktualisierungsintervalls](images/k4_change_autorefresh.jpg "Optionen zum Festlegen eines automatischen Aktualisierungsintervalls")


Sie können das Aktualisierungsintervall anhalten, indem Sie auf die Pauseschaltfläche ![Pauseschaltfläche](images/k4_auto_refresh_pause_icon.jpg "Pause") klicken. 


## Auf der Seite 'Discover' angezeigte Daten ermitteln
{: #k4_identify_data}

Bei der Analyse der {{site.data.keyword.Bluemix_notm}}-Protokolle in Kibana hängen die angezeigten Daten von der Art und Weise, wie Sie Kibana starten, vom konfigurierten Indexmuster (Index Pattern) und von angepassten Abfragen und Filtern ab, die Sie angewendet haben.

Berücksichtigen Sie die folgenden Informationen, um die Daten zu ermitteln, die in der Tabelle und im Histogramm der Seite 'Discover' verfügbar sind:

1. Überprüfen Sie das Indexmuster auf der Seite mit den Einstellungen.

    Das Indexmuster (Index Pattern) definiert die Suchabfrage, die standardmäßig angewendet wird, um Einträge auf Ihren Kibana-Seiten anzuzeigen. Das Indexmuster ist standardmäßig vorkonfiguriert und so eingestellt, dass alle Daten, die in einem Bereich verfügbar sind, erfasst werden. Beispiel:

    * Wenn Sie Kibana von der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle aus starten (d. h. vom Abschnitt *Protokoll* der Benutzerschnittstellenseiten einer bestimmten Ressource, wie z. B. einer Cloud Foundry-Anwendung (CF-Anwendung) oder eines Containers), schließt das Indexmuster, das angewendet wird, alle Einträge ein, die in dem Bereich verfügbar sind.
    
    * Wenn Sie Kibana in einem Browser starten, schließt das Indexmuster, das angewendet wird, alle Einträge ein, die in dem Bereich, den Kibana anzeigt, verfügbar sind, an dem Sie angemeldet sind.
        
2. Überprüfen Sie die Abfrage auf der Seite 'Discover'.  

    Die Abfrage, die auf der Seite 'Discover' angezeigt wird, dient zum Filtern der Einträge, die standardmäßig zur Analyse verfügbar sind. Beispiel:

    * Wenn Sie eine Zeichenfolge in die Suchleiste eingeben, durchsucht die Abfrage alle Felder nach dieser Zeichenfolge.
    
    * Wenn als Abfrage die Zeichenfolge `application_id:<GUID>` angegeben wird, wobei *GUID* die ID einer CF-App ist, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die für diese CF-App in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
    * Wenn als Abfrage die Zeichenfolge `instance_id:<GUID>` angegeben wird, wobei *GUID* die ID einer Containerinstanz ist, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die für diesen Container in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
    * Wenn als Abfrage die Zeichenfolge `instance_id:<GUID> AND instance_id:<GUID>` angegeben wird, wobei *GUID* die ID einer Containerinstanz ist, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die für diese Containergruppe in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
   
    * Wenn als Abfrage das Zeichen `*` angegeben wird, werden die Daten auf alle Einträge gesetzt, die in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
    * o	Wenn als Abfrage die Zeichenfolge `application_id:<GUID> AND message:"MEIN_Suchtext"` angegeben wird, wobei *GUID* die ID einer CF-App ist und *MEIN_Suchtext* die Zeichenfolge ist, nach der Sie suchen wollen, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die *MEIN_Suchtext* im Nachrichtenfeld für diese CF-App-Einträge enthalten, die in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
3. Überprüfen Sie die Feldfilter, die auf Ihre Abfrage auf der Seite 'Discover' angewendet werden.

    Sie können keinen oder mehrere Feldfilter definieren, um Einträge auf der Basis des Werts des Felds umzuschalten. Wenn zum Beispiel ein Feldfilter aktiviert ist, entsprechen die Einträge, die angezeigt werden, Einträgen, in denen der Wert dieses Felds übereinstimmt.
    

## Einträge nach Wert eines indexierten Felds anordnen 
{: #kibana_discover_sort_by_table}

Sie können nur Einträge in der Tabelle nach Feldern sortieren, die indexiert werden.

Um zu ermitteln, welche Felder indexiert sind, führen Sie die folgenden Schritte aus:

1. Klicken Sie auf der Seite 'Discover' auf das Symbol 'Konfigurieren' ![Symbol 'Konfigurieren'](images/k4_configure_icon.jpg "Symbol 'Konfigurieren'"). Der Abschnitt, in dem Sie Felder im Abschnitt **Selected fields** der Seite filtern können, wird angezeigt.

    ![Konfigurationsabschnitt mit Feldern mit bestimmten Attributen](images/k4_reset_filters.jpg "Konfigurationsabschnitt mit Feldern mit bestimmten Attributen")
    
2. Wählen Sie zum Ermitteln der Felder, die indexiert sind, die Option **Yes** für das Suchfeld **Indexed** aus.

    ![Indexiertes Attribut](images/k4_reset_filters_indexed_options.jpg "Indexiertes Attribut")
    
 Die Liste der indexierten Felder wird angezeigt.
 
 ![Liste der indexierten Felder](images/k4_list_indexed_fields.jpg "Liste der indexierten Felder")
  	
 
Führen Sie die folgenden Schritte aus, um die Einträge in der Tabelle nach den Werten eines indexierten Felds zu sortieren: 

1. Bewegen Sie den Mauscursor über den Namen des Felds in der Tabelle, nach dem Sie die Daten sortieren wollen. Die verschiedenen Aktionsschaltflächen werden angezeigt.
2. Klicken Sie auf die Sortierschaltfläche für das Feld, nach dem Sie die Daten sortieren wollen. Klicken Sie ein zweites Mal auf das Sortiersymbol für das Feld, wenn Sie die Sortierreihenfolge umkehren wollen.

**Hinweis:** Wenn Sie nach einem Zeitfeld sortieren, werden die Einträge standardmäßig in umgekehrt chronologischer Reihenfolge angezeigt. Die neuesten Einträge werden zuerst angezeigt.


## Feldspalten in der Tabelle neu anordnen
{: #kibana_discover_rearrange_fields_in_table}

Sie können die Feldspalten in der Tabelle neu anordnen. Setzen Sie den Mauscursor auf die Überschrift der Spalte, die Sie verschieben wollen, und klicken Sie auf die Schaltfläche **Move column to the left** (Spalte nach links verschieben) oder **Move column to the right** (Spalte nach rechts verschieben).
<br>
![Feld in der Tabelle verschieben](images/k4_add_field_filter_new_table_look.jpg "Feld in der Tabelle verschieben")


## Feldliste neu laden
{: #kibana_discover_view_reload_fields}

Führen Sie die folgenden Schritte aus, um die Feldliste erneut zu laden, die in Kibana angezeigt wird:

1. Wählen Sie die Seite mit den Einstellungen aus.

    Wenn Sie die Seite mit den Einstellungen auswählen, wird die Registerkarte *Indices* geöffnet.
   
2. Wählen Sie das Indexmuster aus, um jedes Feld und den zugeordneten Kerntyp des Felds, wie von Elasticsearch aufgezeichnet, anzuzeigen. 

3. Klicken Sie auf die Schaltfläche *Reload field list* ![Reload field list](images/k4_reload_field_list_icon.jpg "Reload field list"), um die Indexmusterfelder erneut zu laden. 

Die Feldliste wird aktualisiert.


## Feldspalten aus der Tabelle entfernen
{: #kibana_discover_remove_fields_from_table}

Führen Sie die folgenden Schritte aus, um Felder aus der Tabelle zu entfernen:

1. Suchen Sie in der Tabelle das Feld, das Sie aus der Tabellenansicht entfernen möchten.
2. Klicken Sie auf **Remove column**.
    
    ![Ansicht zum Entfernen eines Feldes aus der Tabelle](images/k4_remove_field_column.jpg "Ansicht zum Entfernen eines Feldes aus der Tabelle")


## Eintrag in der Tabelle anzeigen
{: #kibana_discover_view_entry_in_table}

Klicken Sie zum Anzeigen der Daten eines Eintrags in der Tabelle auf die Erweiterungsschaltfläche ![Erweiterungsschaltfläche](images/k4_expand_icon.jpg "Erweiterungsschaltfläche") des Eintrags, den Sie analysieren wollen. 

![Tabelle auf der Seite 'Discover' in Kibana](images/k4_table_discover.jpg "Tabelle auf der Seite 'Discover' in Kibana") 	

Wählen Sie dann eine der folgenden Optionen aus, um die Daten anzuzeigen:

* Zum Anzeigen der Daten im Tabellenformat klicken Sie auf **Table**. Der Wert für jedes Feld wird angezeigt, das zur Analyse in einem Tabellenformat verfügbar ist. Für jedes Feld sind außerdem Filterschaltflächen und eine Umschaltfläche verfügbar.
* Zum Anzeigen der Daten im JSON-Format klicken Sie auf **JSON**.

## Statistiken zu Felddaten anzeigen
{: #kibana_discover_view_fields_stats}

Auf der Seite 'Discover' können Sie Statistiken für jedes Feld in der Feldliste *Fields* und im *Histogramm* anzeigen. 

In der Feldliste werden die folgenden Informationen angezeigt:
* Die Anzahl der Einträge in der Tabelle, die ein bestimmtes Feld enthält.
* Die jeweils 5 höchsten Werte.
* Der Prozentsatz der Einträge, die die einzelnen Werte enthalten.

Im Histogramm werden die folgenden Informationen angezeigt:
* Anzahl der Einträge in einem Zeitbereich.

Zum Anzeigen der Statistiken im Histogramm klicken Sie auf eine Zeitmarke, um die Statistiken für diesen Zeitraum einzublenden. Beispiel: 

![Statistiken für ein Feld im Histogramm anzeigen](images/k4_see_stats_on_histogram.jpg "Statistiken für ein Feld im Histogramm anzeigen")
   	
 	
Zum Anzeigen der Statistiken zu einem Feld in der Feldliste klicken Sie auf den Namen. Beispiel:

![Statistiken für ein Feld in der Feldliste anzeigen](images/k4_stats_field_list.jpg "Statistiken für ein Feld in der Feldliste anzeigen")


