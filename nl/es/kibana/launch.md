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


# Navegación al panel de control de Kibana
{: #launch}

Puede iniciar Kibana desde el servicio {{site.data.keyword.loganalysisshort}}, desde la interfaz de usuario de {{site.data.keyword.Bluemix}} o directamente desde un navegador web.
{:shortdesc}

Para las apps de CF y los contenedores Docker, puede iniciar Kibana desde la IU de {{site.data.keyword.Bluemix_notm}} para ver y analizar datos en el contexto del recurso desde el que inicia Kibana. Por ejemplo, puede iniciar los registros específicos de la app CF en Kibana, en el contexto de la app específica.
    
Para cualquier recurso de nube, como un contenedor Docker desplegado en una infraestructura de Kubernetes, puede iniciar Kibana desde un enlace directo de navegador o desde el panel de control del servicio {{site.data.keyword.loganalysisshort}} si desea ver datos de registros agregados desde los servicios dentro de un espacio concreto. La consulta que se utiliza para filtrar los datos que aparecen en el panel de control recupera las entradas de registro correspondientes a un espacio de la organización. La información de registro que muestra Kibana incluye registros correspondientes a todos los recursos desplegados dentro del espacio de la organización en la que ha iniciado la sesión. 

En la siguiente tabla se muestran algunos recursos de nube y métodos de navegación soportados para iniciar Kibana:

<table>
<caption>Tabla 1. Lista de los recursos y métodos de navegación soportados. </caption>
  <tr>
    <th>Recurso</th>
	<th>Navegación al panel de control de Kibana desde el panel de control del servicio {{site.data.keyword.loganalysisshort}}</th>
    <th>Navegación al panel de control de Kibana desde el panel de control de Bluemix</th>
    <th>Navegación al panel de control de Kibana desde un navegador web</th>
  </tr>
  <tr>
    <td>App CF</td>
	<td>Sí</td>
    <td>Sí</td>
    <td>Sí</td>
  </tr>  
  <tr>
    <td>Contenedor desplegado en un clúster de Kubernetes</td>
	<td>Sí</td>
    <td>Sí</td>
    <td>Sí</td>
  </tr>  
  <tr>
    <td>Contenedor desplegado en una infraestructura gestionada por {{site.data.keyword.Bluemix_notm}} (en desuso)</td>
	<td>Sí</td>
    <td>Sí</td>
    <td>Sí</td>
  </tr>  
</table>

Para obtener más información sobre Kibana, consulte la [Guía del usuario de Kibana ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.
    

##  Navegación a Kibana desde el panel de control del servicio Análisis de registros
{: #launch_Kibana_from_log_analysis}

La consulta que se utiliza para filtrar los datos que aparecen en Kibana recupera las entradas de registro correspondientes a ese espacio de la organización. 
	
La información de registro que muestra Kibana incluye registros correspondientes a todos los recursos desplegados dentro del espacio de la organización en la que ha iniciado la sesión.

Siga los pasos siguientes para iniciar Kibana desde el panel de control del servicio {{site.data.keyword.loganalysisshort}}:

1. Inicie una sesión en {{site.data.keyword.Bluemix_notm}} y pulse el servicio {{site.data.keyword.loganalysisshort}} en el panel de control de {{site.data.keyword.Bluemix_notm}}. 
    
2. Seleccione el separador **Gestionado** de la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}.

3. Pulse **INICIAR**. Se abre el panel de control de Kibana.

De forma predeterminada, se carga la página **Descubrir** con el patrón de índice predeterminado seleccionado y un filtro de tiempo establecido en los últimos 15 minutos. 

Si la página Descubrir no muestra ninguna entrada de registro, ajuste el selector de tiempo. Para obtener más información, consulte [Establecimiento de un filtro de tiempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

	
	
##  Navegación a Kibana desde un navegador web
{: #launch_Kibana_from_browser}

La consulta que se utiliza para filtrar los datos que aparecen en Kibana recupera las entradas de registro correspondientes a ese espacio de la organización. 
	
La información de registro que muestra Kibana incluye registros correspondientes a todos los recursos desplegados dentro del espacio de la organización en la que ha iniciado la sesión.

Siga los pasos siguientes para iniciar Kibana desde un navegador:

1. Abra un navegador web e inicie Kibana. A continuación, inicie sesión en la interfaz de usuario de Kibana.

    Para ver la lista de URL por región, consulte [URL para iniciar Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana).
    
    Se abre la página Descubrir en Kibana.
	
2. Seleccione el patrón de índice correspondiente al espacio desde el que desea ver y analizar datos de registro.

    1. Pulse **default-index**.
	
	2. Seleccione el patrón de índice correspondiente al espacio. El formato del patrón de índice es el siguiente:
	
	    ```
	    [logstash-Space_ID-]YYYY.MM.DD 
	    ```
        {: screen}
	
	    donde *Space_ID* es el GUID del espacio en el que desea ver y analizar datos de registro. 
	
Si la página Descubrir no muestra ninguna entrada de registro, ajuste el selector de tiempo. Para obtener más información, consulte [Establecimiento de un filtro de tiempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).


	
##  Navegación a Kibana desde el panel de control de una app CF
{: #launch_Kibana_from_cf_app}

La consulta que se utiliza para filtrar los datos que aparecen en Kibana recupera las entradas de registro correspondientes a la app CF de {{site.data.keyword.Bluemix_notm}} desde la que ha iniciado Kibana.

Para ver los registros de una aplicación Cloud Foundry en Kibana, siga los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.Bluemix_notm}}.

    El panel de control de {{site.data.keyword.Bluemix_notm}} se puede encontrar en: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window}.
    
	Cuando inicia sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}.

2. Pulse el nombre de la app o el contenedor desde el panel de control de {{site.data.keyword.Bluemix_notm}}. 
    
3. Abra el separador de registro en la IU de {{site.data.keyword.Bluemix_notm}}.

    Para apps CF, pulse **Registros** en la barra de navegación. 
    Se abre el separador Registros.  

4. Pulse **Ver en Kibana**. Se abre el panel de control de Kibana.

    De forma predeterminada, se carga la página **Descubrir** con el patrón de índice predeterminado seleccionado y un filtro de tiempo establecido en los últimos 15 minutos. La consulta de búsqueda está establecida para que coincida con todas las entradas de la app CF.

    Si la página Descubrir no muestra ninguna entrada de registro, ajuste el selector de tiempo. Para obtener más información, consulte [Establecimiento de un filtro de tiempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

	
	
##  Navegación a Kibana desde el panel de control de un contenedor desplegado en un clúster de Kubernetes
{: #launch_Kibana_for_containers_kube}

La consulta que se utiliza para filtrar los datos que aparecen en Kibana recupera las entradas de registro correspondientes al clúster desde el que ha iniciado Kibana.

Para ver los registros de un contenedor en Kibana, siga los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.Bluemix_notm}}.

    El panel de control de {{site.data.keyword.Bluemix_notm}} se puede encontrar en: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window}.
    
	Cuando inicia sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}.

2. En el menú, seleccione **Panel de control**.

3. En la sección *Clústeres*, seleccione el clúster.

4. En la sección *Visión general*, seleccione **Ver registros**.

    Se abre Kibana.




##  Navegación a Kibana desde el panel de control de un contenedor desplegado en la infraestructura gestionada por {{site.data.keyword.Bluemix_notm}} (en desuso)
{: #launch_Kibana_for_containers}

Este método únicamente se aplica a contenedores desplegados en la infraestructura gestionada por {{site.data.keyword.Bluemix_notm}}.

La consulta que se utiliza para filtrar los datos que aparecen en Kibana recupera las entradas de registro correspondientes al contenedor desde el que ha iniciado Kibana.

Para ver los registros de un contenedor Docker en Kibana, siga los pasos siguientes:

1. Inicie una sesión en {{site.data.keyword.Bluemix_notm}} y pulse el contenedor en el panel de control de {{site.data.keyword.Bluemix_notm}}. 
    
2. Abra el separador de registro en la IU de {{site.data.keyword.Bluemix_notm}}.

    Para contenedores desplegados en la infraestructura gestionada por {{site.data.keyword.IBM_notm}}, seleccione **Supervisión y registros** en la barra de navegación y pulse el separador **Registro**. 
    
    Se abre el separador Registros.  

3. Pulse **Vista avanzada**. Se abre el panel de control de Kibana.

    De forma predeterminada, se carga la página **Descubrir** con el patrón de índice predeterminado seleccionado y un filtro de tiempo establecido en los últimos 30 segundos. La consulta de búsqueda está establecida de modo que coincide con todas las entradas correspondientes al contenedor Docker.

    Si la página Descubrir no muestra ninguna entrada de registro, ajuste el selector de tiempo. Para obtener más información, consulte [Establecimiento de un filtro de tiempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

	



