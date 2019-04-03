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

# Log Analysis CLI({{site.data.keyword.Bluemix_notm}} 플러그인)
{: #log_analysis_cli}

{{site.data.keyword.loganalysislong}} CLI는 로그 수집에 저장되는 로그를 관리하는 데 사용할 수 있는 {{site.data.keyword.Bluemix_notm}} 플러그인입니다.
{: shortdesc}

**전제조건**
* 로깅 명령을 실행하기 전에 `ibmcloud login` 명령으로 {{site.data.keyword.Bluemix_notm}}에 로그인하여 액세스 토큰을 생성하고 세션을 인증하십시오.

{{site.data.keyword.loganalysisshort}} CLI 사용 방법에 대해 알아보려면 [로그 관리](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov)를 참조하십시오.

<table>
  <caption>로그 관리 명령</caption>
  <tr>
    <th>명령</th>
    <th>사용하는 경우</th>
  </tr>
  <tr>
    <td>[ibmcloud logging](#base)</td>
    <td>이 명령을 사용하여 CLI에 대한 정보(예: 명령 목록)를 가져옵니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-delete](#delete)</td>
    <td>이 명령을 사용하여 로그 콜렉션에 저장된 로그를 삭제합니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-download](#download)</td>
    <td>이 명령을 사용하여 로그 콜렉션에서 로컬 파일로 로그를 다운로드하거나 다른 프로그램(예: Elastic Stack)으로 로그를 보냅니다. </td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-show](#status)</td>
    <td>이 명령을 사용하여 영역, 조직 또는 계정에서 수집된 로그에 대한 정보를 가져옵니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging help](#help)</td>
    <td>이 명령을 사용하여 모든 명령의 목록 및 CLI 사용 방법에 대한 도움말을 가져옵니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-show](#optionshow)</td>
    <td>이 명령을 사용하여 영역, 조직 또는 계정에서 사용 가능한 보존 기간을 확인합니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-update](#optionupdate)</td>
    <td>이 명령을 사용하여 영역, 조직 또는 계정에서 사용 가능한 보존 기간을 설정합니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging quota-usage-show](#quotausage)</td>
    <td>이 명령을 사용하여 영역, 조직 또는 계정의 할당량 사용량 정보를 가져옵니다. 또한 할당량 히스토리 정보를 가져올 수도 있습니다.</td>
  </tr>
  <tr>
    <td>[ibmcloud logging session-create](#session_create)</td>
    <td>이 명령을 사용하여 새 세션을 작성합니다.</td>
  <tr>
  <tr>
    <td>[ibmcloud logging session-delete](#session_delete)</td>
    <td>이 명령을 사용하여 세션을 삭제합니다.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging sessions](#session_list)</td>
    <td>이 명령을 사용하여 활성 세션 및 해당 ID를 나열합니다.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging session-show](#session_show)</td>
    <td>이 명령을 사용하여 단일 세션의 상태를 표시합니다.</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging token-get](#tokenget)</td>
    <td>이 명령을 사용하여 {{site.data.keyword.loganalysisshort}} 서비스에 로그 데이터를 전송하기 위한 로깅 토큰을 가져옵니다.</td>
  </tr>
</table>


## ibmcloud logging
{: #base}

CLI에 대한 일반 정보를 제공합니다.

```
ibmcloud logging 
```
{: codeblock}

**예**

명령의 목록을 가져오려면 다음 명령을 실행하십시오.

```
ibmcloud logging
이름:
   ibmcloud logging - IBM Cloud Log Analysis Service
사용법:
   ibmcloud logging command [arguments...] [command options]

명령:
명령:
   log-delete         로그 삭제
   log-download       로그 다운로드
   log-show           일별 로그의 수, 크기 및 유형 표시
   session-create     세션 작성
   session-delete     세션 삭제
   sessions           세션 정보 나열
   session-show       세션 정보 표시
   option-show        로그 보존 표시
   option-update      로그 옵션 표시
   token-get          로그를 전송하기 위해 로깅 토큰 가져오기
   quota-usage-show   할당량 사용량 정보 보기
   help             
   
명령에 대한 자세한 정보를 보려면 'ibmcloud logging help [command]'를 입력하십시오.
```
{: codeblock}




## ibmcloud logging log-delete
{: #delete3}

로그 콜렉션에 저장된 로그를 삭제합니다.

```
ibmcloud logging log-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-f, --force ]
```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 시작 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 2주 전으로 설정됩니다.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 종료 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 현재 날짜로 설정됩니다.
  </dd>
  
  <dt>-f, --force </dt>
  <dd>(선택사항) 이 옵션을 설정하면 조치 확인 없이 로그를 삭제합니다.
  </dd>
</dl>

**예**

2017년 5월 25일에 유형 *linux_syslog*의 로그를 삭제하려면 다음 명령을 실행하십시오.
```
ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: screen}



## ibmcloud logging log-download 
{: #download3}

로그 콜렉션에서 로컬 파일로 로그를 다운로드하거나 다른 프로그램(예: Elastic Stack)으로 로그를 보냅니다. 

**참고:** 파일을 다운로드하려면 먼저 세션을 작성해야 합니다. 세션은 날짜 범위, 로그 유형 및 계정 유형을 기반으로 어느 로그를 다운로드할 것인지 정의합니다. 세션의 컨텍스트 내에서 로그를 다운로드합니다. 자세한 정보는 [ibmcloud logging session-create(베타)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#session_create)를 참조하십시오.

```
 ibmcloud logging log-download  [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-o, --output OUTPUT] SESSION_ID

```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
 
  <dt>-o, --output OUTPUT</dt>
  <dd>(선택사항) 로그가 다운로드되는 로컬 출력 파일에 대한 경로와 파일 이름을 설정합니다. <br>기본값은 하이픈(-)입니다. <br>표준 출력으로 로그를 출력하려면 이 매개변수를 기본값으로 설정하십시오.</dd>

</dl>

**인수**

<dl>
  <dt>SESSION_ID</dt>
  <dd>이 값은 로그를 다운로드할 때 사용해야 하는 세션 ID를 나타냅니다. <br>**참고:** `ibmcloud logging session-create` 명령은 다운로드되는 로그를 제어하는 매개변수를 제공합니다. </dd>
</dl>

**참고:** 다운로드가 완료된 후에 같은 명령을 다시 실행하면 아무 것도 수행하지 않게 됩니다. 동일한 데이터를 다시 다운로드하려면 다른 파일 또는 다른 세션을 사용해야 합니다.

**예**

Linux 시스템에서 로그를 mylogs.gz라는 파일로 다운로드하려면 다음 명령을 실행하십시오.

```
ibmcloud logging log-download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

사용자 자신의 Elastic Stack에 로그를 다운로드하려면 다음 명령을 실행하십시오.

```
ibmcloud logging log-download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
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


## ibmcloud logging help
{: #help}

명령 사용 방법에 대한 정보를 제공합니다.

```
ibmcloud logging help [command] 
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
ibmcloud logging help log-show
이름:
   log-show - 일별 로그 수, 크기 및 유형 표시

사용법:
   ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]

옵션:
   -r, --resource-type     리소스 유형, 올바른 유형은 account, org 또는 space임
   -i, --resource-id       리소스 ID, 대상 리소스 ID
   -s, --start             시작 날짜, YYYY-MM-DD 형식으로 포함된 UTC 시간 값
   -e, --end               종료 날짜, YYYY-MM-DD 형식으로 포함된 UTC 시간 값
   -t, --type              로그 유형(예: "syslog")
   -l, --list-type-detail  상세 유형 목록

```
{: screen}


## ibmcloud logging option-show
{: #optionshow}

영역, 조직 또는 계정에서 사용할 수 있는 로그의 보존 기간을 표시합니다. 

* 기간은 일 수로 설정됩니다.
* 기본값은 **-1**입니다. 

**참고:** 기본적으로 모든 로그가 저장됩니다. **delete** 명령을 사용하여 로그를 수동으로 삭제해야 합니다. 자동으로 로그를 삭제하려면 보존 정책을 설정하십시오.

```
ibmcloud logging option-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>

</dl>

**예**

사용자가 로그인한 영역의 기본 현재 보존 기간을 보려면 다음 명령을 실행하십시오.

```
ibmcloud logging option-show
```
{: screen}




## ibmcloud logging option-update
{: #optionupdate}

영역, 조직 또는 계정에서 사용할 수 있는 로그의 보존 기간을 변경합니다. 

* 기간은 일 수로 설정됩니다.
* 기본값은 **-1**입니다. 

```
ibmcloud logging option-update [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] <-e,--retention RETENTION_VALUE>
```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 정보를 가져오려는 대상 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
  
  <dt>-e,--retention RETENTION_VALUE</dt>
  <dd>로그가 보존되는 일 수를 설정합니다. </dd>

</dl>

**예**

사용자가 로그인한 영역에 대한 보존 기간을 25일로 변경하려면 다음 명령을 실행하십시오.

```
ibmcloud logging option-update -e 25
```
{: screen}


## ibmcloud logging quota-usage-show
{: #quotausage}

영역, 조직 또는 계정의 할당량 사용량에 대한 정보를 제공합니다. 또한 히스토리 사용량을 가져오는 데 할당량 사용량을 사용할 수도 있습니다.

* 기간은 일 수로 설정됩니다.
* 기본값은 **-1**입니다. 

```
ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s,--history]
```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
  
  <dt>-s,--history</dt>
  <dd>(선택사항) 할당량 사용량에 대한 히스토리 정보를 가져오도록 이 매개변수를 설정하십시오.</dd>

</dl>

**예**

영역 도메인에 대한 할당량 사용량을 가져오려면 다음 명령을 실행하십시오.

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}

## ibmcloud logging session-create
{: #session_create}

새 세션을 작성합니다.

**참고:** 하나의 영역에 최대 30개의 동시 세션이 가능합니다. 세션은 사용자에 대해 작성됩니다. 세션은 영역의 사용자 사이에서 공유할 수 없습니다.

```
ibmcloud logging session-create [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-T, --time, LOG_TIME]
```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 시작 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 2주 전으로 설정됩니다.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 종료 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 현재 날짜로 설정됩니다.
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(선택사항) 로그 유형을 설정합니다. <br>예를 들면, *syslog*는 로그의 유형입니다. <br>기본값은 별표(*)로 설정됩니다. <br>각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: *log_type_1,log_type_2,log_type_3*).
  </dd>

  <dt>-T, --time, LOG_TIME</dt>
  <dd>(선택사항) 특정 유형의 로그를 가져오려는 날의 시간(시 단위)을 설정합니다. </br>올바른 값은 0-23입니다. </br>이를 LOG_TYPE과 함께 결합하여 사용해야 합니다.
  </dd>

</dl>


**리턴값**

<dl>

    <dt>ID</dt>
    <dd>세션 ID입니다.</dd>
	
	<dt>리소스 유형</dt>
    <dd>리소스 ID입니다.</dd>

    <dt>AccessTime</dt>
    <dd>세션이 마지막으로 사용된 시간을 표시하는 시간소인입니다.</dd>

    <dt>CreateTime</dt>
    <dd>세션이 작성된 날짜 및 시간에 해당하는 시간소인입니다.</dd>
	
	<dt>시작</dt>
    <dd>로그를 필터링하는 데 사용된 시작 날짜를 표시합니다. </dd>

    <dt>종료</dt>
    <dd>로그를 필터링하는 데 사용된 마지막 날짜를 표시합니다.</dd>

    <dt>유형</dt>
    <dd>세션을 통해 다운로드되는 로그 유형입니다.</dd>

</dl>


**예**

2017년 11월 13일의 로그가 포함된 세션을 작성하려면 다음 명령을 실행하십시오.

```
ibmcloud logging session-create -s 2017-11-13 -e 2017-11-13
Creating session for xxxxx@yyy.com resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   2017-11-13   2017-11-13   ANY_TYPE   
Session: 1ef776d1-4d25-4297-9693-882606c725c8 is created
```
{: screen}


## ibmcloud logging session-delete 
{: #session_delete}

세션 ID별로 지정된 세션을 삭제합니다.

```
ibmcloud session-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID
```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
 
</dl>

**인수**

<dl>
  <dt>SESSION_ID</dt>
  <dd>삭제하려는 활성 세션의 ID입니다.</dd>
</dl>

**예**

세션 ID가 *cI6hvAa0KR_tyhjxZZz9Uw==*인 세션을 삭제하려면 다음 명령을 실행하십시오.

```
ibmcloud logging session-delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud logging sessions
{: #session_list}

활성 세션 및 해당 ID를 나열합니다.

```
ibmcloud logging sessions [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**매개변수**

<dl>

  <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org* </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다.  </dd>
</dl>

**리턴값**

<dl>	
    <dt>SESSION_ID</dt>
    <dd>활성 세션의 ID입니다.</dd>
	   
    <dt>리소스 ID</dt>
    <dd>세션이 유효한 리소스의 ID입니다.</dd>

    <dt>CreateTime</dt>
    <dd>세션이 작성된 날짜 및 시간에 해당하는 시간소인입니다.</dd>

    <dt>AccessTime</dt>
    <dd>세션이 마지막으로 사용된 시간을 표시하는 시간소인입니다.</dd>
</dl>
 
**예**

```
ibmcloud logging sessions
Listing sessions of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   
Listed the sessions of resource xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 
```
:{ screen}


## ibmcloud logging session-show
{: #session_show}

단일 세션의 상태를 표시합니다.

```
ibmcloud logging session-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID

```
{: codeblock}

**매개변수**

<dl>
   <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org* </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다.  </dd>
</dl>

**인수**

<dl>
   <dt>SESSION_ID</dt>
   <dd>정보를 가져오려는 활성 세션의 ID입니다.</dd>
</dl>

**예**

세션 ID가 *cI6hvAa0KR_tyhjxZZz9Uw==*인 세션의 세부사항을 표시하려면 다음 명령을 실행하십시오.

```
ibmcloud logging session-show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}

## ibmcloud logging token-get
{: #tokenget}

로그 데이터를 {{site.data.keyword.loganalysisshort}}로 전송하는 데 필요한 로깅 토큰을 리턴합니다.

```
ibmcloud logging token-get [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 로그 데이터를 전송할 계획인 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
</dl>


**예**

```
ibmcloud logging token-get -r space -i js7ydf98-8682-430d-bav4-36b712341744
Getting log token of resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Tenant Id                              Logging Token   
js7ydf98-8682-430d-bav4-36b712341744   xxxxxxxxxx   
```
{: screen}


## ibmcloud logging log-show
{: #status}

{{site.data.keyword.Bluemix_notm}} 영역 또는 계정에서 수집된 로그에 대한 정보를 리턴합니다.

```
ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]
```
{: codeblock}

* 리소스 유형을 지정하지 않으면 명령은 로그인된 리소스의 세부사항을 리턴합니다.
* 리소스 유형을 지정하면 리소스 ID를 지정해야 합니다.
* 시작 및 종료 날짜를 지정하지 않으면 명령은 로그 콜렉션에 저장된 지난 2주의 로그에 대한 정보만 보고합니다.

**매개변수**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(선택사항) 리소스 유형을 설정합니다. 올바른 값: *space*, *account* 및 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(선택사항) 이 필드를 영역, 조직 또는 계정의 ID로 설정합니다. <br>기본적으로 이 매개변수를 지정하지 않으면 명령은 로그인되는 리소스의 ID를 사용합니다. 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 시작 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 2주 전으로 설정됩니다.
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(선택사항) 협정 세계시(UTC), *YYYY-MM-DD*로 종료 날짜를 설정합니다. 예를 들면, `2006-01-02`입니다. <br>기본값은 현재 날짜로 설정됩니다.
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(선택사항) 로그 유형을 설정합니다. <br>예를 들면, *syslog*는 로그의 유형입니다. <br>기본값은 별표(*)로 설정됩니다. <br>각 유형을 쉼표로 구분하여 여러 개의 로그 유형을 지정할 수 있습니다(예: *log_type_1,log_type_2,log_type_3*).
  </dd>
  
  <dt>-l, --list-type-detail</dt>
  <dd>(선택사항) 각 로그 유형을 개별적으로 나열하도록 이 매개변수를 설정하십시오.
  </dd>
</dl>


**예**

```
ibmcloud logging log-show
Showing log status of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

Date         Size        Count    Searchable   Types   
2017-11-07   1878197     1333     None         default   
2017-11-13   201653512   179391   All          default,linux_syslog   
2017-11-14   32134119    30425    All          default,linux_syslog   
2017-11-15   303901156   269689   All          linux_syslog,default   
2017-11-16   107253679   96648    All          default,linux_syslog   
```
{: screen}

```
 ibmcloud logging log-show -l
Showing log status of resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

Date         Size        Count    Searchable   Type   
2017-11-14   30146764    26611    true         default   
2017-11-14   1987355     3814     true         linux_syslog   
2017-11-15   303004895   267890   true         default   
2017-11-15   896261      1799     true         linux_syslog   
2017-11-16   107918249   96278    true         default   
2017-11-16   912890      1794     true         linux_syslog   
```
{: screen}
