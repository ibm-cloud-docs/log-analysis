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
{: #viewing_log_status1}

로그 콜렉션에 수집되고 저장된 로그에 대한 정보를 얻으려면 [ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#status) 명령을 사용하십시오. 크기, 레코드 수, 로그 유형 및 Kibana에서 분석에 로그를 사용할 수 있는지 여부에 대한 정보를 얻을 수 있습니다.
{:shortdesc}

## 일정 기간 동안의 로그에 대한 정보 얻기
{: #viewing_logs}

`ibmcloud logging log-show` 명령을 **-s** 옵션과 함께 사용하여 시작 날짜를 설정하고 **-e** 옵션으로 종료 날짜를 설정하십시오. 예:

* `ibmcloud logging log-show` - 최근 2주 동안의 정보를 제공합니다.
* `ibmcloud logging log-show -s 2017-05-03` - 2017년 5월 3일부터 현재 날짜까지의 정보를 제공합니다.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` - 2017년 5월 3일과 2017년 5월 8일 사이의 정보를 제공합니다. 

영역에 저장된 로그에 대한 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    예:
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## 일정 기간 동안의 로그 유형에 대한 정보 얻기
{: #viewing_logs_by_log_type}

일정 기간 동안의 특정 로그 유형에 대한 정보를 얻으려면 `ibmcloud logging log-show` 명령을 **-t** 옵션과 함께 사용하여 로그의 유형을 지정하고, **-s** 옵션으로 시작 날짜를 설정하고, **-e** 옵션으로 종료 날짜를 설정하십시오. 예:

* `ibmcloud logging log-show -t syslog` - 최근 2주 동안의 *syslog* 유형의 로그에 대한 정보를 제공합니다.
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` - 2017년 5월 3일부터 현재 날짜까지의 *syslog* 유형의 로그에 대한 정보를 제공합니다.
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` - 2017년 5월 3일과 2017년 5월 8일 사이의 *syslog* 유형의 로그에 대한 정보를 제공합니다. 

일정 기간 동안의 로그 유형에 대한 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging log-show -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    여기서
    
    * *-s*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 시작 날짜를 설정하는 데 사용됨
    * *-e*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 종료 날짜를 설정하는 데 사용됨
    * *-t*는 로그 유형을 설정하는 데 사용됩니다.
    
    각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: **log_type_1,log_type_2,log_type_3**). 
    
    예:
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## 계정 레벨의 로그에 대한 정보 얻기
{: #viewing_logs_account}

일정 기간 동안 계정 레벨에서 사용 가능한 로그에 대한 정보를 얻으려면 `ibmcloud logging log-show` 명령을 **-r account** 및 **-i** 옵션과 함께 사용하여 계정 ID를 설정하십시오. 또한, 로그의 유형을 지정하기 위해 **-t** 옵션을 지정하고, **-s**로 시작일을 설정하고, **-e**로 종료 날짜를 설정할 수 있습니다. 

로그에 대한 계정 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
	
2. 계정 ID를 가져오십시오.

    자세한 정보는 [계정의 GUID를 가져오는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)을 참조하십시오.
    
3. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging log-show -r account -i AccountID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    여기서
    
    * *-r account*는 로그에 대한 정보를 가져오려는 도메인을 설정하는 데 사용됩니다.
    * *-i AccountID*는 계정 ID를 설정하는 데 사용됩니다.
    * *-s*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 시작 날짜를 설정하는 데 사용됨
    * *-e*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 종료 날짜를 설정하는 데 사용됨
    * *-t*는 로그 유형을 설정하는 데 사용됩니다.

    각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: **log_type_1,log_type_2,log_type_3**). 
 
    예를 들어 계정 *123456789123456789567c9c8de6dece*에 대해 2017년 11월 17일에 계정 도메인으로 저장된 로그에 대한 정보를 표시하려면 다음 명령을 실행하십시오.
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## 조직 레벨의 로그에 대한 정보 얻기
{: #viewing_logs_org}

일정 기간 동안 조직 레벨에서 사용 가능한 로그에 대한 정보를 얻으려면 `ibmcloud logging log-show` 명령을 **-r org** 및 **-i** 옵션과 함께 사용하여 조직 ID를 설정하십시오. 또한, 로그의 유형을 지정하기 위해 **-t** 옵션을 지정하고, **-s**로 시작일을 설정하고, **-e**로 종료 날짜를 설정할 수 있습니다. 

로그에 대한 계정 정보를 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
	
2. 계정 ID를 가져오십시오.

    자세한 정보는 [조직의 GUID를 가져오는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#org_guid)을 참조하십시오.
    
3. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging log-show -r org -i OrgID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    여기서
    
    * *-r org*는 로그에 대한 정보를 가져오려는 도메인을 설정하는 데 사용됩니다.
    * *-i OrgID*는 조직 ID를 설정하는 데 사용됩니다.
    * *-s*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 시작 날짜를 설정하는 데 사용됨
    * *-e*는 UTC(Universal Coordinated Time), *YYYY-MM-DD*로 종료 날짜를 설정하는 데 사용됨
    * *-t*는 로그 유형을 설정하는 데 사용됩니다.
    
    각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: **log_type_1,log_type_2,log_type_3**). 
 
    예를 들어 ID가 *abcd56789123456789567c9c8de6dece*인 조직에 대해 2017년 11월 17일에 조직 도메인으로 저장된 로그에 대한 정보를 표시하려면 다음 명령을 실행하십시오.
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








