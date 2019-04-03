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

# Protokolle herunterladen
{: #downloading_logs}

Sie können Protokolle in eine lokale Datei herunterladen oder Daten über eine Pipe an ein anderes Programm umleiten. Sie laden Protokolle im Kontext einer Sitzung herunter. Eine Sitzung gibt an, welche Protokolle heruntergeladen werden. Wenn der Download der Protokolle unterbrochen wird, ermöglicht die Sitzung die Fortsetzung des Downloads an der Stelle, an der er unterbrochen wurde. Wenn der Download abgeschlossen ist, müssen Sie die Sitzung löschen.
{:shortdesc}

Um diese Schritte durchführen zu können, müssen Sie die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle installieren. Weitere Informationen finden Sie in [Die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle konfigurieren](https://console.bluemix.net/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli_).


Führen Sie die folgenden Schritte aus, um Protokolldaten aus einem Bereich in eine lokale Datei herunterzuladen:

## Schritt 1: Anmeldung bei {{site.data.keyword.Bluemix_notm}}
{: #downloading_logs_step1}

Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

## Schritt 2: Verfügbare Protokolle ermitteln
{: #step21}

1. Verwenden Sie den Befehl `ibmcloud logging log-show`, um zu ermitteln, welche Protokolle für die letzten beiden Wochen zur Verfügung stehen. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Dieser Befehl stellt beispielsweise folgende Ausgabe bereit:
    
    ```
    ibmcloud logging log-show 
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-16   794008   706     All          syslog, default   
	2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}

    **Hinweis:** Der {{site.data.keyword.loganalysisshort}}-Service ist ein globaler Service, der die koordinierte Weltzeit (UTC) verwendet. Tage sind als UTC-Tage definiert. Um Protokolle für einen bestimmten Tag in Ortszeit anzufordern, müssen Sie möglicherweise mehrere UTC-Tage herunterladen.


## Schritt 3: Sitzung erstellen
{: #step3}

Eine Sitzung ist erforderlich, um den Umfang der Protokolldaten zu definieren, die für einen Download verfügbar sind, und um den Status des Downloads zu behalten. 

Verwenden Sie den Befehl [ibmcloud logging session-create](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_create) zum Erstellen einer Sitzung. Optional können Sie das Startdatum, das Enddatum und Protokolltypen angeben, wenn Sie eine Sitzung erstellen:  

* Wenn Sie das Startdatum und das Enddatum angeben, ermöglicht die Sitzung den Zugriff auf die Protokolle für diesen Datumsbereich. 
* Wenn Sie den Protokolltyp angeben (**-t**), ermöglicht die Sitzung den Zugriff auf einen bestimmten Protokolltyp. Dies ist ein wichtiges Feature, wenn Sie viele Protokolle verwalten müssen, da Sie den Geltungsbereich auf die Protokolle eingrenzen können, die im betreffenden Fall relevant sind.

**Hinweis:** Für jede Sitzung können Sie Protokolle für bis zu 15 Tage herunterladen.

Um eine Sitzung zu erstellen, die verwendet wird, um alle verfügbaren Protokolle der letzten zwei Wochen herunterzuladen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging session-create 
```
{: codeblock}

Die Sitzung gibt die folgenden Informationen zurück:

* Den Datumsbereich für die herunterzuladenden Daten. Standardmäßig wird das aktuelle UTC-Datum verwendet.
* Die Protokolldateien, die heruntergeladen werden sollen. Standardmäßig umfasst dies alle Protokolltypen, die für den Zeitraum verfügbar sind, den Sie beim Erstellen der Sitzung angegeben haben. 
* Informationen dazu, ob das gesamte Konto oder nur der aktuelle Bereich berücksichtigt werden soll. Standardmäßig erhalten Sie Protokolle in dem Bereich, in dem Sie angemeldet sind.
* Die Sitzungs-ID, die erforderlich ist, um Protokolle herunterladen.

Beispiel:

```
$ ibmcloud logging session-create
Creating session for lopezdsr@uk.ibm.com resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type   
944aec4d-61f4-43d1-8f3b-c040195122da   12345678-1234-5678-abcd-378620d6fab5   2017-11-17T14:17:25.611542863Z   2017-11-17T14:17:25.611542863Z   2017-11-04   2017-11-17   ANY_TYPE   
Session: 944aec4d-61f4-43d1-8f3b-c040195122da is created
```
{: screen}

**Tipp:** Um die Liste aktiver Sitzungen anzuzeigen, führen Sie den Befehl [ibmcloud logging sessions](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_list) aus.

## Schritt 4: Protokolldaten in eine Datei herunterladen
{: #step41}

Führen Sie den folgenden Befehl aus, um die Protokolle herunterzuladen, die durch die Sitzungsparameter angegeben sind:

```
ibmcloud logging log-download -o Log_File_Name Session_ID
```
{: codeblock}

Dabei gilt:

* Log_File_Name ist der Name der Ausgabedatei.
* Session_ID ist die GUID der Sitzung. Sie haben diesen Wert im vorherigen Schritt erhalten.

Beispiel:

```
ibmcloud logging log-download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

Der Fortschrittsanzeiger zeigt den jeweils aktuellen Downloadstatus auf einer Skala von 0 bis 100 Prozent.

**Hinweis:** 

* Das Format der heruntergeladenen Daten ist das komprimierte JSON-Format. Wenn Sie die Datei mit der Erweiterung .gz dekomprimieren und öffnen, können Sie die Daten im JSON-Format sehen. 
* Das komprimierte JSON-Format eignet sich für das Einpflegen per Elasticsearch oder Logstash. Wenn -o nicht angegeben wird, werden die Daten in die Standardausgabe gestreamt, sodass Sie sie direkt in Ihren eigenen ELK-Stack umleiten können.
* Sie können die Daten auch mit einem Programm verarbeiten, das JSON-Parsing ermöglicht. 

## Schritt 5: Sitzung löschen
{: #step5}

Wenn der Download abgeschlossen ist, müssen Sie die Sitzung mit dem Befehl [ibmcloud logging session delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) löschen. 

Führen Sie den folgenden Befehl aus, um eine Sitzung zu löschen:

```
ibmcloud logging session-delete Session_ID
```
{: codeblock}

Dabei ist Session-ID die GUID der Sitzung, die Sie im vorherigen Schritt erstellt haben.

Beispiel:

```
ibmcloud logging session-delete -jshdjsunelsssr4566722==
Deleting session: -jshdjsunelsssr4566722== of resource: 12345678-1234-5678-abcd-378620d6fab5 ...
Session: -jshdjsunelsssr4566722== is deleted

```
{: screen}




