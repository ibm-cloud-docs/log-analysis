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

# Protokolle in Kibana filtern
{:#k4_filter_logs}

Auf der Seite 'Discover' können Sie Suchabfragen erstellen und Filter anwenden, um die Informationen einzuschränken, die für die Analyse angezeigt werden.
{:shortdesc}

* Sie können eine oder mehr Suchabfragen in der Suchleiste der Seite 'Discover' definieren. Eine Suchabfrage definiert ein Subset von Protokolleinträgen. Verwenden Sie die Abfragesprache Lucene zum Definieren einer Suchabfrage. 

* Sie können Filter aus der *Feldliste* oder aus den Tabelleneinträgen hinzufügen. Ein Filter verfeinert die Datenauswahl durch Ein- oder Ausschließen von Informationen. Sie können einen Filter aktivieren oder inaktivieren, die Filteraktion umkehren, den Filter ein- und ausschalten oder ihn vollständig entfernen. 

Wenn Sie eine neue Suche definiert haben, können Sie sie speichern, um sie für eine spätere Analyse auf der Seite 'Discover' erneut zu verwenden oder um Visualisierungen zu erstellen, die Sie in angepassten Dashboards einsetzen können. 

Wenn Sie eine neue Suche ausführen, werden das Histogramm, die Tabelle und die Feldliste automatisch aktualisiert, sodass sie die Suchergebnisse anzeigen. Informationen darüber, welche Daten angezeigt werden, finden Sie unter [Auf der Seite 'Discover' angezeigte Daten ermitteln](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

Sie können angepasste Suchen zum Filtern Ihrer Protokolle erstellen. Die Szenarios in der folgenden Liste veranschaulichen, wie Sie Daten in Ihren Protokollen filtern:

* Sie können Ihr Protokoll nach Einträgen durchsuchen, die einen bestimmten Text in dem Wert eines Felds enthalten. Weitere Informationen finden Sie unter [Protokolle für einen bestimmten Text in einem Feldwert filtern](/docs/services/CloudLogAnalysis/kibana4/k4_filter_logs.html#k4_filter_logs_spec_text).
 
* Sie können Ihr Protokoll nach einem bestimmten Feldwert durchsuchen oder Einträge für einen bestimmten Feldwert aus dem Protokoll ausschließen. Weitere Informationen finden Sie unter [Protokolle für einen bestimmten Feldwert filtern](/docs/services/CloudLogAnalysis/kibana4/k4_filter_logs.html#k4_filter_logs_spec_field).
 
* Sie können Ihre Protokolle filtern, um Einträge innerhalb eines bestimmten Zeitraums anzuzeigen. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana4/k4_filter_logs.html#set_time_filter1).
     

## Filter für einen Wert hinzufügen, der nicht in der *Feldliste* enthalten ist
{:#k4_add_filter_out_value}

Um einen Filter für einen Wert hinzuzufügen, der nicht in der *Feldliste* angezeigt wird, suchen Sie mit einer Abfrage nach Datensätzen, die diesen Wert enthalten. Fügen Sie anschließend den Filter aus dem Tabelleneintrag hinzu, der auf der Seite 'Discover' verfügbar ist. 

Führen Sie die folgenden Schritte aus, um einen Filter für einen Wert hinzuzufügen, der nicht in der Liste enthalten ist, die im Abschnitt *Feldliste* angezeigt wird:

1. Prüfen Sie auf der Kibana-Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

    Die folgende Abbildung zeigt beispielsweise die Werte von Instanzen für eine CF-App in der *Feldliste*. 
    
    ![Werte in der Feldliste anzeigen](images/k4_add_filter_f1.jpg "Werte in der Feldliste anzeigen")
    
    Sie sind an der Instanznummer *3* interessiert, diese ist jedoch nicht in der angezeigten Liste enthalten.

2. Ändern Sie auf der Seite 'Discover' die Abfrage, um nach einem bestimmten Feldwert zu suchen.

    Beispiel: Um nach Instanz *3* zu suchen, geben Sie folgende Abfrage ein:
   `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:"3"`
    
    ![Abfrage ändern](images/k4_add_filter_f2.jpg "Abfrage ändern")
    
    In der Tabelle sehen Sie alle Datensätze, die mit Ihrer Abfrage übereinstimmen. 
    
 3. Erweitern Sie einen Datensatz und wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") aus, um einen Filter hinzuzufügen.
 
     Um beispielsweise einen Filter für die Instanz-ID mit dem Wert *3* hinzuzufügen, klicken Sie neben dem Feld mit der *Instanz-ID* auf die Schaltfläche mit der Lupe ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus").
     
     ![Tabelle anzeigen](images/k4_add_filter_f3.jpg "Tabelle anzeigen")
     
4. Überprüfen Sie, ob der Filter hinzugefügt wurde.

    Die folgende Abbildung zeigt beispielsweise den aktivierten Filtern, nachdem Sie ihn aus der Tabelle hinzugefügt haben.
    
    ![Filter anzeigen](images/k4_add_filter_f4.jpg "Filter anzeigen")
    
    


## Protokolle für einen bestimmten Feldwert filtern
{:#k4_filter_logs_spec_field}

Sie können nach Einträgen suchen, die einen bestimmten Feldwert enthalten. 

Führen Sie die folgenden Schritte aus, um nach Einträgen zu suchen, die einen bestimmten Feldwert enthalten:

1. Prüfen Sie auf der Kibana-Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

2. Geben Sie in der *Feldliste* das Feld an, für das Sie einen Filter definieren möchten, und klicken Sie darauf.

    Für das Feld werden maximal fünf Werte angezeigt. Jeder Wert hat zwei Lupenschaltflächen. 
    
    Wenn Sie den Wert nicht finden, gehen Sie entsprechend den Anweisungen unter [Filter für einen Wert hinzufügen, der nicht in der Feldliste enthalten ist](/docs/services/CloudLogAnalysis/kibana4/k4_filter_logs.html#k4_add_filter_out_value) vor.

3. Um einen Filter hinzuzufügen, der nach Einträgen in einem Feldwert sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") für diesen Wert aus.

    ![Filter mit dem Feldwert](images/k4_add_filter_for_field.jpg "Filter mit dem Feldwert")

    Um einen Filter hinzuzufügen, der nach Einträgen sucht, die diesen Feldwert nicht enthalten, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") für den Wert aus.

    ![Filter, der den Feldwert ausschließt](images/k4_add_filter_to_exclude_field.jpg "Filter, der den Feldwert ausschließt")

4. Wählen Sie eine der folgenden Optionen aus, um in Kibana mit Filtern zu arbeiten:

    <table>
      <caption>Tabelle 1. Methoden für den Einsatz von Filtern</caption>
      <tbody>
        <tr>
          <th align="center">Option</th>
          <th align="center">Beschreibung</th>
          <th align="center">Zusätzliche Information</th>
        </tr>
        <tr>
          <td align="left">Enable</td>
          <td align="left">Wählen Sie diese Option aus, um einen Filter zu aktivieren.</td>
          <td align="left">Wenn Sie einen Filter hinzufügen, wird er automatisch aktiviert. <br> Wenn ein Filter inaktiviert ist, klicken Sie ihn an, um ihn zu aktivieren.</td>
        </tr>
        <tr>
          <td align="left">Disable</td>
          <td align="left">Wählen Sie diese Option aus, um einen Filter zu inaktivieren.</td>
          <td align="left">Wenn Sie nach dem Hinzufügen eines Filters Einträge für einen Feldwert ausblenden möchten, klicken Sie auf **Disable**.</td>
        </tr>
        <tr>
          <td align="left">Pin</td>
          <td align="left">Wählen Sie diese Option aus, damit der Filter über die Kibana-Seiten hinweg erhalten bleibt.</td>
          <td align="left">Sie können einen Filter auf der Seite *Discover*, der Seite *Visualize* oder der Seite *Dashboard* fixieren.</td>
        </tr>
        <tr>
          <td align="left">Toggle</td>
          <td align="left">Wählen Sie diese Option aus, um einen Filter ein- und ausschalten.</td>
          <td align="left">Standardmäßig werden die Einträge angezeigt, die mit einem Filter übereinstimmen. Um Einträge anzuzeigen, die nicht übereinstimmen, schalten Sie den Filter um.</td>
        </tr>
        <tr>
          <td align="left">Remove</td>
          <td align="left">Wählen Sie diese Option aus, um einen Filter zu entfernen.</td>
          <td align="left"></td>
        </tr>
      </tbody>
    </table>

## Protokolle der CF-App nach Quelle filtern
{:#k4_filter_logs_by_source}

Führen Sie die folgenden Schritte aus, um nach Einträgen zu suchen, die eine bestimmte Protokollquelle enthalten:

1. Prüfen Sie auf der Kibana-Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

2. Wählen Sie in der *Feldliste* das Feld **source_id** aus.

    ![Filterliste mit dem Feld für die Quellen-ID](images/k4_filter_sourceid_F1.jpg "Filterliste mit dem Feld für die Quellen-ID")     

3. Um einen Filter hinzuzufügen, der nach Einträgen mit einer bestimmten Quellen-ID (source_id) sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") für diesen Wert aus.

    Eine Liste der Protokollquellen, die für CF-Apps zur Verfügung stehen, finden Sie unter [Protokollquellen für CF-Apps](/docs/services/CloudLogAnalysis/cfapps/logging_cf_apps.html#cf_apps_log_sources_diego).

    Um beispielsweise einen Filter hinzuzufügen, der Protokolleinträge zum Starten, Stoppen oder Absturz einer CF-Anwendung einschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") aus, die für den Wert *CELL* im Abschnitt mit der *Feldliste* verfügbar ist. Die folgende Abbildung zeigt den Filter mit dem aktivierten Wert *CELL* für die Quellen-ID (source_id).
    
    ![Filter mit dem Feldwert](images/k4_filter_sourceid_F2.jpg "Filter mit dem Feldwert")

    Um einen Filter hinzuzufügen, der nach Einträgen ohne eine bestimmte Quellen-ID (source_id) sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") für den Wert aus.
    
    Um beispielsweise einen Filter hinzuzufügen, der Protokolleinträge zum Starten, Stoppen oder Absturz einer CF-Anwendung ausschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") aus, die für den Wert *CELL* im Abschnitt mit der *Feldliste* verfügbar ist. Die folgende Abbildung zeigt den Filter, der Einträge für den Wert *CELL* der Quellen-ID (source_id) ausschließt.

    ![Filter, der den Feldwert ausschließt](images/k4_filter_sourceid_F3.jpg "Filter, der den Feldwert ausschließt")


## Protokolle nach Protokolltyp filtern
{:#k4_filter_logs_by_log_type}

Führen Sie die folgenden Schritte aus, um nach Einträgen zu suchen, die einen bestimmten Protokolltyp enthalten:

1. Prüfen Sie auf der Kibana-Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

2. Wählen Sie in der *Feldliste* das Feld **type** aus.

    In der folgenden Abbildung steht beispielsweise nur ein Protokolltyp zur Verfügung: *syslog*
    
    ![Filterliste mit dem Protokolltyp](images/k4_filter_log_type_F1.jpg "Filterliste mit dem Protokolltyp")
   
3. Um einen Filter hinzuzufügen, der nach Einträgen für einen bestimmten Protokolltyp sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") für den Protokolltyp aus, den Sie analysieren wollen.

    Um beispielsweise einen Filter hinzuzufügen, der Protokolleinträge für *syslog* einschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") aus, die für den Wert *syslog* im Abschnitt mit der *Feldliste* verfügbar ist. Die folgende Abbildung zeigt den Filter, der Einträge für den Protokolltyp *syslog* einschließt.

    ![Filter mit Protokolltypeinträgen für 'syslog'](images/k4_filter_log_type_F2.jpg "Filter mit Protokolltypeinträgen für 'syslog'")

    Um einen Filter hinzuzufügen, der nach Einträgen ohne einen bestimmten Protokolltyp sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") für den Wert aus.

     Um beispielsweise einen Filter hinzuzufügen, der Protokolleinträge für *syslog* ausschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") aus, die für den Wert *syslog* im Abschnitt mit der *Feldliste* verfügbar ist. Die folgende Abbildung zeigt den Filter, der Einträge für den Protokolltyp *syslog* ausschließt.
     
     ![Filter, der Protokolltypeinträge für 'syslog' ausschließt](images/k4_filter_log_type_F3.jpg "Filter, der Protokolltypeinträge für 'syslog' ausschließt")


## Protokolle nach Instanz-ID filtern
{:#k4_filter_logs_by_instance_id}

Führen Sie die folgenden Schritte aus, um Ihre Protokolle im Kibana-Dashboard nach Instanz-ID anzuzeigen und zu filtern:

1. Prüfen Sie auf der Kibana-Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

2. Wählen Sie in der *Feldliste* eines der folgenden Felder aus, um nach einer bestimmten Instanz-ID zu suchen:

    * **instance_ID**: Dieses Feld enthält die verschiedenen Instanz-IDs, die im Protokoll für eine Cloud Foundry-Anwendung verfügbar sind. 
    * **instance**: Dieses Feld enthält die verschiedenen GUIDs aller Instanzen für eine Containergruppe. 

    Die folgende Abbildung zeigt beispielsweise unterschiedliche Werte für Instanzen für eine CF-App:
    
    ![Filterliste mit dem Feld für die Instanz-ID](images/k4_filter_instanceid_f1.jpg "Filterliste mit dem Feld für die Instanz-ID")
   
3. Um einen Filter hinzuzufügen, der nach Einträgen für einen bestimmten Protokolltyp sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") für den Protokolltyp aus, den Sie analysieren wollen.

   Um beispielsweise einen Filter hinzuzufügen, der Einträge für die CF-App-Instanz *2* einschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") aus, die für den Wert *2* im Abschnitt mit der Feldliste verfügbar ist. Die folgende Abbildung zeigt den Filter, der Einträge für die Instanz *2* einschließt.
    
    ![Filter, der Einträge des Typs 'instance_id' für Instanz 2 einschließt](images/k4_filter_instanceid_f2.jpg "Filter, der Einträge des Typs 'instance_id' für Instanz 2 einschließt")

    Um einen Filter hinzuzufügen, der nach Einträgen ohne eine bestimmte Instanz-ID sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") für den Wert aus.

     Um beispielsweise einen Filter hinzuzufügen, der Einträge für die CF-App-Instanz *2* ausschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") aus, die für den Wert *2* im Abschnitt mit der Feldliste verfügbar ist. Die folgende Abbildung zeigt den Filter, der Einträge für die Instanz *2* ausschließt.
     
      ![Filter, der Einträge des Typs 'instance_id' für Instanz 2 ausschließt](images/k4_filter_instanceid_f3.jpg "Filter, der Einträge des Typs 'instance_id' für Instanz 2 ausschließt")


## Protokolle der CF-App nach Nachrichtentyp filtern
{:#k4_filter_cf_logs_by_msg_type}

Führen Sie die folgenden Schritte aus, um nach Einträgen zu suchen, die einen bestimmten Nachrichtentyp enthalten:

1. Prüfen Sie auf der Kibana-Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

2. Wählen Sie in der *Feldliste* das Feld **message_type** aus.

    Die folgende Abbildung zeigt Werte aus dem Feld *message_type* in den Protokollen einer CF-App:
    
    ![Filterliste mit dem Feld für den Nachrichtentyp](images/k4_filter_by_msg_type_f1.jpg "Filterliste mit dem Feld für den Nachrichtentyp")     

3. Um einen Filter hinzuzufügen, der nach Einträgen mit einem bestimmten *message_type* sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") für diesen Wert aus.

    Um beispielsweise einen Filter hinzuzufügen, der Protokolleinträge mit dem Wert *OUT* für 'message_type' einschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Einschlussmodus](images/k4_include_field_icon.jpg "Lupenschaltfläche im Einschlussmodus") aus, die für den Wert *OUT* im Abschnitt mit der *Feldliste* verfügbar ist. Die folgende Abbildung zeigt den Filter mit dem aktivierten Wert *OUT* für den Nachrichtentyp (message_type).
    
    ![Filter mit dem Feldwert](images/k4_filter_by_msg_type_f2.jpg "Filter mit dem Feldwert")

    Um einen Filter hinzuzufügen, der nach Einträgen ohne einen bestimmten *message_type* sucht, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") für den Wert aus.
    
    Um beispielsweise einen Filter hinzuzufügen, der Protokolleinträge mit dem Wert *OUT* für 'message_type' ausschließt, wählen Sie die Lupenschaltfläche ![Lupenschaltfläche im Ausschlussmodus](images/k4_exclude_field_icon.jpg "Lupenschaltfläche im Ausschlussmodus") aus, die für den Wert *OUT* im Abschnitt mit der *Feldliste* verfügbar ist. Die folgende Abbildung zeigt den Filter, der Einträge für den Wert *OUT* des Nachrichtentyps (message_type) ausschließt.

    ![Filter, der den Feldwert ausschließt](images/k4_filter_by_msg_type_f3.jpg "Filter, der den Feldwert ausschließt")


## Protokolle für einen bestimmten Text in einem Feldwert filtern
{:#k4_filter_logs_spec_text}

Sie können Einträge anzeigen und suchen, die einen bestimmten Text im Wert eines Felds enthalten. 

**Hinweis:** Eine freie Textsuche können Sie nur für Zeichenfolgefelder ausführen, die von Elasticsearch Analyzer analysiert werden. 
    
Wenn Elasticsearch den Wert einer Zeichenfolgefelds analysiert, teilt es den Text an den Wortgrenzen (wie vom Unicode Consortium definiert), entfernt Interpunktionszeichen und wandelt alle Wörter in Kleinschreibung um.
    
Führen Sie die folgenden Schritte aus, um nach Einträgen suchen, die bestimmten Text in einem Feldwert enthalten:

1. Prüfen Sie auf der Kibana-Seite 'Discover', welches Subset Ihrer Daten angezeigt wird. Weitere Informationen finden Sie unter [Daten ermitteln, die auf Ihrer Kibana-Seite 'Discover' angezeigt werden](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#k4_identify_data).

2. Geben Sie die Felder an, die standardmäßig in Elasticsearch analysiert werden.

    Um die vollständige Liste der analysierten Felder anzuzeigen, die für das Suchen und Filtern von Protokolldaten zur Verfügung stehen, [laden Sie die Liste der Felder neu](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_view_reload_fields). Führen Sie anschließend in der *Feldliste* auf der Seite 'Discover' die folgenden Schritte aus:
    
    1. Klicken Sie auf das Konfigurationssymbol ![Konfigurationssymbol](images/k4_configure_icon.jpg "Konfigurationssymbol"). Der Abschnitt **Selected Fields**, in dem Sie filtern können, wird angezeigt.

        ![Konfigurationsabschnitt mit Feldern mit bestimmten Attributen](images/k4_reset_filters.jpg "Konfigurationsabschnitt mit Feldern mit bestimmten Attributen")
    
    2. Wählen Sie zum Ermitteln der Felder, die analysiert sind, die Option **Yes** für das Suchfeld **Analyzed** aus.

        ![Analysiertes Attribut](images/k4_reset_filters_analyze_options.jpg "Analysiertes Attribut")
    
        Die Liste der analysierten Felder wird angezeigt.
    
        ![Liste der analysierten Felder](images/k4_list_analyzed_fields.jpg "Liste der analysierten Felder")
        
         
    3. Überprüfen Sie, ob das Feld, in dem Sie nach freiem Text suchen wollen, ein Feld ist, das von Elasticsearch standardmäßig analysiert wird.
    
3. Wenn das Feld analysiert wird, ändern Sie die Abfrage so, dass Einträge in den Protokollen gesucht werden, die freien Text als Teil des Werts eines Felds enthalten.

    
**Beispiel**

Wenn Sie Kibana für eine Cloud Foundry-Anwendung über die {{site.data.keyword.Bluemix}}-Benutzerschnittstelle starten und nach einer bestimmten Nachricht suchen wollen, die die Nachrichten-ID *CWWKT0016I:* enthält, ändern Sie die Suche so, dass sie den freien Text enthält.
    
1. Überprüfen Sie die geladene Suchabfrage und die angezeigten Daten auf der Seite 'Discover'.
       
    ![Standardsuchabfrage](images/k4_filter_by_text_default_query.jpg "Standardsuchabfrage")
        
2. Um nach der Nachrichten-ID *CWWKT0016I* zu suchen, ändern Sie die Suchabfrage und drücken Sie die **Eingabetaste**.
    
    <pre class="pre">application_id:f52f6016-3aab-4b5c-aa2e-5493747cb978 AND message:"CWWKT0016I:" </pre>
        
    ![Abfrage ändern](images/k4_filter_by_text_modify_query.jpg "Abfrage ändern")
      
Die Tabelle enthält Einträge für Ihre CF-App für die Fälle, in denen der Text *CWWKT0016I* in dem Wert im Feld *message* enthalten ist.
    
![Neue Suchansicht](images/k4_filter_by_text_result_query.jpg "Neue Suchansicht")     	
        

## Zeitfilter festlegen
{: #set_time_filter1}

Sie können Protokolle für einen bestimmten Zeitraum anzeigen und filtern, indem Sie die Funktion *Time Picker* konfigurieren.

Sie können die Funktion *Time Picker* auf der Seite 'Discover' konfigurieren. Standardmäßig ist die Funktion auf die letzten 15 Minuten eingestellt. 

Führen Sie die folgenden Schritte aus, um nach Einträgen zu suchen, die eine bestimmte Zeitangabe enthalten:

1. Klicken Sie in der Menüleiste der Seite 'Discover' auf das Zeitauswahlfeld (Time Picker) ![Time Picker](images/k4_time_picker_icon.jpg "Time Picker").

2. Richten Sie das Zeitintervall ein. 

    Sie können eines der folgenden Zeitintervalle definieren:
    
    * Quick: Dies sind vordefinierte Zeitintervalle, die die am häufigsten verwendeten Zeitintervalle des Typs 'Relative' und 'Absolute' umfassen, z. B. *Today* (Heute) und *This Month* (Diesen Monat). 
    
        !['Quick'-Optionen für das Zeitauswahlfeld](images/k4_time_picker_quick.jpg "'Quick'-Optionen für das Zeitauswahlfeld")
    
    * Relative: Dies sind Zeitintervalle, bei denen Sie das Startdatum und die Startzeit sowie das Enddatum und die Endzeit angeben können. Es kann jeweils auf die Stunde gerundet werden.
    
        !['Relative'-Optionen für das Zeitauswahlfeld](images/k4_time_picker_relative.jpg "'Relative'-Optionen für das Zeitauswahlfeld")
    
    * Absolute: Dies sind die Zeitintervalle zwischen einem Startdatum und einem Enddatum.
    
        !['Absolute'-Optionen für das Zeitauswahlfeld](images/k4_time_picker_absolute.jpg "'Absolute'-Optionen für das Zeitauswahlfeld")
      

Wenn Sie ein Zeitintervall konfiguriert haben, entsprechen die in Kibana gezeigten Daten den Einträgen in diesem Zeitraum.








