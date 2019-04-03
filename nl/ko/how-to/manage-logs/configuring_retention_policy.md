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
{: #configuring_retention_policy1}

**cf logging option** 명령을 사용하여 로그 콜렉션에 로그가 보존되는 최대 일 수를 정의하는 보존 정책을 보고 구성합니다. 기본적으로 보존 정책은 사용 안함으로 설정되어 로그가 무기한 보관됩니다. 보존 기간이 만료된 후에 로그는 자동으로 삭제됩니다. 
{:shortdesc}

계정에 정의된 다른 보존 정책이 있을 수 있습니다. 글로벌 계정 정책과 개별 영역 정책이 있을 수 있습니다. 계정 레벨에서 설정한 보존 정책은 로그를 보존할 수 있는 최대 일 수를 설정합니다. 계정 레벨 기간보다 더 긴 기간에 대한 영역 보존 정책을 설정하는 경우, 적용된 정책이 해당 영역에 대해 구성하는 최근 정책입니다. 


## 영역에 대한 로그 보존 정책 사용 안함으로 설정
{: #disable_retention_policy_space1}

보존 정책을 사용하지 않으려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
    
2. 보존 기간을 **-1**로 설정하여 보존 기간을 사용 안함으로 설정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging option -r -1
    ```
    {: codeblock}
    
**예**
    
예를 들어, ID가 *d35da1e3-b345-475f-8502-cfgh436902a3*인 영역에 대한 보존 기간을 사용 안함으로 설정하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging option -r -1
```
{: codeblock}

출력은 다음과 같습니다.

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen} 



## 영역에 대한 로그 보존 정책 확인
{: #check_retention_policy_space1}

영역에 설정된 보존 기간을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
    
2. 보존 기간을 가져오십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging option
    ```
    {: codeblock}

    출력은 다음과 같습니다.

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## 계정의 모든 영역에 대한 로그 보존 정책 확인
{: #check_retention_policy_account}

계정의 각 영역에 설정된 보존 기간을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
    
2. 계정의 각 영역에 대한 보존 기간을 가져오십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging option -a
    ```
    {: codeblock}

    출력은 다음과 같습니다.

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    | fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## 계정 레벨 로그 보존 정책 설정
{: #set_retention_policy_space1}

계정에 대한 보존 기간을 보려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
    
2. 보존 기간을 설정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging option -r *Number_of_days* - a
    ```
    {: codeblock}
    
    여기서 *Number_of_days*는 로그를 보존하려는 일 수를 정의하는 정수입니다. 
    
    
**예**
    
예를 들어, 계정에서 모든 유형의 로그를 15일 동안만 보존하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging option -r 15 -a
```
{: codeblock}

출력은 보존 기간에 대한 정보를 포함한 계정의 각 영역에 대한 항목을 나열합니다.

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        15 |
+--------------------------------------+-----------+
| fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
+--------------------------------------+-----------+
```
{: screen}

## 영역에 대한 로그 보존 정책 설정
{: #set_retention_policy_account}

영역에 대한 보존 기간을 보려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
    
2. 보존 기간을 설정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging option -r *Number_of_days*
    ```
    {: codeblock}
    
    여기서 *Number_of_days*는 로그를 보존하려는 일 수를 정의하는 정수입니다.
    
    
**예**
    
예를 들어, 1년 동안 영역에서 사용 가능한 로그를 보존하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging option -r 365
```
{: codeblock}

출력은 다음과 같습니다.

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |       365 |
+--------------------------------------+-----------+
```
{: screen}


