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

# Configuration de l'interface de ligne de commande {{site.data.keyword.loganalysisshort}}
{: #config_log_collection_cli}

Le service {{site.data.keyword.loganalysisshort}} inclut une interface de ligne de commande que vous pouvez utiliser pour gérer les journaux dans le cloud. Vous pouvez utiliser le plug-in {{site.data.keyword.Bluemix_notm}} pour afficher le statut du journal, télécharger des journaux et configurer la règle de conservation des journaux. L'interface de ligne de commande offre différents types d'aides : une aide générale concernant l'interface de ligne de commande et les commandes prises en charge,
une aide relative aux commandes pour savoir comment utiliser une commande et une aide relative aux sous-commandes pour savoir comment utiliser une sous-commande d'une commande.
{:shortdesc}


## Installation du plug-in {{site.data.keyword.loganalysisshort}} depuis le référentiel {{site.data.keyword.Bluemix_notm}}
{: #install_cli_repo}

Pour installer l'interface de ligne de commande {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.](/docs/cli/index.html#overview)
   
2. Recherchez le nom du plug-in dans le référentiel. Exécutez la commande suivante :

    ```
    ibmcloud plugin repo-plugins
    ```
    {: codeblock}
    
    Le nom du plug-in est **logging-cli**.

3. Installez le plug-in {{site.data.keyword.loganalysisshort}}. Exécutez la commande suivante :

    ```
    ibmcloud plugin install logging-cli -r Bluemix
    ```
    {: codeblock}
 
4. Vérifiez que le plug-in {{site.data.keyword.loganalysisshort}} est installé.
  
    Par exemple, exécutez la commande suivante pour afficher la liste des plug-in qui sont installés :
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}


## Installation du plug-in {{site.data.keyword.loganalysisshort}} depuis un fichier
{: #install_cli}

Pour installer l'interface de ligne de commande {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.](/docs/cli/index.html#overview)

2. Installez le plug-in {{site.data.keyword.loganalysisshort}}.

    * Pour Linux, voir [Installation du plug-in {{site.data.keyword.loganalysisshort}} sous Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_linux).
    * Pour Windows, voir [Installation du plug-in {{site.data.keyword.loganalysisshort}} sous Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_windows).
    * Pour Mac OS X, voir [Installation du plug-in {{site.data.keyword.loganalysisshort}} sous Mac OS X](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#install_cli_mac).
 
3. Vérifiez l'installation du plug-in de l'interface de ligne de commande.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
 


## Installation du plug-in Log Analysis sous Linux depuis un fichier
{: #install_cli_linux}

Procédez comme suit pour installer le plug-in Log Collection sous Linux :

1. Installez le plug-in.

    Téléchargez l'édition la plus récente du plug-in d'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} (IBM-Logging) depuis la [page de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	* Sélectionnez la valeur de plateforme : **linux64**. 
	
	* Cliquez sur **Enregistrer**. 
    
2. Installez le plug-in. Exécutez la commande suivante :
        
    ```
    ibmcloud plugin install -f logging-cli-linux-amd64-0.1.1
    ```
    {: codeblock}




## Installation du plug-in Log Analysis sous Windows depuis un fichier
{: #install_cli_windows}

Procédez comme suit pour installer le plug-in Log Collection sous Windows :

1. Téléchargez l'édition la plus récente du plug-in d'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} (IBM-Logging) depuis la [page de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Sélectionnez la valeur de plateforme : **win64**. 
	2. Cliquez sur **Enregistrer**.  
    
2. Installez le plug-in. Exécutez la commande suivante :
        
    ```
    ibmcloud plugin install -f logging-cli-windows-amd64-0.1.1.exe
    ```
    {: codeblock}

	

## Installation du plug-in Log Analysis sous Mac OS X depuis un fichier
{: #install_cli_mac}

Procédez comme suit pour installer le plug-in Log Collection sous Mac OS X :

1. Téléchargez l'édition la plus récente du plug-in d'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} (IBM-Logging) depuis la [page de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#bluemix-plugins). 
	
	1. Sélectionnez la valeur de plateforme : **osx**. 
	2. Cliquez sur **Enregistrer**.  
    
2. Modifiez les droits du fichier. Exécutez la commande suivante :

    ```
    chmod u+x logging-cli-darwin-amd64-0.1.1
    ```
     {: codeblock}

3. Installez le plug-in. Exécutez la commande suivante :
        
    ```
    ibmcloud plugin install -f logging-cli-darwin-amd64-0.1.1
    ```
    {: codeblock}

	
	
## Désinstallation de l'interface de ligne de commande de Log Analysis
{: #uninstall_cli}

Pour désinstaller l'interface de ligne de commande de journalisation, supprimez le plug-in.
{:shortdesc}

Procédez comme suit pour désinstaller l'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} :

1. Vérifiez la version du plug-in d'interface de ligne de commande de journalisation qui est installée.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}
    
2. Si le plug-in est installé, exécutez la commande `ibmcloud plugin uninstall` pour désinstaller le plug-in d'interface de ligne de commande de journalisation.

    Exécutez la commande suivante :
        
    ```
    ibmcloud plugin uninstall logging-cli
    ```
    {: codeblock}
  

## Mise à jour de l'interface de ligne de commande Log Analysis depuis le référentiel
{: #update_cli}

Pour mettre à jour l'interface de ligne de commande de journalisation, exécutez la commande *ibmcloud plugin update*.
{:shortdesc}

Procédez comme suit pour mettre à jour l'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} :

1. Mettez à jour le plug-in {{site.data.keyword.loganalysisshort}}. Exécutez la commande suivante :

    ```
    ibmcloud plugin update logging-cli -r Bluemix
    ```
    {: codeblock}
 
2. Vérifiez l'installation du plug-in de l'interface de ligne de commande.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud plugin list
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    ibmcloud plugin list
    Listing installed plug-ins...

    Plugin Name          Version   
    logging-cli          0.1.1   
    ```
    {: screen}





## Obtention d'une aide générale
{: #general_cli_help}

Pour obtenir des informations générales sur l'interface de ligne de commande et prendre connaissance des commandes prises en charge, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Affichez des informations sur les commandes prises en charge et sur l'interface de ligne de commande. Exécutez la commande suivante :

    ```
    ibmcloud logging help 
    ```
    {: codeblock}
    
    

## Obtenir de l'aide sur une commande
{: #command_cli_help}

Pour obtenir de l'aide au sujet de l'utilisation d'une commande, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenez la liste des commandes prises en charge et identifiez celle dont vous avez besoin. Exécutez la commande suivante :

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Obtenez de l'aide sur la commande. Exécutez la commande suivante :

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    où *Command* est le nom d'une commande de l'interface de ligne de commande, par exemple *status*.



## Obtention d'aide sur une sous-commande
{: #subcommand_cli_help}

Une commande peut avoir des sous-commandes. Pour obtenir de l'aide sur des sous-commandes, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenez la liste des commandes prises en charge et identifiez celle dont vous avez besoin. Exécutez la commande suivante :

    ```
    ibmcloud logging help 
    ```
    {: codeblock}

3. Obtenez de l'aide sur la commande et identifiez les sous-commandes prises en charge. Exécutez la commande suivante :

    ```
    ibmcloud logging help *Command*
    ```
    {: codeblock}
    
    où *Command* est le nom d'une commande de l'interface de ligne de commande, par exemple *session*.

4. Obtenez de l'aide sur la commande et identifiez les sous-commandes prises en charge. Exécutez la commande suivante :

    ```
    ibmcloud logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    où 
    
    * *Command* est le nom d'une commande de l'interface de ligne de commande, par exemple *status*.
    * *Subcommand* est le nom d'une sous-commande prise en charge. Par exemple, pour la commande *session*, une sous-commande valide est *list*.


## Affichage des détails du plug-in
{: #show}
  
Utilisez la commande 'ibmcloud plugin show logging-cli' pour afficher les détails du plug-in. 

```
ibmcloud plugin show logging-cli
```
{: codeblock}
    
La sortie est similaire à la suivante :
   
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

