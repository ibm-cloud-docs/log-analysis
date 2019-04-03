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

# Kibana-Ressourcen zum Analysieren von {{site.data.keyword.Bluemix_notm}}-Protokollen wiederverwenden
{:#k4_reuse_resource}

Um eine Suche, eine Visualisierung oder ein Dashboard aus einem {{site.data.keyword.Bluemix}}-Bereich in einen anderen zu kopieren, verwenden Sie die in Kibana verfügbaren Import- und Exportfunktionen. Sie können Ressourcen einzeln kopieren oder alle Ressourcen in Kibana exportieren.
{:shortdesc}

| Task | Beschreibung |
|------|-------------|
| [Suche kopieren](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_search) | Kopieren Sie eine Suche zwischen Bereichen. |
| [Visualisierung kopieren](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_visualization) | Kopieren Sie eine Visualisierung zwischen Bereichen. |

Beachten Sie die folgenden Szenarios in {{site.data.keyword.Bluemix_notm}} für die Wiederverwendung von Suchen, Visualisierungen und oder Dashboards: 

* Kopieren einer Ressource zwischen Bereichen in derselben Organisation.

    Sie möchten beispielsweise Visualisierungen vom Entwicklungsbereich in den Staging-Bereich kopieren.
    
* Kopieren einer Ressource zwischen Bereichen in verschiedenen Organisationen im selben Konto.

    Sie möchten beispielsweise Visualisierungen von einem Bereich in der Entwicklungsorganisation in einen Bereich in die Staging-Organisation kopieren.

* Kopieren einer Ressource zwischen Bereichen, die sich zwar in derselben Organisation, aber in unterschiedlichen öffentlichen Regionen befinden.

    Sie möchten beispielsweise Visualisierungen von einem Bereich in Organisation A in {{site.data.keyword.Bluemix_notm}}, der sich in der öffentlichen Region 'USA (Süden)' befindet, in einen Bereich in der Organisation A in der Public-Region 'Vereinigtes Königreich' kopieren.



## Suche kopieren
{:#k4_reuse_search}

Führen Sie die folgenden Schritte aus, um eine Suche zwischen Bereichen in {{site.data.keyword.Bluemix_notm}} zu kopieren:

1. Starten Sie Kibana in dem Bereich, in dem die Suche verfügbar ist, die Sie kopieren möchten. 

    * Kibana über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle starten: Die JSON-Suchdatei, die Sie exportieren können, enthält die folgenden Felder: die *Bereichs-ID* und *Anwendungs-ID* für Cloud Foundry-Anwendungen (CF) oder die *Instanz-ID* für Container. Weitere Informationen finden Sie unter [Vom {{site.data.keyword.Bluemix_notm}}-Dashboard zum Kibana-Dashboard navigieren](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_bluemix).
    
    * Kibana über einen Browser starten: Die JSON-Suchdatei, die Sie exportieren können, enthält das Feld für die *Bereichs-ID*. Weitere Informationen finden Sie unter [Zum Kibana-Dashboard über einen Browser navigieren](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_browser1).

2. Wählen Sie auf der Seite *Settings* die Option **Objects** und anschließend die Registerkarte **Searches** aus. Suchen Sie dann eine Suche aus und kopieren Sie die folgenden Informationen:

    <table>
      <tbody>
        <tr>
          <th align="center">Suchfeld</th>
          <th align="center">Beschreibung</th>
        </tr>
        <tr>
          <td align="left">group</td>
          <td align="left"> Die ID des Bereichs, für den die Suche zum Filtern von Daten anwendet wird.</td>
        </tr>
        <tr>
          <td align="left">title</td>
          <td align="left">Der Name der Suche.</td>
        </tr>
        <tr>
          <td align="left">version</td>
          <td align="left">Die Version der Suche.</td>
        </tr>
      </tbody>
    </table>
   
3. Exportieren Sie die Suche.

    1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.
    2. Wählen Sie in der Registerkarte **Searches** die Suche aus, die Sie exportieren wollen.
    3. Klicken Sie auf **Export**.
    4. Speichern Sie die JSON-Datei.

4. Wechseln Sie in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle zu dem Bereich, in dem Sie die Suche kopieren möchten, und überprüfen Sie, dass die CF-Anwendung bzw. der Container verfügbar und aktiv ist.
    
5. Starten Sie Kibana für den {{site.data.keyword.Bluemix_notm}}-Bereich, in dem Sie die Suche importieren möchten, und rufen Sie anschließend die folgenden Informationen ab:

    Über die [Bluemix-Benutzerschnittstelle](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_bluemix):
    
    <table>
      <tbody>
        <tr>
          <th align="center">Suchfeld</th>
          <th align="center">Beschreibung</th>
        </tr>
        <tr>
          <td align="left">Bereichs-ID</td>
          <td align="left"> <ol><li> Wählen Sie auf der Seite *Settings* die Registerkarte *Indices* aus.</li> <br> <li>Die Bereichs-ID ist im Indexmuster eingebettet. Das Indexmuster hat folgendes Format: `[logstash-3d8d2eae-Bereichs-ID-]JJJJ.MM.TT`, wobei *Bereichs-ID* die ID des Bereichs ist. Kopieren Sie die Bereichs-ID.</li></ol></td>
        </tr>
        <tr>
          <td align="left">Anwendungs-ID oder Instanz-ID</td>
          <td align="left"><ul><li>Wenn Sie Kibana über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle starten, wird standardmäßig die Seite *Discover* geöffnet. Rufen Sie die Anwendungs-ID oder die Instanz-ID über die Suchleiste auf der Seite *Discover* ab. Beispiel: `application_id:d88d1f16-e9d9-4623-bce7-0348c88f5133`.</li> <br> <li>Wenn Sie Kibana über einen Browser starten, wählen Sie das Feld 'application_id' oder 'instance_id' aus der Feldliste auf der Seite 'Discover' aus.</li></ul></td>
        </tr>
      </tbody>
    </table>

6. Ändern Sie die JSON-Suchdatei, die Sie im vorherigen Schritt exportiert haben. Ersetzen Sie den Wert für die Anwendungs-ID (application_id). 

    Der folgende JSON-Codeausschnitt ist ein Beispiel für eine JSON-Suchdatei. 
 
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
    
    In dieser JSON-Beispieldatei können Sie die folgenden Variablen anhand der Informationen des neuen Bereichs ändern: 
    
    * SPACEID: Ersetzen Sie diese Variable durch die Bereichs-ID des neuen Bereichs.
    * NAME: Ersetzen Sie diese Variable, wenn Sie den Namen der Suche im neuen Bereich ändern möchten. Wenn Sie den Namen beibehalten möchten, ändern Sie diesen Wert nicht.
    * APPID: Ersetzen Sie diese Variable durch den Wert für 'application_id' der CF-App im neuen Bereich oder durch den Wert für 'instance_id' des Containers im neuen Bereich.
    
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

6. Importieren Sie die JSON-Suchdatei für den neuen Bereich in Kibana.

    1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.
    2. Wählen Sie auf der Registerkarte **Searches** die JSON-Suchdatei aus, die Sie importieren möchten.
    3. Klicken Sie auf **Import**.

Mit der Suche in Kibana können Sie die Daten überwachen, die für Ihre Anwendung im neuen Bereich verfügbar sind.


    
## Visualisierung kopieren
{:#k4_reuse_visualization}

Führen Sie die folgenden Schritte aus, um eine Visualisierung, mit der Sie Daten einer Anwendung in einem Bereich analysieren, in einen anderen Bereich kopieren:

1. Starten Sie Kibana für den Bereich, in dem die Visualisierung, die Sie kopieren möchten, verfügbar ist. 

    * Kibana über die {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle starten: Die JSON-Suchdatei, die Sie exportieren können, enthält die folgenden Felder: die *Bereichs-ID* und *Anwendungs-ID* für Cloud Foundry-Anwendungen (CF) oder die *Instanz-ID* für Container. Weitere Informationen finden Sie unter [Vom {{site.data.keyword.Bluemix_notm}}-Dashboard zum Kibana-Dashboard navigieren](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_bluemix).
    
    * Kibana über einen Browser starten: Die JSON-Suchdatei, die Sie exportieren können, enthält das Feld für die *Bereichs-ID*. Weitere Informationen finden Sie unter [Zum Kibana-Dashboard über einen Browser navigieren](/docs/services/CloudLogAnalysis/kibana4/k4_launch.html#launch_Kibana_from_browser1).
    
2. Kopieren Sie die Suche, die der Visualisierung zugeordnet ist, zwischen den Bereichen. Weitere Informationen finden Sie unter [Suche zwischen Bluemix-Bereichen kopieren](/docs/services/CloudLogAnalysis/kibana4/k4_reuse_resource.html#k4_reuse_search).

    Eine Visualisierung verwendet eine Suche zum Filtern der angezeigten Daten. Sie kann mit einer Suche verknüpft sein, damit alle Aktualisierungen, die Sie an der Suche vornehmen, automatisch aktualisiert werden. Ist eine Visualisierung nicht mit einer Suche verknüpft, sind die einzigen Daten, die für eine Analyse zur Verfügung stehen, die Daten, die zum Zeitpunkt der Erstellung der Visualisierung angezeigt werden.

    Unabhängig davon, ob eine Visualisierung mit einer Suche verknüpft ist oder nicht, müssen Sie beim Kopieren einer Visualisierung auch die Suche kopieren, die der Visualisierung zugeordnet ist. **Hinweis:** Wenn Sie eine Visualisierung in den neuen Bereich importieren, wird die neue Visualisierung mit der Suche in dem neuen Bereich verknüpft.
    
3. Wählen Sie auf der Seite *Settings* die Option **Objects** und anschließend die Registerkarte **Visualizations** aus. Wählen Sie dann eine Visualisierung aus und rufen Sie die folgenden Informationen ab: 

    <table>
      <tbody>
        <tr>
          <th align="center">Feld 'Visualization'</th>
          <th align="center">Beschreibung</th>
        </tr>
        <tr>
          <td align="left">group</td>
          <td align="left"> Die ID des Bereichs, in dem die Visualisierung für die Analyse von Daten verwendet wird.</td>
        </tr>
        <tr>
          <td align="left">title</td>
          <td align="left">Der Name der Visualisierung.</td>
        </tr>
        <tr>
          <td align="left">version</td>
          <td align="left">Die Version der Visualisierung.</td>
        </tr>
        <tr>
          <td align="left">savedSearchID</td>
          <td align="left">Die ID der Suche, die zum Filtern der Daten verwendet wird, die mithilfe der Visualisierung angezeigt werden. <br> Der Wert weist das folgende Format auf: `Bereichs-ID_Titel_der_Suche`. Dabei ist 'Titel_der_Suche' der Wert des Feldes *title* der Suche. </td>
        </tr>
      </tbody>
    </table>
   

4. Exportieren Sie die Visualisierung.

    1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.
    2. Wählen Sie in der Registerkarte **Visualizations** die Visualisierung aus, die Sie exportieren wollen.
    3. Klicken Sie auf **Export**.
    4. Speichern Sie die JSON-Datei.
    
5. Wechseln Sie in der {{site.data.keyword.Bluemix_notm}}-Benutzerschnittstelle zu dem Bereich, in dem Sie die Visualisierung kopieren möchten, und überprüfen Sie, dass die CF-Anwendung bzw. der Container verfügbar und aktiv ist.
    
6.  Ändern Sie die JSON-Visualisierungsdatei für die Suche, die Sie im vorherigen Schritt exportiert haben. Ersetzen Sie die Werte der Bereichs-ID und der Such-ID. 

    Der folgende JSON-Codeausschnitt ist ein Beispiel für eine JSON-Visualisierungsdatei. 

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
    
    In dieser JSON-Beispieldatei können Sie die folgenden Variablen ändern: 
    
    * SPACEID: Ersetzen Sie diese Variable durch die Bereichs-ID des neuen Bereichs.
    * NAME: Ersetzen Sie diese Variable, wenn Sie den Namen der Visualisierung im neuen Bereich ändern möchten.
    * SEARCHID: Ersetzen Sie dieses Variable durch die Such-ID im neuen Bereich. Dies ist die ID der Abfrage, die zum Filtern der Daten verwendet wird, die mithilfe der Visualisierung angezeigt werden.
    
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

8. Importieren Sie die Visualisierung.

    1. Wählen Sie auf der Seite 'Settings' die Registerkarte **Objects** aus.
    2. Wählen Sie auf der Registerkarte **Visualizations** die JSON-Visualisierungsdatei aus, die Sie importieren möchten.
    3. Klicken Sie auf **Import**.


Mit der Visualisierung in Kibana können Sie die Daten überwachen, die für Ihre Anwendung im neuen Bereich verfügbar sind.
    
