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


# Gestion des journaux
{: #manage_logs}

Vous pouvez utiliser l'interface de ligne de commande {{site.data.keyword.loganalysisshort}} et l'API {{site.data.keyword.loganalysisshort}} pour gérer les journaux qui sont stockés dans le composant Log Collection.
{:shortdesc}

Pour la gestion des journaux, tenez compte des informations suivantes :

1. L'ID utilisateur doit être associé à une règle dans {{site.data.keyword.cloud_notm}} pour {{site.data.keyword.loganalysisshort}} avec les droits permettant de gérer les journaux. 

    Pour la liste des rôles IAM et des tâches de chaque rôle, voir [Rôles IAM](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles). 
	
	Pour plus d'informations sur l'affectation d'une règle, voir [Affectation d'une règle IAM à un utilisateur dans l'interface utilisateur {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account).
	
2. Cette fonction est disponible uniquement pour les plans de service autorisant la conservation des journaux. 

    Pour plus d'informations sur les plans de service, voir [Plans de service](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

Le service {{site.data.keyword.loganalysisshort}} met à disposition deux interfaces de ligne de commande que vous pouvez utiliser pour gérer les journaux :

* Un plug-in {{site.data.keyword.cloud_notm}} {{site.data.keyword.loganalysisshort}}. Pour plus d'informations sur l'interface de ligne de commande, voir [Interface de ligne de commande {{site.data.keyword.loganalysisshort}} (plug-in {{site.data.keyword.cloud_notm}})](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli).
* Un plug-in CF {{site.data.keyword.loganalysisshort}} (déprécié). Pour plus d'informations sur l'interface de ligne de commande, voir [Configuration de l'interface de ligne de commande Log Analysis (plug-in CF)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#logging_cli).


## Configuration d'une règle de conservation des journaux
{: #log_retention_policy}

Vous pouvez utiliser l'interface de ligne de commande {{site.data.keyword.loganalysisshort}} pour afficher et configurer une règle de conservation des journaux. La règle spécifie le nombre de jours pendant lequel les journaux sont conservés dans le composant Log Collection. 

* Par défaut, lorsque vous sélectionnez un plan payant, les journaux sont collectés et conservés dans le composant Log Collection. 
* Lorsque vous définissez une durée de conservation, une fois que celle-ci est arrivée à expiration, les journaux sont supprimés automatiquement du composant Log Collection et ils ne peuvent pas être récupérés.
* Vous pouvez spécifier une durée de conservation pour un compte. La durée de conservation est configurée automatiquement pour tous les espaces de ce compte. 
* Vous pouvez spécifier une durée de conservation pour un espace.
* Vous pouvez modifier la règle de conservation à tout moment.
* Vous pouvez désactiver la règle en définissant la valeur *-1*. 

**Remarque :** lorsque vous désactivez la règle de conservation des journaux, vous
devez maintenir les journaux dans Log Collection. Vous pouvez utiliser la commande de l'interface de ligne de commande
[cf logging delete](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#delete4) pour supprimer les journaux anciens.

Pour plus d'informations, voir :

* [Affichage et configuration de la règle de conservation des journaux avec le plug-in {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy).
* [Affichage et configuration de la règle de conservation des journaux avec le plug-in CF](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy1#configuring_retention_policy).


## Suppression de journaux
{: #log_deletion}

Les journaux qui sont stockés dans le composant Log Search sont supprimés au bout de trois jours.

Les journaux qui sont stockés dans le composant Log Collection sont conservés jusqu'à ce que vous configuriez une règle de conservation ou que vous les supprimiez manuellement. 

* Vous pouvez configurer une règle de conservation des journaux pour définir le nombre de jours pendant lequel vous souhaitez conserver les journaux dans Log Collection. Pour plus d'informations, voir [Affichage et configuration de la règle de conservation des journaux avec le plug-in {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy).

* Vous pouvez utiliser l'[API Log Collection](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} ou l'[interface de ligne de commande Log Collection](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window} pour supprimer manuellement des journaux depuis le composant Log Collection. 

* Vous pouvez utiliser l'interface de ligne de commande. Pour plus d'informations sur la suppression manuelle des journaux via l'interface de ligne de commande, voir [ibmcloud logging log-delete avec le plug-in {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs).
    


## Téléchargement des journaux
{: #download_logs2}

Dans Kibana, vous pouvez rechercher les journaux des 3 derniers jours. Pour pouvoir analyser des données de journal plus anciennes, vous pouvez télécharger les journaux vers un fichier
local ou les diriger vers d'autres programmes comme par exemple une instance locale d'Elastic Stack. 

Pour plus d'informations, voir :

* [Téléchargement des journaux avec le plug-in {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs#downloading_logs).
* [Téléchargement des journaux avec le plug-in CF](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs1#downloading_logs1).



## Obtention d'informations sur les journaux
{: #info_about_logs}

Pour obtenir des informations générales sur vos journaux, utilisez la commande `ibmcloud logging log-show` ou `cf logging status`. Pour plus d'informations, voir :

* [Affichage des informations sur le journal avec le plug-in {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status1#viewing_log_status1)
* [Affichage des informations sur le journal avec le plug-in CF](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status#viewing_log_status1).

Par exemple, pour contrôler les coûts, il est utile de connaître la taille des journaux de vos applications pendant une période donnée. Ainsi, vous pouvez décider de surveiller la taille de chaque
type de journal pendant une semaine pour un espace {{site.data.keyword.cloud_notm}} afin de déterminer si une application ou un service génère plus de journaux que prévu. Pour vérifier la taille de vos journaux, utilisez la commande `ibmcloud logging log-show` ou `cf logging status`.

Vous pouvez afficher des informations sur les journaux qui sont stockés dans un domaine d'espace, un domaine d'organisation ou un domaine de compte.



## Installation de l'interface de ligne de commande {{site.data.keyword.loganalysisshort_notm}} (plug-in {{site.data.keyword.cloud_notm}})
{: #install_cli2}

Pour savoir comment installer l'interface de ligne de commande, voir
[Installation de l'interface de ligne de commande de journalisation](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli).

Pour vérifier la version de l'interface de ligne de commande, exécutez la commande `ibmcloud plugin list`.

Pour obtenir de l'aide sur l'exécution des commandes, voir [Aide sur
l'utilisation de la ligne de commande pour exécuter les commandes](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#command_cli_help).


## Noeuds finaux de journalisation
{: #endpoints}

Le tableau suivant répertorie les URL de journalisation par région :

<table>
    <caption>Noeuds finaux par région</caption>
    <tr>
      <th>Région</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>Francfort</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>Sydney</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td>Royaume-Uni</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>Sud des Etats-Unis</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## Rôles requis par un utilisateur pour gérer les journaux
{: #roles1}

Dans {{site.data.keyword.cloud_notm}}, vous pouvez affecter un ou plusieurs rôles à des utilisateurs. Ces rôles définissent quelles tâches sont activées pour que cet utilisateur puisse utiliser le service {{site.data.keyword.loganalysisshort}}. 

Les tableaux suivants répertorient les rôles qu'un utilisateur doit avoir pour pouvoir gérer les journaux :

<table>
  <caption>Droits requis par un **propriétaire de compte** pour gérer les journaux</caption>
  <tr>
	<th>Rôle IAM</th>
	<th>Actions</th>
  </tr>
  <tr>
    <td>*Administrateur*</td>
    <td>Vérifier le statut des journaux </br>Télécharger les journaux </br>Supprimer les journaux </br>Changer la règle de conservation des journaux </br>Gérer les sessions </td>
</table>

<table>
  <caption>Droits requis par un **auditeur** pour gérer les journaux</caption>
  <tr>
	<th>Rôle IAM</th>
	<th>Actions</th>
  </tr>
  <tr>
    <td>*Afficheur*</td>
    <td>Obtenir des informations sur les journaux hébergés dans le composant Log Collection </br>Obtenir des informations sur la règle de conservation des journaux qui est configurée </td>
</table>

<table>
  <caption>Droits requis par un **administrateur** pour gérer les journaux</caption>
  <tr>
	<th>Rôle IAM</th>
	<th>Actions</th>
  </tr>
  <tr>
    <td>*Administrateur*</td>
    <td>Vérifier le statut des journaux </br>Télécharger les journaux </br>Supprimer les journaux </br>Changer la règle de conservation des journaux </br>Gérer les sessions </td>
</table>

<table>
  <caption>Droits requis par un **développeurs** pour gérer les journaux.</caption>
  <tr>
	<th>Rôle IAM</th>
	<th>Actions</th>
  </tr>
  <tr>
    <td>*Editeur*</td>
    <td>Vérifier le statut des journaux </br>Télécharger les journaux </br>Supprimer les journaux </br>Changer la règle de conservation des journaux </br>Gérer les sessions</td>
</table>

