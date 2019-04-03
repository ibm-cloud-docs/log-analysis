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

# Visualización de la información de registro
{: #viewing_log_status1}

Utilice el mandato [ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#status) para obtener información sobre los registros que se recopilan y almacenan en el componente de recopilación de registros. Puede obtener información sobre el tamaño, el número de registros, los tipos de registro y si los registros están disponibles o no para su análisis en Kibana.
{:shortdesc}

## Obtención de información sobre los registros durante un periodo de tiempo
{: #viewing_logs}

Utilice el mandato `ibmcloud logging log-show` con las opciones **-s** para definir la fecha inicial y **-e** para definir la fecha final. Por ejemplo:

* `ibmcloud logging log-show` ofrece información correspondiente a las 2 últimas semanas.
* `ibmcloud logging log-show -s 2017-05-03` ofrece información comprendida entre el 3 de mayo de 2017 y el día de hoy.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` ofrece información comprendida entre el 3 de mayo de 2017 y el 8 de mayo de 2017. 

Siga estos pasos para obtener para obtener información sobre los registros almacenados en un espacio:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Ejecute el mandato siguiente:

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    Por ejemplo,
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## Obtención de información sobre un tipo de registro durante un periodo de tiempo
{: #viewing_logs_by_log_type}

Para obtener información sobre un tipo de registro durante un periodo de tiempo, utilice el mandato `ibmcloud logging log-show` con las opciones **-t** para especificar el tipo de registro, **-s** para definir la fecha inicial y **-e** para definir la fecha final. Por ejemplo,

* `ibmcloud logging log-show -t syslog` proporciona información sobre los registros de tipo *syslog* durante las 2 últimas semanas.
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` proporciona información sobre los registros de tipo *syslog* comprendido entre el 3 de mayo de 2017 y el día de hoy.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` proporciona información sobre los registros de tipo *syslog* entre el 3 de mayo de 2017 y el 8 de mayo de 2017. 

Siga estos pasos para obtener información sobre un tipo de registro durante un periodo de tiempo:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Ejecute el mandato siguiente:

    ```
    ibmcloud logging log-show -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    donde
    
    * *-s* se utiliza para definir la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-e* se utiliza para definir la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-t* se utiliza para definir el tipo de registro.
    
    Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo **log_type_1,log_type_2,log_type_3**. 
    
    Por ejemplo,
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## Obtención de información sobre los registros a nivel de cuenta
{: #viewing_logs_account}

Para obtener información sobre los registros que están disponibles a nivel de cuenta durante un periodo de tiempo, utilice el mandato `ibmcloud logging log-show` con la opción **-r account** e **-i** para definir el ID de la cuenta. También puede especificar las opciones **-t** para especificar el tipo de registro, **-s** para definir la fecha inicial y **-e** para definir la fecha final. 

Siga estos pasos para obtener para obtener información de la cuenta sobre los registros:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Obtenga el ID de cuenta.

    Para obtener más información, consulte [¿Cómo se obtiene el GUID de una cuenta?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)
    
3. Ejecute el mandato siguiente:

    ```
    ibmcloud logging log-show -r account -i AccountID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    donde
    
    * *-r account* se utiliza para definir el dominio en el que desea obtener información sobre los registros.
    * *-i AccountID* se utiliza para definir el ID de la cuenta.
    * *-s* se utiliza para definir la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-e* se utiliza para definir la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-t* se utiliza para definir el tipo de registro.

    Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo **log_type_1,log_type_2,log_type_3**. 
 
    Por ejemplo, para ver información sobre los registros almacenados correspondientes al 17 de noviembre de 2017 a nivel de cuenta para la cuenta *123456789123456789567c9c8de6dece*, ejecute el siguiente mandato:
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## Obtención de información sobre los registros a nivel de organización
{: #viewing_logs_org}

Para obtener información sobre los registros que están disponibles a nivel de organización durante un periodo de tiempo, utilice el mandato `ibmcloud logging log-show` con la opción **-r org** e **-i** para definir el ID de la organización. También puede especificar las opciones **-t** para especificar el tipo de registro, **-s** para definir la fecha inicial y **-e** para definir la fecha final. 

Siga estos pasos para obtener para obtener información de la cuenta sobre los registros:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
2. Obtenga el ID de cuenta.

    Para obtener más información, consulte [¿Cómo se obtiene el GUID de una organización?](/docs/services/CloudLogAnalysis/qa/cli_qa.html#org_guid)
    
3. Ejecute el mandato siguiente:

    ```
    ibmcloud logging log-show -r org -i OrgID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    donde
    
    * *-r org* se utiliza para definir el dominio en el que desea obtener información sobre los registros.
    * *-i OrgID* se utiliza para definir el ID de la organización.
    * *-s* se utiliza para definir la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-e* se utiliza para definir la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-t* se utiliza para definir el tipo de registro.
    
    Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo **log_type_1,log_type_2,log_type_3**. 
 
    Por ejemplo, para ver información sobre los registros almacenados correspondientes al 17 de noviembre de 2017 en el dominio de organización para la organización con ID *abcd56789123456789567c9c8de6dece*, ejecute el siguiente mandato:
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








