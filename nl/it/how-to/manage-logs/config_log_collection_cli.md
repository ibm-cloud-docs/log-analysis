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

# Configurazione della CLI Analisi dei log (plugin CF) (Obsoleto)
{: #config_log_collection_cli1}

Il servizio {{site.data.keyword.loganalysisshort}} include una CLI (command line interface) che puoi utilizzare per gestire i tuoi log nel cloud. Puoi utilizzare il plugin CF (Cloud Foundry) per visualizzare lo stato del log, per scaricare i log e per configurare la politica di conservazione dei log. La CLI offre diversi tipi di supporto: il supporto generale per le informazioni sulla CLI e i comandi supportati, il supporto sui comandi per le informazioni sull'utilizzo di un comando o il supporto sui comandi secondari per le informazioni su come utilizzare i comandi secondari di un comando.
{:shortdesc}



## Installazione del plugin CF Analisi dei log
{: #install_cli1}

Per installare la CLI {{site.data.keyword.loganalysisshort}}, completa questa procedura:

1. Installa la CLI {{site.data.keyword.Bluemix_notm}}.

   Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).

2. Installa il plugin CF {{site.data.keyword.loganalysisshort}}.

    * Per Linux, vedi [Installazione della CLI {{site.data.keyword.loganalysisshort}} su Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_linux1).
    * Per Windows, vedi [Installazione della CLI {{site.data.keyword.loganalysisshort}} su Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_windows1).
    * Per Mac OS X, vedi [Installazione della CLI {{site.data.keyword.loganalysisshort}} su Mac OS X](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli.html#install_cli_mac1).
 
3. Verifica l'installazione del plugin della CLI.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    Invoking 'cf plugins'...

    Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## Installazione della CLI Analisi dei log su Linux
{: #install_cli_linux1}

Completa la seguente procedura per installare il plugin CF di raccolta dei log su Linux:

1. Installa il plugin della CLI di raccolta dei log.

    1. Scarica la versione più recenti del plugin della CLI del servizio {{site.data.keyword.loganalysisshort}} (IBM-Logging) dalla [pagina della CLI {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
		Seleziona il valore della piattaforma: **linux64**. 
		Fai clic su **Salva file**. 
    
    2. Decomprimi il plugin.
    
        Ad esempio, decomprimi il plugin `logging-cli-linux64.gz` in Ubuntu, esegui il seguente comando:
        
        ```
        gunzip logging-cli-linux64.gz
        ```
        {: codeblock}

    3. Rendi il file eseguibile.
    
        Ad esempio, per rendere il file `logging-cli-linux64` eseguibile, esegui il seguente comando:
        
        ```
        chmod a+x logging-cli-linux64
        ```
        {: codeblock}

    4. Installa il plugin CF di registrazione.
    
        Ad esempio, per rendere il file `logging-cli-linux64` eseguibile, esegui il seguente comando:
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. Imposta la variabile di ambiente **LANG**.

    Imposta *LANG* sul valore predefinito *en_US.UTF-8* se la tua locale di sistema non è supportata da CF. Per informazioni sulle locale supportate da CF, vedi [Introduzione alla CLI CF ![Icona link esterno](../../../../icons/launch-glyph.svg "Icona link esterno")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window}
	
	Ad esempio in un sistema Ubuntu, modifica il file *~/.bashrc* e inserisci le seguenti righe:
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    Apri una nuova finestra di terminale ed esegui il seguente comando per verificare che la variabile LANG sia configurata:
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. Verifica l'installazione del plugin della CLI di registrazione.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## Installazione della CLI Analisi dei log su Windows
{: #install_cli_windows1}

Completa la seguente procedura per installare il plugin CF di raccolta dei log su Windows:

1. Scarica la versione più recenti del plugin della CLI del servizio {{site.data.keyword.loganalysisshort}} (IBM-Logging) dalla [pagina della CLI {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Seleziona il valore della piattaforma: **win64**. 
	2. Fai clic su **Salva file**.  
    
2. Esegui il comando **cf install-plugin** per installare il plugin di raccolta dei log su Windows. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	dove *PluginName* è il nome del file che hai scaricato.
	
    Ad esempio, per installare il plugin *logging-cli-win64_v1.0.1.exe*, immetti il seguente comando da una finestra di terminale:
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    Quando il plugin è installato, ottieni il seguente messaggio: `Il plugin IBM-Logging 1.0.1 è stato installato correttamente.`

3. Verifica l'installazione del plugin della CLI di registrazione.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## Installazione della CLI Analisi dei log su Mac OS X
{: #install_cli_mac1}

Completa la seguente procedura per installare il plugin CF di raccolta dei log su Mac OS X:

1. Scarica la versione più recenti del plugin della CLI del servizio {{site.data.keyword.loganalysisshort}} (IBM-Logging) dalla [pagina della CLI {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Seleziona il valore della piattaforma: **osx**. 
	2. Fai clic su **Salva file**.  
    
2. Esegui il comando **cf install-plugin** per installare il plugin di raccolta dei log su Mac OS X. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	dove *PluginName* è il nome del file che hai scaricato.
	
    Ad esempio, per installare il plugin *logging-cli-darwin_v1.0.1*, immetti il seguente comando da un terminale:
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    Quando il plugin è installato, ottieni il seguente messaggio: `Il plugin IBM-Logging 1.0.1 è stato installato correttamente.`

3. Verifica l'installazione del plugin della CLI di registrazione.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## Disinstallazione della CLI Analisi dei log
{: #uninstall_cli1}

Per disinstallare la CLI di registrazione, elimina il plugin.
{:shortdesc}

Completa la seguente procedura per disinstallare la CLI del servizio {{site.data.keyword.loganalysisshort}}:

1. Verifica la versione del plugin della CLI di registrazione installata.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. Se il plugin è installato, esegui `cf uninstall-plugin` per disinstallare il plugin della CLI di registrazione.

    Esegui il seguente comando:
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## Come ottenere supporto generale
{: #general_cli_help1}

Per ottenere le informazioni generali sulla CLI e su quali comandi sono supportati, completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Per elencare le informazioni sui comandi supportati e sulla CLI. Esegui il seguente comando:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## Come ottenere supporto per un comando
{: #command_cli_help1}

Per ottenere supporto sull'utilizzo di un comando, completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Per ottenere l'elenco dei comandi supportati e identificare il comando di cui hai bisogno. Esegui il comando:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Per ottenere supporto sul comando. Esegui il seguente comando:

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    dove *Command* è il nome di un comando della CLI, ad esempio, *status*.



## Come ottenere supporto per un comando secondario
{: #subcommand_cli_help1}

Un comando può avere comandi secondari. Per ottenere supporto sui comandi secondari, completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Ottieni l'elenco di comandi supportati e identifica quello di cui hai bisogno. Esegui il comando:

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Per ottenere supporto sul comando e identificare i comandi secondari supportati. Esegui il seguente comando:

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    dove *Command* è il nome di un comando della CLI, ad esempio, *session*.

4. Per ottenere supporto sul comando e identificare i comandi secondari supportati. Esegui il seguente comando:

    ```
    ibmcloud cf logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    dove 
    
    * *Command* è il nome di un comando della CLI, ad esempio, *status*.
    * *Subcommand* è il nome del comando secondario supportato, ad esempio, per il comando *session*, un comando secondario valido è *list*.




