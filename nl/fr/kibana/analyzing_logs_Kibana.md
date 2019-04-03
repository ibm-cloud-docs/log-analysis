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

# Affichage et analyse des journaux (Kibana)
{:#analyzing_logs_Kibana}

Vous pouvez utiliser la plateforme de visualisation et d'analyse open source Kibana 5.1 pour surveiller, rechercher, analyser et afficher des données dans différents graphiques, par exemple dans des diagrammes et des tableaux. Utilisez Kibana pour effectuer des tâches analytiques avancées.
{:shortdesc}

Kibana est une interface basée navigateur dans laquelle vous pouvez analyser de manière interactive vos données et personnaliser des tableaux de bord que vous pourrez ensuite utiliser pour analyser les données de journal et effectuer des tâches de gestion avancées. Pour plus d'informations, voir le manuel [Kibana User Guide ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.

Les données qu'affiche une page Kibana sont circonscrites par une recherche. Le jeu de données par défaut est défini par le canevas d'index préconfiguré. Pour filtrer les informations, vous pouvez ajouter de nouvelles requêtes de recherche et appliquer des filtres au jeu de données par défaut. Vous pouvez ensuite sauvegarder la recherche pour une réutilisation future. 

Kibana inclut différentes pages que vous pouvez utiliser pour analyser vos journaux :

| Page Kibana | Description |
|-------------|-------------|
| Discover | Utilisez cette page pour définir des recherches et analyser vos journaux de manière interactive via un tableau et un histogramme. |
| Visualize | Utilisez cette page pour créer des visualisations (par exemple, des graphiques et des tableaux) que vous pourrez utiliser pour analyser vos données de journal et comparer les résultats.  |
| Dashboard | Utilisez cette page pour analyser vos journaux via des collections de visualisations et de recherches sauvegardées.  |
{: caption="Tableau 1. Pages Kibana" caption-side="top"}

**Remarque :** vous ne pouvez analyser qu'une journée entière à la fois via la page Visualize ou la page Dashboard, même si vous pouvez revenir 3 jours en arrière. Les
données de journal sont stockées pendant 3 jours par défaut. 

| Page Kibana | Période de temps |
|-------------|-------------------------|
| Discover | Analyse des données pendant un maximum de 3 jours. |
| Visualize | Analyse des données sur une période de 24 heures. <br> Vous pouvez filtrer les données de journal sur une période personnalisée couvrant 24 heures.  |
| Dashboard | Analyse des données sur une période de 24 heures. <br> Vous pouvez filtrer les données de journal sur une période personnalisée couvrant 24 heures. <br> Le sélecteur de période que vous définissez s'applique à toutes les visualisations incluses dans le tableau de bord. |
{: caption="Tableau 2. Informations de période" caption-side="top"}

Vous pourriez, par exemple, utiliser Kibana ainsi pour afficher des informations sur une application CF ou un conteneur dans votre espace via les différentes pages :

## Accédez au tableau de bord Kibana
{: #launch_Kibana}

Vous pouvez lancer Kibana en procédant de l'une des manières suivantes :

* Depuis le tableau de bord du service {{site.data.keyword.loganalysisshort}}

    Vous pouvez lancer Kibana pour que les données affichées agrègent les journaux des services dans un espace spécifique.
	
	Pour plus d'informations, voir [Accès à Kibana à partir du tableau de bord du service Log Analysis. ](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_log_analysis)

* Depuis {{site.data.keyword.Bluemix_notm}}

    Vous pouvez ouvrir vos journaux d'application CF spécifiques dans Kibana,
dans le contexte de cette application spécifique. Pour plus d'informations, voir [Accès à Kibana depuis le tableau de bord ou une application CF](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app).
    
    Vous pouvez ouvrir vos journaux de conteneur Docker spécifiques dans Kibana,
dans le contexte de ce conteneur spécifique. Cette fonction s'applique uniquement aux conteneurs qui sont déployés dans l'infrastructure gérée par {{site.data.keyword.Bluemix_notm}}. Pour plus d'informations, voir [Accès à Kibana depuis le tableau de bord d'un conteneur](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers).
    
    Pour les applications CF, la requête utilisée pour filtrer les données disponibles pour l'analyse dans Kibana extrait les entrées de journal de l'application Cloud Foundry. Les informations de journal affichées par défaut par Kibana ne concernent qu'une application Cloud Foundry unique et toutes ses instances. 
    
    Pour les conteneurs, la requête utilisée pour filtrer des données disponibles pour l'analyse dans Kibana extrait les entrées de journal pour toutes les instances du conteneur. Les informations de journal affichées par défaut par Kibana ne concernent qu'un conteneur unique, ou un groupe de conteneurs, et toutes ses instances. 
    
    

* A partir d'un lien de navigateur direct

    Vous pouvez lancer Kibana pour que les données affichées agrègent les journaux des services dans un espace spécifique.
    
    La requête utilisée pour filtrer les données affichées dans le tableau de bord extrait des entrées de journal pour un espace dans l'organisation {{site.data.keyword.Bluemix_notm}}. Les informations de journal affichées par Kibana incluent des enregistrements sur toutes les ressources déployées dans l'espace de l'organisation {{site.data.keyword.Bluemix_notm}} à laquelle vous êtes connecté. 
    
    Pour plus d'informations, voir [Accès au tableau de bord Kibana depuis un navigateur Web](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser).
    
    

## Analyse des données de manière interactive
{: #analyze_discover}

Dans la page Discover, vous pouvez définir de nouvelles requêtes de recherche et appliquer des filtres par requête. Les données de journal sont affichées via un tableau et un histogramme. Vous pouvez utiliser ces visualisations pour analyser les données de manière interactive. Pour plus d'informations, voir [Analyses des données en mode interactif dans Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#analize_logs_interactively).

Vous pouvez configurer des filtres depuis les zones du journal, par exemple message_type (type de message) et instance_ID (ID d'instance), et définir une période de temps. Vous pouvez activer ou désactiver dynamiquement ces filtres. Le tableau et l'histogramme afficheront les entrées  de journal correspondant à la requête et aux critères de filtrage activés. Pour plus d'informations, voir [Filtrage des journaux dans Kibana](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs).

## Analyse des données via une visualisation
{: #analyze_visualize}
    
Dans la page Visualize, vous pouvez définir de nouvelles requêtes de recherche et visualisations. Vous pouvez également ouvrir les visualisations sauvegardées ou sauvegarder une
visualisation.

Pour analyser les données, vous pouvez créer des visualisations basées sur une recherche existante ou une nouvelle recherche. Kibana inclut différents types de visualisations (comme un tableau, des tendances et un histogramme) que vous pouvez utiliser pour analyser les informations. L'objectif de chaque visualisation varie. Certaines sont organisées en lignes qui affichent les résultats d'une ou de plusieurs requêtes. D'autres affichent des documents ou des informations personnalisées. Les données dans une visualisation peuvent être fixes ou changer si une requête de recherche est modifiée. Vous pouvez incorporer la visualisation dans une page Web ou la partager. 

Pour plus d'informations, voir [Analyse des journaux à l'aide de visualisations](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#kibana_visualizations).

## Analyse des données dans un tableau de bord
{: #analyze_dashboard}

Dans la page Dashboard, vous pouvez personnaliser, sauvegarder et partager simultanément plusieurs visualisations et recherches. 

Vous pouvez ajouter, retirer et réorganiser des visualisations dans le tableau de bord. Pour plus d'informations, voir [Analyse des journaux dans Kibana via un tableau de bord](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#analize_logs_dashboard).
    
Après avoir personnalisé un tableau de bord Kibana, vous pouvez analyser les données par le biais de ses visualisations et le sauvegarder pour une réutilisation future. Pour plus d'informations, voir [Sauvegarde d'un tableau de bord Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save).

## Personnalisation de Kibana
{: #analyze_management}

Vous pouvez également configurer et gérer les ressources Kibana depuis la page **Gestion**. 

Vous pouvez effectuer les tâches suivantes :

* Sauvegarder, supprimer, exporter et importer des recherches. 
* Sauvegarder, supprimer, exporter et importer des visualisations.
* Sauvegarder, supprimer, exporter et importer des tableaux de bord.
* [Actualiser la liste des zones.](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)

## Limitations
{: #limitations}

Dans Kibana, vous pouvez partager une visualisation ou un tableau de bord uniquement avec des membres de la même organisation ou du même compte.

Les fonctions Kibana suivantes ne sont pas prises en charge :

* Partage d'une recherche.
* Création de canevas d'index. 


## Rôles requis par un utilisateur pour afficher les journaux
{: #roles}

Dans {{site.data.keyword.Bluemix_notm}}, vous pouvez affecter un ou plusieurs rôles à des utilisateurs. Ces rôles définissent quelles tâches sont activées pour que cet utilisateur utilise le service {{site.data.keyword.loganalysisshort}}. 

Les tableaux suivants répertorient les rôles qu'un utilisateur doit avoir pour pouvoir afficher les journaux :

<table>
  <caption>Droits requis par un **propriétaire de compte** pour afficher les journaux</caption>
  <tr>
    <th>Action</th>
	<th>Rôles d'espace CF</th>
	<th>Rôles d'organisation CF</th>
	<th>Rôles IAM</th>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'espace</td>
	<td>*Responsable* </br>*Développeur* </br>*Auditeur*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Afficher les journaux dans le domaine de compte</td>
	<td></td>
	<td></td>
	<td>*Administrateur*</td>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'organisation</td>
	<td></td>
	<td>*Responsable* </br>*Responsable de la facturation*  </br>*Auditeur*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Droits requis par un **auditeur** pour afficher les journaux</caption>
  <tr>
    <th>Action</th>
	<th>Rôles d'espace CF</th>
	<th>Rôles d'organisation CF</th>
	<th>Rôles IAM</th>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'espace</td>
	<td>*Auditeur*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Afficher les journaux dans le domaine de compte</td>
	<td></td>
	<td></td>
	<td>*Afficheur*</td>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'organisation</td>
	<td></td>
	<td>*Auditeur*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Droits requis par un **administrateur** pour afficher les journaux</caption>
  <tr>
    <th>Action</th>
	<th>Rôles d'espace CF</th>
	<th>Rôles d'organisation CF</th>
	<th>Rôles IAM</th>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'espace</td>
	<td>*Développeur*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Afficher les journaux dans le domaine de compte</td>
	<td></td>
	<td></td>
	<td>*Afficheur*</td>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'organisation</td>
	<td></td>
	<td>*Responsable*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Droits requis par un **développeurs** pour afficher les journaux.</caption>
  <tr>
    <th>Action</th>
	<th>Rôles d'espace CF</th>
	<th>Rôles d'organisation CF</th>
	<th>Rôles IAM</th>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'espace</td>
	<td>*Développeur*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Afficher les journaux dans le domaine de compte</td>
	<td></td>
	<td></td>
	<td>*Afficheur*</td>
  </tr>
  <tr>
    <td>Afficher les journaux dans un domaine d'organisation</td>
	<td></td>
	<td>*Auditeur*</td>
	<td></td>
  </tr>
</table>



## URL d'ouverture de Kibana
{: #urls_kibana}

Le tableau suivant répertorie les URL permettant d'ouvrir Kibana ainsi que les versions de Kibana par région :

<table>
    <caption>URL d'ouverture de Kibana</caption>
    <tr>
      <th>Région</th>
      <th>URL</th>
      <th>Version Kibana</th>
    </tr>
	<tr>
      <td>Francfort</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>Sydney</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>Royaume-Uni</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
    <tr>
      <td>Sud des Etats-Unis</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
</table>




