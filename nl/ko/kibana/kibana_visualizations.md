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

# 시각화를 사용하여 Kibana에서 로그 분석 
{:#kibana_visualizations}

Kibana에서 *시각화* 페이지를 사용하여 로그 데이터를 분석하고 결과를 비교하는 데 사용할 수 있는 그래프 및 표와 같은 시각화를 작성할 수 있습니다. 
{:shortdesc}

개별적으로 시각화를 사용하여 로그를 분석할 수 있습니다. 

* *검색* 페이지에 저장하는 검색이나 *시각화* 페이지에 정의하는 새 조회에서 시각화를 작성할 수 있습니다. 검색은 시각화가 표시하는 데이터의 서브세트를 정의합니다.

* 사용자가 선택하는 시각화의 유형은 분석을 위해 데이터가 표시되는 방법을 판별합니다.

여러 가지 시각화 유형이 다음 표에 나열되어 있습니다.

|시각화의 유형 |설명 |
|-----------------------|-------------|
|영역 차트 |양적 데이터를 그래프로 표시합니다. 집계된 데이터의 세트를 두 개 이상을 비교하는 데 사용합니다. |
|데이터 표 |구성된 집계에 대해 원시 데이터를 표 형식으로 표시합니다. |
|선형 차트 |시간 기반 데이터를 표시합니다. 시간 기반으로 집계된 데이터의 세트를 두 개 이상을 비교하는 데 사용합니다. |
|마크다운 위젯 |텍스트 정보를 표시하는 데 사용합니다. |
|메트릭 |히트 수 또는 숫자 필드의 정확한 평균을 표시하는 데 사용합니다. |
|원형 차트 |필드의 다른 값을 표시하는 데 사용합니다. | 
|세로 막대형 차트 |시간 기반인 데이터와 시간 기반이 아닌 데이터를 표시합니다. 데이터를 그룹화하는 데 사용합니다. |
{: caption="표 1. 시각화 유형" caption-side="top"}

시각화 페이지에서 다음 태스크를 수행할 수 있습니다.

|태스크 |자세한 정보 |
|------|------------------|
|[새 시각화 작성](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#create) |*검색* 페이지에 저장하는 검색이나 *시각화* 페이지에 정의하는 새 조회에서 시각화를 작성할 수 있습니다. |
|[시각화 삭제](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#delete) |필요하지 않은 시각화는 삭제합니다. |
|[시각화 내보내기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#export) |시각화를 JSON 파일로 내보낼 수 있습니다.  |
|[시각화 가져오기](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#import1) |시각화를 JSON 파일로 가져올 수 있습니다.  |
|[시각화 로드](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#reload2) |해당 데이터를 업데이트, 수정 또는 분석하기 위해 시각화를 업로드할 수 있습니다. |
|[시각화 저장](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#save2) |나중에 다시 사용할 수 있도록 시각화를 저장할 수 있습니다. |
{: caption="표 2. 시각화로 작업하는 태스크" caption-side="top"}


## Kibana의 조회에서 시각화 작성
{: #create}

시각화 페이지에서 시각화를 작성하려면 다음 단계를 완료하십시오.

1. Kibana를 실행한 후에 **시각화** 페이지를 선택하십시오.

2. 시각화의 유형(예: *표*)을 선택하십시오.

3. **또는, 저장된 검색에서**에서 이전에 저장한 시각화를 선택하거나 **새 검색에서, 인덱스 선택** 섹션에서 인덱스를 선택하십시오.

4. 조회를 구성하십시오.

    * **또는, 저장된 검색에서**를 선택하는 경우, 검색 조회를 선택하십시오. 조회는 시각화에 사용된 데이터를 검색하는 데 사용됩니다. 
	
	    검색을 선택한 후에 시각화 빌더가 열리고 선택한 조회에 대한 데이터를 로드합니다. 
		
		**참고**: 저장된 검색에 작성하는 변경사항은 자동으로 시각화에 반영됩니다. 이 시각화에 링크된 조회에 작성하는 자동 업데이트를 사용 안함으로 설정하려면 *이 시각화는 저장된 검색(your_search_name)에 링크됩니다*라는 메시지를 두 번 클릭하십시오. 

    * **새 검색에서, 인덱스 선택**을 선택하는 경우 새 조회를 정의하십시오. 조회는 시각화에서 검색하고 사용하는 데이터의 서브세트를 정의하는 데 사용됩니다.

        자세한 정보는 [사용자 정의 조회를 정의하여 로그 필터링](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search)을 참조하십시오.

Kibana에 대한 자세한 정보는 [Kibana User Guide ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}를 참조하십시오.


## 시각화 삭제
{: #delete}

시각화를 삭제하려면 **관리** 페이지에서 다음 단계를 완료하십시오.

1. **관리** 페이지에서 **저장된 오브젝트**를 선택하십시오.

2. **시각화** 탭에서 삭제하려는 시각화를 선택하십시오.

3. **삭제**를 클릭하십시오.


## 시각화 내보내기
{: #export1}

시각화를 JSON 파일로 내보내려면 **관리** 페이지에서 다음 단계를 완료하십시오.

1. **관리** 페이지에서 **저장된 오브젝트**를 선택하십시오.

2. **시각화** 탭에서 내보내려는 시각화를 선택하십시오.

3. **내보내기**를 클릭하십시오.

4. 파일을 저장하십시오.

## 시각화 가져오기
{: #import1}

시각화를 JSON 파일로 가져오려면 **관리** 페이지에서 다음 단계를 완료하십시오.

1. **관리** 페이지에서 **저장된 오브젝트**를 선택하십시오.

2. **시각화** 탭에서 **가져오기**를 선택하십시오.

3. 파일을 선택하고 **열기**를 클릭하십시오.

시각화가 시각화 목록에 추가됩니다.


 
## 시각화 로드
{: #reload2}

저장된 시각화를 로드하려면 다음 단계를 완료하십시오.

1. 시각화 페이지의 도구 모음에서 **열기**를 클릭하십시오.

2. 로드하려는 시각화를 선택하십시오. 


## 시각화 저장
{: #save2}

시각화 페이지에서 시각화를 저장하려면 다음 단계를 완료하십시오.

1. 시각화 페이지의 도구 모음에서 **저장**을 클릭하십시오.

2. 시각화의 이름을 입력하십시오.

3. 저장을 클릭하십시오. 


