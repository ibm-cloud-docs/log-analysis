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


# Obtention du jeton IAM
{: #auth_iam1}

Pour gérer les journaux qui sont disponibles dans le domaine de compte via l'API {{site.data.keyword.loganalysisshort}}, vous devez utiliser un jeton d'authentification. Utilisez l'interface de ligne de commande {{site.data.keyword.cloud_notm}} pour obtenir le jeton IAM. Le jeton possède un délai d'expiration. 
{:shortdesc}


## Obtention du jeton IAM
{: #iam_token_cli}

Pour obtenir le jeton d'autorisation via l'interface de ligne de commande {{site.data.keyword.cloud_notm}}, procédez comme suit à partir d'un terminal :

1. Installez l'interface de ligne de commande {{site.data.keyword.cloud_notm}}.

   Pour plus d'informations, voir [Téléchargement et installation de l'interface de ligne de commande {{site.data.keyword.Bluemix}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Si l'interface de ligne de commande est installée, passez à l'étape suivante.
    
2. Connectez-vous à une région dans {{site.data.keyword.cloud_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.cloud_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
3. Exécutez la commande `ibmcloud iam oauth-tokens` pour obtenir le jeton IAM.

    ```
	ibmcloud iam oauth-tokens
	```
	{: codeblock}
	
	La sortie renvoie le jeton IAM que vous devez utiliser pour authentifier votre ID utilisateur dans cet espace et dans cette organisation. Vous pouvez exporter le jeton IAM vers une variable de shell telle que `$iam_token`.



**Remarque :** lorsque vous utilisez le jeton, retirez *Bearer* de la valeur du jeton que vous avez transmis dans un appel d'API.

