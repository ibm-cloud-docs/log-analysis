---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# Eliminación de una instancia
{: #remove}

Puede eliminar una instancia del servicio {{site.data.keyword.la_full_notm}} desde la interfaz de usuario de {{site.data.keyword.Bluemix}} o a través de la línea de mandatos.
{:shortdesc}

Al eliminar una instancia de {{site.data.keyword.cloud_notm}}, realice una limpieza completando las tareas siguientes:

1. Anote la lista de orígenes que reenvían métricas a la instancia de {{site.data.keyword.la_full_notm}} que desea eliminar. Debe eliminar el agente LogDNA de cada origen.
2. Elimine los permisos otorgados a los usuarios que trabajan con la instancia. 

    Si gestiona el acceso utilizando grupos de acceso dedicados para trabajar con una instancia específica, debe eliminar estos grupos de acceso.

    Si gestiona el acceso a varias instancias de registro utilizando grupos de acceso, debe eliminar las políticas que otorgan permisos a la instancia que desee eliminar.
    
    Si otorga políticas individuales a los usuarios, debe recopilar la lista de usuarios que tienen permisos para trabajar con esa instancia. A continuación, para cada usuario que identifique, debe eliminar las políticas relacionadas con la instancia que desee suprimir.


A continuación, suprima la instancia del panel de control de {{site.data.keyword.cloud_notm}}.


## Eliminación de una instancia mediante la interfaz de usuario de {{site.data.keyword.cloud_notm}}
{: #remove_ui}

Para eliminar una instancia de {{site.data.keyword.la_full_notm}} mediante la interfaz de usuario de {{site.data.keyword.cloud_notm}}, siga los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.cloud_notm}}.

2. Vaya al icono de menú ![icono de menú](../../icons/icon_hamburger.svg) &gt; **Observabilidad** para acceder al Panel de control *Observabilidad*.

3. Seleccione **Registro**. Se mostrará la lista de instancias de registro.

4. Seleccione la instancia que desea suprimir.

5. En el menú *Acción*, seleccione **Eliminar**.


## Eliminación de una instancia mediante la CLI
{: #remove_cli}

Para eliminar una instancia de {{site.data.keyword.la_full_notm}} mediante la línea de mandatos, siga los pasos siguientes:

1. [Requisito previo] Instalación de la CLI de {{site.data.keyword.cloud_notm}}.

   Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   Si la CLI está instalada, continúe en el paso siguiente.

2. Inicie una sesión en {{site.data.keyword.cloud_notm}} donde desea suministrar la instancia. Ejecute el siguiente mandato: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Establezca el grupo de recursos en el que se ha suministrado la instancia. Ejecute el siguiente mandato: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    De forma predeterminada, está establecido el grupo de recursos *default*.

4. Elimine la instancia. Ejecute el mandato [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete):

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    Donde NAME es el nombre de la instancia.

    Por ejemplo, para eliminar una instancia, ejecute el mandato siguiente:

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



