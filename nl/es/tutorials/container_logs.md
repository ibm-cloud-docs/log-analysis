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


# Análisis de registros en Kibana para una app desplegada en un clúster de Kubernetes
{: #container_logs}
Utilice esta guía de aprendizaje para aprender a configurar un clúster para reenviar registros al servicio de {{site.data.keyword.loganalysisshort}} en {{site.data.keyword.Bluemix_notm}}.
{:shortdesc}


## Objetivos
{: #objectives}

1. Configurar las configuraciones de registro en un clúster. 
2. Buscar y analizar registros de contenedor para una app desplegada en un clúster de Kubernetes en {{site.data.keyword.Bluemix_notm}}.

Esta guía de aprendizaje le guía por los pasos necesarios para hacer que funcione el siguiente caso de ejemplo completo en {{site.data.keyword.Bluemix_notm}}: Suministrar un clúster, configurar el clúster para enviar registros al servicio de {{site.data.keyword.loganalysisshort}} en {{site.data.keyword.Bluemix_notm}}, desplegar una app en el clúster, y utilizar Kibana para ver y filtrar registros de contenedor para dicho clúster.


**Nota:** Para completar esta guía de aprendizaje, debe completar los requisitos previos y las guías de aprendizaje enlazados desde los distintos pasos.


## Requisitos previos
{: #prereq}

1. Debe ser un miembro o un propietario de una cuenta {{site.data.keyword.Bluemix_notm}} con permisos para crear clústeres de Kubernetes estándar, desplegar apps en clústeres y realizar consultas en los registros de {{site.data.keyword.Bluemix_notm}} para un análisis avanzado en Kibana.

    El ID de usuario para {{site.data.keyword.Bluemix_notm}} debe tener las políticas siguientes asignadas:
    
    * Una política de IAM para {{site.data.keyword.containershort}} con los permisos *editor*, *operador* o *administrador*.
    * Un rol de CF para el espacio donde se suministra el servicio {{site.data.keyword.loganalysisshort}} con los permisos *desarrollador*.
    
    Para obtener más información, consulte [Asignar una política de IAM a un usuario mediante la IU de IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account) y [Cómo otorgar permisos a un usuario para ver registros del espacio mediante la IU de IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space).

2. Tener una sesión de terminal desde la que gestionar el clúster de Kubernetes y desplegar apps desde la línea de mandatos. Los ejemplos en esta guía de aprendizaje se proporcionan para un sistema Ubuntu Linux.

3. Instalar las CLI para trabajar con {{site.data.keyword.containershort}} y {{site.data.keyword.loganalysisshort}} en el sistema Ubuntu.

    * Instale la CLI de {{site.data.keyword.Bluemix_notm}}. Instale la CLI de {{site.data.keyword.containershort}} para crear y gestionar sus clústeres de Kubernetes en {{site.data.keyword.containershort}}, y para desplegar apps contenerizadas en el clúster. Para obtener más información, consulte [Instalación de la CLI de {{site.data.keyword.Bluemix_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
    
    * Instale la CLI de {{site.data.keyword.loganalysisshort}}. Para obtener más información, consulte [Cómo configurar la CLI de Log Analysis (plugin de IBM Cloud)](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli).
    
4. Tener acceso a un espacio denominado **dev** en su cuenta en la región EE.UU. sur. 

    Los registros disponibles en el clúster se configurarán para ser reenviados al dominio de espacio asociado con este espacio. 
    
    En esta página, suministrará el servicio de {{site.data.keyword.loganalysisshort}}.
    
    Debe tener permisos de **desarrollador** en este espacio para poder suministrar el servicio de {{site.data.keyword.loganalysisshort}}.
    
    En la guía de aprendizaje, el nombre de organización utilizado es **MyOrg**.

    
 

## Paso 1: Suministrar un clúster de Kubernetes
{: #step25}

Siga estos pasos:

1. Cree un clúster de Kubernetes estándar.

   Para obtener más información, consulte [Creación de clústeres](/docs/containers?topic=containers-cs_cluster_tutorial#cs_cluster_tutorial).

2. Configure el contexto del clúster en un terminal. Después de haber configurado el contexto, podrá gestionar el clúster de Kubernetes y desplegar la aplicación en dicho clúster de Kubernetes.

    Inicie la sesión en la región, organización y espacio en {{site.data.keyword.Bluemix_notm}} que están asociados al clúster que ha creado. Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

	Inicialice el plug-in del servicio {{site.data.keyword.containershort}}.

	```
	ibmcloud cs init
	```
	{: codeblock}

    Establezca el contexto de terminal para el clúster.
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    El resultado de ejecutar este mandato muestra el mandato que debe ejecutar en el terminal para definir la vía de acceso a su archivo de configuración. Por ejemplo:

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    Copie y pegue el mandato para definir la variable de entorno en el terminal y luego pulse **Intro**.



## Paso 2: Configurar el clúster para reenviar registros automáticamente al servicio de {{site.data.keyword.loganalysisshort}}
{: #step26}

Cuando se despliega la app, los registros los recopila automáticamente {{site.data.keyword.containershort}}. Sin embargo, los registros no se reenvían automáticamente al servicio de {{site.data.keyword.loganalysisshort}}. Debe crear una o más configuraciones de registro en el clúster que definan:

* Dónde se reenviarán los registros. Puede reenviar registros al dominio de la cuenta o al dominio de un espacio.
* Qué registros se reenvían al servicio {{site.data.keyword.loganalysisshort}} para su análisis.


Antes de definir las configuraciones de registro, compruebe las definiciones de configuración de registro actuales en el clúster. Ejecute el mandato siguiente:

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

Donde *ClusterName* es el nombre del clúster.

Por ejemplo, las configuraciones de registro definidas para el clúster *mycluster* son las siguientes: 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

Para ver la lista de orígenes de registro para las que puede definir una configuración de registro, consulte [Orígenes de registros](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_sources).


### Configurar el clúster para reenviar los registros stderr y stdout al servicio {{site.data.keyword.loganalysisshort}}
{: #containerstd}


Realice los pasos siguientes para enviar los registros stdout y stderr a un dominio de espacio, donde el nombre de la organización es *MyOrg* y el nombre de espacio es *dev* en la región EE.UU. sur:

1. Compruebe que el ID de usuario tenga permisos para añadir una configuración de clúster. Solo los usuarios con una política de IAM para {{site.data.keyword.containershort}} con permisos para gestionar clústeres pueden habilitar esta característica. Se necesita uno de los roles siguientes: *Administrador*, *Operador*

    Para comprobar que el ID de usuario tiene una política de IAM asignada para gestionar clústeres, siga estos pasos:
    
    1. Inicie sesión en la consola de {{site.data.keyword.Bluemix_notm}}. Abra un navegador web e inicie el panel de control de {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window} Después de iniciar sesión con su ID de usuario y contraseña, se abrirá la IU de {{site.data.keyword.Bluemix_notm}}.

    2. En la barra de menús, pulse **Gestionar > Cuenta > Usuarios**.  La ventana *Usuarios* muestra una lista de usuarios con sus direcciones de correo electrónico para la cuenta seleccionada actualmente.
	
    3. Seleccione el ID de usuario y verifique que el ID de usuario tenga una política para {{site.data.keyword.containershort}}.

    Si necesita permisos, póngase en contacto con el propietario de cuenta o con un administrador de la cuenta. Solo el propietario de la cuenta o los usuarios con permisos para asignar políticas pueden realizar este paso.

2. Cree una configuración de registro de clúster. Ejecute el siguiente mandato para enviar los archivos de registro *stdout* y *stderr* al servicio de {{site.data.keyword.loganalysisshort}}:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    donde 

    * *ClusterName* es el nombre del clúster.
    * *EndPoint* es el URL para el servicio de registro en la región donde se suministra el servicio de {{site.data.keyword.loganalysisshort}}. Para obtener una lista de puntos finales, consulte [Puntos finales](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
    * *OrgName* es el nombre de la organización donde está disponible el espacio.
    * *SpaceName* es el nombre del espacio donde se suministra el servicio de {{site.data.keyword.loganalysisshort}}.


Por ejemplo, para crear una configuración de registro que reenvíe los registros stdout y stderr al desarrollador de espacios en la región EE.UU. sur, ejecute el mandato siguiente:

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### Configurar el clúster para reenviar registros de trabajo al servicio {{site.data.keyword.loganalysisshort}}
{: #workerlogs }

Realice los pasos siguientes para enviar los registros de trabajo a un dominio de espacio, donde el nombre de la organización sea *MyOrg* y el nombre de espacio sea *dev* en la región EE.UU. sur:

1. Compruebe que el ID de usuario tenga permisos para añadir una configuración de clúster. Solo los usuarios con una política de IAM para {{site.data.keyword.containershort}} con permisos para gestionar clústeres pueden habilitar esta característica. Se necesita uno de los roles siguientes: *Administrador*, *Operador*

    Para comprobar que el ID de usuario tiene una política de IAM asignada para gestionar clústeres, siga estos pasos:
    
    1. Inicie sesión en la consola de {{site.data.keyword.Bluemix_notm}}. Abra un navegador web e inicie el panel de control de {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window} Después de iniciar sesión con su ID de usuario y contraseña, se abrirá la IU de {{site.data.keyword.Bluemix_notm}}.

    2. En la barra de menús, pulse **Gestionar > Cuenta > Usuarios**.  La ventana *Usuarios* muestra una lista de usuarios con sus direcciones de correo electrónico para la cuenta seleccionada actualmente.
	
    3. Seleccione el ID de usuario y verifique que el ID de usuario tenga una política para {{site.data.keyword.containershort}}.

    Si necesita permisos, póngase en contacto con el propietario de cuenta o con un administrador de la cuenta. Solo el propietario de la cuenta o los usuarios con permisos para asignar políticas pueden realizar este paso.

2. Cree una configuración de registro de clúster. Ejecute el siguiente mandato para enviar los archivos de registro */var/log/syslog* y */var/log/auth.log* al servicio {{site.data.keyword.loganalysisshort}}:

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    donde 

    * *ClusterName* es el nombre del clúster.
    * *EndPoint* es el URL para el servicio de registro en la región donde se suministra el servicio de {{site.data.keyword.loganalysisshort}}. Para obtener una lista de puntos finales, consulte [Puntos finales](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls).
    * *OrgName* es el nombre de la organización donde está disponible el espacio.
    * *SpaceName* es el nombre del espacio donde se suministra el servicio de {{site.data.keyword.loganalysisshort}}.

    
Por ejemplo, para crear una configuración de registro que reenvíe los registros de trabajo al dominio del espacio en la región EE.UU. sur, ejecute el mandato siguiente:

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## Paso 3: Otorgar los permisos de usuario para ver los registros en un dominio de espacio
{: #step33}

Para otorgar permisos a un usuario para ver registros en un espacio, debe asignar a ese usuario un rol de Cloud Foundry que describa las acciones que puede realizar este usuario con el servicio {{site.data.keyword.loganalysisshort}} en el espacio. 

Complete los pasos siguientes para otorgar permisos a un usuario para trabajar con el servicio {{site.data.keyword.loganalysisshort}}:

1. Inicie sesión en la consola de {{site.data.keyword.Bluemix_notm}}.

    Abra un navegador web e inicie el panel de control de {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window}
	
	Cuando inicia sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}.

2. En la barra de menús, pulse **Gestionar > Cuenta > Usuarios**. 

    La ventana *Usuarios* muestra una lista de usuarios con sus direcciones de correo electrónico para la cuenta seleccionada actualmente.
	
3. Si el usuario es un miembro de la cuenta, seleccione el nombre de usuario de la lista, o pulse **Gestionar usuario** del menú *Acciones*.

    Si el usuario no es un miembro de la cuenta, consulte [Invitación a usuarios](/docs/iam?topic=iam-iamuserinv#iamuserinv).

4. Seleccione **Acceso de Cloud Foundry** y, a continuación, seleccione la organización.

    Se listará la lista de espacios disponibles en dicha organización.

5. Elija el espacio. A continuación, desde la acción de menú, seleccione **Editar el rol de espacio**.

    Si no puede ver el espacio para EE.UU. sur, cree el espacio antes de continuar.

6. Seleccione *desarrollador*.

    Puede seleccionar uno o más roles. 
    
    Los roles válidos son: *Gestor*, *Desarrollador* y *Auditor*
	
7. Pulse **Guardar rol**.


## Paso 4: Otorgar los permisos de propietario de clave a {{site.data.keyword.containershort_notm}}
{: #step52}

Para que los registros del clúster se reenvíen a un espacio, el propietario de la clave {{site.data.keyword.containershort_notm}} propietario debe tener los permisos siguientes:

* Política de IAM para el servicio {{site.data.keyword.loganalysisshort}} con permisos de *administrador*.
* Permisos de Cloud Foundry (CF) de la organización y el espacio donde se deben reenviar los registros. El propietario de la clave del contenedor necesita el rol *orgManager* para la organización, y *SpaceManager* y *Developer* para el espacio.

Siga estos pasos:

1. Identifique el usuario en la cuenta que es el propietario de la clave de {{site.data.keyword.containershort}}. Desde un terminal, ejecute el mandato siguiente:

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    donde *ClusterName* es el nombre del clúster.

2. Verifique que el usuario que se identifica como el propietario de la clave de {{site.data.keyword.containershort}} tenga el rol *orgManager* para la organización, y *SpaceManager* y *Developer* para el espacio.

    Inicie sesión en la consola de {{site.data.keyword.Bluemix_notm}}. Abra un navegador web e inicie el panel de control de {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window} Después de iniciar sesión con su ID de usuario y contraseña, se abrirá la IU de {{site.data.keyword.Bluemix_notm}}.

    En la barra de menús, pulse **Gestionar > Cuenta > Usuarios**.  La ventana *Usuarios* muestra una lista de usuarios con sus direcciones de correo electrónico para la cuenta seleccionada actualmente.
	
    Seleccione el ID del usuario, y verifique que el usuario tenga el rol *orgManager* para la organización, y *SpaceManager* y *Developer* para el espacio.

    Si el usuario no tiene los permisos correctos, otorgue al usuario los permisos siguientes: rol de *orgManager* para la organización, y *SpaceManager* y *Developer* para el espacio. Para obtener más información, consulte [Cómo otorgar permisos a un usuario para ver registros del espacio mediante la IU de IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space).
    
3. Compruebe que el usuario identificado como el propietario de la clave de {{site.data.keyword.containershort}} tiene una política de IAM para el servicio {{site.data.keyword.loganalysisshort}} con permisos de *administrador*.

    En la barra de menús, pulse **Gestionar > Cuenta > Usuarios**.  La ventana *Usuarios* muestra una lista de usuarios con sus direcciones de correo electrónico para la cuenta seleccionada actualmente.
	
    Seleccione el ID del usuario y verifique que el usuario tenga establecida la política de IAM. 

    Si el usuario no tiene la política de IAM, consulte [Asignación de una política de IAM a un usuario mediante la interfaz de usuario de IBM Cloud](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account).

4. Renueve la configuración de registro. Ejecute el mandato siguiente:
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    donde *ClusterName* es el nombre del clúster.
	



## Paso 5: Desplegar una app de ejemplo en el clúster de Kubernetes para generar contenido en stdout
{: #step53}

Desplegar y ejecutar una app de ejemplo en el clúster de Kubernetes. Complete los pasos de la siguiente guía de aprendizaje para desplegar la app de ejemplo: [Lección 1: Despliegue de apps de una sola instancia en clústeres de Kubernetes](/docs/containers?topic=containers-cs_apps_tutorial#cs_apps_tutorial_lesson1).

La app es una app Node.js Hello World:

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

En esta app de ejemplo, cuando prueba la app en un navegador, la app escribe en la salida estándar el siguiente mensaje: `Sample app is listening on port 8080.`






## Paso 6: Ver datos de registro en Kibana
{: #step6}

Siga estos pasos:

1. Inicie Kibana en un navegador. 

    Para obtener más información sobre cómo iniciar Kibana, consulte [Navegación a Kibana desde un navegador web](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser).

    Para analizar los datos de registro para un clúster, debe acceder a Kibana en la región Pública de la nube en la que se ha creado el clúster. 
    
    Por ejemplo, en la región EE.UU. sur, escriba el siguiente URL para iniciar Kibana:
	
	```
	https://logging.ng.bluemix.net/ 
	```
	{: codeblock}
	
    Se abre Kibana.
    
    **NOTA:** Compruebe que inicia Kibana en la región donde está reenviando los registros de clúster. Para obtener información sobre los URL por región, consulte [Puntos finales de registro](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana).
    	
2. Para ver los datos de registro que están disponibles en el dominio del espacio, siga estos pasos:

    1. En Kibana, pulse el ID de usuario. Se abrirá la vista para establecer el espacio.
    
    2. Seleccione la cuenta donde está disponible el espacio. 
    
    3. Seleccione el dominio siguiente: **espacio**
    
    4. Seleccione la organización *MyOrg* donde está disponible el espacio.
    
    5. Seleccione el espacio *dev*.
    
    
3. En la página **Descubrir**, mire los sucesos que se visualizan. 
        
    En la sección *Campos disponibles*, puede ver una lista de campos para utilizar para definir nuevas consultas o para filtrar las entradas que aparecen listadas en la tabla que se visualiza en la página.
    
    En la siguiente tabla se muestra una lista de algunos de los campos que puede utilizar para definir nuevas consultas de búsquedas. En la tabla también se incluyen valores de ejemplo que corresponden al suceso que la app de ejemplo genera:
 
    <table>
              <caption>Tabla 2. Campos comunes para registros de contenedor </caption>
               <tr>
                <th align="center">Campo</th>
                <th align="center">Descripción</th>
                <th align="center">Ejemplo</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>El valor de este campo corresponde a la región de {{site.data.keyword.Bluemix_notm}} en la que se recopila esta entrada de registro.</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>ID de cuenta</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str*</td>
                <td>ID de clúster.</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>ID de clúster</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str*</td>
                <td>Nombre del espacio de nombres</td>
                <td>*default* es el valor predeterminado.</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>Nombre de contenedor</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>Los campos de etiqueta son opcionales. Puede haber 0 o más etiquetas. Cada etiqueta empieza con el prefijo `kubernetes.labels.` seguido por *nombre_etiqueta*. </td>
                <td>En la app de ejemplo, puede ver dos etiquetas: <br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*stream_str*</td>
                <td>Tipo de registro.</td>
                <td>*stdout*, *stderr*</td>
              </tr>
        </table>
     
Para obtener más información sobre otros campos de búsqueda que son relevantes para los clústeres de Kubernetes, consulte [Búsquedas en los registros](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_search).


## Paso 7: Filtrar datos por nombre de clúster de Kubernetes en Kibana
{: #step7}
    
En la tabla que se muestra en la página *Discovery*, puede ver todas las entradas disponibles para el análisis. Las entradas que se listan corresponden a la consulta de búsqueda que se visualiza en la barra *Buscar*. Utilice un asterisco (*) para visualizar todas las entradas del periodo de tiempo configurado para la página.
    
Por ejemplo, para filtrar los datos por nombre de clúster de Kubernetes, modifique la barra de consulta *Buscar*. Añada un filtro basado en el campo personalizado *kubernetes.cluster_name_str*:
    
1. En la sección **Campos disponibles**, seleccione el campo *kubernetes.cluster_name_str*. Se visualizará un subconjunto de valores disponibles para el campo.    
    
2. Seleccione el valor que corresponda al clúster para el que desea analizar los registros. 
    
    Después de seleccionar el valor, se añade un filtro a la barra *Buscar* para que la tabla visualice únicamente las entradas que coincidan con el criterio que acaba de seleccionar.     
   

**Nota:** 

Si no puede ver el nombre de clúster, añada un filtro para cualquier nombre de clúster. A continuación, seleccione el símbolo de edición del filtro.    
    
Se visualiza la siguiente consulta:
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

Sustituya el nombre del clúster (*cluster1*) por el nombre del clúster *mycluster* para el que desea ver datos de registro.
        
Si no ve ningún dato, intente cambiar el filtro de tiempo. Para obtener más información, consulte [Establecimiento de un filtro de tiempo](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter).

Para obtener más información, consulte [Filtrado de registros en Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs).


## Material de referencia de {{site.data.keyword.containershort_notm}}
{: reference}

Mandatos de CLI:

* [ibmcloud cs api-key-info](/docs/containers?topic=containers-cs_cli_reference#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers?topic=containers-cs_cli_reference#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers?topic=containers-cs_cli_reference#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers?topic=containers-cs_cli_reference#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers?topic=containers-cs_cli_reference#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers?topic=containers-cs_cli_reference#cs_logging_refresh)

