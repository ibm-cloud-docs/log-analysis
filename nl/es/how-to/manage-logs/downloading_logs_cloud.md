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

# Descarga de registros
{: #downloading_logs}

Puede descargar registros en un archivo local o dirigir los datos a otro programa. Los registros se descargan dentro del contexto de una sesión. Una sesión especifica qué registros se descargarán. Si la descarga de los registros se interrumpe, la sesión permite reanudar la descarga desde donde se quedó. Una vez finalizada la descarga, debe suprimir la sesión.
{:shortdesc}

Para completar los pasos, debe instalar la CLI de {{site.data.keyword.loganalysisshort}}. Para obtener más información, consulte [Configuración de la CLI de {{site.data.keyword.loganalysisshort}}](https://console.bluemix.net/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli_).


Siga estos pasos para descargar datos de registro disponibles en un espacio en un archivo local:

## Paso 1: Iniciar sesión en {{site.data.keyword.Bluemix_notm}}
{: #downloading_logs_step1}

Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

## Paso 2: Identificar los registros disponibles
{: #step21}

1. Utilice el mandato `ibmcloud logging log-show` para ver qué registros están disponibles durante las 2 últimas semanas. Ejecute el mandato siguiente:

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Por ejemplo, el resultado de ejecutar este mandato es:
    
    ```
    ibmcloud logging log-show 
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-16   794008   706     All          syslog, default   
	2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}

    **Nota:** El servicio {{site.data.keyword.loganalysisshort}} es un servicio global que utiliza la Hora universal coordinada (UTC). Los días se definen como días UTC. Para obtener los registros correspondientes a un día y hora local específicos, puede que tenga que descargar varios días UTC.


## Paso 3: Crear una sesión
{: #step3}

Se necesita una sesión para definir el ámbito de datos de registro que están disponibles para una descarga y para mantener el estado de la descarga. 

Utilice el mandato [ibmcloud logging session-create](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_create) para crear una sesión. Si lo desea, puede especificar fecha de inicio, fecha final y tipos de registros cuando se crea una sesión:  

* Si especifica la fecha de inicio y la fecha final, la sesión proporciona acceso a los registros entre ambas fechas inclusive. 
* Si especifica el tipo de registro (**-t**), la sesión proporciona acceso a un determinado tipo de registro. Esta es una característica importante para gestionar registros a escala, porque puede delimitar el ámbito de una sesión a un pequeño subconjunto de registros en los que está interesado.

**Nota:** Para cada sesión, puede descargar los registros de un máximo de 15 días.

Para crear una sesión que se utiliza para descargar todos los registros que están disponibles para las últimas 2 semanas, ejecute el mandato siguiente:

```
ibmcloud logging session-create 
```
{: codeblock}

La sesión devuelve la siguiente información:

* El rango de fechas que se va a descargar. El valor predeterminado es la fecha UTC actual.
* Los tipos de registro que se van a descargar. De forma predeterminada, incluye todos los tipos de registro que están disponibles para el periodo de tiempo que especifique al crear la sesión. 
* Información sobre si se debe incluir toda la cuenta o solo el espacio actual. De forma predeterminada, se obtienen registros del espacio en el que se ha iniciado la sesión.
* El ID de sesión, que se necesita para descargar registros.

Por ejemplo,

```
$ ibmcloud logging session-create
Creating session for lopezdsr@uk.ibm.com resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type
944aec4d-61f4-43d1-8f3b-c040195122da   12345678-1234-5678-abcd-378620d6fab5   2017-11-17T14:17:25.611542863Z   2017-11-17T14:17:25.611542863Z   2017-11-04   2017-11-17   ANY_TYPE
Session: 944aec4d-61f4-43d1-8f3b-c040195122da is created
```
{: screen}

**Consejo:** Para ver la lista de sesiones activas, ejecute el mandato [ibmcloud logging sessions](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_list).

## Paso 4: Descargar los datos de registro en un archivo
{: #step41}

Para descargar los registros especificados por los parámetros de sesión, ejecute el mandato siguiente:

```
ibmcloud logging log-download -o Log_File_Name Session_ID
```
{: codeblock}

donde

* Log_File_Name es el nombre del archivo de salida.
* Session_ID es el GUID de la sesión. Este valor se obtiene en el paso anterior.

Por ejemplo,

```
ibmcloud logging log-download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

El indicador de progreso pasa de 0 a 100% a medida que se descargan los registros.

**Nota:** 

* El formato de los datos descargados es JSON comprimido. Si descomprime el archivo .gz y lo abre, verá los datos en formato JSON. 
* El archivo JSON comprimido resulta adecuado para ingestión por parte de ElasticSearch o Logstash. Si no se especifica -o, los datos se direccionarán a la salida estándar, stdout, para que los pueda dirigir directamente a su propia pila ELK.
* También puede procesar los datos con cualquier programa que pueda analizar JSON. 

## Paso 5: Suprimir la sesión
{: #step5}

Una vez finalizada la descarga, debe suprimir la sesión mediante el mandato [ibmcloud logging session delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete). 

Ejecute el siguiente mandato para suprimir una sesión:

```
ibmcloud logging session-delete Session_ID
```
{: codeblock}

Donde Session_ID es el GUID de la sesión que ha creado en un paso anterior.

Por ejemplo,

```
ibmcloud logging session-delete -jshdjsunelsssr4566722==
Deleting session: -jshdjsunelsssr4566722== of resource: 12345678-1234-5678-abcd-378620d6fab5 ...
Session: -jshdjsunelsssr4566722== is deleted

```
{: screen}




