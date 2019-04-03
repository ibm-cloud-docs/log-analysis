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

# Log Analysis-Befehlszeilenschnittstelle ({{site.data.keyword.Bluemix_notm}}-Plug-in)
{: #log_analysis_cli}

Bei der {{site.data.keyword.loganalysislong}}-Befehlszeilenschnittstelle handelt es sich um ein {{site.data.keyword.Bluemix_notm}}-Plug-in, mit dem Sie Protokolle verwalten können, die in 'Log Collection' gespeichert sind.
{: shortdesc}

**Voraussetzungen**
* Bevor Sie die Protokollierungsbefehle ausführen, müssen Sie sich bei {{site.data.keyword.Bluemix_notm}} mit dem Befehl `ibmcloud login` anmelden, um ein Zugriffstoken zu generieren und um Ihre Sitzung zu authentifizieren.

Informationen zur Verwendung der Befehlszeilenschnittstelle von {{site.data.keyword.loganalysisshort}} finden Sie unter [Protokolle verwalten](/docs/services/CloudLogAnalysis/log_analysis_ov.html#log_analysis_ov).

<table>
  <caption>Befehle für die Verwaltung von Protokollen</caption>
  <tr>
    <th>Befehl</th>
    <th>Verwendungszweck</th>
  </tr>
  <tr>
    <td>[ibmcloud logging](#base)</td>
    <td>Mit diesem Befehl können Informationen über die Befehlszeilenschnittstelle (CLI), wie die Liste der Befehle, abgerufen werden.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-delete](#delete)</td>
    <td>Mit diesem Befehl können Sie Protokolle löschen, die in 'Log Collection' gespeichert sind.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-download](#download)</td>
    <td>Verwenden Sie diesen Befehl, um Protokolle aus 'Log Collection' in eine lokale Datei herunterzuladen oder um Protokolle an ein anderes Programm (wie z. B. Elastic Stack) umzuleiten. </td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-show](#status)</td>
    <td>Verwenden Sie diesen Befehl, um Informationen zu den Protokollen abzurufen, die in einem Bereich, einer Organisation oder einem Konto erfasst werden.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging help](#help)</td>
    <td>Mit diesem Befehl können Sie Hilfeinformationen zur Verwendung der Befehlszeilenschnittstelle und eine Liste aller Befehle abrufen.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-show](#optionshow)</td>
    <td>Verwenden Sie diesen Befehl zum Anzeigen des Aufbewahrungszeitraums für Protokolle, die in einem Bereich, einer Organisation oder einem Konto verfügbar sind.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-update](#optionupdate)</td>
    <td>Verwenden Sie diesen Befehl zum Festlegen des Aufbewahrungszeitraums für Protokolle, die in einem Bereich, einer Organisation oder einem Konto verfügbar sind.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging quota-usage-show](#quotausage)</td>
    <td>Verwenden Sie diesen Befehl, um die Informationen zur Kontingentnutzung für einen Bereich, eine Organisation oder ein Konto abzurufen. Sie können auch die Informationen zum Kontingentverlauf abrufen.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging session-create](#session_create)</td>
    <td>Mit diesem Befehl können Sie eine neue Sitzung erstellen.</td>
  <tr>
  <tr>
    <td>[ibmcloud logging session-delete](#session_delete)</td>
    <td>Mit diesem Befehl können Sie eine Sitzung löschen.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging sessions](#session_list)</td>
    <td>Verwenden Sie diesen Befehl, um die aktiven Sitzungen und die zugehörigen IDs aufzulisten.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging session-show](#session_show)</td>
    <td>Verwenden Sie diesen Befehl, um den Status einer einzelnen Sitzung anzuzeigen.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging token-get](#tokenget)</td>
    <td>Verwenden Sie diesen Befehl, um das Protokollierungstoken anzufordern, um Protokolldaten an den {{site.data.keyword.loganalysisshort}}-Service zu senden.</td>
  </tr>
</table>


## ibmcloud logging
{: #base}

Mit diesem Befehl können Sie allgemeine Informationen zur Befehlszeilenschnittstelle bereitstellen.

```
ibmcloud logging 
```
{: codeblock}

**Beispiele**

Um die Liste der Befehle abzurufen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging
NAME:
   ibmcloud logging - IBM Cloud Log Analysis Service
USAGE:
   ibmcloud logging command [Argumente...] [Befehlsoptionen]

COMMANDS:
COMMANDS:
   log-delete         Protokoll löschen
   log-download       Protokoll herunterladen
   log-show           Anzahl, Größe und Typ der Protokolle pro Tag anzeigen
   session-create     Sitzung erstellen
   session-delete     Sitzung löschen
   sessions           Sitzungsinformationen auflisten
   session-show       Sitzungsinformationen anzeigen
   option-show        Protokollspeicherung anzeigen
   option-update      Protokolloptionen anzeigen
   token-get          Protokollierungstoken zum Senden von Protokollen abrufen
   quota-usage-show   Informationen zur Kontingentnutzung anzeigen
   help             
   
Gebe Sie 'ibmcloud logging help [Befehl]' ein, um weitere Informationen zu einem Befehl zu erhalten.
```
{: codeblock}




## ibmcloud logging log-delete
{: #delete3}

Mit diesem Befehl können Sie Protokolle löschen, die in 'Log Collection' gespeichert sind.

```
ibmcloud logging log-delete [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] [-s, --start STARTDATUM] [-e, --end ENDDATUM] [-t, --type, PROTOKOLLTYP] [-f, --force ]
```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
  
  <dt>-s, --start STARTDATUM</dt>
  <dd>(Optional) Legt das Startdatum in koordinierter Weltzeit (UTC) fest: *JJJJ-MM-TT*, z. B `2006-01-02`. <br>Der Standardwert ist auf 'vor zwei Wochen' festgelegt.
  </dd>
  
  <dt>-e, --end ENDDATUM</dt>
  <dd>(Optional) Legt das Enddatum in koordinierter Weltzeit (UTC) fest: *JJJJ-MM-TT*, z. B. `2006-01-02`. <br>Der Standardwert wird auf das aktuelle Datum gesetzt.
  </dd>
  
  <dt>-f, --force </dt>
  <dd>(Optional) Legen Sie diese Option fest, um Protokolle zu löschen, ohne die Aktion bestätigen zu müssen.
  </dd>
</dl>

**Beispiel**

Führen Sie den folgenden Befehl aus, um die Protokolle des Typs *linux_syslog* für den 25. Mai 2017 zu löschen:
```
ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: screen}



## ibmcloud logging log-download 
{: #download3}

Mit diesem Befehl können Sie Protokolle aus 'Log Collection' in eine lokale Datei herunterladen oder Protokolle an ein anderes Programm (zum Beispiel Elastic Stack) umleiten. 

**Hinweis:** Um Dateien herunterladen zu können, müssen Sie zuerst eine Sitzung erstellen. Eine Sitzung definiert die herunterzuladenden Protokolle abhängig vom Datumsbereich, vom Protokolltyp und vom Kontotyp. Sie laden Protokolle im Kontext einer Sitzung herunter. Weitere Informationen finden Sie unter [ibmcloud logging session create (Beta)](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_create).

```
 ibmcloud logging log-download  [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] [-o, --output AUSGABE] SITZUNGS-ID

```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
 
  <dt>-o, --output AUSGABE</dt>
  <dd>(Optional) Legt den Pfad und den Dateinamen für die lokale Ausgabedatei fest, in die die Protokolle heruntergeladen werden. <br>Der Standardwert ist ein Bindestrich (-). <br>Legen Sie diesen Parameter auf den Standardwert fest, damit die Protokolle an die Standardausgabe ausgegeben werden.</dd>

</dl>

**Argumente**

<dl>
  <dt>SITZUNGS-ID</dt>
  <dd>Dieser Wert zeigt die ID der Sitzung an, die beim Herunterladen von Protokollen verwendet werden muss. <br>**Hinweis:** Der Befehl `ibmcloud logging session-create` enthält die Parameter, die steuern, welche Protokolle heruntergeladen werden. </dd>
</dl>

**Hinweis:** Wenn der Download abgeschlossen ist, hat ein nochmaliges Ausführen desselben Befehls keinerlei Auswirkung. Um dieselben Daten erneut herunterzuladen, müssen Sie eine andere Datei oder eine andere Sitzung verwenden.

**Beispiele**

Um unter Linux Protokolle in eine Datei mit dem Namen 'mylogs.gz' herunterzuladen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging log-download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

Führen Sie den folgenden Befehl aus, um Protokolle in eine eigene Elastic Stack-Instanz herunterzuladen:

```
ibmcloud logging log-download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

Die folgende Datei ist ein Beispiel für eine Datei logstash.conf:

```
input {
  stdin {
    codec => json_lines {}
  }
}
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud logging help
{: #help}

Dieser Befehl bietet Hinweise zur Verwendung eines Befehls.

```
ibmcloud logging help [Befehl] 
```
{: codeblock}

**Parameter**

<dl>
<dt>Befehl</dt>
<dd>Geben Sie den Namen des Befehls an, für den Sie Hilfeinformationen abrufen wollen.
</dd>
</dl>


**Beispiele**

Um Hilfeinformationen zu dem Befehl abzurufen, mit dem Sie den Status von Protokollen anzeigen können, führen Sie den folgenden Befehl aus:

```
ibmcloud logging help log-show
NAME:
   log-show - Anzahl, Größe und Typ der Protokolle pro Tag anzeigen

USAGE:
   ibmcloud logging log-show [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] [-s, --start STARTDATUM] [-e, --end ENDDATUM] [-t, --type, PROTOKOLLTYP] [-l, --list-type-detail]

OPTIONS:
   -r, --resource-type     Ressourcentyp, gültiger Ressourcentyp ist 'Konto', 'Organisation' oder 'Bereich'
   -i, --resource-id       Ressourcen-ID, die Zielressourcen-ID
   -s, --start             Startdatum, UTC-Zeitwert im Format JJJJ-MM-TT
   -e, --end               Enddatum, UTC-Zeitwert im Format JJJJ-MM-TT
   -t, --type              Protokolltyp, z. B. "syslog"
   -l, --list-type-detail  Listet den detaillierten Typ auf

```
{: screen}


## ibmcloud logging option-show
{: #optionshow}

Verwenden Sie diesen Befehl zum Anzeigen des Aufbewahrungszeitraums für Protokolle, die in einem Bereich, einer Organisation oder einem Konto verfügbar sind. 

* Der Zeitraum wird als eine Anzahl von Tagen festgelegt.
* Der Standardwert ist **-1**. 

**Hinweis:** Standardmäßig werden alle Protokolle gespeichert. Sie müssen sie manuell mit dem Befehl **delete** löschen. Definieren Sie eine Aufbewahrungsrichtlinie zum automatischen Löschen der Protokolle.

```
ibmcloud logging option-show [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID]
```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>

</dl>

**Beispiele**

Um den aktuellen Standardaufbewahrungszeitraum für den Bereich anzuzeigen, bei dem Sie angemeldet sind, führen Sie den folgenden Befehl aus:

```
ibmcloud logging option-show
```
{: screen}




## ibmcloud logging option-update
{: #optionupdate}

Verwenden Sie diesen Befehl zum Ändern des Aufbewahrungszeitraums für Protokolle, die in einem Bereich, einer Organisation oder einem Konto verfügbar sind. 

* Der Zeitraum wird als eine Anzahl von Tagen festgelegt.
* Der Standardwert ist **-1**. 

```
ibmcloud logging option-update [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] <-e,--retention AUFBEWAHRUNGSWERT>
```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest, für den/die/das Sie Informationen abrufen möchten. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
  
  <dt>-e,--retention AUFBEWAHRUNGSWERT</dt>
  <dd>Legt die Anzahl der Tage fest, die Protokolle aufbewahrt werden. </dd>

</dl>

**Beispiel**

Um den Aufbewahrungszeitraum für den Bereich, bei dem Sie angemeldet sind, in 25 Tage zu ändern, führen Sie den folgenden Befehl aus:

```
ibmcloud logging option-update -e 25
```
{: screen}


## ibmcloud logging quota-usage-show
{: #quotausage}

Informiert über die Kontingentnutzung für einen Bereich, eine Organisation oder ein Konto. Damit lassen sich auch Informationen zum Kontingentverlauf abrufen.

* Der Zeitraum wird als eine Anzahl von Tagen festgelegt.
* Der Standardwert ist **-1**. 

```
ibmcloud logging quota-usage-show [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] [-s,--history]
```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
  
  <dt>-s,--history</dt>
  <dd>(Optional) Legen Sie diesen Parameter fest, um die Historieinformationen zur Kontingentnutzung abzurufen.</dd>

</dl>

**Beispiel**

Um die archivierte Kontingentnutzung für eine Bereichsdomäne anzuzeigen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotment   Usage
2018.02.28   524288000   80405926
2018.03.06   524288000   18955540
2018.03.05   524288000   47262944
2018.03.08   524288000   18311338
2018.03.01   524288000   82416831
2018.03.03   524288000   75045462
2018.03.07   524288000   17386278
2018.03.02   524288000   104316444
2018.03.04   524288000   73125223   
```
{: screen}

## ibmcloud logging session-create
{: #session_create}

Mit diesem Befehl können Sie eine neue Sitzung erstellen.

**Hinweis:** Sie können bis zu 30 Sitzungen in einem Bereich gleichzeitig ausführen. Die Sitzung wird für einen Benutzer erstellt. Sitzungen können nicht von verschiedenen Benutzern in einem Bereich gemeinsam genutzt werden.

```
ibmcloud logging session-create [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] [-s, --start STARTDATUM] [-e, --end ENDDATUM] [-t, --type, PROTOKOLLTYP] [-T, --time, PROTOKOLLZEIT]
```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
  
  <dt>-s, --start STARTDATUM</dt>
  <dd>(Optional) Legt das Startdatum in koordinierter Weltzeit (UTC) fest: *JJJJ-MM-TT*, z. B `2006-01-02`. <br>Der Standardwert ist auf 'vor zwei Wochen' festgelegt.
  </dd>
  
  <dt>-e, --end ENDDATUM</dt>
  <dd>(Optional) Legt das Enddatum in koordinierter Weltzeit (UTC) fest: *JJJJ-MM-TT*, z. B. `2006-01-02`. <br>Der Standardwert wird auf das aktuelle Datum gesetzt.
  </dd>
  
  <dt>-t, --type, PROTOKOLLTYP</dt>
  <dd>(Optional) Legt den Protokolltyp fest. <br>Ein Protokolltyp ist beispielsweise *syslog*. <br>Standardwert ist ein Stern (*). <br>Sie können mehrere Protokolltypen angeben, indem Sie die einzelnen Typen durch Kommas trennen. Beispiel: *log_type_1,log_type_2,log_type_3*.
  </dd>

  <dt>-T, --time, PROTOKOLLZEIT</dt>
  <dd>(Optional) Legt die Stunde des Tages fest, zu der Protokolle eine bestimmten Typs abgerufen werden sollen. </br>Gültige Werte sind 0-23. </br>Diese Option muss zusammen mit LOG_TYPE verwendet werden.
  </dd>

</dl>


**Zurückgegebene Werte**

<dl>

    <dt>ID</dt>
    <dd>Sitzungs-ID.</dd>
	
	<dt>Resource type</dt>
    <dd>Die Ressourcen-ID.</dd>

    <dt>AccessTime</dt>
    <dd>Zeitmarke, die angibt, wann die Sitzung zum letzten Mal verwendet wurde.</dd>

    <dt>CreateTime</dt>
    <dd>Zeitmarke des Zeitpunkts (Datum und Uhrzeit), als die Sitzung erstellt wurde.</dd>
	
	<dt>Start</dt>
    <dd>Gibt den ersten Tag an, der zum Filtern von Protokollen verwendet wird. </dd>

    <dt>End</dt>
    <dd>Gibt den letzten Tag an, der zum Filtern von Protokollen verwendet wird.</dd>

    <dt>Type</dt>
    <dd>Protokolltypen, die über die Sitzung heruntergeladen werden.</dd>

</dl>


**Beispiel**

Um eine Sitzung mit Protokollen für den 13. November 2017 zu erstellen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging session-create -s 2017-11-13 -e 2017-11-13
Creating session for xxxxx@yyy.com resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   2017-11-13   2017-11-13   ANY_TYPE   
Session: 1ef776d1-4d25-4297-9693-882606c725c8 is created
```
{: screen}


## ibmcloud logging session-delete 
{: #session_delete}

Löscht eine Sitzung, die durch die Sitzungs-ID angegeben ist.

```
ibmcloud session-delete [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] SITZUNGS-ID
```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
 
</dl>

**Argumente**

<dl>
  <dt>SITZUNGS-ID</dt>
  <dd>ID der aktiven Sitzung, die Sie löschen wollen.</dd>
</dl>

**Beispiel**

Um eine Sitzung mit der Sitzungs-ID *cI6hvAa0KR_tyhjxZZz9Uw==* zu löschen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging session-delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud logging sessions
{: #session_list}

Listet die aktiven Sitzungen und ihre IDs auf.

```
ibmcloud logging sessions [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID]
```
{: codeblock}

**Parameter**

<dl>

  <dt>-r,--resource-type RESSOURCENTYP</dt>
      <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation* </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
      <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind.  </dd>
</dl>

**Rückgabewerte**

<dl>	
    <dt>SITZUNGS-ID</dt>
    <dd>ID der aktiven Sitzung.</dd>
	   
    <dt>Ressourcen-ID</dt>
    <dd>ID der Ressource, für die die Sitzung gilt.</dd>

    <dt>CreateTime</dt>
    <dd>Zeitmarke des Zeitpunkts (Datum und Uhrzeit), als die Sitzung erstellt wurde.</dd>

    <dt>AccessTime</dt>
    <dd>Zeitmarke, die angibt, wann die Sitzung zum letzten Mal verwendet wurde.</dd>
</dl>
 
**Beispiel**

```
ibmcloud logging sessions
Listing sessions of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   
Listed the sessions of resource xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 
```
:{ screen}


## ibmcloud logging session-show
{: #session_show}

Zeigt den Status einer einzelnen Sitzung.

```
ibmcloud logging session-show [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] SITZUNGS-ID

```
{: codeblock}

**Parameter**

<dl>
   <dt>-r,--resource-type RESSOURCENTYP</dt>
      <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation* </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
      <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind.  </dd>
</dl>

**Argumente**

<dl>
   <dt>SITZUNGS-ID</dt>
   <dd>ID der aktiven Sitzung, für die Sie Informationen abrufen möchten.</dd>
</dl>

**Beispiel**

Um Details zu einer Sitzung mit der Sitzungs-ID *cI6hvAa0KR_tyhjxZZz9Uw==* anzuzeigen, führen Sie den folgenden Befehl aus:

```
ibmcloud logging session-show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}

## ibmcloud logging token-get
{: #tokenget}

Gibt das Protokollierungstoken zurück, das zum Senden von Protokolldaten zu {{site.data.keyword.loganalysisshort}} erforderlich ist.

```
ibmcloud logging token-get [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID]
```
{: codeblock}

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Typ der Ressource fest, zu der Protokolldaten gesendet werden. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
</dl>


**Beispiel**

```
ibmcloud logging token-get -r space -i js7ydf98-8682-430d-bav4-36b712341744
Getting log token of resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Tenant Id                              Logging Token   
js7ydf98-8682-430d-bav4-36b712341744   xxxxxxxxxx   
```
{: screen}


## ibmcloud logging log-show
{: #status}

Verwenden Sie diesen Befehl, um Informationen zu den Protokollen abzurufen, die in einem {{site.data.keyword.Bluemix_notm}}-Bereich oder -Konto erfasst werden.

```
ibmcloud logging log-show [-r,--resource-type RESSOURCENTYP] [-i,--resource-id RESSOURCEN-ID] [-s, --start STARTDATUM] [-e, --end ENDDATUM] [-t, --type, PROTOKOLLTYP] [-l, --list-type-detail]
```
{: codeblock}

* Wenn kein Ressourcentyp angegeben ist, gibt der Befehl die Details der Ressource zurück, wenn Sie angemeldet sind.
* Wenn Sie einen Ressourcentyp festlegen, müssen Sie die Ressourcen-ID angeben.
* Der Befehl meldet nur Informationen zu den Protokollen der letzten zwei Wochen, die in 'Log Collection' gespeichert sind, wenn kein Start- und Enddatum angegeben ist.

**Parameter**

<dl>
  <dt>-r,--resource-type RESSOURCENTYP</dt>
  <dd>(Optional) Legt den Ressourcentyp fest. Gültige Werte: *Bereich*, *Konto* und *Organisation*
  </dd>
  
   <dt>-i,--resource-id RESSOURCEN-ID</dt>
  <dd>(Optional) Legen Sie in diesem Feld die ID des Bereichs, der Organisation oder des Kontos fest. <br>Wenn Sie diesen Parameter nicht angeben, wird im Befehl standardmäßig die ID der Ressource verwendet, bei der Sie angemeldet sind. 
  </dd>
  
  <dt>-s, --start STARTDATUM</dt>
  <dd>(Optional) Legt das Startdatum in koordinierter Weltzeit (UTC) fest: *JJJJ-MM-TT*, z. B `2006-01-02`. <br>Der Standardwert ist auf 'vor zwei Wochen' festgelegt.
  </dd>
  
  <dt>-e, --end ENDDATUM</dt>
  <dd>(Optional) Legt das Enddatum in koordinierter Weltzeit (UTC) fest: *JJJJ-MM-TT*, z. B. `2006-01-02`. <br>Der Standardwert wird auf das aktuelle Datum gesetzt.
  </dd>
  
  <dt>-t, --type, PROTOKOLLTYP</dt>
  <dd>(Optional) Legt den Protokolltyp fest. <br>Ein Protokolltyp ist beispielsweise *syslog*. <br>Standardwert ist ein Stern (*). <br>Sie können mehrere Protokolltypen angeben, indem Sie die einzelnen Typen durch Kommas trennen. Beispiel: *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>-l, --list-type-detail</dt>
  <dd>(Optional) Legen Sie diesen Parameter, um jeden Protokolltyp einzeln aufzuführen.
  </dd>
</dl>


**Beispiel**

```
ibmcloud logging log-show
Showing log status of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

Date         Size        Count    Searchable   Types   
2017-11-07   1878197     1333     None         default   
2017-11-13   201653512   179391   All          default,linux_syslog   
2017-11-14   32134119    30425    All          default,linux_syslog   
2017-11-15   303901156   269689   All          linux_syslog,default   
2017-11-16   107253679   96648    All          default,linux_syslog   
```
{: screen}

```
 ibmcloud logging log-show -l
Showing log status of resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

Date         Size        Count    Searchable   Type   
2017-11-14   30146764    26611    true         default   
2017-11-14   1987355     3814     true         linux_syslog   
2017-11-15   303004895   267890   true         default   
2017-11-15   896261      1799     true         linux_syslog   
2017-11-16   107918249   96278    true         default   
2017-11-16   912890      1794     true         linux_syslog   
```
{: screen}
