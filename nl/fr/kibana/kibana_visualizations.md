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
{:#kibana_visualizations}

Utilisez la page *Visualize* dans Kibana pour créer des visualisations (par exemple, des graphiques et des tableaux) que vous pourrez utiliser pour analyser vos données de journal et comparer les résultats. 
{:shortdesc}

Vous pouvez utiliser une visualisation individuellement pour analyser vos journaux. 

* Vous pouvez créer une visualisation depuis une recherche que vous avez définie et sauvegardée depuis la page *Discover* ou depuis une nouvelle requête que vous définissez dans la page *Visualize*. La recherche définit le sous-ensemble de données qu'affiche une visualisation.

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

Dans la page Visualize, vous pouvez effectuer n'importe laquelle des tâches suivantes :

| Tâche | Informations sur la tâche |
|------|------------------|
| [Créer une nouvelle visualisation](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#create) | Vous pouvez créer une visualisation depuis une recherche que vous avez définie et sauvegardée depuis la page *Discover* ou depuis une nouvelle requête que vous définissez dans la page *Visualize*. |
| [Supprimer une visualisation](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#delete) | Vous pouvez supprimer les visualisations superflues. |
| [Exporter une visualisation](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#export) | Vous pouvez exporter une visualisation sous forme de fichier JSON.  |
| [Importer une visualisation](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#import1) | Vous pouvez importer une visualisation depuis un fichier JSON.  |
| [Charger une visualisation](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#reload2) | Vous pouvez charger une visualisation pour mettre à jour ses données, la modifier ou analyser les données. |
| [Sauvegarder une visualisation](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#save2) | Vous pouvez sauvegarder des visualisations pour les réutiliser plus tard. |
{: caption="Tableau 2. Tâches de gestion de visualisations" caption-side="top"}


## Création de visualisations depuis des requêtes dans Kibana
{: #create}

Pour créer une visualisation depuis la page Visualize, procédez comme suit :

1. Lancez Kibana, puis sélectionnez la page **Visualize**.

2. Choisissez un type de visualisation, par exemple *table*.

3. Sélectionnez une visualisation sauvegardée auparavant en sélectionnant **Or, From a Saved Search** ou en sélectionnant un index dans la section **From a New Search, Select Index**.

4. Configurez la requête.

    * Si vous sélectionnez **Or, From a Saved Search**, sélectionnez une requête de recherche. La requête est utilisée pour extraire les données utilisées pour la visualisation. 
	
	    Après que vous ayez sélectionné une recherche, le générateur de visualisation s'ouvre et charge les données pour la requête sélectionnée. 
		
		**Remarque **: les modifications apportées à une recherche sauvegardée sont automatiquement reflétées dans la visualisation. Pour désactiver l'actualisation automatique avec vos modifications de la requête liée à cette visualisation, effectuez un double-clic sur le message *This visualization is linked to a saved search: your_search_name* 

    * Si vous sélectionnez **From a New Search, Select Index**, définissez une nouvelle requête. La requête est utilisée pour définir le sous-ensemble de données extraites et utilisées par la visualisation.

        Pour plus d'informations, voir [Filtrage de journaux en définissant des requêtes personnalisées](/docs/services/CloudLogAnalysis/kibana/define_search.html#define_search).

Pour plus d'informations sur Kibana, reportez-vous au manuel [Kibana User Guide ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Suppression d'une visualisation
{: #delete}

Pour supprimer une visualisation, effectuez les étapes suivantes dans la page **Management** :

1. Dans la page **Management**, sélectionnez **Saved Objects**.

2. Dans l'onglet **Visualizations**, sélectionnez les visualisations à supprimer.

3. Cliquez sur **Delete**.


## Exportation d'une visualisation
{: #export1}

Pour exporter une visualisation en tant que fichier JSON, effectuez les étapes suivantes dans la page **Management** :

1. Dans la page **Management**, sélectionnez **Saved Objects**.

2. Dans l'onglet **Visualizations**, sélectionnez la visualisation à exporter.

3. Cliquez sur **Export**.

4. Sauvegardez le fichier.

## Importation d'une visualisation
{: #import1}

Pour importer une visualisation en tant que fichier JSON, effectuez les étapes suivantes dans la page **Management** :

1. Dans la page **Management**, sélectionnez **Saved Objects**.

2. Dans l'onglet **Visualizations**, sélectionnez **Import**.

3. Sélectionnez un fichier et cliquez sur **Open**.

La visualisation est ajouté à la liste des visualisations.


 
## Chargement d'une visualisation
{: #reload2}

Pour charger une visualisation sauvegardée, procédez comme suit :

1. Dans la barre d'outils de la page Visualize, cliquez sur **Open**.

2. Sélectionnez la visualisation à charger. 


## Sauvegarde d'une visualisation
{: #save2}

Pour sauvegarder une visualisation dans la page Visualize, procédez comme suit :

1. Dans la barre d'outils de la page Visualize, cliquez sur **Save**.

2. Indiquez un nom pour la visualisation.

3. Cliquez sur Save. 


