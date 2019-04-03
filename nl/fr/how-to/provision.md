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


# Mise à disposition du service Log Analysis
{: #provision}

Vous pouvez mettre à disposition le service {{site.data.keyword.loganalysisshort}} à partir de l'interface utilisateur {{site.data.keyword.Bluemix}} ou de la ligne de commande.
{:shortdesc}


## Mise à disposition à partir de l'interface utilisateur
{: #ui}

Procédez comme suit pour mettre à disposition une instance du service {{site.data.keyword.loganalysisshort}} dans {{site.data.keyword.Bluemix_notm}} :

1. Connectez-vous à votre compte {{site.data.keyword.Bluemix_notm}}.

    Le tableau de bord {{site.data.keyword.Bluemix_notm}} se trouve à l'adresse suivante : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}.
    
	Une fois que vous êtes connecté avec votre ID utilisateur et votre mot de passe, l'interface utilisateur {{site.data.keyword.Bluemix_notm}} s'ouvre.

2. Cliquez sur **Catalogue**. La liste des services disponibles dans {{site.data.keyword.Bluemix_notm}} s'affiche.

3. Sélectionnez la catégorie **Developer Tools** pour filtrer la liste de services affichée.

4. Cliquez sur la vignette **Log Analysis**.

5. Sélectionnez un plan de service. Par défaut, le plan **Lite** est défini.

    Pour plus d'informations sur les plans de service, voir [Plans de service](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).
	
6. Cliquez sur **Créer** pour mettre à disposition le service {{site.data.keyword.loganalysisshort}} dans l'espace {{site.data.keyword.Bluemix_notm}} auquel vous êtes connecté.
  
 

## Mise à disposition à partir de l'interface de ligne de commande
{: #cli}

Procédez comme suit pour mettre à disposition une instance du service {{site.data.keyword.loganalysisshort}} dans {{site.data.keyword.Bluemix_notm}} via la ligne de commande :

1. [Prérequis] Installez l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.

   Pour plus d'informations, voir [Installation de l'interface de ligne de commande {{site.data.keyword.Bluemix_notm}}.](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)
   
   Si l'interface de ligne de commande est installée, passez à l'étape suivante.
    
2. Connectez-vous à la région, l'organisation et l'espace dans l'environnement {{site.data.keyword.Bluemix_notm}} dans lequel mettre le service à disposition. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
3. Exécutez la commande `ibmcloud service create` pour mettre à disposition une instance.

    ```
	ibmcloud service create service_name service_plan service_instance_name
	```
	{: codeblock}
	
	Où
	
	* service_name est le nom du service, en l'occurrence **ibmLogAnalysis**.
	* service_plan est le nom du plan de service. Pour la liste des plans, voir [Plans de service](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).
	* service_instance_name est le nom que vous souhaitez utiliser pour la nouvelle instance de service que vous créez.

	Par exemple, pour créer une instance du service {{site.data.keyword.loganalysisshort}} avec le plan Lite, exécutez la commande suivante :
	
	```
	ibmcloud service create ibmLogAnalysis standard my_logging_svc
	```
	{: codeblock}
	
4. Vérifiez que le service a été créé. Exécutez la commande suivante :

    ```	
	ibmcloud service list
	```
	{: codeblock}
	
	Le résultat de l'exécution de la commande se présente comme suit :
	
	```
    Getting services in org MyOrg / space MySpace as xxx@yyy.com...
    OK
    
    name                           service                  plan                   bound apps              last operation
    my_logging_svc                ibmLogAnalysis           standard                                        create succeeded
	```
	{: screen}

	



