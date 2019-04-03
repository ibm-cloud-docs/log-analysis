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


# Changement de plan
{: #change_plan}

Vous pouvez changer de plan de service {{site.data.keyword.loganalysisshort}} dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}} ou en exécutant la commande `ibmcloud service update`. Vous
pouvez choisir un plan de niveau supérieur ou inférieur à tout moment.
{:shortdesc}

## Modification du plan de service via l'interface utilisateur
{: #change_plan_ui}

Pour changer votre plan de service dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}, procédez comme suit :

1. Connectez-vous à {{site.data.keyword.Bluemix_notm}} : [http://bluemix.net ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](http://bluemix.net){:new_window}. 

2. Sélectionnez la région, l'organisation et l'espace où le service {{site.data.keyword.loganalysisshort}} est disponible.  

3. Cliquez sur l'instance de service {{site.data.keyword.loganalysisshort}} dans le *tableau de bord* {{site.data.keyword.Bluemix_notm}}. 
    
4. Sélectionnez l'onglet **Plan** dans le tableau de bord {{site.data.keyword.loganalysisshort}}.

    Des informations sur le plan en cours s'affichent.
	
5. Sélectionnez un nouveau plan de niveau supérieur ou inférieur. 

6. Cliquez sur **Sauvegarder**.




## Modification du plan de service via l'interface de ligne de commande
{: #change_plan_cli}

Pour modifier votre plan de service dans Bluemix via l'interface de ligne de commande, procédez comme suit :

1. Connectez-vous à une région, une organisation et un espace dans {{site.data.keyword.Bluemix_notm}}. 

    Pour plus d'informations, voir [Comment se connecter à {{site.data.keyword.Bluemix_notm}} ?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)
	
2. Exécutez la commande `ibmcloud service list` pour identifier le plan en cours et obtenir le nom du service {{site.data.keyword.loganalysisshort}} depuis la liste des services qui est disponible dans l'espace. 

    La valeur de la zone **name** est celle que vous devez utiliser pour modifier le plan. 

    Exemple :
	
	```
	$ ibmcloud service list
    Invoking 'cf services'...

    Getting services in org MyOrg / space dev as xxx@ibm.com...
    OK

    name                           service                  plan             bound apps            last operation
    Log Analysis-m2                ibmLogAnalysis           premium                                update succeeded
    ```
	{: screen}
    
3. Choisissez un plan de niveau supérieur ou inférieur. Exécutez la commande `ibmcloud service update`.
    
	```
	ibmcloud service update service_name [-p new_plan]
	```
	{: codeblock}
	
	où 
	
	* *service_name* est le nom de votre service. Vous pouvez exécuter la commande `ibmcloud service list` pour obtenir la valeur.
	* *new_plan* est le nom du plan.
	
	Le tableau suivant présente les différents plans et les valeurs prises en charge :
	
	<table>
	  <caption>Tableau 1. Liste des plans</caption>
	  <tr>
	    <th>Plan</th>
	    <th>Nom</th>
	  </tr>
	  <tr>
	    <td>Lite</td>
	    <td>standard</td>
	  </tr>
	  <tr>
	    <td>Collecte de journaux</td>
	    <td>premium</td>
	  </tr>
	  <tr>
	    <td>Collecte de journaux avec recherche de 2 Go/jour</td>
	    <td>premiumsearch2</td>
	  </tr>
	  <tr>
	    <td>Collecte de journaux avec recherche de 5 Go/jour</td>
	    <td>premiumsearch5</td>
	  </tr>
	  <tr>
	    <td>Collecte de journaux avec recherche de 10 Go/jour</td>
	    <td>premiumsearch10</td>
	  </tr>
	</table>
	
	Par exemple, pour passer au plan de niveau inférieur *Lite*, exécutez la commande suivante :
	
	```
	ibmcloud service update "Log Analysis-m2" -p standard
    Updating service instance Log Analysis-m2 as xxx@ibm.com...
    OK
	```
	{: screen}

4. Vérifiez que le nouveau plan est modifié. Exécutez la commande `ibmcloud service list`.

  ```
	ibmcloud service list
	```
	{: codeblock}






