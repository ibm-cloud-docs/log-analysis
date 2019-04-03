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


# Obtention du jeton UAA
{: #auth_uaa}

Pour gérer les journaux qui sont disponibles dans le domaine d'espace via l'API {{site.data.keyword.loganalysisshort}}, vous devez utiliser un jeton d'authentification.
{:shortdesc}

		
## Obtention du jeton UAA
{: #uaa_cli}


Pour obtenir le jeton d'autorisation, procédez comme suit :

1. Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Téléchargement et installation de l'interface de ligne de commande {{site.data.keyword.Bluemix}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Si l'interface de ligne de commande est installée, passez à l'étape suivante.
    
2. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
3. Exécutez la commande `ibmcloud iam oauth-token` pour obtenir le jeton UAA {{site.data.keyword.Bluemix_notm}}.

    ```
	ibmcloud iam oauth-token
	```
	{: codeblock}
	
	La sortie renvoie le jeton UAA que vous devez utiliser pour authentifier votre ID utilisateur dans cet espace et dans cette organisation.
	

**Remarque :** lorsque vous utilisez le jeton, retirez *Bearer* de la valeur du jeton que vous avez transmis dans un appel d'API.
