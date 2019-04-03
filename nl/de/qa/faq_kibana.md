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


# Kibana - Häufig gestellte Fragen
{: #faq_kibana}

Im Folgenden finden Sie Antworten auf häufig gestellte Fragen zur Verwendung der {{site.data.keyword.Bluemix}}-Protokollfunktionen. {:shortdesc}

* [Was kann ich tun, wenn auf der Seite 'Discover' in Kibana keine Daten angezeigt werden?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#logging_qa_no_data_discover_kibana)
* [Was kann ich tun, wenn ich eine Ausnahmebedingung bei der Authentifizierung erhalte?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#logging_qa_no_data_dashboard_kibana)
* [Warum werden Fragezeichensymbole (?) für Felder auf der Kibana-Seite 'Discover' angezeigt?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#logging_qa_kibana_question)
* [Wenn ich versuche, das Standardindexmuster zu ändern, wird Fehler 403 angezeigt.](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#error_403)
* [Kurz-URL funktioniert nicht](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#short_url)
* [Kann ich meine Kontoprotokolle in Bluemix durchsuchen?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-faq_kibana#acc_logs_1)


## Was kann ich tun, wenn auf der Seite 'Discover' in Kibana keine Daten angezeigt werden?
{: #logging_qa_no_data_discover_kibana}

Es können folgende Situationen entstehen, in denen keine Daten in Kibana angezeigt werden:

1. Beim Starten von Kibana werden keine Daten auf der Seite 'Discover' angezeigt. Sie erhalten die folgende Nachricht: **No results found.**. 
2. Sie arbeiten mit der Seite 'Discover' in Kibana. Nach kurzer Zeit erhalten Sie die Nachricht **No results found**, wenn Sie versuchen, eine Task in Kibana auszuführen.

Um das Problem zu beheben, führen Sie die folgenden Schritte aus:

1. Überprüfen Sie den *Time Picker* (Zeitauswahlfeld), der auf der Seite 'Discover' festgelegt ist, und geben Sie einen höheren Wert für den Zeitraum an. 

    **Hinweis**: Standardmäßig ist der *Time Picker* in {{site.data.keyword.Bluemix_notm}} so eingestellt, dass Daten für die letzten 15 Minuten angezeigt werden.

    Weitere Informationen zum Einstellen des *Time Picker* finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter1).
       
2. Klicken Sie auf die Lupe, die sich in der Suchleiste der Seite *Discover* befindet. Die Seitendaten werden auf der Basis der Standardsuchabfrage aktualisiert.

    Alternativ können Sie für den Zeitraum auch *Auto refresh* einstellen.

    **Hinweis:** In {{site.data.keyword.Bluemix_notm}} ist das Zeitintervall für automatisches Aktualisieren (*Auto-refresh*) standardmäßig inaktiviert (**OFF**).
    
    Informationen zum Aktivieren des Zeitintervalls finden Sie unter [Daten automatisch aktualisieren](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_refresh_interval).



## Was kann ich tun, wenn ich eine Ausnahmebedingung bei der Authentifizierung erhalte?
{: #logging_qa_no_data_dashboard_kibana}

Wenn keine Daten in Ihren Visualisierungen auf einer Dashboard-Seite angezeigt werden und Sie die Fehlernachricht **Error: Exception Authorization** erhalten, überprüfen Sie Ihre Berechtigungen zur Anzeige von Daten in den einzelnen Visualisierungen.

Beachten Sie Folgendes:
Sie können eine oder mehrere Visualisierungen in einer Dashboard-Seite konfigurieren. Wenn die Dashboard-Seite die Erfassung der angezeigten Daten über Visualisierungen anfordert, wird nur eine solche Anforderung für alle Visualisierungen ausgegeben. Wenn Ihnen die Berechtigung zur Anzeige der Daten einer der Visualisierungen fehlt, schlägt die Anforderung insgesamt fehl.

Um das Problem zu beheben, führen Sie die folgenden Schritte aus:

1. Ermitteln Sie die Visualisierungen, für die Sie nicht berechtigt sind.

    1. Klicken Sie auf das *Stiftsymbol* einer Visualisierung auf der Seite *Dashboard*. Die Visualisierung wird auf der Seite *Visualize* geöffnet. Alternativ können Sie eine Visualisierung auf der Seite *Visualize* laden. 
    2. Überprüfen Sie, ob Sie Daten anzeigen können.
    
    Wiederholen Sie diese Schritte für jede Visualisierung.

2. Fordern Sie bei Ihrem Cloudadministrator den gewünschten Zugriff auf Daten in Visualisierungen an.

3. Erstellen Sie eine neue Seite 'Dashboard', die die Visualisierungen ausschließt, für die Sie nicht berechtigt sind, während Sie Zugriff auf die Daten in den Visualisierungen erhalten, die das Problem verursachen. 

    Wenn Sie das Dashboard gemeinsam nutzen, löschen Sie die Visualisierungen nicht, da sich dies auf andere Teammitglieder auswirkt, die dasselbe Dashboard verwenden.



## Warum werden Fragezeichensymbole (?) für Felder auf der Kibana-Seite 'Discover' angezeigt?
{: #logging_qa_kibana_question}

Wenn Sie die Seite 'Discover' in Kibana öffnen, werden möglicherweise Fragezeichen (`?`) für Felder im Abschnitt für verfügbare Felder anstelle des Zeichens `t` angezeigt. Wenn Sie die Feldliste erneut laden, wird der Typ der Felder analysiert und die Zeichen `?` werden durch das Zeichen `t` ersetzt. Weitere Informationen finden Sie unter [Feldliste neu laden](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_reload_fields).


## Wenn ich versuche, das Standardindexmuster zu ändern, wird Fehler 403 angezeigt.
{: #error_403}

Das Standardindexmuster kann nicht geändert werden. 

Wenn Sie versuchen ein neues Indexmuster als neuen Standard festzulegen, wird der folgende Fehler angezeigt: `Config: Error 403 Forbidden`

## Kurz-URL funktioniert nicht
{: #short_url}

Die gemeinsame Nutzung von Suchen, Visualisierungen oder Dashboards wird nicht unterstützt. Daher funktionieren Kurz-URLs für Kibana-Objekte, die Sie freigeben möchten, auch nicht. 

## Kann ich meine Kontoprotokolle in Bluemix durchsuchen?
{: #acc_logs_1}

Als Kontoeigner können Sie Ihre Kontoprotokolle durchsuchen und analysieren.

Führen Sie die folgenden Schritte aus, um die Kontoprotokolle anzuzeigen:

1. [Starten Sie Kibana.](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser) Verwenden Sie beispielsweise für die Region 'USA (Süden)' die URL `https://logging.ng.bluemix.net`.

2. Wählen Sie die Option **View AccountName account Logs** aus, um die Kontoprotokolle anzuzeigen. *AccountName* ist der Name des Kontos.

