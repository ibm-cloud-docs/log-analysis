---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# Protokolle in lokale Datei exportieren
{: #export}

Sie können Protokolldaten im JSONL-Format aus einer {{site.data.keyword.la_full_notm}}-Instanz in eine lokale Datei exportieren. Sie können Protokolle programmgesteuert oder über die Webbenutzerschnittstelle von IBM Log Analysis exportieren. 
{:shortdesc}

Beim Exportieren von Protokolldaten sind die folgenden Informationen zu berücksichtigen:
* Sie exportieren eine Gruppe von Protokolleinträgen. Sie können Filter und Suchvorgänge anwenden, um die zu exportierende Datengruppe zu definieren. Darüber hinaus können Sie den Zeitbereich angeben. 
* Wenn Sie Protokolle über die Webbenutzerschnittstelle exportieren, wird eine E-Mail mit einem Link zu einer komprimierten Datei, die die Daten enthält, an Ihre E-Mail-Adresse gesendet. Zum Abrufen der Daten müssen Sie auf den Link klicken und die komprimierte Datei herunterladen.
* Wenn Sie Protokolle programmgesteuert exportieren, haben Sie die Wahl, eine E-Mail zu senden oder Protokolle per Streaming an das Terminal zu senden.
* Die komprimierte Protokolldatei, die die zu exportierenden Daten enthält, steht maximal 48 Stunden zur Verfügung. 
* Es können maximal 10.000 Zeilen exportiert werden.



## Protokolle über die Webbenutzerschnittstelle exportieren
{: #ui}

Führen Sie die folgenden Schritte aus, um Protokolldaten zu exportieren:

1. Klicken Sie auf das Symbol **Ansichten** ![Konfigurationssymbol](images/views.png).
2. Wählen Sie **Alles** oder eine Ansicht aus.
3. Wenden Sie einen Zeitrahmen, Filter und Suchkriterien an, bis die gewünschten Protokolleinträge angezeigt werden.
4. Klicken Sie auf **Nicht gespeicherte Ansicht**, wenn Sie mit der Ansicht **Alles** beginnen. Klicken Sie auf den Namen Ihrer Ansicht, wenn Sie im vorherigen Schritt eine Ansicht ausgewählt haben.
5. Wählen Sie `Zeilen exportieren` aus. Ein neues Fenster wird geöffnet.
6. Überprüfen Sie den Zeitbereich. Wenn Sie eine Änderung vornehmen müssen, klicken Sie auf den vordefinierten Zeitbereich im Feld zur Änderung des Zeitbereichs für den Export. **
7. Für den Fall, dass die Exportanforderung die Zeilenbegrenzung überschreitet, wählen Sie **Neuere Zeilen beibehalten** oder **Ältere Zeilen beibehalten** aus.
8. Überprüfen Sie Ihre E-Mail. Sie erhalten eine E-Mail von **LogDNA**, die einen Link zum Herunterladen Ihrer exportierten Zeilen enthält.


## Protokolle mithilfe der API programmgesteuert exportieren
{: #api}

Führen Sie die folgenden Schritte aus, um Protokolle programmgesteuert zu exportieren:

1. Generieren Sie einen Serviceschlüssel. 

    **Anmerkung:** Sie müssen über die Rolle **Manager** für die Instanz oder den Service von {{site.data.keyword.la_full_notm}} verfügen, um diesen Schritt ausführen zu können. Weitere Informationen finden Sie in [Berechtigungen zum Verwalten von Protokollen und zum Konfigurieren von Alerts in LogDNA erteilen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

    1. Starten Sie die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}}. Weitere Informationen finden Sie in [Zur Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} navigieren](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

    2. Wählen Sie das Symbol **Konfiguration** aus ![Konfigurationssymbol](images/admin.png). Wählen Sie dann **Organisation** aus. 

    3. Wählen Sie **API-Schlüssel** aus.

        Die erstellten Serviceschlüssel werden angezeigt. 

    4. Klicken Sie auf **Serviceschlüssel erstellen**.

        Der Liste wird ein neuer Schlüssel hinzugefügt. Kopieren Sie diesen Schlüssel.

2. Exportieren Sie Protokolle. Führen Sie den folgenden cURL-Befehl aus:

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    Hierbei gilt Folgendes: 

    * ENDPOINT gibt den Einstiegspunkt für den Service an. Jede Region verfügt über eine andere URL.
    * QUERY_PARAMETERS sind Parameter, die die die Filterkriterien definieren, die auf die Exportanforderung angewendet werden.
    * SERVICE_KEY ist der im vorherigen Schritt erstellte Serviceschlüssel.

Die folgende Tabelle enthält eine Auflistung der Endpunkte nach Region.

| Region         | Endpunkt                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="Endpunkte nach Region" caption-side="top"} 


Die folgende Tabelle enthält eine Auflistung der Abfrageparameter, die Sie festlegen können.

| Abfrageparameter | Typ       | Status     | Beschreibung |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | Erforderlich   | Startzeit. Eine UNIX-Zeitmarke in Sekunden oder Millisekunden. |
| `to`        | `int32`      | Erforderlich   | Endzeit. Eine UNIX-Zeitmarke in Sekunden oder Millisekunden.    |
| `size`      | `string`     | Optional   | Anzahl der zu exportierenden Protokollzeilen.  | 
| `hosts`     | `string`     | Optional   | Durch Kommas getrennte Liste der Hosts. |
| `apps`      | `string`     | Optional   | Durch Kommas getrennte Liste der Anwendungen. |
| `levels`    | `string`     | Optional   | Durch Kommas getrennte Liste der Protokollebenen. |
| `query`     | `string`     | Optional   | Suchabfrage. Weitere Informationen finden Sie in [Protokolle durchsuchen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6). |
| `prefer`    | `string`     | Optional   | Definiert die Protokollzeilen, die exportiert werden sollen. Gültige Werte: `head` (erste Protokollzeilen) und `tail` (letzte Protokollzeilen). Der Standardwert ist 'tail'.  |
| `email`     | `string`     | Optional   | Gibt die E-Mail mit dem Download-Link Ihres Exports an. Die Protokollzeilen werden standardmäßig gestreamt.|
| `emailSubject` | `string`     | Optional   | Dient zur Angabe des Betreffs der E-Mail. </br>Verwenden Sie `%20` für ein Leerzeichen. Zum Beispiel `Protokolle%20exportieren`. |
{: caption="Abfrageparameter" caption-side="top"} 

Sie können beispielsweise den folgenden Befehl ausführen, um Protokollzeilen per Streaming an das Terminal zu senden:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

Sie können den folgenden Befehl ausführen, um eine E-Mail mit dem Link zum Herunterladen der für den Export angegebenen Protokollzeilen zu senden:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


Sie können den folgenden Befehl ausführen, um eine E-Mail mit einem benutzerdefinierten Betreff zu senden:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

