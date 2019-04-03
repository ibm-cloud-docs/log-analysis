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

# 로그 정보 보기
{: #viewing_log_status}

[cf logging status](/docs/services/CloudLogAnalysis/reference/logging_cli.html#status1) 명령을 사용하여 로그 콜렉션에 수집해서 저장된 로그에 대한 정보를 얻습니다.
{:shortdesc}

## 일정 기간 동안의 로그에 대한 정보 얻기
{: #viewing_logs1}

`cf logging status` 명령을 사용하여 크기, 개수, 로그 유형 및 로그가 로그 콜렉션에 저장된 로그에 대해 Kibana에서 분석에 사용 가능한지 여부를 확인합니다. 

`cf logging status` 명령을 **-s** 옵션과 함께 사용하여 시작일을 설정하고 **-e**로 종료 날짜를 설정하십시오. 예:

* `cf logging status` - 최근 2주 동안의 정보를 제공합니다.
* `cf logging status -s 2017-05-03` - 2017년 5월 3일부터 현재 날짜까지의 정보를 제공합니다.
* `cf logging status -s 2017-05-03 -e 2017-05-08` - 2017년 5월 3일과 2017년 5월 8일 사이의 정보를 제공합니다. 

로그에 대한 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. *status* 명령을 실행하십시오.

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    예:
    
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


## 일정 기간 동안의 로그 유형에 대한 정보 얻기
{: #viewing_logs_by_log_type1}

일정 기간 동안의 로그 유형에 대한 정보를 얻으려면 `cf logging status` 명령을 **-t** 옵션과 함께 사용하여 로그의 유형을 지정하고, **-s**로 시작일을 설정하고, **-e**로 종료 날짜를 설정하십시오. 예:

* `cf logging status -t syslog` - 최근 2주 동안의 *syslog* 유형의 로그에 대한 정보를 제공합니다.
* `cf logging status -s 2017-05-03 -t syslog` - 2017년 5월 3일부터 현재 날짜까지의 *syslog* 유형의 로그에 대한 정보를 제공합니다.
* `cf logging status -s 2017-05-03 -e 2017-05-08 -t syslog` - 2017년 5월 3일과 2017년 5월 8일 사이의 *syslog* 유형의 로그에 대한 정보를 제공합니다. 

일정 기간 동안의 로그 유형에 대한 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. *status* 명령을 실행하십시오.

    ```
    ibmcloud cf logging status -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    여기서
    
    * *-s*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 시작 날짜를 설정하는 데 사용됨
    * *-e*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 종료 날짜를 설정하는 데 사용됨
    * *-t*는 로그 유형을 설정하는 데 사용됩니다.
    
    각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: **log_type_1,log_type_2,log_type_3**). 
    
    예:
    
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



## 로그에 대한 계정 정보 얻기
{: #viewing_logs_account1}

{{site.data.keyword.Bluemix_notm}} 계정에서 일정 기간 동안의 로그에 대한 정보를 얻으려면 `cf logging status` 명령을 **-a** 옵션과 함께 사용하십시오. 또한, 로그의 유형을 지정하기 위해 **-t** 옵션을 지정하고, **-s**로 시작일을 설정하고, **-e**로 종료 날짜를 설정할 수 있습니다. 

로그에 대한 계정 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. *status* 명령을 실행하십시오.

    ```
    ibmcloud cf logging status -a -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    여기서
    
    * *-a*는 계정 레벨 정보를 지정하는 데 사용됨
    * *-s*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 시작 날짜를 설정하는 데 사용됨
    * *-e*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 종료 날짜를 설정하는 데 사용됨
    * *-t*는 로그 유형을 설정하는 데 사용됩니다.
    

    각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: **log_type_1,log_type_2,log_type_3**). 
 
    예:
    
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














