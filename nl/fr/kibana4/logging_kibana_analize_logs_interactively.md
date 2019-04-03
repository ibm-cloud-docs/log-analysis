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

# Analyse interactive de journaux dans Kibana
{:#kibana_analize_logs_interactively}

Dans la page Discover, vous pouvez afficher et analyser vos journaux {{site.data.keyword.Bluemix}} de façon interactive. Vous pouvez définir des requêtes de recherche pour filtrer ces données à l'aide du langage d'interrogation Lucene. Pour chaque requête de recherche, vous pouvez appliquer des filtres afin d'affiner les entrées disponibles pour l'analyse. Vous pouvez sauvegarder une recherche pour la réutiliser plus tard.
{:shortdesc}

Par défaut, dans {{site.data.keyword.Bluemix_notm}}, le jeu de données affiché dans la page Discover lorsque vous lancez Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}} est configurée pour n'afficher que les entrées de l'application ou du conteneur CF (Cloud Foundry) depuis lequel vous avez lancé Kibana. 

Le tableau suivant décrit la requête par défaut par ressource lorsque vous lancez Kibana depuis {{site.data.keyword.Bluemix_notm}} :

| Ressource | Requête de recherche Kibana par défaut |
|---------------|---------------|
| Application CF   | `application_id:<app_GUID>`    |
| Conteneur Docker unique | `instance:<instance_GUID>`    |
| Groupe de conteneurs avec 2 instances | `instance:<instance_GUID> OU instance:<instance_GUID>` |
{: caption="Tableau 1. Requête de recherches par défaut" caption-side="top"}

**Remarque :** 
* A chaque fois que vous lancez Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}}, les données affichées correspondent à la requête prédéfinie par défaut et se basent sur le canevas d'index.
* 500 entrées au maximum (correspondant aux plus récentes) sont affichées dans la page Discover. Vous pouvez modifier cette valeur dans la page Settings.

Lorsque vous lancez Kibana depuis un navigateur, les données affichées dans la page Discover correspondent aux données de journal disponibles dans l'espace auquel vous êtes connecté. La page n'est pas limitée à des conteneurs ou à des applications spécifiques.

La page Discover inclut un histogramme et un tableau que vous pouvez personnaliser pour analyser interactivement les données. 

Vous pouvez effectuez les tâches suivantes pour personnaliser le tableau de la page Discover :

| Tâche | Description | 
|------|-------------|
| [Ajouter une colonne de zone](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_add_fields_to_table) | Ajout de zones pour affichage de données spécifiques requises pour l'analyse au lieu du message intégral. |
| [Réorganiser une colonne de zone](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_rearrange_fields_in_table) | Déplacement de la position d'une zone vers celle voulue. |
| [Afficher une entrée](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_view_entry_in_table) | Développement d'une entrée du tableau pour afficher ses informations détaillées analysées par zone ou en tant qu'objet JSON. |
| [Supprimer une colonne de zone](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_remove_fields_from_table) | Suppression d'une zone superflue de la vue pour analyse. |
| [Classer les entrées par valeur d'une zone indexée](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_sort_by_table) | Réorganisation des entrées pour faciliter l'analyse. |
| [Actualiser les données automatiquement](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_view_refresh_interval) | Actualisation des données affichées dans le tableau avec les entrées les plus récentes. Par défaut, l'actualisation est en mode **OFF** (désactivée). |
{: caption="Tableau 2. Tâches de personnalisation d'un tableau" caption-side="top"}

<br>

La figure suivante illustre un exemple de tableau dans la page Discover :

![Page Discover dans Kibana](images/k4_discover_page.jpg "Page Discover dans Kibana")

Vous pouvez définir d'autres recherches. Lorsque vous définissez une nouvelle recherche, les données affichées dans l'histogramme et le tableau sont automatiquement mises à jour.

Pour définir une nouvelle recherche, utilisez comme point de départ la requête de recherche par défaut, puis affinez-la comme suit :

* Appliquez des filtres de zone pour épurer l'ensemble de données affichées. Vous pouvez sélectionner/désélectionner chaque filtre, l'épingler à la page, l'activer ou le désactiver en fonction de vos besoins, et le configurer afin d'inclure ou d'exclure la valeur. 

    **Astuce :** si vous ne localisez pas dans la section *Fields list* une zone que vous vous attendiez à rencontrer, ou que des loupes en regard de zones répertoriées sont désactivées dans la page Discover, rechargez cette liste en actualisant le canevas d'index dans la page Settings. 

    Par exemple, si votre application CF comporte plusieurs instances, vous pouvez décider d'analyser les données d'une instance spécifique. Vous pouvez définir un filtre de zone restreignant les données à celles que vous voulez analyser. 
    
* Personnalisez la zone *Time Picker* pour des données temporelles. Vous pouvez définir pour une requête une plage de temps absolue, relative, ou la sélectionner depuis un ensemble de valeurs prédéfinies. 

Après avoir configuré la recherche définissant le sous-ensemble de données à analyser, vous pouvez la sauvegarder pour une utilisation ultérieure.

Vous pouvez effectuer les tâches suivantes avec des recherches que vous avez définies dans la page Discover :

| Tâche | Description |
|------|-------------|
| Sauvegarde d'une recherche | Sauvegarde de votre recherche pour une utilisation ultérieure.  |
| Suppression d'une recherche | Suppression d'une recherche devenue superflue. |
| Exportation d'une recherche | Exportation d'une recherche pour son partage.  |
| Rechargement d'une recherche  | Téléchargement d'une recherche existante pour nouvelle analyse d'un jeu de données. |
| Actualisation des données d'une recherche | Configuration d'une actualisation automatique des données affichées au cours de la recherche.  |
| Importation d'une recherche | Importation d'une recherche.  |
{: caption="Tableau 3. Tâches de gestion de recherches" caption-side="top"}

<br>

Vous pouvez également examiner des statistiques dans la page Discover :
* Statistiques par zone. 
* Statistiques dans l'histogramme selon l'horodatage (`@timestamp`) configuré.

Pour plus d'informations, voir [Affichage des statistiques sur les données de zone](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_interactively.html#kibana_discover_view_fields_stats).

**Remarque :** les données affichées dans le tableau et l'histogramme sont statiques. Pour pouvoir afficher les plus récentes, vous devez définir un intervalle d'actualisation. 


## Ajout de colonnes de zone au tableau
{: #kibana_discover_add_fields_to_table}

Le tableau disponible pour l'analyse des données dans la page Discover inclut les zones suivantes par défaut :
* **time:** cette zone indique quand l'entrée a été capturée et enregistrée dans {{site.data.keyword.Bluemix_notm}}.
* **_source:** cette zone contient les données d'origine de l'entrée.

Vous pouvez ajouter une colonne de zone au tableau en sélectionnant l'une des options suivantes :

* Ajout d'une colonne de zone depuis la liste Field (Zone) disponible dans la page.

    1. Dans la page Discover, identifiez la zone dans la section `Selected Fields`.
    2. Survolez une zone dans la liste Fields.
    
        ![Ajout de zone depuis la vue de table](images/k4_add_field_column_hover.jpg "Ajout de zone depuis la vue de table")
    
    3. Pour ajouter une zone, cliquez sur **Add**.
    
 * Ajout d'une colonne de zone depuis la vue de table d'une entrée développée.

    1. Développez une entrée dans le tableau.
    2. Dans la vue Table, identifiez la zone à ajouter.
    
        ![Ajout de zone depuis la vue de table](images/k4_add_field_column.jpg "Ajout de zone depuis la vue de table")
    
    3. Cliquez sur l'icône **Toggle Column in table** ![Toggle column in table](images/k4_toggle_field_icon.jpg).
    

**Remarque :** lorsque vous ajoutez une colonne de zone au tableau pour la première fois, la colonne de zone *_source* qui est affichée dans le
tableau est masquée. La zone *_source* affiche la valeur de chaque zone pour chaque entrée de journal. Pour afficher d'autres valeurs de zone pour une entrée de journal après avoir ajouté une colonne à la table, reportez-vous à l'onglet de vue table ou à l'onglet JSON de chaque entrée.

Par exemple, si vous ajoutez la zone *application_id* à la table, celle-ci est modifiée comme suit :

![Vue table après l'ajout d'une nouvelle zone](images/k4_add_field_filter_new_table_look.jpg "Vue table après l'ajout d'une nouvelle zone")


## Actualisation automatique des données
{: #kibana_discover_view_refresh_interval}

Par défaut, dans {{site.data.keyword.Bluemix_notm}}, la période d'*actualisation automatique* est **désactivée** et les données visibles dans Kibana correspondent aux 15 dernières minutes après le lancement de Kibana. Ces 15 minutes correspondent au filtre temporel préconfiguré. Vous pouvez le modifier en stipulant une plage de temps différente. 

Procédez comme suit pour définir une période d'*actualisation automatique* :

1. Dans la barre de menus de la page Discover, cliquez sur le sélecteur de période ![Sélecteur de période](images/k4_time_picker_icon.jpg "Sélecteur de période").

2. Sélectionnez le bouton d'actualisation automatique ![Bouton d'actualisation automatique](images/k4_auto_refresh_icon.jpg "Bouton d'actualisation automatique").

3. Sélectionner un intervalle d'actualisation.

    ![Options pour définition d'un intervalle d'actualisation](images/k4_change_autorefresh.jpg "Options pour définition d'un intervalle d'actualisation")


Vous pouvez interrompre l'intervalle d'actualisation en cliquant sur le bouton Pause ![Bouton Pause](images/k4_auto_refresh_pause_icon.jpg "Pause") 


## Identification des données affichées dans la page Discover
{: #k4_identify_data}

Lorsque vous utilisez Kibana pour analyser les journaux {{site.data.keyword.Bluemix_notm}}, les données présentées dépendent de la manière dont vous avez lancé Kibana, du canevas d'index configuré, ainsi que de la requête et des filtres personnalisés qui sont appliqués.

Prenez en compte les informations suivantes pour identifier les données disponibles dans le tableau et l'histogramme de la page Discover :

1. Vérifiez le canevas d'index dans la page Settings.

    Le canevas d'index définit la requête de recherche appliquée par défaut pour afficher les entrées sur vos pages Kibana. Par défaut, il est préconfiguré et permet d'afficher toutes les données disponibles dans un espace. Exemple :

    * Si vous lancez Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}}, à savoir depuis la section *Journal* des pages de l'interface utilisateur d'une ressource spécifique comme une application  ou un conteneur d'application Cloud Foundry (CF), le canevas d'index appliqué inclut toutes les entrées disponibles dans l'espace.
    
    * Si vous lancez Kibana depuis un navigateur, le canevas d'index appliqué inclut toutes les entrées disponibles dans l'espace où Kibana indique que vous vous êtes connecté.
        
2. Vérifiez la requête dans la page Discover.  

    La requête affichée dans la page Discover est utilisée pour filtrer les entrées disponibles par défaut pour l'analyse. Exemple :

    * Si vous entrez une chaîne dans la barre de recherche, la chaîne est recherchée dans toutes les zones.
    
    * Si la requête est définie sur `application_id:<GUID>` où *GUID* est l'ID d'une application CF, les entrées qui s'affichent correspondent à toutes
les entrées disponibles pour cette application CF dans l'espace qui est configuré dans le canevas d'index.
    
    * Si la requête est définie sur `instance_id:<GUID>` où *GUID* est l'ID d'une instance de conteneur, les entrées qui s'affichent correspondent à
toutes les entrées disponibles pour ce conteneur dans l'espace configuré dans le canevas d'index.
    
    * Si la requête est définie sur `instance_id:<GUID> AND instance_id:<GUID>` où *GUID* est l'ID d'une instance de conteneur, les entrées qui s'affichent correspondent à toutes les entrées disponibles pour ce groupe de conteneurs dans l'espace qui est configuré dans le canevas d'index.
   
    * Si la requête est définie sur `*`, les données correspondent à toutes les entrées disponibles dans l'espace configuré dans le canevas d'index.
    
    * Si la requête est définie sur `application_id:<GUID> AND message:"MY_search_text"` où *GUID* est l'ID d'une application CF
et *My_search_text* est la chaîne à rechercher, les entrées qui s'affichent correspondent à toutes les entrées qui incluent *My_search_text*
dans la zone de message pour ces entrées d'application CF qui sont disponibles dans l'espace configuré dans le canevas d'index.
    
3. Vérifiez les filtres de zone appliqués à votre requête dans la page Discover.

    Vous pouvez ne définir aucun filtre de zone, ou au contraire en définir plusieurs pour passer d'une entrée à l'autre en fonction de la valeur de la zone. Par exemple, si un filtre de zone est activé, les entrées qui s'affichent correspondent à celles pour lesquelles la valeur de cette zone correspond.
    

## Tri des entrées en fonction de la valeur d'une zone indexée 
{: #kibana_discover_sort_by_table}

Vous ne pouvez trier les entrées de la table que pour les zones qui ont été indexées.

Pour identifier les zones indexées, procédez comme suit :

1. Dans la page Discover, cliquez sur l'icône de configuration ![Icône Configurer](images/k4_configure_icon.jpg "Icône Configurer"). La section où vous pouvez filtrer des zones dans la section **Selected fields** (Zones sélectionnées) de la page est affichée.

    ![Section de la configuration affichant des zones avec des attributs spécifiques](images/k4_reset_filters.jpg "Section de la configuration affichant des zones avec des attributs spécifiques")
    
2. Pour identifier les zones indexées, sélectionnez **Yes** pour la zone de recherche **Indexed**.

    ![Attribut Indexé](images/k4_reset_filters_indexed_options.jpg "Attribut Indexé")
    
 La liste des zones indexées est affichée.
 
 ![Liste des zones indexées](images/k4_list_indexed_fields.jpg "Liste des zones indexées")
  	
 
Pour trier les entrées d'une table en fonction des valeurs d'une zone indexée, procédez comme suit : 

1. Survolez dans la table le nom de la zone en fonction de laquelle trier les données. Les différents boutons d'action apparaissent.
2. Cliquez sur le bouton de tri de la zone en fonction de laquelle trier les données. Cliquez une seconde fois sur le bouton de tri si vous voulez inverser l'ordre de tri.

**Remarque :** lorsque vous effectuez un tri en fonction d'une zone d'heure, les entrées sont triées par défaut par ordre chronologique inverse. Les entrées les plus récentes figurent en premier.


## Réorganisation des colonnes de zone dans la table
{: #kibana_discover_rearrange_fields_in_table}

Vous pouvez réorganiser les colonnes de zone dans la table. Survolez l'en-tête de la colonne à déplacer avec votre souris et cliquez sur le bouton **Move column to the left** (Déplacer la colonne vers la gauche) ou sur le bouton **Move column to the right**.
<br>
![Déplacement d'une zone dans la table](images/k4_add_field_filter_new_table_look.jpg "Déplacement d'une zone dans la table")


## Rechargement de la liste des zones
{: #kibana_discover_view_reload_fields}

Pour recharger la liste des zones affichées dans Kibana, procédez comme suit :

1. Sélectionnez la page Settings.

    Lorsque vous sélectionnez la page Settings, l'onglet *Indices* s'ouvre.
   
2. Sélectionnez le canevas d'index afin de visualiser chaque zone et le type principal associé à la zone comme enregistré par Elasticsearch. 

3. Cliquez sur le bouton *Reload field list* ![Recharger la liste des zones](images/k4_reload_field_list_icon.jpg "Recharger la liste des zones") afin de recharger les zones du canevas d'index. 

La liste des zones est actualisée.


## Suppression de colonnes de zone dans la table
{: #kibana_discover_remove_fields_from_table}

Pour supprimer des zones de la table, procédez comme suit :

1. Dans la table, identifiez la zone à supprimer de la vue Table.
2. Cliquez sur **Remove column**.
    
    ![Suppression d'une zone dans la vue table](images/k4_remove_field_column.jpg "Suppression d'une zone dans la vue table")


## Affichage d'une entrée dans la table
{: #kibana_discover_view_entry_in_table}

Pour afficher les données d'une entrée dans la table, cliquez sur le bouton de développement ![Icône de bouton de développement](images/k4_expand_icon.jpg "Icône de bouton de développement") de l'entrée à analyser. 

![Table dans la page Discover dans Kibana](images/k4_table_discover.jpg "Table dans la page Discover dans Kibana") 	

Sélectionnez ensuite l'une des options suivantes pour afficher les données :

* Pour afficher les données au format table, cliquez sur **Table**. La valeur de chaque zone disponible pour l'analyse est affichée dans un tableau. Pour chaque zone, vous disposez aussi de boutons de filtrage et d'un bouton de basculement.
* Pour afficher les données au format Json, cliquez sur **JSON**.

## Affichage des statistiques des données de zone
{: #kibana_discover_view_fields_stats}

Dans la page Discover, vous pouvez consulter des statistiques sur chaque zone de la section *Fields list* et dans l'*histogramme*. 

Les informations suivantes figurent dans la liste des zones :
* Nombre d'entrées dans la table qui contiennent une zone spécifique.
* 5 valeurs les plus élevées.
* Pourcentage des entrées contenant chaque valeur.

Les informations suivantes figurent dans l'histogramme :
* Nombre d'entrées sur un intervalle de temps.

Afin d'examiner les statistiques dans l'histogramme, cliquez sur un horodatage pour consulter les statistiques sur cette période. Exemple : 

![Affichage des statistiques sur une zone dans l'histogramme](images/k4_see_stats_on_histogram.jpg "Affichage des statistiques sur une zone dans les histogrammes")
   	
 	
Pour examiner les statistiques sur une zone dans la liste des zones, cliquez sur le nom de la zone. Exemple :

![Affichage des statistiques sur une zone dans la liste Zones](images/k4_stats_field_list.jpg "Affichage des statistiques sur une zone dans la liste Zones")


