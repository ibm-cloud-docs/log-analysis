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

# Como otorgar permisos para gestionar registros y visualizar registros de cuentas
{: #grant_permissions}

En {{site.data.keyword.Bluemix}}, puede asignar a un usuario uno o varios roles de IAM. Estos roles definen qué tareas están habilitadas para dicho usuario para trabajar con el servicio de {{site.data.keyword.loganalysisshort}}.  
{:shortdesc}

Por ejemplo, puede otorgar a un usuario el rol de **operador** para que pueda gestionar registros. Si sólo desea que un usuario visualice los registros de la cuenta, puede otorgar al usuario el rol de **visor**. Para obtener más información, consulte [Roles de IAM](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).

**Nota:** 

* Para otorgar a un usuario permisos para gestionar registros o para ver registros de una cuenta, debe tener permisos para asignar políticas a otros usuarios en la cuenta, o bien debe ser el propietario de la cuenta. Si no es el propietario de la cuenta, debe tener una política de IAM con el rol de editor, operador o administrador.
* Para otorgar a un usuario permisos para ver registros en un espacio, debe tener permisos en la organización y en el espacio para asignar al
usuario un rol de Cloud Foundry que describa las acciones que puede realizar este usuario con el servicio {{site.data.keyword.loganalysisshort}} en este espacio. 

## Asignación de una política de IAM a un usuario mediante la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_account}

Complete los pasos siguientes para otorgar permisos a un usuario para trabajar con el servicio de {{site.data.keyword.loganalysisshort}}:

1. Inicie sesión en la consola de {{site.data.keyword.Bluemix_notm}}.

    Abra un navegador web y lance el panel de control de {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window}
	
	Cuando inicia sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}.

2. En la barra de menús, pulse **Gestionar > Cuenta > Usuarios**. 

    La ventana *Usuarios* muestra una lista de usuarios con sus direcciones de correo electrónico para la cuenta seleccionada actualmente.
	
3. Si el usuario es un miembro de la cuenta, seleccione el nombre de usuario de la lista, o pulse **Gestionar usuario** del menú *Acciones*.

    Si el usuario no es un miembro de la cuenta, consulte [Invitación a usuarios](/docs/iam/iamuserinv.html#iamuserinv).

4. En la sección **Políticas de acceso**, pulse **Asignar un acceso** y, a continuación, seleccione **Asignar acceso a recursos**.

    Se abrirá la ventana *Asignar acceso de recursos al usuario**.

5. Especifique la información sobre la política. La tabla siguiente lista los campos necesarios para definir una política: 

    <table>
	  <caption>Lista de campos para configurar una política IAM.</caption>
	  <tr>
	    <th>Campo</th>
		<th>Valor</th>
	  </tr>
	  <tr>
	    <td>Servicios</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>Regiones</td>
		<td>Puede especificar las regiones en las que se otorgará acceso al usuario para trabajar con registros. Seleccione una o varias regiones individualmente, o seleccione **Todas las regiones actuales** para otorgar acceso a todas las regiones.</td>
	  </tr>
	  <tr>
	    <td>Instancia de servicio</td>
		<td>Seleccione *Todas las instancias de servicio*.</td>
	  </tr>
	  <tr>
	    <td>Roles</td>
		<td>Seleccione uno o varios roles de IAM. <br>Los roles válidos son: *administrador*, *operador*, *editor*, y *visor*. <br>Para obtener más información sobre las acciones que están permitidas por rol, consulte [Roles de IAM](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles).
		</td>
	  </tr>
     </table>
	
6. Pulse **Asignar**.
	
La política que configure es aplicable a las regiones seleccionadas. 


## Asignación de una política de IAM a un usuario mediante la línea de mandatos
{: #grant_permissions_commandline}

Siga los pasos siguientes para otorgar a un usuario acceso para ver registros de cuenta mediante la línea de mandatos:

1. Desde un terminal, inicie una sesión en la cuenta de {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Compruebe que el usuario es un miembro de la cuenta. Ejecute el siguiente mandato para obtener la lista de usuarios de la cuenta:

    ```
	ibmcloud account users
	```
    {: codeblock}	

	Se muestra una lista de usuarios con sus GUID.

3. Si el usuario no es miembro de la cuenta, póngase en contacto con el propietario de la cuenta y solicite una invitación a la cuenta para el usuario. Para obtener más información, consulte [Invitación a usuarios](/docs/iam/iamuserinv.html#iamuserinv).

    **Consejo:** El mandato para invitar a un usuario a una cuenta es el siguiente: `ibmcloud iam account-user-invite USER_EMAIL`
		
4. Asigne una política al usuario. Ejecute el mandato siguiente:

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	donde
    * USER_NAME es el ID de {{site.data.keyword.Bluemix_notm}} del usuario.
	* ROLE es un rol de IAM. Los valores válidos son: *administrator*, *operator*, *editor* y *viewer*.

5. Compruebe que la política se haya asignado al usuario. Ejecute el siguiente mandato para obtener una lista de todas las políticas asignadas a un usuario:

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## Cómo otorgar a un usuario permisos para ver registros del espacio mediante la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}
{: #grant_permissions_ui_space}

Para otorgar permisos a un usuario para ver registros en un espacio, debe asignar al usuario un rol de Cloud Foundry que describa las acciones que puede realizar este usuario con el servicio {{site.data.keyword.loganalysisshort}} en el espacio. 

Complete los pasos siguientes para otorgar permisos a un usuario para trabajar con el servicio de {{site.data.keyword.loganalysisshort}}:

1. Inicie sesión en la consola de {{site.data.keyword.Bluemix_notm}}.

    Abra un navegador web y lance el panel de control de {{site.data.keyword.Bluemix_notm}}: [http://bluemix.net ![Icono de enlace externo](../../../icons/launch-glyph.svg "Icono de enlace externo")](http://bluemix.net){:new_window}
	
	Cuando inicia sesión con su ID de usuario y su contraseña, se abre la interfaz de usuario de {{site.data.keyword.Bluemix_notm}}.

2. En la barra de menús, pulse **Gestionar > Cuenta > Usuarios**. 

    La ventana *Usuarios* muestra una lista de usuarios con sus direcciones de correo electrónico para la cuenta seleccionada actualmente.
	
3. Si el usuario es un miembro de la cuenta, seleccione el nombre de usuario de la lista, o pulse **Gestionar usuario** del menú *Acciones*.

    Si el usuario no es un miembro de la cuenta, consulte [Invitación a usuarios](/docs/iam/iamuserinv.html#iamuserinv).

4. Seleccione **Acceso de Cloud Foundry** y, a continuación, seleccione la organización.

    Se listará la lista de espacios disponibles en dicha organización.

5. Elija un espacio. A continuación, desde la acción de menú, seleccione **Editar el rol de espacio**.

6. Seleccione uno o más roles de espacio. Los roles válidos son: *Gestor*, *Desarrollador* y *Auditor*
	
7. Pulse **Guardar rol**.




