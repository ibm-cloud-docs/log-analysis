---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# 로컬 파일로 로그 내보내기
{: #export}

{{site.data.keyword.la_full_notm}} 인스턴스에서 로컬 파일로 JSONL 형식의 로그 데이터를 내보낼 수 있습니다. 프로그래밍 방식으로 또는 IBM Log Analysis Web UI에서 로그를 내보낼 수 있습니다. 
{:shortdesc}

로그 데이터를 내보낼 때 다음 정보를 고려하십시오.
* 로그 항목 세트를 내보내십시오. 내보낼 데이터 세트를 정의하려면 필터 및 검색을 적용할 수 있습니다. 또한 시간 범위를 지정할 수 있습니다. 
* Web UI에서 로그를 내보낼 때 이메일 주소로 보낸 이메일을 가져오십시오. 이 이메일에는 데이터가 포함된 압축 파일에 대한 링크가 있습니다. 데이터를 가져오려면 링크를 클릭하고 압축 파일을 다운로드해야 합니다.
* 로그를 프로그래밍 방식으로 내보내는 경우 터미널로 이메일을 발송하거나 로그를 스트리밍하도록 선택할 수 있습니다.
* 내보낼 데이터가 포함된 압축 로그 파일은 최대 48시간 동안 사용 가능합니다. 
* 내보낼 수 있는 최대 행 수는 10,000입니다.



## Web UI에서 로그 내보내기
{: #ui}

로그 데이터를 내보내려면 다음 단계를 완료하십시오.

1. **보기** 아이콘 ![구성 아이콘](images/views.png)을 클릭하십시오.
2. **모든 항목** 또는 보기를 선택하십시오.
3. 내보낼 로그 항목이 표시될 때까지 시간 프레임, 필터 및 검색 기준을 적용하십시오.
4. **모든 항목** 보기에서 시작하는 경우 **저장되지 않은 보기**를 클릭하십시오. 이전 단계에서 보기를 선택한 경우 보기 이름을 클릭하십시오.
5. `행 내보내기`를 선택하십시오. 새 창이 열립니다.
6. 시간 범위를 확인하십시오. 변경해야 하는 경우 *내보내기를 위한 시간 범위* 변경 필드에서 사전 정의된 시간 범위를 클릭하십시오.
7. 내보내기 요청이 행 한계를 초과하는 경우 **최신 행 선호** 또는 **이전 행 선호**를 선택하십시오.
8. 이메일을 확인하십시오. **LogDNA**에서 링크가 포함된 이메일을 수신하여 내보낸 행을 다운로드하십시오.


## API를 사용하여 프로그래밍 방식으로 로그 내보내기
{: #api}

로그를 프로그래밍 방식으로 내보내려면 다음 단계를 완료하십시오.

1. 서비스 키를 생성하십시오. 

    **참고:** 이 단계를 완료하려면 {{site.data.keyword.la_full_notm}} 인스턴스 또는 서비스의 **관리자** 역할을 가져야 합니다. 자세한 정보는 [LogDNA에서 로그 관리 및 경보 구성을 위한 권한 부여](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)를 참조하십시오.

    1. {{site.data.keyword.la_full_notm}} Web UI를 실행하십시오. 자세한 정보는 [{{site.data.keyword.la_full_notm}} Web UI로 이동](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)을 참조하십시오.

    2. **구성** 아이콘 ![구성 아이콘](images/admin.png)을 선택하십시오. 그런 다음 **조직**을 선택하십시오. 

    3. **API 키**를 선택하십시오.

        작성된 서비스 키를 볼 수 있습니다. 

    4. **서비스 키 생성**을 클릭하십시오.

        새 키가 목록에 추가됩니다. 이 키를 복사하십시오.

2. 로그를 내보내십시오. 다음 cURL 명령을 실행하십시오.

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    여기서, 

    * ENDPOINT는 서비스의 시작점을 나타냅니다. 각 지역에는 서로 다른 URL이 있습니다.
    * QUERY_PARAMETERS는 내보내기 요청에 적용되는 필터링 기준을 정의하는 매개변수입니다.
    * SERVICE_KEY는 이전 단계에서 작성한 서비스 키입니다.

다음 표에는 지역별 엔드포인트가 나열되어 있습니다.

| 지역         | 엔드포인트                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="지역별 엔드포인트" caption-side="top"} 


다음 표에는 설정할 수 있는 조회 매개변수가 나열되어 있습니다.

| 조회 매개변수 | 유형       | 상태     | 설명 |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | 필수   | 시작 시간입니다. 초 또는 밀리초 단위의 UNIX 시간소인으로 설정합니다. |
| `to`        | `int32`      | 필수   | 종료 시간입니다. 초 또는 밀리초 단위의 UNIX 시간소인으로 설정합니다.    |
| `size`      | `string`     | 선택사항   | 내보내기에 포함할 로그 행 수입니다.  | 
| `hosts`     | `string`     | 선택사항   | 쉼표로 구분된 호스트 목록입니다. |
| `apps`      | `string`     | 선택사항   | 쉼표로 구분된 애플리케이션 목록입니다. |
| `levels`    | `string`     | 선택사항   | 쉼표로 구분된 로그 레벨 목록입니다. |
| `query`     | `string`     | 선택사항   | 조회를 검색합니다. 자세한 정보는 [로그 검색](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)을 참조하십시오. |
| `prefer`    | `string`     | 선택사항   | 내보낼 로그 행을 정의합니다. 올바른 값은 `head`, 첫 번째 로그 행 및 `tail`, 마지막 로그 행입니다. 지정되지 않은 경우 기본값은 tail입니다.  |
| `email`     | `string`     | 선택사항   | 내보내기에 대한 다운로드 가능 링크가 있는 이메일을 지정합니다. 기본적으로 로그 행이 스트리밍됩니다.|
| `emailSubject` | `string`     | 선택사항   | 이메일의 제목을 설정하는 데 사용합니다. </br>공백을 표시하려면 `%20`을 사용합니다. 예를 들어, 샘플 값은 `Export%20logs`입니다. |
{: caption="조회 매개변수" caption-side="top"} 

예를 들어, 로그 행을 터미널로 스트리밍하기 위해 다음 명령을 실행할 수 있습니다.

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

링크가 포함된 이메일을 발송하여 내보내기에 지정된 로그 행을 다운로드하기 위해 다음 명령을 실행할 수 있습니다.

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


사용자 정의 제목이 포함된 이메일을 발송하기 위해 다음 명령을 실행할 수 있습니다.

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

