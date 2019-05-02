---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# Exportación de registros a un archivo local
{: #export}

Puede exportar datos de registro en formato JSONL de una instancia de {{site.data.keyword.la_full_notm}} a un archivo local. Puede exportar registros mediante programación o desde la interfaz de usuario web de IBM Log Analysis. 
{:shortdesc}

Tenga en cuenta la información siguiente al exportar datos de registro:
* Exporte un conjunto de entradas de registro. Para definir el conjunto de datos que desea exportar, puede aplicar filtros y búsquedas. También puede especificar el intervalo de tiempo. 
* Desde la interfaz de usuario web, al exportar registros, recibe un correo electrónico enviado a su dirección de correo electrónico, con un enlace a un archivo comprimido que incluye los datos. Para obtener los datos, debe pulsar en enlace y descargar el archivo comprimido.
* Al exportar registros mediante programación, puede elegir enviar un correo electrónico o transmitir los registros a su terminal.
* El archivo de registro comprimido que contiene los datos que desea exportar está disponible durante un máximo de 48 horas. 
* El número máximo de líneas que puede exportar es de 10 000.



## Exportación de registros desde la interfaz de usuario web
{: #ui}

Realice los pasos siguientes para exportar datos de registro:

1. Pulse el icono **Vistas** ![Icono Configuración](images/views.png).
2. Seleccione **Todo** o una vista.
3. Aplique un marco de tiempo, filtros y criterios de búsqueda hasta que vea las entradas de registro que desee exportar.
4. Pulse **Vista sin guardar** si está comenzando a partir de la vista **Todo**. Pulse sobre el nombre de la vista si ha seleccionado una vista en el paso anterior.
5. Seleccione `Exportar líneas`. Se abrirá una nueva ventana.
6. Compruebe el intervalo de tiempo. Si necesita cambiarlo, pulse el intervalo de tiempo predefinido en el campo *Cambiar intervalo de tiempo de exportación*.
7. Seleccione **Preferir líneas más nuevas** o **Preferir líneas más antiguas** en caso de que la solicitud de exportación sobrepase el límite de líneas.
8. Compruebe el correo electrónico. Recibirá un correo electrónico de **LogDNA** con un enlace para descargar las líneas exportadas.


## Exportación de registros mediante programación utilizando la API
{: #api}

Realice los pasos siguientes para exportar registros mediante programación:

1. Genere una clave de servicio. 

    **Nota:** debe tener el rol **gestor** para el servicio o la instancia de {{site.data.keyword.la_full_notm}} para poder completar este paso. Para obtener más información, consulte [Cómo otorgar permisos para gestionar registros y configurar alertas en LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna).

    1. Inicie la interfaz de usuario web de {{site.data.keyword.la_full_notm}}. Para obtener más información, consulte [Ir a la interfaz de usuario web de {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

    2. Seleccione el icono **Configuración** ![Icono Configuración](images/admin.png). A continuación, seleccione **Organización**. 

    3. Seleccione **Claves de API**.

        Puede ver las claves de servicio que ha creado. 

    4. Pulse **Generar clave de servicio**.

        Se añade una nueva clave a la lista. Copie esta clave.

2. Exporte los registros. Ejecute el siguiente mandato cURL:

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    Donde 

    * ENDPOINT representa el punto de entrada al servicio. Cada región tiene un URL diferente.
    * QUERY_PARAMETERS son parámetros que definen los criterios de filtro que se aplican a la solicitud de exportación.
    * SERVICE_KEY es la clave de servicio que ha creado en el paso anterior.

En la tabla siguiente se muestran los puntos finales por cada región:

| Región         | Punto final                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com`        |
{: caption="Puntos finales por región" caption-side="top"} 


En la tabla siguiente se muestran los parámetros de consulta que puede establecer:

| Parámetro de consulta | Tipo       | Estado     | Descripción |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | Obligatorio   | Hora de inicio. Establecer como indicación de fecha y hora de UNIX en segundos o milisegundos. |
| `to`        | `int32`      | Obligatorio   | Hora de finalización. Establecer como indicación de fecha y hora de UNIX en segundos o milisegundos.    |
| `size`      | `string`     | Opcional   | Número de líneas de registro a incluir en la exportación.  | 
| `hosts`     | `string`     | Opcional   | Lista de hosts separados por comas. |
| `apps`      | `string`     | Opcional   | Lista de aplicaciones separadas por comas. |
| `levels`    | `string`     | Opcional   | Lista de niveles de registro separados por comas. |
| `query`     | `string`     | Opcional   | Consulta de búsqueda. Para obtener más información, consulte [Buscar en registros](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6). |
| `prefer`    | `string`     | Opcional   | Define las líneas de registro que desea exportar. Los valores válidos son `head`, primeras líneas de registro, y `tail`, últimas líneas de registro. Si no se especifica, el valor predeterminado será tail.  |
| `email`     | `string`     | Opcional   | Especifica el correo electrónico con el enlace descargable de la exportación. De forma predeterminada, se transmiten las líneas de registro.|
| `emailSubject` | `string`     | Opcional   | Se utiliza para establecer el asunto del correo electrónico. </br>Utilice `%20` para representar un espacio. Un valor de ejemplo es `Export%20logs`. |
{: caption="Parámetros de consulta" caption-side="top"} 

Por ejemplo, para transmitir líneas de registro en el terminal, puede ejecutar el mandato siguiente:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

Para enviar un correo electrónico con el enlace para descargar las líneas de registro especificadas en la exportación, puede ejecutar el mandato siguiente:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


Para enviar un correo electrónico con un asunto personalizado, puede ejecutar el mandato siguiente:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

