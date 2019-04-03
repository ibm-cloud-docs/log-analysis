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

# 로그 다운로드
{: #downloading_logs1}

로그를 로컬 파일에 다운로드하거나 데이터를 다른 프로그램으로 보낼 수 있습니다. 세션의 컨텍스트 내에서 로그를 다운로드합니다. 세션은 어떤 로그를 다운로드할 것인지 지정합니다. 로그의 다운로드가 중단된 경우, 세션은 다운로드가 중지된 지점에서 다운로드를 재개할 수 있습니다. 다운로드가 완료된 후에는 세션을 삭제해야 합니다.
{:shortdesc}

{{site.data.keyword.Bluemix_notm}} 영역에서 사용 가능한 로그 데이터를 로컬 파일에 다운로드하려면 다음 단계를 완료하십시오.

## 1단계: IBM Cloud에 로그인

{{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

## 2단계: 사용 가능한 로그 식별
{: #step31}

1. `ibmcloud cf logging status` 명령을 사용하여 최근 2주 동안의 사용 가능한 로그를 확인하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    예를 들면, 이 명령을 실행하면 출력은 다음과 같습니다.
    
    ```
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}

    **참고:** {{site.data.keyword.loganalysisshort}} 서비스는 협정 세계시(UTC)를 사용하는 글로벌 서비스입니다. 일은 UTC 일로 정의됩니다. 특정 로컬 시간 일에 대한 로그를 가져오기 위해 여러 개의 UTC 일을 다운로드해야 할 수 있습니다.


## 3단계: 세션 작성
{: #step32}

세션은 다운로드의 상태를 유지하고, 다운로드할 수 있는 로그 데이터의 범위를 정의하기 위해 필요합니다. 

[cf logging session create](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) 명령을 사용하여 세션을 작성하십시오. 선택사항으로 시작 날짜, 종료 날짜 및 세션 작성 시 로그의 유형을 지정할 수 있습니다.  

* 시작 날짜 및 종료 날짜를 지정하면 세션은 해당 날짜가 포함된 범위에서 로그에 대한 액세스를 제공합니다. 
* 로그의 유형(**-t**)을 지정하면 세션은 특정 유형의 로그에 대한 액세스를 제공합니다. 사용자가 관심이 있는 작은 서브세트의 로그로만 세션의 범위를 정할 수 있기 때문에 범위에서 로그를 관리할 때 중요한 기능입니다.

**참고:** 각 세션에 대해 최대 15일 동안의 로그를 다운로드할 수 있습니다.

*log* 유형의 로그를 다운로드하는 데 사용되는 세션을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging session create -t log
```
{: codeblock}

세션은 다음과 같은 정보를 리턴합니다.

* 다운로드할 날짜 범위. 기본값은 현재 UTC 날짜입니다.
* 다운로드할 로그 유형. 기본적으로 세션을 작성할 때 지정하는 기간에 사용 가능한 모든 로그 유형이 포함됩니다. 
* 전체 계정을 포함할 것인지 현재 영역만 포함할 것인지 여부에 대한 정보. 기본적으로 사용자가 로그인한 영역의 로그를 가져옵니다.
* 로그를 다운로드하는 데 필요한 세션 ID.

예:

```
$ ibmcloud cf logging session create -t log     
+--------------+--------------------------------------+
|     NAME     |                VALUE                 |
+--------------+--------------------------------------+
| Access-Time  | 2017-05-25T18:04:21.743792338Z       |
| Create-Time  | 2017-05-25T18:04:21.743792338Z       |
| Date-Range   | {                                    |
|              |  "End": "2017-05-25T00:00:00Z",      |
|              |  "Start": "2017-05-25T00:00:00Z"     |
|              | }                                    |
| Id           | -jshdjsunelsssr4566722==             |
| Space        | fdgrghg3-b090-4567-vvfg-afbc436902a3 |
| Type-Account | {                                    |
|              |  "Type": "log"                       |
|              | }                                    |
| Username     | xxx@yyy.com                          |
+--------------+--------------------------------------+
```
{: screen}

**팁:** 활성 세션의 목록을 보려면 [cf logging session list](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_list1) 명령을 실행하십시오.

## 4단계: 파일에 로그 데이터 다운로드
{: #step42}

세션 매개변수에 의해 지정된 로그를 다운로드하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging download -o Log_File_Name Session_ID
```
{: codeblock}

여기서

* Log_File_Name은 출력 파일의 이름입니다.
* Session_ID는 세션의 GUID입니다. 이전 단계에서 이 값을 얻습니다.

예:

```
ibmcloud cf logging download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

로그가 다운로드되면서 진행 표시기가 0에서 100%로 이동합니다.

**참고:** 

* 다운로드된 데이터의 형식은 압축된 JSON입니다. .gz 파일의 압축을 풀고 열면 JSON 형식의 데이터를 볼 수 있습니다. 
* 압축된 JSON은 ElasticSearch 또는 Logstash에서 수집하기에 적합합니다. -o가 제공되지 않는 경우, 데이터는 사용자의 ELK 스택으로 직접 보낼 수 있도록 stdout로 스트림됩니다.
* JSON을 구문 분석할 수 있는 모든 프로그램으로 데이터를 처리할 수도 있습니다. 

## 5단계: 세션 삭제
{: #step51}

다운로드가 완료된 후에 [cf logging session delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_delete1) 명령을 사용하여 세션을 삭제해야 합니다. 

세션을 삭제하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging session delete Session_ID
```
{: codeblock}

여기서 Session_ID는 이전 단계에서 작성한 세션의 GUID입니다.

예:

```
ibmcloud cf logging session delete -jshdjsunelsssr4566722==
+---------+------------------------+
|  NAME   |         VALUE          |
+---------+------------------------+
| Message | Delete session success |
+---------+------------------------+
```
{: screen}




