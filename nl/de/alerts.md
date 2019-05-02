---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, alerts

subcollection: LogDNA

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

 
# Mit Alerts arbeiten
{: #alerts}

Sie können einer Ansicht mindestens einen Alert zuordnen. Sie können mehrere Benachrichtigungskanäle für einen Alert definieren. Sie können Alerts stumm schalten. Sie können die Zuordnung zwischen einer Ansicht und Alerts aufheben.
{:shortdesc}

Sie können für einen Alert jede der folgenden Bedingungen konfigurieren:

* *Frequenz*: Geben Sie an, wie oft ein Alert ausgelöst werden soll. Gültige Werte: 30 Sekunden, 1 Minute, 5 Minuten, 15 Minuten, 30 Minuten, 1 Stunde, 6 Stunden, 12 Stunden, 24 Stunden.
* *Protokollzeilenzähler*: Geben Sie die Anzahl der Protokollzeilen an, die den Filter- und Suchkriterien der Ansicht entsprechen. Wenn die Anzahl der Protokollzeilen erreicht ist, wird ein Alert ausgelöst.

Sie können festlegen, ob beide Bedingungen überprüft werden oder nur eine Bedingung. Sind beide Bedingungen festgelegt, wird ein Alert ausgelöst, wenn einer der Schwellenwerte erreicht wird. 

Sie können beispielsweise einen Alert konfigurieren, der nach 30 Sekunden ausgelöst wird oder wenn 100 Protokollzeilen, die den Filter- und Suchkriterien der Ansicht entsprechen, erfasst wurden.

Sie können mehrere Benachrichtigungskanäle konfigurieren. Gültige Kanäle: `E-Mail`, `Slack`, `PagerDuty`, `Webhook`, `OpsGenie`, `Datadog`, `AppOptics`, `VictorOps`

Sie können auch eine **Voreinstellung** definieren. Eine Voreinstellung ist eine Alertvorlage, die Sie einer beliebigen Anzahl Ansichten zuordnen können. 

Damit Sie eine Alertkonfiguration für verschiedene Ansichten wiederverwenden können, konfigurieren Sie eine **Alertvoreinstellung**.
{: tip}

In der Ansicht wird ein Glockensymbol angezeigt, um zu signalisieren, dass dieser Ansicht ein Alert zugeordnet ist.



## Voreinstellung (Alertvorlage) konfigurieren
{: #config_preset}

Führen Sie die folgenden Schritte aus, um eine Voreinstellung zu konfigurieren:

1. Wählen Sie das Symbol **Konfiguration** aus ![Konfigurationssymbol](images/admin.png "Verwaltungssymbol").
2. Wählen Sie **Alerts** aus.
3. Wählen Sie **Voreingestellten Alert hinzufügen** aus.
4. Wählen Sie einen Benachrichtigungskanal aus. 
5. Definieren Sie die Schwellenwertbedingungen.

    1. Wählen Sie eine Frequenz aus. Zum Beispiel 12 Stunden.

    2. Geben Sie die Anzahl Protokollzeilen ein, nach denen der Alert ausgelöst werden soll.

    3. Wählen Sie aus, ob beide Bedingungen überprüft werden sollen oder nur eine Bedingung.

6. Fügen Sie die Details für den ausgewählten Benachrichtigungskanal hinzu.

    Fügen Sie beispielsweise für den E-Mail-Benachrichtigungskanal mindestens einen Empfänger und wahlweise eine Zeitzone hinzu.

7. Klicken Sie auf **Alert speichern**.



## Alert mit einer Voreinstellung konfigurieren
{: #config_alert_preset}

Führen Sie die folgenden Schritte aus, um einer Ansicht eine Voreinstellung zuzuordnen:

1. Klicken Sie auf das Symbol **Ansichten** ![Konfigurationssymbol](images/views.png).
2. Erstellen Sie eine Ansicht. 

    Wenden Sie einen Zeitrahmen, Filter und Suchkriterien an, um die in der Ansicht angezeigten Protokollzeilen zu filtern. 

    Weitere Informationen finden Sie im Abschnitt [Ansichten erstellen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Klicken Sie auf den Ansichtsnamen. Wählen Sie dann **Alert zuordnen** aus.

4. Wählen Sie eine Voreinstellung aus, um eine Alertdefinition wiederzuverwenden. 

5. Klicken Sie auf **Alert speichern**. 




## Ansichtsspezifischen Alert konfigurieren
{: #config_alert_view}

Führen Sie die folgenden Schritte aus, um einer Ansicht einen Alert zuzuordnen:

1. Klicken Sie auf das Symbol **Ansichten** ![Konfigurationssymbol](images/views.png).
2. Erstellen Sie eine Ansicht. 

    Wenden Sie einen Zeitrahmen, Filter und Suchkriterien an, um die in der Ansicht angezeigten Protokollzeilen zu filtern. 

    Weitere Informationen finden Sie im Abschnitt [Ansichten erstellen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Klicken Sie auf den Ansichtsnamen. Wählen Sie dann **Alert zuordnen** aus.

4. Wählen Sie **Ansichtsspezifischer Alert** aus.

5. Wählen Sie einen Benachrichtigungskanal aus. 

6. Definieren Sie die Schwellenwertbedingungen.

    1. Wählen Sie eine Frequenz aus. Zum Beispiel 12 Stunden.

    2. Geben Sie die Anzahl Protokollzeilen ein, nach denen der Alert ausgelöst werden soll.

    3. Wählen Sie aus, ob beide Bedingungen überprüft werden sollen oder nur eine Bedingung.

7. Fügen Sie die Details für den ausgewählten Benachrichtigungskanal hinzu.

    Fügen Sie beispielsweise für den E-Mail-Benachrichtigungskanal mindestens einen Empfänger und wahlweise eine Zeitzone hinzu.

8. Klicken Sie auf **Alert speichern**.



## Voreinstellung (Alertvorlage) löschen
{: #delete_preset}

Führen Sie die folgenden Schritte aus, um eine Voreinstellung zu löschen:

1. Wählen Sie das Symbol **Konfiguration** aus ![Konfigurationssymbol](images/admin.png "Verwaltungssymbol").
2. Wählen Sie **Alerts** aus.
3. Berühren Sie die Schaltfläche *Bearbeiten* der Voreinstellung, die Sie löschen wollen, mit dem Mauscursor. Die Option *Löschen* wird angezeigt.
4. Wählen Sie **Löschen** aus.
5. Bestätigen Sie das Löschen der Voreinstellung. Klicken Sie auf **Löschen**.

## Zuordnung zwischen einem ansichtsspezifischen Alert und einer Ansicht aufheben
{: #delete_alert}

Führen Sie die folgenden Schritte aus, um die Zuordnung einer Voreinstellung aufzuheben:

1. Wählen Sie das Symbol **Konfiguration** aus ![Konfigurationssymbol](images/admin.png "Verwaltungssymbol").
2. Wählen Sie **Alerts** aus.
3. Berühren Sie die Schaltfläche *Bearbeiten* des Alerts, den Sie löschen wollen, mit dem Mauscursor. Die Option *Löschen* wird angezeigt.
4. Wählen Sie **Zuordnung aufheben** aus.
5. Bestätigen Sie das Löschen des Alerts. Klicken Sie auf **Zuordnung aufheben**.



## Benachrichtigungskanäle
{: #channels}

Die folgende Tabelle enthält eine Auflistung der Benachrichtigungskanäle, die Sie konfigurieren können, wenn ein Alert ausgelöst wird.

| Kanal           | Konfigurationsdetails | 
|-------------------|-----------------------|
| `E-Mail`             | Sie können mindestens eine E-Mail-Adresse konfigurieren.  | 
| `Slack`             | Sie können einen Slack-Kanal konfigurieren. |
| `Webhook`           | Sie können eine Webhook-URL konfigurieren. |
| `PagerDuty`         | Sie können Verbindungsdetails für Ihr PagerDuty-System konfigurieren und einen Service auswählen.|
| `OpsGenie`          | Sie können den API-Schlüssel für eine Verbindung zu Ihrem OpsGenie-System konfigurieren. |
| `Datadog`           | Sie können den API-Schlüssel für eine Verbindung zu Ihrem `Datadog`-System konfigurieren. |
| `AppOptics/Librato` | Sie können den API-Schlüssel für eine Verbindung zu Ihrem AppOptics/Librato-System konfigurieren. |
| `VictorOps`         | Sie können die URL konfigurieren, die benachrichtigt werden soll, wenn ein Alert ausgelöst wird, den Routing-Schlüssel und einen Alerttyp. Gültige Alerttypen: `info`, `warning`, `critical` |
{: caption="Benachrichtigungskanäle" caption-side="top"} 


