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

# Machines virtuelles
{: #logging_vm_ov}

Les fonctions de journalisation ne sont pas activées automatiquement pour les machines virtuelles. Cependant, vous pouvez configurer votre machine virtuelle pour envoyer des journaux à Log Collection. Pour collecter et envoyer des données de journal d'une machine virtuelle au service {{site.data.keyword.loganalysisshort}}, vous devez configurer un
réexpéditeur Logstash à service partagé (mt-logstash-forwarder). Vous pouvez ensuite afficher, filtrer et analyser les journaux dans Kibana.
{:shortdesc}


## Ingestion de journaux
{: #log_ingestion2}

Le service {{site.data.keyword.loganalysisshort}} propose différents plans. Tous les
plans, à l'exception du plan *Lite*, permettent d'envoyer des journaux à Log Collection. Pour plus d'informations sur les plans, voir
[Plans de service](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

Vous pouvez envoyer des journaux dans {{site.data.keyword.loganalysisshort}} à l'aide du réexpéditeur mt-logstash-forwarder. Pour plus d'informations, voir [Envoyer des données de journaux à l'aide d'un réexpéditeur Logstash à service partagé (mt-logstash-forwarder)](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt).


## Collecte de journaux
{: #log_collection2}

Par défaut, {{site.data.keyword.Bluemix_notm}} stocke les données de journal jusqu'à 3 jours :   

* Un maximum de 500 Mo par espace de données est stocké par jour. Les journaux dépassant le plafond de 500 Mo sont rejetés. Les allocations de plafond sont réinitialisées chaque jour à
00h30 (temps universel coordonné).
* Il est possible de rechercher jusqu'à 1,5 Go de données sur un maximum de 3 jours. Les données de journal sont écrasées (sur la base Premier entré, premier sorti) une fois que la
limite de 1,5 Go de données est atteinte ou au bout de 3 jours.

Le service {{site.data.keyword.loganalysisshort}} fournit des plans additionnels qui vous permettent de stocker des journaux dans Log Collection aussi longtemps que vous
en avez besoin. Pour obtenir plus d'informations sur le tarif de chaque plan, voir [Plans de service](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

* Vous pouvez configurer une règle de conservation des journaux que vous pouvez utiliser pour définir le nombre de jours pendant lequel vous souhaitez conserver les journaux dans Log Collection. Pour plus d'informations, voir [Règle de conservation des journaux](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#log_retention_policy).
* Vous pouvez supprimer les journaux manuellement via l'interface de ligne de commande de Log Collection ou l'API.


## Recherche de journaux
{: #log_search2}

Par défaut, vous pouvez utiliser Kibana pour rechercher jusqu'à 500 Mo de journaux par jour dans {{site.data.keyword.Bluemix_notm}}. 

Le service {{site.data.keyword.loganalysisshort}} fournit plusieurs plans. Chaque plan offre des fonctions de recherche de journaux différentes. Par exemple, le plan
*Collecte de journaux* vous permet de rechercher jusqu'à 1 Go de données par jour. Pour plus d'informations sur les plans, voir
[Plans de service](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).


## Analyse des journaux
{: #log_analysis}

Afin d'analyser les données de journal, utilisez Kibana pour effectuer des tâches analytiques avancées. Vous pouvez utiliser la plateforme de visualisation et d'analyse open source Kibana pour surveiller, rechercher, analyser et afficher des données dans différents graphiques, par exemple dans des diagrammes et des tableaux. Pour plus d'informations, voir [Analyse des journaux dans Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#analyzing_logs_Kibana).
