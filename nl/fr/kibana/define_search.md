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

# Définition de requêtes de recherche personnalisées
{:#define_search}

Dans la barre de recherche de la page Discover, vous pouvez définir et enregistrer des requêtes de recherche en utilisant le langage de requête Lucene. Pour chaque recherche, vous pouvez appliquer des filtres afin d'affiner les entrées disponibles pour l'analyse.
{:shortdesc}

Pour définir une recherche personnalisée, procédez comme suit :

1. Lancez Kibana.

    Pour les applications Cloud Foundry (CF), voir [Accès à Kibana depuis le tableau de bord d'une application CF](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app).

	Pour les conteneurs qui s'exécutent dans l'infrastructure gérée par {{site.data.keyword.Bluemix_notm}}, voir [Accès à Kibana depuis le tableau de bord d'un conteneur](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers).
    
    Pour toutes les ressources de cloud, par exemple les conteneurs qui s'exécutent dans un cluster Kubernetes, voir [Accès à Kibana depuis le navigateur](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser). 
	
	Lorsque vous accédez à Kibana, la recherche par défaut est appliquée. Vous pouvez voir les journaux pour la liste d'instances de la ressource que vous interrogez. Vous pouvez filtrer les journaux pour une ressource {{site.data.keyword.Bluemix_notm}} spécifique ou pour toutes les ressources dans cet espace.

2. Examinez la page Discover pour déterminer le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data). Modifiez ensuite la recherche par défaut pour filtrer les entrées.

    **Remarque :** utilisez le langage Lucene pour définir votre requête par défaut. Pour plus d'informations, voir [Apache Lucene - Query Parser Syntax  ![Icône de lien externe](../../../icons/launch-glyph.svg "Icône de lien externe")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}
    
    Lorsque Kibana est lancé depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}}, pour modifier la requête et définir plusieurs critères de recherche, vous pouvez utiliser les termes logiques **AND** et **OR**. Ces opérateurs doivent être en majuscules.    
    
    * Pour rechercher un mot clé ou une partie d'un mot clé, entrez un mot suivi d'un astérisque (*), qui est un caractère générique ; par exemple, `Java*`. 
    * Pour rechercher une expression en particulier, entrez cette expression en prenant soin de la placer entre guillemets (" ") ; par exemple, `"Java/1.8.0"`.
    * Pour créer des recherches plus complexes, vous pouvez utiliser les termes logiques AND et OR ; par exemple, `"Java/1.8.0" OR "Java/1.7.0"`.
    * Pour rechercher une valeur dans une zone spécifique, entrez votre recherche au format suivant : *nom_zone_journal:terme_recherche* ; par exemple, `instance_id:"1"`.
    * Pour rechercher une plage de valeurs dans une zone de journal spécifique, entrez votre recherche au format suivant : *nom_zone_journal:[début_plage TO fin_plage]* ; par exemple, `instance_id:["1" TO "2"]`.

     Par exemple, pour une application CF, vous pouvez créer une requête `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]` qui ne répertorie que des entrées pour les instances *0* et *1*. 

3. Enregistrez la requête pour pouvoir la réutiliser ultérieurement. Pour plus d'informations, voir [Sauvegarde d'une recherche](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1). 

**Remarque :** si vous devez supprimer une requête, voir [Suppression d'une recherche](/docs/services/CloudLogAnalysis/kibana/define_search.html#delete_search).



## Suppression d'une recherche
{: #delete_search}

Pour supprimer une recherche, procédez comme suit dans la page Settings :

1. Dans la page Settings, sélectionnez l'onglet **Objects**.

2. Dans l'onglet **Searches**, sélectionnez la recherche à supprimer.

3. Cliquez sur **Delete**.


## Exportation d'une recherche
{: #export_search}

Pour exporter une recherche, procédez comme suit dans la page Settings :

1. Dans la page Settings, sélectionnez l'onglet **Objects**.

2. Dans l'onglet **Searches**, sélectionnez la recherche à exporter.

3. Cliquez sur **Export**.

4. Sauvegardez le fichier.

 
## Importation d'une recherche
{: #import_search}

Pour importer une recherche, procédez comme suit dans la page Settings :

1. Dans la page Settings, sélectionnez l'onglet **Objects**.

2. Dans l'onglet **Searches**, sélectionnez **Import**.

3. Sélectionnez un fichier et cliquez sur **Open**.

La recherche est ajoutée à la liste des recherches.

## Actualisation du contenu d'une recherche
{: #refresh_search}

Pour actualiser manuellement le contenu d'une recherche, vous pouvez cliquer sur l'icône représentant une loupe située dans la barre de recherche. 

Pour actualiser automatiquement les données affichées dans la page Discover, vous pouvez configurer un intervalle d'actualisation. La valeur actuelle de cet intervalle est affichée dans la barre de menu de la page Discover. Par défaut, l'actualisation automatique est définie à **OFF** (Désactivée).

Pour définir un intervalle d'actualisation, procédez comme suit :

1. Dans la page Discover, cliquez sur l'option **Time Filter** située dans la barre de menu.

2. Cliquez sur **Auto Refresh** ![Régénération automatique](images/auto_refresh_icon.jpg "Régénération automatique").

3. Sélectionnez dans la liste un intervalle d'actualisation. 

**Remarque **: après avoir activé un intervalle d'actualisation automatique, vous pouvez mettre en pause l'actualisation en cliquant sur le bouton Pause ![Pause](images/auto_refresh_pause_icon.jpg "Pause").


## Rechargement d'une recherche
{: #reload_search1}

Pour charger une recherche sauvegardée, procédez comme suit :

1. Dans la barre d'outils de la page Discover, cliquez sur le bouton **Load Search** ![Charger une recherche](images/load_icon.jpg "Charger une recherche").

2. Sélectionnez la recherche à charger. 

## Lancement d'une nouvelle recherche
{: #k4_new_search}

Pour lancer une nouvelle recherche, cliquez sur le bouton **New Search** ![Nouvelle recherche](images/new_search_icon.jpg "Nouvelle recherche") dans la barre d'outils de la page Discover.

## Sauvegarde d'une recherche 
{: #save_search1}

Tenez compte des informations suivantes concernant la sauvegarde des recherches personnalisées dans Kibana :

* Lorsque vous sauvegardez une recherche, la chaîne de requête de recherche et le canevas d'index sélectionné sont enregistrés.
* Lorsque vous ouvrez une recherche dans la page *Discover* et la modifiez, vous pouvez choisir de la sauvegarder avec le même nom ou de sauvegarder la recherche personnalisée modifiée sous un autre nom. Par défaut, le nom de recherche fourni est celui qui correspond à la recherche personnalisée que vous avez ouverte initialement.

    * Pour sauvegarder la recherche personnalisée modifiée avec le même nom, cliquez sur **Save**. Notez que la recherche personnalisée d'origine est écrasée. 
	
	* Pour sauvegarder la recherche personnalisée modifiée sous un autre nom, entrez un nouveau nom dans la zone **Save Search**, puis cliquez sur **Save**. 


Pour sauvegarder la recherche actuelle dans la page Discover, procédez comme suit :

1. Dans la barre d'outils de la page Discover, cliquez sur le bouton **Save Search** ![Sauvegarder la recherche](images/save_search_icon.jpg "Sauvegarder la recherche").

2. Entrez un nom pour la recherche.

    **Remarque :** lorsque vous cliquez sur **Save**, aucun avertissement concernant l'écrasement ne s'affiche ; par conséquent, si vous spécifiez un nom existant, la sauvegarde remplacera cette version sans vous en informer.

3. Cliquez sur **Save**. 
