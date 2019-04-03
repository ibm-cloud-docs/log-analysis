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

# Definición de consultas de búsqueda personalizadas
{:#define_search}

En la barra de búsqueda de la página Descubrir, puede definir y guardar consultas de búsqueda utilizando el lenguaje de consulta de Lucene. Para cada búsqueda, puede aplicar filtros para precisar las entradas que están disponibles para el análisis.
{:shortdesc}

Complete las siguientes tareas para definir una búsqueda personalizada:

1. Inicie Kibana.

    Para las apps Cloud Foundry (CF), consulte [inicio de Kibana desde el panel de control de una app CF](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app).

	Para contenedores que se ejecutan en la infraestructura gestionada por {{site.data.keyword.Bluemix_notm}}, consulte [inicio de Kibana desde el panel de control de un contenedor](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers).
    
    Para todos los recursos de nube, por ejemplo los contenedores que se ejecutan en un clúster Kubernetes, consulte [inicio de Kibana desde el navegador](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser). 
	
	Cuando se accede a Kibana, se aplica la búsqueda predeterminada. Puede ver los registros de la lista de instancias del recurso que está consultando. Puede filtrar los registros para cualquiera de los recursos de {{site.data.keyword.Bluemix_notm}} o para todos ellos en este espacio.

2. Examine la página Descubrir para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data). A continuación, modifique la consulta predeterminada para filtrar las entradas.

    **Nota:** Utilice el lenguaje de consulta de Lucene para definir la consulta personalizada. Para obtener más información, consulte [Apache Lucene - Sintaxis del analizador de consultas ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}
    
    Cuando Kibana se inicia desde la IU de {{site.data.keyword.Bluemix_notm}}, para modificar la consulta y definir varios criterios de búsqueda puede utilizar los términos lógicos **AND** y **OR**. Estos operadores deben estar en mayúsculas.    
    
    * Para buscar una palabra clave, o parte de una palabra clave, escriba una palabra seguida de un asterisco (*), que es un comodín; por ejemplo, `Java*`. 
    * Para buscar una determinada frase, escriba la frase entre comillas dobles (" "); por ejemplo, `"Java/1.8.0"`.
    * Para crear búsquedas más complejas, puede utilizar los términos lógicos AND y OR; por ejemplo `"Java/1.8.0" OR "Java/1.7.0"`.
    * Para buscar un valor dentro de un campo determinado, escriba la búsqueda con el siguiente formato: *log_field_name:search_term*; por ejemplo, `instance_id:"1"`.
    * Para buscar un rango de valores para un determinado campo de registro, escriba la búsqueda con el siguiente formato: *log_field_name:[start_of_range TO end_of_range]*; por ejemplo, `instance_id:["1" TO "2"]`.

     Por ejemplo, para una app CF, puede crear una consulta `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]`que muestre solo  las entradas correspondientes a las instancias *0* y *1*. 

3. Guarde la consulta para poderla reutilizar más adelante. Para obtener más información, consulte [Cómo guardar una búsqueda](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1). 

**Nota:** Si tiene que suprimir una consulta, consulte [Supresión de una búsqueda](/docs/services/CloudLogAnalysis/kibana/define_search.html#delete_search).



## Supresión de una búsqueda
{: #delete_search}

Para suprimir una búsqueda, siga los pasos siguientes en la página Valores:

1. En la página Valores, seleccione el separador **Objetos**.

2. En el separador **Búsquedas**, seleccione las búsquedas que desea suprimir.

3. Pulse **Suprimir**.


## Exportación de una búsqueda
{: #export_search}

Para exportar una búsqueda, siga los pasos siguientes en la página Valores:

1. En la página Valores, seleccione el separador **Objetos**.

2. En el separador **Búsquedas**, seleccione las búsquedas que desea exportar.

3. Pulse **Exportar**.

4. Guarde el archivo.

 
## Importación de una búsqueda
{: #import_search}

Para importar una búsqueda, siga los pasos siguientes en la página Valores:

1. En la página Valores, seleccione el separador **Objetos**.

2. En el separador **Búsquedas**, seleccione **Importar**.

3. Seleccione un archivo y pulse **Abrir**.

La búsqueda se añade a la lista de búsquedas.

## Renovación del contenido de una búsqueda
{: #refresh_search}

Para renovar de forma manual el contenido de una búsqueda, puede pulsar sobre la lupa que está disponible en la barra de búsqueda. 

Para renovar automáticamente los datos que se muestran en la página Descubrir, puede configurar un intervalo de renovación. El valor actual del intervalo de renovación se muestra en la barra de menús de la página Descubrir. De forma predeterminada, la opción para renovar automáticamente está **DESACTIVADA**.

Siga los siguientes pasos para establecer un intervalo de renovación:

1. En la página Descubrir, pulse el **Filtro de tiempo** que está disponible en la barra de menús.

2. Pulse **Renovación automática** ![Renovación automática](images/auto_refresh_icon.jpg "Renovación automática").

3. Seleccione un intervalo de renovación de la lista. 

**Nota**: Después de habilitar un intervalo de renovación automática, puede colocarlo en pausa pulsando el botón de pausa ![Pausa](images/auto_refresh_pause_icon.jpg "Pausa").


## Cómo volver a cargar una búsqueda
{: #reload_search1}

Siga los siguientes pasos para cargar una búsqueda guardada:

1. En la barra de herramientas de la página Descubrir, pulse el botón **Cargar búsqueda** ![Cargar búsqueda](images/load_icon.jpg "Cargar búsqueda").

2. Seleccione la búsqueda que desea cargar. 

## Inicio de una nueva búsqueda
{: #k4_new_search}

Para iniciar una nueva búsqueda, pulse el botón **Nueva búsqueda** ![Nueva búsqueda](images/new_search_icon.jpg "Nueva búsqueda") en la barra de herramientas de la página Descubrir.

## Cómo guardar una búsqueda 
{: #save_search1}

Tenga en cuenta la siguiente información sobre cómo guardar búsquedas personalizadas en Kibana:

* Cuando se guarda una búsqueda, se guardan la serie de consulta de la búsqueda y el patrón de índice seleccionado actualmente.
* Cuando abre una búsqueda en la página *Descubrir* y la modifica, puede elegir entre guardarla con el mismo nombre o guardar la búsqueda personalizada modificada con otro nombre. De forma predeterminada, el nombre de búsqueda que se proporciona es el que corresponde a la búsqueda personalizada que haya abierto inicialmente.

    * Para guardar la búsqueda personalizada modificada con el mismo nombre, pulse **Guardar**. Tenga en cuenta que la búsqueda personalizada original se sobrescribe. 
	
	* Para guardar la búsqueda personalizada modificada con otro nombre, escriba un nombre nuevo en el campo **Guardar búsqueda** y, a continuación, pulse **Guardar**. 


Siga los pasos siguientes para guardar la búsqueda actual en la página Descubrir:

1. En la barra de herramientas de la página Descubrir, pulse el botón **Guardar búsqueda** ![Guardar búsqueda](images/save_search_icon.jpg "Guardar búsqueda").

2. Escriba un nombre para la búsqueda.

    **Nota:** Cuando pulse **Guardar**, no hay aviso acerca de la sobrescritura, por lo que, si especifica un nombre existente, se sustituirá dicha versión sin ninguna indicación.

3. Pulse **Guardar**. 
