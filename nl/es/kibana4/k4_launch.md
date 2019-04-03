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
{: #k4_launch}

Inicie Kibana desde la interfaz de usuario de {{site.data.keyword.Bluemix}} o directamente desde un navegador web.
{:shortdesc}

Inicie Kibana desde {{site.data.keyword.Bluemix_notm}} para ver y analizar datos en el contexto del recurso desde el que inicia Kibana. Por ejemplo, puede iniciar los registros específicos de la app CF en Kibana, en el contexto de la app específica.

En la siguiente tabla se muestra una lista de los recursos y métodos de navegación soportados para iniciar Kibana:

<table>
<caption>Tabla 1. Lista de los recursos y métodos de navegación soportados. </caption>
  <tr>
    <th>Recurso</th>
    <th>Navegación al panel de control de Kibana desde el panel de control de Bluemix</th>
    <th>Navegación al panel de control de Kibana desde un navegador web</th>
  <tr>
  <tr>
    <td>App CF</td>
    <td>Sí</td>
    <td>Sí</td>
  <tr>  
  <tr>
    <td>Contenedor desplegado en un clúster Kubernetes</td>
    <td>Sí</td>
    <td>Sí</td>
  <tr>  
</table>

Para obtener más información sobre Kibana, consulte la [Guía del usuario de Kibana ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}.
    

##  Navegación al panel de control de Kibana desde el panel de control de Bluemix
{: #launch_Kibana_from_bluemix}

La consulta que se utiliza para filtrar los datos que aparecen en Kibana recupera las entradas de registro correspondientes a la app CF de {{site.data.keyword.Bluemix_notm}} o contenedor desde el que ha iniciado Kibana.

Para ver los registros de una aplicación Cloud Foundry o de un contenedor Docker en Kibana, siga los pasos siguientes:

1. Inicie una sesión en {{site.data.keyword.Bluemix_notm}} y pulse el nombre de la app o el contenedor en el panel de control de {{site.data.keyword.Bluemix_notm}}. 
    
2. Abra el separador de registro en la IU de {{site.data.keyword.Bluemix_notm}}.

    * Para apps CF, pulse **Registros** en la barra de navegación. 
    * Para contenedores desplegados en la infraestructura gestionada por {{site.data.keyword.Bluemix_notm}}, seleccione **Supervisión y registros** en la barra de navegación y pulse el separador **Registro**. 
    
        Se abre el separador Registros.  

3. Pulse **Vista avanzada**. Se abre el panel de control de Kibana.

    De forma predeterminada, se carga la página **Descubrir** con el patrón de índice predeterminado seleccionado y un filtro de tiempo establecido en los últimos 30 segundos. La consulta de búsqueda está establecida para que coincida con todas las entradas de la app CF o el contenedor Docker.

    Si la página Descubrir no muestra ninguna entrada de registro, ajuste el selector de tiempo. 


##  Navegación al panel de control de Kibana desde un navegador web
{: #launch_Kibana_from_browser1}

La consulta que se utiliza para filtrar los datos que aparecen en Kibana recupera las entradas de registro correspondientes a un espacio de la organización {{site.data.keyword.Bluemix_notm}}. La información de registro que muestra Kibana incluye registros correspondientes a todos los recursos desplegados dentro del espacio de la organización {{site.data.keyword.Bluemix_notm}} en la que ha iniciado la sesión.

Complete el siguiente paso para iniciar Kibana desde un navegador:

1. Inicie la interfaz de usuario de Kibana.
    
    Por ejemplo, 
      
        <table>
          <caption>Tabla 1. URL para iniciar Kibana  </caption>
           <tr>
            <th>Región</th>
            <th>URL</th>
          </tr>
          <tr>
            <td>EE.UU. sur</td>
            <td>https://logging.ng.bluemix.net/ </td>
          </tr>
          <tr>
            <td>Reino Unido</td>
            <td>https://logging.eu-gb.bluemix.net/ </td>
          </tr>
        </table>

    Si la página Descubrir no muestra ninguna entrada de registro, ajuste el selector de tiempo. 

