---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# Desconexión de un agente de LogDNA de una instancia
{: #detach_agent}

Desconecte un agente de LogDNA de una instancia de registro para detener la recopilación de registros.
{:shortdesc}

## Desconexión de un agente de LogDNA de clúster de Kubernetes
{: #detach_agent_kube}

Para hacer que el clúster de Kubernetes deje de enviar registros a la instancia de {{site.data.keyword.la_full_notm}}, debe eliminar el agente de LogDNA del clúster. 

Para hacer que el clúster de Kubernetes deje de reenviar registros a la instancia de LogDNA, realice los pasos siguientes desde la línea de mandatos:

1. Abra un terminal. A continuación, [inicie la sesión en {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} y siga las indicaciones.

    Seleccione la cuenta donde ha suministrado la instancia de {{site.data.keyword.la_full_notm}}.

2. Configure el entorno de clúster. Ejecute los mandatos siguientes:

    En primer lugar, obtenga el mandato para establecer la variable de entorno y descargar los archivos de configuración de Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Cuando termine la descarga de los archivos de configuración, se muestra un mandato que puede utilizar para establecer la vía de acceso al archivo de configuración de Kubernetes local como variable de entorno.

    A continuación, copie y pegue el mandato que se muestra en el terminal para definir la variable de entorno `KUBECONFIG`.

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




