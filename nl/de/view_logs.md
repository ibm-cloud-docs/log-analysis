---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

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

# Protokolle anzeigen
{: #view_logs}

Nach der Bereitstellung einer Instanz des {{site.data.keyword.la_full_notm}}-Service in {{site.data.keyword.cloud_notm}} und der Konfiguration eines LogDNA-Agenten für eine Protokollquelle können Sie Protokolldaten über die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} anzeigen, überwachen und verwalten.
{:shortdesc}

Wenn Sie die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} starten, werden Protokolleinträge in einem vordefinierten Format angezeigt. Im Abschnitt **Benutzervorgaben** können Sie die Art der Informationsanzeige in jeder Protokollzeile ändern. Sie können außerdem Protokolle filtern und Sucheinstellungen ändern und anschließend das Ergebnis als *Ansicht* kennzeichnen. Sie können einer Ansicht mindestens einen Alert zuordnen und die Zuordnung wieder aufheben. Für die Anzeige der Zeilen in der Ansicht können Sie ein benutzerdefiniertes Format angeben. Sie können eine Protokollzeile erweitern und die geparsten Daten anzeigen.


Führen Sie die folgenden Schritte aus, um Protokolle anzuzeigen:


## Schritt 1: Einem Benutzer IAM-Richtlinien zum Anzeigen von Protokollen gewähren
{: #view_logs_step1}

**Anmerkung:** Sie müssen Administrator des {{site.data.keyword.la_full_notm}}-Service oder der {{site.data.keyword.la_full_notm}}-Instanz sein oder im Konto über IAM-Berechtigungen verfügen, anderen Benutzern Richtlinien zu gewähren.

Die folgende Tabelle enthält eine Auflistung der Richtlinien, die ein Benutzer mindestens benötigt, um die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} starten und Protokolle anzeigen zu können:

| Service                        | Rolle                      | Erteilte Berechtigung            |
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` | Plattformrolle: Anzeigeberechtigter     | Der Benutzer kann die Liste der Serviceinstanzen im Dashboard Beobachtbarkeit - Protokollierung anzeigen. |
| `{{site.data.keyword.la_full_notm}} ` | Servicerolle: Leseberechtigter      | Der Benutzer kann die Webbenutzerschnittstelle starten und Protokolle in der Webbenutzerschnittstelle anzeigen.  |
{: caption="Tabelle 1. IAM-Richtlinien" caption-side="top"} 

Weitere Informationen zur Konfiguration dieser Richtlinien für einen Benutzer finden Sie in [Benutzer Berechtigungen zum Anzeigen von Protokollen in LogDNA erteilen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Schritt 2. Über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle zur Webbenutzerschnittstelle navigieren
{: #view_logs_step2}

Führen Sie die folgenden Schritte aus, um die {{site.data.keyword.la_full_notm}}-Benutzerschnittstelle über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle zu starten:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird das {{site.data.keyword.cloud_notm}}-*Dashboard* geöffnet.

2. Wählen Sie im Navigationsmenü **Beobachtbarkeit** aus. 

3. Wählen Sie **Protokollierung** aus. 

    Die Liste der in {{site.data.keyword.cloud_notm}} verfügbaren {{site.data.keyword.la_full_notm}}-Instanzen wird angezeigt.

4. Wählen Sie eine Instanz aus. Klicken Sie dann auf **LogDNA anzeigen**.

Die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} wird geöffnet, in der die an diese Instanz weitergeleiteten Protokolle angezeigt werden.


## Schritt 3. Standardansicht anpassen
{: #view_logs_step3}

Im Abschnitt **Benutzervorgaben** können Sie die Reihenfolge der pro Zeile angezeigten Datenfelder ändern.

Führen Sie die folgenden Schritte aus, um das Format einer Protokollzeile zu ändern:

1. Wählen Sie das Symbol **Konfiguration** aus ![Konfigurationssymbol](images/admin.png "Verwaltungssymbol").
2. Wählen Sie **Benutzervorgaben** aus. Ein neues Fenster wird geöffnet.
3. Wählen Sie **Protokollformat** aus.
4. Ändern Sie den Abschnitt *Zeilenformat* Ihren Anforderungen entsprechend. Ziehen Sie Felder.


## Schritt 4. Protokollzeile anzeigen
{: #view_logs_step4}

Sie können jederzeit jede Protokollzeile im Kontext anzeigen.

Führen Sie die folgenden Schritte aus: 

1. Klicken Sie auf das Symbol **Ansichten** ![Konfigurationssymbol](images/views.png "Konfigurationssymbol").
2. Wählen Sie **Alles** oder eine Ansicht aus.
3. Geben Sie eine Zeile in dem Protokoll an, die Sie untersuchen wollen.
4. Blenden Sie die Protokollzeile ein. 

    Es werden Informationen zu Zeilen-IDs, Tags und Kennsätzen angezeigt.

5. Klicken Sie auf **Im Kontext anzeigen**, um die Protokollzeile im Kontext mit anderen Protokollzeilen von diesem Host und/oder von dieser App anzuzeigen.

6. Klicken Sie auf **In Zwischenablage kopieren**, um das Nachrichtenfeld in die Zwischenablage zu kopieren.

Wenn Sie fertig sind, schließen Sie die Zeile.


## Schritt 5. Protokolle filtern
{: #view_logs_step5}

Sie können Protokolle nach Protokollquelle, Anwendung und Protokollebene filtern. 

* Eine mögliche Quelle ist ein Host, ein Computer, eine virtuelle Maschine oder eine Heroku-App.
* Eine Anwendung stellt eine Protokolldatei, ein Programm oder einen Container dar.
* Beispiele für Protokollebenen sind: INFO, DEBUG, ERROR

Führen Sie die folgenden Schritte aus, um Protokolle zu filtern:

1. Klicken Sie auf das Symbol **Ansichten** ![Konfigurationssymbol](images/views.png "Konfigurationssymbol").
2. Wählen Sie **Alles** oder eine Ansicht aus.
3. Erweitern Sie **Alle Tags**, um die Liste der in den Protokollen identifizierten Tags anzuzeigen, und wählen Sie dann die gewünschten Tags aus.
4. Erweitern Sie **Alle Quellen**, um die Liste der in den Protokollen identifizierten Protokollquellen anzuzeigen, und wählen Sie dann die gewünschten Quellen aus.
5. Erweitern Sie **Alle Apps**, um die Liste der in den Protokollen identifizierten Apps anzuzeigen, und wählen Sie dann die gewünschten Apps aus.
6. Erweitern Sie **Alle Ebenen**, um die Liste der in den Protokollen identifizierten Protokollebenen anzuzeigen, und wählen Sie dann die gewünschten Ebenen aus.


**Anmerkung:** In jedem Abschnitt können Sie mehrere Optionen in einer Gruppe zusammenfassen. Die in einer Gruppe zusammengefassten Tags, Protokollquellen, Apps und Protokollebenen können beim Filtern von Protokolldaten in anderen angepassten Ansichten wiederverwendet werden.

Wenn Sie eine Gruppe erstellen möchten, wählen Sie mehrere Werte aus. Klicken Sie dann auf **Als Gruppe speichern**. Geben Sie einen Namen für die Gruppe ein und speichern Sie sie.


## Schritt 6. Protokolle durchsuchen
{: #view_logs_step6}

Wenn Sie Protokolldaten durchsuchen, werden alle Protokollfilter und Zeitabfragen angewendet, die in der jeweiligen Ansicht konfiguriert sind.

Sie können einfache Suchen (einzelner Begriff), Verbundsuchen (mehrere Suchbegriffe und Operatoren), Feldsuchen, falls die Protokollzeile geparst werden kann, und andere Suchvorgänge durchführen. Weitere Informationen finden Sie in [Protokolle durchsuchen ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://docs.logdna.com/docs/search){:new_window} in der LogDNA-Dokumentation.

**Anmerkung:** Die Operatoren AND und OR müssen in Großbuchstaben angegeben und die Groß-/Kleinschreibung muss beachtet werden.



## Schritt 7. Ansichten erstellen
{: #view_logs_step7}


Führen Sie die folgenden Schritte aus, um eine Ansicht zu erstellen:

1. Klicken Sie auf das Symbol **Ansichten** ![Konfigurationssymbol](images/views.png "Konfigurationssymbol").
2. Wählen Sie **Alles** oder eine Ansicht aus.
3. Filtern Sie die Protokolldaten und klicken Sie dann auf **Als neue Ansicht/neuen Alert speichern**.

    Die Seite *Neue Ansicht erstellen* wird geöffnet.

4. Geben Sie einen Namen für die Sicht in das Feld *Name* ein.

5. Fügen Sie wahlweise eine Kategorie hinzu. Geben Sie einen Namen ein und klicken Sie dann auf **Als neue Ansichtskategorie hinzufügen**.

6. Ordnen Sie wahlweise einen Alert zu. Ein neuer Abschnitt wird angezeigt, in dem Sie den Alert konfigurieren können.

7. Klicken Sie auf **Ansicht speichern**.


