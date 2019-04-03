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

# Suppression de journaux
{: #deleting_logs}

Utilisez la commande [ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) pour supprimer des journaux de Log Collection. 
{:shortdesc}

* Vous pouvez supprimer des journaux dans un intervalle spécifique.
* Vous pouvez supprimer des journaux par type. Notez que chaque fichier journal ne comporte qu'un seul type d'entrées de journal.
* Vous pouvez supprimer des journaux pour un espace, pour une organisation, ou dans le domaine de compte.


## Suppression de tous les journaux pour une période spécifique
{: #time_range}

Procédez comme suit pour supprimer tous les journaux qui sont stockés dans un domaine d'espace pour une période spécifique :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Exécutez la commande suivante pour afficher les journaux disponibles dans Log Collection :

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Exemple :
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-abcd-4193-aere-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. Supprimez les journaux qui ont été stockés un jour spécifique.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	où
	
	* *-s* définit la date de début en temps universel coordonné (TUC) : AAAA-MM-JJ, par exemple 2006-01-02.
    * *-e* définit la date de fin en temps universel coordonné (TUC) : AAAA-MM-JJ.
    	
	Par exemple, pour supprimer les journaux du 25 mai 2017, exécutez la commande suivante :
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## Suppression de journaux par type de journal pour une période spécifique 
{: #log_type}

Procédez comme suit pour supprimer par type de journal des journaux qui sont stockés dans un domaine d'espace pour une période spécifique :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Exécutez la commande suivante pour afficher les journaux disponibles dans Log Collection :

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Exemple :
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. Supprimez les journaux qui ont été stockés un jour spécifique.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	où
	
	* *-s* définit la date de début en temps universel coordonné (TUC) : AAAA-MM-JJ, par exemple 2006-01-02.
    * *-e* définit la date de fin en temps universel coordonné (TUC) : AAAA-MM-JJ.
	* *-t* définit le type de journal.
    	
	Par exemple, pour supprimer les journaux du type linux_syslog du 25 mai 2017, entrez la commande suivante :
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## Suppression de journaux de compte par type de journal pour une période spécifique 
{: #time_range_acc}

Procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Obtenez l'ID de compte.

    Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'un compte ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid).
    
3. Exécutez la commande suivante pour afficher les journaux qui sont disponibles dans Log Collection au niveau du compte :

    ```
    ibmcloud logging log-show  -r account -i AccountID
    ```
    {: codeblock}
    
    Exemple :
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    All                 default
	2017-05-25   2000       76115   All                 linux_syslog,log
    2017-05-26   195678     17639   All                 default,linux_syslog    
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}
	
4. Supprimez les journaux qui ont été stockés un jour spécifique.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType -r account -i AccountID
	```
	{: codeblock}
	
	où
	
	* *-s* définit la date de début en temps universel coordonné (TUC) : AAAA-MM-JJ, par exemple 2006-01-02.
    * *-e* définit la date de fin en temps universel coordonné (TUC) : AAAA-MM-JJ.
	* *-t* définit le type de journal.
    	
	Par exemple, afin de supprimer les journaux de type linux_syslog du 25 mai 2017 qui sont stockés dans Log Collection au niveau du compte, exécutez la commande suivante :
	
	```
	ibmcloud logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -r account -i 123456789123456789567c9c8de6dece
	```
	{: screen}
	












