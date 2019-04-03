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


# Calcul du quota de recherche et de l'utilisation quotidienne
{: #quota}

Pour obtenir le quota et l'utilisation quotidienne actuelle d'un domaine de journaux du service {{site.data.keyword.loganalysisshort}}, vous pouvez exécuter une commande cURL. 
{:shortdesc}

## Calcul du quota de recherche et de l'utilisation quotidienne à l'aide de l'interface de ligne de commande
{: #quota_cli}

Procédez comme suit :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}}.

    Par exemple, pour vous connecter à la région Sud des Etats-Unis, exécutez la commande suivante :

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Exécutez la commande d'interface de ligne de commande `ibmcloud logging quota-usage-show`. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    où 

    * Les valeurs admises pour RESOURCE_TYPE sont les suivantes : space, account
    * RESOURCE_ID est l'identificateur global unique du compte ou de l'espace dont vous voulez obtenir l'utilisation de quota.


Par exemple, pour afficher l'utilisation du quota d'un compte, exécutez la commande suivante :

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage   
524288000         0   
```
{: screen}

Pour afficher l'utilisation du quota d'un espace, exécutez la commande suivante :

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage   
524288000         6774014   
```
{: screen}


## Obtention de l'historique du quota de recherche à l'aide de l'interface de ligne de commande
{: #quota_history_cli}


Procédez comme suit :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}}.

    Par exemple, pour vous connecter à la région Sud des Etats-Unis, exécutez la commande suivante :

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Exécutez la commande d'interface de ligne de commande `ibmcloud logging quota-usage-show` avec le paramètre `-s`. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    où 

    * Les valeurs admises pour RESOURCE_TYPE sont les suivantes : space, account
    * RESOURCE_ID est l'identificateur global unique du compte ou de l'espace dont vous voulez obtenir l'utilisation de quota.

Par exemple

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}



## Calcul du quota de recherche et de l'utilisation quotidienne d'un compte à l'aide de l'API
{: #account}

Procédez comme suit :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Obtenez l'ID du compte. Exécutez la commande suivante :

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	La liste des comptes avec leur identificateur global unique s'affiche.
	
	Exportez l'ID de compte dans une variable de shell. Exemple :
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. Obtenez le jeton UAA. 

    Pour plus d'informations, voir [Obtention du jeton UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exportez le jeton UAA dans une variable de shell. N'incluez pas le préfixe `Bearer`. Exemple :
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Obtenez le quota du domaine et l'utilisation actuelle. Exécutez la commande suivante :

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	où *ENDPOINT* est différent selon la région. Pour la liste des noeuds finaux par région, voir [Noeuds finaux de journalisation](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).
	
	Par exemple, exécutez la commande cURL afin d'obtenir le quota pour le compte dans la région Sud des Etats-Unis :
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	Le résultat inclut les informations relatives à l'utilisation et au quota quotidiens.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}

	
## Calcul du quota de recherche et de l'utilisation quotidienne d'un espace à l'aide de l'API
{: #space1}

Procédez comme suit :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Obtenez l'ID de l'espace.

    Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'un espace ?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid).
	
	Exportez l'ID d'espace dans une variable de shell. Exemple :
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. Obtenez le jeton UAA. 

    Pour plus d'informations, voir [Obtention du jeton UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exportez le jeton UAA dans une variable de shell. N'incluez pas le préfixe `Bearer`. Exemple :
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Obtenez le quota du domaine et l'utilisation actuelle. Exécutez la commande suivante :

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	où *ENDPOINT* est différent selon la région. Pour la liste des noeuds finaux par région, voir [Noeuds finaux de journalisation](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).

    Par exemple, exécutez la commande cURL suivante pour obtenir le quota et l'utilisation d'un domaine d'espace dans la région Sud des Etats-Unis :
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	Le résultat inclut les informations relatives à l'utilisation et au quota quotidiens.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}



