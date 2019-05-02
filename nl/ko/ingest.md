---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

subcollection: LogDNA

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

 
# 로그 보내기
{: #ingest}

{{site.data.keyword.la_full_notm}} 인스턴스에 로그 데이터를 전송할 수 있습니다. 
{:shortdesc}

프로그래밍 방식으로 로그를 전송하려면 다음 단계를 완료하십시오.

## 1단계. 수집 API 키 가져오기 
{: #ingest_step1}

**참고:** 이 단계를 완료하려면 {{site.data.keyword.la_full_notm}} 인스턴스 또는 서비스의 **관리자** 역할을 가져야 합니다. 자세한 정보는 [LogDNA에서 로그 관리 및 경보 구성을 위한 권한 부여](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)를 참조하십시오.

수집 키를 가져오려면 다음 단계를 완료하십시오.
    
1. {{site.data.keyword.la_full_notm}} Web UI를 실행하십시오. 자세한 정보는 [{{site.data.keyword.la_full_notm}} Web UI로 이동](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)을 참조하십시오.

2. **구성** 아이콘 ![구성 아이콘](images/admin.png)을 선택하십시오. 그런 다음 **조직**을 선택하십시오. 

3. **API 키**를 선택하십시오.

    작성된 수집 키를 볼 수 있습니다. 

4. 기존 수집 키를 사용하거나 **수집 키 생성**을 클릭하여 새로 작성하십시오.

    새 키가 목록에 추가됩니다. 키를 복사하십시오.


## 2단계. 로그 전송
{: #ingest_step2}

로그를 전송하려면 다음 cURL 명령을 실행하십시오.

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

여기서, 

* ENDPOINT는 서비스의 시작점을 나타냅니다. 각 지역에는 서로 다른 URL이 있습니다.
* QUERY_PARAMETERS는 수집 요청에 적용되는 필터링 기준을 정의하는 매개변수입니다.
* LOG_LINES는 전송할 로그 행 세트를 설명합니다. 이는 오브젝트의 배열로 정의됩니다.
* INGESTION_KEY는 이전 단계에서 작성한 키입니다.

다음 표에는 지역별 엔드포인트가 나열되어 있습니다.

| 지역         | 엔드포인트                                             | 
|----------------|------------------------------------------------------|
| `미국 남부`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="지역별 엔드포인트" caption-side="top"} 


다음 표에는 조회 매개변수가 나열되어 있습니다.

| 조회 매개변수 |유형       |상태     |설명 |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | 필수   | 소스의 호스트 이름입니다. |
| `mac`           | `string`     | 선택사항   | 호스트 컴퓨터의 네트워크 MAC 주소입니다.    |
| `ip`            | `string`     | 선택사항   | 호스트 컴퓨터의 로컬 IP 주소입니다.  | 
| `now`           | `date-time`  | 선택사항   | 요청 시 밀리초 단위의 소스 UNIX 시간소인입니다. 시간 드리프트를 계산하는 데 사용됩니다.|
| `tags`          | `string`     | 선택사항   | 동적으로 호스트를 그룹화하는 데 사용되는 태그입니다. |
{: caption="조회 매개변수" caption-side="top"} 



다음 표에는 로그 행마다 필요한 데이터가 나열되어 있습니다.

| 매개변수     |유형       |설명                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | 로그 항목이 기록된 UNIX 시간소인입니다(밀리초 포함).       | 
| `line`           | `string`     | 로그 행의 텍스트입니다.                                     |
| `app`            | `string`     | 로그 행을 생성하는 애플리케이션의 이름입니다.  |
| `level`          | `string`     | 레벨에 대한 값을 설정합니다. 예를 들어, 이 매개변수의 샘플 값은 `INFO`, `WARNING`, `ERROR`입니다. |
| `meta`           |            | 이 필드는 로그 행과 연관된 사용자 정의 정보용으로 예약되어 있습니다. API 호출에 메타데이터를 추가하려면 행 오브젝트 아래에 메타 필드를 지정합니다. 행의 컨텍스트 내에서 메타데이터를 볼 수 있습니다.                      |
{: caption="행 오브젝트 필드" caption-side="top"} 

예를 들어, 다음 샘플은 수집할 로그 행에 대한 JSON을 보여줍니다.

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00, 
      "line":"This is my first log line.", 
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## 예
{: #ingest_example}

다음 샘플은 {{site.data.keyword.la_full_notm}} 서비스의 인스턴스로 하나의 로그 행을 전송하는 cURL 명령을 보여줍니다. 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

