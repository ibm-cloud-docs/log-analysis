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

# Visualización y análisis de registros (Kibana)
{:#analyzing_logs_Kibana}

Puede utilizar Kibana 5.1, una plataforma de visualización y análisis de código abierto, para supervisar, buscar, analizar y visualizar datos en diversos gráficos, como diagramas y tablas. Utilice Kibana para realizar tareas avanzadas de análisis.
{:shortdesc}

Kibana es una interfaz basada en navegador con la que puede analizar datos de forma interactiva y personalizar paneles de control que luego puede utilizar para analizar datos de registro y realizar tareas avanzadas de gestión. Para obtener más información, consulte la [Guía del usuario de Kibana ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.

Los datos que muestran una página de Kibana están restringidos por una búsqueda. El conjunto de datos predeterminado se define mediante un patrón de índice preconfigurado. Para filtrar la información, puede añadir nuevas consultas de búsqueda y aplicar filtros al conjunto de datos predeterminado. Luego puede guardar la búsqueda para reutilizarla en el futuro. 

Kibana incluye varias páginas que puede utilizar para analizar los registros:

| Página de Kibana | Descripción |
|-------------|-------------|
| Descubrir | Utilice esta página para definir búsquedas y analizar los registros de forma interactiva a través de una tabla y un histograma. |
| Visualizar | Utilice esta página para crear visualizaciones, como gráficos y tablas, que puede utilizar para analizar los datos de registro y comparara los resultados.  |
| Panel de control | Utilice esta página para analizar los registros a través de recopilaciones de visualizaciones y búsquedas guardadas.  |
{: caption="Tabla 1. Páginas de Kibana" caption-side="top"}

**Nota:** Sólo puede analizar 1 día completa cada vez mediante la página Visualizar o la página Panel de control, aunque puede retroceder 3 días. Los datos del registro se guardan de forma predeterminada durante 3 días. 

| Página de Kibana | Información sobre periodo de tiempo |
|-------------|-------------------------|
| Descubrir | Analizar datos correspondientes a un máximo de 3 días. |
| Visualizar | Analizar datos correspondientes a un periodo de 24 horas. <br> Puede filtrar los datos de registro durante un periodo personalizado que comprenda 24 horas.  |
| Panel de control | Analizar datos correspondientes a un periodo de 24 horas. <br> Puede filtrar los datos de registro durante un periodo personalizado que comprenda 24 horas. <br> El selector de tiempo que defina se aplica a todas las visualizaciones que se incluyen en el panel de control. |
{: caption="Tabla 2. Información sobre periodo de tiempo" caption-side="top"}

Por ejemplo, así es cómo puede utilizar Kibana para que muestre información sobre una app CF o un contenedor del espacio en diversas páginas:

## Navegación al panel de control de Kibana
{: #launch_Kibana}

Puede iniciar Kibana de cualquiera de estas formas:

* Desde el panel de control del servicio {{site.data.keyword.loganalysisshort}}

    Puede iniciar Kibana para que los datos que ve agreguen registros de servicios de un espacio especificado.
	
	Para obtener más información, consulte [Navegación a Kibana desde el panel de control del servicio Análisis de registros](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_log_analysis).

* Desde {{site.data.keyword.Bluemix_notm}}

    Puede iniciar los registros específicos de la app CF en Kibana, dentro del contexto de la app específica. Para obtener más información, consulte [Navegación a Kibana desde el panel de control de una app CF](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app).
    
    Puede iniciar registros de un contenedor Docker específico en Kibana, dentro del contexto de dicho contenedor en concreto. Esta característica únicamente se aplica a contenedores desplegados en la infraestructura gestionada por {{site.data.keyword.Bluemix_notm}}. Para obtener más información, consulte [Navegación a Kibana desde el panel de control de un contenedor](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers).
    
    Para las apps CF, la consulta que se utiliza para filtrar los datos disponibles para análisis en Kibana recupera las entradas de registro de la aplicación Cloud Foundry. La información de registro que muestra Kibana de forma predeterminada está relacionada con una sola aplicación Cloud Foundry y todas sus instancias. 
    
    Para contenedores, la consulta que se utiliza para filtrar los datos disponibles para análisis en Kibana recupera las entradas de registro de todas las instancias del contenedor. La información de registro que muestra Kibana de forma predeterminada está relacionada con un solo contenedor o con un grupo de contenedores y todas sus instancias. 
    
    

* Desde un enlace directo del navegador

    Puede iniciar Kibana para que los datos que ve agreguen registros de servicios de un espacio especificado.
    
    La consulta que se utiliza para filtrar los datos que aparecen en el panel de control recupera las entradas de registro correspondientes a un espacio de la organización {{site.data.keyword.Bluemix_notm}}. La información de registro que muestra Kibana incluye registros correspondientes a todos los recursos desplegados dentro del espacio de la organización {{site.data.keyword.Bluemix_notm}} en la que ha iniciado la sesión. 
    
    Para obtener más información, consulte [Navegación al panel de control de Kibana desde un navegador web](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser).
    
    

## Análisis de datos de forma interactiva
{: #analyze_discover}

En la página Descubrir, puede definir nuevas consultas de búsqueda y aplicar filtros por consulta. Los datos de registro se muestran en una tabla y un histograma. Puede utilizar estas visualizaciones para analizar los datos de forma interactiva. Para obtener más información, consulte [Análisis interactivo de registros en Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#analize_logs_interactively).

Puede configurar filtros desde campos de registro, por ejemplo message_type e instance_ID, y definir un periodo de tiempo. Puede habilitar o inhabilitar dinámicamente estos filtros. La tabla y el histograma mostrarán las entradas de registro que cumplan la consulta y los criterios de filtro que habilite. Para obtener más información, consulte [Filtrado de registros en Kibana](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs).

## Análisis de datos mediante su visualización
{: #analyze_visualize}
    
En la página Visualizar, puede definir nuevas consultas de búsqueda y visualizaciones. También puede abrir visualizaciones guardadas o guardar una visualización.

Para analizar los datos, puede crear visualizaciones basadas en una búsqueda existente o en una búsqueda nueva. Kibana incluye distintos tipos de visualizaciones, como tabla, tendencias e histograma, que puede utilizar para analizar la información. El objetivo de cada visualización varía. Algunas visualizaciones se organizan en filas que proporcionan los resultados de una o varias consultas. Otras visualizaciones muestran documentos o información personalizada. Los datos de una visualización se pueden dejar fijos o modificar si una se actualiza una consulta de búsqueda. Puede incluir la visualización en una página web o puede compartirla. 

Para obtener más información, consulte [Análisis de registros mediante visualizaciones](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#kibana_visualizations).

## Análisis de datos en un panel de control
{: #analyze_dashboard}

En la página Panel de control, puede personalizar, guardar y compartir varias visualizaciones y búsquedas simultáneamente. 

Puede añadir, eliminar y cambiar la disposición de las visualizaciones del panel de control. Para obtener más información, consulte [Análisis de registros en Kibana mediante un panel de control](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#analize_logs_dashboard).
    
Después de personalizar un panel de control de Kibana, puede analizar los datos a través de sus visualizaciones y guardarlos para volverlos a utilizar en el futuro. Para obtener más información, consulte [Cómo guardar un panel de control de Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save).

## Personalización de Kibana
{: #analyze_management}

También puede configurar y gestionar recursos de Kibana desde la página **Gestión**. 

Puede realizar cualquiera de estas tareas:

* Guardar, suprimir, exportar e importar búsquedas. 
* Guardar, suprimir, exportar e importar visualizaciones.
* Guardar, suprimir, exportar e importar paneles de control.
* [Renovar la lista de campos.](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)

## Limitaciones
{: #limitations}

En Kibana, solo puede compartir una visualización o un panel de control con miembros de la misma organización o cuenta.

No se da soporte a las siguientes características de Kibana:

* Compartición de una búsqueda.
* Creación de nuevos patrones de índice. 


## Roles que necesita un usuario para ver registros
{: #roles}

En {{site.data.keyword.Bluemix_notm}}, puede asignar uno o varios roles a los usuarios. Estos roles definen qué tareas están habilitadas para dicho usuario para trabajar con el servicio de {{site.data.keyword.loganalysisshort}}. 

Las tablas siguientes muestran los roles que debe tener un usuario para ver registros:

<table>
  <caption>Permisos que necesita un **propietario de cuenta** para ver registros</caption>
  <tr>
    <th>Acción</th>
	<th>Roles de espacio de CF</th>
	<th>Roles de organización de CF</th>
	<th>Roles de IAM</th>
  </tr>
  <tr>
    <td>Ver registros en un dominio del espacio</td>
	<td>*Gestor* </br>*Desarrollador* </br>*Auditor*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Ver registros en el dominio de la cuenta</td>
	<td></td>
	<td></td>
	<td>*Administrador*</td>
  </tr>
  <tr>
    <td>Ver registros en un dominio de la organización</td>
	<td></td>
	<td>*Gestor* </br>*Gestor de facturación*  </br>*Auditor*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Permisos que necesita un **auditor** para ver registros</caption>
  <tr>
    <th>Acción</th>
	<th>Roles de espacio de CF</th>
	<th>Roles de organización de CF</th>
	<th>Roles de IAM</th>
  </tr>
  <tr>
    <td>Ver registros en un dominio del espacio</td>
	<td>*Auditor*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Ver registros en el dominio de la cuenta</td>
	<td></td>
	<td></td>
	<td>*Visor*</td>
  </tr>
  <tr>
    <td>Ver registros en un dominio de la organización</td>
	<td></td>
	<td>*Auditor*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Permisos que necesita un **administrador** para ver registros</caption>
  <tr>
    <th>Acción</th>
	<th>Roles de espacio de CF</th>
	<th>Roles de organización de CF</th>
	<th>Roles de IAM</th>
  </tr>
  <tr>
    <td>Ver registros en un dominio del espacio</td>
	<td>*Desarrollador*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Ver registros en el dominio de la cuenta</td>
	<td></td>
	<td></td>
	<td>*Visor*</td>
  </tr>
  <tr>
    <td>Ver registros en un dominio de la organización</td>
	<td></td>
	<td>*Gestor*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>Permisos que necesita un **desarrollador** para ver registros</caption>
  <tr>
    <th>Acción</th>
	<th>Roles de espacio de CF</th>
	<th>Roles de organización de CF</th>
	<th>Roles de IAM</th>
  </tr>
  <tr>
    <td>Ver registros en un dominio del espacio</td>
	<td>*Desarrollador*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>Ver registros en el dominio de la cuenta</td>
	<td></td>
	<td></td>
	<td>*Visor*</td>
  </tr>
  <tr>
    <td>Ver registros en un dominio de la organización</td>
	<td></td>
	<td>*Auditor*</td>
	<td></td>
  </tr>
</table>



## URL para lanzar Kibana
{: #urls_kibana}

En la tabla siguiente se muestran los URL para iniciar Kibana y las versiones de Kibana por región:

<table>
    <caption>URL para lanzar Kibana</caption>
    <tr>
      <th>Región</th>
      <th>URL</th>
      <th>Versión de Kibana</th>
    </tr>
	<tr>
      <td>Frankfurt</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>Sídney</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>Reino Unido</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
    <tr>
      <td>EE.UU. sur</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
</table>




