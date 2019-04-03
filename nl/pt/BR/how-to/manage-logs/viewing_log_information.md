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

# Visualizando informações de log
{: #viewing_log_status}

Use o comando [cf logging status](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#status1) para obter informações sobre os logs coletados e armazenados na Coleção de logs.
{:shortdesc}

## Obtendo informações sobre logs em um período de tempo
{: #viewing_logs1}

Use o comando `cf logging status` para ver o tamanho, a contagem, os tipos de log e se os logs estão disponíveis ou não para análise no Kibana para logs armazenados na Coleção de logs. 

Use o comando `cf logging status` com as opções **-s** para configurar o dia de início e **-e** para configurar a data de encerramento. Por exemplo:

* `cf logging status` fornece informações das duas últimas semanas.
* `cf logging status -s 2017-05-03` fornece informações de 3 de maio de 2017 até a data atual.
* `cf logging status -s 2017-05-03 -e 2017-05-08` fornece informações entre 3 de maio de 2017 e 8 de maio de 2017. 

Conclua as etapas a seguir para obter informações sobre logs:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Execute o comando *status*.

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    Por
exemplo,
    
    ```
    $ ibmcloud cf logging status +------------+--------+-------+--------------------+------------+ | DATE | COUNT | SIZE | TYPES | SEARCHABLE | +------------+--------+-------+--------------------+------------+ | 2017-05-24 | 16 | 3020 | log | None | +------------+--------+-------+--------------------+------------+ | 2017-05-25 | 1224 | 76115 | linux_syslog,log | All | +------------+--------+-------+--------------------+------------+
    ```
    {: screen}


## Obtendo informações sobre um tipo de log em um período de tempo
{: #viewing_logs_by_log_type1}

Para obter informações sobre um tipo de log em um período de tempo, use o comando `cf logging status` com as opções **-t** para especificar o tipo de log, **-s** para configurar o dia de início e **-e** para configurar a data de encerramento. Por
exemplo,

* `cf logging status -t syslog` fornece informações sobre logs do tipo *syslog* para as duas últimas semanas.
* `cf logging status -s 2017-05-03 -t syslog` fornece informações sobre logs do tipo *syslog* de 3 de maio de 2017 até a data atual.
* `cf logging status -s 2017-05-03 -e 2017-05-08 -t syslog` fornece informações sobre logs do tipo *syslog* entre 3 de maio de 2017 e 8 de maio de 2017. 

Conclua as etapas a seguir para obter informações sobre um tipo de log durante um período de tempo:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Execute o comando *status*.

    ```
    ibmcloud cf logging status -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    Em que
    
    * *-s* é usado para configurar a data de início em Universal Coordinated Time (UTC): *AAAA-MM-DD*
    * *-e* é usado para configurar a data de encerramento em Universal Coordinated Time (UTC): *AAAA-MM-DD*
    * *-t* é usado para configurar o tipo de log.
    
    É possível especificar múltiplos tipos de log separando cada tipo com uma vírgula, por exemplo, **log_type_1,log_type_2,log_type_3**. 
    
    Por
exemplo,
    
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



## Obtendo informações sobre logs de conta
{: #viewing_logs_account1}

Para obter informações sobre logs em um período de tempo na conta do {{site.data.keyword.Bluemix_notm}}, use o comando `cf logging status` com a opção **-a**. Também é possível especificar as opções **-t** para especificar o tipo de log, **-s** para configurar o dia de início e **-e** para configurar a data de encerramento. 

Conclua as etapas a seguir para obter dados da conta sobre logs:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Execute o comando *status*.

    ```
    ibmcloud cf logging status -a -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    Em que
    
    * *-a* é usado para especificar informações de nível de conta
    * *-s* é usado para configurar a data de início em Universal Coordinated Time (UTC): *AAAA-MM-DD*
    * *-e* é usado para configurar a data de encerramento em Universal Coordinated Time (UTC): *AAAA-MM-DD*
    * *-t* é usado para configurar o tipo de log.
    

    É possível especificar múltiplos tipos de log separando cada tipo com uma vírgula, por exemplo, **log_type_1,log_type_2,log_type_3**. 
 
    Por
exemplo,
    
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














