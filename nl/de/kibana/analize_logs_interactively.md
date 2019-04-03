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
{:#analize_logs_interactively}

Auf der Seite 'Discover' können Sie Ihre Protokolle interaktiv anzeigen und analysieren. Sie können Suchabfragen in der Abfragesprache Lucene definieren, um die Daten zu filtern. Für jede Suchabfrage können Sie Filter anwenden, um die Einträge einzugrenzen, die für die Analyse verfügbar sind. Sie können eine Suche zur späteren Verwendung speichern.
{:shortdesc}

In {{site.data.keyword.Bluemix_notm}} ist die Gruppe von Daten, die auf der Seite 'Discover' angezeigt wird, wenn Sie Kibana in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle starten, standardmäßig so konfiguriert, dass nur die Einträge für die Cloud Foundry-Anwendung (CF-Anwendung) oder den Cloud Foundry-Container angezeigt werden, aus der bzw. dem heraus Kibana gestartet wird. Weitere Informationen dazu, wie Sie ermitteln, welches Subset Ihrer Daten auf der Seite 'Discover' angezeigt wird, finden Sie unter [Angezeigte Daten ermitteln](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

In der folgenden Tabelle wird die Standardabfrage für jede Ressource beim Starten von Kibana über {{site.data.keyword.Bluemix_notm}} angegeben:

| Ressource | Standard-Kibana-Suchabfrage |
|---------------|---------------|
| CF-Anwendung   | `Anwendungs-ID:<app_GUID>`    |
| Einzelner Docker-Container | `Instanz:<instance_GUID>`    |
| Containergruppe mit zwei Instanzen | `Instanz:<instance_GUID> ODER Instanz:<instance_GUID>` |
{: caption="Tabelle 1. Standardsuchabfragen" caption-side="top"}

**Hinweis:** 
* Jedes Mal, wenn Sie Kibana aus der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle heraus starten, werden Daten angezeigt, die der standardmäßig vordefinierten Abfrage entsprechen und auf dem Indexmuster basieren.
* Auf der Seite 'Discover' werden maximal 500 Einträge angezeigt, die den zuletzt hinzugefügten Einträgen entsprechen. Um diesen Wert zu ändern, können Sie das Feld * discover:sampleSize * im Abschnitt **Advanced Options** ändern, der auf der Seite **Management** verfügbar ist.

Wenn Sie Kibana über einen Browser oder über das Dashboard des {{site.data.keyword.loganalysisshort}}-Service starten, umfassen die Daten, die auf der Seite 'Discover' angezeigt werden, alle Protokolldaten, die in dem Bereich verfügbar sind, in dem Sie angemeldet sind. Die Seite wird nicht auf bestimmte Services, Container oder Apps beschränkt.

Die Seite 'Discover' enthält ein Histogramm und eine Tabelle, die Sie anpassen können, sodass Sie die Daten interaktiv analysieren können. 

Zur Anpassung der Tabelle auf der Seite 'Discover' können Sie beliebige der folgenden Tasks ausführen:

| Task | Beschreibung | 
|------|-------------|
| [Feldspalte hinzufügen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_add_fields_to_table) | Sie können Felder hinzufügen, um anstelle der vollständigen Nachricht bestimmte Daten anzuzeigen, die für die Analyse erforderlich sind. |
| [Datenansicht automatisch aktualisieren](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_refresh_interval) | Sie können die Daten, die in der Tabelle angezeigt werden, mit den neuesten Einträgen aktualisieren. Standardmäßig ist die Aktualisierung inaktiviert (**OFF**). |
| [Einträge nach Wert eines indexierten Felds anordnen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_sort_by_table) | Sie können die Einträge zur einfacheren Analyse neu sortieren. |
| [Feldspalte neu anordnen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_rearrange_fields_in_table) | Verschieben Sie die Position eines Felds in der Tabelle auf der Position, an der Sie es wollen. |
| [Feldspalte entfernen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_remove_fields_from_table) | Sie können ein Feld entfernen, wenn es in der Ansicht für die Analyse nicht erforderlich ist. |
| [Eintrag anzeigen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_entry_in_table) | Sie können einen Eintrag in der Tabelle erweitern, um die Details des Eintrags nach Feld geparst oder als JSON-Daten anzuzeigen. |
{: caption="Tabelle 2. Tasks für die Anpassung einer Tabelle" caption-side="top"}

<br>

Die folgende Abbildung zeigt ein Beispiel für eine Tabelle auf der Seite 'Discover':

![Seite 'Discover' in Kibana](images/discover_page.gif "Seite 'Discover' in Kibana")

Sie können weitere Suchen definieren. Weitere Informationen finden Sie unter [Protokolle durch Definieren angepasster Suchen filtern](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search). Wenn Sie eine neue Suche definieren, werden die Daten, die im Histogramm und in der Tabelle angezeigt werden, automatisch aktualisiert.

Zum Definieren einer neuen Suche verwenden Sie die Standardsuchabfrage als Ausgangspunkt und grenzen die Suche dann durch folgende Aktionen ein:

* Wenden Sie Feldfilter an, um die Gruppe von Daten einzugrenzen, die angezeigt wird. Sie können jeden Filter umschalten, auf der Seite fixieren, nach Bedarf aktivieren oder inaktivieren und so konfigurieren, dass der Wert eingeschlossen oder ausgeschlossen wird. Weitere Informationen finden Sie unter [Protokolle in Kibana filtern](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs).

    **Tipp:** Wenn Sie ein Feld in der Liste *Fields*  nicht finden können, das Sie erwarten, oder wenn einige der Lupensymbole neben den aufgelisteten Feldern auf der Seite 'Discover' inaktiviert sind, laden Sie die Feldliste erneut, indem Sie das Indexmuster auf der Seite 'Settings' aktualisieren. Weitere Informationen finden Sie unter [Feldliste erneut laden](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_reload_fields).

    Wenn Ihre CF-App zum Beispiel viele Instanzen hat, möchten Sie möglicherweise die Daten für eine bestimmte Instanz analysieren. Sie können einen Feldfilter für den bestimmten Instanz-ID-Wert definieren, den Sie analysieren wollen. 
    
* Passen Sie das Zeitauswahlfeld (*Timer Picker*) für zeitbasierte Daten an. Sie können einen absoluten Zeitbereich oder einen relativen Zeitbereich für eine Abfrage angeben oder Sie können einen Zeitbereich aus einer Reihe vordefinierter Werte auswählen. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

Wenn Sie die Suche, die das Datensubset definiert, das Sie analysieren wollen, konfiguriert haben, können Sie sie zur späteren Wiederverwendung speichern. Weitere Informationen finden Sie unter [Suche speichern](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search).

Sie können eine der folgenden Tasks für Suchen ausführen, die Sie auf der Seite 'Discover' definieren:

| Task | Beschreibung |
|------|-------------|
| [Suche löschen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#delete_search) | Sie können eine Suche löschen, wenn sie nicht mehr benötigt wird. |
| [Suche exportieren](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#export_search) | Sie können eine Suche zur gemeinsamen Nutzung exportieren.  |
| [Suche importieren](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#import_search) | Sie können eine Suche importieren.  |
| [Suche neu laden](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#reload_search1)  | Sie können eine vorhandene Suche hochladen, um eine Gruppe von Daten erneut zu analysieren. |
| [Daten einer Suche aktualisieren](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#refresh_search) | Sie können eine automatische Aktualisierung der Daten, die durch die Suche angezeigt wird, konfigurieren.  |
| [Suche speichern](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search) | Sie können eine Suche zur späteren Verwendung speichern.  |
{: caption="Tabelle 3. Tasks für die Arbeit mit Suchen" caption-side="top"}


Sie können auch Statistikdaten auf der Seite 'Discover' ansehen:
* Sie können Statistiken pro Feld anzeigen. 
* Sie können Statistiken im Histogramm pro konfigurierter Zeitmarke (`@timestamp`) anzeigen.

Weitere Informationen finden Sie unter [Statistiken zu Felddaten anzeigen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_fields_stats).

**Hinweis:** Die Daten, die in der Tabelle und im Histogramm angezeigt werden, sind statisch. Wenn Sie immer wieder die neuesten Einträge anzeigen wollen, müssen Sie ein Aktualisierungsintervall festlegen. 


## Feldspalte einer Tabelle hinzufügen
{: #discover_add_fields_to_table}

Die Tabelle, die zur Analyse von Daten auf der Seite 'Discover' verfügbar ist, enthält standardmäßig die folgenden Felder:
* **time:** Dieses Feld gibt an, wann der Eintrag erfasst und in {{site.data.keyword.Bluemix_notm}} aufgezeichnet wurde.
* **_source:** Dieses Feld enthält die Originaldaten des Eintrags.

Sie können der Tabelle durch eine der folgenden Optionen eine Feldspalte hinzufügen:

* Fügen Sie eine Feldspalte aus der Feldliste ('Fields') hinzu, die auf der Seite verfügbar ist.

    1. Suchen Sie auf der Seite 'Discover' das Feld im Abschnitt `Selected Fields`.
    2. Setzen Sie den Mauszeiger auf ein Feld in der Feldliste.
    3. Klicken auf **Add**, um ein Feld hinzuzufügen.
    
 * Fügen Sie eine Feldspalte in der Tabellenansicht eines erweiterten Eintrags hinzu.

    1. Erweitern Sie einen Eintrag in der Tabelle.
    2. Suchen Sie in der Tabellenansicht das Feld, das Sie hinzufügen wollen.
    3. Klicken Sie auf das Symbol **Toggle Column in table** ![Toggle column in table](images/toggle_field_icon.jpg "Toggle column image").
    

**Hinweis:** Wenn Sie der Tabelle zum ersten Mal eine Feldspalte hinzufügen, wird die in der Tabelle angezeigte Feldspalte *_source* ausgeblendet. Das Feld *_source* zeigt den Wert jedes einzelnen Felds für jeden Protokolleintrag. Wenn Sie andere Feldwerte für einen Protokolleintrag in der Tabelle anzeigen wollen, nachdem Sie der Tabelle eine Spalte hinzugefügt haben, zeigen Sie die Registerkarte für die Tabellenansicht ('Table') oder die Registerkarte 'JSON' für den jeweiligen Eintrag an.


## Datenansicht automatisch aktualisieren
{: #discover_view_refresh_interval}

In {{site.data.keyword.Bluemix_notm}} ist das Zeitintervall für automatisches Aktualisieren (*Auto-refresh*) standardmäßig inaktiviert (**OFF**) und die Daten, die in Kibana angezeigt werden, entsprechen den letzten 15 Minuten seit dem Start von Kibana. Die 15 Minuten entsprechen dem Zeitfilter, der vorkonfiguriert ist. Sie können diesen Zeitfilter ändern, indem Sie ein anderes Zeitintervall festlegen. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

Führen Sie die folgenden Schritte aus, um ein Zeitintervall für automatisches Aktualisieren (*Auto-refresh*) festzulegen:

1. Klicken Sie in der Menüleiste der Seite 'Discover' auf das Zeitauswahlfeld (Time Picker) ![Time Picker](images/time_picker_icon.jpg "Time Picker").

2. Wählen Sie die Schaltfläche für automatisches Aktualisieren ![Schaltfläche für automatisches Aktualisieren](images/auto_refresh_icon.jpg "Schaltfläche für automatisches Aktualisieren") aus.

3. Wählen Sie ein Aktualisierungsintervall aus.

    Gültige Werte sind *Inaktiv* (Off), *5 Sekunden*, *10 Sekunden*, *30 Sekunden*, *45 Sekunden*, *1 Minute*, *5 Minuten*, *15 Minuten*, *30 Minuten*, *1 Stunde*, *2 Stunden*, *12 Stunden*, *1 Tag*. 

Sie können das Aktualisierungsintervall anhalten, indem Sie auf die Pauseschaltfläche ![Pauseschaltfläche](images/auto_refresh_pause_icon.jpg "Pause") klicken. 


## Auf der Seite 'Discover' angezeigte Daten ermitteln
{:#identify_data}

Bei der Analyse der {{site.data.keyword.Bluemix_notm}}-Protokollen in Kibana hängen die angezeigten Daten von der Art und Weise, wie Sie Kibana starten, vom konfigurierten Indexmuster (Index Pattern) und von angepassten Abfragen und Filtern ab, die Sie angewendet haben.

Berücksichtigen Sie die folgenden Informationen, um die Daten zu ermitteln, die in der Tabelle und im Histogramm der Seite 'Discover' verfügbar sind:

1. Prüfen Sie das Indexmuster auf der Seite **Management**.

    Das Indexmuster (Index Pattern) definiert die Suchabfrage, die standardmäßig angewendet wird, um Einträge auf Ihren Kibana-Seiten anzuzeigen. Das Indexmuster ist standardmäßig vorkonfiguriert und so eingestellt, dass alle Daten, die in einem Bereich verfügbar sind, erfasst werden. Beispiel:

    * Wenn Sie Kibana von der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle aus starten (d. h. vom Abschnitt *Protokoll* der Benutzerschnittstellenseiten einer bestimmten Ressource, wie z. B. einer Cloud Foundry-Anwendung (CF-Anwendung) oder eines Containers), schließt das Indexmuster, das angewendet wird, alle Einträge ein, die in dem Bereich verfügbar sind.
    
    * Wenn Sie Kibana in einem Browser oder über das Dashboard des {{site.data.keyword.loganalysisshort}}-Service starten, schließt das Indexmuster, das angewendet wird, alle Einträge ein, die in dem Bereich, den Kibana anzeigt, verfügbar sind, an dem Sie angemeldet sind.
        
2. Überprüfen Sie die Abfrage auf der Seite 'Discover'.  

    Die Abfrage, die auf der Seite 'Discover' angezeigt wird, dient zum Filtern der Einträge, die standardmäßig zur Analyse verfügbar sind. Beispiel:

    * Wenn Sie eine Zeichenfolge in die Suchleiste eingeben, durchsucht die Abfrage alle Felder nach dieser Zeichenfolge.
    
    * Wenn als Abfrage die Zeichenfolge `application_id:<GUID>` angegeben wird, wobei *GUID* die ID einer CF-App ist, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die für diese CF-App in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
    * Wenn als Abfrage die Zeichenfolge `instance_id:<GUID>` angegeben wird, wobei *GUID* die ID einer Containerinstanz ist, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die für diesen Container in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
    * Wenn als Abfrage die Zeichenfolge `instance_id:<GUID> AND instance_id:<GUID>` angegeben wird, wobei *GUID* die ID einer Containerinstanz ist, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die für diese Containergruppe in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
   
    * Wenn als Abfrage das Zeichen `*` angegeben wird, werden die Daten auf alle Einträge gesetzt, die in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
    * o	Wenn als Abfrage die Zeichenfolge `application_id:<GUID> AND message:"MEIN_Suchtext"` angegeben wird, wobei *GUID* die ID einer CF-App ist und *MEIN_Suchtext* die Zeichenfolge ist, nach der Sie suchen wollen, entsprechen die Einträge, die angezeigt werden, allen Einträgen, die *MEIN_Suchtext* im Nachrichtenfeld für diese CF-App-Einträge enthalten, die in dem Bereich verfügbar sind, der im Indexmuster konfiguriert ist.
    
3. Überprüfen Sie die Feldfilter, die auf Ihre Abfrage auf der Seite 'Discover' angewendet werden.

    Sie können Feldfilter definieren, um Einträge auf der Basis des Werts des Felds umzuschalten. Wenn zum Beispiel ein Feldfilter aktiviert ist, entsprechen die Einträge, die angezeigt werden, Einträgen, in denen der Wert dieses Felds übereinstimmt.
    

## Einträge nach Wert eines indexierten Felds anordnen 
{: #discover_sort_by_table}

Sie können nur Einträge in der Tabelle nach Feldern sortieren, die indexiert werden.

Um zu ermitteln, welche Felder indexiert sind, führen Sie die folgenden Schritte aus:

1. Klicken Sie auf der Seite 'Discover' auf das Symbol 'Konfigurieren' ![Konfigurationssymbol](images/configure_icon.jpg "Konfigurationssymbol"), das im Abschnitt **Selected Fields** der Seite enthalten ist.

2. Wählen Sie zum Ermitteln der Felder, die indexiert sind, die Option **Yes** für das Suchfeld **Indexed** aus.

    Die Liste der indexierten Felder wird angezeigt.
 
Führen Sie die folgenden Schritte aus, um die Einträge in der Tabelle nach den Werten eines indexierten Felds zu sortieren: 

1. Bewegen Sie den Mauscursor über den Namen des Felds in der Tabelle, nach dem Sie die Daten sortieren wollen. Die verschiedenen Aktionsschaltflächen werden angezeigt.
2. Klicken Sie auf die Sortierschaltfläche für das Feld, nach dem Sie die Daten sortieren wollen. Klicken Sie ein zweites Mal auf das Sortiersymbol für das Feld, wenn Sie die Sortierreihenfolge umkehren wollen.

**Hinweis:** Wenn Sie nach einem Zeitfeld sortieren, werden die Einträge standardmäßig in umgekehrt chronologischer Reihenfolge angezeigt. Die neuesten Einträge werden zuerst angezeigt.


## Feldspalten in der Tabelle neu anordnen
{: #discover_rearrange_fields_in_table}

Sie können die Feldspalten in der Tabelle neu anordnen. Setzen Sie den Mauscursor auf die Überschrift der Spalte, die Sie verschieben wollen, und klicken Sie auf die Schaltfläche **Move column to the left** (Spalte nach links verschieben) oder **Move column to the right** (Spalte nach rechts verschieben).


## Feldliste neu laden
{: #discover_view_reload_fields}

Führen Sie die folgenden Schritte aus, um die Feldliste erneut zu laden, die in Kibana angezeigt wird:

1. Wählen Sie die Seite **Management** und dann **Index Patterns** aus, um die verfügbaren Indizes aufzulisten.
   
2. Wählen Sie das Indexmuster aus, um jedes Feld und den zugeordneten Kerntyp des Felds, wie von Elasticsearch aufgezeichnet, anzuzeigen. 

3. Klicken Sie auf die Schaltfläche *Reload field list* ![Reload field list](images/reload_field_list_icon.jpg "Reload field list"), um die Indexmusterfelder erneut zu laden. 

Die Feldliste wird aktualisiert.


## Feldspalten aus der Tabelle entfernen
{: #discover_remove_fields_from_table}

Führen Sie die folgenden Schritte aus, um Felder aus der Tabelle zu entfernen:

1. Suchen Sie in der Tabelle das Feld, das Sie aus der Tabellenansicht entfernen möchten.
2. Klicken Sie auf **Remove column**.
    

## Eintrag in der Tabelle anzeigen
{: #discover_view_entry_in_table}

Klicken Sie zum Anzeigen der Daten eines Eintrags in der Tabelle auf die Erweiterungsschaltfläche ![Erweiterungsschaltfläche](images/expand_icon.jpg "Erweiterungsschaltfläche") des Eintrags, den Sie analysieren wollen. 

Wählen Sie dann eine der folgenden Optionen aus, um die Daten anzuzeigen:

* Zum Anzeigen der Daten im Tabellenformat klicken Sie auf **Table**. Der Wert für jedes Feld wird angezeigt, das zur Analyse in einem Tabellenformat verfügbar ist. Für jedes Feld sind außerdem Filterschaltflächen und eine Umschaltfläche verfügbar.
* Zum Anzeigen der Daten im JSON-Format klicken Sie auf **JSON**.

## Statistiken zu Felddaten anzeigen
{: #discover_view_fields_stats}

Auf der Seite 'Discover' können Sie Statistiken für jedes Feld in der Feldliste *Fields* und im *Histogramm* anzeigen. 

In der Feldliste werden die folgenden Informationen angezeigt:
* Die Anzahl der Einträge in der Tabelle, die ein bestimmtes Feld enthalten.
* Die jeweils 5 höchsten Werte.
* Der Prozentsatz der Einträge, die die einzelnen Werte enthalten.

Im Histogramm werden die folgenden Informationen angezeigt:
* Anzahl der Einträge in einem Zeitbereich.

Zum Anzeigen der Statistiken im Histogramm klicken Sie auf eine Zeitmarke, um die Statistiken für diesen Zeitraum einzublenden. Zum Anzeigen der Statistiken zu einem Feld in der Feldliste klicken Sie auf den Namen. 


