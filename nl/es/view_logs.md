---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

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

# Visualización de registros
{: #view_logs}

Después de suministrar una instancia del servicio {{site.data.keyword.la_full_notm}} en {{site.data.keyword.cloud_notm}} y configurar un agente LogDNA para un origen de registro, puede visualizar, supervisar y gestionar datos de registro a través de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}.
{:shortdesc}

Al iniciar la interfaz de usuario web de {{site.data.keyword.la_full_notm}}, las entradas de registro se muestran con un formato predefinido. En la sección **Preferencias de usuario**, puede modificar el modo en que se muestra la información en cada línea de registro. También puede filtrar registros y modificar valores de búsqueda y, a continuación, marcar el resultado como una *vista*. Puede adjuntar y quitar una o más alertas a una vista. Puede definir un formato personalizado para el modo en que las líneas se muestran en la vista. Puede expandir una línea de registro y ver los datos analizados.


Realice los pasos siguientes para visualizar registros:


## Paso 1. Otorgar políticas de IAM a un usuario para visualizar registros
{: #view_logs_step1}

**Nota:** debe ser un administrador del servicio {{site.data.keyword.la_full_notm}} o un administrador de la instancia de {{site.data.keyword.la_full_notm}} o debe tener permisos de IAM de la cuenta para poder otorgar políticas a otros usuarios.

En la tabla siguiente se muestran las políticas mínimas que debe tener un usuario para poder iniciar la interfaz de usuario web de {{site.data.keyword.la_full_notm}} y visualizar registros:

| Servicio                        | Rol                      | Permiso otorgado            |
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` | Rol de la plataforma: Visor     | Permite que el usuario pueda ver la lista de instancias de servicio en el panel de control Registro de observabilidad. |
| `{{site.data.keyword.la_full_notm}} ` | Rol de servicio: Lector      | Permite que el usuario pueda iniciar la interfaz de usuario web y ver registros en la interfaz de usuario web.  |
{: caption="Tabla 1. Políticas de IAM" caption-side="top"} 

Para obtener más información sobre cómo configurar estas políticas para un usuario, consulte [Cómo otorgar permisos a un usuario para ver registros en LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Paso 2. Navegar a la interfaz de usuario web a través de la interfaz de usuario de {{site.data.keyword.cloud_notm}}
{: #view_logs_step2}

Para iniciar la interfaz de usuario de {{site.data.keyword.la_full_notm}}  a través de la interfaz de usuario de {{site.data.keyword.cloud_notm}}, realice los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Después de iniciar sesión con su ID de usuario y su contraseña, se abrirá el *Panel de control* de {{site.data.keyword.cloud_notm}}.

2. En el menú de navegación, seleccione **Observabilidad**. 

3. Seleccione **Registro**. 

    Aparecerá la lista de instancias de {{site.data.keyword.la_full_notm}} que están disponibles en {{site.data.keyword.cloud_notm}}.

4. Seleccione una instancia. A continuación, pulse **Ver LogDNA**.

Se abrirá la interfaz de usuario web de {{site.data.keyword.la_full_notm}}, que muestra los registros reenviados a dicha instancia.


## Paso 3. Personalizar la vista predeterminada
{: #view_logs_step3}

En la sección **PREFERENCIAS DE USUARIO**, puede modificar el orden de los campos de datos que se muestran en cada línea.

Realice los pasos siguientes para modificar el formato de una línea de registro:

1. Seleccione el icono **Configuración** ![Icono Configuración](images/admin.png "Icono Administración").
2. Seleccione **PREFERENCIAS DE USUARIO**. Se abrirá una nueva ventana.
3. Seleccione **Formato de registro**.
4. Modifique la sección *Formato de línea* para que se ajuste a sus requisitos. Arrastre los recuadros.


## Paso 4. Buscar en una línea de registro
{: #view_logs_step4}

En cualquier momento, puede ver cada línea de registro en su contexto.

Siga los pasos siguientes: 

1. Pulse el icono **Vistas** ![Icono Configuración](images/views.png "Icono Configuración").
2. Seleccione **Todo** o una vista.
3. Identifique una línea en el registro que desee explorar.
4. Expanda la línea de registro. 

    Aparecerá información sobre identificadores, códigos y etiquetas de línea.

5. Pulse **Ver en contexto** para ver la línea de registro en el contexto de otras líneas de registro de dicho host, app, o ambos.

6. Pulse **Copiar al portapapeles** para copiar el campo de mensaje al portapapeles.

Cuando haya terminado, cierre la línea.


## Paso 5. Filtrar registros
{: #view_logs_step5}

Puede filtrar registros por origen de registro, aplicación y nivel de registro. 

* Un origen puede ser un host, un sistema, una máquina virtual o una app de Heroku.
* Una aplicación representa un archivo de registro, un programa o un contenedor.
* Los ejemplos de niveles de registro son: INFO, DEBUG, ERROR

Realice los pasos siguientes para filtrar registros:

1. Pulse el icono **Vistas** ![Icono Configuración](images/views.png "Icono Configuración").
2. Seleccione **Todo** o una vista.
3. Expanda **Todas las etiquetas** para ver la lista de etiquetas que están identificadas en los registros. A continuación, elija las que desee.
4. Expanda **Todos los orígenes** para ver la lista de orígenes que están identificados en los registros. A continuación, elija los que desee.
5. Expanda **Todas las apps** para ver la lista de apps que están identificadas en los registros. A continuación, elija las que desee.
6. Expanda **Todos los niveles** para ver la lista de niveles de registro que están identificados en los registros. A continuación, elija los que desee.


**Nota:** en cada sección, puede agrupar varias opciones en un grupo. Agrupe etiquetas, orígenes de registro, apps y niveles de registro para reutilizar estas agrupaciones al filtrar datos de registro en otras vistas personalizadas.

Para crear un grupo, seleccione varios valores. A continuación, pulse **Guardar como grupo**. Especifique un nombre para el grupo y guárduelo.


## Paso 6. Buscar en registros
{: #view_logs_step6}

Al buscar datos de registro, la búsqueda aplica todos los filtros de registro y consultas de tiempo que se hayan configurado en esa vista.

Puede realizar búsquedas simples (búsqueda de series de un solo término), búsquedas compuestas (varios términos de búsqueda y operadores), búsquedas de campo si la línea de registro se puede analizar, y otras. Para obtener más información, consulte [Cómo buscar en los registros en documentos LogDNA ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://docs.logdna.com/docs/search){:new_window}.

**Nota:** los operadores AND y OR distinguen entre mayúsculas y minúsculas y se deben poner en mayúsculas.



## Paso 7. Crear vistas
{: #view_logs_step7}


Realice los pasos siguientes para crear una vista:

1. Pulse el icono **Vistas** ![Icono Configuración](images/views.png "Icono Configuración").
2. Seleccione **Todo** o una vista.
3. Filtre los datos de registro y, a continuación, pulse **Guardar como nueva vista / alerta**.

    Se abrirá la página *Crear nueva vista*.

4. Especifique un nombre para la vista en el campo *Nombre*.

5. De manera opcional, añada una categoría. Especifique un nombre y, a continuación, pulse **Añadir esta como nueva categoría de vista**.

6. Opcionalmente, adjunte una alerta. Aparecerá una nueva sección para que pueda configurar la alerta.

7. Pulse **Guardar vista**


