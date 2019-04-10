---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, IAM, security, logging, access groups

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

 
# Gestión de políticas de IAM y grupos de acceso
{: #work_iam}

Puede utilizar {{site.data.keyword.iamlong}} (IAM) para autenticar usuarios de forma segura y controlar el acceso a todos los recursos de nube de manera coherente en {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

Para obtener más información, consulte [Gestión del acceso de usuario con IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).


## Cómo otorgar permisos a un usuario para que se convierta en administrador del servicio en la cuenta de {{site.data.keyword.cloud_notm}}
{: #admin_account}

Como **propietario de la cuenta** o como **administrador del servicio {{site.data.keyword.la_full_notm}}**, debe tener permisos para ejecutar las acciones siguientes: 

* Otorgar a otros miembros de la cuenta acceso para trabajar con el servicio
* Suministrar una instancia de servicio
* Suprimir una instancia de servicio
* Ver detalles de una instancia de servicio
* Crear un ID de servicio

Por lo tanto, para otorgar a un usuario el rol de administrador para gestionar el servicio en la cuenta, el usuario debe tener una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de plataforma **Administrador**. Debe asignar a este usuario acceso a un recurso individual de la cuenta. 

Siga los pasos siguientes para asignar a un usuario el rol de administrador sobre el servicio {{site.data.keyword.la_full_notm}} en la cuenta: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso a recursos**.
4. Seleccione **IBM Log Analysis with LogDNA**.
5. Seleccione **Todas las regiones actuales**.
6. Seleccione **Todas las instancias de servicio actuales**.
7. Seleccione el rol de **Administrador** de la plataforma.
8. Pulse Asignar.


## Cómo otorgar permisos a un usuario para que se convierta en administrador del servicio dentro de un grupo de recursos
{: #admin_rg}

Como **administrador del servicio {{site.data.keyword.la_full_notm}}**, debe tener permisos para ejecutar las acciones siguientes: 

* Otorgar a otros miembros de la cuenta acceso para trabajar con el servicio
* Suministrar una instancia de servicio
* Suprimir una instancia de servicio
* Ver detalles de una instancia de servicio
* Crear un ID de servicio

Por lo tanto, para otorgar a un usuario el rol de administrador para gestionar instancias dentro de un grupo de recursos en la cuenta, el usuario debe tener una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de plataforma **Administrador** dentro del contexto del grupo de recursos. 

Siga los pasos siguientes para asignar a un usuario el rol de administrador sobre el servicio {{site.data.keyword.la_full_notm}} dentro del contexto de un grupo de recursos: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso dentro de un grupo de recursos**.
4. Seleccione un grupo de recursos.
5. Si el usuario no tiene todavía un rol otorgado para el grupo de recursos seleccionado, elija un rol para el campo **Asignar acceso a un grupo de recursos**. 

    En función del rol que seleccione, el usuario puede ver el grupo de recursos en su panel de control, editar el nombre del grupo de recursos o gestionar el acceso de usuarios al grupo. 
    
    Puede seleccionar **Sin acceso** si desea que el usuario solo tenga acceso al servicio {{site.data.keyword.la_full_notm}} en el grupo de recursos.

6. Seleccione **IBM Log Analysis with LogDNA**.
7. Seleccione el rol de **Administrador** de la plataforma.
8. Pulse **Asignar**.


## Cómo otorgar permisos a un usuario de DevOps para gestionar el servicio en la cuenta de {{site.data.keyword.cloud_notm}}
{: #devops_account}

Como **usuario de DevOps**, debe tener permisos para ejecutar las acciones siguientes: 

* Suministrar una instancia de servicio
* Suprimir una instancia de servicio
* Ver detalles de una instancia de servicio
* Crear un ID de servicio

Por lo tanto, necesita tener una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de plataforma **Editor**.

Siga los pasos siguientes para asignar a un usuario el rol de editor sobre el servicio {{site.data.keyword.la_full_notm}} en la cuenta: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso a recursos**.
4. Seleccione **IBM Log Analysis with LogDNA**.
5. Seleccione **Todas las instancias de servicio**.
6. Seleccione el rol de **Editor** de la plataforma.
7. Pulse Asignar.

## Cómo otorgar permisos a un usuario de DevOps para gestionar una instancia en la cuenta de {{site.data.keyword.cloud_notm}}
{: #devops_account_instance}

Siga los pasos siguientes para asignar a un usuario el rol de editor sobre una instancia del servicio {{site.data.keyword.la_full_notm}} en la cuenta: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso a recursos**.
4. Seleccione **IBM Log Analysis with LogDNA**.
5. Seleccione la instancia.
6. Seleccione el rol de **Editor** de la plataforma.
7. Pulse Asignar.



## Cómo otorgar permisos a un usuario de DevOps para gestionar el servicio dentro de un grupo de recursos
{: #devops_rg}

Como **usuario de DevOps**, debe tener permisos para ejecutar las acciones siguientes: 

* Suministrar una instancia de servicio
* Suprimir una instancia de servicio
* Ver detalles de una instancia de servicio
* Crear un ID de servicio

Por lo tanto, necesita una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de plataforma **Editor**.

Siga los pasos siguientes para asignar a un usuario el rol de editor sobre el servicio {{site.data.keyword.la_full_notm}} dentro del contexto de un grupo de recursos: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso dentro de un grupo de recursos**.
4. Seleccione un grupo de recursos.
5. Si el usuario no tiene todavía un rol otorgado para el grupo de recursos seleccionado, elija un rol para el campo **Asignar acceso a un grupo de recursos**. 

    En función del rol que seleccione, el usuario puede ver el grupo de recursos en su panel de control, editar el nombre del grupo de recursos o gestionar el acceso de usuarios al grupo. 
    
    Puede seleccionar **Sin acceso** si desea que el usuario solo tenga acceso al servicio {{site.data.keyword.la_full_notm}} en el grupo de recursos.

6. Seleccione **IBM Log Analysis with LogDNA**.
7. Seleccione el rol de **Editor** de la plataforma.
8. Pulse **Asignar**.

## Cómo otorgar permisos para gestionar registros y configurar alertas en LogDNA
{: #admin_user_logdna}

Como **usuario administrador** en LogDNA, debe tener permisos para ejecutar las acciones siguientes: 

* Añadir orígenes de registro de LogDNA
* Ver registros
* Buscar en registros
* Filtrar registros
* Configurar alertas

Por lo tanto, necesita las políticas siguientes:

* Una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de **Editor** de la plataforma. Esta política otorga permisos para ver los detalles de la instancia de servicio a través de la línea de mandatos y en el panel de control de {{site.data.keyword.cloud_notm}}.
* Una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de **Gestor** del servicio. Esta política otorga permisos para supervisar, filtrar y buscar en el registro, así como para definir alertas a través de la interfaz de usuario web de LogDNA.

**Nota:** como administrador del servicio, cuando otorgue a un usuario estas políticas, tenga en cuenta la posibilidad de hacerlo dentro del contexto de un grupo de recursos. Se suministra una instancia de {{site.data.keyword.la_full_notm}} dentro del contexto de un grupo de recursos. Por lo tanto, otorgue permisos de acceso dentro del contexto del grupo de recursos.


Siga los pasos siguientes para asignar a un usuario ambas políticas sobre el servicio {{site.data.keyword.la_full_notm}} dentro del contexto de un grupo de recursos: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso dentro de un grupo de recursos**.
4. Seleccione un grupo de recursos.
5. Si el usuario aún no tiene un rol otorgado para el grupo de recursos seleccionado, elija un rol para el campo **Asignar acceso a un grupo de recursos**. 

    En función del rol que seleccione, el usuario puede ver el grupo de recursos en su panel de control, editar el nombre del grupo de recursos o gestionar el acceso de usuarios al grupo. 
    
    Puede seleccionar **Sin acceso** si desea que el usuario solo tenga acceso al servicio {{site.data.keyword.la_full_notm}} en el grupo de recursos.

6. Seleccione **IBM Log Analysis with LogDNA**.
7. Seleccione el rol de **Editor** de la plataforma.
8. Seleccione el rol de **Gestor** del servicio.
8. Pulse **Asignar**.

## Cómo otorgar permisos a un usuario para ver registros en LogDNA
{: #user_logdna}

Como **usuario**, **auditor** o **desarrollador**, es posible que necesite permisos para ejecutar las siguientes acciones: 

* Ver registros
* Buscar en registros
* Filtrar registros

Por lo tanto, necesita las políticas siguientes:

* Una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de **Visor** de la plataforma. Esta política otorga permisos para ver los detalles de la instancia de servicio a través de la línea de mandatos y en el panel de control de {{site.data.keyword.cloud_notm}}.
* Una política de IAM para el servicio {{site.data.keyword.la_full_notm}} con el rol de servicio **Lector**. Esta política otorga permisos para ver, filtrar y buscar en los registros a través de la interfaz de usuario web de LogDNA.

**Nota:** como administrador del servicio, cuando otorgue a un usuario estas políticas, tenga en cuenta la posibilidad de hacerlo dentro del contexto de un grupo de recursos. Se suministra una instancia de {{site.data.keyword.la_full_notm}} dentro del contexto de un grupo de recursos. Por lo tanto, otorgue permisos de acceso a los usuarios dentro del contexto del grupo de recursos.

Siga los pasos siguientes para asignar a un usuario ambas políticas sobre el servicio {{site.data.keyword.la_full_notm}} dentro del contexto de un grupo de recursos: 

1. En la barra de menús, pulse **Gestionar** &gt; **Acceso (IAM)** y seleccione **Usuarios**.
2. En la fila del usuario al que desea asignar acceso, seleccione el menú **Acciones** y, a continuación, pulse **Asignar acceso**.
3. Seleccione **Asignar acceso dentro de un grupo de recursos**.
4. Seleccione un grupo de recursos.
5. Si el usuario aún no tiene un rol otorgado para el grupo de recursos seleccionado, elija un rol para el campo **Asignar acceso a un grupo de recursos**. 

    En función del rol que seleccione, el usuario puede ver el grupo de recursos en su panel de control, editar el nombre del grupo de recursos o gestionar el acceso de usuarios al grupo. 
    
    Puede seleccionar **Sin acceso** si desea que el usuario solo tenga acceso al servicio {{site.data.keyword.la_full_notm}} en el grupo de recursos.

6. Seleccione **IBM Log Analysis with LogDNA**.
7. Seleccione el rol de **Visor** de la plataforma.
8. Seleccione el rol de servicio **Lector**.
8. Pulse **Asignar**.

