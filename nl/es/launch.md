---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# Navegación a la interfaz de usuario web
{: #launch}

Después de suministrar una instancia del servicio {{site.data.keyword.la_full_notm}} en {{site.data.keyword.cloud_notm}} y configurar un agente LogDNA para un origen de datos de registro, puede visualizar, supervisar y gestionar registros a través de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}.
{:shortdesc}


## Cómo otorgar políticas de IAM a un usuario para visualizar datos 
{: #step1}

**Nota:** debe ser administrador del servicio {{site.data.keyword.la_full_notm}}, administrador de una instancia de {{site.data.keyword.la_full_notm}} o tener permisos de IAM de cuenta para poder otorgar políticas a otros usuarios.

En la tabla siguiente se muestran las políticas mínimas que un usuario debe tener para iniciar la interfaz de usuario web y visualizar datos:

| Servicio                              | Rol                      | Permiso otorgado       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | Rol de la plataforma: Visor     | Permite que el usuario pueda ver la lista de instancias de servicio en el panel de control Registro de observabilidad. |
| `{{site.data.keyword.la_full_notm}}` | Rol de servicio: Escritor      | Permite que el usuario pueda iniciar la interfaz de usuario web y ver registros en la interfaz de usuario web.    |
{: caption="Tabla 1. Políticas de IAM" caption-side="top"} 

Para obtener más información sobre cómo configurar estas políticas para un usuario, consulte [Cómo otorgar permisos a un usuario para ver registros](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Inicio de la interfaz de usuario web a través de la interfaz de usuario de {{site.data.keyword.cloud_notm}}
{: #launch_step2}

Puede iniciar la interfaz de usuario web dentro del contexto de una instancia de {{site.data.keyword.la_full_notm}}, desde la interfaz de usuario de {{site.data.keyword.cloud_notm}}. 

Siga los pasos siguientes para iniciar la interfaz de usuario web:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre el panel de control de {{site.data.keyword.cloud_notm}}.

2. En el menú de navegación, seleccione **Observabilidad**. 

3. Seleccione **Registro**. 

    Se muestra la lista de instancias que están disponibles en {{site.data.keyword.cloud_notm}}.

4. Seleccione una instancia. A continuación, pulse **Ver LogDNA**.

Se abre la interfaz de usuario web.


## Obtención del URL de la interfaz de usuario web desde {{site.data.keyword.cloud_notm}}
{: #launch_get}

Para obtener el URL de la interfaz de usuario web, realice los pasos siguientes desde un terminal:

1. Establezca el grupo de recursos donde se ha suministrado la instancia de {{site.data.keyword.la_full_notm}}.

    ```
    export logdna_rg_name=<Resource_Group_Name_Where_LogDNA_Instance_Is_Created>
    ```
    {: codeblock}

2. Establezca el nombre de la instancia de {{site.data.keyword.la_full_notm}}.

    ```
    export logdna_instance_name=<Your_LogDNA_Instance_Name>
    ```
    {: codeblock}

3. Establezca el punto final.

    ```
    export rc_endpoint=resource-controller.cloud.ibm.com
    ```
    {: codeblock}

4. Establezca la señal IAM.

    ```
    export iam_token=$(ibmcloud iam oauth-tokens | grep IAM | grep -oP  "eyJ.*")
    ```
    {: codeblock}

    **Nota:** si va a trabajar en un terminal de MacOS, el mandato será el siguiente: `export iam_token=$(ic iam oauth-tokens | grep IAM | grep -o  "eyJ.*")`

5. Establezca el ID del grupo de recursos.

    ```
    export resource_group_id=$(ibmcloud resource groups | grep "^$logdna_rg_name" | awk '{print $2}')
    ```
    {: codeblock}

6. Establezca el URL de la interfaz de usuario web en una variable.

    ```
    export dashboard_url=$(curl -H "Accept: application/json" -H "Authorization: Bearer $iam_token" "https://$rc_endpoint/v1/resource_instances?resource_group_id=$resource_group_id&type=service_instance" | jq ".resources[] | select(.name==\"$logdna_instance_name\") | .dashboard_url")
    ```
    {: codeblock}

7. Obtenga el URL de la interfaz de usuario web.

    ```
    echo $dashboard_url
    ```
    {: codeblock}

    

