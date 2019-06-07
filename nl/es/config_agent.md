---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# Configuración de un agente LogDNA
{: #config_agent}

El agente LogDNA es el responsable de recopilar y reenviar registros a su instancia de {{site.data.keyword.la_full_notm}}. Después de suministrar una instancia de {{site.data.keyword.la_full}}, debe configurar un agente LogDNA para cada origen de registro que desee supervisar.
{:shortdesc}

* El agente LogDNA se autentica utilizando la clave de ingestión de LogDNA y abre un socket web seguro a los servidores de ingestión de {{site.data.keyword.la_full_notm}}. 
* De forma predeterminada, el agente supervisa todos los archivos con extensión *.log*, así como los archivos sin extensión de */var/log/*.
* El agente realiza el seguimiento de nuevos datos de registro y busca archivos nuevos que se hayan añadido a los directorios de registro que supervisa el agente.

Puede configurar los parámetros siguientes a través del agente LogDNA: 

| Parámetro | Descripción |
|-----------|-------------|
| `tags`    | Defina etiquetas para agrupar hosts de forma automática en grupos dinámicos. |
| `logdir`  | Defina vías de acceso personalizadas que desee que supervise el agente. </br>Separe las vías por comas. Puede utilizar patrones glob. Puede configurar archivos específicos. Especifique patrones glob utilizando signos de comillas dobles. |
| `exclude` | Defina los archivos que no desee que supervise el agente LogDNA. **Nota:** estos archivos se pueden encontrar en cualquiera de las vías de acceso definidas a través del parámetro logdir. </br>Separe los archivos por comas. Puede utilizar patrones glob. Puede configurar archivos específicos. |
| `exclude_regex` | Defina patrones de expresiones regulares para filtrar las líneas que coincidan con el patrón. No incluya `/` al principio ni al final. |
| `hostname` | Defina el nombre de host. Este valor sustituye al nombre de host del sistema operativo. |
| `autoupdate` | Establézcalo en `1` para actualizar automáticamente el agente cuando se actualice la definición del agente del repositorio público. Establézcalo en `0` para inhabilitar esta característica. |  
{: caption="Tabla 1. Parámetros para personalizar un agente LogDNA" caption-side="top"} 



## Configuración de un agente LogDNA en un clúster de Kubernetes utilizando un script
{: #config_agent_kube_script}

Para configurar el clúster de Kubernetes para enviar registros a la instancia de {{site.data.keyword.la_full_notm}}, debe instalar un pod *logdna-agent* en cada nodo del clúster. El agente LogDNA lee archivos de registro del pod donde está instalado y reenvía los datos de registro a la instancia de LogDNA.

Para configurar el clúster de Kubernetes para reenviar registros a su instancia de LogDNA, realice los pasos siguientes desde la línea de mandatos:

1. Abra un terminal para iniciar sesión en {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   Seleccione la cuenta donde ha suministrado la instancia de {{site.data.keyword.la_full_notm}}.

2. Establezca el clúster donde desee configurar el registro como contexto para esta sesión.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   Cuando termine la descarga de los archivos de configuración, se muestra un mandato que puede utilizar para establecer la vía de acceso al archivo de configuración de Kubernetes local como variable de entorno. Copie y pegue el mandato que se muestra en el terminal para definir la variable de entorno `KUBECONFIG`.

3. Cree un secreto de Kubernetes para almacenar la clave de ingestión de logDNA para la instancia de servicio. La clave de ingestión de LogDNA se utiliza para abrir un socket web seguro al servidor de ingestión de LogDNA y para autenticar el agente de registro con el servicio {{site.data.keyword.la_full_notm}}.

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
    ```
    {: pre}

4. Cree un conjunto de daemons de Kubernetes para desplegar el agente LogDNA en cada nodo de trabajador del clúster de Kubernetes. El agente LogDNA recopila registros con la extensión `*.log` y archivos sin extensión que se almacenan en el directorio `/var/log` del pod. De forma predeterminada, se recopilan los registros de todos los espacios de nombres, incluyendo `kube-system`, y se reenvían automáticamente al servicio {{site.data.keyword.la_full_notm}}.

    <table>
      <caption>Mandatos por región</caption>
      <tr>
        <th>Ubicación</th>
        <th>Mandato</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-eu-de.yaml`</td>
      </tr>
    </table>

5. Compruebe que el agente LogDNA se ha desplegado correctamente. 

   ```
   kubectl get pods
   ```
   {: pre}
   

El despliegue se habrá realizado de forma correcta cuando vea uno o más pods de LogDNA.
* **El número de pods de LogDNA es igual al número de nodos de trabajador del clúster.** 
* Todos los pods deben estar en un estado `Running`.
* *Stdout* y *stderr* se recopilan y reenvían automáticamente desde todos los contenedores. Los datos de registro incluyen registros de aplicación y registros de trabajador. 
* De forma predeterminada, el pod del agente LogDNA que se ejecuta en un trabajador recopila registros de todos los espacios de nombres en dicho nodo, incluyendo registros de kube-system.



## Adición de etiquetas a un agente LogDNA en un clúster de Kubernetes
{: #config_agent_kube_tags}

Realice los pasos siguientes para añadir etiquetas:

1. Configure el entorno de clúster. Ejecute los mandatos siguientes:

    En primer lugar, obtenga el mandato para establecer la variable de entorno y descargar los archivos de configuración de Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Cuando termine la descarga de los archivos de configuración, se muestra un mandato que puede utilizar para establecer la vía de acceso al archivo de configuración de Kubernetes local como variable de entorno.

    A continuación, copie y pegue el mandato que se muestra en el terminal para definir la variable de entorno KUBECONFIG.

2. Compruebe la estrategia de actualización del DaemonSet. A continuación, decida si se utilizará *kubectl apply* o *kubectl edit* para modificar el archivo de configuración del agente.

    Para comprobar la estrategia de actualización, ejecute el mandato siguiente:

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    Si la estrategia de actualización se establece en *OnDelete* o si tiene el archivo de configuración que se gestiona a través de un sistema de control de versiones, actualice el archivo de configuración local y aplique los cambios al agente LogDNA utilizando *kubectl apply*.

    Si la estrategia de actualización se establece en *RollingUpdate*, puede actualizar y aplicar los cambios al agente LogDNA utilizando *kubectl edit*.

3. Edite el archivo `logdna-agent-configmap.yaml`. 

    Actualice el archivo de configuración modificando la copia local. **Nota:** también puede generar el archivo de configuración del agente ejecutando el mandato siguiente:

    ```
    kubectl get daemonset logdna-agent -o=yaml > prod-logdna-agent-ds.yaml
    ```
    {: codeblock}

    Como alternativa, actualice el archivo de configuración utilizando *kubectl edit*.

    ```
    kubectl edit daemonset logdna-agent
    ```
    {: codeblock}

4. Realice los cambios. Añada la sección **LOGDNA_TAGS**.

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    Por ejemplo, la sección siguiente muestra dónde añadir etiquetas en el archivo de configuración:

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. Aplique los cambios de configuración si edita el archivo de manera local. 

    ```
    kubectl apply -f prod-logdna-agent-ds.yaml
    ```
    {: codeblock}
    
    **Nota:** si utiliza *kubectl edit*, los cambios se aplicarán automáticamente cuando guarde las modificaciones.


## Configuración de un agente LogDNA en Linux Ubuntu o Debian
{: #config_agent_linux}

Para configurar el servidor Ubuntu para enviar registros a la instancia de {{site.data.keyword.la_full_notm}}, debe instalar un `logdna-agent`. El agente LogDNA lee archivos de registro de */var/log* y reenvía los datos de registro a la instancia de LogDNA.

Para configurar el servidor Ubuntu para reenviar registros a la instancia de LogDNA, realice los pasos siguientes desde un terminal de Ubuntu:

1. Instale el agente LogDNA. Ejecute los mandatos siguientes:

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. Establezca la clave de ingestión que debe utilizar el agente LogDNA para reenviar registros a la instancia de {{site.data.keyword.la_full_notm}}.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    Donde INGESTION_KEY contiene la clave de ingestión activa para la instancia de {{site.data.keyword.la_full_notm}} donde va a configurar el reenvío de registros.

3. Establezca el punto final de autenticación. El agente LogDNA utiliza este host para autenticarse y obtener la señal para reenviar registros.

    <table>
      <caption>Mandatos por región</caption>
      <tr>
        <th>Ubicación</th>
        <th>Mandato</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_APIHOST=api.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

4. Establezca el punto final de ingestión.

    <table>
      <caption>Mandatos por región</caption>
      <tr>
        <th>Ubicación</th>
        <th>Mandato</th>
      </tr>
      <tr>
        <td>`US-South`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com`</td>
      </tr>
      <tr>
        <td>`EU-DE`</td>
        <td>`sudo logdna-agent -s LOGDNA_LOGHOST=logs.eu-de.logging.cloud.ibm.com`</td>
      </tr>
    </table>

5. Defina más vías de acceso de registro a supervisar. Ejecute el mandato siguiente: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    De forma predeterminada, se supervisa **/var/log**.

6. De manera opcional, configure el agente LogDNA para etiquetar los hosts. 


## Adición de etiquetas a un agente LogDNA en Linux Ubuntu o Debian
{: #config_agent-linux_tags}
 

Realice los pasos siguientes para añadir más etiquetas al agente LogDNA:

1. Compruebe que el agente LogDNA esté en ejecución.

2. Añada una o más etiquetas.

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


También puede editar el archivo de configuración de LogDNA y añadir etiquetas. El archivo de configuración se encuentra en */etc/logdna.conf*.

1. Edite el archivo.

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. Añada etiquetas.

3. Reinicie el agente LogDNA.

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














