---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

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

# 로그 보기
{: #view_logs}

{{site.data.keyword.cloud_notm}}에서 {{site.data.keyword.la_full_notm}} 서비스의 인스턴스를 프로비저닝하고 로그 데이터 소스에 대한 LogDNA 에이전트를 구성하면 {{site.data.keyword.la_full_notm}} Web UI를 통해 로그 데이터를 보고 모니터하고 관리할 수 있습니다.
{:shortdesc}

{{site.data.keyword.la_full_notm}} Web UI를 실행하면 로그 항목이 사전 정의된 형식으로 표시됩니다. **사용자 환경 설정** 섹션에서 각 로그 행의 정보를 표시하는 방법을 수정할 수 있습니다. 또한 로그를 필터링하고 검색 설정을 수정한 다음 결과를 *보기*로 북마킹할 수 있습니다. 하나 이상의 경보를 보기에 첨부하고 분리할 수 있습니다. 행을 보기에 표시하는 방법에 대한 사용자 정의 형식을 정의할 수 있습니다. 로그 행을 펼치고 구문 분석된 데이터를 볼 수 있습니다.


로그를 보려면 다음 단계를 완료하십시오.


## 1단계. 로그를 볼 수 있도록 사용자에게 IAM 정책 부여
{: #view_logs_step1}

**참고:** {{site.data.keyword.la_full_notm}} 서비스의 관리자나 {{site.data.keyword.la_full_notm}} 인스턴스의 관리자여야 하거나 다른 사용자 정책을 부여할 수 있는 계정 IAM 권한을 가져야 합니다.

다음 표에는 사용자가 {{site.data.keyword.la_full_notm}} Web UI를 실행하고 로그를 보기 위해 필요한 최소한의 정책이 나열되어 있습니다.

| 서비스                        | 역할                      | 부여되는 권한            |
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` | 플랫폼 역할: 뷰어     | 사용자가 관찰 가능성 로깅 대시보드에서 서비스 인스턴스 목록을 볼 수 있게 합니다. |
| `{{site.data.keyword.la_full_notm}} ` | 서비스 역할: 독자      | 사용자가 Web UI를 실행하고 Web UI에서 로그를 볼 수 있게 합니다.  |
{: caption="표 1. IAM 정책" caption-side="top"} 

사용자를 위한 이러한 정책을 구성하는 방법에 대한 자세한 정보는 [사용자에게 LogDNA에서 로그를 볼 수 있는 권한 부여](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)를 참조하십시오.


## 2단계. {{site.data.keyword.cloud_notm}} UI를 통해 Web UI 탐색
{: #view_logs_step2}

{{site.data.keyword.cloud_notm}} UI를 통해 {{site.data.keyword.la_full_notm}} UI를 실행하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.cloud_notm}} 계정에 로그인하십시오.

    [{{site.data.keyword.cloud_notm}} 대시보드 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://cloud.ibm.com/login){:new_window}를 클릭하여 {{site.data.keyword.cloud_notm}} 대시보드를 실행하십시오.

	사용자 ID와 비밀번호로 로그인하면 {{site.data.keyword.cloud_notm}} *대시보드*가 열립니다.

2. 탐색 메뉴에서 **관찰 가능성**을 선택하십시오. 

3. **로깅**을 선택하십시오. 

    {{site.data.keyword.cloud_notm}}에서 사용 가능한 {{site.data.keyword.la_full_notm}} 인스턴스의 목록이 표시됩니다.

4. 하나의 인스턴스를 선택하십시오. 그런 다음 **LogDNA 보기**를 클릭하십시오.

{{site.data.keyword.la_full_notm}} Web UI가 열리고 해당 인스턴스로 전달된 로그가 표시됩니다.


## 3단계. 기본 보기 사용자 정의
{: #view_logs_step3}

**USER PREFERENCES** 섹션에서 행마다 표시되는 데이터 필드의 순서를 수정할 수 있습니다.

로그 행의 형식을 수정하려면 다음 단계를 완료하십시오.

1. **구성** 아이콘 ![구성 아이콘](images/admin.png "관리 아이콘")을 선택하십시오.
2. **USER PREFERENCES**를 선택하십시오. 새 창이 열립니다.
3. **로그 형식**을 선택하십시오.
4. 요구사항에 맞도록 *행 형식* 섹션을 수정하십시오. 상자를 끌어오십시오.


## 4단계. 로그 행 조사
{: #view_logs_step4}

언제든지 컨텍스트에서 각 로그 행을 볼 수 있습니다.

다음 단계를 완료하십시오. 

1. **보기** 아이콘 ![구성 아이콘](images/views.png "구성 아이콘")을 클릭하십시오.
2. **모든 항목** 또는 보기를 선택하십시오.
3. 탐색할 로그에서 행을 식별하십시오.
4. 로그 행을 펼치십시오. 

    행 ID, 태그 및 레이블에 대한 정보가 표시됩니다.

5. **컨텍스트에서 보기**를 클릭하여 이 호스트, 앱 또는 둘 다에서 다른 로그 행의 컨텍스트에 있는 로그 행을 보십시오.

6. **클립보드에 복사**를 클릭하여 클립보드에 메시지 필드를 복사하십시오.

완료되면 행을 닫으십시오.


## 5단계. 로그 필터링
{: #view_logs_step5}

로그 소스, 애플리케이션 및 로그 레벨로 로그를 필터링할 수 있습니다. 

* 소스는 호스트, 컴퓨터, 가상 머신 또는 Heroku 앱입니다.
* 애플리케이션은 로그 파일, 프로그램 또는 컨테이너를 나타냅니다.
* 로그 레벨 예는 INFO, DEBUG, ERROR입니다.

로그를 필터링하려면 다음 단계를 완료하십시오.

1. **보기** 아이콘 ![구성 아이콘](images/views.png "구성 아이콘")을 클릭하십시오.
2. **모든 항목** 또는 보기를 선택하십시오.
3. **모든 태그**를 펼쳐 로그에서 식별되는 태그 목록을 보십시오. 그런 다음 원하는 태그를 선택하십시오.
4. **모든 소스**를 펼쳐 로그에서 식별되는 로그 소스 목록을 보십시오. 그런 다음 원하는 로그 소스를 선택하십시오.
5. **모든 앱**을 펼쳐 로그에서 식별되는 앱 목록을 보십시오. 그런 다음 원하는 앱을 선택하십시오.
6. **모든 레벨**을 펼쳐 로그에서 식별되는 로그 레벨 목록을 보십시오. 그런 다음 원하는 로그 레벨을 선택하십시오.


**참고:** 각 섹션에서 여러 옵션을 하나의 그룹으로 그룹화할 수 있습니다. 다른 사용자 정의 보기에서 로그 데이터를 필터링할 때 이러한 그룹을 재사용하려면 태그, 로그 소스, 앱 및 로그 레벨을 그룹화하십시오.

그룹을 작성하려면 여러 개의 값을 선택하십시오. 그런 다음 **그룹으로 저장**을 클릭하십시오. 그룹 이름을 입력한 후 저장하십시오.


## 6단계. 로그 검색
{: #view_logs_step6}

로그 데이터를 검색하는 경우 검색은 보기에 구성된 로그 필터 및 시간 조회를 적용합니다.

단순 검색(단일 용어 문자열 검색), 복합 검색(다중 검색어 및 연산자), 필드 검색(로그 행을 구문 분석할 수 있는 경우) 및 기타 검색을 수행할 수 있습니다. 자세한 정보는 [LogDNA에서 로그를 검색하는 방법에 대한 문서 ![외부 링크 아이콘](../../icons/launch-glyph.svg "외부 링크 아이콘")](https://docs.logdna.com/docs/search){:new_window}를 참조하십시오.

**참고:** AND 및 OR 연산자는 대소문자를 구분하며 대문자로 사용해야 합니다.



## 7단계. 보기 작성
{: #view_logs_step7}


보기를 작성하려면 다음을 완료하십시오.

1. **보기** 아이콘 ![구성 아이콘](images/views.png "구성 아이콘")을 클릭하십시오.
2. **모든 항목** 또는 보기를 선택하십시오.
3. 로그 데이터를 필터링한 다음 **새 보기/경보로 저장**을 클릭하십시오.

    *보기 새로 작성* 페이지가 열립니다.

4. *이름* 필드에서 보기의 이름을 입력하십시오.

5. 선택적으로 카테고리를 추가하십시오. 이름을 입력한 후 **새 보기 카테고리로 추가**를 클릭하십시오.

6. 선택적으로 경보를 첨부하십시오. 경보를 구성하도록 새 섹션이 표시됩니다.

7. **보기 저장**을 클릭하십시오.


