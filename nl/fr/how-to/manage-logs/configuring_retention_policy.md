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

# Configuration de la règle de conservation des journaux
{: #configuring_retention_policy1}

Utilisez la commande **cf logging option** pour afficher et configurer la règle de conservation qui définit le nombre maximal de jours pendant lequel les journaux sont
conservés dans Collecte des journaux. Par défaut, la règle de conservation est désactivée et les journaux sont conservés indéfiniment. Une fois que la durée de conservation a expiré, les journaux sont supprimés automatiquement. 
{:shortdesc}

Vous pouvez définir différentes règles de conservation sur le compte, notamment une règle de compte globale et des règles d'espace individuelles. La règle de conservation que vous avez
définie au niveau du compte définit le nombre de jours pendant lequel vous pouvez conserver les journaux. Si vous définissez la règle de conservation d'un espace sur une durée supérieure à la
durée du niveau de compte, la règle appliquée est la dernière règle configurée pour cet espace. 


## Désactivation de la règle de conservation des journaux pour un espace
{: #disable_retention_policy_space1}

Effectuez les étapes suivantes pour désactiver une règle de conservation :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Définissez la valeur **-1** pour désactiver la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud cf logging option -r -1
    ```
    {: codeblock}
    
**Exemple**
    
Par exemple, pour désactiver la durée de conservation d'un espace dont l'ID est *d35da1e3-b345-475f-8502-cfgh436902a3*, exécutez la commande suivante :

```
ibmcloud cf logging option -r -1
```
{: codeblock}

La sortie est :

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen} 



## Vérification de la règle de conservation des journaux d'un espace
{: #check_retention_policy_space1}

Afin d'obtenir la durée de conservation définie pour un espace, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenez la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud cf logging option
    ```
    {: codeblock}

    La sortie est :

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## Vérification de la règle de conservation des journaux de tous les espaces d'un compte
{: #check_retention_policy_account}

Afin d'obtenir la durée de conservation définie pour chaque espace sur un compte, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Obtenez la durée de conservation de chaque espace du compte. Exécutez la commande suivante :

    ```
    ibmcloud cf logging option -a
    ```
    {: codeblock}

    La sortie est :

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    | fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## Définition de la règle de conservation des journaux au niveau du compte
{: #set_retention_policy_space1}

Afin d'afficher la durée de conservation pour un compte, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Définissez la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud cf logging option -r *Number_of_days* - a
    ```
    {: codeblock}
    
    où *Number_of_days* est un nombre entier qui définit le nombre de jours pendant lequel vous souhaitez conserver les journaux. 
    
    
**Exemple**
    
Par exemple, pour conserver un type de journal spécifique dans votre compte pendant seulement 15 jours, exécutez la commande suivante :

```
ibmcloud cf logging option -r 15 -a
```
{: codeblock}

La sortie affiche une entrée pour chaque espace du compte, y compris des informations sur la durée de conservation :

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        15 |
+--------------------------------------+-----------+
| fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
+--------------------------------------+-----------+
```
{: screen}

## Définition de la règle de conservation des journaux pour un espace
{: #set_retention_policy_account}

Afin d'afficher la durée de conservation pour un espace, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Définissez la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud cf logging option -r *Number_of_days*
    ```
    {: codeblock}
    
    où *Number_of_days* est un nombre entier qui définit le nombre de jours pendant lequel vous souhaitez conserver les journaux.
    
    
**Exemple**
    
Par exemple, pour conserver les journaux disponibles dans un espace pendant un an, exécutez la commande suivante :

```
ibmcloud cf logging option -r 365
```
{: codeblock}

La sortie est :

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |       365 |
+--------------------------------------+-----------+
```
{: screen}


