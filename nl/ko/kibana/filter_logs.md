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

# Kibana에서 로그 필터링
{:#filter_logs}

검색 페이지에서 분석을 위해 표시되는 정보를 제한하도록 검색 조회를 작성하고 필터를 적용할 수 있습니다.
{:shortdesc}

* 검색 페이지의 검색 표시줄에 하나 이상의 검색 조회를 정의할 수 있습니다. 검색 조회는 로그 항목의 서브세트를 정의합니다. Lucene 조회 언어를 사용하여 검색 조회를 정의합니다. 

* *필드 목록* 또는 표 항목에서 필터를 추가할 수 있습니다. 필터는 정보를 포함하거나 제외하여 데이터 선택을 세분화합니다. 필터를 사용 또는 사용 안함으로 설정, 필터 조치 전환, 필터를 설정 또는 해제로 전환하거나 완전히 제거할 수 있습니다. 

새 검색을 정의한 후에 검색 페이지에서 향후 분석에 다시 사용할 수 있도록 하거나 사용자 정의 대시보드에서 사용할 수 있는 시각화를 작성하도록 저장하십시오. 자세한 정보는 [검색 저장](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search1)을 참조하십시오.

새 검색을 수행하면 히스토그램, 표 및 필드 목록이 검색 결과를 표시하도록 자동으로 업데이트됩니다. 어떤 데이터가 표시되는지 알아보려면 [검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

다음 목록은 로그에서 데이터를 필터링하는 방법을 표시하는 시나리오를 간략하게 설명합니다.

* 로그를 필터링하기 위한 사용자 정의 검색을 작성할 수 있습니다. 자세한 정보는 [사용자 정의 조회를 정의하여 로그 필터링](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search)을 참조하십시오.

* 필드의 값에서 특정 텍스트를 포함하는 항목에 대한 로그를 검색할 수 있습니다. 자세한 정보는 [필드 값에서 특정 텍스트에 대한 로그 필터링](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs_spec_text)을 참조하십시오.
 
* 특정 필드 값에 대한 로그를 검색하거나 특정 필드 값에 대한 로그에서 항목을 제외할 수 있습니다. 자세한 정보는 [특정 필드 값에 대한 로그 필터링](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs_spec_field)을 참조하십시오.
 
* 어느 기간 내의 항목을 표시하도록 로그를 필터링할 수 있습니다. 자세한 정보는 [시간 필터 설정](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)을 참조하십시오.
     

## *필드 목록*에 나열되지 않은 값에 대한 필터 추가
{:#add_filter_out_value}

*필드 목록*에 표시되지 않은 값에 대한 필터를 추가하려면 조회를 통해 해당 값을 포함하는 레코드를 검색하십시오. 그리고 검색 페이지에서 사용 가능한 표 항목에서 필터를 추가하십시오. 

*필드 목록* 섹션에 표시된 목록에서 사용할 수 없는 값에 대한 필터를 추가하려면 다음 단계를 완료하십시오.

1. Kibana 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

2. 검색 페이지에서 특정 필드 값을 검색하려면 조회를 수정하십시오.

    예를 들어, 인스턴스 *3*을 검색하려면 입력하는 조회는 다음과 같습니다.
   `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:"3"`
    
    표에서 조회와 일치하는 레코드를 볼 수 있습니다. 
    
 3. 하나의 레코드를 펼치고 돋보기 단추 ![포함 모드의 돋보기 단추](images/include_field_icon.jpg "포함 모드의 돋보기 단추")를 선택하여 필터를 추가하십시오.
     
4. 필터가 추가되었는지 확인하십시오.

   


## 특정 필드 값에 대한 로그 필터링
{:#filter_logs_spec_field}

특정 필드 값을 포함하는 항목을 검색할 수 있습니다. 

특정 필드 값이 포함된 항목을 검색하려면 다음 단계를 완료하십시오.

1. Kibana 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

2. *필드 목록*에서 필터를 정의하려는 필드를 식별해서 그 필드를 클릭하십시오.

    최대 5개의 값이 필드에 표시됩니다. 각 값에는 두 개의 돋보기 단추가 있습니다. 
    
    값을 볼 수 없는 경우, [필드 목록에 나열되지 않은 값에 대한 필터 추가](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#add_filter_out_value)를 참조하십시오.

3. 필드 값이 있는 항목을 검색하는 필터를 추가하려면 해당 값에 대한 더하기 부호가 있는 돋보기 ![포함 모드의 돋보기 단추](images/include_field_icon.jpg "포함 모드의 돋보기 단추")를 선택하십시오.

    해당 필드 값이 포함되지 않은 항목을 검색하는 필터를 추가하려면 값에 대한 빼기 부호가 있는 돋보기 ![제외 모드의 돋보기 단추](images/exclude_field_icon.jpg "제외 모드의 돋보기 단추")를 선택하십시오.

4. Kibana의 필터로 작업하려면 다음 옵션 중에서 선택하십시오.

    <table>
      <caption>표 1. 필터로 작업하는 방법</caption>
      <tbody>
        <tr>
          <th align="center">옵션</th>
          <th align="center">설명</th>
          <th align="center">기타 정보</th>
        </tr>
        <tr>
          <td align="left">사용</td>
          <td align="left">필터를 사용하려면 이 옵션을 선택하십시오.</td>
          <td align="left">필터를 추가하면 자동으로 사용 가능하게 설정됩니다. <br> 필터가 사용 안함으로 되어 있으면 클릭하여 사용으로 설정하십시오.</td>
        </tr>
        <tr>
          <td align="left">사용 안함</td>
          <td align="left">필터를 사용 안함으로 설정하려면 이 옵션을 선택하십시오.</td>
          <td align="left">필터를 추가한 후에 필드 값에 대한 항목을 숨기고 싶으면 **사용 안함**을 클릭하십시오.</td>
        </tr>
        <tr>
          <td align="left">핀</td>
          <td align="left">Kibana 페이지에서 필터를 유지하려면 이 옵션을 선택하십시오.</td>
          <td align="left">*검색* 페이지, *시각화* 페이지 또는 *대시보드* 페이지에서 필터를 핀으로 고정할 수 있습니다.</td>
        </tr>
        <tr>
          <td align="left">전환</td>
          <td align="left">필터를 전환하려면 이 옵션을 선택하십시오.</td>
          <td align="left">기본적으로 필터와 일치하는 항목이 표시됩니다. 일치하지 않는 항목을 표시하려면 필터를 전환하십시오.</td>
        </tr>
        <tr>
          <td align="left">제거</td>
          <td align="left">필터를 제거하려면 이 옵션을 선택하십시오.</td>
          <td align="left"></td>
        </tr>
      </tbody>
    </table>

	
## 소스별 CF 앱 로그 필터링
{:#filter_logs_by_source}

특정 로그 소스가 포함된 항목을 검색하려면 다음 단계를 완료하십시오.

1. Kibana 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

2. *필드 목록*에서 **source_id** 필드를 선택하십시오.

3. 특정 source_id가 포함된 항목을 검색하는 필터를 추가하려면 해당 값에 대한 돋보기 단추 ![포함 모드의 돋보기 단추](images/include_field_icon.jpg "포함 모드의 돋보기 단추")를 선택하십시오.

    CF 앱에 사용 가능한 로그 소스의 목록에 대해서는 [CF 앱에 대한 로그 소스](/docs/services/CloudLogAnalysis/cfapps?topic=cloudloganalysis-logging_cf_apps#logging_bluemix_cf_apps_log_sources)를 참조하십시오.

    특정 source_id가 포함되지 않은 항목을 검색하는 필터를 추가하려면 값에 대한 돋보기 단추 ![제외 모드의 돋보기 단추](images/exclude_field_icon.jpg "제외 모드의 돋보기 단추")를 선택하십시오.
    


## 로그 유형별 로그 필터링
{:#filter_logs_by_log_type}

특정 로그 유형이 포함된 항목을 검색하려면 다음 단계를 완료하십시오.

1. Kibana 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

2. *필드 목록*에서 **유형** 필드를 선택하십시오.

3. 특정 로그 유형을 검색하는 필터를 추가하려면 분석하고 싶은 로그의 유형에 대한 돋보기 단추 ![포함 모드의 돋보기 단추](images/include_field_icon.jpg "포함 모드의 돋보기 단추")를 선택하십시오.

    특정 로그 유형이 포함되지 않은 항목을 검색하는 필터를 추가하려면 값에 대한 돋보기 단추 ![제외 모드의 돋보기 단추](images/exclude_field_icon.jpg "제외 모드의 돋보기 단추")를 선택하십시오.



## 인스턴스 ID별 로그 필터링
{:#filter_logs_by_instance_id}

Kibana 대시보드에서 인스턴스 ID별로 로그를 보고 필터링하려면 다음 단계를 완료하십시오.

1. Kibana 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

2. *필드 목록*에서 특정 인스턴스 ID를 검색하려면 다음 필드 중 하나를 선택하십시오.

    * **instance_ID**: 이 필드에는 Cloud Foundry 애플리케이션의 로그에서 사용할 수 있는 여러 가지 인스턴스 ID가 나열됩니다. 
    * **instance**: 이 필드에는 컨테이너 그룹에 대한 모든 인스턴스의 여러 가지 GUID가 나열됩니다. 
	* **docker.container_id_str**: 이 필드에는 Kubernetes 인프라에 배치된 컨테이너에 대한 여러 가지 컨테이너 ID가 나열됩니다.
   
3. 특정 로그 유형을 검색하는 필터를 추가하려면 분석하고 싶은 로그의 유형에 대한 돋보기 단추 ![포함 모드의 돋보기 단추](images/include_field_icon.jpg "포함 모드의 돋보기 단추")를 선택하십시오.

    특정 인스턴스 ID가 포함되지 않은 항목을 검색하는 필터를 추가하려면 값에 대한 돋보기 단추 ![제외 모드의 돋보기 단추](images/exclude_field_icon.jpg "제외 모드의 돋보기 단추")를 선택하십시오.



## 메시지 유형별 CF 앱 로그 필터링
{:#filter_cf_logs_by_msg_type}

특정 메시지 유형이 포함된 항목을 검색하려면 다음 단계를 완료하십시오.

1. Kibana 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

2. *필드 목록*에서 **message_type** 필드를 선택하십시오.

    사용 가능한 필드 유형이 표시됩니다. 

3. 특정 *message_type*이 포함된 항목을 검색하는 필터를 추가하려면 해당 값에 대한 돋보기 단추 ![포함 모드의 돋보기 단추](images/include_field_icon.jpg "포함 모드의 돋보기 단추")를 선택하십시오.

    특정 *message_type*이 포함되지 않은 항목을 검색하는 필터를 추가하려면 값에 대한 돋보기 단추 ![제외 모드의 돋보기 단추](images/exclude_field_icon.jpg "제외 모드의 돋보기 단추")를 선택하십시오.
    
 
	

## 필드 값의 특정 텍스트에 대한 로그 필터링
{:#filter_logs_spec_text}

필드의 값에서 특정 텍스트를 포함하는 항목을 보고 검색합니다. 

**참고:** Elasticsearch 분석기에서 분석한 문자열 필드의 자유 텍스트 검색만 수행할 수 있습니다. 
    
Elasticsearch가 문자열 필드의 값을 분석할 때 단어 경계에서 텍스트를 분할하며 유니코드 컨소시엄에 의해 정의된 대로 모든 단어에서 구두점 및 소문자를 제거합니다.
    
필드 값에 특정 텍스트가 포함된 항목을 검색하려면 다음 단계를 완료하십시오.

1. Kibana 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)을 참조하십시오.

2. 기본적으로 ElasticSearch에서 분석되는 필드를 식별하십시오.

    로그 데이터 검색 및 필터링에 사용할 수 있는 분석된 필드의 전체 목록을 표시하려면 [필드의 목록을 다시 로드](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#discover_view_reload_fields)하십시오. 그리고 검색 페이지에서 사용 가능한 *필드 목록*에서 다음 단계를 완료하십시오.
    
    1. 구성 아이콘 ![구성 아이콘](images/configure_icon.jpg "구성 아이콘")을 클릭하십시오. 필드를 필터링할 수 있는 **선택한 필드** 섹션이 표시됩니다.

    2. 분석된 필드를 식별하려면 검색 필드 **분석됨**에 **예**를 선택하십시오.

        분석된 필드의 목록이 표시됩니다.
    
    3. 자유 텍스트를 검색하려는 필드가 기본적으로 ElasticSearch에 의해 분석된 필드인지 확인하십시오.
    
3. 필드가 분석된 경우, 필드의 값의 일부로 자유 텍스트가 포함된 로그에서 항목을 검색하도록 조회를 수정하십시오.

    
**예**

{{site.data.keyword.Bluemix}} UI에서 CF(Cloud Foundry) 애플리케이션에 대해 Kibana를 실행하고, 메시지 ID *CWWKT0016I:*가 포함된 특정 메시지를 검색하려는 경우, 자유 텍스트를 포함하도록 검색을 수정하십시오.
    
1. 로드된 검색 조회 및 검색 페이지에 표시되는 데이터를 확인하십시오.
       
2. 메시지 ID *CWWKT0016I*를 검색하려면 **검색 표시줄**에서 검색 조회를 수정하고 **Enter**를 클릭하십시오.
    
    예를 들면, ID *f52f6016-3aab-4b5c-aa2e-5493747cb978*의 CF 앱에 대해 다음 텍스트를 검색 표시줄에 입력하십시오.

	`<pre class="pre">application_id:f52f6016-3aab-4b5c-aa2e-5493747cb978 AND message:"CWWKT0016I:" </pre>`
        
          
텍스트 *CWWKT0016I*가 *메시지* 필드에서 값의 일부인 CF 앱에 대한 항목이 표에 표시됩니다.
    
 	
        

## 시간 필터 설정
{: #set_time_filter}

*시간 선택도구*를 구성하여 기간 내의 로그를 보고 필터링하십시오.

검색 페이지에서 *시간 선택도구*를 구성할 수 있습니다. 기본적으로 최근 15분으로 설정됩니다. 

특정 시간이 포함된 항목을 검색하려면 다음 단계를 완료하십시오.

1. 검색 페이지 메뉴 표시줄에서 시간 선택도구 ![시간 선택도구](images/time_picker_icon.jpg "시간 선택도구")를 클릭하십시오.

2. 시간 간격을 설정하십시오. 

    다음과 같은 유형의 시간 간격을 정의할 수 있습니다.
    
    * 빠름: 상대 및 절대 시간 간격 모두의 가장 일반적인 사용을 포함하는 사전 정의된 시간 간격입니다(예: *오늘* 및 *이번 달*). 
       
    * 상대: 시작 날짜와 시간 및 종료 날짜와 시간을 지정할 수 있는 시간 간격입니다. 시간 단위로 반올림할 수 있습니다.
    
    * 절대: 시작 날짜와 종료 날짜 사이의 시간 간격입니다.
    

시간 간격을 구성한 후에는 Kibana에 표시된 데이터가 그 시간 범위 내의 항목에 해당합니다.








