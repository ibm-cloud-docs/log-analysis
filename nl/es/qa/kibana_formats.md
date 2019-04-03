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

# Formatos de registro de Kibana
{: #kibana_formats}

Puede configurar Kibana para que visualice en la página *Descubrir* distintos campos para cada entrada de registro.
{:shortdesc}



## Formato de registro de Kibana para aplicaciones de Cloud Foundry
{: #kibana_log_format_cf}

Puede configurar Kibana para que muestre los campos siguientes para cada entrada de registro en la página *Descubrir*:

| Campo | Descripción |
|-------|-------------|
| @timestamp | `aaaa-MM-ddTHH:mm:ss:SS-0500`  <br> La hora del suceso registrado. <br> La indicación de fecha y hora se define hasta en milisegundos. |
| @version | Versión del suceso. |
| ALCH_TENANT_ID | ID del espacio de {{site.data.keyword.Bluemix_notm}}. |
| \_id | El ID exclusivo del documento de registro. |
| \_index | El índice de la entrada de registro. |
| \_type | El tipo de registro; por ejemplo, *syslog*. |
| nombre_app | El nombre de la aplicación. |
| application_id | El ID exclusivo de la aplicación. |
| host | El nombre de la aplicación que ha generado los datos del registro. |
| instance_id | El ID de instancia de la instancia de aplicación que ha generado los datos de registro. |
| loglevel | La gravedad del suceso registrado. |
| message | Mensaje emitido por el componente. <br> El mensaje varía en función del contexto. |
| message_type | La secuencia en la que se escribe el mensaje de registro. <br> * **OUT** se refiere a la secuencia de stdout <br> * **ERR** se refiere a la secuencia de stderr. |
| org_id | El ID exclusivo de la organización de {{site.data.keyword.Bluemix_notm}} |
| org_name | El nombre de la organización de {{site.data.keyword.Bluemix_notm}} en la que se transfiere la app. |
| origin | Componente en el que se ha originado el suceso. |
| source_id | El componente que genera registros. <br> En la siguiente lista se describen los registros de cada componente: <br> * **API**: Respuestas registradas a llamadas de API que solicitan un cambio en el estado de la app. <br> * **APP**: Respuestas registradas procedentes de la app. <br> * **CELL**: Respuestas registradas procedentes de la célula de Diego que indican cuándo se inicia, se detiene o se cuelga una app <br> * **LGR**: Respuestas registradas de loggregator que indican problemas con el proceso de registro. <br> * **RTR**: Respuestas registradas del componente direccionador cuando direcciona solicitudes HTTP a la app. <br> * **SSH**: Respuestas registradas procedentes de la célula de Diego cuando un usuario accede a un contenedor de app mediante el mandato `cf ssh`. <br> * **STG**: Respuestas registradas procedentes de la célula de Diego o de Droplet Execution Agent cuando la app se transfiere o se vuelve a transferir. |
| nombre_espacio | El nombre del espacio de {{site.data.keyword.Bluemix_notm}} en el que se transfiere la app. |
| timestamp | La hora del suceso registrado. La indicación de fecha y hora se define hasta en milisegundos. |
{: caption="Tabla 1. Campos para apps de CF" caption-side="top"}



## Formato de registro de Kibana para contenedores Docker desplegados en un clúster Kubernetes
{: #kibana_log_format_containers_kubernetes}

Puede configurar Kibana para que muestre los campos siguientes para cada entrada de registro en la página *Descubrir*. Estos campos los establece {{site.data.keyword.IBM}} e incluyen los datos de su mensaje. 

| Campo | Descripción | Información adicional |
|-------|-------------|---------------------------|
| @timestamp | `aaaa-MM-ddTHH:mm:ss:SS-0500`  <br> La hora del suceso registrado. <br> La indicación de fecha y hora se define hasta en milisegundos. | |
| @version | Versión del suceso. | |
| ALCH_TENANT_ID | ID del espacio de {{site.data.keyword.Bluemix_notm}}. | |
| \_id | El ID exclusivo del documento de registro. | |
| \_index | El índice de la entrada de registro. | |
| \_score |  |  |
| \_type | El tipo de registro; por ejemplo, *logs*. | |
| crn_str | Información sobre el origen del registro. | De forma predeterminada, este campo lo establece {{site.data.keyword.IBM_notm}}. <br> **Nota**: Si envía el mensaje de registro en un formato JSON válido, y uno de los campos se denomina `crn`, se sobrescribe el valor del campo con el valor que se establece en el mensaje.  |  
| docker.container_id_str | GUID del contenedor que se está ejecutando en un pod. | |
| ibm-containers.account_str | GUID de la cuenta de {{site.data.keyword.Bluemix_notm}}.  |  |
| ibm-containers.cluster_id_str | GUID del clúster de Kubernetes.  |  |
| ibm-containers.cluster_type_str |  | Valor reservado para uso interno de {{site.data.keyword.IBM_notm}}. |
| ibm-containers.region_str | Región en {{site.data.keyword.Bluemix_notm}}.  |  |
| kubernetes.container_name_str | Nombre del contenedor donde se despliega una app.  |  |
| kubernetes.host | Dirección IP pública del trabajador en el que se ejecuta el contenedor. |  |
| kubernetes.labels.*nombre_etiqueta_ejemplo*\_str | Pareja de clave/valor que se adjunta a un objeto Kubernetes como, por ejemplo, un pod. | Cada etiqueta que adjunta a un objeto Kubernetes aparece listada como un campo en la entrada de registro que se visualiza en Kibana. <br> Puede haber 0 o más etiquetas. |
| kubernetes.namespace_name_str | Espacio de nombres de Kubernetes donde se despliega el contenedor. |  |
| kubernetes.pod_id_str | GUID del contenedor en donde se despliega el contenedor. |  |
| kubernetes.pod_name_str | Nombre del pod. |  |
| message | Mensaje completo. | Si envía un mensaje en formato JSON válido, cada campo se analiza de forma individual y se visualiza en Kibana.  |
| stream_str |  | Valor reservado para uso interno de {{site.data.keyword.IBM_notm}}. |
|tag_str |  | Valor reservado para uso interno de {{site.data.keyword.IBM_notm}}. |
{: caption="Tabla 3. Campos para contenedores Docker" caption-side="top"}


## Formato de registro de Kibana para Message Hub
{: #kibana_log_format_messagehub}

Puede configurar Kibana para que muestre los campos siguientes para cada entrada de registro en la página *Descubrir*:

| Campo | Descripción |
|-------|-------------|
| @timestamp | `aaaa-MM-ddTHH:mm:ss:SS-0500`  <br> La hora del suceso registrado. <br> La indicación de fecha y hora se define hasta en milisegundos. |
| @version | Versión del suceso. |
| ALCH_TENANT_ID | ID del espacio de {{site.data.keyword.Bluemix_notm}}. |
| \_id | El ID exclusivo del documento de registro. |
| \_index | El índice de la entrada de registro. |
| \_type | El tipo de registro; por ejemplo, *syslog*. |
| loglevel | La gravedad del suceso registrado; por ejemplo, **Info**. |
| module | Este campo se establece en **MessageHub**. |
{: caption="Tabla 4. Campos para sucesos de Message Hub" caption-side="top"}

Ejemplo de una entrada de registro:

```
March 8th 2017, 17:15:16.454	

message:
    Creating topic ABC
@version:
    1
@timestamp:
    March 8th 2017, 17:15:16.454
loglevel:
    Info
module:
    MessageHub
ALCH_TENANT_ID:
    3d8d2eae-f3f0-44f6-9717-126113a00b51
&#95;id:
    AVqu6vJl1zcfr8KYMI95
&#95;type:
    logs
&#95;index:
    logstash-2017.03.08
```
{: screen}


