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
{: #downloading_logs1}

Puede descargar registros en un archivo local o dirigir los datos a otro programa. Los registros se descargan dentro del contexto de una sesión. Una sesión especifica qué registros se descargarán. Si la descarga de los registros se interrumpe, la sesión permite reanudar la descarga desde donde se quedó. Una vez finalizada la descarga, debe suprimir la sesión.
{:shortdesc}

Siga estos pasos para descargar datos de registro disponibles en un espacio de {{site.data.keyword.Bluemix_notm}} en un archivo local:

## Paso 1: Iniciar sesión en IBM Cloud

Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

## Paso 2: Identificar los registros disponibles
{: #step31}

1. Utilice el mandato `ibmcloud cf logging status` para ver qué registros están disponibles durante las 2 últimas semanas. Ejecute el mandato siguiente:

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Por ejemplo, el resultado de ejecutar este mandato es:
    
    ```
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}

    **Nota:** El servicio {{site.data.keyword.loganalysisshort}} es un servicio global que utiliza la Hora universal coordinada (UTC). Los días se definen como días UTC. Para obtener los registros correspondientes a un día y hora local específicos, puede que tenga que descargar varios días UTC.


## Paso 3: Crear una sesión
{: #step32}

Se necesita una sesión para definir el ámbito de datos de registro que están disponibles para una descarga y para mantener el estado de la descarga. 

Utilice el mandato [cf logging session create](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) para crear una sesión. Si lo desea, puede especificar fecha de inicio, fecha final y tipos de registros cuando se crea una sesión:  

* Si especifica la fecha de inicio y la fecha final, la sesión proporciona acceso a los registros entre ambas fechas inclusive. 
* Si especifica el tipo de registro (**-t**), la sesión proporciona acceso a un determinado tipo de registro. Esta es una característica importante para gestionar registros a escala, porque puede delimitar el ámbito de una sesión a un pequeño subconjunto de registros en los que está interesado.

**Nota:** Para cada sesión, puede descargar los registros de un máximo de 15 días.

Para crear una sesión que se utilice para descargar los registros de tipo *log*, ejecute el mandato siguiente:

```
ibmcloud cf logging session create -t log
```
{: codeblock}

La sesión devuelve la siguiente información:

* El rango de fechas que se va a descargar. El valor predeterminado es la fecha UTC actual.
* Los tipos de registro que se van a descargar. De forma predeterminada, incluye todos los tipos de registro que están disponibles para el periodo de tiempo que especifique al crear la sesión. 
* Información sobre si se debe incluir toda la cuenta o solo el espacio actual. De forma predeterminada, se obtienen registros del espacio en el que se ha iniciado la sesión.
* El ID de sesión, que se necesita para descargar registros.

Por ejemplo,

```
$ ibmcloud cf logging session create -t log     
+--------------+--------------------------------------+
|     NAME     |                VALUE                 |
+--------------+--------------------------------------+
| Access-Time  | 2017-05-25T18:04:21.743792338Z       |
| Create-Time  | 2017-05-25T18:04:21.743792338Z       |
| Date-Range   | {                                    |
|              |  "End": "2017-05-25T00:00:00Z",      |
|              |  "Start": "2017-05-25T00:00:00Z"     |
|              | }                                    |
| Id           | -jshdjsunelsssr4566722==             |
| Space        | fdgrghg3-b090-4567-vvfg-afbc436902a3 |
| Type-Account | {                                    |
|              |  "Type": "log"                       |
|              | }                                    |
| Username     | xxx@yyy.com                          |
+--------------+--------------------------------------+
```
{: screen}

**Consejo:** Para ver la lista de sesiones activas, ejecute el mandato [cf logging session list](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_list1).

## Paso 4: Descargar los datos de registro en un archivo
{: #step42}

Para descargar los registros especificados por los parámetros de sesión, ejecute el mandato siguiente:

```
ibmcloud cf logging download -o Log_File_Name Session_ID
```
{: codeblock}

donde

* Log_File_Name es el nombre del archivo de salida.
* Session_ID es el GUID de la sesión. Este valor se obtiene en el paso anterior.

Por ejemplo,

```
ibmcloud cf logging download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

El indicador de progreso pasa de 0 a 100% a medida que se descargan los registros.

**Nota:** 

* El formato de los datos descargados es JSON comprimido. Si descomprime el archivo .gz y lo abre, verá los datos en formato JSON. 
* El archivo JSON comprimido resulta adecuado para ingestión por parte de ElasticSearch o Logstash. Si no se especifica -o, los datos se direccionarán a la salida estándar, stdout, para que los pueda dirigir directamente a su propia pila ELK.
* También puede procesar los datos con cualquier programa que pueda analizar JSON. 

## Paso 5: Suprimir la sesión
{: #step51}

Una vez finalizada la descarga, debe suprimir la sesión mediante el mandato [cf logging session delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_delete1). 

Ejecute el siguiente mandato para suprimir una sesión:

```
ibmcloud cf logging session delete Session_ID
```
{: codeblock}

Donde Session_ID es el GUID de la sesión que ha creado en un paso anterior.

Por ejemplo,

```
ibmcloud cf logging session delete -jshdjsunelsssr4566722==
+---------+------------------------+
|  NAME   |         VALUE          |
+---------+------------------------+
| Message | Delete session success |
+---------+------------------------+
```
{: screen}




