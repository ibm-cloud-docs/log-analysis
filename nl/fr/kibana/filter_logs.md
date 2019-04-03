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

# Filtrage des journaux dans Kibana
{:#filter_logs}

Dans la page Discover, vous pouvez définir de nouvelles requêtes de recherche et appliquer des filtres pour circonscrire les informations affichées pour l'analyse.
{:shortdesc}

* Vous pouvez définir une ou plusieurs requêtes de recherche dans la barre de recherche de la page Discover. Une requête de recherche définit un sous-ensemble d'entrées de journal. Utilisez le langage d'interrogation Lucene pour définir une requête de recherche. 

* Vous pouvez ajouter des filtres depuis la section *Fields list* ou depuis les entrées de la table. Un filtre affine la sélection de données en incluant ou en excluant des informations. Vous pouvez activer ou désactiver un filtre, inverser l'opération de filtrage, basculer l'état du filtre ou le supprimer complètement. 

Lorsque vous définissez une nouvelle recherche, enregistrez-la pour pouvoir la réutiliser dans une requête future dans la page Discover ou pour créer des visualisations dans des tableaux de bord personnalisés. Pour plus d'informations, voir [Sauvegarde d'une recherche](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1).

Lorsque vous lancez une nouvelle recherche, l'histogramme, le tableau et la section Fields list sont mis à jour automatiquement en affichant les résultats de la recherche. Pour déterminer quelles données sont affichées, voir [Identification des données affichées dans la page Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

La liste suivante décrit des scénarios de filtrage des données de vos journaux :

* Vous pouvez créer des recherches personnalisées pour filtrer vos journaux. Pour plus d'informations, voir [Filtrage de journaux en définissant des requêtes personnalisées](/docs/services/CloudLogAnalysis/kibana/define_search.html#define_search).

* Vous pouvez rechercher dans vos journaux des entrées contenant un texte spécifique dans la valeur d'une zone. Pour plus d'informations, voir [Filtrage de vos journaux d'après un texte spécifique dans la valeur d'une zone](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs_spec_text).
 
* Vous pouvez rechercher dans votre journal une valeur de zone spécifique ou exclure les entrées de journal contenant une valeur de zone spécifique. Pour plus d'informations, voir [Filtrage de vos journaux d'après une valeur de zone spécifique](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs_spec_field).
 
* Vous pouvez filtrer vos journaux afin d'afficher les entrées correspondant à une période donnée. Pour plus d'informations, voir [Définition d'un filtre temporel](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter).
     

## Ajout d'un filtre pour une valeur non répertoriée dans la section *Fields list*
{:#add_filter_out_value}

Pour ajouter un filtre pour une valeur ne figurant pas dans la section *Field list*, recherchez par le biais d'une requête les enregistrements contenant cette valeur. Ajoutez ensuite le filtre depuis l'entrée de table figurant dans la page Discover. 

Pour ajouter un filtre pour une valeur ne figurant pas dans la section *Fields list*, procédez comme suit :

1. Examinez la page Discover de Kibana pour identifier le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir  [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Dans la page Discover, modifiez la requête afin de rechercher une valeur de zone spécifique.

    Par exemple, pour rechercher l'instance *3*, la requête à saisir serait la suivante :
   `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:"3"`
    
    Dans le tableau, vous pouvez voir les enregistrements éventuels correspondant à votre requête. 
    
 3. Développez un enregistrement et sélectionnez la loupe ![Loupe en mode inclusif](images/include_field_icon.jpg "Loupe en mode inclusif") afin d'ajouter un filtre.
     
4. Vérifiez que le filtre a été ajouté.

   


## Filtrage de vos journaux d'après une valeur de zone spécifique
{:#filter_logs_spec_field}

Vous pouvez rechercher des entrées contenant une valeur de zone spécifique. 

Pour rechercher des entrées contenant une valeur de zone spécifique, procédez comme suit :

1. Examinez la page Discover de Kibana pour identifier le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir  [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Dans la zone *Field List*, identifiez celle pour laquelle vous voulez définir un filtre et cliquez dessus.

    5 valeurs au maximum sont affichées pour la zone. Chaque valeur comporte deux boutons en forme de loupe. 
    
    Si vous ne voyez pas la valeur recherchée, voir [Ajout d'un filtre pour une valeur non répertoriée dans la liste des zones](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#add_filter_out_value).

3. Pour ajouter un filtre recherchant des entrées avec une valeur de zone, sélectionnez la loupe avec un signe plus ![Loupe en mode inclusif](images/include_field_icon.jpg "Bouton en forme de loupe en mode inclusif") pour cette valeur.

    Pour ajouter un filtre recherchant des entrées n'incluant pas la valeur de zone, sélectionnez la loupe avec un signe moins ![Loupe en mode exclusif](images/exclude_field_icon.jpg "Bouton en forme de loupe en mode exclusif") pour cette valeur.

4. Choisissez l'une des options suivantes pour utiliser des filtres dans Kibana :

    <table>
      <caption>Tableau 1. Méthodes de gestion de filtres</caption>
      <tbody>
        <tr>
          <th align="center">Option</th>
          <th align="center">Description</th>
          <th align="center">Autres informations</th>
        </tr>
        <tr>
          <td align="left">Enable</td>
          <td align="left">Sélectionnez cette option pour activer un filtre.</td>
          <td align="left">Lorsque vous ajoutez un filtre, il est automatiquement activé. <br> Si un filtre est désactivé, cliquez dessus pour l'activer.</td>
        </tr>
        <tr>
          <td align="left">Disable</td>
          <td align="left">Sélectionnez cette option pour désactiver un filtre.</td>
          <td align="left">Après avoir ajouté un filtre, si vous voulez masquer les entrées correspondant à une valeur de zone, cliquez sur **disable**.</td>
        </tr>
        <tr>
          <td align="left">Pin</td>
          <td align="left">Sélectionnez cette option pour reproduire le filtre sur les pages Kibana.</td>
          <td align="left">Vous pouvez épingler un filtre dans la page *Discover*, la page *Visualize*, ou la page *Dashboard*.</td>
        </tr>
        <tr>
          <td align="left">Toggle</td>
          <td align="left">Sélectionnez cette option pour basculer l'opération du filtre.</td>
          <td align="left">Par défaut, les entrées correspondant à un filtre sont affichées. Pour afficher les entrées ne correspondant pas, basculez l'opération du filtre.</td>
        </tr>
        <tr>
          <td align="left">Remove</td>
          <td align="left">Sélectionnez cette option pour supprimer un filtre.</td>
          <td align="left"></td>
        </tr>
      </tbody>
    </table>

	
## Filtrage de vos applications CF par source
{:#filter_logs_by_source}

Pour rechercher des entrées de journal se rapportant à une source de journal spécifique, procédez comme suit :

1. Examinez la page Discover de Kibana pour identifier le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir  [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Dans la section *Field List*, sélectionnez la zone **source_id**.

3. Pour ajouter un filtre recherchant des entrées incluant une valeur source_id spécifique, sélectionnez la loupe ![Bouton Loupe en mode inclusif](images/include_field_icon.jpg "Bouton Loupe en mode inclusif") en regard de cette valeur.

    Pour consulter la liste des sources de journal disponibles pour les applications CF, voir [Sources de journal pour les applications CF](/docs/services/CloudLogAnalysis/cfapps/logging_cf_apps.html#logging_bluemix_cf_apps_log_sources).

    Pour ajouter un filtre recherchant des entrées n'incluant pas un élément source_id spécifique, sélectionnez la loupe ![Loupe en mode exclusif](images/exclude_field_icon.jpg "Loupe en mode exclusif") en regard de cette valeur.
    


## Filtrage de vos journaux par type de journal
{:#filter_logs_by_log_type}

Pour rechercher des entrées incluant un type de journal spécifique, procédez comme suit :

1. Examinez la page Discover de Kibana pour identifier le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir  [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Dans la section *Field List*, sélectionnez la zone **type**.

3. Pour ajouter un filtre recherchant un type de journal spécifique, sélectionnez la loupe ![Loupe en mode inclusif](images/include_field_icon.jpg "Loupe en mode inclusif") associée au type de journal à analyser.

    Pour ajouter un filtre recherchant des entrées n'incluant pas un type de journal spécifique, sélectionnez la loupe ![Loupe en mode exclusif](images/exclude_field_icon.jpg "Loupe en mode exclusif") en regard de la valeur concernée.



## Filtrage de vos journaux par ID d'instance
{:#filter_logs_by_instance_id}

Pour afficher et filtrer vos journaux par ID d'instance dans le tableau de bord Kibana, procédez comme suit :

1. Examinez la page Discover de Kibana pour identifier le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir  [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Dans la liste des zones (*Field List*), sélectionnez l'une des zones suivantes pour rechercher un ID d'instance spécifique :

    * **instance_ID** : Cette zone répertorie les différents ID d'instance disponibles dans le journal pour une application Cloud Foundry. 
    * **instance** : Cette zone répertorie les différents identificateurs globaux uniques (GUID) de toutes les instances d'un groupe de conteneurs. 
	* **docker.container_id_str** : Cette zone répertorie les différents ID des conteneurs déployés dans une infrastructure Kubernetes.
   
3. Pour ajouter un filtre recherchant un type de journal spécifique, sélectionnez la loupe ![Loupe en mode inclusif](images/include_field_icon.jpg "Loupe en mode inclusif") associée au type de journal à analyser.

    Pour ajouter un filtre afin de rechercher des entrées n'incluant pas un ID d'instance spécifique, sélectionnez la loupe ![Loupe en mode exclusif](images/exclude_field_icon.jpg "Loupe en mode exclusif") en regard de cette valeur.



## Filtrage de vos journaux d'application CF par type de message
{:#filter_cf_logs_by_msg_type}

Pour rechercher des entrées incluant un type de message spécifique, procédez comme suit :

1. Examinez la page Discover de Kibana pour identifier le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir  [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Dans la section *Field List*, sélectionnez la zone **message_type**.

    Les types de zones disponibles s'affichent. 

3. Pour ajouter un filtre recherchant des entrées incluant un *message_type* spécifique, sélectionnez la loupe ![Loupe en mode inclusif](images/include_field_icon.jpg "Loupe en mode inclusif") en regard de cette valeur.

    Pour ajouter un filtre recherchant des entrées n'incluant pas un élément *message_type* spécifique, sélectionnez la loupe ![Loupe en mode exclusif](images/exclude_field_icon.jpg "Loupe en mode exclusif") en regard de cette valeur.
    
 
	

## Filtrage de vos journaux d'après un texte spécifique dans la valeur d'une zone
{:#filter_logs_spec_text}

Vous pouvez afficher et rechercher des entrées incluant un texte spécifique dans la valeur d'une zone. 

**Remarque :** vous ne pouvez effectuer une recherche de texte libre que dans des zones de chaîne analysées par l'analyseur Elasticsearch. 
    
Lorsque Elasticsearch analyse la valeur d'une zone de type chaîne, il décompose le texte d'après les limites de mot définies par l'organisme Unicode Consortium, supprime la ponctuation et convertit en minuscules tous les mots.
    
Pour rechercher des entrées contenant un texte spécifique dans une valeur de zone, procédez comme suit :

1. Examinez la page Discover de Kibana pour identifier le sous-ensemble de données qu'elle affiche. Pour plus d'informations, voir  [Identification des données affichées dans votre page Kibana Discover](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data).

2. Identifiez les zones analysées par défaut dans ElasticSearch.

    Pour afficher la liste complète des zones analysées qui sont disponibles pour recherche et filtrage des données de journal, [rechargez la liste des zones](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields). Ensuite, dans la liste des zones (*Fields list*) disponibles dans la page Discover, procédez comme suit :
    
    1. Cliquez sur l'icône Configurer ![Icône Configurer](images/configure_icon.jpg "Icône Configurer"). La section **Selected fields** est affichée et vous permet de filtrer les zones.

    2. Pour identifier les zones analysées, sélectionnez **Yes** pour la zone de recherche **Analyzed**.

        La liste des zones analysées s'affiche.
    
    3. Vérifiez si la zone dans laquelle vous voulez effectuer une recherche en texte libre est une zone analysée par défaut par ElasticSearch.
    
3. S'il s'agit d'une zone analysée, modifiez la requête afin de rechercher des entrées dans les journaux incluant ce texte libre dans la valeur d'une zone.

    
**Exemple**

Supposons que vous lancez Kibana pour une application Cloud Foundry (CF) depuis l'interface utilisateur {{site.data.keyword.Bluemix}} et voulez rechercher un message spécifique comportant l'ID de message *CWWKT0016I:*, modifiez la recherche en incluant le texte libre.
    
1. Examinez la requête de recherche chargée et les données affichées dans la page Discover.
       
2. Pour rechercher l'ID de message *CWWKT0016I*, modifiez la requête de recherche dans la **barre de recherche**, puis cliquez sur **Enter**.
    
    Par exemple, entrez le texte suivant dans la barre de recherche pour une application CF avec l'ID *f52f6016-3aab-4b5c-aa2e-5493747cb978* :

	`<pre class="pre">application_id:f52f6016-3aab-4b5c-aa2e-5493747cb978 AND message:"CWWKT0016I:" </pre>`
        
          
Le tableau affiche les entrées pour votre application CF où le texte *CWWKT0016I* fait partie de la valeur de la zone *message*.
    
 	
        

## Définition d'un filtre temporel
{: #set_time_filter}

Affichez et filtrez les journaux pour une période spécifique en configurant le *sélecteur de période*.

Vous pouvez configurer le *sélecteur de période* dans la page Discover. Par défaut, il est configuré sur les 15 dernières minutes. 

Pour rechercher des entrées couvrant une date/heure spécifique, procédez comme suit :

1. Dans la barre de menu de la page Discover, cliquez sur le sélecteur de période ![Sélecteur de période](images/time_picker_icon.jpg "Sélecteur de période").

2. Configurez l'intervalle de temps. 

    Vous pouvez définir l'un des types suivants d'intervalle de temps :
    
    * Quick : Intervalles de temps prédéfinis incluant les utilisations les plus courantes d'intervalle de temps relatif et absolu. Par exemple, *Today* et *This Month*. 
       
    * Relative : Intervalles de temps vous permettant de spécifier la date et heure de début et la date et heure de fin. Vous pouvez arrondir sur l'heure la plus proche.
    
    * Absolute : Intervalles de temps entre une date de début et une date de fin.
    

Après avoir configuré un intervalle de temps, les données affichées dans Kibana correspondent aux entrées sur la période concernée.








