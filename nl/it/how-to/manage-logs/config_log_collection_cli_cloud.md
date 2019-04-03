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

# Configurazione della CLI {{site.data.keyword.loganalysisshort}}
{: #config_log_collection_cli}

Il servizio {{site.data.keyword.loganalysisshort}} include una CLI (command line interface) che puoi utilizzare per gestire i log nel cloud. Puoi utilizzare il plugin {{site.data.keyword.Bluemix_notm}} per visualizzare lo stato del log, per scaricare i log e per configurare la politica di conservazione dei log. La CLI offre diversi tipi di supporto: il supporto generale per le informazioni sulla CLI e i comandi supportati, il supporto sui comandi per le informazioni sull'utilizzo di un comando o il supporto sui comandi secondari per le informazioni su come utilizzare i comandi secondari di un comando.
{:shortdesc}


## Installazione del plugin {{site.data.keyword.loganalysisshort}} dal repository {{site.data.keyword.Bluemix_notm}}
{: #install_cli_repo}

Per installare la CLI {{site.data.keyword.loganalysisshort}}, completa questa procedura:

1. Installa la CLI {{site.data.keyword.Bluemix_notm}}.

   Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
2. Identifica il nome del plugin nel repository. Esegui il seguente comando:

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    Il nome del plugin è **logging-cli**.

3. Installa il plugin {{site.data.keyword.loganalysisshort}}. Esegui il seguente comando:

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. Verifica che il plugin {{site.data.keyword.loganalysisshort}} sia installato.
  
    Ad esempio, esegui questo comando per visualizzare l'elenco dei plugin installati:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## Installazione del plugin {{site.data.keyword.loganalysisshort}} da un file
{: #install_cli}

Per installare la CLI {{site.data.keyword.loganalysisshort}}, completa questa procedura:

1. Installa la CLI {{site.data.keyword.Bluemix_notm}}.

   Per ulteriori informazioni, vedi [Installazione della CLI {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).

2. Installa il plugin {{site.data.keyword.loganalysisshort}}.

    * Per Linux, vedi [Installazione del plugin {{site.data.keyword.loganalysisshort}} su Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux).
    * Per Windows, vedi [Installazione del plugin {{site.data.keyword.loganalysisshort}} su Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows).
    * Per Mac OS X, vedi [Installazione della plugin {{site.data.keyword.loganalysisshort}} su Mac OS X](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac).
 
3. Verifica l'installazione del plugin della CLI.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## Installazione del plugin Analisi dei log su Linux da un file
{: #install_cli_linux}

Completa la seguente procedura per installare il plugin Raccolta dei log su Linux:

1. Installa il plugin.

    Scarica la versione più recenti del plugin della CLI del servizio {{site.data.keyword.loganalysisshort}} (IBM-Logging) dalla [pagina della CLI {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	* Seleziona il valore della piattaforma: **linux64**. 
	
	* Fai clic su **Salva file**. 
    
2. Installa il plugin. Esegui il seguente comando:
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## Installazione del plugin Analisi dei log su Windows da un file
{: #install_cli_windows}

Completa la seguente procedura per installare il plugin Raccolta dei log su Windows:

1. Scarica la versione più recenti del plugin della CLI del servizio {{site.data.keyword.loganalysisshort}} (IBM-Logging) dalla [pagina della CLI {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Seleziona il valore della piattaforma: **win64**. 
	2. Fai clic su **Salva file**.  
    
2. Installa il plugin. Esegui il seguente comando:
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## Installazione del plugin Analisi dei log su Mac OS X da un file
{: #install_cli_mac}

Completa la seguente procedura per installare il plugin Raccolta dei log su Mac OS X:

1. Scarica la versione più recenti del plugin della CLI del servizio {{site.data.keyword.loganalysisshort}} (IBM-Logging) dalla [pagina della CLI {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Seleziona il valore della piattaforma: **osx**. 
	2. Fai clic su **Salva file**.  
    
2. Modifica le autorizzazioni del file. Esegui il seguente comando:

    ```
    chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. Installa il plugin. Esegui il seguente comando:
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## Disinstallazione della CLI Analisi dei log
{: #uninstall_cli}

Per disinstallare la CLI di registrazione, elimina il plugin.
{:shortdesc}

Completa la seguente procedura per disinstallare la CLI del servizio {{site.data.keyword.loganalysisshort}}:

1. Verifica la versione del plugin della CLI di registrazione installata.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. Se il plugin è installato, esegui `ibmcloud plugin uninstall` per disinstallare il plugin della CLI di registrazione.

    Esegui il seguente comando:
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## Aggiornamento della CLI Log Analysis dal repository
{: #update_cli}

Per aggiornare la CLI di registrazione, esegui il comando *ibmcloud plugin update*.
{:shortdesc}

Completa la seguente procedura per aggiornare la CLI del servizio {{site.data.keyword.loganalysisshort}}:

1. Aggiorna il plugin {{site.data.keyword.loganalysisshort}}. Esegui il seguente comando:

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. Verifica l'installazione del plugin della CLI.
  
    Ad esempio, verifica la versione del plugin. Esegui il seguente comando:
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    L'output sarà simile al seguente:
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## Come ottenere supporto generale
{: #general_cli_help}

Per ottenere le informazioni generali sulla CLI e su quali comandi sono supportati, completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Per elencare le informazioni sui comandi supportati e sulla CLI. Esegui il seguente comando:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## Come ottenere supporto per un comando
{: #command_cli_help}

Per ottenere supporto sull'utilizzo di un comando, completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Per ottenere l'elenco dei comandi supportati e identificare il comando di cui hai bisogno. Esegui il comando:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Per ottenere supporto sul comando. Esegui il seguente comando:

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    dove *Command* è il nome di un comando della CLI, ad esempio, *status*.



## Come ottenere supporto per un comando secondario
{: #subcommand_cli_help}

Un comando può avere comandi secondari. Per ottenere supporto sui comandi secondari, completa la seguente procedura:

1. Accedi a una regione, un'organizzazione e uno spazio in {{site.data.keyword.Bluemix_notm}}. 

    Per ulteriori informazioni, vedi [Come accedo a {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Per ottenere l'elenco dei comandi supportati e identificare il comando di cui hai bisogno. Esegui il comando:

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Per ottenere supporto sul comando e identificare i comandi secondari supportati. Esegui il seguente comando:

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    dove *Command* è il nome di un comando della CLI, ad esempio, *session*.

4. Per ottenere supporto sul comando e identificare i comandi secondari supportati. Esegui il seguente comando:

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    dove 
    
    * *Command* è il nome di un comando della CLI, ad esempio, *status*.
    * *Subcommand* è il nome del comando secondario supportato, ad esempio, per il comando *session*, un comando secondario valido è *list*.


## Mostra i dettagli del plugin
{: #show}
  
Utilizza il comando 'ibmcloud plugin show logging-cli' per visualizzare i dettagli del plugin. 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
L'output sarà simile al seguente:
   
```
ibmcloud plugin show logging-cli
                                  
Plugin                         logging-cli
Version                        0.1.1
Minimal CLI version required   0.5.0
Commands
                               logging log-delete       Delete log
                               logging log-download     Download a log
                               logging log-show         Show the count, size, and type of logs per day
                               logging session-create   Create a session
                               logging session-delete   Delete session
                               logging sessions         List sessions info
                               logging session-show     Show a session info
                               logging option-show      Show the log retention
                               logging option-update    Show the log options    
```
{: screen}

