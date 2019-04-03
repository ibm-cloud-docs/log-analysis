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


# Kibana 대시보드로 이동
{: #k4_launch}

{{site.data.keyword.Bluemix}} UI에서 또는 웹 브라우저에서 직접 Kibana를 실행할 수 있습니다.
{:shortdesc}

Kibana를 실행하는 원본 리소스의 컨텍스트에서 데이터를 보고 분석하려면 {{site.data.keyword.Bluemix_notm}}에서 Kibana를 실행하십시오. 예를 들면, 해당 특정 앱의 맥락에서 Kibana에서 사용자의 특정 CF 앱 로그에 실행할 수 있습니다.

다음 표는 리소스 및 Kibana를 실행하기 위해 지원되는 탐색 방법을 나열합니다.

<table>
<caption>표 1. 리소스의 목록 및 지원되는 탐색 방법. </caption>
  <tr>
    <th>리소스</th>
    <th>Bluemix 대시보드에서 Kibana 대시보드로 이동</th>
    <th>웹 브라우저에서 Kibana 대시보드로 이동</th>
  <tr>
  <tr>
    <td>CF 앱</td>
    <td>예</td>
    <td>예</td>
  <tr>  
  <tr>
    <td>Kubernetes 클러스터에 배치된 컨테이너</td>
    <td>예</td>
    <td>예</td>
  <tr>  
</table>

Kibana에 대한 자세한 정보는 [Kibana User Guide ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](https://www.elastic.co/guide/en/kibana/4.1/index.html){: new_window}를 참조하십시오.
    

##  Bluemix 대시보드에서 Kibana 대시보드로 이동
{: #launch_Kibana_from_bluemix}

Kibana에 표시되는 데이터 필터링에 사용되는 조회는 Kibana를 실행하는 {{site.data.keyword.Bluemix_notm}} CF 앱 또는 컨테이너에 대한 로그 항목을 검색합니다.

Kibana에서 Cloud Foundry 애플리케이션 또는 Docker 컨테이너의 로그를 보려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}에 로그인한 후에 {{site.data.keyword.Bluemix_notm}} 대시보드에서 앱 이름 또는 컨테이너를 클릭하십시오. 
    
2. {{site.data.keyword.Bluemix_notm}} UI에서 로그 탭을 여십시오.

    * CF 앱의 경우, 탐색줄에서 **로그**를 클릭하십시오. 
    * {{site.data.keyword.Bluemix_notm}} 관리 인프라에 배치된 컨테이너의 경우, 탐색줄에서 **모니터링 및 로그**를 선택한 후에 **로깅** 탭을 클릭하십시오. 
    
        로그 탭이 열립니다.  

3. **고급 보기**를 클릭하십시오. Kibana 대시보드가 열립니다.

    기본적으로 **검색** 페이지는 기본 인덱스 패턴이 선택되고 시간 필터가 최근 30초로 설정되어 로드됩니다. 검색 조회는 CF 앱 또는 Docker 컨테이너의 모든 항목과 일치하도록 설정됩니다.

    검색 페이지에 로그 항목이 표시되지 않는 경우, 시간 선택도구를 조정하십시오. 


##  웹 브라우저에서 Kibana 대시보드로 이동
{: #launch_Kibana_from_browser1}

Kibana에 표시되는 데이터 필터링에 사용되는 조회는 {{site.data.keyword.Bluemix_notm}} 조직에서 영역에 대한 로그 항목을 검색합니다. Kibana가 표시하는 로그 정보에는 사용자가 로그인한 {{site.data.keyword.Bluemix_notm}} 조직의 영역 내에 배치된 모든 리소스에 대한 레코드가 포함되어 있습니다.

브라우저에서 Kibana를 실행하려면 다음 단계를 완료하십시오.

1. Kibana 사용자 인터페이스를 실행하십시오.
    
    예: 
      
        <table>
          <caption>표 1. Kibana를 실행하는 URL  </caption>
           <tr>
            <th>지역</th>
            <th>URL</th>
          </tr>
          <tr>
            <td>미국 남부</td>
            <td>https://logging.ng.bluemix.net/ </td>
          </tr>
          <tr>
            <td>영국</td>
            <td>https://logging.eu-gb.bluemix.net/ </td>
          </tr>
        </table>

    검색 페이지에 로그 항목이 표시되지 않는 경우, 시간 선택도구를 조정하십시오. 

