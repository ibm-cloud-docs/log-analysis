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
{: #viewing_log_status}

Utilisez la commande [cf logging status](/docs/services/CloudLogAnalysis/reference/logging_cli.html#status1) pour obtenir des informations sur les journaux qui sont collectés et stockés dans Collecte des journaux.
{:shortdesc}

## Obtention d'informations sur les journaux durant une période définie
{: #viewing_logs1}

Utilisez la commande `cf logging status` pour voir la taille, le nombre, les types de journaux et pour voir s'ils sont disponibles ou non pour une analyse dans Kibana
pour les journaux qui sont stockés dans Log Collection. 

Utilisez la commande `cf logging status` avec les options **-s** pour définir la date de début et **-e** pour définir la date de fin. Par exemple :

* `cf logging status` fournit des informations pour les deux dernières semaines.
* `cf logging status -s 2017-05-03` fournit des informations pour la période du 3 mai 2017 à la date en cours.
* `cf logging status -s 2017-05-03 -e 2017-05-08` fournit des informations pour la période comprise entre le 3 mai 2017 et le 8 mai 2017. 

Procédez comme suit pour obtenir des informations sur les journaux :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Exécutez la commande *status*.

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Exemple
    
    ```
    $ ibmcloud cf logging status
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}


## Obtention d'informations sur un type de journal pour une période donnée
{: #viewing_logs_by_log_type1}

Pour obtenir des informations sur un type de journal pour une période donnée, utilisez la commande `cf logging status` avec les options **-t** pour
spécifier le type de journal, **-s** pour définir la date de début et **-e** pour définir la date de fin. Exemple

* `cf logging status -t syslog` fournit des informations sur les journaux de type *syslog* pour les deux dernières semaines.
* `cf logging status -s 2017-05-03 -t syslog` fournit des informations sur les journaux de type *syslog* pour la période du 3 mai 2017 à la date en cours.
* `cf logging status -s 2017-05-03 -e 2017-05-08 -t syslog` fournit des informations sur les journaux de type *syslog* pour la période comprise entre le 3 mai 2017 et le 8 mai 2017. 

Procédez comme suit pour obtenir des informations sur un type de journal pour une période donnée :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Exécutez la commande *status*.

    ```
    ibmcloud cf logging status -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    où
    
    * *-s* est utilisé pour définir la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-e* est utilisé pour définir la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-t* est utilisé pour définir le type de journal.
    
    Vous pouvez spécifier plusieurs types de journaux en les séparant par une virgule, par exemple **log_type_1,log_type_2,log_type_3**. 
    
    Exemple
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}



## Obtention d'informations de compte sur les journaux
{: #viewing_logs_account1}

Pour obtenir des informations sur les journaux durant une période définie pour le compte {{site.data.keyword.Bluemix_notm}}, utilisez la commande `cf logging
status` avec l'option **-a**. Vous pouvez également spécifier les options **-t** pour spécifier le type de journal, **-s**
pour définir la date de début et **-e** pour définir la date de fin. 

Procédez comme suit pour obtenir des informations de compte sur les journaux :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Exécutez la commande *status*.

    ```
    ibmcloud cf logging status -a -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    où
    
    * *-a* est utilisé pour spécifier les informations sur le niveau de compte
    * *-s* est utilisé pour définir la date de début en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-e* est utilisé pour définir la date de fin en temps universel coordonné (TUC) : *AAAA-MM-JJ*
    * *-t* est utilisé pour définir le type de journal.
    

    Vous pouvez spécifier plusieurs types de journaux en les séparant par une virgule, par exemple **log_type_1,log_type_2,log_type_3**. 
 
    Exemple
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log -a
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}














