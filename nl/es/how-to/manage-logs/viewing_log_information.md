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
{: #viewing_log_status}

Utilice el mandato [cf logging status](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#status1) para obtener información sobre los registros que se recopilan y almacenan en el componente de recopilación de registros.
{:shortdesc}

## Obtención de información sobre los registros durante un periodo de tiempo
{: #viewing_logs1}

Utilice el mandato `cf logging status` para ver el tamaño, recuento, tipos de registros y si los registros están o no disponibles para su análisis en Kibana para los registros que se almacenan en el componente de recopilación de registros. 

Utilice el mandato `cf logging status` con las opciones **-s** para definir la fecha inicial y **-e** para definir la fecha final. Por ejemplo:

* `cf logging status` ofrece información correspondiente a las 2 últimas semanas.
* `cf logging status -s 2017-05-03` ofrece información comprendida entre el 3 de mayo de 2017 y el día de hoy.
* `cf logging status -s 2017-05-03 -e 2017-05-08` ofrece información comprendida entre el 3 de mayo de 2017 y el 8 de mayo de 2017. 

Siga estos pasos para obtener para obtener información sobre los registros:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Ejecute el mandato *status*.

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Por ejemplo,
    
    ```
    $ ibmcloud cf logging status
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}


## Obtención de información sobre un tipo de registro durante un periodo de tiempo
{: #viewing_logs_by_log_type1}

Para obtener información sobre un tipo de registro durante un periodo de tiempo, utilice el mandato `cf logging status` con las opciones **-t** para especificar el tipo de registro, **-s** para definir la fecha inicial y **-e** para definir la fecha final. Por ejemplo,

* `cf logging status -t syslog` proporciona información sobre los registros de tipo *syslog* durante las 2 últimas semanas.
* `cf logging status -s 2017-05-03 -t syslog` proporciona información sobre los registros de tipo *syslog* comprendido entre el 3 de mayo de 2017 y el día de hoy.
* `cf logging status -s 2017-05-03 -e 2017-05-08 -t syslog` proporciona información sobre los registros de tipo *syslog* entre el 3 de mayo de 2017 y el 8 de mayo de 2017. 

Siga estos pasos para obtener información sobre un tipo de registro durante un periodo de tiempo:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Ejecute el mandato *status*.

    ```
    ibmcloud cf logging status -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    donde
    
    * *-s* se utiliza para definir la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-e* se utiliza para definir la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-t* se utiliza para definir el tipo de registro.
    
    Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo **log_type_1,log_type_2,log_type_3**. 
    
    Por ejemplo,
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}



## Obtención de información de cuenta sobre los registros
{: #viewing_logs_account1}

Para obtener información sobre los registros durante un periodo de tiempo de la cuenta de {{site.data.keyword.Bluemix_notm}}, utilice el mandato `cf logging status` con la opción **-a**. También puede especificar las opciones **-t** para especificar el tipo de registro, **-s** para definir la fecha inicial y **-e** para definir la fecha final. 

Siga estos pasos para obtener para obtener información de la cuenta sobre los registros:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Ejecute el mandato *status*.

    ```
    ibmcloud cf logging status -a -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    donde
    
    * *-a* se utiliza para especificar información de nivel de cuenta
    * *-s* se utiliza para definir la fecha inicial en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-e* se utiliza para definir la fecha final en hora universal coordinada (UTC): *AAAA-MM-DD*
    * *-t* se utiliza para definir el tipo de registro.
    

    Puede especificar varios tipos de registro separando cada tipo con una coma, por ejemplo **log_type_1,log_type_2,log_type_3**. 
 
    Por ejemplo,
    
    ```
    $ ibmcloud cf logging status -s 2017-05-24 -e 2017-05-25 -t log -a
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 |        log         |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}














