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


# Protokolle in Kibana für eine App analysieren, die in einem Kubernetes-Cluster bereitgestellt ist
{: #container_logs}
In diesem Lernprogramm erfahren Sie, wie Sie Ihren Cluster so konfigurieren, dass Protokolle an den {{site.data.keyword.loganalysisshort}}-Service in {{site.data.keyword.Bluemix_notm}} weitergeleitet werden.
{:shortdesc}


## Zielsetzungen
{: #objectives}

1. Protokollierungskonfigurationen in einem Cluster konfigurieren. 
2. Containerprotokolle für eine App, die in einem Kubernetes-Cluster bereitgestellt ist, in {{site.data.keyword.Bluemix_notm}} suchen und analysieren.

In diesem Lernprogramm werden die Schritte gezeigt, die erforderlich sind, um das folgende End-to-End-Szenario in {{site.data.keyword.Bluemix_notm}} umzusetzen: einen Cluster bereitstellen, den Cluster für das Senden von Protokollen an den {{site.data.keyword.loganalysisshort}}-Service in {{site.data.keyword.Bluemix_notm}} konfigurieren, eine App im Cluster bereitstellen und Kibana zum Anzeigen und Filtern von Containerprotokollen für diesen Cluster verwenden.


**Hinweis:** Zur vollständigen Durchführung dieses Lernprogramms müssen Sie alle Vorbedingungen erfüllen und die Lernprogramme durchführen, zu denen Sie in den jeweiligen Schritten über Links geführt werden.


## Voraussetzungen
{: #prereq}

1. Werden Sie Mitglied oder Eigner eines {{site.data.keyword.Bluemix_notm}}-Kontos mit Berechtigungen für das Erstellen von Kubernetes-Standardclustern, das Bereitstellen von Anwendungen in Clustern und das Abfragen der Protokolle in {{site.data.keyword.Bluemix_notm}} für die erweiterte Analyse in Kibana.

    Ihrer Benutzer-ID für {{site.data.keyword.Bluemix_notm}} müssen die folgenden Richtlinien zugewiesen sein:
    
    * Eine IAM-Richtlinie für den {{site.data.keyword.containershort}} mit den Berechtigungen *editor*, *operator* oder *administrator*.
    * Eine CF-Rolle für den Bereich, in dem der {{site.data.keyword.loganalysisshort}}-Service mit *Entwickler*-Berechtigungen bereitgestellt wird.
    
    Weitere Informationen finden Sie unter [Einem Benutzer eine IAM-Richtlinie über die IBM Cloud-Benutzerschnittstelle zuweisen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account) und [Einem Benutzer Berechtigungen zum Anzeigen von Bereichsprotokollen unter Verwendung der IBM Cloud-Benutzerschnittstelle erteilen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).

2. Führen Sie eine Terminalsitzung durch, von der aus Sie den Kubernetes-Cluster verwalten und Apps über die Befehlszeile bereitstellen können. Die Beispiele in diesem Lernprogramm sind für ein Ubuntu Linux-System ausgelegt.

3. Installieren Sie die CLIs für die Arbeit mit dem {{site.data.keyword.containershort}} und {{site.data.keyword.loganalysisshort}} in Ihrem Ubuntu-System.

    * Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle. Installieren Sie die {{site.data.keyword.containershort}}-CLI, um Ihre Kubernetes-Cluster in {{site.data.keyword.containershort}} zu erstellen und zu verwalten und um containerisierte Apps für Ihren Cluster bereitzustellen. Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle installieren](/docs/cli/index.html#overview).
    
    * Installieren Sie die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle. Weitere Informationen finden Sie unter [Log Analysis-CLI (IBM Cloud-Plug-in) konfigurieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli).
    
4. Sie müssen Zugriff auf einen Bereich mit dem Namen **dev** in Ihrem Konto in der Region "USA (Süden)" haben. 

    Protokolle, die in diesem Cluster verfügbar sind, werden so konfiguriert, dass sie an die Bereichsdomäne weitergeleitet werden, die diesem Bereich zugeordnet ist. 
    
    In diesem Bereich stellen Sie den {{site.data.keyword.loganalysisshort}}-Service bereit.
    
    Sie müssen über **Entwickler**-Berechtigungen in diesem Bereich verfügen, sodass Sie den {{site.data.keyword.loganalysisshort}}Service bereitstellen können.
    
    Im Lernprogramm ist der verwendete Name der Organisation **MyOrg**.

    
 

## Schritt 1: Bereitstellung in einem Kubernetes-Cluster
{: #step25}

Führen Sie die folgenden Schritte aus:

1. Erstellen Sie einen Standard-Kubernetes-Cluster.

   Weitere Informationen finden Sie unter [Cluster erstellen](/docs/containers/cs_tutorials.html#cs_cluster_tutorial).

2. Richten Sie den Clusterkontext in einem Terminal ein. Nachdem der Kontext festgelegt ist, können Sie den Kubernetes-Cluster verwalten und die Anwendung im Kubernetes-Cluster bereitstellen.

    Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an, die/der dem von Ihnen erstellten Cluster zugeordnet ist. Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

	Initialisieren Sie das Plug-in für den {{site.data.keyword.containershort}}-Service.

	```
	ibmcloud cs init
	```
	{: codeblock}

    Legen Sie den Terminalkontext für den Cluster fest.
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    Die Ausgabe dieses Befehls stellt den Befehl bereit, den Sie im Terminal zum Festlegen des Pfads zur Konfigurationsdatei ausführen müssen. Beispiel:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    Kopieren Sie den Befehl und fügen Sie ihn ein, um die Umgebungsvariable in Ihrem Terminal festzulegen, und drücken Sie dann die **Eingabetaste**.



## Schritt 2: Ihren Cluster für die automatische Weiterleitung von Protokollen an den {{site.data.keyword.loganalysisshort}}-Service konfigurieren
{: #step26}

Wenn die App bereitgestellt wird, werden Protokolle automatisch vom {{site.data.keyword.containershort}} erfasst. Jedoch werden Protokolle nicht automatisch an den {{site.data.keyword.loganalysisshort}}-Service weitergeleitet. Sie müssen mindestens eine Protokollierungskonfiguration in Ihrem Cluster erstellen, die Folgendes definiert:

* Wohin die Protokolle weitergeleitet werden sollen. Sie können Protokolle an die Kontodomäne oder an eine Bereichsdomäne weiterleiten.
* Welche Protokolle an den {{site.data.keyword.loganalysisshort}}-Service zur Analyse weitergeleitet werden sollen.


Bevor Sie Protokollierungskonfigurationen definieren, überprüfen Sie Ihre aktuellen Definitionen für die Protokollierungskonfiguration im Cluster. Führen Sie den folgenden Befehl aus:

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

Dabei ist *ClusterName* der Name Ihres Clusters.

Zum Beispiel sind die Protokollierungskonfigurationen, die für den Cluster *mycluster* definiert werden, die folgenden: 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

Informationen zum Anzeigen der Liste von Protokollquellen, für die Sie eine Protokollierungskonfiguration definieren können, finden Sie unter [Protokollquellen](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_sources).


### Konfigurieren Sie Ihren Cluster so, dass 'stderr'- und 'stdout'-Protokolle an den {{site.data.keyword.loganalysisshort}}-Service weitergeleitet werden
{: #containerstd}


Führen Sie die folgenden Schritte aus, um 'stdout'- und 'stderr'-Protokolle an eine Bereichsdomäne zu senden, wobei der Name der Organisation *MyOrg* und der Name des Bereichs *dev* in der Region "USA (Süden)" ist:

1. Überprüfen Sie, ob Ihre Benutzer-ID über Berechtigungen zum Hinzufügen einer Clusterkonfiguration verfügt. Nur Benutzer mit einer IAM-Richtlinie für den {{site.data.keyword.containershort}} mit Berechtigungen zum Verwalten von Clustern können diese Funktion aktivieren. Dazu ist mindestens eine der folgenden Rollen erforderlich: *Administrator*, *Operator*.

    Führen Sie die folgenden Schritte aus, um zu überprüfen, ob Ihrer Benutzer-ID eine IAM-Richtlinie zum Verwalten von Clustern zugewiesen ist:
    
    1. Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an. Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window} Nachdem Sie sich mit Ihrer Benutzer-ID und Ihrem Kennwort angemeldet haben, wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

    2. Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**.  Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
    3. Wählen Sie die Benutzer-ID aus und stellen Sie sicher, dass diese über eine Richtlinie für den {{site.data.keyword.containershort}} verfügt.

    Wenn Sie Berechtigungen benötigen, kontaktieren Sie den Kontoeigner oder einen Kontoadministrator. Nur der Kontoeigner oder Benutzer mit Berechtigungen zum Zuweisen von Richtlinien können diese Aktion durchführen.

2. Erstellen Sie eine Protokollierungskonfiguration für den Cluster. Führen Sie den folgenden Befehl aus, um *stdout*- und *stderr*-Protokolldateien an den {{site.data.keyword.loganalysisshort}}-Service zu senden:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    Dabei gilt: 

    * *ClusterName* ist der Name des Clusters.
    * *EndPoint* ist die URL zum Protokollierungsservice in der Region, in der der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Eine Liste der Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
    * *OrgName* ist der Name der Organisation, in der der Bereich verfügbar ist.
    * *SpaceName* ist der Name des Bereichs, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist.


Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die 'stdout'- und 'stderr'-Protokolle an 'space dev' in der Region "USA (Süden)" weiterleitet:

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### Konfigurieren Sie Ihren Cluster so, dass Workerprotokolle an den {{site.data.keyword.loganalysisshort}}-Service weitergeleitet werden
{: #workerlogs }

Führen Sie die folgenden Schritte aus, um Workerprotokolle an eine Bereichsdomäne zu senden, wobei der Name der Organisation *MyOrg* und der Name des Bereichs *dev* in der Region "USA (Süden)" ist:

1. Überprüfen Sie, ob Ihre Benutzer-ID über Berechtigungen zum Hinzufügen einer Clusterkonfiguration verfügt. Nur Benutzer mit einer IAM-Richtlinie für den {{site.data.keyword.containershort}} mit Berechtigungen zum Verwalten von Clustern können diese Funktion aktivieren. Dazu ist mindestens eine der folgenden Rollen erforderlich: *Administrator*, *Operator*.

    Führen Sie die folgenden Schritte aus, um zu überprüfen, ob Ihrer Benutzer-ID eine IAM-Richtlinie zum Verwalten von Clustern zugewiesen ist:
    
    1. Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an. Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window} Nachdem Sie sich mit Ihrer Benutzer-ID und Ihrem Kennwort angemeldet haben, wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

    2. Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**.  Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
    3. Wählen Sie die Benutzer-ID aus und stellen Sie sicher, dass diese über eine Richtlinie für den {{site.data.keyword.containershort}} verfügt.

    Wenn Sie Berechtigungen benötigen, kontaktieren Sie den Kontoeigner oder einen Kontoadministrator. Nur der Kontoeigner oder Benutzer mit Berechtigungen zum Zuweisen von Richtlinien können diese Aktion durchführen.

2. Erstellen Sie eine Protokollierungskonfiguration für den Cluster. Führen Sie den folgenden Befehl aus, um die Protokolldateien */var/log/syslog* und */var/log/auth.log* an den {{site.data.keyword.loganalysisshort}}-Service zu senden:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    Dabei gilt: 

    * *ClusterName* ist der Name des Clusters.
    * *EndPoint* ist die URL zum Protokollierungsservice in der Region, in der der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist. Eine Liste der Endpunkte finden Sie unter [Endpunkte](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls).
    * *OrgName* ist der Name der Organisation, in der der Bereich verfügbar ist.
    * *SpaceName* ist der Name des Bereichs, in dem der {{site.data.keyword.loganalysisshort}}-Service bereitgestellt ist.

    
Führen Sie zum Beispiel den folgenden Befehl aus, um eine Protokollierungskonfiguration zu erstellen, die Workerprotokolle an die Bereichsdomäne in der Region "USA (Süden)" weiterleitet:

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## Schritt 3: Ihrem Benutzer Berechtigungen erteilen, damit dieser Protokolle in einer Bereichsdomäne anzeigen kann
{: #step33}

Um einem Benutzer Berechtigungen zum Anzeigen von Protokollen in einem Bereich zu erteilen, müssen Sie diesen Benutzer eine Cloud Foundry-Rolle zuweisen, die die Aktionen beschreibt, die dieser Benutzer mit dem {{site.data.keyword.loganalysisshort}}-Service im Bereich ausführen kann. 

Führen Sie die folgenden Schritte aus, um einem Benutzer Berechtigungen für die Arbeit mit dem {{site.data.keyword.loganalysisshort}}-Service zu erteilen:

1. Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an.

    Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window}
	
	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

2. Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**. 

    Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
3. Wenn der Benutzer ein Mitglied des Kontos ist, wählen Sie den Benutzernamen aus der Liste aus oder klicken Sie im Menü *Aktionen* auf **Benutzer verwalten**.

    Wenn der Benutzer kein Mitglied des Kontos ist, finden Sie unter [Benutzer einladen](/docs/iam/iamuserinv.html#iamuserinv) Informationen zum entsprechenden Vorgehen in diesem Fall.

4. Wählen Sie **Cloud Foundry-Zugriff** und anschließend die Organisation aus.

    Die in dieser Organisation verfügbaren Bereiche werden aufgelistet.

5. Wählen Sie den Bereich aus. Anschließend wählen Sie aus der Menüaktion **Bereichsrolle bearbeiten** aus.

    Wenn Ihnen der Bereich für "USA (Süden)" nicht angezeigt wird, erstellen Sie den Bereich, bevor Sie fortfahren.

6. Wählen Sie *Entwickler* aus.

    Sie können eine oder mehrere Rollen auswählen. 
    
    Gültige Rollen sind: *Manager*, *Entwickler* und *Prüfer*
	
7. Klicken Sie auf **Rolle speichern**.


## Schritt 4: Die {{site.data.keyword.containershort_notm}}-Schlüsseleignerberechtigungen erteilen
{: #step52}

Damit Clusterprotokolle an einen Bereich weitergeleitet werden können, muss der {{site.data.keyword.containershort_notm}}-Schlüsseleigner die folgenden Berechtigungen besitzen:

* IAM-Richtlinie für den {{site.data.keyword.loganalysisshort}}-Service mit den Berechtigungen als *Administrator*.
* Cloud Foundry (CF)-Berechtigungen in der Organisation und in dem Bereich, an die die Protokolle weitergeleitet werden. Der Container-Schlüsseleigner benötigt die *orgManager*-Rolle für die Organisation sowie die Rollen *SpaceManager* und *Developer* für den Bereich.

Führen Sie die folgenden Schritte aus:

1. Identifizieren Sie den Benutzer in dem Konto, der der {{site.data.keyword.containershort}}-Schlüsseleigner ist. Führen Sie über ein Terminal den folgenden Befehl aus:

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    Dabei ist *ClusterName* der Name des Clusters.

2. Überprüfen Sie, ob der als {{site.data.keyword.containershort}}-Schlüsseleigner identifizierte Benutzer über die Rollen *Organisationsmanager* für die Organisation sowie *Bereichsmanager* und *Entwickler* für den Bereich verfügt.

    Melden Sie sich bei der {{site.data.keyword.Bluemix_notm}}-Konsole an. Öffnen Sie einen Web-Browser und starten Sie das {{site.data.keyword.Bluemix_notm}}-Dashboard: [http://bluemix.net ![Symbol für externen Link](../../../icons/launch-glyph.svg "Symbol für externen Link")](http://bluemix.net){:new_window} Nachdem Sie sich mit Ihrer Benutzer-ID und Ihrem Kennwort angemeldet haben, wird die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle geöffnet.

    Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**.  Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
    Wählen Sie die ID des Benutzers aus und überprüfen Sie, ob der Benutzer über die Rolle *Organisationsmanager* für die Organisation sowie die Rollen *Bereichsmanager* und *Entwickler* für den Bereich verfügt.

    Wenn der Benutzer nicht über die richtigen Berechtigungen verfügt, erteilen Sie dem Benutzer die folgenden Berechtigungen: die Rolle *orgManager* für die Organisation sowie die Rollen *SpaceManager* und *Developer* für den Bereich. Weitere Informationen finden Sie unter [Einem Benutzer Berechtigungen zum Anzeigen von Bereichsprotokollen unter Verwendung der IBM Cloud-Benutzerschnittstelle erteilen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).
    
3. Überprüfen Sie, ob der als {{site.data.keyword.containershort}}-Schlüsseleigner identifizierte Benutzer über die IAM-Richtlinie für den {{site.data.keyword.loganalysisshort}}-Service mit den Berechtigungen als *Administrator* verfügt.

    Klicken Sie in der Menüleiste auf **Verwalten > Konto > Benutzer**.  Im Fenster *Benutzer* wird eine Liste mit Benutzern und den entsprechenden E-Mail-Adressen für das aktuell ausgewählte Konto angezeigt.
	
    Wählen Sie die ID des Benutzers aus und überprüfen Sie, ob der Benutzer über den IAM-Richtliniensatz verfügt. 

    Wenn der Benutzer nicht über die IAM-Richtlinie verfügt, siehe [Einem Benutzer über die IBM Cloud-Benutzerschnittstelle eine IAM-Richtlinie zuweisen](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account).

4. Aktualisieren Sie die Protokollierungskonfiguration. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    Dabei ist *ClusterName* der Name des Clusters.
	



## Schritt 5: Eine Beispielapp im Kubernetes-Cluster bereitstellen, um Inhalt in 'stdout' zu generieren
{: #step53}

Stellen Sie eine Beispielapp im Kubernetes-Cluster bereit und führen Sie sie aus. Führen Sie die Schritte des folgenden Lernprogramms aus, um die Beispielapp bereitzustellen: [Lerneinheit 1: Apps für einzelne Instanzen in Kubernetes-Cluster bereitstellen](/docs/containers/cs_tutorials_apps.html#cs_apps_tutorial_lesson1).

Die App ist eine 'Hello World'-Node.js-App:

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

In dieser Beispielapp schreibt die App, wenn Sie sie in einem Browser testen, die folgende Nachricht an 'stdout': `Sample app is listening on port 8080.`






## Schritt 6: Protokolldaten in Kibana anzeigen
{: #step6}

Führen Sie die folgenden Schritte aus:

1. Starten Sie Kibana in einem Browser. 

    Weitere Informationen zum Starten von Kibana finden Sie unter [Zu Kibana über einen Web-Browser navigieren](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser).

    Zum Anzeigen von Protokolldaten für einen Cluster müssen Sie in der öffentlichen Cloudregion, in der der Cluster erstellt wird, auf Kibana zugreifen. 
    
    Geben Sie z. B. in der Region "USA (Süden)" die folgende URL ein, um Kibana zu starten:
	
	```
	https://logging.ng.bluemix.net/ 
	```
	{: codeblock}
	
    Kibana wird geöffnet.
    
    **HINWEIS:** Achten Sie darauf, Kibana in der Region zu starten, an die Sie Ihre Clusterprotokolle weiterleiten. Informationen zu den URLs für die einzelnen Regionen finden Sie unter [Protokollierungsendpunkte](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#urls_kibana).
    	
2. Führen Sie die folgenden Schritte aus, um Protokolldaten anzuzeigen, die in der Bereichsdomäne verfügbar sind:

    1. Klicken Sie in Kibana auf Ihre Benutzer-ID. Die Ansicht für das Einrichten des Bereichs wird geöffnet.
    
    2. Wählen Sie das Konto aus, in dem der Bereich verfügbar ist. 
    
    3. Wählen Sie die folgende Domäne aus: **Bereich**
    
    4. Wählen Sie die Organisation *MyOrg* aus, in der der Bereich verfügbar ist.
    
    5. Wählen Sie den Bereich *dev* aus.
    
    
3. Auf der Seite **Discover** können Sie die angezeigten Ereignisse sehen. 
        
    Im Abschnitt *Available fields* können Sie die Liste der Felder sehen, die verwendet werden können, um neue Abfragen zu definieren oder die Einträge zu filtern, die in der Tabelle auf dieser Seite aufgelistet sind.
    
    In der folgenden Tabelle sind einige der Felder aufgeführt, über die Sie bei der Analyse von Anwendungsprotokollen neue Suchabfragen definieren können. Außerdem enthält die Tabelle Beispielwerte entsprechend dem Ereignis, das von der Beispielapp generiert wird:
 
    <table>
              <caption>Tabelle 2. Allgemeine Felder für Containerprotokolle </caption>
               <tr>
                <th align="center">Feld</th>
                <th align="center">Beschreibung</th>
                <th align="center">Beispiel</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>Der Wert dieses Felds entspricht der {{site.data.keyword.Bluemix_notm}}-Region, in der der Protokolleintrag erfasst wird.</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>Konto-ID.</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str *</td>
                <td>Cluster-ID.</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>Cluster-ID.</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str*</td>
                <td>Name des Namensbereichs</td>
                <td>*default* ist der Standardwert.</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>Containername.</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>Die Felder 'Label' sind optional. Sie können 0 oder mehrere Bezeichnungen ("labels") haben. Jede Bezeichnung beginnt mit dem Präfix `kubernetes.labels.`, gefolgt von *label_name*. </td>
                <td>In der Beispielapp werden zwei Bezeichnungen angezeigt: <br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*stream_str *</td>
                <td>Protokolltyp.</td>
                <td>*stdout*, *stderr*</td>
              </tr>
        </table>
     
Weitere Informationen zu anderen Suchfeldern, die für Kubernetes-Cluster relevant sind, finden Sie unter [Protokolle durchsuchen](/docs/services/CloudLogAnalysis/containers/containers_kubernetes.html#log_search).


## Schritt 7: Daten nach Kubernetes-Clusternamen in Kibana filtern
{: #step7}
    
In der Tabelle, die auf der Seite *Discover* angezeigt wird, können Sie alle Einträge sehen, die für die Analyse zur Verfügung stehen. Die aufgelisteten Einträge entsprechen der Suchabfrage, die in der *Suchleiste* angezeigt wird. Verwenden Sie einen Stern (*), um alle Einträge im Zeitraum anzuzeigen, die für die Seite konfiguriert sind.
    
Um beispielsweise die Daten nach Kubernetes-Clusternamen zu filtern, ändern Sie die Abfrage in der *Suchleiste*. Fügen Sie einen Filter auf Grundlage des angepassten Felds *kubernetes.cluster_name_str* hinzu:
    
1. Wählen Sie im Abschnitt **Verfügbare Felder** das Feld *kubernetes.cluster_name_str* aus. Eine Untergruppe der verfügbaren Werte für das Feld wird angezeigt.    
    
2. Wählen Sie den Wert aus, der dem Cluster entspricht, für den Sie Protokolle analysieren möchten. 
    
    Nachdem Sie den Wert ausgewählt haben, wird ein Filter in der *Suchleiste* hinzugefügt und die Tabelle zeigt nur Einträge an, die mit den von Ihnen soeben ausgewählten Kriterien übereinstimmen.     
   

**Hinweis:** 

Wenn Ihnen Ihr Clustername nicht angezeigt wird, fügen Sie einen Filter für beliebige Clusternamen hinzu. Anschließend wählen Sie das Bearbeitungssymbol für den Filter aus.    
    
Die folgende Abfrage wird angezeigt:
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

Ersetzen Sie den Namen des Clusters (*cluster1*) durch den Namen des Clusters *mycluster*, für den Sie Protokolldaten anzeigen möchten.
        
Wenn keine Daten angezeigt werden, versuchen Sie, den Zeitfilter zu ändern. Weitere Informationen finden Sie unter [Zeitfilter festlegen](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).

Weitere Informationen finden Sie unter [Protokolle in Kibana filtern](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs).


## {{site.data.keyword.containershort_notm}}-Referenzmaterial
{: reference}

CLI-Befehle:

* [ibmcloud cs api-key-info](/docs/containers/cs_cli_reference.html#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers/cs_cli_reference.html#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers/cs_cli_reference.html#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers/cs_cli_reference.html#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers/cs_cli_reference.html#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers/cs_cli_reference.html#cs_logging_refresh)

