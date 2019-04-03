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

# 로그 보존 정책 구성
{: #configuring_retention_policy}

기본적으로 보존 정책은 사용 안함으로 설정되어 로그가 무기한 보관됩니다. 보존 정책을 변경하려면 **ibmcloud logging option-update** 명령을 사용하십시오.
{:shortdesc}

**ibmcloud logging option-show** 명령을 사용하여 로그 콜렉션에 로그가 보존되는 최대 일 수를 정의하는 보존 정책을 볼 수 있습니다. 

보존 기간을 설정하면 보존 기간이 만료된 후에 로그가 자동으로 삭제됩니다.


## 계정에 대한 로그 보존 정책 사용 안함으로 설정
{: #disable_retention_policy_acc}

보존 정책을 사용하지 않으면 모든 로그가 보관됩니다. 

보존 정책을 사용하지 않으려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
	
2. 계정 ID를 가져오십시오.

    자세한 정보는 [계정의 GUID를 가져오는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)을 참조하십시오.
    
3. 보존 기간을 **-1**로 설정하여 보존 기간을 사용 안함으로 설정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE는 일 수를 정의하는 숫자입니다.
    
**예**
    
예를 들어 ID가 *12345677fgh436902a3*인 계정에 대한 보존 기간을 사용 안함으로 설정하려면 다음 명령을 실행하십시오.

```
ibmcloud logging option-update -r account -i 12345677fgh436902a3 -e -1
```
{: codeblock}


## 영역에 대한 로그 보존 정책 사용 안함으로 설정
{: #disable_retention_policy_space}

보존 정책을 사용하지 않으면 모든 로그가 보관됩니다.  

보존 정책을 사용하지 않으려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 보존 기간을 **-1**로 설정하여 보존 기간을 사용 안함으로 설정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging option-show -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE는 일 수를 정의하는 숫자입니다.
    
**예**
    
예를 들어, ID가 *d35da1e3-b345-475f-8502-cfgh436902a3*인 영역에 대한 보존 기간을 사용 안함으로 설정하려면 다음 명령을 실행하십시오.

```
ibmcloud logging option-update -e -1
```
{: codeblock}


## 계정에 대한 로그 보존 정책 확인
{: #check_retention_policy_acc}

계정에 대해 설정된 보존 기간을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

2. 계정 ID를 가져오십시오.

    자세한 정보는 [계정의 GUID를 가져오는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)을 참조하십시오.
    
3. 보존 기간을 가져오십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging option-show -r account -i AccountID
    ```
    {: codeblock}

    출력은 다음과 같습니다.

    ```
    ibmcloud logging option-show -r account -i kjskdsjfksjdflkjdsfbbd06461b066
    Showing log options of resource: kjskdsjfksjdflkjdsfbbd06461b066 ...

    Resource ID                              Retention   
    a:kjskdsjfksjdflkjdsfbbd06461b066       30   
	```
    {: screen}
	
## 영역에 대한 로그 보존 정책 확인
{: #check_retention_policy_space}

영역에 설정된 보존 기간을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 보존 기간을 가져오십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging option-show
    ```
    {: codeblock}

    출력은 다음과 같습니다.

    ```
    ibmcloud logging option-show
    Showing log options of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    SpaceId                                Retention   
    12345678-1234-2edr-a9de-378620d6fab5   30   
	```
    {: screen}
    


## 계정 레벨 로그 보존 정책 설정
{: #set_retention_policy_acc}

다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

2. 계정 ID를 가져오십시오.

    자세한 정보는 [계정의 GUID를 가져오는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)을 참조하십시오.
    
3. 보존 기간을 설정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
    ```
    {: codeblock}
    
    여기서 *RETENTION_VALUE*는 로그를 보존할 일 수를 정의하는 정수입니다. 
    
    
**예**
    
예를 들어, 계정에서 모든 유형의 로그를 15일 동안만 보존하려면 다음 명령을 실행하십시오.

```
ibmcloud logging option-update -r account -i AccountID -e 15
```
{: codeblock}



## 영역에 대한 로그 보존 정책 설정
{: #set_retention_policy_space}

영역에 대한 보존 기간을 보려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.
    
2. 보존 기간을 설정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud logging option-update -e RETENTION_VALUE
    ```
    {: codeblock}
    
    여기서 *RETENTION_VALUE*는 로그를 보존할 일 수를 정의하는 정수입니다.
    
    
**예**
    
예를 들어, 1년 동안 영역에서 사용 가능한 로그를 보존하려면 다음 명령을 실행하십시오.

```
ibmcloud logging option-update -e 365
```
{: codeblock}




