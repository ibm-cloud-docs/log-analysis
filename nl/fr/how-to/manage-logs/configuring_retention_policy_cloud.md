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
{: #configuring_retention_policy}

Par défaut, la règle de conservation est désactivée et les journaux sont conservés indéfiniment. Utilisez la commande **ibmcloud logging option-update** pour changer la règle de conservation.
{:shortdesc}

Vous pouvez utiliser la commande **ibmcloud logging option-show** pour afficher la règle de conservation qui définit le nombre maximal de jours pendant lequel les journaux sont conservés dans le composant Log Collection. 

Lorsque vous définissez une règle de conservation, une fois que la durée de conservation est arrivée à expiration, les journaux sont supprimés automatiquement.


## Désactivation de la règle de conservation des journaux pour un compte
{: #disable_retention_policy_acc}

Lorsque vous désactivez la règle de conservation, tous les journaux sont conservés. 

Procédez comme suit pour désactiver une règle de conservation :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
2. Obtenez l'ID de compte.

    Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'un compte ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Pour désactiver la règle de conservation, définissez la valeur **-1**. Exécutez la commande suivante :

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE est une valeur numérique définissant le nombre de jours.
    
**Exemple**
    
Par exemple, afin de désactiver la durée de conservation pour un compte dont l'ID est *12345677fgh436902a3*, exécutez la commande suivante :

```
ibmcloud logging option-update -r account -i 12345677fgh436902a3 -e -1
```
{: codeblock}


## Désactivation de la règle de conservation des journaux pour un espace
{: #disable_retention_policy_space}

Lorsque vous désactivez la règle de conservation, tous les journaux sont conservés.  

Procédez comme suit pour désactiver une règle de conservation :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Pour désactiver la règle de conservation, définissez la valeur **-1**. Exécutez la commande suivante :

    ```
    ibmcloud logging option-show -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE est une valeur numérique définissant le nombre de jours.
    
**Exemple**
    
Par exemple, pour désactiver la durée de conservation d'un espace dont l'ID est *d35da1e3-b345-475f-8502-cfgh436902a3*, exécutez la commande suivante :

```
ibmcloud logging option-update -e -1
```
{: codeblock}


## Vérification de la règle de conservation des journaux d'un compte
{: #check_retention_policy_acc}

Afin d'obtenir la durée de conservation définie pour un compte, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)

2. Obtenez l'ID de compte.

    Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'un compte ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Obtenez la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud logging option-show -r account -i AccountID
    ```
    {: codeblock}

    La sortie est :

    ```
    ibmcloud logging option-show -r account -i kjskdsjfksjdflkjdsfbbd06461b066
    Showing log options of resource: kjskdsjfksjdflkjdsfbbd06461b066 ...

    Resource ID                              Retention   
    a:kjskdsjfksjdflkjdsfbbd06461b066       30   
	```
    {: screen}
	
## Vérification de la règle de conservation des journaux d'un espace
{: #check_retention_policy_space}

Afin d'obtenir la durée de conservation définie pour un espace, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Obtenez la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud logging option-show
    ```
    {: codeblock}

    La sortie est :

    ```
    ibmcloud logging option-show
    Showing log options of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    SpaceId                                Retention   
    12345678-1234-2edr-a9de-378620d6fab5   30   
	```
    {: screen}
    


## Définition de la règle de conservation des journaux au niveau du compte
{: #set_retention_policy_acc}

Procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)

2. Obtenez l'ID de compte.

    Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'un compte ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Définissez la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
    ```
    {: codeblock}
    
    où *RETENTION_VALUE* est un nombre entier qui définit le nombre de jours pendant lequel vous souhaitez conserver les journaux. 
    
    
**Exemple**
    
Par exemple, pour conserver un type de journal spécifique dans votre compte pendant seulement 15 jours, exécutez la commande suivante :

```
ibmcloud logging option-update -r account -i AccountID -e 15
```
{: codeblock}



## Définition de la règle de conservation des journaux pour un espace
{: #set_retention_policy_space}

Afin d'afficher la durée de conservation pour un espace, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
    
2. Définissez la durée de conservation. Exécutez la commande suivante :

    ```
    ibmcloud logging option-update -e RETENTION_VALUE
    ```
    {: codeblock}
    
    où *RETENTION_VALUE* est un nombre entier qui définit le nombre de jours pendant lequel vous souhaitez conserver les journaux.
    
    
**Exemple**
    
Par exemple, pour conserver les journaux disponibles dans un espace pendant un an, exécutez la commande suivante :

```
ibmcloud logging option-update -e 365
```
{: codeblock}




