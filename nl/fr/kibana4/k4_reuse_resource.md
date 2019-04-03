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

# Réutilisation des ressources Kibana pour l'analyse des journaux {{site.data.keyword.Bluemix_notm}}
{:#k4_reuse_resource}

Pour copier une recherche, une visualisation ou un tableau de bord depuis un espace {{site.data.keyword.Bluemix}} vers un autre espace, utilisez les fonctions d'exportation et d'importation disponible dans Kibana. Vous pouvez copier des ressources une par une ou exporter toutes les ressources dans Kibana.
{:shortdesc}

| Tâche | Description |
|------|-------------|
| [Copie d'une recherche](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_search) | Copie d'une recherche d'un espace vers un autre. |
| [Copie d'une visualisation](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_visualization) | Copie d'une visualisation d'un espace vers un autre |

Prenez en compte les scénarios suivants dans {{site.data.keyword.Bluemix_notm}} pour la réutilisation de recherches, de visualisations ou de tableaux de bord : 

* Copie d'une ressource depuis un espace vers un autre figurant dans une même organisation

    Par exemple, vous pouvez copier vos visualisations depuis votre espace de développement dans votre espace de mise en préproduction.
    
* Copie d'une ressource depuis un espace vers un autre figurant dans différentes organisations d'un même compte

    Par exemple, vous pouvez copier vos visualisations depuis un espace dans votre organisation de développement vers un espace dans votre organisation de mise en préproduction.

* Copie d'une ressource entre des espaces se trouvant dans une même organisation mais situés dans différentes régions publiques

    Par exemple, vous pouvez copier vos visualisations depuis un espace dans l'organisation A dans {{site.data.keyword.Bluemix_notm}} qui se trouve dans la région publique Sud des Etats-Unis vers l'organisation A dans la région publique Royaume-Uni.



## Copie d'une recherche
{:#k4_reuse_search}

Procédez comme suit pour copier une recherche entre des espaces dans {{site.data.keyword.Bluemix_notm}} :

1. Lancez Kibana pour l'espace dans lequel la recherche à copier est disponible. 

    * Lancez Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}} : le fichier de recherche JSON que vous pouvez exporter inclut les zones suivantes : *space ID* et *application ID* pour les applications Cloud Foundry (CF) ou *instance ID* pour les conteneurs. Pour plus d'informations, voir [Accès au tableau de bord Kibana depuis le tableau de bord {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_bluemix).
    
    * Lancez Kibana depuis un navigateur : le fichier de recherche JSON que vous pouvez exporter inclut la zone *ID d'espace*. Pour plus d'informations, voir [Accès au tableau de bord Kibana depuis un navigateur](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_browser1).

2. Dans la page *Paramètres*, sélectionnez **Objects**, puis l'onglet **Searches**. Ensuite, sélectionnez une recherche et copiez les informations suivantes :

    <table>
      <tbody>
        <tr>
          <th align="center">Zone de recherche</th>
          <th align="center">Description</th>
        </tr>
        <tr>
          <td align="left">group</td>
          <td align="left"> ID de l'espace où la recherche est appliquée à des données de filtre.</td>
        </tr>
        <tr>
          <td align="left">title</td>
          <td align="left">Nom de la recherche.</td>
        </tr>
        <tr>
          <td align="left">version</td>
          <td align="left">Version de la recherche.</td>
        </tr>
      </tbody>
    </table>
   
3. Exportez la recherche.

    1. Dans la page Settings, sélectionnez l'onglet **Objects**.
    2. Dans l'onglet **Searches**, sélectionnez la recherche à exporter.
    3. Cliquez sur **Export**.
    4. Sauvegardez le fichier JSON.

4. Dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}, passez dans l'espace dans lequel copier la recherche, puis vérifiez que l'application ou le conteneur CF est disponible et en cours d'exécution.
    
5. Lancez Kibana pour l'espace {{site.data.keyword.Bluemix_notm}} dans lequel importer la recherche, puis procurez-vous les informations suivantes :

    Depuis l'[interface utilisateur Bluemix](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_bluemix) :
    
    <table>
      <tbody>
        <tr>
          <th align="center">Zone de recherche</th>
          <th align="center">Description</th>
        </tr>
        <tr>
          <td align="left">ID d'espace</td>
          <td align="left"> <ol><li> Dans la page *Settings*, sélectionnez l'onglet *Indices*.</li> <br> <li>L'ID d'espace est imbriqué dans le canevas d'index. Le format du canevas d'index est le suivant : `[logstash-3d8d2eae-SpaceID-]YYYY.MM.DD` où *SpaceID* est l'ID d'espace. Copiez l'ID d'espace.</li></ol></td>
        </tr>
        <tr>
          <td align="left">ID d'application ou ID d'instance</td>
          <td align="left"><ul><li>Lorsque vous lancez Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}}, la page *Discover* s'ouvre par défaut. Récupérez l'ID d'application ou l'ID d'instance dans la barre de recherche de la page *Discover*, par exemple, `application_id:d88d1f16-e9d9-4623-bce7-0348c88f5133`.</li> <br> <li>Lorsque vous lancez kibana depuis un navigateur, sélectionnez l'élément application_id ou instance_id dans la liste de zones de la page Discover.</li></ul></td>
        </tr>
      </tbody>
    </table>

6. Modifiez le fichier de recherche JSON que vous avez exporté lors d'une étape précédente. Remplacez la valeur de l'ID d'application. 

    L'objet JSON suivant est un exemple de fichier JSON de recherche : 
 
    <pre class="pre">
    [
  {
    "_id": "52edf6e6-5386-4235-8fb8-598de3b80f41_Dev",
    "_type": "search",
    "_source": {
      "columns": [
        "application_id",
        "source_id",
        "instance_id"
      ],
      "description": "",
      "group": "52edf6e6-5386-4235-8fb8-598de3b80f41",
      "hits": 0,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"[logstash-52edf6e6-5386-4235-8fb8-598de3b80f41-]YYYY.MM.DD\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"application_id:4ae73dcd-1fc4-48f0-9dc7-425839040436\"}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647},\"filter\":[{\"meta\":{\"negate\":false,\"index\":\"[logstash-52edf6e6-5386-4235-8fb8-598de3b80f41-]YYYY.MM.DD\",\"key\":\"application_id\",\"value\":\"4ae73dcd-1fc4-48f0-9dc7-425839040436\",\"disabled\":false},\"query\":{\"match\":{\"application_id\":{\"query\":\"4ae73dcd-1fc4-48f0-9dc7-425839040436\",\"type\":\"phrase\"}}}}]}"
      },
      "sort": [
        "@timestamp",
        "desc"
      ],
      "title": "Dev",
      "version": 1
    }
  }
]
    </pre>
    
    Dans cet exemple de fichier JSON, vous pouvez modifier les variables suivantes avec les informations du nouvel espace : 
    
    * SPACEID : Remplacez cette variable par l'ID d'espace du nouvel espace.
    * NAME : Remplacez cette variable si vous souhaitez modifier le nom de la recherche dans le nouvel espace. Pour conserver le même nom, ne modifiez pas cette valeur.
    * APPID : Remplacez cette variable par la valeur application_id de l'application CF dans le nouvel espace ou l'ID d'instance du conteneur dans le nouvel espace.
    
   <pre class="pre">
   [
  {
    "_id": "SPACEID_NAME",
    "_type": "search",
    "_source": {
      "columns": [
        "application_id",
        "source_id",
        "instance_id"
      ],
      "description": "",
      "group": "SPACEID",
      "hits": 0,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"[logstash-SPACEID-]YYYY.MM.DD\",\"query\":{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"application_id:APPID\"}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647},\"filter\":[{\"meta\":{\"negate\":false,\"index\":\"[logstash-SPACEID-]YYYY.MM.DD\",\"key\":\"application_id\",\"value\":\"APPID\",\"disabled\":false},\"query\":{\"match\":{\"application_id\":{\"query\":\"APPID\",\"type\":\"phrase\"}}}}]}"
      },
      "sort": [
        "@timestamp",
        "desc"
      ],
      "title": "Dev",
      "version": 1
    }
  }
]
    </pre>

6. Importez le fichier JSON de recherche dans Kibana pour le nouvel espace.

    1. Dans la page Settings, sélectionnez l'onglet **Objects**.
    2. Sur l'onglet **Searches**, sélectionnez le fichier JSON de recherche que vous souhaitez importer.
    3. Cliquez sur **Import**.

Vous pouvez utiliser la recherche dans Kibana pour surveiller les données disponibles pour votre application dans le nouvel espace.


    
## Copie d'une visualisation
{:#k4_reuse_visualization}

Procédez comme suit pour copier vers un autre espace une visualisation à utiliser en vue d'analyser les données d'une application d'un espace :

1. Lancez Kibana pour l'espace dans lequel la visualisation à copier est disponible. 

    * Lancez Kibana depuis l'interface utilisateur {{site.data.keyword.Bluemix_notm}} : le fichier de recherche JSON que vous pouvez exporter inclut les zones suivantes : *space ID* et *application ID* pour les applications Cloud Foundry (CF) ou *instance ID* pour les conteneurs. Pour plus d'informations, voir [Accès au tableau de bord Kibana depuis le tableau de bord {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_bluemix).
    
    * Lancez Kibana depuis un navigateur : le fichier de recherche JSON que vous pouvez exporter inclut la zone *ID d'espace*. Pour plus d'informations, voir [Accès au tableau de bord Kibana depuis un navigateur](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_browser1).
    
2. Copiez la recherche qui est associée à la visualisation d'un espace vers un autre. Pour plus d'informations, voir [Copie d'une recherche d'un espace Bluemix vers un autre](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_search).

    Une visualisation utilise une recherche pour filtrer les données qui s'affichent. Il se peut qu'une visualisation soit liée à une recherche, dans ce cas, toutes les mises à jour que vous apportez à cette recherche sont mises à jour automatiquement, ou qu'elle ne soit pas liée à une recherche, dans ce cas, les seules données disponibles pour l'analyse sont celles qui sont affichées au moment où la visualisation est créée.

    Lorsque vous copiez une visualisation, quel que soit son statut de liaison à une recherche, vous devez aussi copier la recherche qui lui est associée. **Remarque :** lorsque vous importez une visualisation dans le nouvel espace, la nouvelle visualisation est liée à la recherche dans le nouvel espace.
    
3. Dans la page *Settings*, sélectionnez **Objects**, puis l'onglet **Visualizations**. Puis, sélectionnez une visualisation et procurez-vous les informations suivantes : 

    <table>
      <tbody>
        <tr>
          <th align="center">Zone de visualisation</th>
          <th align="center">Description</th>
        </tr>
        <tr>
          <td align="left">group</td>
          <td align="left"> ID de l'espace dans lequel la visualisation est utilisée pour analyser des données.</td>
        </tr>
        <tr>
          <td align="left">title</td>
          <td align="left">Nom de la visualisation.</td>
        </tr>
        <tr>
          <td align="left">version</td>
          <td align="left">Version de la visualisation.</td>
        </tr>
        <tr>
          <td align="left">savedSearchID</td>
          <td align="left">ID de la recherche qui est utilisée pour filtrer les données affichées via la visualisation. <br> Le format de la valeur est le suivant : `SpaceID_SearchTitle` où SearchTitle est la valeur de la zone *title* de la recherche. </td>
        </tr>
      </tbody>
    </table>
   

4. Exportez la visualisation.

    1. Dans la page Settings, sélectionnez l'onglet **Objects**.
    2. Dans l'onglet **Visualizations**, sélectionnez la visualisation à exporter.
    3. Cliquez sur **Export**.
    4. Sauvegardez le fichier JSON.
    
5. Dans l'interface utilisateur {{site.data.keyword.Bluemix_notm}}, passez dans l'espace dans lequel copier la visualisation, puis vérifiez que l'application ou le conteneur CF est disponible et en cours d'exécution.
    
6.  Modifiez le fichier de visualisation JSON que vous avez exporté lors d'une étape précédente. Remplacez les valeurs d'ID d'espace et d'ID de recherche. 

    L'objet JSON suivant est un exemple de fichier JSON de visualisation : 

    <pre class="pre">
    [
  {
    "_id": "3d8d2eae-f3f0-44f6-9717-126113a00b51_test",
    "_type": "visualization",
    "_source": {
      "description": "",
      "group": "3d8d2eae-f3f0-44f6-9717-126113a00b51",
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"filter\":[]}"
      },
      "savedSearchId": "3d8d2eae-f3f0-44f6-9717-126113a00b51_Default_9d222152-8834-4bab-8685-3036cd25931a",
      "title": "test",
      "version": 1,
      "visState": "{\"type\":\"line\",\"params\":{\"shareYAxis\":true,\"addTooltip\":true,\"addLegend\":true,\"showCircles\":true,\"smoothLines\":false,\"interpolate\":\"linear\",\"scale\":\"linear\",\"drawLinesBetweenPoints\":true,\"radiusRatio\":9,\"times\":[],\"addTimeMarker\":false,\"defaultYExtents\":false,\"setYExtents\":false,\"yAxis\":{}},\"aggs\":[{\"id\":\"1\",\"type\":\"count\",\"schema\":\"metric\",\"params\":{}}],\"listeners\":{}}"
    }
    }
    ]
    </pre>
    
    Dans cet exemple de fichier JSON, vous pouvez modifier les variables suivantes : 
    
    * SPACEID : Remplacez cette variable par l'ID d'espace du nouvel espace.
    * NAME : Remplacez cette variable si vous souhaitez modifier le nom de la visualisation dans le nouvel espace.
    * SEARCHID : Remplacez cette variable par l'ID de recherche du nouvel espace. ID de la requête qui est utilisée pour filtrer les données affichées via la visualisation.
    
       <pre class="pre">
    [
  {
    "_id": "SPACEID_NAME",
    "_type": "visualization",
    "_source": {
      "description": "",
      "group": "SPACEID",
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"filter\":[]}"
      },
      "savedSearchId": "SPACEID_SEARCHID",
      "title": "NAME",
      "version": 1,
      "visState": "{\"type\":\"line\",\"params\":{\"shareYAxis\":true,\"addTooltip\":true,\"addLegend\":true,\"showCircles\":true,\"smoothLines\":false,\"interpolate\":\"linear\",\"scale\":\"linear\",\"drawLinesBetweenPoints\":true,\"radiusRatio\":9,\"times\":[],\"addTimeMarker\":false,\"defaultYExtents\":false,\"setYExtents\":false,\"yAxis\":{}},\"aggs\":[{\"id\":\"1\",\"type\":\"count\",\"schema\":\"metric\",\"params\":{}}],\"listeners\":{}}"
    }
    }
    ]
    </pre>

8. Importez la visualisation.

    1. Dans la page Settings, sélectionnez l'onglet **Objects**.
    2. Sur l'onglet **Visualizations**, sélectionnez le fichier JSON de visualisation à importer.
    3. Cliquez sur **Import**.


Vous pouvez utiliser la visualisation dans Kibana pour surveiller les données disponibles pour votre application dans le nouvel espace.
    
