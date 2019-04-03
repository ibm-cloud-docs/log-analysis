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


# 로그 관리
{: #manage_logs}

{{site.data.keyword.loganalysisshort}} CLI 및 {{site.data.keyword.loganalysisshort}} API를 사용하여 로그 콜렉션에 저장된 로그를 관리할 수 있습니다.
{:shortdesc}

로그를 관리하려면 다음 정보를 고려하십시오.

1. 사용자 ID에는 {{site.data.keyword.cloud_notm}}에서 로그 관리를 위한 권한이 있는 {{site.data.keyword.loganalysisshort}}에 대한 정책이 지정되어 있어야 합니다. 

    IAM 역할 및 역할별 태스크 목록은 [IAM 역할](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles)을 참조하십시오. 
	
	정책 지정 방법에 대한 자세한 정보는 [{{site.data.keyword.cloud_notm}} UI를 통해 사용자에게 IAM 정책 지정](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account)을 참조하십시오.
	
2. 이 기능은 로그를 보존할 수 있는 서비스 플랜에 대해서만 사용할 수 있습니다. 

    서비스 플랜에 대한 자세한 정보는 [서비스 플랜](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)을 참조하십시오.

{{site.data.keyword.loganalysisshort}} 서비스는 로그를 관리하는 데 사용할 수 있는 2개의 CLI를 제공합니다.

* {{site.data.keyword.loganalysisshort}} {{site.data.keyword.cloud_notm}} 플러그인. 이 CLI에 대한 자세한 정보는 [{{site.data.keyword.loganalysisshort}} CLI({{site.data.keyword.cloud_notm}} 플러그인)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli)를 참조하십시오.
* {{site.data.keyword.loganalysisshort}} CF 플러그인(더 이상 사용되지 않음). 이 CLI에 대한 자세한 정보는 [Log Analysis CLI(CF 플러그인) 구성](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#logging_cli)을 참조하십시오.


## 로그 보존 정책 구성
{: #log_retention_policy}

{{site.data.keyword.loganalysisshort}} CLI를 사용하여 로그 보존 정책을 보고 구성할 수 있습니다. 이 정책은 로그 콜렉션에 로그가 보존되는 일 수를 지정합니다. 

* 기본적으로 유료 플랜을 선택하면 로그가 수집되어 로그 콜렉션에 보존됩니다. 
* 보존 기간을 설정하면 보존 기간이 만료된 후에 로그는 로그 콜렉션에서 자동으로 삭제되며 복구될 수 없습니다.
* 계정에 대한 보존 기간을 지정할 수 있습니다. 그 계정의 모든 영역에 대해 보존 기간이 자동으로 구성됩니다. 
* 영역에 대한 보존 기간을 지정할 수 있습니다.
* 보존 기간을 언제든지 변경할 수 있습니다.
* 정책의 값을 *-1*로 설정하여 사용 안함으로 설정할 수 있습니다. 

**참고:** 로그 보존 정책을 사용 안함으로 설정하면 로그 콜렉션에서 로그를 유지보수해야 합니다. 이전 로그를 삭제하기 위해 CLI 명령 [cf logging delete](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#delete4)를 사용할 수 있습니다.

자세한 정보는 다음을 참조하십시오.

* [CF 플러그인을 사용하여 로그 보존 정책 보기 및 구성](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy).
* [CF 플러그인을 사용하여 로그 보존 정책 보기 및 구성](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy1#configuring_retention_policy).


## 로그 삭제
{: #log_deletion}

로그 검색에 저장된 로그는 3일 이후에 삭제됩니다.

로그 콜렉션에 저장된 로그는 보존 정책을 구성하거나 해당 로그를 수동으로 삭제할 때까지 보관됩니다. 

* 로그 콜렉션에 로그를 보존하기 원하는 일 수를 정의하기 위한 로그 보존 정책을 구성할 수 있습니다. 자세한 정보는 [{{site.data.keyword.cloud_notm}} 플러그인을 사용하여 로그 보존 정책 보기 및 구성](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy)을 참조하십시오.

* [로그 콜렉션 API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} 또는 [로그 콜렉션 CLI](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window}를 사용하여 로그 콜렉션에서 로그를 수동으로 삭제할 수 있습니다. 

* CLI를 사용할 수 있습니다. CLI를 통해 수동으로 로그를 삭제하는 데 대한 자세한 정보는 [{{site.data.keyword.Bluemix_notm}} 플러그인을 사용한 ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs)를 참조하십시오.
    


## 로그 다운로드
{: #download_logs2}

Kibana에서 최근 3일 동안의 로그를 검색할 수 있습니다. 더 이전의 로그 데이터를 분석할 수 있도록 로그를 로컬 파일에 다운로드하거나 로컬 Elastic Stack과 같은 다른 프로그램에 해당 로그를 보낼 수 있습니다. 

자세한 정보는 다음을 참조하십시오.

* [{{site.data.keyword.cloud_notm}} 플러그인을 사용하여 로그 다운로드](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs#downloading_logs).
* [CF 플러그인을 사용하여 로그 다운로드](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs1#downloading_logs1).



## 사용자 로그에 대한 정보 가져오기
{: #info_about_logs}

사용자의 로그에 대한 일반 정보를 얻으려면 `ibmcloud logging log-show` 또는 `cf logging status` 명령을 사용하십시오. 자세한 정보는 다음을 참조하십시오.

* [{{site.data.keyword.cloud_notm}} 플러그인을 사용하여 로그 정보 보기](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status1#viewing_log_status1)
* [CF 플러그인을 사용하여 로그 정보 보기](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status#viewing_log_status1).

예를 들어 비용을 계속 제어하기 위해 일정 기간 동안의 앱의 로그 크기를 모니터하고자 할 수 있습니다. 예를 들면, 앱 또는 서비스가 예상보다 더 많은 로그를 생성하고 있는지 식별하기 위해 {{site.data.keyword.cloud_notm}} 영역에 대해 1주일 동안의 각 로그 유형의 크기를 알려고 할 수 있습니다. 로그 크기를 확인하려면 `ibmcloud logging log-show` 또는 `cf logging status` 명령을 사용하십시오.

영역 도메인, 조직 도메인 또는 계정 도메인에 저장되는 로그에 대한 정보를 볼 수 있습니다.



## {{site.data.keyword.loganalysisshort_notm}} CLI 설치({{site.data.keyword.cloud_notm}} 플러그인)
{: #install_cli2}

CLI 설치 방법을 학습하려면 [로깅 CLI 설치](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli)를 참조하십시오.

CLI 버전을 확인하려면 `ibmcloud plugin list` 명령을 실행하십시오.

명령 실행 방법에 대한 도움말을 보려면 [명령 실행을 위한 명령행 도움말 가져오기](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#command_cli_help)를 참조하십시오.


## 로깅 엔드포인트
{: #endpoints}

다음 표는 지역별 로깅 URL을 나열합니다.

<table>
    <caption>지역별 엔드포인트</caption>
    <tr>
      <th>지역</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>프랑크푸르트</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>시드니</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td>영국</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>미국 남부</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## 로그 관리를 위해 사용자에게 필요한 역할
{: #roles1}

{{site.data.keyword.cloud_notm}}에서 사용자에게 하나 이상의 역할을 지정할 수 있습니다. 이러한 역할은 사용자가 {{site.data.keyword.loganalysisshort}} 서비스를 사용하여 수행할 수 있는 태스크를 정의합니다. 

다음 표는 로그를 관리하기 위해 사용자에게 필요한 역할을 나열합니다.

<table>
  <caption>로그 관리를 위해 **계정 소유자**에게 필요한 권한</caption>
  <tr>
	<th>IAM 역할</th>
	<th>조치</th>
  </tr>
  <tr>
    <td>*관리자*</td>
    <td>로그 상태 확인 </br>로그 다운로드 </br>로그 삭제 </br>로그 보존 정책 변경 </br>세션 관리 </td>
</table>

<table>
  <caption>로그 관리를 위해 **감사자**에게 필요한 권한</caption>
  <tr>
	<th>IAM 역할</th>
	<th>조치</th>
  </tr>
  <tr>
    <td>*뷰어*</td>
    <td>로그 콜렉션에 있는 로그에 대한 정보를 가져옵니다. </br>구성되는 로그 보존 정책에 대한 정보를 가져옵니다. </td>
</table>

<table>
  <caption>로그 관리를 위해 **관리자**에게 필요한 권한</caption>
  <tr>
	<th>IAM 역할</th>
	<th>조치</th>
  </tr>
  <tr>
    <td>*관리자*</td>
    <td>로그 상태 확인 </br>로그 다운로드 </br>로그 삭제 </br>로그 보존 정책 변경 </br>세션 관리 </td>
</table>

<table>
  <caption>로그 관리를 위해 **개발자**에게 필요한 권한</caption>
  <tr>
	<th>IAM 역할</th>
	<th>조치</th>
  </tr>
  <tr>
    <td>*편집자*</td>
    <td>로그 상태 확인 </br>로그 다운로드 </br>로그 삭제 </br>로그 보존 정책 변경 </br>세션 관리</td>
</table>

