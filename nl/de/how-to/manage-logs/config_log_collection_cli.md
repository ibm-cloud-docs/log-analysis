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

# Log Analysis-Befehlszeilenschnittstelle (CF-Plug-in) konfigurieren (veraltet)
{: #config_log_collection_cli1}

Der {{site.data.keyword.loganalysisshort}}-Service beinhaltet eine Befehlszeilenschnittstelle (CLI), die Sie zur Verwaltung Ihrer Protokolle in der Cloud verwenden können. Sie können das Cloud Foundry-Plug-in (CF) verwenden, um den Status des Protokolls anzuzeigen, um Protokolle herunterzuladen und um die Protokollaufbewahrungsrichtlinie zu konfigurieren. Die Befehlszeilenschnittstelle bietet verschiedene Arten von Hilfe: erweiterte Hilfe zu den CLI- und unterstützten Befehlen sowie Hilfe zur Verwendung von Befehlen und Unterbefehlen.
{:shortdesc}



## CF-Plug-in für Log Analysis installieren
{: #install_cli1}

Führen Sie die folgenden Schritte aus, um die Befehlszeilenschnittstelle für {{site.data.keyword.loganalysisshort}} zu installieren:

1. Installieren Sie die {{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle.

   Weitere Informationen finden Sie in [{{site.data.keyword.Bluemix_notm}}-Befehlszeilenschnittstelle installieren](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).

2. Installieren Sie das CF-Plug-in für {{site.data.keyword.loganalysisshort}}.

    * Die Schritte für Linux finden Sie unter [Befehlszeilenschnittstelle von {{site.data.keyword.loganalysisshort}} unter Linux installieren](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_linux1).
    * Die Schritte für Windows finden Sie unter [Befehlszeilenschnittstelle von {{site.data.keyword.loganalysisshort}} unter Windows installieren](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_windows1).
    * Die Schritte für Mac OS X finden Sie unter [Befehlszeilenschnittstelle von {{site.data.keyword.loganalysisshort}} unter Mac OS X installieren](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_mac1).
 
3. Überprüfen Sie die Installation des Plug-ins für die Benutzerschnittstelle.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    Invoking 'cf plugins'...

    Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## Befehlszeilenschnittstelle für 'Log Analysis' unter Linux installieren
{: #install_cli_linux1}

Führen Sie die folgenden Schritte aus, um das CF-Plug-in für 'Log Collection' unter Linux zu installieren:

1. Installieren Sie das CLI-Plug-in für 'Log Collection'.

    1. Laden Sie die aktuelle Version des CLI-Plug-ins für den {{site.data.keyword.loganalysisshort}}-Service (IBM-Logging) von der [{{site.data.keyword.Bluemix_notm}}-CLI-Seite](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins) herunter. 
	
		Wählen Sie den Wert für die Plattform aus: **linux64**. 
		Klicken Sie auf die Schaltfläche zum Speichern der Datei (**Save file**). 
    
    2. Dekomprimieren Sie das Plug-in.
    
        Beispiel: Um das Plug-in `logging-cli-linux64.gz` in Ubuntu zu dekomprimieren, führen Sie den folgenden Befehl aus:
        
        ```
        gunzip logging-cli-linux64.gz
        ```
        {: codeblock}

    3. Machen Sie die Datei zu einer ausführbaren Datei.
    
        Beispiel: Um die Datei `logging-cli-linux64` in eine ausführbare Datei umzuwandeln, führen Sie den folgenden Befehl aus:
        
        ```
        chmod a+x logging-cli-linux64
        ```
        {: codeblock}

    4. Installieren Sie das CF-Plug-in für die Protokollierung.
    
        Beispiel: Um die Datei `logging-cli-linux64` in eine ausführbare Datei umzuwandeln, führen Sie den folgenden Befehl aus:
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. Legen Sie einen Wert für die Umgebungsvariable **LANG** fest.

    Geben Sie für *LANG* den Standardwert *en_US.UTF-8* an, wenn die Ländereinstellung Ihres Systems nicht von CF unterstützt wird. Weitere Informationen zu den von CF unterstützten Ländereinstellungen finden Sie unter [Einführung in die CF-Befehlszeilenschnittstelle ![Symbol für externen Link](../../../../icons/launch-glyph.svg "Symbol für externen Link")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window}.
	
	Beispiel: Bearbeiten Sie in einem Ubuntu-System die Datei *~/.bashrc* und fügen Sie die folgenden Zeilen ein:
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    Öffnen Sie ein neues Terminalfenster und führen Sie den folgenden Befehl aus, um zu überprüfen, ob die Variable LANG festgelegt wurde:
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. Überprüfen Sie die Installation des CLI-Plug-ins für die Protokollierung.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## Befehlszeilenschnittstelle für 'Log Analysis' unter Windows installieren
{: #install_cli_windows1}

Führen Sie die folgenden Schritte aus, um das CF-Plug-in für 'Log Collection' unter Windows zu installieren:

1. Laden Sie die aktuelle Version des CLI-Plug-ins für den {{site.data.keyword.loganalysisshort}}-Service (IBM-Logging) von der [{{site.data.keyword.Bluemix_notm}}-CLI-Seite](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins) herunter. 
	
	1. Wählen Sie den Wert für die Plattform aus: **win64**. 
	2. Klicken Sie auf die Schaltfläche zum Speichern der Datei (**Save file**).  
    
2. Führen Sie den Befehl **cf install-plugin** aus, um das Plug-in für 'Log Collection' unter Windows zu installieren. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	Hierbei steht *PluginName* für den Namen der Datei, die Sie heruntergeladen haben.
	
    Beispiel: Zum Installieren des Plug-ins *logging-cli-win64_v1.0.1.exe* führen Sie den folgenden Befehl in einem Terminalfenster aus:
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    Wenn das Plug-in installiert ist, wird folgende Nachricht angezeigt: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Überprüfen Sie die Installation des CLI-Plug-ins für die Protokollierung.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## Befehlszeilenschnittstelle für Log Analysis unter Mac OS X installieren
{: #install_cli_mac1}

Führen Sie die folgenden Schritte aus, um das CF-Plug-in für 'Log Collection' unter Mac OS X zu installieren:

1. Laden Sie die aktuelle Version des CLI-Plug-ins für den {{site.data.keyword.loganalysisshort}}-Service (IBM-Logging) von der [{{site.data.keyword.Bluemix_notm}}-CLI-Seite](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins) herunter. 
	
	1. Wählen Sie den Wert für die Plattform aus: **osx**. 
	2. Klicken Sie auf die Schaltfläche zum Speichern der Datei (**Save file**).  
    
2. Führen Sie den Befehl **cf install-plugin** aus, um das Plug-in für 'Log Collection' unter Mac OS X zu installieren. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	Hierbei steht *PluginName* für den Namen der Datei, die Sie heruntergeladen haben.
	
    Beispiel: Zum Installieren des Plug-ins *logging-cli-darwin_v1.0.1* führen Sie den folgenden Befehl in einem Terminal aus:
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    Wenn das Plug-in installiert ist, wird folgende Nachricht angezeigt: `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Überprüfen Sie die Installation des CLI-Plug-ins für die Protokollierung.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## Befehlszeilenschnittstelle für Log Analysis deinstallieren
{: #uninstall_cli1}

Um die Befehlszeilenschnittstelle für die Protokollierung zu deinstallieren, löschen Sie das Plug-in.
{:shortdesc}

Führen Sie die folgenden Schritte aus, um die Befehlszeilenschnittstelle für den {{site.data.keyword.loganalysisshort}}-Service zu deinstallieren:

1. Überprüfen Sie die Version des installierten CLI-Plug-ins für die Protokollierung.
  
    Überprüfen Sie beispielsweise die Version des Plug-ins. Führen Sie den folgenden Befehl aus:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    Die Ausgabe sieht wie folgt aus:
   
    ```
    Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. Wenn das Plug-in installiert ist, führen Sie den Befehl `cf uninstall-plugin` aus, um das CLI-Plug-in für die Protokollierung zu deinstallier.

    Führen Sie den folgenden Befehl aus:
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## Allgemeine Hilfe anfordern
{: #general_cli_help1}

Führen Sie die folgenden Schritte aus, um allgemeine Informationen zur Befehlszeilenschnittstelle und den unterstützten Befehlen zu erhalten:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Listen Sie Informationen zu den unterstützten Befehlen und zur Befehlszeilenschnittstelle auf. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## Hilfe zu einem Befehl abrufen
{: #command_cli_help1}

Gehen Sie wie folgt vor, um Hilfe zur Verwendung eines Befehls abzurufen:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Rufen Sie die Liste der unterstützten Befehle auf und suchen Sie nach dem gewünschten Befehl. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Rufen Sie Hilfeinformationen zu dem Befehl ab. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging help *Befehl*
    ```
    {: codeblock}
    
    Dabei ist *Befehl* der Name eines CLI-Befehls, z. B. *status*.



## Hilfe zu einem Unterbefehl abrufen
{: #subcommand_cli_help1}

Ein Befehl kann Unterbefehle haben. Gehen Sie wie folgt vor, um Hilfe zu Unterbefehlen abzurufen:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Rufen Sie die Liste der unterstützten Befehle auf und suchen Sie nach dem gewünschten Befehl. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Rufen Sie Hilfeinformationen zu dem Befehl ab und ermitteln Sie die unterstützten Unterbefehle. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging help *Befehl*
    ```
    {: codeblock}
    
    Dabei ist *Befehl* der Name eines CLI-Befehls, z. B. *session*.

4. Rufen Sie Hilfeinformationen zu dem Befehl ab und ermitteln Sie die unterstützten Unterbefehle. Führen Sie den folgenden Befehl aus:

    ```
    ibmcloud cf logging *Befehl* help *Unterbefehl*
    ```
    {: codeblock}
    
    Dabei gilt: 
    
    * *Befehl* ist der Name eines CLI-Befehls, z. B. *status*.
    * *Unterbefehl* ist der Name eines unterstützten Unterbefehls; z. B. ist *list* ein gültiger Unterbefehl für den Befehl *session*.




