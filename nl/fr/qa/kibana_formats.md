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

# Formats de journal Kibana
{: #kibana_formats}

Vous pouvez configurer Kibana pour afficher dans la page *Discover* différentes zones pour chaque entrée de journal.
{:shortdesc}



## Format de journal Kibana pour les applications Cloud Foundry
{: #kibana_log_format_cf}

Vous pouvez configurer Kibana pour afficher dans la page *Discover* les zones suivantes pour chaque entrée de journal :

| Zone | Description |
|-------|-------------|
| @timestamp | `yyyy-MM-jjTHH:mm:ss:SS-0500`  <br> Heure à laquelle l'événement a été consigné. <br> L'horodatage est défini à la milliseconde près. |
| @version | Version de l'événement. |
| ALCH_TENANT_ID | ID de l'espace {{site.data.keyword.Bluemix_notm}}. |
| \_id | ID unique de votre document de journal. |
| \_index | Index de votre entrée de journal. |
| \_type | Type de journal, par exemple, *syslog*. |
| app_name | Nom de votre application. |
| application_id | ID unique de votre application. |
| hôte | Nom de l'application ayant produit les données de journal. |
| instance_id | ID d'instance de l'instance d'application ayant produit les données de journal. |
| loglevel | Niveau de gravité de l'événement consigné. |
| message | Message émis par le composant. <br> Il varie selon le contexte. |
| message_type | Flux dans lequel le message de journal est écrit. <br> * **OUT** fait référence au flux de sortie standard (stdout) <br> * **ERR** fait référence au flux d'erreur standard (stderr). |
| org_id | ID unique de votre organisation {{site.data.keyword.Bluemix_notm}}. |
| org_name | Nom de l'organisation {{site.data.keyword.Bluemix_notm}} dans laquelle votre application est constituée en préproduction. |
| origin | Composant ayant généré l'événement. |
| source_id | Composant qui génère les journaux. <br> La liste suivante décrit les journaux provenant de chaque composant : <br> * **API** : Réponses consignées vers les
appels d'API qui requièrent une modification de l'état de votre application. <br> * **APP** : Réponses consignées depuis votre application. <br> * **CELL** : Réponses consignées depuis la cellule Diego et qui indique quand une application démarre, s'arrête ou tombe en panne. <br> * **LGR** : Réponses consignées depuis loggregator et qui indique des problèmes affectant le processus de journalisation. <br> * **RTR**: Réponses consignées depuis le composant Router quand il achemine des demandes HTTP à votre application. <br> *
**SSH** : Réponses consignées depuis la cellule Diego lorsqu'un utilisateur accède à un conteneur d'application à l'aide de la commande `cf ssh`. <br> *
**STG** : Réponses consignées depuis la cellule Diego ou l'agent DEA (Droplet Execution Agent) quand votre application est constituée ou reconstituée en préproduction. |
| space_name | Nom de l'espace {{site.data.keyword.Bluemix_notm}} dans lequel votre application est constituée en préproduction. |
| timestamp | Heure à laquelle l'événement a été consigné. L'horodatage est défini à la milliseconde près. |
{: caption="Tableau 1. Zones des applications Cloud Foundry" caption-side="top"}



## Format de journal Kibana pour les conteneurs Docker déployés dans un cluster Kubernetes
{: #kibana_log_format_containers_kubernetes}

Vous pouvez configurer Kibana pour afficher dans la page *Discover* les zones suivantes pour chaque entrée de journal. Des zones sont définies par {{site.data.keyword.IBM}} et incluent vos données de message. 

| Zone | Description | Autres informations |
|-------|-------------|---------------------------|
| @timestamp | `yyyy-MM-jjTHH:mm:ss:SS-0500`  <br> Heure à laquelle l'événement a été consigné. <br> L'horodatage est défini à la milliseconde près. | |
| @version | Version de l'événement. | |
| ALCH_TENANT_ID | ID de l'espace {{site.data.keyword.Bluemix_notm}}. | |
| \_id | ID unique de votre document de journal. | |
| \_index | Index de votre entrée de journal. | |
| \_score |  |  |
| \_type | Type de journal. Par exemple, *logs*. | |
| crn_str | Informations sur la source du journal. | Par défaut, cette zone est définie par {{site.data.keyword.IBM_notm}}. <br> **Remarque **: si vous envoyez le message sous un format JSON valide et que l'une des zones est nommée `crn`, la valeur de la zone est remplacée par celle définie dans le message.  |  
| docker.container_id_str | Identificateur global unique du conteneur s'exécutant dans un pod. | |
| ibm-containers.account_str | Identificateur global unique du compte {{site.data.keyword.Bluemix_notm}}.  |  |
| ibm-containers.cluster_id_str | Identificateur global unique du cluster Kubernetes.  |  |
| ibm-containers.cluster_type_str |  | Valeur réservée pour utilisation interne {{site.data.keyword.IBM_notm}}. |
| ibm-containers.region_str | Région dans {{site.data.keyword.Bluemix_notm}}.  |  |
| kubernetes.container_name_str | Nom du conteneur dans lequel une application est déployée.  |  |
| kubernetes.host | Adresse IP publique de l'agent sur lequel le conteneur s'exécute. |  |
| kubernetes.labels.*exemple_nom_libellé*\_str | Paire clé-valeur associée à un objet Kubernetes tel qu'un pod. | Chaque libellé associé à un objet Kubernetes est répertoriée sous forme de zone dans l'entrée de journal affichée dans Kibana. <br> Vous pouvez ne pas les utiliser ou en utiliser plusieurs. |
| kubernetes.namespace_name_str | Espace de nom Kubernetes où le conteneur est déployé. |  |
| kubernetes.pod_id_str | Identificateur global unique du pod où le conteneur est déployé. |  |
| kubernetes.pod_name_str | Nom du pod. |  |
| message | Message complet. | Si vous envoyez un message avec un format JSON valide, chaque zone est analysée individuellement et affichée dans Kibana.  |
| stream_str |  | Valeur réservée pour utilisation interne {{site.data.keyword.IBM_notm}}. |
|tag_str |  | Valeur réservée pour utilisation interne {{site.data.keyword.IBM_notm}}. |
{: caption="Tableau 3. Zones pour conteneurs Docker" caption-side="top"}


## Format de journal Kibana pour {{site.data.keyword.messagehub}}
{: #kibana_log_format_messagehub}

Vous pouvez configurer Kibana pour afficher dans la page *Discover* les zones suivantes pour chaque entrée de journal :

| Zone | Description |
|-------|-------------|
| @timestamp | `yyyy-MM-jjTHH:mm:ss:SS-0500`  <br> Heure à laquelle l'événement a été consigné. <br> L'horodatage est défini à la milliseconde près. |
| @version | Version de l'événement. |
| ALCH_TENANT_ID | ID de l'espace {{site.data.keyword.Bluemix_notm}}. |
| \_id | ID unique de votre document de journal. |
| \_index | Index de votre entrée de journal. |
| \_type | Type de journal, par exemple, *syslog*. |
| loglevel | Gravité de l'événement consigné. Par exemple, **Info**. |
| module | Cette zone est définie sur **MessageHub**. |
{: caption="Tableau 4. Zones des événements {{site.data.keyword.messagehub}}" caption-side="top"}

Exemple d'entrée de journal :

```
March 8th 2017, 17:15:16.454	

message:
    Creating topic ABC
@version:
    1
@timestamp:
    March 8th 2017, 17:15:16.454
loglevel:
    Info
module:
    MessageHub
ALCH_TENANT_ID:
    3d8d2eae-f3f0-44f6-9717-126113a00b51
&#95;id:
    AVqu6vJl1zcfr8KYMI95
&#95;type:
    logs
&#95;index:
    logstash-2017.03.08
```
{: screen}


