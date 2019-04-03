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

# 로그 보기 및 분석(Kibana)
{:#analyzing_logs_Kibana}

오픈 소스 분석 및 시각화 플랫폼인 Kibana 5.1을 사용하여 다양한 그래프(예: 차트, 표)로 된 데이터를 모니터, 검색, 분석 및 시각화할 수 있습니다. Kibana를 사용하여 고급 분석 태스크를 수행합니다.
{:shortdesc}

Kibana는 데이터를 대화식으로 분석하고 대시보드를 사용자 정의하여 로그 데이터를 분석하고 고급 관리 태스크를 수행하는 데 사용할 수 있는 브라우저 기반 인터페이스입니다. 자세한 정보는 [Kibana User Guide ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}를 참조하십시오.

Kibana 페이지에 표시되는 데이터는 검색에 의해 제한됩니다. 기본 데이터 세트는 사전 구성된 인덱스 패턴에 의해 정의됩니다. 정보를 필터링하기 위해 새 검색 조회를 추가하고 기본 데이터 세트에 필터를 적용할 수 있습니다. 그리고 나서 나중에 다시 사용할 수 있도록 검색을 저장할 수 있습니다. 

Kibana에는 로그 분석에 사용할 수 있는 여러 가지 페이지가 포함되어 있습니다.

|Kibana 페이지 |설명 |
|-------------|-------------|
|Discover |이 페이지를 사용하여 검색을 정의하고 표 및 히스토그램을 통해 대화식으로 로그를 분석합니다. |
|시각화 |이 페이지를 사용하여 로그 데이터를 분석하고 결과를 비교하는 데 사용할 수 있는 그래프 및 표와 같은 시각화를 작성합니다.  |
|대시보드 |이 페이지를 사용하여 저장된 시각화 및 검색의 콜렉션을 통해 로그를 분석합니다.  |
{: caption="표 1. Kibana 페이지" caption-side="top"}

**참고:** 3일 전으로 갈 수 있어도 시각화 페이지 또는 대시보드 페이지를 통해 한 번에 1일 전체만 분석할 수 있습니다. 로그 데이터는 기본적으로 3일 동안 저장됩니다. 

|Kibana 페이지 |기간 정보 |
|-------------|-------------------------|
|Discover |최대 3일 동안의 데이터를 분석합니다. |
|시각화 |24시간 동안의 데이터를 분석합니다. <br> 24시간이 경과하는 사용자 정의 기간에 대한 로그 데이터를 필터링할 수 있습니다.  |
|대시보드 |24시간 동안의 데이터를 분석합니다. <br> 24시간이 경과하는 사용자 정의 기간에 대한 로그 데이터를 필터링할 수 있습니다. <br> 사용자가 설정하는 시간 선택도구는 대시보드에 포함된 모든 시각화에 적용됩니다. |
{: caption="표 2. 기간 정보" caption-side="top"}

예를 들면, 이는 다른 페이지를 통해 영역에서 컨테이너 또는 CF 앱에 대한 정보를 표시하도록 Kibana를 사용할 수 있는 방법입니다.

## Kibana 대시보드로 이동
{: #launch_Kibana}

다음 방법 중에서 Kibana를 실행할 수 있습니다.

* {{site.data.keyword.loganalysisshort}} 서비스 대시보드에서

    사용자가 보는 데이터가 제공된 영역 내의 서비스에서 로그를 집계하도록 Kibana를 실행할 수 있습니다.
	
	자세한 정보는 [로그 분석 서비스의 대시보드에서 Kibana로 이동](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_log_analysis)을 참조하십시오.

* {{site.data.keyword.Bluemix_notm}}에서

    해당 특정 앱의 컨텍스트 내에서 Kibana의 특정 CF 앱 로그에 실행할 수 있습니다.  자세한 정보는 [로그 분석 서비스의 대시보드에서 Kibana로 이동](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app)을 참조하십시오.
    
    해당 특정 컨테이너의 컨텍스트 내에서 Kibana의 특정 Docker 컨테이너 로그에 실행할 수 있습니다. 이 기능은 {{site.data.keyword.Bluemix_notm}} 관리 인프라에 배치된 컨테이너에만 적용됩니다.  자세한 정보는 [로그 분석 서비스의 대시보드에서 Kibana로 이동](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers)을 참조하십시오.
    
    CF 앱의 경우, Kibana에서 분석에 사용할 수 있는 데이터 필터링에 사용되는 조회는 Cloud Foundry 애플리케이션에 대한 로그 항목을 검색합니다. 기본적으로 Kibana가 표시하는 로그 정보는 모두 하나의 Cloud Foundry 애플리케이션과 모든 해당 인스턴스와 관련됩니다. 
    
    컨테이너의 경우, Kibana에서 분석에 사용할 수 있는 데이터 필터링에 사용되는 조회는 컨테이너의 모든 인스턴스에 대한 로그 항목을 검색합니다. 기본적으로 Kibana가 표시하는 로그 정보는 모두 하나의 컨테이너 또는 컨테이너 그룹과 모든 해당 인스턴스와 관련됩니다. 
    
    

* 직접 브라우저 링크에서

    사용자가 보는 데이터가 제공된 영역 내의 서비스에서 로그를 집계하도록 Kibana를 실행할 수 있습니다.
    
    대시보드에 표시되는 데이터 필터링에 사용되는 조회는 {{site.data.keyword.Bluemix_notm}} 조직에서 영역에 대한 로그 항목을 검색합니다.     Kibana가 표시하는 로그 정보에는 사용자가 로그인한 {{site.data.keyword.Bluemix_notm}} 조직의 영역 내에 배치된
    모든 리소스에 대한 레코드가 포함되어 있습니다. 
    
    자세한 정보는 [웹 브라우저에서 Kibana 대시보드로 이동](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)을 참조하십시오.
    
    

## 대화식으로 데이터 분석
{: #analyze_discover}

검색 페이지에서 새 검색 조회를 정의하고 조회별로 필터를 적용할 수 있습니다. 로그 데이터는 표와 히스토그램을 통해 표시됩니다. 이러한 시각화를 사용하여 데이터를 대화식으로 분석할 수 있습니다. 자세한 정보는 [Kibana에서 대화식으로 로그 분석](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#analize_logs_interactively)을 참조하십시오.

로그 필드(예: message_type 및 instance_ID)에서 필터를 구성하고 기간을 설정할 수 있습니다. 이러한 필터를 동적으로 사용 또는 사용 안함으로 설정할 수 있습니다. 사용 가능하게 설정하는 조회 및 필터링 기준을 충족하는 로그 항목이 표와 히스토그램에 표시됩니다. 자세한 정보는 [Kibana에서 로그 필터링](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs)을 참조하십시오.

## 시각화를 통해 데이터 분석
{: #analyze_visualize}
    
시각화 페이지에서 새 검색 조회 및 시각화를 정의할 수 있습니다. 저장된 시각화를 열거나 시각화를 저장할 수도 있습니다.

데이터를 분석하기 위해 기존 검색 또는 새 검색을 기반으로 시각화를 작성할 수 있습니다. Kibana에는 정보를 분석하는 데 사용할 수 있는 표, 동향 및 히스토그램과 같은 여러 가지 유형의 시각화가 포함되어 있습니다. 각 시각화의 목적은 다양합니다. 일부 시각화는 하나 이상의 조회 결과를 제공하는 행으로 구성됩니다. 다른 시각화는 문서 또는 사용자 정의 정보를 표시합니다. 검색 조회가 업데이트되는 경우 시각화의 데이터가 수정되거나 변경될 수 있습니다. 웹 페이지에 시각화를 임베드하거나 공유할 수 있습니다. 

자세한 정보는 [시각화를 사용하여 로그 분석](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#kibana_visualizations)을 참조하십시오.

## 대시보드에서 데이터 분석
{: #analyze_dashboard}

대시보드 페이지에서 여러 시각화와 검색을 동시에 사용자 정의, 저장 및 공유할 수 있습니다. 

대시보드에서 시각화를 추가, 제거하고 재배열할 수 있습니다. 자세한 정보는 [대시보드를 통해 Kibana에서 로그 분석](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#analize_logs_dashboard)을 참조하십시오.
    
Kibana 대시보드를 사용자 정의한 후에 해당 시각화를 통해 데이터를 분석하고 나중에 다시 사용할 수 있도록 저장할 수 있습니다. 자세한 정보는 [Kibana 대시보드 저장](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save)을 참조하십시오.

## Kibana 사용자 정의
{: #analyze_management}

**관리** 페이지에서 Kibana 리소스를 구성하고 관리할 수도 있습니다. 

다음 태스크를 완료할 수 있습니다.

* 검색 저장, 삭제, 내보내기 및 가져오기. 
* 시각화 저장, 삭제, 내보내기 및 가져오기.
* 대시보드 저장, 삭제, 내보내기 및 가져오기.
* [필드 목록 새로 고치기.](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)

## 제한사항
{: #limitations}

Kibana에서는 시각화 또는 대시보드를 동일한 조직이나 계정의 멤버와만 공유할 수 있습니다.

다음 Kibana 기능은 지원되지 않습니다.

* 검색 공유.
* 새 인덱스 패턴 작성. 


## 로그 보기를 위해 사용자에게 필요한 역할
{: #roles}

{{site.data.keyword.Bluemix_notm}}에서 사용자에게 하나 이상의 역할을 지정할 수 있습니다. 이러한 역할은 사용자가 {{site.data.keyword.loganalysisshort}} 서비스를 사용하여 수행할 수 있는 태스크를 정의합니다. 

다음 표는 로그를 보기 위해 사용자에게 필요한 역할을 나열합니다.

<table>
  <caption>로그 보기를 위해 **계정 소유자**에게 필요한 권한</caption>
  <tr>
    <th>조치</th>
	<th>CF 영역 역할</th>
	<th>CF 조직 역할</th>
	<th>IAM 역할</th>
  </tr>
  <tr>
    <td>영역 도메인의 로그 보기</td>
	<td>*관리자* </br>*개발자* </br>*감사자*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>계정 도메인의 로그 보기</td>
	<td></td>
	<td></td>
	<td>*관리자*</td>
  </tr>
  <tr>
    <td>조직 도메인의 로그 보기</td>
	<td></td>
	<td>*관리자* </br>*청구 관리자*  </br>*감사자*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>로그 보기를 위해 **감사자**에게 필요한 권한</caption>
  <tr>
    <th>조치</th>
	<th>CF 영역 역할</th>
	<th>CF 조직 역할</th>
	<th>IAM 역할</th>
  </tr>
  <tr>
    <td>영역 도메인의 로그 보기</td>
	<td>*감사자*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>계정 도메인의 로그 보기</td>
	<td></td>
	<td></td>
	<td>*뷰어*</td>
  </tr>
  <tr>
    <td>조직 도메인의 로그 보기</td>
	<td></td>
	<td>*감사자*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>로그 보기를 위해 **관리자**에게 필요한 권한</caption>
  <tr>
    <th>조치</th>
	<th>CF 영역 역할</th>
	<th>CF 조직 역할</th>
	<th>IAM 역할</th>
  </tr>
  <tr>
    <td>영역 도메인의 로그 보기</td>
	<td>*개발자*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>계정 도메인의 로그 보기</td>
	<td></td>
	<td></td>
	<td>*뷰어*</td>
  </tr>
  <tr>
    <td>조직 도메인의 로그 보기</td>
	<td></td>
	<td>*관리자*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>로그 보기를 위해 **개발자**에게 필요한 권한</caption>
  <tr>
    <th>조치</th>
	<th>CF 영역 역할</th>
	<th>CF 조직 역할</th>
	<th>IAM 역할</th>
  </tr>
  <tr>
    <td>영역 도메인의 로그 보기</td>
	<td>*개발자*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>계정 도메인의 로그 보기</td>
	<td></td>
	<td></td>
	<td>*뷰어*</td>
  </tr>
  <tr>
    <td>조직 도메인의 로그 보기</td>
	<td></td>
	<td>*감사자*</td>
	<td></td>
  </tr>
</table>



## Kibana를 실행하는 URL
{: #urls_kibana}

다음 표는 Kibana를 실행하는 URL 및 지역별 Kibana 버전을 나열합니다.

<table>
    <caption>Kibana를 실행하는 URL</caption>
    <tr>
      <th>지역</th>
      <th>URL</th>
      <th>Kibana 버전</th>
    </tr>
	<tr>
      <td>프랑크푸르트</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>시드니</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>영국</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
    <tr>
      <td>미국 남부</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
</table>




