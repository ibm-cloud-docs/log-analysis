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


# Conformité
{: #compliance}

[{{site.data.keyword.Bluemix}} fournit une plateforme cloud et des services qui respectent les normes strictes de sécurité d'IBM.](/docs/security/compliance.html#compliance). Le service {{site.data.keyword.loganalysislong}} est un service DevOps conçu pour {{site.data.keyword.Bluemix_notm}}. 
{:shortdesc}


## Règlement général sur la protection des données

Le règlement général sur la protection des données (RGPD) vise à créer une loi harmonisée sur la protection des données au sein de l'Union européenne et a pour objectif de redonner aux citoyens le contrôle de leurs données personnelles, tout en imposant des règles strictes à ceux qui hébergent et "traitent" ces données, n'importe où dans le monde. Ce règlement introduit également des règles en matière de libre circulation des données personnelles au sein et en dehors de l'UE. 

**Clause de protection :** le service {{site.data.keyword.loganalysisshort}} stocke et affiche les enregistrements de journal provenant des ressources de cloud qui s'exécutent sur votre compte dans {{site.data.keyword.Bluemix_notm}}, et provenant des journaux que vous pouvez envoyer depuis un emplacement externe à {{site.data.keyword.Bluemix_notm}}. Les informations personnelles ne doivent être incluses dans aucune des entrées de journal stockées dans {{site.data.keyword.loganalysisshort}} car ces données sont accessibles à d'autres utilisateurs au sein de votre entreprise, ainsi qu'à {{site.data.keyword.IBM_notm}} pour permettre la prise en charge du service cloud.

### Régions
{: #regions}

Le service {{site.data.keyword.loganalysisshort}} est conforme au RGPD (Règlement général sur la protection des données) dans les régions {{site.data.keyword.Bluemix_notm}} Public où le service est disponible.


### Conservation des données
{: #data_retention}

Le service {{site.data.keyword.loganalysisshort}} inclut deux référentiels de données dans lesquels vos données peuvent être stockées : 

* Log Search, qui héberge les données de journal disponibles pour l'analyse via Kibana.
* Log Collection, qui héberge les données de journal pour un stockage à long terme.

Selon le plan de service {{site.data.keyword.loganalysisshort}}, les données sont stockées dans Log Search, ou dans Log Search et Log Collection. Le plan standard ou Lite stocke uniquement les données dans Log Search. Les autres plans les stockent dans Log Search et Log Collection.

* Les journaux qui sont stockés dans le composant Log Search sont conservés pendant trois jours.
* Les journaux qui sont stockés dans le composant Log Collection sont conservés jusqu'à ce que vous configuriez une règle de conservation ou que vous les supprimiez manuellement. Par défaut, les journaux sont conservés indéfiniment dans Log Collection.



### Suppression des données
{: #data_deletion}

Prenez en compte les informations suivantes :

* Les journaux qui sont stockés dans le composant Log Search sont supprimés au bout de trois jours.

* Les journaux qui sont stockés dans le composant Log Collection sont supprimés après un certain nombre de jours lorsque vous configurez une règle de conservation, ou lorsque vous les supprimez manuellement. 

    Vous pouvez configurer une règle de conservation des journaux pour définir le nombre de jours pendant lequel vous souhaitez conserver les journaux dans Log Collection. Pour plus d'informations, voir [Affichage et configuration de la règle de conservation des journaux avec le plug-in {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy).

    Vous pouvez utiliser l'[API Log Collection](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} ou l'[interface de ligne de commande Log Collection](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window} pour supprimer manuellement des journaux depuis le composant Log Collection. 

    Vous pouvez utiliser l'interface de ligne de commande pour supprimer manuellement des journaux du composant Log Collection. Pour plus d'informations, voir [ibmcloud logging log-delete avec le plug-in {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs).


Si vous passez d'un plan payant au plan standard ou Lite, les journaux situés dans le composant Log Collection seront supprimés au bout d'une journée environ.

A tout moment, vous pouvez ouvrir un ticket de demande de service et demander que toutes vos données soient supprimées des composants Log Search et Log Collection. Pour plus d'informations sur l'ouverture d'un ticket de demande de service IBM, voir la rubrique décrivant [comment contacter le support](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support).



### Informations sur la tâche
{: #info}

Pour plus d'informations, voir :

[Conformité aux règles de sécurité {{site.data.keyword.Bluemix_notm}}](/docs/security/compliance.html#compliance)

[RGPD - Page officielle {{site.data.keyword.IBM_notm}}](https://www.ibm.com/data-responsibility/gdpr/)



