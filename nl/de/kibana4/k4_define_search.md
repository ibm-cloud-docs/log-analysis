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

# Angepasste Suchabfragen definieren
{:#k4_define_search}

In der Suchleiste der Seite 'Discover' können Sie Suchabfragen mithilfe der Abfragesprache Lucene definieren und speichern. Für jede Suche können Sie Filter anwenden, um die Einträge einzugrenzen, die für die Analyse verfügbar sind.
{:shortdesc}

Führen Sie folgende Schritte aus, um eine angepasste Suche zu definieren:

1. Starten Sie Kibana.

    Führen Sie für CF-Apps (Cloud Foundry) oder Container, die in der von {{site.data.keyword.Bluemix}} verwalteten Cloudinfrastruktur ausgeführt werden, die folgenden Schritte aus:
    
    1. Greifen Sie auf die Registerkarte **Protokolle** der CF-App (Cloud Foundry) oder des Containers zu. 

        Klicken Sie im {{site.data.keyword.Bluemix_notm}}-Dashboard auf den App-Namen oder Container. Klicken Sie dann für CF-Apps auf die Registerkarte **Protokolle**; für Container klicken Sie auf die Registerkarte **Überwachung und Protokolle** und wählen die Registerkarte **Protokollierung** aus. Die Protokolle werden angezeigt.

    2. Greifen Sie auf Kibana zu. Klicken Sie dazu auf **Erweiterte Ansicht** ![Link für erweiterte Ansicht](images/logging_advanced_view.jpg "Link für erweiterte Ansicht"). Das Kibana-Dashboard wird angezeigt.
    
    Für Container, die in einem Kubernetes-Cluster ausgeführt werden, [starten Sie Kibana über den Browser](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_browser1). 
    
    Wenn Sie auf Kibana zugreifen, wird die Standardsuche angewendet. Sie können die Protokolle für die Instanzenliste der Ressource anzeigen, für die Sie Kibana gestartet haben. Sie können die Protokolle für eine oder alle der {{site.data.keyword.Bluemix_notm}}-Ressourcen in diesem Bereich filtern.

2. Prüfen Sie auf der Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data). Ändern Sie anschließend die Standardabfrage zum Filtern der Einträge.

    **Hinweis** Verwenden Sie die Abfragesprache Lucene zum Definieren Ihrer angepassten Abfrage. Weitere Informationen finden Sie unter [Apache Lucene - Query Parser Syntax![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}.
    
    Wenn Kibana über {{site.data.keyword.Bluemix_notm}} gestartet wird, können Sie die logischen Operatoren **AND** und **OR** verwenden, um die Abfrage zu ändern und um verschiedene Suchkriterien zu definieren. Diese Operatoren müssen in Großbuchstaben geschrieben werden.    
    
    * Um nach einem Schlüsselwort bzw. einem Teil eines Schlüsselworts zu suchen, geben Sie ein Wort ein, gefolgt von einem Platzhaltersymbol \*; Beispiel: `Java*`. 
    * Um nach einem bestimmten Ausdruck zu suchen, geben Sie den Ausdruck in doppelten Anführungszeichen ein; Beispiel: `"Java/1.8.0"`.
    * Um komplexere Suchen zu erstellen, können Sie die logischen Operatoren AND und OR verwenden; `"Java/1.8.0" OR "Java/1.7.0"`.
    * Um in einem bestimmten Feld nach einem Wert zu suchen, geben Sie Ihre Suche in folgendem Format ein: *Protokollfeldname:Suchbegriff*; z. B. `instance_id:"1"`.
    * Um nach einem Wertebereich für ein bestimmtes Protokollfeld zu suchen, geben Sie Ihre Suche in folgendem Format ein: *Protokollfeldname:[Anfang_des_Bereichs TO Ende_des_Bereichs]*; z. B. `instance_id:["1" TO "2"]`.

     Beispiel: Für eine CF-App können Sie die Abfrage `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]` erstellen, die nur die Einträge für die Instanzen *0* und *1* auflistet. 

3. Speichern Sie die Abfrage, sodass Sie sie später wiederverwenden können. 




## Suche löschen
{: #k4_delete_search}

Führen Sie auf der Seite 'Settings' die folgenden Schritte aus, um eine Suche zu löschen:

1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.

2. Wählen Sie in der Registerkarte **Searches** die Suche aus, die Sie löschen wollen.

3. Klicken Sie auf **Delete**.


## Suche exportieren
{: #k4_export_search}

Führen Sie auf der Seite 'Settings' die folgenden Schritte aus, um eine Suche zu exportieren:

1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.

2. Wählen Sie in der Registerkarte **Searches** die Suche aus, die Sie exportieren wollen.

3. Klicken Sie auf **Export**.

4. Speichern Sie die Datei.

 
## Suche importieren
{: #k4_import_search}

Führen Sie auf der Seite 'Settings' die folgenden Schritte aus, um eine Suche zu importieren:

1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.

2. Wählen Sie in der Registerkarte **Searches** die Option **Import** aus.

3. Wählen Sie eine Datei aus und klicken Sie auf **Open**.

Die Suche wird zur Liste der Suchen hinzugefügt.

## Inhalt einer Suche aktualisieren
{: #k4_refresh_search}

Um den Inhalt einer Suche manuell zu aktualisieren, können Sie auf die Lupe klicken, die sich in der Suchleiste befindet. 

Um die Daten automatisch zu aktualisieren, die auf der Seite 'Discover' angezeigt werden, können Sie ein Aktualisierungsintervall konfigurieren. Der aktuelle Wert des Aktualisierungsintervalls wird in der Menüleiste der Seite 'Discover' angezeigt. Standardmäßig ist die automatische Aktualisierung auf **OFF** eingestellt.

Führen Sie die folgenden Schritte aus, um ein Aktualisierungsintervall festzulegen:

1. Klicken Sie auf der Seite 'Discover' auf **Time Filter** (in der Menüleiste).

2. Klicken Sie auf **Auto Refresh** ![Auto Refresh](images/k4_auto_refresh_icon.jpg "Auto Refresh").

3. Wählen Sie ein Aktualisierungsintervall aus der Liste aus. 

    ![Optionen für das Aktualisierungsintervall](images/k4_change_autorefresh.jpg "Optionen für das Aktualisierungsintervall")


**Hinweis**: Wenn Sie ein Intervall für die automatische Aktualisierung aktiviert haben, können Sie es anhalten, indem Sie auf die Schaltfläche 'Pause' klicken ![Pause](images/k4_auto_refresh_pause_icon.jpg "Pause").


## Suche neu laden
{: #k4_reload_search}

Führen Sie die folgenden Schritte aus, um eine gespeicherte Suche zu laden:

1. Klicken Sie in der Symbolleiste der Seite 'Discover' auf die Schaltfläche **Load Search** ![Load Search](images/k4_load_icon.jpg "Load Search").

2. Wählen Sie die Suche aus, die Sie laden wollen. 

## Neue Suche starten
{: #k4_new_search1}

Um eine neue Suche zu starten, klicken Sie in der Symbolleiste der Seite 'Discover' auf die Schaltfläche **New Search** ![New Search](images/k4_new_search_icon.jpg "New Search").

## Suche speichern 
{: #k4_save_search}

Wenn Sie eine Suche speichern, werden die Suchabfragezeichenfolge und das zu diesem Zeitpunkt ausgewählte Indexmuster gespeichert.

Führen Sie die folgenden Schritte aus, um die aktuelle Suche auf der Seite 'Discover' zu speichern:

1. Klicken Sie in der Symbolleiste der Seite 'Discover' auf die Schaltfläche **Save Search** ![Save Search](images/k4_save_search_icon.jpg "Save Search").

2. Geben Sie einen Namen für die Suche ein.

3. Klicken Sie auf 'Save'. 
