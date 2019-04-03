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

# Configuración de la política de retención de registros
{: #configuring_retention_policy}

De forma predeterminada, la política de retención está inhabilitada y los registros se conservan indefinidamente. Utilice el mandato **ibmcloud logging option-update** para modificar la política de retención.
{:shortdesc}

Puede utilizar el mandato **ibmcloud logging option-show** para ver la política de retención que define el número máximo de días que se conservan los registros en el componente de recopilación de registros. 

Si define una política de retención, una vez transcurrido el periodo de retención, los registros se suprimen automáticamente.


## Inhabilitación de la política de retención de registros para una cuenta
{: #disable_retention_policy_acc}

Cuando se inhabilita la política de retención, se conservan todos los registros. 

Siga los siguientes pasos para inhabilitar una política de retención:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
2. Obtenga el ID de cuenta.

    Para obtener más información, consulte [¿Cómo se obtiene el GUID de una cuenta?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)
    
3. Establezca el periodo de retención en **-1** para inhabilitar el periodo de retención. Ejecute el mandato:

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE es un valor numérico que define el número de días.
    
**Ejemplo**
    
Por ejemplo, para inhabilitar el periodo de retención para una cuenta con el ID *12345677fgh436902a3*, ejecute el siguiente mandato:

```
ibmcloud logging option-update -r account -i 12345677fgh436902a3 -e -1
```
{: codeblock}


## Inhabilitación de la política de retención de registros para un espacio
{: #disable_retention_policy_space}

Cuando se inhabilita la política de retención, se conservan todos los registros.  

Siga los siguientes pasos para inhabilitar una política de retención:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Establezca el periodo de retención en **-1** para inhabilitar el periodo de retención. Ejecute el mandato:

    ```
    ibmcloud logging option-show -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE es un valor numérico que define el número de días.
    
**Ejemplo**
    
Por ejemplo, para inhabilitar el periodo de retención para un espacio con el ID *d35da1e3-b345-475f-8502-cfgh436902a3*, ejecute el siguiente mandato:

```
ibmcloud logging option-update -e -1
```
{: codeblock}


## Comprobación de la política de retención de registros para una cuenta
{: #check_retention_policy_acc}

Para obtener el periodo de retención establecido para una cuenta, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

2. Obtenga el ID de cuenta.

    Para obtener más información, consulte [¿Cómo se obtiene el GUID de una cuenta?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)
    
3. Obtenga el periodo de retención. Ejecute el mandato:

    ```
    ibmcloud logging option-show -r account -i AccountID
    ```
    {: codeblock}

    La salida es:

    ```
    ibmcloud logging option-show -r account -i kjskdsjfksjdflkjdsfbbd06461b066
    Showing log options of resource: kjskdsjfksjdflkjdsfbbd06461b066 ...

    Resource ID                              Retention   
    a:kjskdsjfksjdflkjdsfbbd06461b066       30   
	```
    {: screen}
	
## Comprobación de la política de retención de registros para un espacio
{: #check_retention_policy_space}

Para obtener el periodo de retención establecido para un espacio, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Obtenga el periodo de retención. Ejecute el mandato:

    ```
    ibmcloud logging option-show
    ```
    {: codeblock}

    La salida es:

    ```
    ibmcloud logging option-show
    Showing log options of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    SpaceId                                Retention   
    12345678-1234-2edr-a9de-378620d6fab5   30   
	```
    {: screen}
    


## Establecimiento de una política de retención de registros a nivel de cuenta
{: #set_retention_policy_acc}

Siga estos pasos:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

2. Obtenga el ID de cuenta.

    Para obtener más información, consulte [¿Cómo se obtiene el GUID de una cuenta?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)
    
3. Establezca el periodo de retención. Ejecute el mandato:

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
    ```
    {: codeblock}
    
    donde *RETENTION_VALUE* es un entero que define el número de días que desea conservar los registros. 
    
    
**Ejemplo**
    
Por ejemplo, para conservar cualquier tipo de registro en su cuenta durante solo 15 días, ejecute el mandato siguiente:

```
ibmcloud logging option-update -r account -i AccountID -e 15
```
{: codeblock}



## Establecimiento de la política de retención de registros para un espacio
{: #set_retention_policy_space}

Para ver el periodo de retención correspondiente a un espacio, siga los pasos siguientes:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Establezca el periodo de retención. Ejecute el mandato:

    ```
    ibmcloud logging option-update -e RETENTION_VALUE
    ```
    {: codeblock}
    
    donde *RETENTION_VALUE* es un entero que define el número de días que desea conservar los registros.
    
    
**Ejemplo**
    
Por ejemplo, para conservar los registros disponibles en un espacio durante un año, ejecute el
siguiente
mandato:

```
ibmcloud logging option-update -e 365
```
{: codeblock}




