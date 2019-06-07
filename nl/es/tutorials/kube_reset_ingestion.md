---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# Restablecimiento de la clave de ingestión utilizada por un clúster de Kubernetes para reenviar registros a una instancia de {{site.data.keyword.la_full_notm}}
{: #kube_reset}

Si la clave de ingestión que utiliza para reenviar registros desde un clúster a una instancia de {{site.data.keyword.la_full_notm}} en {{site.data.keyword.cloud_notm}} se ve comprometida, debe restablecer la clave y actualizar la configuración del clúster de Kubernetes para que utilice la nueva clave de ingestión. 
{:shortdesc}

## Antes de empezar
{: #kube_reset_prereqs}

Trabaje en la región EE. UU. sur. Ambos recursos, tanto la instancia de {{site.data.keyword.la_full_notm}} como el clúster de Kubernetes, deben ejecutarse en la misma cuenta.

La instancia de {{site.data.keyword.la_full_notm}} se suministra en el grupo de recursos **Default** (predeterminado).

Obtenga más información sobre {{site.data.keyword.la_full_notm}}. Para obtener más información, consulte [Acerca de LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Para poder realizar los pasos de esta guía de aprendizaje, el ID de {{site.data.keyword.IBM_notm}} debe tener asignadas políticas de IAM para cada uno de los recursos siguientes: 

| Recurso                             | Ámbito de la política de acceso | Roles    | Región    | Información                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Grupo de recursos **predeterminado**           |  Grupo de recursos            | Visor  | us-south  | Esta política es necesaria para permitir que el usuario vea las instancias de servicio en el grupo de recursos predeterminado.    |
| Servicio {{site.data.keyword.la_full_notm}} |  Grupo de recursos            | Editor </br>Gestor  | us-south  | Esta política es necesaria para permitir que el usuario pueda restablecer la clave de ingestión.   |
| Instancia de clúster de Kubernetes          |  Recurso                  | Editor  | us-south  | Esta política es necesaria para poder suprimir y configurar el secreto y el agente LogDNA en el clúster de Kubernetes. |
{: caption="Tabla 1. Lista de políticas de IAM necesarias para completar la guía de aprendizaje" caption-side="top"} 

Para obtener más información sobre los roles de IAM de {{site.data.keyword.containerlong}}, consulte [Permisos de acceso de usuario](/docs/containers?topic=containers-access_reference#access_reference).

Instale la CLI de {{site.data.keyword.cloud_notm}} y el plugin de CLI de Kubernetes. Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).


## Paso 1: Restablecer la clave de ingestión
{: #kube_reset_step1}

Para renovar la clave de ingestión para una instancia de {{site.data.keyword.la_full_notm}} utilizando la interfaz de usuario web de {{site.data.keyword.la_full_notm}}, realice los pasos siguientes:

1. Inicie la interfaz de usuario web de {{site.data.keyword.la_full_notm}}. Para obtener más información, consulte [Inicio de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Seleccione el icono **Configuración**. A continuación, seleccione **Organización**. 

3. Seleccione **Claves de API**.

    Puede ver las claves de ingestión que se han creado. 

4. Seleccione **Generar clave de ingestión**.

    Se añade una nueva clave a la lista.

5. Suprima la clave de ingestión antigua. Pulse **Suprimir**.


## Paso 2: Eliminar la configuración del clúster que utilice la clave de ingestión antigua
{: #kube_reset_step2}

Siga los pasos siguientes:

1. Abra un terminal. A continuación, inicie una sesión en {{site.data.keyword.cloud_notm}}. Ejecute el mandato siguiente y siga las indicaciones:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Seleccione la cuenta en la que ha suministrado la instancia de {{site.data.keyword.la_full_notm}}.

2. Configure el entorno de clúster. Ejecute los mandatos siguientes:

    En primer lugar, obtenga el mandato para establecer la variable de entorno y descargar los archivos de configuración de Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Cuando termine la descarga de los archivos de configuración, se muestra un mandato que puede utilizar para establecer la vía de acceso al archivo de configuración de Kubernetes local como variable de entorno.

    A continuación, copie y pegue el mandato que se muestra en el terminal para definir la variable de entorno KUBECONFIG.

    **Nota:** cada vez que inicie una sesión en la CLI de {{site.data.keyword.containerlong}} para trabajar con clústeres, debe ejecutar estos mandatos para establecer la vía de acceso al archivo de configuración del clúster como una variable de sesión. La CLI de Kubernetes utiliza esta variable para buscar un archivo de configuración local y los certificados necesarios para conectar con el clúster en {{site.data.keyword.cloud_notm}}.

3. Elimine el secreto del clúster de Kubernetes. El secreto de Kubernetes contiene la clave de ingestión de LogDNA. Ejecute el mandato siguiente:

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Elimine el agente LogDNA en cada trabajador (nodo) del clúster de Kubernetes. El agente LogDNA es el responsable de recopilar y reenviar los registros. Ejecute el mandato siguiente:

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. Compruebe que el agente LogDNA se ha suprimido correctamente. Ejecute el mandato siguiente:

    ```
    kubectl get pods
    ```
    {: codeblock}

    No debería aparecer ningún pod de LogDNA.


## Paso 3: Configurar el clúster de Kubernetes con la nueva clave de ingestión
{: #kube_reset_step3}

Para configurar el clúster de Kubernetes para reenviar registros a su instancia de LogDNA, realice los pasos siguientes desde la línea de mandatos:

1. Abra un terminal. A continuación, inicie una sesión en {{site.data.keyword.cloud_notm}}. Ejecute el mandato siguiente y siga las indicaciones:

    ```
    ibmcloud login -a cloud.ibm.com
    ```
    {: codeblock}

    Seleccione la cuenta en la que ha suministrado la instancia de {{site.data.keyword.la_full_notm}}.

2. Configure el entorno de clúster. Ejecute los mandatos siguientes:

    En primer lugar, obtenga el mandato para establecer la variable de entorno y descargar los archivos de configuración de Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Cuando termine la descarga de los archivos de configuración, se muestra un mandato que puede utilizar para establecer la vía de acceso al archivo de configuración de Kubernetes local como variable de entorno.

    A continuación, copie y pegue el mandato que se muestra en el terminal para definir la variable de entorno KUBECONFIG.

    **Nota:** cada vez que inicie una sesión en la CLI de {{site.data.keyword.containerlong}} para trabajar con clústeres, debe ejecutar estos mandatos para establecer la vía de acceso al archivo de configuración del clúster como una variable de sesión. La CLI de Kubernetes utiliza esta variable para buscar un archivo de configuración local y los certificados necesarios para conectar con el clúster en {{site.data.keyword.cloud_notm}}.

3. Añada un secreto a su clúster de Kubernetes. Ejecute el mandato siguiente:

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE muestra la clave de ingestión de LogDNA para la instancia.

    El secreto de Kubernetes contiene la clave de ingestión de LogDNA. La clave de ingestión de LogDNA se utiliza para autenticar el agente de registro con el servicio {{site.data.keyword.la_full_notm}}. Se utiliza para abrir un socket web seguro al servidor de ingestión en el sistema de fondo de registro.

4. Configure el agente LogDNA en cada trabajador (nodo) del clúster de Kubernetes. Ejecute el mandato siguiente:

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    El agente LogDNA es el responsable de recopilar y reenviar los registros.

    El agente recopila automáticamente registros con la extensión *.log y archivos sin extensión que se encuentran en /var/log. De forma predeterminada, se recopilan registros de todos los espacios de nombres, incluyendo kube-system.

5. Compruebe que el agente LogDNA se ha creado correctamente y vea su estado. Ejecute el mandato siguiente:

    ```
    kubectl get pods
    ```
    {: codeblock}


## Paso 4: Iniciar la interfaz de usuario web de LogDNA
{: #kube_reset_step4}

Para iniciar el panel de control de IBM Log Analysis with LogDNA a través de la interfaz de usuario de {{site.data.keyword.cloud_notm}}, realice los pasos siguientes:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Después de iniciar sesión con su ID de usuario y su contraseña, se abre el panel de control de {{site.data.keyword.cloud_notm}}.

2. En el menú de navegación, seleccione **Observabilidad**. 

3. Seleccione **Registro**. 

    Aparecerá la lista de instancias de {{site.data.keyword.la_full_notm}} que están disponibles en {{site.data.keyword.cloud_notm}}.

3. Seleccione una instancia. A continuación, pulse **Ver registros**.

    Se abrirá la interfaz de usuario web de LogDNA y mostrará los registros de clúster.


## Paso 5: Visualizar los registros
{: #kube_reset_step5}

Desde la interfaz de usuario web de LogDNA, puede ver los registros a medida que pasan a través del sistema. Puede visualizar registros utilizando el seguimiento de registros. 

**Nota:** con el plan de servicio **gratuito**, solo puede realizar el seguimiento de los registros más recientes.



## Pasos siguientes
{: #kube_reset_next_steps}

  Si desea [filtrar registros del clúster](https://docs.logdna.com/docs/filters), [buscar en los registros del clúster](https://docs.logdna.com/docs/search), [definir vistas](https://docs.logdna.com/docs/views) y [configurar alertas](https://docs.logdna.com/docs/alerts), deberá actualizar el plan de {{site.data.keyword.la_full_notm}} a un plan de pago.



