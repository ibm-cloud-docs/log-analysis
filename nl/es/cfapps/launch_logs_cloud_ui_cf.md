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

# Navegación a los registros de una app Cloud Foundry
{: #launch_logs_cloud_ui_cf}

En la IU de {{site.data.keyword.Bluemix}}, puede ver, filtrar y analizar registros desde el separador de registro disponible para cada app de Cloud Foundry o mediante la IU del servicio {{site.data.keyword.loganalysisshort}}.
{:shortdesc}

Para ver registros de las apps de CF, tenga en cuenta la siguiente información: 

<table>
  <caption>Información sobre registros de apps de CF en {{site.data.keyword.Bluemix_notm}}</caption>
  <tr>
    <th>Opciones de la IU</th>
    <th>Información</th>
  </tr>
  <tr>
    <td>Separador de registro disponible en la IU de las apps de CF </td>
    <td>Los registros que están disponibles para su análisis incluyen datos correspondientes a las últimas 24 horas.</td>
  </tr>
  <tr>
    <td>Panel de control de {{site.data.keyword.loganalysisshort}} (Kibana)</td>
    <td>Los registros que están disponibles para su análisis incluyen datos correspondientes a los últimos 3 días. También puede especificar un periodo personalizado.</td>
  </tr>
</table>


## Navegación por los registros de una app de CF mediante el panel de control de app de CF 
{: #cfapp_ui}

Para ver los registros de despliegue o de tiempo de ejecución de una app Cloud Foundry, siga los pasos siguientes:

1. En el panel de control Apps, pulse el nombre de su app Cloud Foundry. 
    
2. En la página de detalles de la app, pulse **Registros**.
    
    En el separador **Registros**, puede ver los registros recientes de la app o la parte más reciente de los registros en tiempo real. Además, puede filtrar registros por componente (tipo de registro), por ID de instancia de la app y por error.
    
De forma predeterminada, los registros que están disponibles para su análisis desde la consola de {{site.data.keyword.Bluemix_notm}} incluyen datos correspondientes a las últimas 24 horas.


## Navegación por los registros de una app de CF mediante la IU de {{site.data.keyword.loganalysisshort}} 
{: #cfapp_la}

Para ver los registros de despliegue o de tiempo de ejecución de una app Cloud Foundry, siga los pasos siguientes:

1. En el panel de control Apps, pulse el nombre de su app Cloud Foundry. 
    
2. En la página de detalles de la app, pulse **Registros**.
    
3. Pulse **Ver en Kibana**.

De forma predeterminada, los registros que están disponibles para su análisis incluyen datos correspondientes a los últimos 15 minutos.

**Consejo:** Para analizar datos correspondientes a un periodo personalizado, consulte [Análisis avanzado de registros con Kibana](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#analyzing_logs_Kibana). 


