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

# 사용자 정의 검색 조회 정의
{:#define_search}

검색 페이지의 검색 표시줄에서 Lucene 조회 언어를 사용하여 검색 조회를 정의하고 저장할 수 있습니다. 각 검색에 대해 필터를 적용하여 분석에 사용할 수 있는 항목을 세분화할 수 있습니다.
{:shortdesc}

사용자 정의 검색을 정의하려면 다음 태스크를 완료하십시오.

1. Kibana를 실행하십시오.

    CF(Cloud Foundry) 앱의 경우, [CF 앱의 대시보드에서 Kibana 실행](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app)을 참조하십시오.

	{{site.data.keyword.Bluemix_notm}} 관리 인프라에서 실행되는 컨테이너의 경우 [컨테이너의 대시보드에서 Kibana 실행](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers)을 참조하십시오.
    
    모든 클라우드 리소스(예: Kubernetes 클러스터에서 실행되는 컨테이너)의 경우, [브라우저에서 Kibana 실행](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)을 참조하십시오. 
	
	Kibana에 액세스하면 기본 검색이 적용됩니다. 조회 중인 리소스에 해당하는 인스턴스의 목록에 대한 로그를 볼 수 있습니다. 해당 영역의 일부 또는 모든 {{site.data.keyword.Bluemix_notm}} 리소스에 대해 로그를 필터링할 수 있습니다.

2. 검색 페이지에서 표시하는 데이터의 서브세트를 확인하십시오. 자세한 정보는 [Kibana 검색 페이지에 표시된 데이터 식별](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data)을 참조하십시오. 그런 다음 항목을 필터링하도록 기본 조회를 수정하십시오.

    **참고:** Lucene 조회 언어를 사용하여 사용자 정의 조회를 정의합니다. 자세한 정보는 [Apache Lucene - 조회 구문 분석기 구문 ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}을 참조하십시오.
    
    {{site.data.keyword.Bluemix_notm}} UI에서 Kibana가 실행되면 조회를 수정하고 다중 검색 기준을 정의하기 위해 논리 용어 **AND** 및 **OR**을 사용할 수 있습니다. 이러한 연산자는 대문자여야 합니다.    
    
    * 키워드 또는 키워드의 일부를 검색하려면 단어 다음에 와일드카드인 별표(*)를 입력하십시오(예: `Java*`). 
    * 특정 문구를 검색하려면 큰따옴표 안(" ")에 해당 문구를 입력하십시오(예: `"Java/1.8.0"`).
    * 더 복잡한 검색을 작성하려면 논리 용어 AND 및 OR를 사용할 수 있습니다(예: `"Java/1.8.0" OR "Java/1.7.0"`).
    * 특정 필드 내의 값을 검색하려면 *log_field_name:search_term* 양식으로 검색을 입력하십시오(예: `instance_id:"1"`).
    * 특정 로그 필드에 대한 값의 범위를 검색하려면 *log_field_name:[start_of_range TO end_of_range]* 양식으로 검색을 입력하십시오(예: `instance_id:["1" TO "2"]`).

     예를 들어, CF 앱의 경우 인스턴스 *0* 및 *1*에 대한 항목만 나열하는 조회 `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]`을 작성할 수 있습니다. 

3. 나중에 다시 사용할 수 있도록 조회를 저장하십시오. 자세한 정보는 [검색 저장](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1)을 참조하십시오. 

**참고:** 조회를 삭제해야 하는 경우, [검색 삭제](/docs/services/CloudLogAnalysis/kibana/define_search.html#delete_search)를 참조하십시오.



## 검색 삭제
{: #delete_search}

검색을 삭제하려면 설정 페이지에서 다음 단계를 완료하십시오.

1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.

2. **검색** 탭에서 삭제하려는 검색을 선택하십시오.

3. **삭제**를 클릭하십시오.


## 검색 내보내기
{: #export_search}

검색을 내보내려면 설정 페이지에서 다음 단계를 완료하십시오.

1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.

2. **검색** 탭에서 내보내려는 검색을 선택하십시오.

3. **내보내기**를 클릭하십시오.

4. 파일을 저장하십시오.

 
## 검색 가져오기
{: #import_search}

검색을 가져오려면 설정 페이지에서 다음 단계를 완료하십시오.

1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.

2. **검색** 탭에서 **가져오기**를 선택하십시오.

3. 파일을 선택하고 **열기**를 클릭하십시오.

검색이 검색 목록에 추가됩니다.

## 검색의 컨텐츠 새로 고치기
{: #refresh_search}

검색 컨텐츠를 수동으로 새로 고치려면 검색 표시줄에서 사용할 수 있는 돋보기를 클릭합니다. 

검색 페이지에 표시된 데이터를 자동으로 새로 고치도록 새로 고치기 간격을 구성할 수 있습니다. 새로 고치기 간격의 현재 값은 검색 페이지의 메뉴 표시줄에 표시됩니다. 기본적으로 자동으로 새로 고치기는 **OFF**로 설정됩니다.

새로 고치기 간격을 설정하려면 다음 단계를 완료하십시오.

1. 검색 페이지에서 메뉴 표시줄에 있는 **시간 필터**를 클릭하십시오.

2. **자동으로 새로 고치기** ![자동으로 새로 고치기](images/auto_refresh_icon.jpg "자동으로 새로 고치기")를 클릭하십시오.

3. 목록에서 새로 고치기 간격을 선택하십시오. 

**참고**: 자동으로 새로 고치기 간격을 사용으로 설정한 후에 일시정지 단추 ![일시정지](images/auto_refresh_pause_icon.jpg "일시정지")를 클릭하여 일시정지할 수 있습니다.


## 검색 다시 로드
{: #reload_search1}

저장된 검색을 로드하려면 다음 단계를 완료하십시오.

1. 검색 페이지의 도구 모음에서 **검색 로드** 단추 ![검색 로드](images/load_icon.jpg "검색 로드")를 클릭하십시오.

2. 로드하려는 검색을 선택하십시오. 

## 새 검색 시작
{: #k4_new_search}

새 검색을 시작하려면 검색 페이지 도구 모음에서 **새 검색** 단추 ![새 검색](images/new_search_icon.jpg "새 검색")을 클릭하십시오.

## 검색 저장 
{: #save_search1}

Kibana에서 사용자 정의 검색을 저장하는 데 대해서는 다음 정보를 고려하십시오.

* 검색을 저장하면 검색 조회 문자열 및 현재 선택된 인덱스 패턴이 저장됩니다.
* *검색* 페이지에서 검색을 열어 이를 수정하는 경우 동일한 이름으로 저장할지 선택하거나 수정된 사용자 정의 검색을 다른 이름으로 저장할 수 있습니다. 기본적으로 제공되는 검색 이름은 처음에 연 사용자 정의 검색의 이름입니다.

    * 수정된 사용자 정의 검색을 동일한 이름으로 저장하려면 **저장**을 클릭하십시오. 원본 사용자 정의 검색을 겹쳐씁니다. 
	
	* 수정된 사용자 정의 검색을 다른 이름으로 저장하려면 **검색 저장** 필드에 새 이름을 입력한 다음 **저장**을 클릭하십시오. 


검색 페이지에서 현재 검색을 저장하려면 다음 단계를 완료하십시오.

1. 검색 페이지의 도구 모음에서 **검색 저장** 단추 ![검색 저장](images/save_search_icon.jpg "검색 저장")을 클릭하십시오.

2. 검색의 이름을 입력하십시오.

    **참고:** **저장**을 클릭하면 겹쳐쓰기에 대한 경고 메시지가 표시되므로 기존 이름을 지정하는 경우 저장은 다른 표시 없이 해당 버전을 바꿉니다.

3. **저장**을 클릭하십시오. 
