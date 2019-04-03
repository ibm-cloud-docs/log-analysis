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

# Filtrado de registros en Kibana
{:#filter_logs}

En la página Descubrir, puede crear consultas de búsqueda y aplicar filtros para restringir la información que se muestra para su análisis.
{:shortdesc}

* Puede definir una o varias consultas de búsqueda en la barra de búsqueda de la página Descubrir. Una consulta de búsqueda define un subconjunto de las entradas de registro. Utilice el lenguaje de consulta Lucene para definir una consulta de búsqueda. 

* Puede añadir filtros de la *Lista de campos* o de las entradas de la tabla. Un filtro ajusta la selección de datos mediante la inclusión o exclusión de información. Puede habilitar o inhabilitar un filtro, invertir la acción de filtrado, activar y desactivar el filtro o eliminarlo por completo. 

Después de definir una nueva búsqueda, guárdela para poder utilizarla para un análisis posterior en la página Descubrir o para crear visualizaciones que puede utilizar en los paneles de control personalizados. Para obtener más información, consulte [Cómo guardar una búsqueda](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search1).

Cuando realiza una nueva búsqueda, el histograma, la tabla y la lista de campos se actualizan automáticamente para mostrar los resultados de la búsqueda. Para averiguar qué datos se muestran, consulte [Identificación de los datos que se muestran en la página Descubrir](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

En la lista siguiente se resumen casos de ejemplo que muestran cómo filtrar datos en los registros:

* Puede crear búsquedas personalizadas para filtrar los registros. Para obtener más información, consulte [Filtrado de registros mediante la definición de consultas personalizadas](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search).

* Puede buscar en el registro las entradas que incluyan un determinado texto en el valor de un campo. Para obtener más información, consulte [Filtrado de registros para un determinado texto en un valor de campo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs_spec_text).
 
* Puede buscar en el registro un determinado valor de campo o excluir del registro las entradas correspondientes a un valor de campo específico. Para obtener más información, consulte [Filtrado de registros para un determinado valor de campo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs_spec_field).
 
* Puede filtrar los registros para que muestren las entradas comprendidas en un periodo de tiempo. Para obtener más información, consulte [Establecimiento de un filtro de tiempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).
     

## Adición de un filtro para un valor que no aparece en la *Lista de campos*
{:#add_filter_out_value}

Para añadir un filtro para un valor que no se muestra en la *Lista de campos*, busque los registros que incluyen dicho valor mediante una consulta. A continuación, añada el filtro de la entrada de la tabla que está disponible en la página Descubrir. 

Siga los pasos siguientes para añadir un filtro para un valor que no está disponible en la lista que se muestra en la sección *Lista de campos*:

1. Examine la página Descubrir de Kibana para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

2. En la página Descubrir, modifique la consulta para que busque un determinado valor de campo.

    Por ejemplo, para buscar la instancia *3*, la consulta que debe especificar es la siguiente:
   `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:"3"`
    
    En la tabla verá los registros que coincidan con la consulta. 
    
 3. Expanda un registro y seleccione el botón de lupa ![Botón de lupa en modalidad de inclusión](images/include_field_icon.jpg "Botón de lupa en modalidad de inclusión") para añadir un filtro.
     
4. Compruebe que el filtro se ha añadido.

   


## Filtrado de los registros correspondientes a un valor de campo específico
{:#filter_logs_spec_field}

Puede buscar entradas que incluyan un determinado valor de campo. 

Siga estos pasos para buscar entradas que incluyan un determinado valor de campo:

1. Examine la página Descubrir de Kibana para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

2. En la *Lista de campos*, identifique el campo para la que desee definir un filtro y pulse sobre el mismo.

    En el campo se muestra un máximo de 5 valores. Cada valor tiene dos botones de lupa. 
    
    Si no puede ver el valor, consulte [Adición de un filtro para un valor que no aparece en la lista de campos](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#add_filter_out_value).

3. Para añadir un filtro que busque entradas con un valor de campo, seleccione la lupa con un signo más ![Botón de lupa en modalidad de inclusión](images/include_field_icon.jpg "Botón de lupa en modalidad de inclusión") para dicho valor.

    Para añadir un filtro que busque entradas que no incluyan este valor de campo, seleccione la lupa con un signo menos ![Botón de lupa en modalidad de exclusión](images/exclude_field_icon.jpg "Botón de lupa en modalidad de exclusión") para dicho valor.

4. Elija una de las siguientes opciones para trabajar con filtros en Kibana:

    <table>
      <caption>Tabla 1. Métodos para trabajar con filtros</caption>
      <tbody>
        <tr>
          <th align="center">Opción</th>
          <th align="center">Descripción</th>
          <th align="center">Otra información</th>
        </tr>
        <tr>
          <td align="left">Habilitar</td>
          <td align="left">Seleccione esta opción para habilitar un filtro.</td>
          <td align="left">Cuando añade un filtro, se habilita automáticamente. <br> Si un filtro está inhabilitado, pulse sobre el mismo para habilitarlo.</td>
        </tr>
        <tr>
          <td align="left">Inhabilitar</td>
          <td align="left">Seleccione esta opción para inhabilitar un filtro.</td>
          <td align="left">Después de añadir un filtro, si desea ocultar las entradas correspondientes a un valor de campo, pulse **inhabilitar**.</td>
        </tr>
        <tr>
          <td align="left">Fijar</td>
          <td align="left">Seleccione esta opción para que el filtro se aplique en todas las páginas de Kibana.</td>
          <td align="left">Puede fijar un filtro en la página *Descubrir*, en la página *Visualizar* o en la página *Panel de control*.</td>
        </tr>
        <tr>
          <td align="left">Conmutar</td>
          <td align="left">Seleccione esta opción para conmutar un filtro.</td>
          <td align="left">De forma predeterminada, se muestran las entradas que coinciden con un filtro. Para visualizar las entradas que no coinciden, conmute el filtro.</td>
        </tr>
        <tr>
          <td align="left">Eliminar</td>
          <td align="left">Seleccione esta opción para eliminar un filtro.</td>
          <td align="left"></td>
        </tr>
      </tbody>
    </table>

	
## Filtrado de los registros de una app CF por origen
{:#filter_logs_by_source}

Siga estos pasos para buscar entradas que incluyan un determinado origen de registro:

1. Examine la página Descubrir de Kibana para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

2. En la *Lista de campos*, seleccione el campo **source_id**.

3. Para añadir un filtro que busque las entradas que incluyan un determinado source_id, seleccione el botón de lupa ![Botón de lupa en modalidad de inclusión](images/include_field_icon.jpg "Botón de lupa en modalidad de inclusión") para dicho valor.

    Para obtener una lista de orígenes de registro que están disponibles para apps CF, consulte [Orígenes de registro para apps CF](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-logging_cf_apps#logging_bluemix_cf_apps_log_sources).

    Para añadir un filtro que busque las entradas que no incluyan un determinado source_id, elija el botón de lupa ![Botón de lupa en modalidad de exclusión](images/exclude_field_icon.jpg "Botón de lupa en modalidad de exclusión") para el valor.
    


## Filtrado de registros por tipo de registro
{:#filter_logs_by_log_type}

Siga estos pasos para buscar entradas que incluyan un determinado tipo de registro:

1. Examine la página Descubrir de Kibana para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

2. En la *Lista de campos*, seleccione el campo **type**.

3. Para añadir un filtro que busque un determinado tipo de registro, seleccione el botón de lupa ![Botón de lupa en modalidad de inclusión](images/include_field_icon.jpg "Botón de lupa en modalidad de inclusión") para el tipo de registro que desea analizar.

    Para añadir un filtro que busque las entradas que no incluyan un determinado tipo de registro, seleccione el botón de lupa ![Botón de lupa en modalidad de exclusión](images/exclude_field_icon.jpg "Botón de lupa en modalidad de exclusión") para el valor.



## Filtrado de registros por ID de instancia
{:#filter_logs_by_instance_id}

Siga estos pasos para ver y filtrar los registros por ID de instancia en el panel de control de Kibana:

1. Examine la página Descubrir de Kibana para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

2. En la *Lista de campos*, seleccione uno de los siguientes campos para buscar un determinado ID de instancia:

    * **instance_ID**: Este campo muestra los distintos ID de instancia disponibles en el registro para una aplicación Cloud Foundry. 
    * **instance**: Este campo muestra los distintos GUID de todas las instancias correspondientes a un grupo de contenedores. 
	* **docker.container_id_str**: Este campo muestra los distintos ID correspondientes a los contenedores desplegados en una infraestructura de Kubernetes.
   
3. Para añadir un filtro que busque un determinado tipo de registro, seleccione el botón de lupa ![Botón de lupa en modalidad de inclusión](images/include_field_icon.jpg "Botón de lupa en modalidad de inclusión") para el tipo de registro que desea analizar.

    Para añadir un filtro que busque las entradas que no incluyan un determinado ID de instancia, seleccione el botón de lupa ![Botón de lupa en modalidad de exclusión](images/exclude_field_icon.jpg "Botón de lupa en modalidad de exclusión") para el valor.



## Filtrado de registros de la app CF por tipo de mensaje
{:#filter_cf_logs_by_msg_type}

Siga estos pasos para buscar entradas que incluyan un determinado tipo de mensaje:

1. Examine la página Descubrir de Kibana para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

2. En la *Lista de campos*, seleccione el campo **message_type**.

    Se muestran los tipos de campos disponibles. 

3. Para añadir un filtro que busque las entradas que incluyan un determinado *message_type*, seleccione el botón de lupa ![Botón de lupa en modalidad de inclusión](images/include_field_icon.jpg "Botón de lupa en modalidad de inclusión") para dicho valor.

    Para añadir un filtro que busque las entradas que no incluyan un determinado *message_type*, elija el botón de lupa ![Botón de lupa en modalidad de exclusión](images/exclude_field_icon.jpg "Botón de lupa en modalidad de exclusión") para el valor.
    
 
	

## Filtrado de los registros correspondientes a un texto específico en un valor de campo
{:#filter_logs_spec_text}

Vea y busque entradas que incluyan un texto específico en el valor de un campo. 

**Nota:** sólo puede realizar una búsqueda de texto libre de campos de serie de caracteres que analice el analizador Elasticsearch. 
    
Cuando Elasticsearch analiza el campo valor de una serie, divide el texto en límites de palabras, según lo establecido por el consorcio Unicode, y elimina los signos de puntuación y las minúsculas en todas las palabras.
    
Siga estos pasos para buscar entradas que incluyan un determinado texto en un valor de campo:

1. Examine la página Descubrir de Kibana para ver el subconjunto de datos que muestra. Para obtener más información, consulte [Identificación de los datos que se muestran en la página Descubrir de Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data).

2. Identifique los campos que se analizan en ElasticSearch de forma predeterminada.

    Para ver la lista completa de campos analizados que están disponibles para buscar y filtrar datos de registro, [vuelva a cargar la lista de campos](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_reload_fields). A continuación, en la *Lista de campos* disponible en la página Descubrir, siga los pasos siguientes:
    
    1. Pulse el icono de configuración ![Icono de configuración](images/configure_icon.jpg "Icono de configuración"). Se muestra la sección **Campos seleccionados**, donde puede filtrar los campos.

    2. Para identificar los campos que se analizan, seleccione **Sí** en el campo de búsqueda **Analizado**.

        Se muestra la lista de campos analizados.
    
    3. Compruebe si el campo en el que desea buscar texto libre es un campo analizado por ElasticSearch de forma predeterminada.
    
3. Si es un campo analizado, modifique la consulta para buscar las entradas en los registros que incluyan dicho texto libre como parte del valor de un campo.

    
**Ejemplo**

Si inicia Kibana para una aplicación Cloud Foundry (CF) desde la IU de {{site.data.keyword.Bluemix}} y desea buscar un determinado mensaje que incluya el ID de mensaje *CWWKT0016I:*, modifique la búsqueda para que incluya el texto libre.
    
1. Compruebe la consulta de búsqueda que se carga y los datos que se muestran en la página Descubrir.
       
2. Para buscar el ID de mensaje *CWWKT0016I*, modifique la consulta de búsqueda en la **barra de búsqueda** y pulse **Intro**.
    
    Por ejemplo, escriba el siguiente texto en la barra de búsqueda para una app CF con el ID *f52f6016-3aab-4b5c-aa2e-5493747cb978*:

	`<pre class="pre">application_id:f52f6016-3aab-4b5c-aa2e-5493747cb978 AND message:"CWWKT0016I:" </pre>`
        
          
La tabla muestra las entradas de la app CF en las que el texto *CWWKT0016I* forma parte del valor del campo *Mensaje*.
    
 	
        

## Establecimiento de un filtro de tiempo
{: #set_time_filter}

Vea y filtre los registros comprendidos en un periodo de tiempo configurando el *Selector de tiempo*.

Puede configurar el *Selector de tiempo* en la página Descubrir. De forma predeterminada, está establecido en los últimos 15 minutos. 

Siga estos pasos para buscar entradas que incluyan un determinado tiempo:

1. En la barra de menús de la página Descubrir, pulse Selector de tiempo ![Selector de tiempo](images/time_picker_icon.jpg "Selector de tiempo").

2. Configure el intervalo de tiempo. 

    Puede definir cualquiera de los siguientes tipos de intervalos de tiempo:
    
    * Rápido: son intervalos de tiempo predefinidos que incluyen los casos más comunes de los intervalos de tiempo Relativo y Absoluto; por ejemplo *Hoy* y *Este mes*. 
       
    * Relativo: son intervalos de tiempo en los que puede especificar la fecha y hora de inicio y la fecha y hora final. Las puede redondear por hora.
    
    * Absoluto: son intervalos de tiempo entre una fecha inicial y una fecha final.
    

Después de configurar un intervalo de tiempo, los datos que aparecen en Kibana corresponden a las entradas comprendidas en dicho rango de tiempo.








