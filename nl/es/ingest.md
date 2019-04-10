---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

subcollection: LogDNA

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

 
# Envío de registros
{: #ingest}

Puede enviar datos de registro a una instancia de {{site.data.keyword.la_full_notm}}. 
{:shortdesc}

Realice los pasos siguientes para enviar registros mediante programación:

## Paso 1. Obtener la clave de API de ingestión 
{: #ingest_step1}

**Nota:** debe tener el rol **gestor** para el servicio o la instancia de {{site.data.keyword.la_full_notm}} para poder completar este paso. Para obtener más información, consulte [Cómo otorgar permisos para gestionar registros y configurar alertas en LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

Realice los pasos siguientes para obtener la clave de ingestión:
    
1. Inicie la interfaz de usuario web de {{site.data.keyword.la_full_notm}}. Para obtener más información, consulte [Ir a la interfaz de usuario web de {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleccione el icono **Configuración** ![Icono Configuración](images/admin.png). A continuación, seleccione **Organización**. 

3. Seleccione **Claves de API**.

    Puede ver las claves de ingestión que se han creado. 

4. Utilice una clave de ingestión existente o pulse **Generar clave de ingestión** para crear una nueva.

    Se añade una nueva clave a la lista. Copie la clave.


## Paso 2. Enviar registros
{: #ingest_step2}

Para enviar registros, ejecute el mandato cURL siguiente:

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

Donde 

* ENDPOINT representa el punto de entrada al servicio. Cada región tiene un URL diferente.
* QUERY_PARAMETERS son parámetros que definen los criterios de filtro que se aplican a la solicitud de ingestión.
* LOG_LINES describe el conjunto de líneas de registro que desea enviar. Se define como una matriz de objetos.
* INGESTION_KEY es la clave que ha creado en el paso anterior.

En la tabla siguiente se muestran los puntos finales por cada región:

| Región         | Punto final                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="Puntos finales por región" caption-side="top"} 


En la tabla siguiente, se muestran los parámetros de consulta:

| Parámetro de consulta | Tipo       | Estado     | Descripción |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | necesario   | Nombre de host del origen. |
| `mac`           | `string`     | opcional   | Dirección MAC de red del sistema host.    |
| `ip`            | `string`     | opcional   | Dirección IP local del sistema host.  | 
| `now`           | `date-time`  | opcional   | Indicación de fecha y hora UNIX de origen en milisegundos en el momento de la solicitud. Se utiliza para calcular la desviación de tiempo.|
| `tags`          | `string`     | opcional   | Etiquetas utilizadas para agrupar hosts de forma dinámica. |
{: caption="Parámetros de consulta" caption-side="top"} 



En la tabla siguiente se muestran los datos necesarios por cada línea de registro:

| Parámetros     | Tipo       | Descripción                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | Indicación de fecha y hora de UNIX, en milisegundos, del momento en que se registró la entrada de registro.       | 
| `line`           | `string`     | Texto de la línea de registro.                                     |
| `app`            | `string`     | Nombre de la aplicación que genera la línea de registro.  |
| `level`          | `string`     | Establezca un valor para el nivel. Por ejemplo, los valores de ejemplo para este parámetro son `INFO`, `WARNING`, `ERROR`. |
| `meta`           |            | Este campo está reservado a información personalizada asociada con una línea de registro. Para añadir metadatos a una llamada de API, especifique el campo meta bajo el objeto de líneas. Los metadatos se pueden visualizar dentro del contexto de dicha línea.                      |
{: caption="Campos de objeto de línea" caption-side="top"} 

Por ejemplo, el ejemplo siguiente muestra el JSON para una línea de registro que desea ingerir:

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00,
      "line":"This is my first log line.",
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## Ejemplo
{: #ingest_example}

El ejemplo siguiente muestra el mandato cURL para enviar una línea de registro a una instancia del servicio {{site.data.keyword.la_full_notm}}: 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

