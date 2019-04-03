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


# Envío de registros desde fuera de {{site.data.keyword.Bluemix_notm}}
{: #log_ingestion}

Puede enviar registros desde fuera de {{site.data.keyword.IBM_notm}} Cloud al servicio {{site.data.keyword.loganalysisshort}} utilizando el servicio Logstash Forwarder multiarrendatario. 
{:shortdesc}

Esta característica solo está disponible para los planes de servicio que permiten la ingestión de registros. Para obtener más información, consulte [Planes de servicio](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

Para enviar registros desde fuera de {{site.data.keyword.IBM_notm}} Cloud al servicio {{site.data.keyword.loganalysisshort}}, necesita los siguientes recursos de nube:

* Un ID de {{site.data.keyword.IBM_notm}} para iniciar una sesión en {{site.data.keyword.Bluemix_notm}}. Este ID de usuario debe tener permisos para trabajar con el servicio {{site.data.keyword.loganalysisshort}} en un espacio en {{site.data.keyword.Bluemix_notm}}. El espacio es el dominio de {{site.data.keyword.Bluemix_notm}} donde piensa enviar y analizar los registros.
* Una señal de registro que se genera mediante la CLI de {{site.data.keyword.loganalysisshort}} y que se utiliza para autenticar el entorno local con el servicio {{site.data.keyword.loganalysisshort}}.  

En el entorno local, debe configurar mt-logstash-forwarder y especificar los archivos de registro que desea enviar al servicio {{site.data.keyword.loganalysisshort}}.

Para obtener más información sobre cómo configurar el entorno local para que envíe registros al servicio {{site.data.keyword.loganalysisshort}}, consulte [Envío de datos locales a un espacio en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt).



## URL de ingestión
{: #log_ingestion_urls}

En la tabla siguiente se muestran los URL que debe utilizar para enviar registros a {{site.data.keyword.Bluemix_notm}}:

<table>
  <caption>URL de ingestión</caption>
    <tr>
      <th>Región</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>Alemania</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Sídney</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Reino Unido</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>EE.UU. sur</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


