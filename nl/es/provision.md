---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# Suministro de una instancia
{: #provision}

Para poder supervisar y gestionar datos de registro con {{site.data.keyword.la_full_notm}}, primero debe suministrar una instancia del servicio en {{site.data.keyword.cloud_notm}}.
{:shortdesc}

Para suministrar una instancia de {{site.data.keyword.la_full_notm}} en una región de Cloud pública, debe seleccionar el plan de servicio asociado a la instancia, la región donde se recopilan los registros y el plan que determina el periodo de retención de los registros. Puede elegir periodos de retención de 7, 14 o 30 días.

Como alternativa, {{site.data.keyword.la_full_notm}} ofrece un plan `Lite` que puede utilizar para ver los registros a medida que pasan a través del sistema. Puede visualizar registros utilizando el seguimiento de registros. También puede diseñar filtros para preparar la actualización a un plan con un periodo de retención más largo. Este plan tiene un periodo de retención de 0 días.


## Suministro de una instancia a través del panel de control Observabilidad.
{: #provision_ui}

Para suministrar una instancia desde el panel de control Observabilidad en {{site.data.keyword.cloud_notm}}, realice los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    El panel de control de {{site.data.keyword.cloud_notm}} se puede encontrar en: [Panel de control de {{site.data.keyword.cloud_notm}}![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.cloud_notm}}.

2. Vaya al icono de menú ![icono de menú](../../icons/icon_hamburger.svg). A continuación, seleccione **Observabilidad** para acceder al panel de control *Observabilidad*.

3. Seleccione **Registro** y, a continuación, pulse **Crear instancia**. 

4. Especifique un nombre para la instancia de servicio.

5. Seleccione un grupo de recursos. 

    De forma predeterminada, se selecciona el grupo de recursos **predeterminado**.

    **Nota:** si no puede seleccionar un grupo de recursos, compruebe que tiene permisos de edición sobre el grupo de recursos donde desea suministrar la instancia.

6. Seleccione el plan de servicio `Lite`. 

    De forma predeterminada, se establece el plan Lite.

    Para obtener más información acerca de los otros planes de servicio, consulte [Planes de servicio](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

7. Pulse **Crear**.

Después de suministrar una instancia, se abrirá el panel de control *Registro*. 

A continuación, configure un origen de registro añadiendo un agente LogDNA. Este agente es responsable de recopilar y reenviar registros a la instancia. 



## Suministro de una instancia a través del catálogo
{: #provision_catalog}

Para suministrar una instancia de {{site.data.keyword.la_full_notm}} a través del catálogo de {{site.data.keyword.cloud_notm}}, realice los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.cloud_notm}}.

2. Pulse **Catálogo**. Se abrirá la lista de servicios disponibles en {{site.data.keyword.cloud_notm}}.

3. Para filtrar la lista de servicios que se visualiza, seleccione la categoría **Herramientas de desarrollador**.

4. Pulse el mosaico **{{site.data.keyword.la_full_notm}}**. 

5. Especifique un nombre para la instancia de servicio.

6. Seleccione un grupo de recursos. 

    De forma predeterminada, se selecciona el grupo de recursos **predeterminado**.

    **Nota:** si no puede seleccionar un grupo de recursos, compruebe que tiene permisos de edición sobre el grupo de recursos donde desea suministrar la instancia.

7. Seleccione el plan de servicio `Lite`. 

    De forma predeterminada, se establece el plan Lite.

    Para obtener más información acerca de los otros planes de servicio, consulte [Planes de servicio](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. Pulse **Crear**.

Después de suministrar una instancia, se abrirá el panel de control *Registro*. 

A continuación, configure un origen de registro añadiendo un agente LogDNA. Este agente es responsable de recopilar y reenviar registros a la instancia. 



## Suministro de una instancia a través de la CLI
{: #provision_cli}

Para suministrar una instancia de {{site.data.keyword.la_full_notm}} a través de la línea de mandatos, realice los pasos siguientes:

1. [Requisito previo] Instalación de la CLI de {{site.data.keyword.cloud_notm}}.

   Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   Si la CLI está instalada, continúe en el paso siguiente.

2. Inicie una sesión en {{site.data.keyword.cloud_notm}} donde desea suministrar la instancia. Ejecute el siguiente mandato: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Establezca el grupo de recursos en el que desea suministrar la instancia. Ejecute el siguiente mandato: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    De forma predeterminada, está establecido el grupo de recursos `default`.

4. Cree la instancia. Ejecute el mandato [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create):

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    Donde

    NAME es el nombre de la instancia

    El valor *logdna* es el nombre del servicio {{site.data.keyword.la_full_notm}} en {{site.data.keyword.cloud_notm}}

    SERVICE_PLAN_NAME es el tipo de plan. Los valores válidos son *lite*, *7-days*, *14-days* y *30-days*
    
    LOCATION es la región donde se crea la instancia de LogDNA. El valor válido es *us-south*

    Por ejemplo, para suministrar una instancia con el plan de retención de 7 días, ejecute el mandato siguiente:

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}

5. Cree una clave de servicio con permisos de **administrador** para trabajar con la instancia. Ejecute el mandato [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create):

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    Donde

    NAME es el nombre de la clave de API. Puede denominar la clave de API como la instancia de {{site.data.keyword.la_full_notm}} para ayudarle a identificar la clave de API más adelante.

    ROLE_NAME es el rol que define los permisos que están habilitados. Los valores válidos son *editor*, *operator*, *administrator*

    SERVICE_INSTANCE_NAME es el nombre de la instancia en {{site.data.keyword.cloud_notm}}

    Por ejemplo, para crear una clave de API para la instancia *logdna-instance-01* con permisos de *administrator* (administrador) sobre la instancia de servicio, ejecute el mandato siguiente:

    ```
    ibmcloud resource service-key-create logdna-instance-01 Administrator --instance-name logdna-instance-01
    ```
    {: pre}

    La salida de este mandato incluye distintos valores como el valor `crn` de la instancia y la clave de ingestión de LogDNA.


