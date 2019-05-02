---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

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

 
# Protokolle senden
{: #ingest}

Sie können Protokolldaten an eine {{site.data.keyword.la_full_notm}}-Instanz senden. 
{:shortdesc}

Führen Sie die folgenden Schritte aus, um Protokolle programmgesteuert zu senden:

## Schritt 1. Aufnahme-API-Schlüssel abrufen 
{: #ingest_step1}

**Anmerkung:** Sie müssen über die Rolle **Manager** für die Instanz oder den Service von {{site.data.keyword.la_full_notm}} verfügen, um diesen Schritt ausführen zu können. Weitere Informationen finden Sie in [Berechtigungen zum Verwalten von Protokollen und zum Konfigurieren von Alerts in LogDNA erteilen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

Führen Sie die folgenden Schritte aus, um den Aufnahmeschlüssel abzurufen:
    
1. Starten Sie die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}}. Weitere Informationen finden Sie in [Zur Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} navigieren](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Wählen Sie das Symbol **Konfiguration** aus ![Konfigurationssymbol](images/admin.png). Wählen Sie dann **Organisation** aus. 

3. Wählen Sie **API-Schlüssel** aus.

    Die erstellten Aufnahmeschlüssel werden angezeigt. 

4. Verwenden Sie einen vorhandenen Aufnahmeschlüssel oder klicken Sie auf **Aufnahmeschlüssel generieren**, um einen neuen Schlüssel zu erstellen.

    Der Liste wird ein neuer Schlüssel hinzugefügt. Kopieren Sie den Schlüssel.


## Schritt 2. Protokolle senden
{: #ingest_step2}

Führen Sie den folgenden cURL-Befehl aus, um Protokolle zu senden:

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

Hierbei gilt Folgendes: 

* ENDPOINT gibt den Einstiegspunkt für den Service an. Jede Region verfügt über eine andere URL.
* QUERY_PARAMETERS sind Parameter, die die die Filterkriterien definieren, die auf die Aufnahmeanforderung angewendet werden.
* LOG_LINES beschreibt die Protokollzeilen, die gesendet werden sollen. Es ist als Objektarray definiert.
* INGESTION_KEY ist der im vorherigen Schritt erstellte Schlüssel.

Die folgende Tabelle enthält eine Auflistung der Endpunkte nach Region.

| Region         | Endpunkt                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="Endpunkte nach Region" caption-side="top"} 


Die folgende Tabelle enthält eine Auflistung der Abfrageparameter.

| Abfrageparameter | Typ       | Status     | Beschreibung |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | Erforderlich   | Hostname der Quelle. |
| `mac`           | `string`     | Optional   | Die Netz-MAC-Adresse des Host-Computers.    |
| `ip`            | `string`     | Optional   | Die lokale IP-Adresse des Host-Computers.  | 
| `now`           | `date-time`  | Optional   | Die UNIX-Zeitmarke der Quelle in Millisekunden zum Anforderungszeitpunkt. Wird zur Berechnung der Zeitabweichung verwendet.|
| `tags`          | `string`     | Optional   | Tags, die zum dynamischen Gruppieren von Hosts verwendet werden. |
{: caption="Abfrageparameter" caption-side="top"} 



Die folgende Tabelle enthält eine Auflistung der Daten, die pro Protokollzeile erforderlich sind.

| Parameter     | Typ       | Beschreibung                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | UNIX-Zeitmarke (einschließlich Millisekunden) der Protokolleintragsaufzeichnung.       | 
| `line`           | `string`     | Text der Protokollzeile.                                     |
| `app`            | `string`     | Name der Anwendung, die die Protokollzeile generiert.  |
| `level`          | `string`     | Einen Wert für die Stufe festlegen. Dieser Parameter kann z. B. folgende Werte haben: `INFO`, `WARNING`, `ERROR`. |
| `meta`           |            | Dieses Feld ist für benutzerdefinierte Informationen reserviert, die einer Protokollzeile zugeordnet sind. Sollen einem API-Aufruf Metadaten hinzugefügt werden, geben Sie das Metafeld unter dem Linienobjekt an. Metadaten können im Kontext dieser Zeile angezeigt werden.                      |
{: caption="Linienobjektfelder" caption-side="top"} 

Das folgende Beispiel zeigt die JSON für eine Protokollzeile, die Sie aufnehmen wollen:

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00, 
      "line":"This is my first log line.", 
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## Beispiel
{: #ingest_example}

Das folgende Beispiel zeigt den cURL-Befehl, mit dem 1 Protokollzeile an eine Instanz des {{site.data.keyword.la_full_notm}}-Service gesendet wird: 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

