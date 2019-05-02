---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ubuntu, tutorial

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


# Ubuntu-Protokolle mit {{site.data.keyword.la_full_notm}} verwalten
{: #ubuntu}

Mit dem {{site.data.keyword.la_full}}-Service können Sie Ubuntu-Protokolle in einem zentralen Protokollierungssystem in {{site.data.keyword.cloud_notm}} überwachen und verwalten. 
{:shortdesc}

Sie können System- und Anwendungsprotokolle erfassen und überwachen. 

Der LogDNA-Agent für Ubuntu überwacht standardmäßig Protokolldateien im Verzeichnis **/var/log**. Beispielsweise wird das Ubuntu-Systemprotokoll (*/var/log/syslog*) standardmäßig überwacht.

Wenn Sie in {{site.data.keyword.cloud_notm}} auf einem Ubuntu-Server die Weiterleitung von Protokollen an eine {{site.data.keyword.la_full_notm}}-Instanz konfigurieren wollen, müssen Sie die folgenden Schritte ausführen:

1. Stellen Sie eine Instanz des {{site.data.keyword.la_full_notm}}-Service bereit. 
2. Konfigurieren Sie den LogDNA-Agenten auf dem Ubuntu-Server.
3. Fügen Sie wahlweise weitere Verzeichnisse hinzu, die der Agent überwachen soll.

![Komponentenübersicht in {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Komponentenübersicht in {{site.data.keyword.cloud_notm}}")

In diesem Lernprogramm erfahren Sie, wie Sie auf einem Ubuntu-Server die Weiterleitung von Protokollen an eine {{site.data.keyword.la_full_notm}}-Instanz konfigurieren.

## Vorbereitende Schritte
{: #ubuntu_prereqs}

Informieren Sie sich über {{site.data.keyword.la_full_notm}}. Weitere Informationen finden Sie in [Informationen zu LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Arbeiten Sie in der Region US-South. {{site.data.keyword.la_full_notm}} ist derzeit in der Region US-South verfügbar. **Anmerkung:** Sie können Daten von einem Ubuntu-Server senden, der sich in derselben Region oder in einer anderen Region befindet. 

Verwenden Sie eine Benutzer-ID, die Mitglied oder Eigner eines {{site.data.keyword.cloud_notm}}-Kontos ist. Um eine {{site.data.keyword.cloud_notm}}-Benutzer-ID anzufordern, rufen Sie [Registrierung![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window} auf.

Ihrer {{site.data.keyword.IBM_notm}} ID müssen IAM-Richtlinien für jede der folgenden Ressourcen zugeordnet sein: 

| Ressource                             | Geltungsbereich der Zugriffsrichtlinie | Rolle    | Region    | Informationen                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Ressourcengruppe **Standard**           |  Ressourcengruppe            | Anzeigeberechtigter  | us-south  | Diese Richtlinie ist erforderlich, damit der Benutzer Serviceinstanzen in der Ressourcengruppe Standard anzeigen kann.    |
| {{site.data.keyword.la_full_notm}}-Service |  Ressourcengruppe            | Bearbeiter  | us-south  | Diese Richtlinie ist erforderlich, damit der Benutzer den {{site.data.keyword.la_full_notm}}-Service in der Ressourcengruppe Standard bereitstellen und verwalten kann.   |
{: caption="Tabelle 1. Liste der für das Lernprogramm erforderlichen IAM-Richtlinien" caption-side="top"} 

Installieren Sie die Befehlszeilenschnittstelle (CLI) von {{site.data.keyword.cloud_notm}}. Weitere Informationen finden Sie in [{{site.data.keyword.cloud_notm}}-CLI installieren](/docs/cli/index.html#overview).



## Schritt 1. Eine {{site.data.keyword.la_full_notm}}-Instanz bereitstellen
{: #ubuntu_step1}

Führen Sie die folgenden Schritte aus, um eine {{site.data.keyword.la_full_notm}}-Instanz über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle bereitzustellen:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die Benutzerschnittstelle von {{site.data.keyword.cloud_notm}} geöffnet.

2. Klicken Sie auf **Katalog**. Die Liste der in {{site.data.keyword.cloud_notm}} verfügbaren Services wird geöffnet.

3. Wählen Sie die Kategorie **Entwicklertools** aus, um die angezeigte Liste der Services zu filtern.

4. Klicken Sie auf die Kachel **{{site.data.keyword.la_full_notm}}**.

5. Geben Sie einen Namen für die Serviceinstanz ein.

6. Wählen Sie die Ressourcengruppe **Standard** aus. 

    Die Ressourcengruppe **Standard** ist standardmäßig festgelegt.

7. Wählen Sie den Serviceplan **Lite** aus. 

    Der Plan **Lite** ist standardmäßig festgelegt.

    Weitere Informationen zu anderen Serviceplänen finden Sie in [Preisstrukturpläne](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. Klicken Sie auf **Erstellen**, um den {{site.data.keyword.la_full_notm}}-Service in der {{site.data.keyword.cloud_notm}}-Ressourcengruppe bereitzustellen, in der Sie angemeldet sind.

Nachdem Sie eine Instanz bereitgestellt haben, wird das {{site.data.keyword.la_full_notm}}-Dashboard geöffnet. 


**Anmerkung:** Informationen zum Bereitstellen einer LogDNA-Instanz über die Befehlszeilenschnittstelle finden Sie unter [Instanz über die {{site.data.keyword.cloud_notm}}-Befehlszeilenschnittstelle bereitstellen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli).


## Schritt 2. Ubuntu-Server konfigurieren, so dass Protokolle an Ihre Instanz gesendet werden
{: #ubuntu_step2}

Wenn Sie Ihren Ubuntu-Server so konfigurieren möchten, dass Protokolle an Ihre {{site.data.keyword.la_full_notm}}-Instanz gesendet werden, müssen Sie einen LogDNA-Agenten (`logdna-agent`) installieren. Der LogDNA-Agent liest Protokolldateien aus */var/log* und leitet die Protokolldaten an Ihre LogDNA-Instanz weiter.

Führen Sie die folgenden Schritte über ein Ubuntu-Terminal aus, wenn Sie Ihren Ubuntu-Server so konfigurieren möchten, dass Protokolle an Ihre LogDNA-Instanz weitergeleitet werden:

1. Installieren Sie den LogDNA-Agenten. Führen Sie die folgenden Befehle aus:

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. Definieren Sie den Aufnahmeschlüssel, den der LogDNA-Agent für die Weiterleitung von Protokollen an die {{site.data.keyword.la_full_notm}}-Instanz verwenden muss.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    Hierbei enthält INGESTION_KEY den Aufnahmeschlüssel, der für die {{site.data.keyword.la_full_notm}}-Instanz aktiv ist, in der Sie die Weiterleitung von Protokollen konfigurieren.

3. Geben Sie den Authentifizierungsendpunkt an. Der LogDNA-Agent verwendet diesen Host zur Authentifizierung und zum Abrufen des Tokens für die Weiterleitung von Protokollen.

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. Geben Sie den Aufnahmeendpunkt an.

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. Definieren Sie weitere zu überwachende Protokollpfade. Führen Sie den folgenden Befehl aus: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    Standardmäßig wird **/var/log** überwacht.

6. Geben Sie in der Konfiguration des LogDNA-Agenten wahlweise an, dass Ihre Hosts mit Tags versehen werden. Führen Sie die folgenden Befehle aus:

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}


## Schritt 3: LogDNA-Webbenutzerschnittstelle starten
{: #ubuntu_step3}

Führen Sie die folgenden Schritte aus, um das IBM Log Analysis with LogDNA-Dashboard über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle zu starten:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird das {{site.data.keyword.cloud_notm}}-Dashboard geöffnet.

2. Wählen Sie im Navigationsmenü **Beobachtbarkeit** aus. 

3. Wählen Sie **Protokollierung** aus. 

    Die Liste der in {{site.data.keyword.cloud_notm}} verfügbaren {{site.data.keyword.la_full_notm}}-Instanzen wird angezeigt.

3. Wählen Sie eine Instanz aus. Klicken Sie dann auf **LogDNA anzeigen**.

    Die LogDNA-Webbenutzerschnittstelle wird geöffnet, in der Ihre Clusterprotokolle angezeigt werden.


## Schritt 4: Protokolle anzeigen
{: #ubuntu_step4}

Über die LogDNA-Webbenutzerschnittstelle können Sie Ihre Protokolle beim Durchlaufen des Systems anzeigen. Sie zeigen Protokolle mithilfe des Protokoll-Tailings (Liveanzeige der aktuellen letzten Protokollzeilen) an. 

**Anmerkung:** Mit dem Serviceplan **Kostenfrei** können Sie nur Ihre neuesten Protokolle per Protokoll-Tailing (Liveanzeige der aktuellen letzten Protokollzeilen) anzeigen.

Weitere Informationen finden Sie unter [Protokolle anzeigen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs).


## Nächste Schritte
{: #ubuntu_next_steps}

[Protokolle filtern](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [Protokolle durchsuchen](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [Ansichten definieren](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7) und [Alerts konfigurieren](https://docs.logdna.com/docs/alerts). 

**Anmerkung:** Damit diese Features verwendet werden können, müssen Sie ein Upgrade des {{site.data.keyword.la_full_notm}}-Plans auf einen kostenpflichtigen Plan durchführen.

