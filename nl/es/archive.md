---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, archive logs, COS, cloud object storage

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

 
# Archivado de registros en IBM Cloud Object Storage
{: #archiving}

Puede archivar registros desde una instancia de {{site.data.keyword.la_full_notm}} en un grupo en una instancia de {{site.data.keyword.cos_full_notm}} (COS). 
{:shortdesc}

Para configurar el archivado, debe tener una política de IAM con el rol de plataforma **Visor** y el rol de servicio **Gestor** para el servicio {{site.data.keyword.la_full_notm}}.

Puede archivar registros desde una instancia de {{site.data.keyword.la_full_notm}} en un grupo en una instancia de {{site.data.keyword.cos_full_notm}} (COS). Cada instancia de {{site.data.keyword.la_full_notm}} tiene su propia configuración de archivado. 

Los registros se archivan automáticamente una vez al día en un formato comprimido **(.json.gz)**. Cada línea mantiene sus metadatos.

Los registros se archivan en 24-48 horas después de guardar la configuración. 

La instancia de {{site.data.keyword.cos_full_notm}} se suministra dentro del contexto de un grupo de recursos. La instancia de {{site.data.keyword.la_full_notm}} también se suministra dentro del contexto de un grupo de recursos. Ambas instancias se pueden agrupar bajo el mismo grupo de recursos o en grupos distintos. 

{{site.data.keyword.la_full_notm}} utiliza un ID de servicio para comunicarse con el servicio {{site.data.keyword.cos_full_notm}}.

* El ID de servicio que cree para una instancia de {{site.data.keyword.cos_full_notm}} lo utilizará {{site.data.keyword.la_full_notm}} para autenticarse y acceder a la instancia de {{site.data.keyword.cos_full_notm}}. 
* Puede asignar políticas de acceso específicas a un ID de servicio que restrinjan los permisos en la instancia de {{site.data.keyword.cos_full_notm}}. Restrinja el ID de servicio para que solo tenga permisos de escritura sobre el grupo donde tenga pensado archivar los registros.

En la figura siguiente se muestra una vista de alto nivel de los distintos componentes que están integrados al archivar registros:

![Vista de alto nivel de archivado de registros](images/archive.png "Vista de alto nivel de archivado de registros")


Realice los pasos siguientes para archivar una instancia de {{site.data.keyword.la_full_notm}} en un grupo en una instancia de {{site.data.keyword.cos_full_notm}}:


## Paso 1. Otorgar políticas de IAM a un usuario para trabajar con {{site.data.keyword.cos_full_notm}}
{: #archiving_step1}

**Nota:** este paso debe completarlo el propietario de la cuenta o un administrador del servicio {{site.data.keyword.cos_full_notm}} en {{site.data.keyword.cloud_notm}}.

Como administrador del servicio {{site.data.keyword.cos_full_notm}}, debe poder suministrar instancias del servicio, otorgar a otros usuarios permisos para trabajar con estas instancias y crear ID de servicio. 

Hay distintas maneras de otorgar un permiso de usuario para que pase a ser un editor del servicio {{site.data.keyword.cos_full_notm}}:

* Como administrador del servicio en la cuenta, el usuario debe tener una política de IAM para el servicio {{site.data.keyword.cos_full_notm}} con el rol de plataforma *Administrator* (administrador). Debe asignar a este usuario acceso a un recurso individual de la cuenta. 

* Como administrador del servicio dentro del contexto de un grupo de recursos, el usuario debe tener una política de IAM para el servicio {{site.data.keyword.cos_full_notm}} con el rol de plataforma *Administrator* (administrador) dentro del contexto del grupo de recursos. 


En la tabla siguiente se muestran los roles que puede tener un usuario para completar las acciones que se indican para el servicio {{site.data.keyword.cos_full_notm}}:

| Servicio                    | Roles de plataforma    | Acción                                                                                        | 
|----------------------------|-------------------|-----------------------------------------------------------------------------------------------|       
| `Cloud Object Storage`     | Administrador     | Permite que el usuario pueda asignar políticas a los usuarios de la cuenta para trabajar con el servicio
{{site.data.keyword.cos_full_notm}}. |
| `Cloud Object Storage`     | Administrador </br>Editor | Permite que el usuario pueda suministrar una instancia del servicio {{site.data.keyword.cos_full_notm}}.    |
| `Cloud Object Storage`     | Administrador </br>Editor </br>Operador | Permite que el usuario pueda crear un ID de servicio.    | 
{: caption="Tabla 1. Roles y acciones" caption-side="top"} 


Siga los pasos siguientes para asignar a un usuario el rol de administrador sobre el servicio {{site.data.keyword.cos_full_notm}} dentro del contexto de un grupo de recursos: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso dentro de un grupo de recursos**.
4. Seleccione un grupo de recursos.
5. Si el usuario aún no tiene un rol otorgado para el grupo de recursos seleccionado, elija un rol para el campo **Asignar acceso a un grupo de recursos**. 

    En función del rol que seleccione, el usuario puede ver el grupo de recursos en su panel de control, editar el nombre del grupo de recursos o gestionar el acceso de usuarios al grupo. 
    
    Puede seleccionar **Sin acceso** si desea que el usuario solo tenga acceso al servicio {{site.data.keyword.la_full_notm}} en el grupo de recursos.

6. Seleccione **Cloud Object Storage**.
7. Seleccione el rol de **Administrador** de la plataforma.
8. Pulse **Asignar**.



## Paso 2. Suministrar una instancia de {{site.data.keyword.cos_full_notm}}
{: #archiving_step2}

**Nota:** este paso debe completarlo un editor o un administrador del servicio {{site.data.keyword.cos_full_notm}} en {{site.data.keyword.cloud_notm}}. 

Realice los pasos siguientes para suministrar una instancia de {{site.data.keyword.cos_full_notm}}:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.cloud_notm}}.

2. Pulse **Catálogo**. Se abrirá la lista de servicios disponibles en {{site.data.keyword.cloud_notm}}.

3. Para filtrar la lista de servicios mostrada, seleccione la categoría **Almacenamiento**.

4. Pulse el mosaico **Object Storage**.

5. Especifique un nombre para la instancia de servicio.

6. Seleccione un grupo de recursos. 

    De forma predeterminada, se selecciona el grupo de recursos **predeterminado**.

7. Seleccione un plan de servicio. 

    De forma predeterminada, se establece el plan **Lite**.

9. Pulse **Crear**.



## Paso 3. Crear un grupo
{: #archiving_step3}

Los grupos son una manera de organizar los datos en una instancia de {{site.data.keyword.cos_full_notm}}. 

Para gestionar los grupos, se deben otorgar al usuario permisos para trabajar con grupos en la instancia de {{site.data.keyword.cos_full_notm}}. En la tabla siguiente se describen las distintas acciones y roles que puede tener un usuario para trabajar con grupos:

| Servicio                    | Roles                   | Acción                             | 
|----------------------------|-------------------------|------------------------------------|       
| `Cloud Object Storage`     | Rol de la plataforma: Visor   | Permite que el usuario pueda ver todos los grupos y listar los objetos dentro de ellos a través de la interfaz de usuario de {site.data.keyword.Bluemix_notm}}. |
| `Cloud Object Storage`     | Rol de servicio: Gestor   | Permite que el usuario pueda establecer objetos como públicos.                                                       |
| `Cloud Object Storage`     | Roles de servicio: Gestor </br>Escritor | Permite que el usuario pueda crear y destruir grupos y objetos.                         | 
| `Cloud Object Storage`     | Rol de servicio: Lector    | Permite que el usuario pueda listar y descargar objetos.                                                 |
{: caption="Tabla 1. Roles y acciones para trabajar con grupos" caption-side="top"} 

**Nota:** para crear un grupo, el usuario debe tener permisos de gestor o de escritor para la instancia de {{site.data.keyword.cos_full_notm}}.

Realice los pasos siguientes para crear un grupo:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre el panel de control de {{site.data.keyword.cloud_notm}}.

2. Desde el Panel de control, seleccione la instancia de {{site.data.keyword.cos_full_notm}} donde tenga pensado crear el grupo.

3. Seleccione **Grupos**. A continuación, pulse **Crear grupo**.

4. Especifique un nombre de grupo en el campo *Nombre de grupo exclusivo*.

    **Nota:** todos los grupos de todas las regiones de todo el mundo comparten un único espacio de nombres. 

    Puede utilizar el nombre de la instancia de {{site.data.keyword.la_full_notm}} como parte del nombre del grupo. Por ejemplo, para una instancia con el nombre *logdna-1*, puede utilizar *accountN-logdna-1* como nombre de grupo.

    Necesitará este nombre para configurar el archivado a través de la interfaz de usuario web de {{site.data.keyword.la_full_notm}}.

5. Elija el tipo de capacidad de recuperación y una ubicación donde desee que se almacenen físicamente los datos.

    La capacidad de recuperación hace referencia al ámbito y la escala del área geográfica en la que se distribuyen los datos. 
    
    La capacidad de recuperación entre regiones distribuirá los datos en varias áreas metropolitanas.
    
    La capacidad de recuperación regional distribuirá los datos en una única área metropolitana. 
    
    Un centro de datos individual solo distribuirá los datos en dispositivos dentro de un único sitio.

    Para obtener más información, consulte [Seleccionar regiones y puntos finales](/docs/services/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints).

6. Elija el tipo de *Clase de almacenamiento*.

    Puede crear grupos con distintas clases de almacenamiento. Elija la clase de almacenamiento del grupo según sus requisitos de recuperación de datos. Para obtener más información, consulte [Utilizar clases de almacenamiento](/docs/services/cloud-object-storage?topic=cloud-object-storage-use-storage-classes#use-storage-classes).

    **Nota:** no es posible cambiar la clase de almacenamiento de un grupo una vez que se haya creado. Si fuera necesario volver a clasificar los objetos, se deben mover los datos a otro grupo con la clase de almacenamiento deseada.

7. También puede añadir una clave de protección de clave para cifrar los datos en reposo.

    Todos los objetos se cifran de forma predeterminada utilizando claves generadas de forma aleatoria y una transformación de todo o nada. Aunque este modelo de cifrado predeterminado proporciona seguridad en reposo, algunas cargas de trabajo necesitan estar en posesión de las claves de cifrado utilizadas. Para obtener más información, consulte [Gestionar el cifrado](/docs/services/cloud-object-storage?topic=cloud-object-storage-manage-encryption#manage-encryption).



## Paso 4. Crear un ID de servicio para la instancia de {{site.data.keyword.cos_full_notm}}
{: #archiving_step4}

Un ID de servicio identifica un servicio de manera similar en que un ID de usuario identifica un usuario. Los ID de servicio no están vinculados a un usuario específico. Si el usuario que crea el ID de servicio deja la organización y se suprime de la cuenta, el ID de servicio se conserva.

Debe crear un ID de servicio para la instancia de {{site.data.keyword.cos_full_notm}}. Este ID de servicio lo utilizará la instancia de {{site.data.keyword.la_full_notm}} para autenticarse con la instancia de {{site.data.keyword.cos_full_notm}}. 

Debe asignar políticas de acceso específicas al ID de servicio que restrinjan los permisos para utilizar servicios específicos, o incluso combinen permisos para acceder a distintos servicios. Por ejemplo, para restringir el acceso a un grupo individual, asegúrese de que el ID de servicio no tiene ninguna política a nivel de instancia que utilice la consola ni la CLI.


Realice los pasos siguientes para crear un ID de servicio con permisos de escritura para la instancia de {{site.data.keyword.cos_full_notm}}:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre el panel de control de {{site.data.keyword.cloud_notm}}.

2. Desde el Panel de control, seleccione la instancia de {{site.data.keyword.cos_full_notm}} donde tenga pensado crear el grupo.

3. Seleccione **Credenciales de servicio**. A continuación, seleccione **Nueva credencial**.

4. Especifique un nombre. 

5. Seleccione el rol **Escritor**.

6. Pulse **Añadir**.

    Se añade un nuevo ID de servicio a la lista. 


Para el ID de servicio que acaba de crear, pulse **Ver credenciales**. Puede ver información relacionada con el ID de servicio. 

* Copie la clave de API. Este es el valor establecido en el campo **apikey**.
* Copie el ID de instancia de recurso. Este es el valor establecido para el campo **resource_instance_id**.


## Paso 5. Restringir el ID de servicio para que solo tenga permisos de escritura para el grupo
{: #archiving_step5}

Si desea restringir el ID de servicio para que solo tenga permisos de escritura para un grupo, realice los pasos siguientes:

1. Lea la información relativa al ID de servicio y anote el valor del campo **iam_apikey_name** y el valor del campo **iam_apikey_name**. 

2. En el panel de control, seleccione **Gestionar** &gt; **Acceso (IAM)** y, a continuación, seleccione **Usuarios**.

3. Seleccione **ID de servicio**.

4. Busque un ID de servicio que tenga el nombre siguiente: **auto-generated-serviceId-<ID que forma parte del valor de iam_apikey_name>.

5. Seleccione el ID de servicio. A continuación, en **Políticas de acceso**, pulse **Escritor**.

6. En el campo *Tipo de recurso*, especifique **grupo**.

7. En el campo *ID de recurso*, especifique el nombre del grupo.

8. Pulse **Guardar**.

**Nota:** si deja el campo Tipo de recurso o el campo Recurso en blanco, la política que se crea es una política a nivel de instancia.


## Paso 6. Seleccionar el punto final
{: #archiving_step6}

Un punto final define dónde buscar un grupo. Hay distintos puntos finales en función de la región y el tipo de capacidad de recuperación. Para obtener más información, consulte [Seleccionar regiones y puntos finales](/docs/services/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints).

Realice los pasos siguientes para obtener el punto final para el grupo:

1. Inicie una sesión en su cuenta de {{site.data.keyword.cloud_notm}}.

    Pulse el [panel de control de {{site.data.keyword.cloud_notm}} ![Icono de enlace externo](../../icons/launch-glyph.svg "Icono de enlace externo")](https://cloud.ibm.com/login){:new_window} para iniciar el panel de control de {{site.data.keyword.cloud_notm}}.

	Cuando inicia una sesión con su ID de usuario y su contraseña, se abre el panel de control de {{site.data.keyword.cloud_notm}}.

2. Desde el Panel de control, seleccione la instancia de {{site.data.keyword.cos_full_notm}} donde tenga pensado crear el grupo.

3. Seleccione **Grupos**. A continuación, seleccione el grupo que ha creado donde desea archivar registros.

4. Seleccione **Configuración**.

5. Copie uno de los puntos finales privados. 



## Paso 7. Otorgar políticas de IAM a un usuario para archivar registros
{: #archiving_step7}

En la tabla siguiente se muestran las políticas que un usuario debe tener para configurar el archivado de registros desde la interfaz de usuario web de {{site.data.keyword.la_full_notm}} en un grupo de una instancia de {{site.data.keyword.cos_full_notm}}:

| Servicio                        | Rol                      | Permiso otorgado                  | 
|--------------------------------|---------------------------|-------------------------------------|  
| `{{site.data.keyword.la_full_notm}}` | Rol de la plataforma: Visor     | Permite que el usuario pueda ver la lista de instancias de servicio en el panel de control Registro de observabilidad. |
| `{{site.data.keyword.la_full_notm}}` | Rol de servicio: Gestor      | Permite que el usuario pueda iniciar la interfaz de usuario web y ver registros en la interfaz de usuario web.                             |
{: caption="Tabla 2. Políticas de IAM" caption-side="top"} 

Para obtener más información sobre cómo configurar estas políticas para un usuario, consulte [Cómo otorgar permisos a un usuario para ver registros en LogDNA](/docs/services/Log-Analysis-with-LogDNA/work_iam.html#user_logdna).

Realice los pasos siguientes para asignar a un usuario permiso para archivar registros: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso dentro de un grupo de recursos**.
4. Seleccione un grupo de recursos.
5. Si el usuario aún no tiene un rol otorgado para el grupo de recursos seleccionado, elija un rol para el campo **Asignar acceso a un grupo de recursos**. 

    En función del rol que seleccione, el usuario puede ver el grupo de recursos en su panel de control, editar el nombre del grupo de recursos o gestionar el acceso de usuarios al grupo. 
    
    Puede seleccionar **Sin acceso** si desea que el usuario solo tenga acceso al servicio {{site.data.keyword.la_full_notm}} en el grupo de recursos.

6. Seleccione **IBM Log Analysis with LogDNA**.
7. Seleccione el rol de **Visor** de la plataforma.
8. Seleccione el rol de **Gestor** del servicio.
9. Pulse **Asignar**.



## Paso 8. Configurar el archivado para su instancia de {{site.data.keyword.la_full_notm}}
{: #archiving_step8}


Realice los pasos siguientes para configurar el archivado de su instancia de {{site.data.keyword.la_full_notm}} en un grupo COS:

1. Inicie la interfaz de usuario web de {{site.data.keyword.la_full_notm}}. [Más información](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#view_logs_step2).

2. Seleccione el icono **Configuración**. A continuación, seleccione **Archivado**. 

3. Seleccione **IBM Cloud Object Storage**.

4. Establezca el grupo, el punto final, la clave de API y el ID de la instancia donde desea que se archiven los registros.

    <table>
      <caption>Tabla 3. Campos de COS</caption>
      <tr>
         <th>Campo</th>
         <th>Valor</th>
      </tr>
      <tr>
         <td>Grupo</td>
         <td>Establézcalo en el nombre del grupo de COS. </td>
      </tr>
      <tr>
         <td>Punto final</td>
         <td>Establézcalo en el punto final privado del grupo de COS.</td>
      </tr>
      <tr>
         <td>Clave de API</td>
         <td>Establézcalo en la clave de API asociada con el ID de servicio de COS.</td>
      </tr>
      <tr>
         <td>ID de instancia</td>
         <td>Establézcalo en el ID de instancia de COS. </td>
      </tr>
    </table>

5. Pulse **Guardar**.


Después de guardar la configuración, los registros se archivarán una vez al día.



