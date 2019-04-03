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

# 대시보드를 통해 Kibana에서 로그 분석
{:#kibana_analize_logs_dashboard}

Kibana의 *대시보드* 페이지를 사용하여 대시보드에 그룹화된 시각화 콜렉션을 표시합니다. 대시보드를 사용하여 로그 데이터를 분석하고 결과를 비교합니다.
{:shortdesc}

{{site.data.keyword.Bluemix_notm}}에는 데이터를 시각화하고 분석하기 위해 정의하고 사용자 정의할 수 있는 여러 가지 유형의 대시보드가 있습니다. 그 예로 일부 공통 대시보드 유형이 다음 표에 나열되어 있습니다.

|대시보드의 유형 |설명 |
|-------------------|-------------|
|단일 cf-app 대시보드 |단일 Cloud Foundry 애플리케이션에 대한 정보를 표시하는 대시보드입니다. |
|단일 컨테이너 대시보드  |단일 컨테이너에 대한 정보를 표시하는 대시보드입니다.  |
|컨테이너 그룹 대시보드  |특정 컨테이너 그룹에 대한 정보를 표시하는 대시보드입니다.  |
|다중 cf-app 대시보드 |동일한 영역에 배치된 모든 Cloud Foundry 애플리케이션에 대한 정보를 표시하는 대시보드입니다.  | 
|다중 컨테이너 대시보드 |동일한 영역에 배치된 모든 컨테이너에 대한 정보를 표시하는 대시보드입니다.  |
|영역 대시보드 |영역에서 사용할 수 있는 로깅 데이터를 표시하는 대시보드입니다.  | 
{: caption="표 1. 대시보드 유형의 샘플" caption-side="top"}

대시보드에서 데이터를 시각화하기 위해 패널을 구성합니다. Kibana에는 정보를 분석하는 데 사용할 수 있는 표, 상태동향 및 히스토그램과 같은 여러 다른 시각화가 포함되어 있습니다. 시각화는 패널로 대시보드에 추가됩니다. 대시보드에서 패널을 추가, 제거하고 재배열할 수 있습니다. 각 패널의 목적은 다양합니다. 일부 패널은 하나 이상의 조회 결과를 제공하는 행으로 구성됩니다. 다른 패널은 문서 또는 사용자 정의 정보를 표시합니다. 각 패널은 검색을 기반으로 합니다. 검색은 패널에 표시되는 데이터의 서브세트를 정의합니다. 예를 들어, 데이터를 시각화해서 분석하기 위해 막대형 차트, 원형 차트 또는 표를 구성할 수 있습니다.  

대시보드 페이지에서 수행할 수 있는 여러 가지 태스크가 다음 표에 나열되어 있습니다.

|태스크 |자세한 정보 |
|------|------------------|
|[새 대시보드 작성](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#K4_dashboard_new) |여러 대시보드를 작성할 수 있습니다. 여러 가지 검색, 시각화 및 다양한 로그 데이터의 서브세트를 포함하도록 각 대시보드를 디자인할 수 있습니다.  |
|[대시보드 저장](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#k4_dashboard_save) |나중에 다시 사용할 수 있도록 대시보드를 저장할 수 있습니다. |
|[대시보드 로드](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#k4_dashboard_reload) |해당 데이터를 업데이트, 수정 또는 분석하기 위해 대시보드를 업로드할 수 있습니다. |
|[대시보드 삭제](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#k4_dashboard_delete) |필요하지 않은 대시보드는 삭제합니다. |
|[대시보드 내보내기](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#k4_dashboard_export) |대시보드를 JSON 파일로 내보낼 수 있습니다. |
|[대시보드 가져오기](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#k4_dashboard_import) |대시보드를 JSON 파일로 가져올 수 있습니다. |
|[대시보드 공유](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#k4_dashboard_share) |HTML 소스 또는 Kibana 대시보드를 통해 대시보드를 공유할 수 있습니다. |
|[시각화 추가](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_analize_logs_dashboard.html#k4_dashboard_add_visualization) |기존 시각화 또는 검색을 대시보드에 추가할 수 있습니다.|
{: caption="표 2. 대시보드로 작업하는 태스크" caption-side="top"}

Kibana에 대한 자세한 정보는 [Kibana User Guide ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}를 참조하십시오.

## 새 검색 또는 시각화 추가
{: #k4_dashboard_add_visualization}

기존 시각화 또는 검색을 추가하려면 다음 단계를 완료하십시오.

1. 대시보드 페이지의 도구 모음에서 **시각화 추가** 단추 ![시각화 추가](images/k4_dash_add_visualization_icon.jpg "시각화 추가")를 클릭하십시오.

    **참고**: 시각화와 검색을 추가할 수 있습니다. 

2. **시각화** 탭을 선택하여 시각화를 추가하거나 **검색** 탭을 선택하여 검색을 추가하십시오.

3. 추가하려는 검색 또는 시각화를 클릭하십시오.

    해당 검색 또는 시각화에 대한 패널이 대시보드에 추가됩니다.

## 새 Kibana 대시보드 작성
{: #K4_dashboard_new}

새 대시보드를 작성하려면 다음 단계를 완료하십시오.

1. 대시보드 페이지의 도구 모음에서 **새 대시보드** 단추 ![새 대시보드](images/k4_dash_new_icon.jpg "새 대시보드")를 클릭하십시오.

2. 하나 이상의 검색 및 시각화를 추가하십시오. 자세한 정보는 [새 검색 또는 시각화 추가](/docs/services/CloudLogAnalysis/kibana4/logging_kibana_visualizations.html#logging_k4_visualizations_create)를 참조하십시오.

    검색 또는 시각화를 추가하면 패널이 대시보드에 추가됩니다.

3. 원하는 위치인 대시보드의 부분으로 패널을 끌어서 놓으십시오.
 
4. 나중에 다시 사용할 수 있도록 대시보드를 저장하십시오. 

## Kibana 대시보드 삭제
{: #k4_dashboard_delete}

시각화를 삭제하려면 설정 페이지에서 다음 단계를 완료하십시오.

1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.

2. **시각화** 탭에서 삭제하려는 시각화를 선택하십시오.

3. **삭제**를 클릭하십시오.

## Kibana 대시보드 내보내기
{: #k4_dashboard_export}

대시보드를 JSON 파일 형식으로 내보내려면 설정 페이지에서 다음 단계를 완료하십시오.

1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.

2. **대시보드** 탭에서 내보내려는 대시보드를 선택하십시오.

3. **내보내기**를 클릭하십시오.

4. 파일을 저장하십시오.

## Kibana 대시보드 가져오기
{: #k4_dashboard_import}

대시보드를 JSON 파일 형식으로 가져오려면 설정 페이지에서 다음 단계를 완료하십시오.

1. 설정 페이지에서 **오브젝트** 탭을 선택하십시오.

2. **대시보드** 탭에서 **가져오기**를 선택하십시오.

3. 파일을 선택하고 **열기**를 클릭하십시오.

대시보드가 대시보드 목록에 추가됩니다.

## Kibana 대시보드 로드
{: #k4_dashboard_reload}

저장된 대시보드를 로드하려면 다음 단계를 완료하십시오.

1. 대시보드 페이지의 도구 모음에서 **저장된 대시보드 로드** 단추 ![저장된 대시보드 로드](images/k4_dash_load_icon.jpg "저장된 대시보드 로드")를 클릭하십시오.

2. 로드하려는 대시보드를 선택하십시오. 

## Kibana 대시보드 저장
{: #k4_dashboard_save}

Kibana 대시보드를 사용자 정의한 후에 저장하려면 다음 단계를 완료하십시오.

1. 도구 모음에서 **저장** 단추 ![대시보드 저장](images/k4_dash_save_icon.jpg "대시보드 저장")를 클릭하십시오.

2. 대시보드의 이름을 입력하십시오.

    **참고:** 이름에 공백이 있는 대시보드를 저장하는 경우 저장되지 않습니다.

3. 이름 필드 옆에 있는 **저장** 아이콘을 클릭하십시오.

## Kibana 대시보드 공유
{: #k4_dashboard_share}

대시보드를 공유하려면 다음 단계를 완료하십시오.

1. 대시보드 페이지의 도구 모음에서 **대시보드 공유** 단추 ![대시보드 공유](images/k4_dash_share_icon.jpg "대시보드 공유")를 클릭하십시오.

2. 다음 조치 중 하나를 선택하십시오.

    * **이 대시보드 임베드**: HTML 소스를 통해 대시보드를 공유하려면 이 옵션을 선택하십시오. 
    
        HTML 소스에서 대시보드를 임베드하는 데 사용할 수 있는 HTML 코드를 복사하려면 복사 단추 ![클립보드에 복사](images/k4_copy_to_clipboard.jpg "클립보드에 복사")를 클릭하십시오. 
        
        **참고**: 대시보드를 보려면 사용자가 Kibana에 액세스할 수 있어야 합니다.
	
    * **링크 공유**: Kibana의 대시보드를 다른 사용자와 공유하려면 이 옵션을 선택하십시오.



