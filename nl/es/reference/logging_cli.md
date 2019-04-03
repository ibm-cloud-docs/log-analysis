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

# CLI de IBM Cloud Log Analysis (plugin CF)
{: #logging_cli}

La CLI de {{site.data.keyword.loganalysislong}} es un plugin para gestionar los registros correspondientes a los recursos de nube que se ejecutan en un espacio de una organización de {{site.data.keyword.Bluemix}}.
{: shortdesc}

**Requisitos previos**
* Antes de ejecutar mandatos de registro, inicie una sesión en {{site.data.keyword.Bluemix_notm}} con el mandato `ibmcloud login` para generar una señal de acceso de {{site.data.keyword.Bluemix_short}} y autenticar la sesión. Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

Para obtener información sobre la utilización de la interfaz de línea de mandatos de {{site.data.keyword.loganalysisshort}}, consulte [Gestión de registros](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov).

<table>
  <caption>Mandatos para gestionar registros</caption>
  <tr>
    <th>Mandato</th>
    <th>Cuándo utilizarlo</th>
  </tr>
  <tr>
    <td>[ibmcloud cf logging](#base)</td>
    <td>Utilice este mandato para obtener información sobre la CLI, como por ejemplo la versión o la lista de mandatos.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging auth](#auth)</td>
    <td>Utilice este mandato para obtener la señal de registro que puede utilizar para enviar registros al servicio {{site.data.keyword.loganalysisshort}}.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging delete](#delete)</td>
    <td>Utilice este mandato para suprimir los registros almacenados en el componente de recopilación de registros.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging download (Beta)](#download)</td>
    <td>Utilice este mandato para descargar de la recopilación de registros en un archivo local, o para direccionar los registros a otro programa, como por ejemplo Elastic Stack. </td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging help](#help)</td>
    <td>Utilice este mandato para obtener ayuda sobre cómo utilizar la CLI y una lista de todos los mandatos.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging option](#option)</td>
    <td>Utilice este mandato para ver o definir el periodo de retención para los registros que están disponibles en un espacio o una cuenta.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging session create (Beta)](#session_create1)</td>
    <td>Utilice este mandato para crear una nueva sesión.</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete (Beta)](#session_delete1)</td>
    <td>Utilice este mandato para suprimir una sesión.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session list (Beta)](#session_list1)</td>
    <td>Utilice este mandato para obtener una lista de las sesiones activas y sus ID.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session show (Beta)](#session_show1)</td>
    <td>Utilice este mandato para ver el estado de una sesión individual.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging status](#status1)</td>
    <td>Utilice este mandato para obtener información sobre los registros que se han recopilado en un espacio o cuenta.</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

Proporciona información sobre la versión de la CLI y sobre cómo utilizar la CLI.

```
ibmcloud cf logging [parámetros]
```
{: codeblock}

**Parámetros**

<dl>
<dt>--help, -h</dt>
<dd>Establezca este parámetro para mostrar la lista de mandatos o para obtener ayuda para un mandato.
</dd>

<dt>--version, -v</dt>
<dd>Establezca este parámetro para que se muestre la versión de la CLI.</dd>
</dl>

**Ejemplos**

Para obtener la lista de mandatos, ejecute el mandato siguiente:

```
ibmcloud cf logging --help
```
{: codeblock}

Para obtener la versión de la CLI, ejecute el mandato siguiente:

```
ibmcloud cf logging --version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

Devuelve una señal de registro que puede utilizar para enviar registros al servicio {{site.data.keyword.loganalysisshort}}. 

**Nota:** La señal no caduca.

```
ibmcloud cf logging auth
```
{: codeblock}

**Devuelve**

<dl>
  <dt>Señal de registro</dt>
  <dd>Por ejemplo, `jec8BmipiEZc`.
  </dd>
  
  <dt>ID de organización</dt>
  <dd>GUID de la organización de {{site.data.keyword.Bluemix_notm}} en la que ha iniciado la sesión.
  </dd>
  
  <dt>ID de espacio</dt>
  <dd>GUID del espacio de la organización en el que ha iniciado la sesión.
  </dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

Suprime los registros almacenados en el componente de recopilación de registros.

```
ibmcloud cf logging delete [parámetros]
```
{: codeblock}

**Parámetros**

<dl>
  <dt>--start valor, -s valor</dt>
  <dd>(Opcional) Establece la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*, por ejemplo `2006-01-02`. <br>El valor predeterminado es hace 2 semanas.
  </dd>
  
  <dt>--end valor, -e valor</dt>
  <dd>(Opcional) Establece la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD* <br>El formato UTC de la fecha es **AAAA-MM-DD**, por ejemplo `2006-01-02`. <br>El valor predeterminado es la fecha actual.
  </dd>
  
  <dt>--type valor, -t valor</dt>
  <dd>(Opcional) Define el tipo de registro. <br>Por ejemplo, *syslog* es un tipo de registro. <br>El valor predeterminado es **\***. <br>Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo **log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Opcional) Establece el ámbito de la información de registro que se proporciona a nivel de cuenta. <br>Si no se especifica este parámetro, el valor predeterminado se establece de modo que se proporciona información de registro solo sobre el espacio actual.
  </dd>
</dl>

**Ejemplo**

Para suprimir los registros de tipo *linux_syslog* del 25 de mayo de 2017, ejecute el mandato siguiente:
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download (Beta)
{: #download4}

Descarga los registros del componente de recopilación de registros en un archivo local o direcciona los registros a otro programa, como por ejemplo Elastic Stack. 

**Nota:** Para descargar archivos, primero tiene que crear una sesión. Una sesión define los registros que se van a descargar en función de rango de fechas, tipo de registro y tipo de cuenta. Los registros se descargan dentro del contexto de una sesión. Para obtener más información, consulte [ibmcloud cf logging session create (Beta)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#session_create1).

```
ibmcloud cf logging download [parámetros] [argumentos]
```
{: codeblock}

**Parámetros**

<dl>
<dt>--output valor, -o valor</dt>
<dd>(Opcional) Establece la vía de acceso y el nombre del archivo de salida local en el que se descargan los registros. <br>El valor predeterminado es un guión (-). <br>Establezca este parámetro en el valor predeterminado para dirigir los registros a la salida estándar.</dd>
</dl>

**Argumentos**

<dl>
<dt>ID_sesión</dt>
<dd>Establezca el valor de ID de sesión que se obtiene cuando se ejecuta el mandato `ibmcloud cf logging session create`. Este valor indica la sesión que se utilizará para descargar los registros. <br>**Nota:** El mandato `ibmcloud cf logging session create` proporciona los parámetros que controlan los registros que se descargan. </dd>
</dl>

**Nota:** Una vez finalizada la descarga, si se intenta ejecutar el mismo mandato de nuevo, este no hará nada. Para volver a descargar los mismos datos, debe utilizar otro archivo u otra sesión.

**Ejemplos**

En un sistema Linux, para descargar registros en un archivo denominado mylogs.gz, ejecute el mandato siguiente:

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

Para descargar registros en su propia plataforma Elastic Stack, ejecute el mandato siguiente:

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

A continuación verá un ejemplo de archivo logstash.conf:

```
input {
  stdin {
    codec => json_lines {}
  }
}
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud cf logging help
{: #help1}

Proporciona información sobre cómo utilizar un mandato.

```
ibmcloud cf logging help [mandato]
```
{: codeblock}

**Parámetros**

<dl>
<dt>Mandato</dt>
<dd>Establezca el nombre del mandato para el que desea obtener ayuda.
</dd>
</dl>


**Ejemplos**

Para obtener ayuda sobre cómo ejecutar el mandato para ver el estado de los registros, ejecute el mandato siguiente:

```
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

Muestra o cambia el periodo de retención para los registros que están disponibles en un espacio o una cuenta. 

* El periodo se establece en número de días.
* El valor predeterminado es **-1**. 

**Nota:** de forma predeterminada, se almacenan todos los registros. Debe suprimirlos manualmente mediante el mandato **delete**. Defina una política de retención para suprimir registros automáticamente.

```
ibmcloud cf logging option [parámetros]
```
{: codeblock}

**Parámetros**

<dl>
<dt>--retention valor, -r valor</dt>
<dd>(Opcional) Define el número de días de retención. <br> El valor predeterminado es *-1* días.</dd>

<dt>--at-account-level, -a </dt>
  <dd>(Opcional) Establece el ámbito a nivel de cuenta. <br>Si no se especifica este parámetro, el valor predeterminado se establece en *-1* para el espacio actual, que es el espacio donde ha iniciado la sesión mediante el mandato `ibmcloud cf login`.
  </dd>
</dl>

**Ejemplos**

Para ver el periodo de retención actual predeterminado para el espacio en el que ha iniciado la sesión, ejecute el mandato siguiente:

```
ibmcloud cf logging option
```
{: codeblock}

La salida es:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


Para cambiar el periodo de retención por 25 días para el espacio en el que ha iniciado la sesión, ejecute el mandato siguiente:

```
ibmcloud cf logging option -r 25
```
{: codeblock}

La salida es:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create (Beta)
{: #session_create1}

Crea una nueva sesión.

**Nota:** Puede tener un máximo de 30 sesiones simultáneas en un espacio. La sesión se crea para un usuario. Las sesiones no se pueden compartir entre usuarios de un espacio.

```
ibmcloud cf logging session create [parámetros]
```
{: codeblock}

**Parámetros**

<dl>
  <dt>--start valor, -s valor</dt>
  <dd>(Opcional) Establece la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*, por ejemplo `2006-01-02`. <br>El valor predeterminado es hace 2 semanas.
  </dd>
  
  <dt>--end valor, -e valor</dt>
  <dd>(Opcional) Establece la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD*, por ejemplo `2006-01-02`. <br>El valor predeterminado es la fecha actual.
  </dd>
  
  <dt>--type valor, -t valor</dt>
  <dd>(Opcional) Define el tipo de registro. <br>Por ejemplo, *syslog* es un tipo de registro. <br>El valor predeterminado es asterisco (*). <br>Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Opcional) Establece el ámbito a nivel de cuenta. <br>Si no se especifica este parámetro, el valor predeterminado se establece en solo el espacio actual, es decir, el espacio donde ha iniciado la sesión mediante el mandato `ibmcloud cf login`.
  </dd>
</dl>

**Valores que se devuelven**

<dl>
<dt>Access-Time</dt>
<dd>Indicación de fecha y hora que muestra cuándo se ha utilizado la sesión por última vez.</dd>

<dt>Create-Time</dt>
<dd>Indicación de fecha y hora correspondiente a la fecha y hora en que se ha creado la sesión.</dd>

<dt>Date-Range</dt>
<dd>Indica los días que se utilizan para filtrar registros. Los registros identificados en este rango de fechas están disponibles para la gestión mediante la sesión.</dd>

<dt>ID</dt>
<dd>ID de sesión.</dd>

<dt>Space</dt>
<dd>ID del espacio en el que la sesión está activa.</dd>

<dt>Type-Account</dt>
<dd>Los tipos de registro que se descargan a través de la sesión.</dd>

<dt>Username</dt>
<dd>ID de {{site.data.keyword.IBM_notm}} del usuario que ha creado la sesión.</dd>
</dl>


**Ejemplo**

Para crear una sesión que incluya los registros comprendidos entre el 20 de mayo de 2017 y el 26 de mayo de 2017 para el tipo de registro *log*, ejecute el mandato siguiente:

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete (Beta)
{: #session_delete1}

Suprime una sesión, especificada por ID de sesión.

```
ibmcloud cf logging session delete [argumentos]
```
{: codeblock}

**Argumentos**

<dl>
<dt>ID de
sesión</dt>
<dd>ID de la sesión que desea suprimir. <br>Puede utilizar el mandato `ibmcloud cf logging session list` para obtener todos los ID de sesiones activas.</dd>
</dl>

**Ejemplo**

Para suprimir una sesión con el ID de sesión *cI6hvAa0KR_tyhjxZZz9Uw==*, ejecute el mandato siguiente:

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list (Beta)
{: #session_list1}

Muestra una lista de las sesiones activas y sus ID.

```
ibmcloud cf logging session list 
```
{: codeblock}

**Valores que se devuelven**

<dl>
<dt>ID</dt>
<dd>ID de sesión.</dd>

<dt>SPACE</dt>
<dd>ID del espacio en el que la sesión está activa.</dd>

<dt>USERNAME</dt>
<dd>ID de {{site.data.keyword.IBM_notm}} del usuario que ha creado la sesión.</dd>

<dt>CREATE-TIME</dt>
<dd>Indicación de fecha y hora correspondiente a la fecha y hora en que se ha creado la sesión.</dd>

<dt>ACCESS-TIME</dt>
<dd>Indicación de fecha y hora que muestra cuándo se ha utilizado la sesión por última vez.</dd>
</dl>
 

## ibmcloud cf logging session show (Beta)
{: #session_show1}

Muestra el estado de una sesión individual.

```
ibmcloud cf logging session show [argumentos]
```
{: codeblock}

**Argumentos**

<dl>
<dt>ID_sesión</dt>
<dd>ID de la sesión activa sobre la que desea obtener información.</dd>
</dl>

**Valores que se devuelven**

<dl>
<dt>Access-Time</dt>
<dd></dd>

<dt>Create-Time</dt>
<dd>Indicación de fecha y hora correspondiente a la fecha y hora en que se ha creado la sesión.</dd>

<dt>Date-Range</dt>
<dd>Indica los días que se utilizan para filtrar registros. Los registros identificados en este rango de fechas están disponibles para la gestión mediante la sesión.</dd>

<dt>ID</dt>
<dd>ID de sesión.</dd>

<dt>Space</dt>
<dd>ID del espacio en el que la sesión está activa.</dd>

<dt>Type-Account</dt>
<dd>Los tipos de registro que se descargan a través de la sesión.</dd>

<dt>Username</dt>
<dd>ID de {{site.data.keyword.IBM_notm}} del usuario que ha creado la sesión.</dd>
</dl>

**Ejemplo**

Para mostrar los detalles de una sesión con el ID de sesión *cI6hvAa0KR_tyhjxZZz9Uw==*, ejecute el mandato siguiente:

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

Devuelve información sobre los registros que se han recopilado en un espacio o cuenta.

```
ibmcloud cf logging status [parámetros]
```
{: codeblock}

**Parámetros**

<dl>
  <dt>--start valor, -s valor</dt>
  <dd>(Opcional) Establece la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*, por ejemplo `2006-01-02`. <br>El valor predeterminado es hace 2 semanas.
  </dd>
  
  <dt>--end valor, -e valor</dt>
  <dd>(Opcional) Establece la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD*, por ejemplo `2006-01-02`. <br>El valor predeterminado es la fecha actual.
  </dd>
  
  <dt>--type valor, -t valor</dt>
  <dd>(Opcional) Define el tipo de registro. <br>Por ejemplo, *syslog* es un tipo de registro. <br>El valor predeterminado es asterisco (*). <br>Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo *log_type_1,log_type_2,log_type_3*.
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(Opcional) Establece el ámbito a nivel de cuenta. <br> **Nota:** Defina este valor para obtener información sobre la cuenta. <br>Si no se especifica este parámetro, el valor predeterminado se establece en solo el espacio actual, es decir, el espacio donde ha iniciado la sesión mediante el mandato `ibmcloud cf login`.
  </dd>
  
  <dt>--list-type-detail, -l</dt>
  <dd>(Opcional) Defina este parámetro para obtener una lista del subtotal de tipos de registro para cada día.
  </dd>
</dl>

**Nota:** El mandato `ibmcloud cf logging status` solo muestra las 2 últimas semanas de registros que se han almacenado en el componente de recopilación de registros cuando no se especifican fechas inicial y final.


