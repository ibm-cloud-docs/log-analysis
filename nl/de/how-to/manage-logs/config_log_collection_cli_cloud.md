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

# Die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle
{: #config_log_collection_cli}

Der {{site.data.keyword.loganalysisshort}}-Service beinhaltet eine Befehlszeilenschnittstelle (CLI), die Sie zur Verwaltung von Protokollen in der Cloud verwenden können. Sie können das {{site.data.keyword.Bluemix_notm}}-Plug-in verwenden, um den Status des Protokolls anzuzeigen, um Protokolle herunterzuladen und um die Protokollaufbewahrungsrichtlinie zu konfigurieren. Die Befehlszeilenschnittstelle bietet verschiedene Arten von Hilfe: erweiterte Hilfe zu den CLI- und unterstützten Befehlen sowie Hilfe zur Verwendung von Befehlen und Unterbefehlen.
{:shortdesc}


## {{site.data.keyword.loganalysisshort}}-Plug-in über {{site.data.keyword.Bluemix_notm}}-Repository installieren
{: #install_cli_repo}

Führen Sie die folgenden Schritte aus, um die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle zu installieren:

1. Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle.

   Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle installieren](/docs/cli/index.html#overview).
   
2. Suchen Sie den Namen des Plug-ins im Repository. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    Der Name des Plug-ins ist **logging-cli**.

3. Installieren Sie das Plug-in für {{site.data.keyword.loganalysisshort}}. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. Überprüfen Sie, ob das {{site.data.keyword.loganalysisshort}}-Plug-in installiert wurde.
  
    Führen Sie beispielsweise den folgenden Befehl aus, um die Liste der installierten Plug-ins anzuzeigen:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## {{site.data.keyword.loganalysisshort}}-Plug-in über eine Datei installieren
{: #install_cli}

Führen Sie die folgenden Schritte aus, um die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle zu installieren:

1. Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle.

   Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle installieren](/docs/cli/index.html#overview).

2. Installieren Sie das Plug-in für {{site.data.keyword.loganalysisshort}}.

    * Die Schritte für Linux finden Sie unter [{{site.data.keyword.loganalysisshort}}-Plug-in unter Linux installieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux).
    * Die Schritte für Windows finden Sie unter [{{site.data.keyword.loganalysisshort}}-Plug-in unter Windows installieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows).
    * Die Schritte für Mac OS X finden Sie unter [{{site.data.keyword.loganalysisshort}}-Plug-in unter Mac OS X installieren](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac).
 
3. Überprüfen Sie die Installation des Plug-ins für die Benutzerschnittstelle.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## Log Analysis-Plug-in unter Linux über eine Datei installieren
{: #install_cli_linux}

Führen Sie die folgenden Schritte aus, um das Log Analysis-Plug-in unter Linux zu installieren:

1. Installieren Sie das Plug-in.

    Laden Sie die aktuelle Version des CLI-Plug-ins für den {{site.data.keyword.loganalysisshort}}-Service (IBM-Logging) von der [{{site.data.keyword.Bluemix_notm}}-CLI-Seite](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins) herunter. 
	
	* Wählen Sie den Wert für die Plattform aus: **linux64**. 
	
	* Klicken Sie auf die Schaltfläche zum Speichern der Datei (**Save file**). 
    
2. Installieren Sie das Plug-in. Führen Sie den folgenden Befehl aus:
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## Log Analysis-Plug-in unter Windows über eine Datei installieren
{: #install_cli_windows}

Führen Sie die folgenden Schritte aus, um das Log Analysis-Plug-in unter Windows zu installieren:

1. Laden Sie die aktuelle Version des CLI-Plug-ins für den {{site.data.keyword.loganalysisshort}}-Service (IBM-Logging) von der [{{site.data.keyword.Bluemix_notm}}-CLI-Seite](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins) herunter. 
	
	1. Wählen Sie den Wert für die Plattform aus: **win64**. 
	2. Klicken Sie auf die Schaltfläche zum Speichern der Datei (**Save file**).  
    
2. Installieren Sie das Plug-in. Führen Sie den folgenden Befehl aus:
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## Log Analysis-Plug-in unter Mac OS X über eine Datei installieren
{: #install_cli_mac}

Führen Sie die folgenden Schritte aus, um das Log Analysis-Plug-in unter Mac OS X zu installieren:

1. Laden Sie die aktuelle Version des CLI-Plug-ins für den {{site.data.keyword.loganalysisshort}}-Service (IBM-Logging) von der [{{site.data.keyword.Bluemix_notm}}-CLI-Seite](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins) herunter. 
	
	1. Wählen Sie den Wert für die Plattform aus: **osx**. 
	2. Klicken Sie auf die Schaltfläche zum Speichern der Datei (**Save file**).  
    
2. Ändern Sie die Berechtigungen der Datei. Führen Sie den folgenden Befehl aus:

    ```
    chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. Installieren Sie das Plug-in. Führen Sie den folgenden Befehl aus:
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## Befehlszeilenschnittstelle für Log Analysis deinstallieren
{: #uninstall_cli}

Um die Befehlszeilenschnittstelle für die Protokollierung zu deinstallieren, löschen Sie das Plug-in.
{:shortdesc}

Führen Sie die folgenden Schritte aus, um die Befehlszeilenschnittstelle für den {{site.data.keyword.loganalysisshort}}-Service zu deinstallieren:

1. Überprüfen Sie die Version des installierten CLI-Plug-ins für die Protokollierung.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. Wenn das Plug-in installiert ist, führen Sie den Befehl `ibmcloud plugin uninstall` aus, um das CLI-Plug-in für die Protokollierung zu deinstallieren.

    Führen Sie den folgenden Befehl aus:
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## Log Analysis-Befehlszeilenschnittstelle über das Repository aktualisieren
{: #update_cli}

Zum Aktualisieren der Befehlszeilenschnittstelle für die Protokollierung führen Sie den Befehl *ibmcloud plugin update* aus.
{:shortdesc}

Führen Sie die folgenden Schritte aus, um die Befehlszeilenschnittstelle für den {{site.data.keyword.loganalysisshort}}-Service zu aktualisieren:

1. Aktualisieren Sie das {{site.data.keyword.loganalysisshort}}-Plug-in. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. Überprüfen Sie die Installation des Plug-ins für die Benutzerschnittstelle.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## Allgemeine Hilfe anfordern
{: #general_cli_help}

Führen Sie die folgenden Schritte aus, um allgemeine Informationen zur Befehlszeilenschnittstelle und den unterstützten Befehlen zu erhalten:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Listen Sie Informationen zu den unterstützten Befehlen und zur Befehlszeilenschnittstelle auf. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## Hilfe zu einem Befehl abrufen
{: #command_cli_help}

Gehen Sie wie folgt vor, um Hilfe zur Verwendung eines Befehls abzurufen:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Rufen Sie die Liste der unterstützten Befehle auf und suchen Sie nach dem gewünschten Befehl. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Rufen Sie Hilfeinformationen zu dem Befehl ab. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging help *Befehl*
    ```
    {: codeblock}
    
    Dabei ist *Befehl* der Name eines CLI-Befehls, z. B. *status*.



## Hilfe zu einem Unterbefehl abrufen
{: #subcommand_cli_help}

Ein Befehl kann Unterbefehle haben. Gehen Sie wie folgt vor, um Hilfe zu Unterbefehlen abzurufen:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie unter [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Rufen Sie die Liste der unterstützten Befehle auf und suchen Sie nach dem gewünschten Befehl. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Rufen Sie Hilfeinformationen zu dem Befehl ab und ermitteln Sie die unterstützten Unterbefehle. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging help *Befehl*
    ```
    {: codeblock}
    
    Dabei ist *Befehl* der Name eines CLI-Befehls, z. B. *session*.

4. Rufen Sie Hilfeinformationen zu dem Befehl ab und ermitteln Sie die unterstützten Unterbefehle. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud logging *Befehl* help *Unterbefehl*
    ```
    {: codeblock}
    
    Dabei gilt: 
    
    * *Befehl* ist der Name eines CLI-Befehls, z. B. *status*.
    * *Unterbefehl* ist der Name eines unterstützten Unterbefehls; z. B. ist *list* ein gültiger Unterbefehl für den Befehl *session*.


## Details des Plug-ins anzeigen
{: #show}
  
Mit dem Befehl 'ibmcloud plugin show logging-cli' können Sie die Details des Plug-ins anzeigen. 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
Die Ausgabe sieht wie folgt aus:
   
```
ibmcloud plugin show logging-cli
                                  
Plug-in                         logging-cli
Version                        0.1.1
Erforderliche CLI-Mindestversion   0.5.0
Befehle
                               logging log-delete       Protokoll löschen
                               logging log-download     Protokoll herunterladen
                               logging log-show         Anzahl, Größe und Typ der Protokolle pro Tag anzeigen
                               logging session-create   Sitzung erstellen
                               logging session-delete   Sitzung löschen
                               logging sessions         Sitzungsinformationen auflisten
                               logging session-show     Sitzungsinformationen anzeigen
                               logging option-show      Protokollspeicherung anzeigen
                               logging option-update    Protokolloptionen anzeigen    
```
{: screen}

