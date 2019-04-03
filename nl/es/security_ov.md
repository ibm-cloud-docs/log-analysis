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

# Seguridad
{: #security_ov}

Para controlar las acciones de {{site.data.keyword.loganalysisshort}} que puede realizar un usuario, puede asignar uno o varios roles a un usuario. 
{:shortdesc}

Para trabajar con la API del servicio {{site.data.keyword.loganalysisshort}}, debe utilizar una señal de UAA o una señal de IAM. Para enviar registros al servicio {{site.data.keyword.loganalysisshort}}, necesita una señal de registro.


## Modelos de autenticación
{: #auth1}

Para trabajar con el servicio {{site.data.keyword.loganalysisshort}} mediante la CLI o la API, necesita una señal de autenticación.

El servicio {{site.data.keyword.loganalysisshort}} da soporte a los siguientes modelos de autenticación:

* [Autenticación de UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)

    Solo puede utilizar la CLI para gestionar las señales de UAA.
	
* [Autenticación de IAM](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)

    El modelo de autenticación de IAM ofrece funciones de gestión de IU, CLI o API. 

**Nota:** Una señal de UAA y una señal de IAM caducan transcurrido un periodo de tiempo. 

## Roles
{: #roles3}

Hay dos tipos de roles en {{site.data.keyword.Bluemix_notm}} que controlan las acciones que pueden llevar a cabo los usuarios cuando trabajan con el servicio {{site.data.keyword.loganalysisshort}}:

* Roles de Cloud Foundry (CF): El usuario controla las acciones de {{site.data.keyword.loganalysisshort}} que puede realizar un usuario asignando uno o varios roles de CF. Con estos roles, controla los permisos del usuario para ver y gestionar registros en un espacio o una organización.
* Roles de IAM: El usuario controla las acciones de {{site.data.keyword.loganalysisshort}} que puede realizar un usuario asignando uno o varios roles de IAM. Con estos roles, controla los permisos del usuario para ver y gestionar registros de cuentas. 


En la tabla siguiente se muestra el tipo de roles y el dominio de {{site.data.keyword.Bluemix_notm}} que controlan:

<table>
  <caption>Tabla 1. Tipo de roles que controlan acciones por dominio</caption>
  <tr>
    <th></th>
	<th align="right">Cuenta</th>
    <th align="right">Organización</th>
    <th align="right">Space</th>	
  </tr>
  <tr>
    <td align="left">Roles de CF</td>
	<td align="center">No</td>
	<td align="center">Sí</td>
	<td align="center">Sí</td>
  </tr>
  <tr>
    <td align="left">Roles de IAM</td>
	<td align="center">Sí</td>
	<td align="center">No</td>
	<td align="center">No</td>
  </tr>
</table>


## Roles de CF
{: #bmx_roles}

En la tabla siguiente se muestran los privilegios de cada uno de los roles de CF para trabajar con el servicio {{site.data.keyword.loganalysisshort}}:

<table>
  <caption>Tabla 2. Roles y privilegios de Cloud Foundry para trabajar con el servicio {{site.data.keyword.loganalysisshort}}.</caption>
  <tr>
    <th>Rol</th>
	<th>Dominio</th>
	<th>Privilegios de acceso</th>
  </tr>
  <tr>
    <td>Gestor</td>
	<td>Organización <br>Space</td>
	<td>Todas las API RESTful</td>
  </tr>
  <tr>
    <td>Desarrollador</td>
	<td>Space</td>
	<td>Todas las API RESTful</td>
  </tr>
  <tr>
    <td>Auditor</td>
	<td>Organización <br>Space</td>
	<td>Solo las API RESTful que realizan operaciones de solo lectura, como por ejemplo consultar registros.</td>
  </tr>
</table>


## Roles de IAM
{: #iam_roles}

En la tabla siguiente se muestran los privilegios de cada uno de los roles de IAM para trabajar con el servicio {{site.data.keyword.loganalysisshort}}:

<table>
  <caption>Tabla 3. Roles y privilegios de IAM para trabajar con el servicio {{site.data.keyword.loganalysisshort}}.</caption>
  <tr>
    <th>Rol</th>
	<th>Privilegios</th>
  </tr>
  <tr>
    <td>Administrador</td>
	  <td>Ver información sobre los registros en un espacio o a nivel de cuenta. <br>Descargar los registros en un archivo local o dirigir los registros a otro programa, como Elastic Stack. <br>Muestra el periodo de retención para los registros que están disponibles en un espacio o una cuenta. <br>Actualiza el periodo de retención para los registros que están disponibles en un espacio o una cuenta. <br>Muestra una lista de las sesiones activas y sus ID. <br>Crear una sesión que puede utilizar para descargar los registros. <br>Suprimir una sesión, especificada por ID de sesión. <br>Muestra el estado de una sesión individual. <br>Suprimir registros. </td>
  </tr>
  <tr>
    <td>Editor</td>
	  <td>Ver información sobre los registros en un espacio o a nivel de cuenta. <br>Descargar los registros en un archivo local o dirigir los registros a otro programa, como Elastic Stack. <br>Muestra el periodo de retención para los registros que están disponibles en un espacio o una cuenta. <br>Actualiza el periodo de retención para los registros que están disponibles en un espacio o una cuenta. <br>Muestra una lista de las sesiones activas y sus ID. <br>Crear una sesión que puede utilizar para descargar los registros. <br>Suprimir una sesión, especificada por ID de sesión. <br>Muestra el estado de una sesión individual. <br>Suprimir registros.  </td>
  </tr>
  <tr>
    <td>Operador</td>
	  <td>Ver información sobre los registros en un espacio o a nivel de cuenta. <br>Muestra el periodo de retención para los registros que están disponibles en un espacio o una cuenta. <br>Muestra una lista de las sesiones activas y sus ID. <br>Muestra el estado de una sesión individual. <br>Descargar los registros en un archivo local o dirigir los registros a otro programa, como Elastic Stack.  <br>Crear una sesión que puede utilizar para descargar los registros. <br>Suprimir una sesión, especificada por ID de sesión. </td>
  </tr>
  <tr>
    <td>Visor</td>
	  <td>Ver información sobre los registros en un espacio o a nivel de cuenta. <br>Muestra el periodo de retención para los registros que están disponibles en un espacio o una cuenta. <br>Muestra una lista de las sesiones activas y sus ID. <br>Muestra el estado de una sesión individual. </td>
  </tr>
</table>

En la tabla siguiente se muestran las relaciones entre la API, una acción de servicio y un rol de IAM que utiliza el servicio {{site.data.keyword.loganalysisshort}}.

<table>
  <caption>Tabla 4. Relación entre la API, una acción de servicio y un rol de IAM. </caption>
  <tr>
    <th>API</th>
	<th>Acción</th>
	<th>Rol de IAM</th>
	<th>Descripción</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>Administrador, Editor</td>
	<td>Suprimir registros.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>Administrador, Editor, Visor</td>
	<td>Ver información sobre los registros en un espacio de {{site.data.keyword.Bluemix_notm}} o a nivel de cuenta.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>Administrador, Editor</td>
	<td>Descargar los registros en un archivo local o dirigir los registros a otro programa, como Elastic Stack.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>Administrador, Editor, Visor</td>
    <td>Muestra el periodo de retención para los registros que están disponibles en un espacio o una cuenta de {{site.data.keyword.Bluemix_notm}}.</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>Administrador, Editor</td>
    <td>Actualiza el periodo de retención para los registros que están disponibles en un espacio o una cuenta de {{site.data.keyword.Bluemix_notm}}.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Administrador, Editor, Visor</td>
    <td>Muestra una lista de las sesiones activas y sus ID.</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>Administrador, Editor</td>
    <td>Crear una sesión que puede utilizar para descargar los registros.</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>Administrador, Editor</td>
    <td>Suprimir una sesión, especificada por ID de sesión.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>Administrador, Editor, Visor</td>
    <td>Muestra el estado de una sesión individual.</td>
  </tr>
</table>

## Obtención de una señal de autenticación para gestionar registros mediante la API
{: #get_token}

Para gestionar registros mediante la API de {{site.data.keyword.loganalysisshort}}, debe utilizar una señal de autenticación. 

**Cómo trabajar con los registros que están disponibles en el dominio del espacio**

* Utilice la CLI de {{site.data.keyword.loganalysisshort}} para obtener la señal de UAA. 
* La señal tiene un tiempo de caducidad. 

Para obtener más información, consulte [Obtención de la señal de UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

**Cómo trabajar con los registros que están disponibles en el dominio de la cuenta**

* Utilice la CLI de {{{site.data.keyword.Bluemix_notm}} para obtener la señal de IAM. 
* La señal tiene un tiempo de caducidad. 

Para obtener más información, consulte [Obtención de la señal de IAM](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1).


## Obtención de la señal de registro para enviar registros al análisis de registros
{: #get_logging_token}

Para enviar registros al servicio {{site.data.keyword.loganalysisshort}}, necesita una señal de registro. 

Para enviar registros a un dominio del espacio, elija uno de los siguientes métodos:

* [Obtención de la señal de registro para enviar registros a un espacio mediante el mandato de {{site.data.keyword.Bluemix_notm}} ibmcloud service ](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_cloud_cli)
* [Obtención de la señal de registro para enviar registros a un espacio mediante la CLI de análisis de registro](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_la_cloud_cli)
* [Obtención de la señal de registro para enviar registros a un espacio mediante la API de análisis de registro](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_api)


## Cómo otorgar permisos a un usuario para que trabaje con registros
{: #grant_permissions1}

Para que un usuario pueda gestionar registros o ver registros, se deben otorgar al usuario permisos en {{site.data.keyword.Bluemix_notm}} para trabajar con el servicio {{site.data.keyword.loganalysisshort}}.

* Para obtener información sobre los permisos necesarios para gestionar registros, consulte [Roles que necesita un usuario para gestionar registros](/docs/services/CloudLogAnalysis/manage_logs.html#roles1).
* Para obtener información sobre los permisos necesarios para ver registros, consulte [Roles que necesita un usuario para ver registros](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#roles).

Para obtener más información sobre cómo otorgar permisos, consulte:

* [Asignación de una política de IAM a un usuario mediante la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions).
* [Asignación de una política de IAM a un usuario mediante la línea de mandatos](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_commandline).
* [Cómo otorgar a un usuario permisos para ver registros del espacio mediante la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).


