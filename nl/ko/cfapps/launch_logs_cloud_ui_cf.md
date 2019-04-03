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

# Cloud Foundry 앱의 로그로 이동
{: #launch_logs_cloud_ui_cf}

{{site.data.keyword.Bluemix}} UI에서 각 Cloud Foundry 앱에 사용 가능한 로그 탭 또는 {{site.data.keyword.loganalysisshort}} 서비스 UI를 통해 로그를 보고 필터링하고 분석할 수 있습니다.
{:shortdesc}

CF 앱 로그를 보려면 다음 정보를 고려하십시오. 

<table>
  <caption>{{site.data.keyword.Bluemix_notm}}의 CF 앱 로그에 대한 정보</caption>
  <tr>
    <th>UI 옵션</th>
    <th>정보</th>
  </tr>
  <tr>
    <td>CF 앱 UI를 통해 사용 가능한 로그 탭 </td>
    <td>분석에 사용할 수 있는 로그에는 최근 24시간 동안의 데이터가 포함되어 있습니다.</td>
  </tr>
  <tr>
    <td>{{site.data.keyword.loganalysisshort}} 대시보드(Kibana)</td>
    <td>분석에 사용할 수 있는 로그에는 최근 3일 동안의 데이터가 포함되어 있습니다. 또한 사용자 정의 기간을 지정할 수도 있습니다.</td>
  </tr>
</table>


## CF 앱 대시보드를 통해 CF 앱 로그로 이동 
{: #cfapp_ui}

Cloud Foundry 앱의 런타임 로그 또는 배치를 보려면 다음 단계를 완료하십시오.

1. 앱 대시보드에서 Cloud Foundry 앱의 이름을 클릭하십시오. 
    
2. 앱 세부사항 페이지에서 **로그**를 클릭하십시오.
    
    **로그** 탭에서 앱의 최신 로그를 보거나 실시간으로 로그를 수행할 수 있습니다. 또한, 컴포넌트별(로그 유형), 앱 인스턴스 ID별, 오류별로 로그를 필터링할 수 있습니다.
    
기본적으로 {{site.data.keyword.Bluemix_notm}} 콘솔에서 분석에 사용할 수 있는 로그에는 최근 24시간 동안의 데이터가 포함되어 있습니다.


## {{site.data.keyword.loganalysisshort}} UI를 통해 CF 앱 로그로 이동 
{: #cfapp_la}

Cloud Foundry 앱의 런타임 로그 또는 배치를 보려면 다음 단계를 완료하십시오.

1. 앱 대시보드에서 Cloud Foundry 앱의 이름을 클릭하십시오. 
    
2. 앱 세부사항 페이지에서 **로그**를 클릭하십시오.
    
3. **Kibana에서 보기**를 클릭하십시오.

기본적으로 분석에 사용할 수 있는 로그에는 최근 15분 동안의 데이터가 포함되어 있습니다.

**팁:** 사용자 정의 기간 동안의 데이터를 분석하려면 [Kibana를 사용한 고급 로그 분석](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#analyzing_logs_Kibana)을 참조하십시오. 


