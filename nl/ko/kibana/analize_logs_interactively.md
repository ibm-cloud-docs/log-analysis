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

# Kibana에서 대화식으로 로그 분석
{:#analize_logs_interactively}

검색 페이지에서 대화식으로 로그를 보고 분석할 수 있습니다. 검색 조회를 정의하여 Lucene 조회 언어를 사용하여 데이터를 필터링할 수 있습니다. 각 검색 조회에 대해 필터를 적용하여 분석에 사용할 수 있는 항목을 세분화할 수 있습니다. 나중에 다시 사용할 수 있도록 검색을 저장할 수 있습니다.
{:shortdesc}

{{site.data.keyword.Bluemix_notm}}에서 기본적으로 {{site.data.keyword.Bluemix_notm}} UI에서 Kibana를 실행할 때 검색 페이지에 표시되는 데이터 세트는 Kibana를 실행하는 컨테이너 또는 CF(Cloud Foundry) 애플리케이션에 대한 항목만 표시하도록 구성됩니다. 검색 페이지에 어떤 데이터의 서브세트가 표시되는지 보는 방법에 대한 자세한 정보는 [표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

{{site.data.keyword.Bluemix_notm}}에서 Kibana를 실행할 때 리소스별 기본 조회가 다음 표에 표시됩니다.

|리소스 |기본 Kibana 검색 조회 |
|---------------|---------------|
|CF 애플리케이션   |`application_id:<app_GUID>`    |
|단일 Docker 컨테이너 |`instance:<instance_GUID>`    |
|2개의 인스턴스가 있는 컨테이너 그룹 |`instance:<instance_GUID> OR instance:<instance_GUID>` |
{: caption="표 1. 기본 조회 검색" caption-side="top"}

**참고:** 
* {{site.data.keyword.Bluemix_notm}} UI에서 Kibana를 실행할 때마다 사용자가 볼 수 있는 데이터는 기본적으로 사전 정의되고 인덱스 패턴을 기반으로 하는 조회에 해당합니다.
* 최신 항목에 해당하는 최대 500개의 항목이 검색 페이지에 표시됩니다. 이 값을 변경하려면 **관리** 페이지의 **고급 옵션** 섹션에서 *discover:sampleSize* 필드를 수정할 수 있습니다.

{{site.data.keyword.loganalysisshort}} 서비스의 대시보드 또는 브라우저에서 Kibana를 실행할 때 검색 페이지에 표시되는 데이터에는 사용자가 로그인한 영역에서 사용 가능한 모든 로그 데이터가 포함됩니다. 페이지는 특정 서비스, 컨테이너 또는 앱에 제한되지 않습니다.

검색 페이지에는 데이터를 대화식으로 분석할 수 있도록 사용자 정의할 수 있는 표와 히스토그램이 포함되어 있습니다. 

검색 페이지에서 표를 사용자 정의하기 위해 다음 태스크 중에서 수행할 수 있습니다.

|태스크 |설명 | 
|------|-------------|
|[필드 열 추가](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_add_fields_to_table) |전체 메시지 대신에 분석에 필요한 특정 데이터를 보기 위한 필드를 추가합니다. |
|[자동으로 데이터 새로 고치기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_refresh_interval) |표에 표시되는 데이터를 최신 항목으로 새로 고칩니다. 기본적으로 새로 고치기는 **OFF**입니다. |
|[색인화된 필드의 값으로 항목 순서 지정](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_sort_by_table) |분석이 더 용이하도록 항목을 다시 정렬합니다. |
|[필드 열 재배열](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_rearrange_fields_in_table) |표에서 필드의 위치를 원하는 위치로 이동합니다. |
|[필드 열 제거](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_remove_fields_from_table) |필드가 분석을 위해 보기에서 필요하지 않은 경우 해당 필드를 제거합니다. |
|[항목 보기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_entry_in_table) |필드에 의해 구문 분석된 항목의 세부사항을 보거나 JSON으로 보기 위해 표에서 항목을 펼칩니다. |
{: caption="표 2. 표 사용자 정의 태스크" caption-side="top"}

<br>

다음 그림에는 검색 페이지에서 표의 샘플이 표시됩니다.

![Kibana의 검색 페이지](images/discover_page.gif "Kibana의 검색 페이지")

다른 검색을 정의할 수 있습니다. 자세한 정보는 [사용자 정의 검색을 정의하여 로그 필터링](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search)을 참조하십시오. 새 검색을 정의하면 히스토그램과 표에 표시되는 데이터가 자동으로 업데이트됩니다.

새 검색을 정의하려면 기본 검색 조회를 시작점으로 사용한 후에 다음 태스크를 수행하여 검색을 세분화하십시오.

* 볼 수 있는 데이터 세트를 세분화하기 위한 필드 필터를 적용하십시오. 각 필터를 전환하고 페이지에 고정해서 필요에 따라 사용 또는 사용 안함으로 설정하고 값을 포함하거나 제외하도록 구성할 수 있습니다. 자세한 정보는 [Kibana에서 로그 필터링](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs)을 참조하십시오.

    **팁:** *필드 목록*에서 보고자 하는 필드를 찾을 수 없거나 나열된 필드 옆의 돋보기 중 일부가 검색 페이지에서 사용할 수 없는 경우, 설정 페이지에서 인덱스 패턴을 새로 고치기해서 필드의 목록을 다시 로드하십시오. 자세한 정보는 [필드 목록 다시 로드](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_reload_fields)를 참조하십시오.

    예를 들어, CF 앱에 여러 개의 인스턴스가 있는 경우, 특정 인스턴스에 대한 데이터를 분석하고자 할 수 있습니다. 분석하려는 특정 인스턴스 ID 값의 필드 필터를 정의할 수 있습니다. 
    
* 시간 기반 데이터에 대해 *시간 선택도구*를 사용자 정의하십시오. 조회에 대한 절대 시간 범위, 상대 시간 범위를 정의하거나 사전 정의된 값의 세트에서 선택할 수 있습니다. 자세한 정보는 [시간 필터 설정](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)을 참조하십시오.

분석하려는 데이터 서브세트를 정의하는 검색을 구성한 후에 나중에 다시 사용하기 위해 저장할 수 있습니다. 자세한 정보는 [검색 저장](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search)을 참조하십시오.

검색 페이지에서 정의하는 검색을 사용하여 다음 태스크 중에서 수행할 수 있습니다.

|태스크 |설명 |
|------|-------------|
|[검색 삭제](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#delete_search) |더 이상 필요하지 않은 경우 검색을 삭제합니다. |
|[검색 내보내기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#export_search) |검색을 공유하도록 내보냅니다.  |
|[검색 가져오기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#import_search) |검색을 가져옵니다.  |
|[검색 다시 로드](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#reload_search1)  |데이터 세트를 다시 분석하도록 기존 검색을 업로드합니다. |
|[검색의 데이터 새로 고치기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#refresh_search) |검색을 통해 표시된 데이터의 자동 새로 고치기를 구성합니다.  |
|[검색 저장](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search) |나중에 다시 사용하도록 검색을 저장합니다.  |
{: caption="표 3. 검색으로 작업하는 태스크" caption-side="top"}


검색 페이지에서 통계를 볼 수도 있습니다.
* 필드별 통계를 볼 수 있습니다. 
* 구성한 `@timestamp`별로 히스토그램에서 통계를 볼 수 있습니다.

자세한 정보는 [필드 데이터 통계 보기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_fields_stats)를 참조하십시오.

**참고:** 표와 히스토그램에 표시된 데이터는 정적입니다. 최신 항목을 계속 보려면 새로 고치기 간격을 설정해야 합니다. 


## 표에 필드 열 추가
{: #discover_add_fields_to_table}

검색 페이지에서 데이터를 분석하는 데 사용할 수 있는 표에는 기본적으로 다음과 같은 필드가 포함됩니다.
* **time:** 이 필드는 {{site.data.keyword.Bluemix_notm}}에서 항목이 캡처되고 기록되는 시간을 표시합니다.
* **_source:** 이 필드는 항목의 원래 데이터를 포함합니다.

다음과 같은 옵션 중에서 선택하여 필드 열을 표에 추가할 수 있습니다.

* 페이지에서 사용할 수 있는 필드 목록에서 필드 열을 추가하십시오.

    1. 검색 페이지의 `선택한 필드` 섹션에서 필드를 식별하십시오.
    2. 필드 목록에 있는 필드 위로 마우스를 이동하십시오.
    3. 필드를 추가하려면 **추가**를 클릭하십시오.
    
 * 확장된 항목의 표 보기에서 필드 열을 추가하십시오.

    1. 표에서 항목을 펼치십시오.
    2. 표 보기에서 추가하려는 필드를 식별하십시오.
    3. **표에서 열 전환** 아이콘 ![표에서 열 전환](images/toggle_field_icon.jpg "열 전환 이미지")을 클릭하십시오.
    

**참고:** 표에 하나의 필드 열을 처음 추가하면 표에 표시되는 *_소스* 필드 열이 숨겨집니다. *_소스* 필드는 각 로그 항목에 대한 각 필드의 값을 표시합니다. 표에 열을 추가한 후에 표에서 로그 항목에 대한 다른 필드 값을 보려면 각 항목의 JSON 탭 또는 표 보기 탭을 보십시오.


## 자동으로 데이터 새로 고치기
{: #discover_view_refresh_interval}

기본적으로 {{site.data.keyword.Bluemix_notm}}에서 *자동으로 새로 고치기* 기간은 **OFF**로 설정되고 Kibana에서 볼 수 있는 데이터는 사용자가 Kibana를 실행한 이후 최근 15분에 해당합니다. 이 15 분은 사전 구성된 시간 필터에 해당합니다. 다른 기간을 설정하여 이를 변경할 수 있습니다. 자세한 정보는 [시간 필터 설정](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)을 참조하십시오.

*자동으로 새로 고치기* 간격을 설정하려면 다음 단계를 완료하십시오.

1. 검색 페이지 메뉴 표시줄에서 시간 선택도구 ![시간 선택도구](images/time_picker_icon.jpg "시간 선택도구")를 클릭하십시오.

2. 자동으로 새로 고치기 단추 ![자동으로 새로 고치기 단추](images/auto_refresh_icon.jpg "자동으로 새로 고치기 단추")를 선택하십시오.

3. 새로 고치기 간격을 선택하십시오.

    올바른 값: *Off*, *5초*, *10초*, *30초*, *45초*, *1분*, *5분*, *15분*, *30분*, *1시간*, *2시간*, *12시간*, *1일*. 

일시정지 단추 ![일시정지 단추](images/auto_refresh_pause_icon.jpg "일시정지")를 클릭하여 새로 고치기 간격을 일시정지할 수 있습니다. 


## 검색 페이지에 표시된 데이터 식별
{:#identify_data}

Kibana를 사용하여 {{site.data.keyword.Bluemix_notm}} 로그를 분석할 때 볼 수 있는 데이터는 Kibana를 실행하는 방법, 구성된 인덱스 패턴, 사용자가 적용한 사용자 정의 조회 및 필터에 따라 달라질 수 있습니다.

검색 페이지의 표와 히스토그램에서 사용 가능한 데이터를 식별하려면 다음과 같은 정보를 고려하십시오.

1. **관리** 페이지에서 인덱스 패턴을 확인하십시오.

    인덱스 패턴은 Kibana 페이지에 항목을 표시하도록 기본적으로 적용되는 검색 조회를 정의합니다. 기본적으로 인덱스 패턴은 사전 구성되고 영역에서 사용 가능한 모든 데이터에 설정됩니다. 예:

    * {{site.data.keyword.Bluemix_notm}} UI에서 Kibana를 실행하는 경우, 다시 말하면, CF(Cloud Foundry) 애플리케이션 또는 컨테이너와 같은 특정 리소스의 UI 페이지의 *로그* 섹션에서 Kibana를 실행하는 경우, 적용된 인덱스 패턴에는 영역에서 사용할 수 있는 모든 항목이 포함됩니다.
    
    * {{site.data.keyword.loganalysisshort}} 서비스의 대시보드 또는 브라우저에서 Kibana를 실행하는 경우, 적용되는 인덱스 패턴에는 사용자가 로그인한 Kibana에 표시되는 영역에서 사용 가능한 모든 항목이 포함됩니다.
        
2. 검색 페이지에서 조회를 확인하십시오.  

    검색 페이지에 표시되는 조회는 기본적으로 분석에 사용 가능한 항목을 필터링하는 데 사용됩니다. 예:

    * 검색 표시줄에 임의의 문자열을 입력하면 조회는 해당 문자열에 대한 모든 필드를 스캔합니다.
    
    * 조회가 다음과 같이 설정된 경우: `application_id:<GUID>` 여기서 *GUID*는 CF 앱의 ID이며, 사용자가 볼 수 있는 항목은 인덱스 패턴에서 구성된 영역의 그 CF 앱에 사용 가능한 모든 항목에 해당합니다.
    
    * 조회가 다음과 같이 설정된 경우: `instance_id:<GUID>` 여기서 *GUID*는 컨테이너 인스턴스의 ID이며, 사용자가 볼 수 있는 항목은 인덱스 패턴에서 구성된 영역의 그 컨테이너에 사용 가능한 모든 항목에 해당합니다.
    
    * 조회가 다음과 같이 설정된 경우: `instance_id:<GUID> AND instance_id:<GUID>` 여기서 *GUID*는 컨테이너 인스턴스의 ID이며, 사용자가 볼 수 있는 항목은 인덱스 패턴에서 구성된 영역의 그 컨테이너 그룹에 사용 가능한 모든 항목에 해당합니다.
   
    * 조회가 `*`로 설정된 경우, 데이터가 인덱스 패턴에서 구성된 영역에서 사용 가능한 모든 항목으로 설정됩니다.
    
    * 조회가 다음과 같이 설정된 경우: `application_id:<GUID> AND message:"MY_search_text"` 여기서 *GUID*는 CF 앱의 ID이고 *My_search_text*는 검색하려는 문자열이며, 사용자가 볼 수 있는 항목은 인덱스 패턴에 구성된 영역에서 사용 가능한 그 CF 앱 항목에 대한 메시지 필드의 *My_search_text*가 포함된 모든 항목에 해당합니다.
    
3. 검색 페이지에서 조회에 적용된 필드 필터를 확인하십시오.

    필드 필터를 정의하여 필드의 값을 기반으로 항목을 전환할 수 있습니다. 예를 들어 필드 필터가 사용 가능한 경우, 표시되는 항목은 해당 필드의 값이 일치하는 항목에 해당합니다.
    

## 색인화된 필드의 값순으로 항목 순서 지정 
{: #discover_sort_by_table}

색인화된 필드의 항목만 표에서 정렬할 수 있습니다.

색인화된 필드를 알아보려면 다음 단계를 완료하십시오.

1. 검색 페이지에서 그 페이지의 **사용 가능한 필드** 섹션에서 사용 가능한 구성 아이콘 ![구성 아이콘](images/configure_icon.jpg "구성 아이콘")을 클릭하십시오.

2. 색인화된 필드를 식별하려면 **색인화됨** 검색 필드에 대해 **예**를 선택하십시오.

    색인화된 필드의 목록이 표시됩니다.
 
색인화된 필드의 값으로 표에서 항목을 정렬하려면 다음 단계를 완료하십시오. 

1. 데이터를 정렬하려는 표에 있는 필드의 이름 위로 마우스를 이동하십시오. 다른 조치 단추가 표시됩니다.
2. 데이터를 정렬하려는 필드에 대해 정렬 단추를 클릭하십시오. 정렬 순서를 반대로 하려면 필드 정렬 아이콘을 두 번 클릭하십시오.

**참고:** 시간별로 필드를 정렬할 때는 기본적으로 항목이 역시간 순서로 정렬됩니다. 최신 항목이 우선 표시됩니다.


## 표에서 필드 열 재배열
{: #discover_rearrange_fields_in_table}

표에서 필드 열을 재배열할 수 있습니다. 이동하려는 열의 헤더 위로 마우스를 이동하고 **왼쪽으로 열 이동** 단추 또는 **오른쪽으로 열 이동** 단추를 클릭하십시오.


## 필드의 목록 다시 로드
{: #discover_view_reload_fields}

Kibana에 표시되는 필드의 목록을 다시 로드하려면 다음 단계를 완료하십시오.

1. **관리** 페이지를 선택한 후에 **인덱스 패턴**을 선택하여 사용 가능한 인덱스를 나열하십시오.
   
2. Elasticsearch에 의해 기록된 대로 모든 필드 및 필드의 연관된 코어 유형을 보려면 사용자의 영역의 인덱스 패턴을 선택하십시오. 

3. 인덱스 패턴 필드를 다시 로드하려면 *필드 목록 다시 로드* 단추 ![필드 목록 다시 로드](images/reload_field_list_icon.jpg "필드 목록 다시 로드")를 클릭하십시오. 

필드의 목록이 새로 고쳐집니다.


## 표에서 필드 열 제거
{: #discover_remove_fields_from_table}

표에서 필드를 제거하려면 다음 단계를 완료하십시오.

1. 표 보기에서 제거하려는 필드를 표에서 식별하십시오.
2. **열 제거**를 클릭하십시오.
    

## 표에서 항목 보기
{: #discover_view_entry_in_table}

표에서 항목의 데이터를 보려면 분석하려는 항목의 펼치기 단추 ![펼치기 단추 아이콘](images/expand_icon.jpg "펼치기 단추 아이콘")을 클릭하십시오. 

그리고 데이터를 보려면 다음 옵션 중 하나를 선택하십시오.

* 표 형식으로 데이터를 보려면 **표**를 클릭하십시오. 분석에 사용 가능한 각 필드의 값을 표 형식으로 볼 수 있습니다. 또한, 각 필드에 필터 단추와 전환 단추가 있습니다.
* JSON 형식으로 데이터를 보려면 **JSON**을 클릭하십시오.

## 필드 데이터 통계 보기
{: #discover_view_fields_stats}

검색 페이지에서 *필드 목록* 및 *히스토그램*에서 각 필드의 통계를 볼 수 있습니다. 

필드 목록에서 다음 정보를 볼 수 있습니다.
* 특정 필드가 포함된 표의 항목 수.
* 상위 5개의 값.
* 각 값이 포함된 항목의 백분율.

히스토그램에서 다음 정보를 볼 수 있습니다.
* 시간 범위의 항목 수.

예를 들어, 히스토그램에서 통계를 보려면 시간 소인을 클릭하여 해당 기간에 대한 통계를 보십시오. 필드 목록에서 필드에 대한 통계를 보려면 이름을 클릭하십시오. 


