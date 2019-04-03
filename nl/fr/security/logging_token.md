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


# Obtention du jeton de journalisation
{: #logging_token}

Obtenez un jeton de journalisation pour envoyer des journaux au service {{site.data.keyword.loganalysisshort}}. 
{:shortdesc}


## Obtention du jeton de journalisation pour envoyer des journaux dans un espace via l'interface de ligne de commande {{site.data.keyword.loganalysisshort}} 
{: #logging_token_la_cloud_cli}

Pour obtenir le jeton de journalisation que vous pouvez utiliser pour envoyer des journaux au service {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Téléchargement et installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Si l'interface de ligne de commande est installée, passez à l'étape suivante.
    
2. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
3. Exécutez la commande suivante :

    ```
	ibmcloud logging token-get
	```
	{: codeblock}

La sortie renvoie le jeton de journalisation.


## Obtention du jeton de journalisation pour envoyer des journaux dans un espace via l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}} 
{: #logging_token_cloud_cli}

Pour obtenir le jeton de journalisation que vous pouvez utiliser pour envoyer des journaux au service {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Téléchargement et installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Si l'interface de ligne de commande est installée, passez à l'étape suivante.
    
2. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
3. Créez une clé de service dans l'espace dans lequel le service {{site.data.keyword.loganalysisshort}} est mis à disposition. Exécutez les commandes suivantes :

    Répertoriez les services afin d'obtenir le nom de l'instance {{site.data.keyword.loganalysisshort}} dans l'espace :
	
    ```
	ibmcloud service list
	```
	{: codeblock}
	
	Exemple :
	
	```
	ibmcloud service list
    Invoking 'cf services'...

    Getting services in org lopezdsr_org / space dev as xxx@yyyy...
    OK

    name              service          plan       bound apps   last operation
    Log Analysis-vg   ibmloganalysis   standard                create succeeded
    ```
	{: screen}
	
	Créez une clé. Utilisez la valeur de **name** pour servicename et entrez le nom de votre clé.
	
	```
	ibmcloud service key-create servicename KeyName 
	```
	{: codeblock}
	
	Exemple :
	
	```
	ibmcloud service key-create "Log Analysis-vg" mykey2
    Invoking 'cf create-service-key Log Analysis-vg mykey2'...

    Creating service key mykey2 for service instance Log Analysis-vg as xxx@yyyy...
    OK
    ```
	{: screen}
	
4. Obtenez le jeton de journalisation. Exécutez la commande suivante :
	
	```
	ibmcloud service key-show name Keyname
	```
	{: codeblock}
	
	Exemple : 
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" 
    Invoking 'cf service-key Log Analysis-vg mykey2'...

    Getting key mykey2 for service instance Log Analysis-vg as xxx@yyyy...

    {
     "LOG_INGESTION_MTLJ_URL": "https://ingest-eu-fra.logging.bluemix.net:9091",
     "logging_token": "sdtghyrtfde4",
     "space_id": "12345678-avfg-erft-b1f2-2efrtgcb1744"
    }
    ```
	{: screen}
	
	Pour obtenir le jeton de journalisation, vous pouvez exécuter la commande suivante :
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" | tail -n +4 | jq -r .logging_token
    sdtghyrtfde4
	```
	{: screen}


	
## Obtention du jeton de journalisation pour envoyer des journaux dans un espace via l'API Log Analysis
{: #logging_token_api}


Pour obtenir le jeton de journalisation que vous pouvez utiliser pour envoyer des journaux au service {{site.data.keyword.loganalysisshort}}, procédez comme suit :

1. Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Téléchargement et installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Si l'interface de ligne de commande est installée, passez à l'étape suivante.
    
2. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
3. Obtenez le [jeton UAA](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#uaa_cli).

    Par exemple, exécutez la commande `ibmcloud cf oauth-token` pour obtenir le jeton UAA.

    ```
	ibmcloud cf oauth-token
	```
	{: codeblock}
	
	La sortie renvoie le jeton UAA que vous devez utiliser pour authentifier votre ID utilisateur dans cet espace et dans cette organisation.

4. Obtenez l'identificateur global unique de l'espace.

   Pour plus d'informations, voir [Comment obtenir l'identificateur global unique d'un espace ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#space_guid2).  
	
5. Exportez les variables suivantes : TOKEN et SPACEID.

    * *TOKEN* est le jeton oauth que vous avez obtenu à l'étape précédente sans le préfixe Bearer.
	
	* *SPACEID* est l'identificateur global unique de l'espace que vous avez obtenu à l'étape précédente. 
		
	Exemple :
	
	```
	export TOKEN="eyJhbGciOiJI....cGFzc3dvcmQiLCJjZiIsInVhYSIsIm9wZW5pZCJdfQ.JaoaVudG4jqjeXz6q3JQL_SJJfoIFvY8m-rGlxryWS8"
	export SPACEID="667fb895-abcd-defg-aaaa-cf4587341095"
	```
	{: screen}
	
6. Obtenez le jeton de journalisation. Exécutez la commande suivante :
 
    ```
	curl -k -X GET  --header "X-Auth-Token: ${TOKEN}"  --header "X-Auth-Project-Id: s-${SPACEID}"  LOGGING_ENDPOINT/token
    ```
    {: codeblock}	
	
	où
	* SPACEID est l'identificateur global unique de l'espace dans lequel le service s'exécute.
	* TOKEN est le jeton UAA que vous avez obtenu à l'étape précédente sans le préfixe Bearer.
	* LOGGING_ENDPOINT est le noeud final {{site.data.keyword.loganalysisshort}} pour la région {{site.data.keyword.Bluemix_notm}} où l'organisation et l'espace sont disponibles. LOGGING_ENDPOINT est différent selon la région. Pour afficher les URL des différents noeuds finaux, voir [Noeuds finaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#endpoints).
	
    La commande renvoie le jeton de journalisation que vous devez utiliser pour envoyer des journaux dans cet espace.
	
