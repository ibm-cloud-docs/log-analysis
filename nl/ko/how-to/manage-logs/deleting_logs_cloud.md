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

# 로그 삭제
{: #deleting_logs}

로그 콜렉션에서 로그를 삭제하려면 [ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) 명령을 사용하십시오. 
{:shortdesc}

* 특정 시간 범위 내의 로그를 삭제할 수 있습니다.
* 유형별 로그를 삭제할 수 있습니다. 각 로그 파일에는 한 유형의 로그 항목만 있습니다.
* 영역, 조직 또는 계정 도메인에 대한 로그를 삭제할 수 있습니다.


## 특정 기간의 모든 로그 삭제
{: #time_range}

다음 단계를 사용하여 특정 기간 동안 영역 도메인에 저장된 모든 로그를 삭제합니다.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 다음 명령을 실행하여 로그 콜렉션에서 사용할 수 있는 로그를 확인하십시오.

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    예:
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-abcd-4193-aere-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 특정일에 저장된 로그를 삭제하십시오.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	여기서
	
	* *-s*는 시작 날짜를 협정 세계시(UTC)를 사용하여 YYYY-MM-DD로 설정합니다(예: 2006-01-02).
    * *-e*는 종료 날짜를 협정 세계시(UTC)를 사용하여 YYYY-MM-DD로 설정합니다.
    	
	예를 들어 2017년 5월 25일의 로그를 삭제하려면 다음 명령을 실행하십시오.
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## 특정 기간 동안의 로그 유형별 로그 삭제 
{: #log_type}

특정 기간 동안 영역 도메인에 저장된 로그를 로그 유형별로 삭제하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 다음 명령을 실행하여 로그 콜렉션에서 사용할 수 있는 로그를 확인하십시오.

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    예:
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 특정일에 저장된 로그를 삭제하십시오.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	여기서
	
	* *-s*는 시작 날짜를 협정 세계시(UTC)를 사용하여 YYYY-MM-DD로 설정합니다(예: 2006-01-02).
    * *-e*는 종료 날짜를 협정 세계시(UTC)를 사용하여 YYYY-MM-DD로 설정합니다.
	* *-t*는 로그 유형을 설정합니다.
    	
	예를 들어 2017년 5월 25일에 생성된 linux_syslog 유형의 로그를 삭제하려면 다음 명령을 실행하십시오.
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## 특정 기간 동안의 로그 유형별 계정 로그 삭제 
{: #time_range_acc}

다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
	
2. 계정 ID를 가져오십시오.

    자세한 정보는 [계정의 GUID를 가져오는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)을 참조하십시오.
    
3. 다음 명령을 실행하여 로그 콜렉션에서 사용할 수 있는 로그를 계정 레벨에서 확인하십시오.

    ```
    ibmcloud logging log-show  -r account -i AccountID
    ```
    {: codeblock}
    
    예:
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    All                 default
	2017-05-25   2000       76115   All                 linux_syslog,log
    2017-05-26   195678     17639   All                 default,linux_syslog    
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}
	
4. 특정일에 저장된 로그를 삭제하십시오.

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType -r account -i AccountID
	```
	{: codeblock}
	
	여기서
	
	* *-s*는 시작 날짜를 협정 세계시(UTC)를 사용하여 YYYY-MM-DD로 설정합니다(예: 2006-01-02).
    * *-e*는 종료 날짜를 협정 세계시(UTC)를 사용하여 YYYY-MM-DD로 설정합니다.
	* *-t*는 로그 유형을 설정합니다.
    	
	예를 들어 2017년 5월 25일에 로그 콜렉션에서 계정 레벨로 저장된 linux_syslog 유형의 로그를 삭제하려면 다음 명령을 실행하십시오.
	
	```
	ibmcloud logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -r account -i 123456789123456789567c9c8de6dece
	```
	{: screen}
	












