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

# Affichage des informations sur le journal
{: #viewing_log_status1}

Utilisez la commande [ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#status) pour obtenir des informations sur les journaux qui sont collectés et stockés dans le composant Log Collection. Vous pouvez obtenir des informations sur la taille, le nombre d'enregistrements, les types de journaux, ainsi que sur la disponibilité des journaux pour l'analyse dans Kibana.
{:shortdesc}

## Obtention d'informations sur les journaux pour une période donnée
{: #viewing_logs}

Utilisez la commande `ibmcloud logging log-show` avec les options **-s** pour définir la date de début et **-e** pour définir la date de fin. Par exemple :

* `ibmcloud logging log-show` fournit des informations pour les deux dernières semaines.
* `ibmcloud logging log-show -s 2017-05-03` fournit des informations pour la période comprise entre le 3 mai 2017 et la date en cours.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` fournit des informations pour la période comprise entre le 3 mai 2017 et le 8 mai 2017. 

Procédez comme suit pour obtenir des informations sur les journaux qui sont stockés dans un espace :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Exécutez la commande suivante :

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Par exemple
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## Obtention d'informations sur un type de journal pour une période donnée
{: #viewing_logs_by_log_type}

Pour obtenir des informations sur un type de journal pour une période donnée, utilisez la commande `ibmcloud logging log-show` avec les options **-t** pour spécifier le type de journal, **-s** pour définir la date de début et **-e** pour définir la date de fin. Par exemple

* `ibmcloud logging log-show -t syslog` fournit des informations sur les journaux de type *syslog* pour les deux dernières semaines.
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` fournit des informations sur les journaux de type *syslog* pour la période du 3 mai 2017 à la date en cours.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` fournit des informations sur les journaux de type *syslog* pour la période du 3 mai 2017 au 8 mai 2017. 

Procédez comme suit pour obtenir des informations sur un type de journal pour une période donnée :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Exécutez la commande suivante :

    ```
    ibmcloud logging log-show -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    où
    
    * *-s* est utilisé pour définir la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-e* est utilisé pour définir la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-t* est utilisé pour définir le type de journal.
    
    Vous pouvez spécifier plusieurs types de journaux en séparant chaque type par une virgule, par exemple **log_type_1,log_type_2,log_type_3**. 
    
    Par exemple
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## Obtention d'informations sur les journaux au niveau du compte
{: #viewing_logs_account}

Pour obtenir des informations sur les journaux qui sont disponibles au niveau du compte pour une période donnée, utilisez la commande `ibmcloud logging log-show` avec les options **-r account** et **-i** afin de définir l'ID du compte. Vous pouvez également spécifier les options **-t** pour spécifier le type de journal, **-s**
pour définir la date de début et **-e** pour définir la date de fin. 

Procédez comme suit pour obtenir des informations de compte sur les journaux :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
2. Obtenez l'ID de compte.

    Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'un compte ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Exécutez la commande suivante :

    ```
    ibmcloud logging log-show -r account -i AccountID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    où
    
    * *-r account* est utilisé pour définir le domaine dans lequel vous voulez obtenir les informations sur les journaux.
    * *-i AccountID* est utilisé pour définir l'ID du compte.
    * *-s* est utilisé pour définir la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-e* est utilisé pour définir la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-t* est utilisé pour définir le type de journal.

    Vous pouvez spécifier plusieurs types de journaux en séparant chaque type par une virgule, par exemple **log_type_1,log_type_2,log_type_3**. 
 
    Par exemple, pour afficher des informations sur les journaux qui ont été stockés le 17 novembre 2017 dans le domaine de compte pour le compte *123456789123456789567c9c8de6dece*, exécutez la commande suivante :
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## Obtention d'informations sur les journaux au niveau de l'organisation
{: #viewing_logs_org}

Pour obtenir des informations sur les journaux qui sont disponibles au niveau de l'organisation pour une période donnée, utilisez la commande `ibmcloud logging log-show` avec les options **-r org** et **-i** afin de définir l'ID de l'organisation. Vous pouvez également spécifier les options **-t** pour spécifier le type de journal, **-s**
pour définir la date de début et **-e** pour définir la date de fin. 

Procédez comme suit pour obtenir des informations de compte sur les journaux :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
2. Obtenez l'ID de compte.

    Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'une organisation ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#org_guid).
    
3. Exécutez la commande suivante :

    ```
    ibmcloud logging log-show -r org -i OrgID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    où
    
    * *-r org* est utilisé pour définir le domaine dans lequel vous voulez obtenir les informations sur les journaux.
    * *-i OrgID* est utilisé pour définir l'ID de l'organisation.
    * *-s* est utilisé pour définir la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-e* est utilisé pour définir la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-t* est utilisé pour définir le type de journal.
    
    Vous pouvez spécifier plusieurs types de journaux en séparant chaque type par une virgule, par exemple **log_type_1,log_type_2,log_type_3**. 
 
    Par exemple, pour afficher des informations sur les journaux qui ont été stockés le 17 novembre 2017 dans le domaine d'organisation pour l'organisation dont l'ID est *abcd56789123456789567c9c8de6dece*, exécutez la commande suivante :
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








