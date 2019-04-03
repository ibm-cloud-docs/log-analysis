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


# {{site.data.keyword.Bluemix_notm}} 외부에서 로그 전송
{: #log_ingestion}

여러 테넌트 Logstash 포워더를 사용하여 로그를 {{site.data.keyword.IBM_notm}} Cloud 외부에서 {{site.data.keyword.loganalysisshort}} 서비스로 보낼 수 있습니다. 
{:shortdesc}

이 기능은 로그를 수집할 수 있는 서비스 플랜에 대해서만 사용할 수 있습니다. 자세한 정보는 [서비스 플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.

로그를 {{site.data.keyword.IBM_notm}} Cloud 외부에서 {{site.data.keyword.loganalysisshort}} 서비스로 보내려면 다음 Clould 리소스가 필요합니다.

* {{site.data.keyword.Bluemix_notm}}에 로그인할 {{site.data.keyword.IBM_notm}} ID. 이 사용자 ID에는 {{site.data.keyword.Bluemix_notm}}의 영역에서 {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행할 수 있는 권한이 있어야 합니다. 영역은 로그를 보내고 분석하려는 {{site.data.keyword.Bluemix_notm}}의 도메인입니다.
* {{site.data.keyword.loganalysisshort}} CLI를 사용하여 생성되고 {{site.data.keyword.loganalysisshort}} 서비스를 사용하여 로컬 환경을 인증하는 데 사용되는 로깅 토큰.  

로컬 환경에서 mt-logstash-forwarder를 구성해야 하며 {{site.data.keyword.loganalysisshort}} 서비스로 보내려는 로그 파일을 지정해야 합니다.

로그를 {{site.data.keyword.loganalysisshort}} 서비스로 보내도록 로컬 환경을 구성하는 방법에 대한 자세한 정보는 [{{site.data.keyword.Bluemix_notm}}의 영역으로 온프레미스 데이터 전송](/docs/services/CloudLogAnalysis/how-to/send-data/send_data_mt.html#send_data_mt)을 참조하십시오.



## 수집 URL
{: #log_ingestion_urls}

다음 표는 로그를 {{site.data.keyword.Bluemix_notm}}로 보내는 데 사용해야 하는 URL을 나열합니다.

<table>
  <caption>수집 URL</caption>
    <tr>
      <th>지역</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>독일</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>시드니</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>영국</td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>미국 남부</td>
	  <td>ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


