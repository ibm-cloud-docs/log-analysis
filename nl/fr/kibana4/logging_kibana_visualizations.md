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

# Analyse de journaux dans Kibana à l'aide de visualisations 
{:#logging_kibana_visualizations}

Utilisez la page *Visualize* dans Kibana pour créer des visualisations (par exemple, des graphiques et des tableaux) que vous pourrez utiliser pour analyser vos données de journal et comparer les résultats. 
{:shortdesc}

Vous pouvez utiliser une visualisation individuellement pour analyser vos journaux. 

* Vous pouvez créer une visualisation depuis une recherche que vous avez définie et sauvegardée depuis la page *Discover* ou depuis une nouvelle requête que vous définissez sur la page *Visualize*. La recherche définit le sous-ensemble de données qu'affiche une visualisation.

* Le type de visualisation que vous sélectionnez détermine comment sont affichées les données pour leur analyse.

Le tableau suivant répertorie différents types de visualisation :

| Type de visualisation | Description |
|-----------------------|-------------|
| Area chart | Affiche sous forme graphique des données quantitatives. Permet de comparer deux jeux de données agrégées (ou plus). |
| Data table | Affiche des données brutes sous forme de tableau pour une agrégation composée. |
| Line chart | Affiche des données sur une base chronologique. Permet de comparer deux jeux de données (ou plus) agrégées sur une base chronologique. |
| Markdown widget | Affiche des informations sous forme de texte. |
| Metric | Affiche le nombre de hits, ou la moyenne exacte d'une zone numérique. |
| Pie chart | Affiche les différentes valeurs d'une zone. | 
| Vertical bar chart | Affiche des données à base chronologique et non chronologique. Permet de regrouper des données. |
{: caption="Tableau 1. Types de visualisation" caption-side="top"}

Sur la page Visualize, vous pouvez effectuer n'importe laquelle des tâches suivantes :

| Tâche | Informations sur la tâche |
|------|------------------|
| [Créer une nouvelle visualisation](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_k4_visualizations_create) | Vous pouvez créer une visualisation depuis une recherche que vous avez définie et sauvegardée depuis la page *Discover* ou depuis une nouvelle requête que vous définissez sur la page *Visualize*. |
| [Sauvegarder une visualisation](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_save) | Vous pouvez sauvegarder des visualisations pour les réutiliser plus tard. |
| [Charger une visualisation](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_reload) | Vous pouvez charger une visualisation pour mettre à jour ses données, la modifier ou analyser les données. |
| [Supprimer une visualisation](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_delete) | Vous pouvez supprimer les visualisations superflues. |
| [Exporter une visualisation](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_export) | Vous pouvez exporter une visualisation sous forme de fichier JSON.  |
| [Importer une visualisation](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_import) | Vous pouvez importer une visualisation depuis un fichier JSON.  |
| [Partager une visualisation](/docs/services/CloudLogAnalysis/kibana4?topic=cloudloganalysis-logging_kibana_visualizations#logging_kibana_visualizations_share) | Vous pouvez partager une visualisation via votre source HTML ou via le tableau de bord Kibana.  |
{: caption="Tableau 2. Tâches de gestion de visualisations" caption-side="top"}


## Création de visualisations depuis des requêtes dans Kibana
{:#logging_k4_visualizations_create}

Pour créer une visualisation depuis la page Visualize, procédez comme suit :

1. Lancez Kibana, puis sélectionnez la page **Visualize**.

2. Créez une nouvelle visualisation. Dans la barre d'outils cliquez sur le bouton **New Visualization** (Nouvelle visualisation) ![Nouvelle visualisation](images/k4_visualization_new_icon.jpg "Nouvelle visualisation").

3. Sélectionnez une visualisation.
    
4. Sélectionnez une source de recherche. Sélectionnez l'une des options suivantes :

    * Cliquez sur **From a new search** (Depuis une nouvelle recherche).
    * Cliquez sur **From a saved search** (Depuis une recherche sauvegardée). 
  
5. Configurez la requête.

    * Si vous sélectionnez **From a saved search**, sélectionnez une requête de recherche. La requête est utilisée pour extraire les données utilisées pour la visualisation. 

        Après que vous ayez sélectionné une recherche, le générateur de visualisation s'ouvre et charge les données pour la requête sélectionnée. Le message suivant s'affiche : *This visualization is linked to a saved search: your_search_name* (Cette visualisation est liée à une recherche sauvegardée : nom de la recherche). 
	
	**Remarque **: les modifications apportées à une recherche sauvegardée sont automatiquement reflétées dans la visualisation. Pour désactiver l'actualisation automatique avec vos modifications de la requête liée à cette visualisation, effectuez un double-clic sur le message *This visualization is linked to a saved search: your_search_name* 

    * Si vous avez sélectionné **From a new search**, définissez une nouvelle requête. La requête est utilisée pour définir le sous-ensemble de données extraites et utilisées par la visualisation.

6. Dans le générateur de visualisation, sélectionnez une agrégation de métriques pour l'axe des Y.

7. Dans le générateur de visualisation, sélectionnez un type d'intervalle. Sélectionnez ensuite une agrégation d'intervalle.
  
8. Ajoutez des sous-intervalles pour décomposer les données.

Pour plus d'informations sur Kibana, reportez-vous au manuel [Kibana User Guide ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}.

## Suppression d'une visualisation
{:#logging_kibana_visualizations_delete}

Pour supprimer une visualisation, procédez comme suit dans la page Settings (Paramètres) :

1. Dans la page Settings, sélectionnez l'onglet **Objects**.

2. Dans l'onglet **Visualizations**, sélectionnez les visualisations que vous désirez supprimer.

3. Cliquez sur **Delete**.


## Exportation d'une visualisation
{:#logging_kibana_visualizations_export}

Pour exporter une visualisation sous forme de fichier JSON, procédez comme suit dans la page Settings (paramètres) :

1. Dans la page Settings, sélectionnez l'onglet **Objects**.

2. Dans l'onglet **Visualizations**, sélectionnez la visualisation que vous désirez exporter.

3. Cliquez sur **Export**.

4. Sauvegardez le fichier.

## Importation d'une visualisation
{:#logging_kibana_visualizations_import}

Pour importer une visualisation depuis un fichier JSON, procédez comme suit dans la page Settings (paramètres) :

1. Dans la page Settings, sélectionnez l'onglet **Objects**.

2. Dans l'onglet **Visualizations**, sélectionnez **Import**.

3. Sélectionnez un fichier et cliquez sur **Open**.

La visualisation est ajouté à la liste des visualisations.


 
## Chargement d'une visualisation
{:#logging_kibana_visualizations_reload}

Pour charger une visualisation sauvegardée, procédez comme suit :

1. Dans la barre d'outil de la page Visualize, cliquez sur le bouton **Load Saved Visualization** (Charger une visualisation sauvegardée) ![Charger une visualisation sauvegardée](images/k4_visualization_open_icon.jpg "Charger une visualisation sauvegardée").

2. Sélectionnez la visualisation que vous désirez charger. 


## Sauvegarde d'une visualisation
{:#logging_kibana_visualizations_save}

Pour sauvegarder une visualisation sur la page Visualize, procédez comme suit :

1. Dans la barre d'outil de la page Visualize, cliquez sur le bouton **Save Visualization** (Sauvegarder une visualisation) ![Sauvegarder une visualisation](images/k4_visualization_save_icon.jpg "Sauvegarder une visualisation").

2. Indiquez un nom pour la visualisation.

3. Cliquez sur Save. 



## Partage d'une visualisation
{:#logging_kibana_visualizations_share}

Procédez comme suit pour partager une visualisation dans la page Visualize :

1. Dans la barre d'outils de la page Visualize, cliquez sur le bouton **Share Visualization** (Partager une visualisation) ![Partager une visualisation](images/k4_visualization_share_icon.jpg "Partager une visualisation ").

2. Sélectionnez l'une des options suivantes :

    * **Embed this visualization** (Incorporer la visualisation) : Sélectionnez cette option pour partager la visualisation via votre source HTML . 
    
        Cliquez sur le bouton Copy (Copier) ![Copier dans le presse-papiers](images/k4_copy_to_clipboard.jpg "Copier dans le presse-papiers") pour copier le code HTML que vous pouvez utiliser pour incorporer la visualisation dans votre source HTML. 
	
	**Remarque ** : pour voir la visualisation, les utilisateurs doivent pouvoir accéder à Kibana.
	
    * **Share a link** (Partager un lien) : Sélectionnez cette option pour partager la visualisation dans Kibana avec d'autres utilisateurs.



