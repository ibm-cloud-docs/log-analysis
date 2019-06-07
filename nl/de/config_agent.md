---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# LogDNA-Agenten konfigurieren
{: #config_agent}

Der LogDNA-Agent ist für die Erfassung und Weiterleitung von Protokollen an Ihre {{site.data.keyword.la_full_notm}}-Instanz zuständig. Nachdem Sie eine Instanz von {{site.data.keyword.la_full}} bereitgestellt haben, müssen Sie einen LogDNA-Agenten für jede Protokollquelle, die Sie überwachen wollen, konfigurieren.
{:shortdesc}

* Der LogDNA-Agent wird mit dem LogDNA-Aufnahmeschlüssel authentifiziert und öffnet ein sicheres Web-Socket für die {{site.data.keyword.la_full_notm}}-Aufnahmeserver. 
* Der Agent überwacht standardmäßig alle Dateien mit der Erweiterung *.log* sowie Dateien ohne Erweiterung in */var/log/*.
* Der Agent zeigt neue Protokolldaten per Tailing (Liveanzeige der aktuellen letzten Protokollzeilen) an und sucht neue Dateien, die den von ihm überwachten Protokollverzeichnissen hinzugefügt werden.

Sie können mit dem LogDNA-Agenten die folgenden Parameter konfigurieren: 

| Parameter | Beschreibung |
|-----------|-------------|
| `tags`    | Tags für die automatische Zusammenfassung von Hosts in dynamischen Gruppen definieren. |
| `logdir`  | Angepasste Pfade definieren, die der Agent überwachen soll. </br>Mehrere Pfade werden durch Kommas getrennt. Sie können globale Muster verwenden. Sie können bestimmte Dateien konfigurieren. Globale Muster geben Sie mit Anführungszeichen ein. |
| `exclude` | Dateien definieren, die der LogDNA-Agent nicht überwachen soll. **Anmerkung:** Diese Dateien können sich in jedem der Pfade befinden, die mit dem Parameter 'logdir' definiert sind. </br>Mehrere Dateien werden durch Kommas getrennt. Sie können globale Muster verwenden. Sie können bestimmte Dateien konfigurieren. |
| `exclude_regex` | Regex-Muster definieren, um alle Zeilen herauszufiltern, die mit einem Muster übereinstimmen. Geben Sie keine vorangestellten und abschließenden Schrägstriche (`/`) an. |
| `hostname` | Hostnamen definieren. Dieser Wert überschreibt den Hostnamen des Betriebssystems. |
| `autoupdate` | Bei Angabe von `1` wird der Agent automatisch aktualisiert, wenn die Definition des öffentlichen Repo-Agenten aktualisiert wird. Bei Angabe von `0` wird diese Funktion inaktiviert. |  
{: caption="Tabelle 1. Parameter für die Anpassung eines LogDNA-Agenten" caption-side="top"} 



## LogDNA-Agenten mit einem Script in einem Kubernetes-Cluster konfigurieren
{: #config_agent_kube_script}

Wenn Sie Ihren Kubernetes-Cluster so konfigurieren möchten, dass Protokolle an Ihre {{site.data.keyword.la_full_notm}}-Instanz gesendet werden, müssen Sie auf jedem Knoten des Clusters einen *logdna-agent*-Pod installieren. Der LogDNA-Agent liest Protokolldateien aus dem Pod, in dem er installiert ist, und leitet die Protokolldaten an Ihre LogDNA-Instanz weiter.

Führen Sie die folgenden Schritte über die Befehlszeile aus, wenn Sie Ihren Kubernetes-Cluster so konfigurieren möchten, dass Protokolle an Ihre LogDNA-Instanz weitergeleitet werden:

1. Öffnen Sie ein Terminal für die Anmeldung bei {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Wählen Sie das Konto aus, in dem Sie die {{site.data.keyword.la_full_notm}}-Instanz bereitgestellt haben.

2. Legen Sie den Cluster fest, in dem Sie die Protokollierung als Kontext für diese Sitzung konfigurieren wollen.

   ```
   ibmcloud ks cluster-config <Clustername_oder_-ID>
   ```
   {: pre}

   Sobald der Download der Konfigurationsdateien beendet ist, wird ein Befehl angezeigt, mit dem Sie den Pfad zur lokalen Kubernetes-Konfigurationsdatei als Umgebungsvariable festlegen können. Kopieren Sie den Befehl, der in Ihrem Terminal angezeigt wird, und fügen Sie ihn ein, um die Umgebungsvariable `KUBECONFIG` zu definieren.

3. Erstellen Sie einen geheimen Kubernetes-Schlüssel, um den logDNA-Aufnahmeschlüssel für Ihre Serviceinstanz speichern zu können. Mit dem LogDNA-Aufnahmeschlüssel wird ein sicheres Web-Socket für den logDNA-Aufnahmeserver geöffnet und der Protokollierungsagent im {{site.data.keyword.la_full_notm}}-Service authentifiziert.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA-Aufnahmeschlüssel>
    ```
    {: pre}

4. Erstellen Sie einen Kubernetes-Dämon, um den LogDNA-Agenten auf jedem Workerknoten Ihres Kubernetes-Clusters zu implementieren. Der LogDNA-Agent sammelt Protokolle mit der Erweiterung `*.log` und Dateien ohne Erweiterung, die im Verzeichnis `/var/log` Ihres Pods gespeichert sind. Protokolle werden standardmäßig aus allen Namensbereichen erfasst, einschließlich `Kube-System`, und automatisch an den {{site.data.keyword.la_full_notm}}-Service weitergeleitet.

    <table>
      <caption>Befehle nach Region</caption>
      <tr>
        <th>Standort</th>
        <th>Befehl</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-eu-de.yaml`</td>
      </tr>
    </table>

5. Überprüfen Sie, ob der LogDNA-Agent erfolgreich implementiert wurde. 

   ```
   kubectl get pods
   ```
   {: pre}
   

Die Implementierung ist erfolgreich, wenn mindestens ein LogDNA-Pod angezeigt wird.
* **Die Anzahl der LogDNA-Pods entspricht der Anzahl Workerknoten in Ihrem Cluster. ** 
* Alle Pods müssen sich im Status `Aktiv` befinden.
* Die Standardausgabe (*stdout*) und die Standard-Fehlerausgabe (*stderr*) werden automatisch erfasst und von allen Containern weitergeleitet. Protokolldaten umfassen Anwendungsprotokolle und Workerprotokolle. 
* Der LogDNA-Agentenpod, der auf einem Workerknoten ausgeführt wird, erfasst standardmäßig Protokolle aus allen Namensbereichen auf diesem Knoten, einschließlich Kube-Systemprotokollen.



## Tags einem LogDNA-Agenten in einem Kubernetes-Cluster hinzufügen
{: #config_agent_kube_tags}

Führen Sie die folgenden Schritte aus, um Tags hinzuzufügen:

1. Richten Sie die Clusterumgebung ein. Führen Sie die folgenden Befehle aus:

    Führen Sie zunächst den Befehl zur Angabe der Umgebungsvariablen und zum Herunterladen der Kubernetes-Konfigurationsdateien aus.

    ```
    ibmcloud ks cluster-config <Clustername_oder_-ID>
    ```
    {: codeblock}

    Sobald der Download der Konfigurationsdateien beendet ist, wird ein Befehl angezeigt, mit dem Sie den Pfad zur lokalen Kubernetes-Konfigurationsdatei als Umgebungsvariable festlegen können.

    Kopieren Sie dann den Befehl, der in Ihrem Terminal angezeigt wird, und fügen Sie ihn ein, um die Umgebungsvariable KUBECONFIG zu definieren.

2. Überprüfen Sie die Aktualisierungsstrategie des DaemonSet. Wählen Sie dann aus, ob *kubectl apply* oder *kubectl edit* für die Änderung der Konfigurationsdatei des Agenten verwendet werden soll.

    Führen Sie den folgenden Befehl aus, um die Aktualisierungsstrategie zu überprüfen:

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    Wenn *OnDelete* für die Aktualisierungsstrategie angegeben ist oder wenn die Konfigurationsdatei durch ein Versionssteuerungssystem verwaltet wird, aktualisieren Sie Ihre lokale Konfigurationsdatei und wenden Sie Änderungen des LogDNA-Agenten mithilfe von *kubectl apply* an.

    Wenn *RollingUpdate* für die Aktualisierungsstrategie angegeben ist, können Sie mithilfe von *kubectl edit* den LogDNA-Agenten aktualisieren und Änderungen auf ihn anwenden.

3. Bearbeiten Sie die Datei `logdna-agent-configmap.yaml`. 

    Aktualisieren Sie die Konfigurationsdatei durch eine Änderung der lokalen Kopie. **Anmerkung:** Sie können die Konfigurationsdatei des Agenten auch mit dem folgenden Befehl generieren:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    Alternativ können Sie die Konfigurationsdatei mithilfe von *kubectl edit* aktualisieren.

    ```
    kubectl edit daemonset logdna-agent
    ```
    {: codeblock}

4. Nehmen Sie Änderungen vor. Fügen Sie den Abschnitt **LOGDNA_TAGS** hinzu.

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    Im folgenden Abschnitt wird gezeigt, wo Tags in der Konfigurationsdatei hinzugefügt werden:

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. Wenden Sie die Konfigurationsänderungen an, wenn Sie die Datei lokal bearbeiten. 

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}
    
    **Anmerkung:** Wenn Sie *kubectl edit* verwenden, werden Änderungen beim Speichern automatisch angewendet.


## LogDNA-Agenten unter Linux Ubuntu oder Debian konfigurieren
{: #config_agent_linux}

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

    <table>
      <caption>Befehle nach Region</caption>
      <tr>
        <th>Standort</th>
        <th>Befehl</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_APIHOST=api.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

4. Geben Sie den Aufnahmeendpunkt an.

    <table>
      <caption>Befehle nach Region</caption>
      <tr>
        <th>Standort</th>
        <th>Befehl</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

5. Definieren Sie weitere zu überwachende Protokollpfade. Führen Sie den folgenden Befehl aus: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    Standardmäßig wird **/var/log** überwacht.

6. Geben Sie in der Konfiguration des LogDNA-Agenten wahlweise an, dass Ihre Hosts mit Tags versehen werden. 


## Tags einem LogDNA-Agenten unter Linux Ubuntu oder Debian hinzufügen
{: #config_agent-linux_tags}
 

Führen Sie die folgenden Schritte aus, um dem LogDNA-Agenten weitere Tags hinzuzufügen:

1. Überprüfen Sie, ob der LogDNA-Agent aktiv ist.

2. Fügen Sie mindestens einen Tag hinzu.

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


Sie können auch die LogDNA-Konfigurationsdatei bearbeiten und Tags hinzufügen. Die Konfigurationsdatei befindet sich in */etc/logdna.conf*.

1. Bearbeiten Sie die Datei.

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. Fügen Sie Tags hinzu.

3. Starten Sie den LogDNA-Agenten erneut.

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














