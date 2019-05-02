---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# Cómo trabajar con claves de ingestión
{: #ingestion_key}

La clave de ingestión es una clave de seguridad que debe utilizar para configurar agentes LogDNA y reenviar correctamente los registros a su instancia de {{site.data.keyword.la_full_notm}} en {{site.data.keyword.cloud_notm}}. Obtendrá automáticamente la clave de ingestión al suministrar una instancia. Como alternativa, también puede obtener la clave de ingestión creando un ID de servicio para la instancia. 
{:shortdesc}

**Nota:** 

* Para trabajar con claves de ingestión a través de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}, debe tener una política de IAM con el rol de plataforma **Visor** y el rol de servicio **Gestor** para el servicio {{site.data.keyword.la_full_notm}}. 
* Para trabajar con claves de ingestión a través de la interfaz de usuario de {{site.data.keyword.cloud_notm}}, debe tener una política de IAM con el rol de plataforma **Editor** y el rol de servicio **Gestor** para el servicio {{site.data.keyword.la_full_notm}}. 


## Obtenga la clave de ingestión a través de la interfaz de usuario de {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_ui}

Para obtener la clave de ingestión para una instancia de {{site.data.keyword.la_full_notm}} utilizando la interfaz de usuario de {{site.data.keyword.cloud_notm}}, realice los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.cloud_notm}}.

2. En el menú de navegación, seleccione **Observabilidad**. 

3. Seleccione **Registro**. Se abre el panel de control de {{site.data.keyword.la_full_notm}}. Puede ver la lista de instancias de registro que están disponibles en {{site.data.keyword.cloud_notm}}.

3. Identifique la instancia para la que desea obtener la clave de ingestión y pulse **Ver clave de ingestión**.

4. Se abrirá una ventana donde puede pulsar **Mostrar** para ver la clave de ingestión.


## Obtenga la clave de ingestión a través de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}
{: #logdna_ui}

Para obtener la clave de ingestión para una instancia de {{site.data.keyword.la_full_notm}} utilizando la interfaz de usuario web de {{site.data.keyword.la_full_notm}}, realice los pasos siguientes:

1. Inicie la interfaz de usuario web de {{site.data.keyword.la_full_notm}}. Para obtener más información, consulte [Inicio de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleccione el icono **Configuración**. A continuación, seleccione **Organización**. 

3. Seleccione **Claves de API**.

Puede ver las claves de ingestión que se han creado. 

**Nota:** solo hay una clave de ingestión activa al mismo tiempo. 


## Obtenga la clave de ingestión a través de la CLI de {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_cli}

Para obtener la clave de ingestión para una instancia de {{site.data.keyword.la_full_notm}} a través de la línea de mandatos, realice los pasos siguientes:

1. [Requisito previo] Instale la CLI de {{site.data.keyword.cloud_notm}}.

   Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

   Si la CLI está instalada, continúe en el paso siguiente.

2. Inicie sesión en la región de {{site.data.keyword.cloud_notm}} donde se ejecuta la instancia. Ejecute el siguiente mandato: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Establezca el grupo de recursos donde se está ejecutando la instancia de {{site.data.keyword.la_full_notm}}. Ejecute el mandato siguiente: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target) con la opción `-g`.

    De forma predeterminada, está establecido el grupo de recursos `default`.

4. Obtenga el nombre de la clave de API asociada con la instancia de {{site.data.keyword.la_full_notm}}. Ejecute el mandato [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys):

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    Identifique la clave de servicio asociada con la instancia.

5. Obtenga la clave de ingestión. Ejecute el mandato [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key):

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    Donde APIKEY_NAME es el nombre de la clave de API
 
    La salida de este mandato incluye el campo **ingestion_key**, que contiene la clave de ingestión para la instancia.


## Restablecer la clave de ingestión 
{: #reset}

Si la clave de ingestión se ve comprometida o tiene una política para renovarla después de un número determinado de días, puede generar una nueva clave y suprimir la anterior.

Para renovar la clave de ingestión para una instancia de {{site.data.keyword.la_full_notm}} utilizando la interfaz de usuario web de {{site.data.keyword.la_full_notm}}, realice los pasos siguientes:

1. Inicie la interfaz de usuario web de {{site.data.keyword.la_full_notm}}. Para obtener más información, consulte [Inicio de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleccione el icono **Configuración**. A continuación, seleccione **Organización**. 

3. Seleccione **Claves de API**.

    Puede ver las claves de ingestión que se han creado. 

4. Seleccione **Generar clave de ingestión**.

    Se añade una nueva clave a la lista.

5. Suprima la clave de ingestión antigua. Pulse **Suprimir**.

**Nota:** después de restablecer la clave de ingestión, debe actualizar la clave de ingestión para los orígenes de registro que haya configurado para reenviar registros a esta instancia de {{site.data.keyword.la_full_notm}}.



