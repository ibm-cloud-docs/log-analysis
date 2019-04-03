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

# IBM Cloud Log Analysis CLI(CF 플러그인)
{: #logging_cli}

{{site.data.keyword.loganalysislong}} CLI는 {{site.data.keyword.Bluemix}} 조직의 영역에서 실행 중인 클라우드 리소스에 대한 로그를 관리하는 플러그인입니다.
{: shortdesc}

**전제조건**
* 로깅 명령을 실행하기 전에 `ibmcloud login` 명령으로 {{site.data.keyword.Bluemix_notm}}에 로그인하여 {{site.data.keyword.Bluemix_short}} 액세스 토큰을
생성하고 세션을 인증하십시오. 자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.

{{site.data.keyword.loganalysisshort}} CLI 사용 방법에 대해 알아보려면 [로그 관리](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov)를 참조하십시오.

<table>
  <caption>로그 관리 명령</caption>
  <tr>
    <th>명령</th>
    <th>사용하는 경우</th>
  </tr>
  <tr>
    <td>[ibmcloud cf logging](#base)</td>
    <td>이 명령을 사용하여 CLI에 대한 정보(예: 명령의 목록 또는 버전)를 가져옵니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging auth](#auth)</td>
    <td>이 명령을 사용하여 {{site.data.keyword.loganalysisshort}} 서비스에 로그를 전송하는 데 사용할 수 있는 로깅 토큰을 가져옵니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging delete](#delete)</td>
    <td>이 명령을 사용하여 로그 콜렉션에 저장된 로그를 삭제합니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging download(베타)](#download)</td>
    <td>이 명령을 사용하여 로그 콜렉션에서 로컬 파일로 로그를 다운로드하거나 다른 프로그램(예: Elastic Stack)으로 로그를 보냅니다. </td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging help](#help)</td>
    <td>이 명령을 사용하여 모든 명령의 목록 및 CLI 사용 방법에 대한 도움말을 가져옵니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging option](#option)</td>
    <td>이 명령을 사용하여 영역 또는 계정에서 사용 가능한 로그에 대한 보존 기간을 보거나 설정합니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging session create(베타)](#session_create1)</td>
    <td>이 명령을 사용하여 새 세션을 작성합니다.</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete(베타)](#session_delete1)</td>
    <td>이 명령을 사용하여 세션을 삭제합니다.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session list(베타)](#session_list1)</td>
    <td>이 명령을 사용하여 활성 세션 및 해당 ID를 나열합니다.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session show(베타)](#session_show1)</td>
    <td>이 명령을 사용하여 단일 세션의 상태를 표시합니다.</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging status](#status1)</td>
    <td>이 명령을 사용하여 영역 또는 계정에서 수집된 로그에 대한 정보를 가져옵니다.</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

CLI의 버전 및 CLI 사용 방법에 대한 정보를 제공합니다.

```
ibmcloud cf logging [parameters]
```
{: codeblock}

**매개변수**

<dl>
<dt>--help, -h</dt>
<dd>명령의 목록을 표시하거나 하나의 명령에 대한 도움말을 가져오려면 이 매개변수를 설정하십시오.
</dd>

<dt>--version, -v</dt>
<dd>CLI의 버전을 인쇄하려면 이 매개변수를 설정하십시오.</dd>
</dl>

**예**

명령의 목록을 가져오려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging --help
```
{: codeblock}

CLI의 버전을 가져오려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging --version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

{{site.data.keyword.loganalysisshort}} 서비스에 로그를 전송하기 위해 사용할 수 있는 로깅 토큰을 리턴합니다. 

**참고: ** 토큰은 만료되지 않습니다.

```
ibmcloud cf logging auth
```
{: codeblock}

**리턴**

<dl>
  <dt>로깅 토큰</dt>
  <dd>예: `jec8BmipiEZc`.
  </dd>
  
  <dt>조직 ID</dt>
  <dd>사용자가 로그인한 {{site.data.keyword.Bluemix_notm}} 조직의 GUID입니다.
  </dd>
  
  <dt>영역 ID</dt>
  <dd>사용자가 로그인한 조직 내 영역의 GUID입니다.
  </dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

로그 콜렉션에 저장된 로그를 삭제합니다.

```
ibmcloud cf logging delete [parameters]
```
{: codeblock}

**매개변수**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 시작 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 2주 전으로 설정됩니다.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 종료 날짜를 설정합니다. <br>날짜의 UTC 형식은 **YYYY-MM-DD**(예: `2006-01-02`)입니다. <br>기본값은 현재 날짜로 설정됩니다.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(선택사항) 로그 유형을 설정합니다. <br>예를 들면, *syslog*는 로그의 유형입니다. <br>기본값은 **\***로 설정됩니다. <br>각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: **log_type_1,log_type_2,log_type_3*).
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(선택사항) 계정 레벨에 제공되는 로그 정보의 범위를 설정합니다. <br>이 매개변수가 지정되지 않은 경우, 현재 영역에 대해서만 로그 정보를 제공하도록 기본값이 설정됩니다.
  </dd>
</dl>

**예**

2017년 5월 25일에 유형 *linux_syslog*의 로그를 삭제하려면 다음 명령을 실행하십시오.
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download(베타)
{: #download4}

로그 콜렉션에서 로컬 파일로 로그를 다운로드하거나 다른 프로그램(예: Elastic Stack)으로 로그를 보냅니다. 

**참고:** 파일을 다운로드하려면 먼저 세션을 작성해야 합니다. 세션은 날짜 범위, 로그 유형 및 계정 유형을 기반으로 어느 로그를 다운로드할 것인지 정의합니다. 세션의 컨텍스트 내에서 로그를 다운로드합니다. 자세한 정보는 [ibmcloud cf logging session create(베타)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#session_create1)를 참조하십시오.

```
ibmcloud cf logging download [parameters] [arguments]
```
{: codeblock}

**매개변수**

<dl>
<dt>--output value, -o value</dt>
<dd>(선택사항) 로그가 다운로드되는 로컬 출력 파일에 대한 경로와 파일 이름을 설정합니다. <br>기본값은 하이픈(-)입니다. <br>표준 출력으로 로그를 출력하려면 이 매개변수를 기본값으로 설정하십시오.</dd>
</dl>

**인수**

<dl>
<dt>session_ID</dt>
<dd>`ibmcloud cf logging session create` 명령을 실행하여 가져오는 세션 ID 값으로 설정하십시오. 이 값은 로그를 다운로드할 때 사용할 세션을 표시합니다. <br>**참고:** `ibmcloud cf logging session create` 명령은 다운로드되는 로그를 제어하는 매개변수를 제공합니다. </dd>
</dl>

**참고:** 다운로드가 완료된 후에 같은 명령을 다시 실행하면 아무 것도 수행하지 않게 됩니다. 동일한 데이터를 다시 다운로드하려면 다른 파일 또는 다른 세션을 사용해야 합니다.

**예**

Linux 시스템에서 로그를 mylogs.gz라는 파일로 다운로드하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

사용자 자신의 Elastic Stack에 로그를 다운로드하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

다음 파일은 logstash.conf 파일의 예입니다.

```
input {
  stdin {
    codec => json_lines {}
  }
}
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud cf logging help
{: #help1}

명령 사용 방법에 대한 정보를 제공합니다.

```
ibmcloud cf logging help [command]
```
{: codeblock}

**매개변수**

<dl>
<dt>명령</dt>
<dd>도움말을 가져오려는 명령 이름을 설정하십시오.
</dd>
</dl>


**예**

로그의 상태를 보기 위해 명령을 실행하는 방법에 대한 도움말을 가져오려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

영역 또는 계정에서 사용 가능한 로그에 대한 보존 기간을 표시하거나 변경합니다. 

* 기간은 일 수로 설정됩니다.
* 기본값은 **-1**입니다. 

**참고:** 기본적으로 모든 로그가 저장됩니다. **delete** 명령을 사용하여 로그를 수동으로 삭제해야 합니다. 자동으로 로그를 삭제하려면 보존 정책을 설정하십시오.

```
ibmcloud cf logging option [parameters]
```
{: codeblock}

**매개변수**

<dl>
<dt>--retention value, -r value</dt>
<dd>(선택사항) 보존일 수를 설정합니다. <br> 기본값은 *-1*일입니다.</dd>

<dt>--at-account-level, -a </dt>
  <dd>(선택사항) 계정 레벨에 범위를 설정합니다. <br>이 매개변수가 지정되지 않은 경우, `ibmcloud cf login` 명령을 사용하여 로그인한 영역인 현재 영역에 대해 *-1*로 기본값이 설정됩니다.
  </dd>
</dl>

**예**

사용자가 로그인한 영역의 기본 현재 보존 기간을 보려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging option
```
{: codeblock}

출력은 다음과 같습니다.

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


사용자가 로그인한 영역에 대한 보존 기간을 25일로 변경하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging option -r 25
```
{: codeblock}

출력은 다음과 같습니다.

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create(베타)
{: #session_create1}

새 세션을 작성합니다.

**참고:** 하나의 영역에 최대 30개의 동시 세션이 가능합니다. 세션은 사용자에 대해 작성됩니다. 세션은 영역의 사용자 사이에서 공유할 수 없습니다.

```
ibmcloud cf logging session create [parameters]
```
{: codeblock}

**매개변수**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 시작 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 2주 전으로 설정됩니다.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 종료 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 현재 날짜로 설정됩니다.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(선택사항) 로그 유형을 설정합니다. <br>예를 들면, *syslog*는 로그의 유형입니다. <br>기본값은 별표(*)로 설정됩니다. <br>각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: *log_type_1,log_type_2,log_type_3*).
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(선택사항) 계정 레벨에 범위를 설정합니다. <br>이 매개변수가 지정되지 않은 경우, `ibmcloud cf login` 명령을 사용하여 로그인한 영역인 현재 영역만으로 기본값이 설정됩니다.
  </dd>
</dl>

**리턴값**

<dl>
<dt>Access-Time</dt>
<dd>세션이 마지막으로 사용된 시간을 표시하는 시간소인입니다.</dd>

<dt>Create-Time</dt>
<dd>세션이 작성된 날짜 및 시간에 해당하는 시간소인입니다.</dd>

<dt>Date-Range</dt>
<dd>로그를 필터링하는 데 사용된 일 수를 표시합니다. 이 날짜 범위에 식별된 로그는 세션을 통해 관리에 사용할 수 있습니다.</dd>

<dt>ID</dt>
<dd>세션 ID입니다.</dd>

<dt>영역</dt>
<dd>세션이 활성인 영역 ID입니다.</dd>

<dt>Type-Account</dt>
<dd>세션을 통해 다운로드되는 로그 유형입니다.</dd>

<dt>Username</dt>
<dd>세션을 작성한 사용자의 {{site.data.keyword.IBM_notm}} ID입니다.</dd>
</dl>


**예**

*log*의 로그 유형에 대해 2017년 5월 20일과 2017년 5월 26일 사이의 로그가 포함된 세션을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete(베타)
{: #session_delete1}

세션 ID별로 지정된 세션을 삭제합니다.

```
ibmcloud cf logging session delete [arguments]
```
{: codeblock}

**인수**

<dl>
<dt>세션 ID</dt>
<dd>삭제하려는 세션의 ID입니다. <br>`ibmcloud cf logging session list` 명령을 사용하여 모든 활성 세션 ID를 가져올 수 있습니다.</dd>
</dl>

**예**

세션 ID가 *cI6hvAa0KR_tyhjxZZz9Uw==*인 세션을 삭제하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list(베타)
{: #session_list1}

활성 세션 및 해당 ID를 나열합니다.

```
ibmcloud cf logging session list 
```
{: codeblock}

**리턴값**

<dl>
<dt>ID</dt>
<dd>세션 ID입니다.</dd>

<dt>SPACE</dt>
<dd>세션이 활성인 영역 ID입니다.</dd>

<dt>USERNAME</dt>
<dd>세션을 작성한 사용자의 {{site.data.keyword.IBM_notm}} ID입니다.</dd>

<dt>CREATE-TIME</dt>
<dd>세션이 작성된 날짜 및 시간에 해당하는 시간소인입니다.</dd>

<dt>ACCESS-TIME</dt>
<dd>세션이 마지막으로 사용된 시간을 표시하는 시간소인입니다.</dd>
</dl>
 

## ibmcloud cf logging session show(베타)
{: #session_show1}

단일 세션의 상태를 표시합니다.

```
ibmcloud cf logging session show [arguments]
```
{: codeblock}

**인수**

<dl>
<dt>session_ID</dt>
<dd>정보를 가져오려는 활성 세션의 ID입니다.</dd>
</dl>

**리턴값**

<dl>
<dt>Access-Time</dt>
<dd></dd>

<dt>Create-Time</dt>
<dd>세션이 작성된 날짜 및 시간에 해당하는 시간소인입니다.</dd>

<dt>Date-Range</dt>
<dd>로그를 필터링하는 데 사용된 일 수를 표시합니다. 이 날짜 범위에 식별된 로그는 세션을 통해 관리에 사용할 수 있습니다.</dd>

<dt>ID</dt>
<dd>세션 ID입니다.</dd>

<dt>영역</dt>
<dd>세션이 활성인 영역 ID입니다.</dd>

<dt>Type-Account</dt>
<dd>세션을 통해 다운로드되는 로그 유형입니다.</dd>

<dt>Username</dt>
<dd>세션을 작성한 사용자의 {{site.data.keyword.IBM_notm}} ID입니다.</dd>
</dl>

**예**

세션 ID가 *cI6hvAa0KR_tyhjxZZz9Uw==*인 세션의 세부사항을 표시하려면 다음 명령을 실행하십시오.

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

영역 또는 계정에서 수집된 로그에 대한 정보를 리턴합니다.

```
ibmcloud cf logging status [parameters]
```
{: codeblock}

**매개변수**

<dl>
  <dt>--start value, -s value</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 시작 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 2주 전으로 설정됩니다.
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 종료 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 현재 날짜로 설정됩니다.
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>(선택사항) 로그 유형을 설정합니다. <br>예를 들면, *syslog*는 로그의 유형입니다. <br>기본값은 별표(*)로 설정됩니다. <br>각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: *log_type_1,log_type_2,log_type_3*).
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>(선택사항) 계정 레벨에 범위를 설정합니다. <br> **참고:** 계정 정보를 가져오려면 이 값을 설정하십시오. <br>이 매개변수가 지정되지 않은 경우, `ibmcloud cf login` 명령을 사용하여 로그인한 영역인 현재 영역만으로 기본값이 설정됩니다.
  </dd>
  
  <dt>--list-type-detail, -l</dt>
  <dd>(선택사항) 매일에 대한 로그 유형의 부분 합계를 나열하려면 이 매개변수를 설정합니다.
  </dd>
</dl>

**참고:** `ibmcloud cf logging status` 명령은 시작 및 종료 날짜가 지정되지 않은 경우 로그 콜렉션에 저장된 최근 2주 동안의 로그만 보고합니다.


