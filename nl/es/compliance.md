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


# Conformidad
{: #compliance}

[{{site.data.keyword.Bluemix}} ofrece una plataforma de nube y servicio basados en los estrictos estándares de seguridad de IBM.](/docs/security/compliance.html#compliance). El servicio {{site.data.keyword.loganalysislong}} es un servicio de DevOps creado para {{site.data.keyword.Bluemix_notm}}. 
{:shortdesc}


## Reglamento General de Protección de Datos

El Reglamento General de Protección de Datos (GDPR) busca crear un marco jurídico armonizado de protección de datos en la Unión Europea y tiene como objetivo devolver a los ciudadanos el control de sus datos personales, imponiendo reglas estrictas sobre los que albergan y 'procesan' sus datos, en cualquier lugar del mundo. El reglamento también presenta reglas referentes a la libre circulación de datos personales dentro y fuera de la Unión Europea. 

**Declaración de limitación de responsabilidad:** El servicio {{site.data.keyword.loganalysisshort}} almacena y muestra registros procedentes de recursos de la nube que se ejecutan en la cuenta del usuario en {{site.data.keyword.Bluemix_notm}} y de registros que el usuario envía desde fuera de {{site.data.keyword.Bluemix_notm}}. No se debe incluir información personal (PI) en ninguna de las entradas de registro almacenadas en {{site.data.keyword.loganalysisshort}}, ya que estos datos resultan accesibles para otros usuarios de la empresa así como para {{site.data.keyword.IBM_notm}} a fin de poder dar servicio técnico al servicio de nube.

### Regiones
{: #regions}

El servicio {{site.data.keyword.loganalysisshort}} cumple el GDPR en las regiones de {{site.data.keyword.Bluemix_notm}} públicas en las que está disponible.


### Retención de datos
{: #data_retention}

El servicio {{site.data.keyword.loganalysisshort}} incluye 2 repositorios de datos donde se pueden almacenar los datos: 

* Búsqueda de registros, que alberga los datos de registro que están disponibles para su análisis mediante Kibana.
* Recopilación de registros, que alberga los datos de registro para su almacenamiento a largo plazo.

En función del plan de servicio de {{site.data.keyword.loganalysisshort}}, los datos se guardan en búsqueda de registros o en búsqueda de registro y en recopilación de registros. El plan estándar y el plan lite solo guardan los datos en búsqueda de registros. El resto de los planes guardan los datos en búsqueda de registros y en recopilación de registros.

* Los registros que se almacenan en búsqueda de registros se conservan durante 3 días.
* Los registros que se almacenan en el componente de recopilación de registros se conservan hasta que el usuario configura una política de retención o hasta que los suprime manualmente. De forma predeterminada, los registros se conservan indefinidamente en el componente de recopilación de registros.



### Supresión de datos
{: #data_deletion}

Considere la siguiente información:

* Los registros que se almacenan en búsqueda de registros se suprimen transcurridos 3 días.

* Los registros que se almacenan en el componente de recopilación de registros se suprimen transcurridos un cierto número de días cuando se configura una política de retención o se conservan hasta que el usuario los suprime manualmente. 

    Puede configurar una política de retención de registros para definir el número de días que desea conservar los registros en la recopilación de registros. Para obtener más información, consulte [Visualización y configuración de la política de retención de registros mediante el plugin de {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy).

    Puede utilizar la [API de recopilación de registros](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} o la [CLI de recopilación de registros](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window} para suprimir registros manualmente del componente de recopilación de registros. 

    Puede utilizar la CLI para suprimir registros manualmente del componente de recopilación de registros. Para obtener más información, consulte [ibmcloud logging log-delete mediante el plugin de {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs).


Si pasa de un plan de pago al plan lite o estándar, los registros de la recopilación de registros se suprimirán en un día aproximadamente.

En cualquier momento, puede abrir una incidencia de soporte y pedir que todos sus datos se supriman del componente de búsqueda de registros o de recopilación de registros. Para obtener información sobre cómo abrir una incidencia de soporte de IBM, consulte [Cómo obtener soporte](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support).



### Más información
{: #info}

Para obtener más información, consulte:

[Conformidad de seguridad de {{site.data.keyword.Bluemix_notm}}](/docs/security/compliance.html#compliance)

[GDPR - Página oficial de {{site.data.keyword.IBM_notm}}](https://www.ibm.com/data-responsibility/gdpr/)



