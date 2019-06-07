---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# Von einem Kubernetes-Cluster verwendeten Aufnahmeschlüssel zur Weiterleitung von Protokollen an eine {{site.data.keyword.la_full_notm}}-Instanz zurücksetzen
{: #kube_reset}

Wenn der Aufnahmeschlüssel, den Sie zum Weiterleiten von Protokollen aus einem Cluster an eine {{site.data.keyword.la_full_notm}}-Instanz in {{site.data.keyword.cloud_notm}} verwenden, beschädigt ist, müssen Sie den Schlüssel zurücksetzen und die Konfiguration des Kubernetes-Clusters aktualisieren, damit der neue Aufnahmeschlüssel verwendet wird. 
{:shortdesc}

## Vorbereitende Schritte
{: #kube_reset_prereqs}

Arbeiten Sie in der Region US-South. Beide Ressourcen, die {{site.data.keyword.la_full_notm}}-Instanz und der Kubernetes-Cluster, müssen in demselben Konto ausgeführt werden.

Die {{site.data.keyword.la_full_notm}}-Instanz wird in der Ressourcengruppe **Standard** bereitgestellt.

Informieren Sie sich über {{site.data.keyword.la_full_notm}}. Weitere Informationen finden Sie in [Informationen zu LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Damit Sie die Schritte in diesem Lernprogramm ausführen können, müssen Ihrer {{site.data.keyword.IBM_notm}} ID IAM-Richtlinien für jede der folgenden Ressourcen zugeordnet sein: 

| Ressource                             | Geltungsbereich der Zugriffsrichtlinie | Rollen    | Region    | Informationen                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Ressourcengruppe **Standard**           |  Ressourcengruppe            | Anzeigeberechtigter  | us-south  | Diese Richtlinie ist erforderlich, damit der Benutzer Serviceinstanzen in der Ressourcengruppe Standard anzeigen kann.    |
| {{site.data.keyword.la_full_notm}}-Service |  Ressourcengruppe            | Bearbeiter </br>Manager  | us-south  | Diese Richtlinie ist erforderlich, damit der Benutzer den Aufnahmeschlüssel zurücksetzen kann.   |
| Kubernetes-Clusterinstanz          |  Ressource                  | Bearbeiter  | us-south  | Diese Richtlinie ist erforderlich, um den geheimen Schlüssel und den LogDNA-Agenten im Kubernetes-Cluster löschen und konfigurieren zu können. |
{: caption="Tabelle 1. Liste der für das Lernprogramm erforderlichen IAM-Richtlinien" caption-side="top"} 

Weitere Informationen zu den IAM-Rollen von {{site.data.keyword.containerlong}} finden Sie in [Benutzerzugriffsberechtigungen](/docs/containers?topic=containers-access_reference#access_reference).

Installieren Sie die Befehlszeilenschnittstelle (CLI) von {{site.data.keyword.cloud_notm}} und das Kubernetes-CLI-Plug-in. Weitere Informationen finden Sie in [{{site.data.keyword.cloud_notm}}-CLI installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).


## Schritt 1: Aufnahmeschlüssel zurücksetzen
{: #kube_reset_step1}

Führen Sie die folgenden Schritte aus, um den Aufnahmeschlüssel für eine {{site.data.keyword.la_full_notm}}-Instanz über die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} zu erneuern:

1. Starten Sie die Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}}. Weitere Informationen finden Sie unter [Webbenutzerschnittstelle von {{site.data.keyword.la_full_notm}} starten](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Wählen Sie das Symbol **Konfiguration** aus. Wählen Sie dann **Organisation** aus. 

3. Wählen Sie **API-Schlüssel** aus.

    Die erstellten Aufnahmeschlüssel werden angezeigt. 

4. Wählen Sie **Aufnahmeschlüssel generieren** aus.

    Der Liste wird ein neuer Schlüssel hinzugefügt.

5. Löschen Sie den alten Aufnahmeschlüssel. Klicken Sie auf **Löschen**.


## Schritt 2: Alle Konfigurationen im Cluster entfernen, in denen der alte Aufnahmeschlüssel verwendet wird
{: #kube_reset_step2}

Führen Sie die folgenden Schritte aus:

1. Öffnen Sie ein Terminal. Melden Sie sich dann bei {{site.data.keyword.cloud_notm}} an. Führen Sie den folgenden Befehl aus und folgen Sie den Eingabeaufforderungen:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Wählen Sie das Konto aus, in dem Sie die {{site.data.keyword.la_full_notm}}-Instanz bereitgestellt haben.

2. Richten Sie die Clusterumgebung ein. Führen Sie die folgenden Befehle aus:

    Führen Sie zunächst den Befehl zur Angabe der Umgebungsvariablen und zum Herunterladen der Kubernetes-Konfigurationsdateien aus.

    ```
    ibmcloud ks cluster-config <Clustername_oder_-ID>
    ```
    {: codeblock}

    Sobald der Download der Konfigurationsdateien beendet ist, wird ein Befehl angezeigt, mit dem Sie den Pfad zur lokalen Kubernetes-Konfigurationsdatei als Umgebungsvariable festlegen können.

    Kopieren Sie dann den Befehl, der in Ihrem Terminal angezeigt wird, und fügen Sie ihn ein, um die Umgebungsvariable KUBECONFIG zu definieren.

    **Anmerkung:** Sie müssen diese Befehle, mit denen der Pfad zur Konfigurationsdatei des Clusters als Sitzungsvariable definiert wird, bei jeder Anmeldung bei der Befehlszeilenschnittstelle von {{site.data.keyword.containerlong}} für die Arbeit mit Clustern ausführen. Diese Variable wird in der Kubernetes-Befehlszeilenschnittstelle verwendet, um eine lokale Konfigurationsdatei und Zertifikate zu finden, die für die Verbindung zum Cluster in {{site.data.keyword.cloud_notm}} erforderlich sind.

3. Entfernen Sie den geheimen Schlüssel aus dem Kubernetes-Cluster. Der geheime Kubernetes-Schlüssel enthält den LogDNA-Aufnahmeschlüssel. Führen Sie den folgenden Befehl aus:

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Entfernen Sie den LogDNA-Agenten auf jedem Worker (Knoten) Ihres Kubernetes-Clusters. Der LogDNA-Agent ist für die Erfassung und Weiterleitung Ihrer Protokolle zuständig. Führen Sie den folgenden Befehl aus:

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. Überprüfen Sie, ob der LogDNA-Agent erfolgreich gelöscht wurde. Führen Sie den folgenden Befehl aus:

    ```
    kubectl get pods
    ```
    {: codeblock}

    Es sollten keine LogDNA-Pods angezeigt werden.


## Schritt 3: Kubernetes-Cluster mit dem neuen Aufnahmeschlüssel konfigurieren
{: #kube_reset_step3}

Führen Sie die folgenden Schritte über die Befehlszeile aus, wenn Sie Ihren Kubernetes-Cluster so konfigurieren möchten, dass Protokolle an Ihre LogDNA-Instanz weitergeleitet werden:

1. Öffnen Sie ein Terminal. Melden Sie sich dann bei {{site.data.keyword.cloud_notm}} an. Führen Sie den folgenden Befehl aus und folgen Sie den Eingabeaufforderungen:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Wählen Sie das Konto aus, in dem Sie die {{site.data.keyword.la_full_notm}}-Instanz bereitgestellt haben.

2. Richten Sie die Clusterumgebung ein. Führen Sie die folgenden Befehle aus:

    Führen Sie zunächst den Befehl zur Angabe der Umgebungsvariablen und zum Herunterladen der Kubernetes-Konfigurationsdateien aus.

    ```
    ibmcloud ks cluster-config <Clustername_oder_-ID>
    ```
    {: codeblock}

    Sobald der Download der Konfigurationsdateien beendet ist, wird ein Befehl angezeigt, mit dem Sie den Pfad zur lokalen Kubernetes-Konfigurationsdatei als Umgebungsvariable festlegen können.

    Kopieren Sie dann den Befehl, der in Ihrem Terminal angezeigt wird, und fügen Sie ihn ein, um die Umgebungsvariable KUBECONFIG zu definieren.

    **Anmerkung:** Sie müssen diese Befehle, mit denen der Pfad zur Konfigurationsdatei des Clusters als Sitzungsvariable definiert wird, bei jeder Anmeldung bei der Befehlszeilenschnittstelle von {{site.data.keyword.containerlong}} für die Arbeit mit Clustern ausführen. Diese Variable wird in der Kubernetes-Befehlszeilenschnittstelle verwendet, um eine lokale Konfigurationsdatei und Zertifikate zu finden, die für die Verbindung zum Cluster in {{site.data.keyword.cloud_notm}} erforderlich sind.

3. Fügen Sie einen geheimen Schlüssel in Ihrem Kubernetes-Cluster hinzu. Führen Sie den folgenden Befehl aus:

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE zeigt den LogDNA-Aufnahmeschlüssel für Ihre Instanz.

    Der geheime Kubernetes-Schlüssel enthält den LogDNA-Aufnahmeschlüssel. Mit dem LogDNA-Aufnahmeschlüssel wird der Protokollierungsagent im {{site.data.keyword.la_full_notm}}-Service authentifiziert. Er dient zum Öffnen eines sicheren Web-Socket für den Aufnahmeserver auf dem Protokollierungs-Back-End-System.

4. Konfigurieren Sie den LogDNA-Agenten auf jedem Worker (Knoten) Ihres Kubernetes-Clusters. Führen Sie den folgenden Befehl aus:

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    Der LogDNA-Agent ist für die Erfassung und Weiterleitung Ihrer Protokolle zuständig.

    Der Agent erfasst Protokolle mit der Erweiterung *.log und Dateien ohne Erweiterung in /var/log automatisch. Protokolle werden standardmäßig aus allen Namensbereichen erfasst, einschließlich Kube-System.

5. Überprüfen Sie, ob der LogDNA-Agent erfolgreich erstellt wurde, und seinen Status. Führen Sie den folgenden Befehl aus:

    ```
    kubectl get pods
    ```
    {: codeblock}


## Schritt 4: LogDNA-Webbenutzerschnittstelle starten
{: #kube_reset_step4}

Führen Sie die folgenden Schritte aus, um das IBM Log Analysis with LogDNA-Dashboard über die {{site.data.keyword.cloud_notm}}-Benutzerschnittstelle zu starten:

1. Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an.

    Klicken Sie auf [{{site.data.keyword.cloud_notm}}-Dashboard ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}, um das {{site.data.keyword.cloud_notm}}-Dashboard zu starten.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird das {{site.data.keyword.cloud_notm}}-Dashboard geöffnet.

2. Wählen Sie im Navigationsmenü **Beobachtbarkeit** aus. 

3. Wählen Sie **Protokollierung** aus. 

    Die Liste der in {{site.data.keyword.cloud_notm}} verfügbaren {{site.data.keyword.la_full_notm}}-Instanzen wird angezeigt.

3. Wählen Sie eine Instanz aus. Klicken Sie dann auf **Protokolle anzeigen**.

    Die LogDNA-Webbenutzerschnittstelle wird geöffnet, in der Ihre Clusterprotokolle angezeigt werden.


## Schritt 5: Protokolle anzeigen
{: #kube_reset_step5}

Über die LogDNA-Webbenutzerschnittstelle können Sie Ihre Protokolle beim Durchlaufen des Systems anzeigen. Sie zeigen Protokolle mithilfe des Protokoll-Tailings (Liveanzeige der aktuellen letzten Protokollzeilen) an. 

**Anmerkung:** Mit dem Serviceplan **Kostenfrei** können Sie nur Ihre neuesten Protokolle per Protokoll-Tailing (Liveanzeige der aktuellen letzten Protokollzeilen) anzeigen.



## Nächste Schritte
{: #kube_reset_next_steps}

  Wenn Sie [Clusterprotokolle filtern](https://docs.logdna.com/docs/filters), [Clusterprotokolle durchsuchen](https://docs.logdna.com/docs/search), [Ansichten definieren](https://docs.logdna.com/docs/views) und [Alerts konfigurieren](https://docs.logdna.com/docs/alerts) wollen, müssen Sie ein Upgrade des {{site.data.keyword.la_full_notm}}-Plans auf einen kostenpflichtigen Plan durchführen.



