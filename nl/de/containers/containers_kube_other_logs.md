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


# Automatische Erfassung von Clusterprotokollen aktivieren
{: #containers_kube_other_logs}

Um Clusterprotokolle im {{site.data.keyword.loganalysisshort}}-Service anzeigen und analysieren zu können, müssen Sie den Cluster so konfigurieren, dass diese Protokolle an den {{site.data.keyword.loganalysisshort}}-Service weitergeleitet werden. 
{:shortdesc}

## Schritt 1: Berechtigungen für Ihre Benutzer-ID überprüfen
{: step1}

Ihre Benutzer-ID muss über die folgenden Berechtigungen verfügen, damit Sie dem Cluster eine Protokollierungskonfiguration hinzufügen können:

* IAM-Richtlinie für den {{site.data.keyword.containershort}} mit Berechtigungen als **Anzeigeberechtigter**.
* IAM-Richtlinie für die Cluster-Instanz mit den Berechtigungen als **Administrator** oder **Operator**.

Führen Sie die folgenden Schritte aus, um zu überprüfen, ob Ihre Benutzer-ID über diese IAM-Richtlinien verfügt:

**Hinweis:** Nur der Kontoeigner oder Benutzer mit Berechtigungen zum Zuweisen von Richtlinien können diese Aktion durchführen.

1. Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an. Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window}
	
	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

2. Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**.  Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
3. Wählen Sie die Benutzer-ID aus und stellen Sie sicher, dass diese über Richtlinien verfügt.




## Schritt 2: Clusterkontext einrichten
{: #step2}

Führen Sie die folgenden Schritte aus:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Initialisieren Sie das Plug-in für den {{site.data.keyword.loganalysisshort}}-Service.

	```
	ibmcloud ks init
	```
	{: codeblock}

3. Legen Sie den Terminalkontext für den Cluster fest.
    
	```
	ibmcloud ks cluster-config ClusterName
	```
	{: codeblock}

    Die Ausgabe dieses Befehls stellt den Befehl bereit, den Sie im Terminal zum Festlegen des Pfads zur Konfigurationsdatei ausführen müssen. Für einen Cluster mit dem Namen *MyCluster* beispielsweise:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

4. Kopieren Sie den Befehl und fügen Sie ihn ein, um die Umgebungsvariable in Ihrem Terminal festzulegen, und drücken Sie dann die **Eingabetaste**.



## Schritt 3: Cluster konfigurieren
{: step3}

Sie können festlegen, welche Clusterprotokolle an den {{site.data.keyword.loganalysisshort}}-Service weitergeleitet werden sollen. 

* Informationen zur automatischen Protokollerfassung und Weiterleitung von 'stdout' und 'stderr' finden Sie unter [Automatische Protokollerfassung und Weiterleitung von Containerprotokollen aktivieren](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#containers).
* Informationen zur automatischen Erfassung von Protokollen und Weiterleitung von Anwendungsprotokollen finden Sie unter [Automatische Erfassung von Protokollen und Weiterleitung von Anwendungsprotokollen aktivieren](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#apps).
* Informationen zur automatischen Erfassung von Protokollen und Weiterleitung von Workerprotokollen finden Sie unter [Automatische Erfassung von Protokollen und Weiterleitung von Workerprotokollen aktivieren](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#workers).
* Informationen zur automatischen Erfassung von Protokollen und Weiterleitung von Protokollen von Kubernetes-Systemkomponenten finden Sie unter [Automatische Erfassung von Protokollen und Weiterleitung von Protokollen von Kubernetes-Systemkomponenten aktivieren](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#system).
* Informationen zur automatischen Erfassung von Protokollen und Weiterleitung von Kubernetes-Ingress-Controllerprotokollen finden Sie unter [Automatische Erfassung von Protokollen und Weiterleitung von Kubernetes-Ingress-Controllerprotokollen aktivieren](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kube_other_logs#controller).



## Schritt 4: Berechtigungen für den {{site.data.keyword.containershort_notm}}-Schlüsseleigner einrichten
{: #step4}


Der {{site.data.keyword.containershort}}-Schlüsseleigner benötigt die folgenden IAM-Richtlinien:

* IAM-Richtlinie für den {{site.data.keyword.containershort}} mit der Rolle als **Administartor**.
* IAM-Richtlinie für den {{site.data.keyword.loganalysisshort}}-Service mit der Rolle als **Administrator**.

Führen Sie die folgenden Schritte aus: 

1. Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an. Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window}
	
	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

2. Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**.  Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
3. Wählen Sie die Benutzer-ID für den {{site.data.keyword.containershort_notm}}-Schlüsseleigner aus und stellen Sie sicher, dass diese über Richtlinien verfügt.


Wenn Sie Protokolle an eine Bereichsdomäne weiterleiten, müssen Sie auch Cloud Foundry (CF)-Berechtigungen an den {{site.data.keyword.containershort}}-Schlüsseleigner in der Organisation und im Bereich erteilen. Der Schlüsseleigner benötigt die Rolle *orgManager* für die Organisation sowie die Rollen *SpaceManager* oder *Developer* für den Bereich.

Führen Sie die folgenden Schritte aus:

1. Identifizieren Sie den Benutzer in dem Konto, der der {{site.data.keyword.containershort}}-Schlüsseleigner ist. Führen Sie über ein Terminal den folgenden Befehl aus:

    ```
    ibmcloud ks api-key-info ClusterName
    ```
    {: codeblock}
    
    Dabei ist *ClusterName* der Name des Clusters.
    
2. Überprüfen Sie, ob der als {{site.data.keyword.containershort}}-Schlüsseleigner identifizierte Benutzer über die Rollen *Organisationsmanager* für die Organisation sowie *Bereichsmanager* und *Entwickler* für den Bereich verfügt.

    Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an. Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window} Nachdem Sie sich mit Ihrer Benutzer-ID und Ihrem Kennwort angemeldet haben, wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

    Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**.  Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
    Wählen Sie die ID des Benutzers aus und überprüfen Sie, ob der Benutzer über die Rolle *Organisationsmanager* für die Organisation sowie die Rollen *Bereichsmanager* oder *Entwickler* für den Bereich verfügt.
 
3. Wenn der Benutzer nicht über die richtigen Berechtigungen verfügt, führen Sie die folgenden Schritte aus:

    1. Erteilen Sie dem Benutzer die folgenden Berechtigungen: die Rolle *Organisationsmanager* für die Organisation sowie die Rollen *Bereichsmanager* und *Entwickler* für den Bereich. Weitere Informationen finden Sie unter [Einem Benutzer Berechtigungen zum Anzeigen von Bereichsprotokollen unter Verwendung der IBM Cloud-Benutzerschnittstelle erteilen](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space).
    
    2. Aktualisieren Sie die Protokollierungskonfiguration. Führen Sie den folgenden Befehl aus:
    
        ```
        ibmcloud ks logging-config-refresh ClusterName
        ```
        {: codeblock}
        
        Dabei ist *ClusterName* der Name des Clusters.
  




## Automatische Erfassung von Protokollen und Weiterleitung von Containerprotokollen aktivieren 
{: #containers}

Führen Sie den folgenden Befehl aus, um *stdout*- und *stderr*-Protokolldateien an den {{site.data.keyword.loganalysisshort}}-Service zu senden:

```
ibmcloud ks logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

Dabei gilt: 

* *ClusterName* ist der Name des Clusters.
* *EndPoint* ist die URL zum Protokollierungsservice in der Region, in der der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Eine Liste der Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* ist der Name der Organisation, in der der Bereich verfügbar ist.
* *SpaceName* ist der Name des Bereichs, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist.


Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die 'stdout'- und 'stderr'-Protokolle an die Kontodomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}

Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die 'stdout'- und 'stderr'-Protokolle an eine Bereichsdomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace
```
{: screen}



## Automatische Erfassung von Protokollen und Weiterleitung von Anwendungsprotokollen aktivieren 
{: #apps}

Führen Sie die folgenden Befehl aus, um die Protokolldateien */var/log/apps/**/.log* und */var/log/apps/*/.err* an den {{site.data.keyword.loganalysisshort}}-Service zu senden:

```
ibmcloud ks logging-config-create ClusterName --logsource application --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName --app-containers --app-paths
```
{: codeblock}

Dabei gilt: 

* *ClusterName* ist der Name des Clusters.
* *EndPoint* ist die URL zum Protokollierungsservice in der Region, in der der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Eine Liste der Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* ist der Name der Organisation, in der der Bereich verfügbar ist.
* *SpaceName* ist der Name des Bereichs, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist.
* *app-containers* ist ein optionaler Parameter, den Sie festlegen können, um eine Liste von Containern definieren können, die Sie überwachen möchten. Diese Container sind die einzigen, von denen Protokolle an {{site.data.keyword.loganalysisshort}} weitergeleitet werden. Sie können einen oder mehrere Container festlegen, indem Sie sie durch Kommas trennen.
* *app-paths* definiert die Pfade in den Container, die Sie überwachen möchten. Sie können einen oder mehrere Pfade angeben und durch Kommas trennen. Platzhalterzeichen, wie '/var/log/*.log', werden akzeptiert. 

Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Anwendungsprotokolle an eine Bereichsdomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org MyOrg --space MySpace --app-paths /var/log/*.log
```
{: screen}

Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Anwendungsprotokolle an die Kontodomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource application --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --app-paths /var/log/*.log
```
{: screen}



## Automatische Erfassung von Protokollen und Weiterleitung von Workerprotokollen aktivieren 
{: #workers}


Führen Sie den folgenden Befehl aus, um die Protokolldateien */var/log/syslog* und */var/log/auth.log* an den {{site.data.keyword.loganalysisshort}}-Service zu senden:

```
ibmcloud ks logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

Dabei gilt: 

* *ClusterName* ist der Name des Clusters.
* *EndPoint* ist die URL zum Protokollierungsservice in der Region, in der der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Eine Liste der Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* ist der Name der Organisation, in der der Bereich verfügbar ist.
* *SpaceName* ist der Name des Bereichs, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist.



Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Workerprotokolle an eine Bereichsdomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Workerprotokolle an die Kontodomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource worker  --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Automatische Erfassung von Protokollen und Weiterleitung von Protokollen von Kubernetes-Systemkomponenten aktivieren
{: #system}

Führen Sie den folgenden Befehl aus, um die Protokolldateien */var/log/kubelet.log* und */var/log/kube-proxy.log* an den {{site.data.keyword.loganalysisshort}}-Service zu senden:

```
ibmcloud ks logging-config-create ClusterName --logsource kubernetes --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
```
{: codeblock}

Dabei gilt: 

* *ClusterName* ist der Name des Clusters.
* *EndPoint* ist die URL zum Protokollierungsservice in der Region, in der der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Eine Liste der Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* ist der Name der Organisation, in der der Bereich verfügbar ist.
* *SpaceName* ist der Name des Bereichs, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist.



Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Protokolle von Kubernetes-Systemkomponenten an eine Bereichsdomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Protokolle von Kubernetes-Systemkomponenten an die Kontodomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyCluster --logsource kubernetes --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 
```
{: screen}



## Automatische Erfassung von Protokollen und Weiterleitung von Protokollen von Kubernetes-Systemkomponenten aktivieren
{: #controller}

Führen Sie den folgenden Befehl aus, um die Protokolldateien */var/log/alb/ids/.log*, */var/log/alb/ids/.err*, */var/log/alb/customerlogs/.log* und '/var/log/alb/customerlogs/.err*' an den {{site.data.keyword.loganalysisshort}}-Service zu senden:

```
ibmcloud ks logging-config-create ClusterName --logsource ingress --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName
```
{: codeblock}

Dabei gilt: 

* *ClusterName* ist der Name des Clusters.
* *EndPoint* ist die URL zum Protokollierungsservice in der Region, in der der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Eine Liste der Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
* *OrgName* ist der Name der Organisation, in der der Bereich verfügbar ist.
* *SpaceName* ist der Name des Bereichs, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist.



Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Protokolle des Ingress-Controllers an eine Bereichsdomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091 --org OrgName --space SpaceName 
```
{: screen}

Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Protokolle des Ingress-Controllers an die Kontodomäne in der Region "Deutschland" weiterleitet:

```
ibmcloud ks logging-config-create MyLoggingDemoCluster --logsource ingress --type ibm --hostname ingest-eu-fra.logging.bluemix.net --port 9091  
```
{: screen}



