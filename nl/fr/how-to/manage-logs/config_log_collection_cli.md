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

# Configuration de l'interface de ligne de commande Log Analysis (plug-in CF) - Dépréciée
{: #config_log_collection_cli1}

Le service {{site.data.keyword.loganalysisshort}} inclut une interface de ligne de commande (CLI) que vous pouvez utiliser pour gérer vos journaux dans le cloud. Vous pouvez utiliser le plug-in Cloud Foundry (CF) pour afficher le statut du journal, télécharger des journaux et configurer la règle de conservation des journaux. L'interface CLI offre différents types d'aides : une aide générale concernant l'interface CLI et les commandes prises en charge,
une aide relative aux commandes pour savoir comment utiliser une commande et une aide relative aux sous-commandes pour savoir comment utiliser une sous-commande d'une commande.
{:shortdesc}



## Installation du plug-in CF Log Analysis
{: #install_cli1}

Pour installer l'interface de ligne de commande {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)

2. Installez le plug-in CF {{site.data.keyword.loganalysisshort}}.

    * Pour Linux, voir [Installation de l'interface CLI {{site.data.keyword.loganalysisshort}} sous Linux](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_linux1).
    * Pour Windows, voir [Installation de l'interface CLI {{site.data.keyword.loganalysisshort}} sous Windows](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_windows1).
    * Pour Mac OS X, voir [Installation de l'interface CLI {{site.data.keyword.loganalysisshort}} sous Mac OS X ](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli1#install_cli_mac1).
 
3. Vérifiez l'installation du plug-in de l'interface CLI.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    Invoking 'cf plugins'...

    Listing Installed Plugins...
    OK

    Plugin Name           Version   Command Name   Command Help
    IBM-Logging           1.0.2     logging        IBM Logging plug-in
    ```
    {: screen}
 


## Installation de l'interface de ligne de commande de Log Analysis sous Linux
{: #install_cli_linux1}

Procédez comme suit pour installer le plug-in CF Log Collection sous Linux :

1. Installez le plug-in d'interface de ligne de commande Log Collection.

    1. Téléchargez l'édition la plus récente du plug-in d'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} (IBM-Logging) depuis la [page de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
		Sélectionnez la valeur de plateforme : **linux64**. 
		Cliquez sur **Enregistrer**. 
    
    2. Décompressez le plug-in.
    
        Par exemple, pour décompresser le plug-in `logging-cli-linux64.gz` dans Ubuntu, exécutez la commande suivante :
        
        ```
        gunzip logging-cli-linux64.gz
        ```
        {: codeblock}

    3. Rendez le fichier exécutable.
    
        Par exemple, pour rendre le fichier `logging-cli-linux64` exécutable, exécutez la commande suivante :
        
        ```
        chmod a+x logging-cli-linux64
        ```
        {: codeblock}

    4. Installation du plug-in CF de journalisation.
    
        Par exemple, pour rendre le fichier `logging-cli-linux64` exécutable, exécutez la commande suivante :
        
        ```
        ibmcloud cf install-plugin -f logging-cli-linux64
        ```
        {: codeblock}

2. Définissez la variable d'environnement **LANG**.

    Pour *LANG*, définissez la valeur par défaut *en_US.UTF-8* si les paramètres régionaux de votre système ne sont pas pris en charge par CF. Pour des informations
sur les environnements locaux pris en charge par CF, voir [Getting Started with the cf CLI
![Icône de lien externe](../../../../icons/launch-glyph.svg "Icône de lien externe")](https://docs.cloudfoundry.org/cf-cli/getting-started.html){: new_window}
	
	Par exemple, dans un système Ubuntu, éditez le fichier *~/.bashrc* et entrez les lignes suivantes :
    
    ```
    # add entry for logging CLI
    export LANG = en_US.UTF-8
    ```
    {: codeblock}
    
    Ouvrez une nouvelle fenêtre de terminal et exécutez la commande suivante pour vérifier que la variable LANG est définie :
    
    ```
    $echo LANG
    en_US.UTF-8
    ```
    {: screen}   
    
3. Vérifiez l'installation du plug-in de l'interface de ligne de commande de journalisation.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    cf logging version 1.0.2
    ```
    {: screen}


## Installation de l'interface de ligne de commande de Log Analysis sous Windows
{: #install_cli_windows1}

Procédez comme suit pour installer le plug-in CF Log Collection sous Windows :

1. Téléchargez l'édition la plus récente du plug-in d'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} (IBM-Logging) depuis la [page de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Sélectionnez la valeur de plateforme : **win64**. 
	2. Cliquez sur **Enregistrer**.  
    
2. Exécutez la commande **cf install-plugin** pour installer le plug-in Log Collection sous Windows. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	où *PluginName* est le nom du fichier que vous avez téléchargé.
	
    Par exemple, pour installer le plug-in *logging-cli-win64_v1.0.1.exe*, exécutez la commande suivante depuis une fenêtre de terminal :
	
	```
	ibmcloud cf install-plugin logging-cli-win64_v1.0.1.exe
	```
	{: codeblock}
	
    Lorsque le plug-in est installé, le message suivant s'affiche : `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Vérifiez l'installation du plug-in de l'interface de ligne de commande de journalisation.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	

## Installation de l'interface de ligne de commande de Log Analysis sous Mac OS X
{: #install_cli_mac1}

Procédez comme suit pour installer le plug-in Log Collection CF sous Mac OS X :

1. Téléchargez l'édition la plus récente du plug-in d'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} (IBM-Logging) depuis la [page de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](https://clis.ng.bluemix.net/ui/repository.html#cf-plugins). 
	
	1. Sélectionnez la valeur de plateforme : **osx**. 
	2. Cliquez sur **Enregistrer**.  
    
2. Exécutez la commande **cf install-plugin** pour installer le plug-in Log Collection sous Mac OS X. 

    ```
	ibmcloud cf install-plugin PluginName
	```
	{: codeblock}
	
	où *PluginName* est le nom du fichier que vous avez téléchargé.
	
    Par exemple, pour installer le plug-in *logging-cli-darwin_v1.0.1*, exécutez la commande suivante depuis un terminal :
	
	```
	ibmcloud cf install-plugin logging-cli-darwin_v1.0.1
	```
	{: codeblock}
	
    Lorsque le plug-in est installé, le message suivant s'affiche : `Plugin IBM-Logging 1.0.1 successfully installed.`

3. Vérifiez l'installation du plug-in de l'interface de ligne de commande de journalisation.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud cf logging --version
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    ibmcloud cf logging version 1.0.1
    ```
    {: screen}
	
	
## Désinstallation de l'interface de ligne de commande de Log Analysis
{: #uninstall_cli1}

Pour désinstaller l'interface de ligne de commande de journalisation, supprimez le plug-in.
{:shortdesc}

Procédez comme suit pour désinstaller l'interface de ligne de commande du service {{site.data.keyword.loganalysisshort}} :

1. Vérifiez la version du plug-in d'interface de ligne de commande de journalisation qui est installée.
  
    Par exemple, vérifiez la version du plug-in. Exécutez la commande suivante :
    
    ```
    ibmcloud cf plugins
    ```
    {: codeblock}
    
    La sortie est similaire à la suivante :
   
    ```
    Listing Installed Plugins...
    OK

    Plugin Name   Version   Command Name   Command Help
    IBM-Logging   1.0.1     logging        IBM Logging plug-in
    ```
    {: screen}
    
2. Si le plug-in est installé, exécutez la commande `cf uninstall-plugin` pour désinstaller le plug-in d'interface de ligne de commande de journalisation.

    Exécutez la commande suivante :
        
    ```
    ibmcloud cf uninstall-plugin IBM-Logging
    ```
    {: codeblock}
  

## Obtention d'une aide générale
{: #general_cli_help1}

Pour obtenir des informations générales sur l'interface de ligne de commande et prendre connaissance des commandes prises en charge, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Affichez des informations sur les commandes prises en charge et sur l'interface de ligne de commande. Exécutez la commande suivante :

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}
    
    

## Obtenir de l'aide sur une commande
{: #command_cli_help1}

Pour obtenir de l'aide au sujet de l'utilisation d'une commande, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Obtenez la liste des commandes prises en charge et identifiez celle dont vous avez besoin. Exécutez la commande suivante :

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Obtenez de l'aide sur la commande. Exécutez la commande suivante :

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    où *Command* est le nom d'une commande de l'interface de ligne de commande, par exemple *status*.



## Obtention d'aide sur une sous-commande
{: #subcommand_cli_help1}

Une commande peut avoir des sous-commandes. Pour obtenir de l'aide sur des sous-commandes, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Obtenez la liste des commandes prises en charge et identifiez celle dont vous avez besoin. Exécutez la commande suivante :

    ```
    ibmcloud cf logging help 
    ```
    {: codeblock}

3. Obtenez de l'aide sur la commande et identifiez les sous-commandes prises en charge. Exécutez la commande suivante :

    ```
    ibmcloud cf logging help *Command*
    ```
    {: codeblock}
    
    où *Command* est le nom d'une commande de l'interface de ligne de commande, par exemple *session*.

4. Obtenez de l'aide sur la commande et identifiez les sous-commandes prises en charge. Exécutez la commande suivante :

    ```
    ibmcloud cf logging *Command* help *Subcommand*
    ```
    {: codeblock}
    
    où 
    
    * *Command* est le nom d'une commande de l'interface de ligne de commande, par exemple *status*.
    * *Subcommand* est le nom d'une sous-commande prise en charge. Par exemple, pour la commande *session*, une sous-commande valide est *list*.




