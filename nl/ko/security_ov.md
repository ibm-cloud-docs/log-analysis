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

# 보안
{: #security_ov}

사용자가 수행할 수 있는 {{site.data.keyword.loganalysisshort}} 조치를 제어하기 위해 사용자에게 하나 이상의 역할을 지정할 수 있습니다. 
{:shortdesc}

{{site.data.keyword.loganalysisshort}} 서비스 API에 대한 작업을 수행하려면 UAA 토큰 또는 IAM 토큰을 사용해야 합니다. 로그를 {{site.data.keyword.loganalysisshort}} 서비스로 보내려면 로깅 토큰이 필요합니다.


## 인증 모델
{: #auth1}

CLI 또는 API를 통해 {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행하려면 인증 토큰이 필요합니다.

{{site.data.keyword.loganalysisshort}} 서비스는 다음 인증 모델을 지원합니다.

* [UAA 인증](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)

    CLI만 사용하여 UAA 토큰을 관리할 수 있습니다.
	
* [IAM 인증](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)

    IAM 인증 모델은 UI, CLI 또는 API 관리 기능을 제공합니다. 

**참고:** UAA 토큰 및 IAM 토큰은 특정 기간 이후에 만료됩니다. 

## 역할
{: #roles3}

{{site.data.keyword.Bluemix_notm}}에는 {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 실행할 때 사용자가 수행할 수 있는 조치를 제어하는 두 가지 역할 유형이 있습니다.

* CF(Cloud Foundry) 역할: 하나 이상의 CF 역할을 지정하여 사용자가 수행할 수 있는 {{site.data.keyword.loganalysisshort}} 조치를 제어합니다. 해당 역할을 사용하여 영역 또는 조직에서 로그를 보고 관리하는 사용자 권한을 제어합니다.
* IAM 역할: 하나 이상의 IAM 역할을 지정하여 사용자가 수행할 수 있는 {{site.data.keyword.loganalysisshort}} 조치를 제어합니다. 해당 역할을 사용하여 계정 로그를 보고 관리하는 사용자 권한을 제어합니다. 


다음 표는 역할 유형 및 역할 유형이 제어하는 {{site.data.keyword.Bluemix_notm}}의 도메인을 나열합니다.

<table>
  <caption>표 1. 도메인별 조치를 제어하는 역할 유형</caption>
  <tr>
    <th></th>
	<th align="right">계정</th>
    <th align="right">조직</th>
    <th align="right">영역</th>	
  </tr>
  <tr>
    <td align="left">CF 역할</td>
	<td align="center">아니오</td>
	<td align="center">예</td>
	<td align="center">예</td>
  </tr>
  <tr>
    <td align="left">IAM 역할</td>
	<td align="center">예</td>
	<td align="center">아니오</td>
	<td align="center">아니오</td>
  </tr>
</table>


## CF 역할
{: #bmx_roles}

다음 표는 {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행하는 각 CF 역할의 권한을 나열합니다.

<table>
  <caption>표 2. {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행하는 Cloud Foundry 역할 및 권한.</caption>
  <tr>
    <th>역할</th>
	<th>도메인</th>
	<th>액세스 권한</th>
  </tr>
  <tr>
    <td>관리자</td>
	<td>조직 <br>영역</td>
	<td>모든 RESTful API</td>
  </tr>
  <tr>
    <td>개발자</td>
	<td>영역</td>
	<td>모든 RESTful API</td>
  </tr>
  <tr>
    <td>감사자</td>
	<td>조직 <br>영역</td>
	<td>로그 조회와 같이 읽기 전용 조작을 수행하는 RESTful API만.</td>
  </tr>
</table>


## IAM 역할
{: #iam_roles}

다음 표는 {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행하는 각 IAM 역할의 권한을 나열합니다.

<table>
  <caption>표 3. {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행하는 IAM 역할 및 권한.</caption>
  <tr>
    <th>역할</th>
	<th>권한</th>
  </tr>
  <tr>
    <td>관리자</td>
	  <td>영역 또는 계정 레벨의 로그에 대한 정보를 봅니다. <br>로그를 로컬 파일에 다운로드하거나 로그를 Elastic Stack과 같은 다른 프로그램에 파이프합니다. <br>영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 표시합니다. <br>영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 업데이트합니다. <br>활성 세션 및 해당 ID를 나열합니다. <br>로그를 다운로드하는 데 사용할 수 있는 세션을 작성합니다. <br>세션 ID로 지정된 세션을 삭제합니다. <br>단일 세션의 상태를 표시합니다. <br>로그를 삭제합니다. </td>
  </tr>
  <tr>
    <td>편집자</td>
	  <td>영역 또는 계정 레벨의 로그에 대한 정보를 봅니다. <br>로그를 로컬 파일에 다운로드하거나 로그를 Elastic Stack과 같은 다른 프로그램에 파이프합니다. <br>영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 표시합니다. <br>영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 업데이트합니다. <br>활성 세션 및 해당 ID를 나열합니다. <br>로그를 다운로드하는 데 사용할 수 있는 세션을 작성합니다. <br>세션 ID로 지정된 세션을 삭제합니다. <br>단일 세션의 상태를 표시합니다. <br>로그를 삭제합니다.  </td>
  </tr>
  <tr>
    <td>운영자</td>
	  <td>영역 또는 계정 레벨의 로그에 대한 정보를 봅니다. <br>영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 표시합니다. <br>활성 세션 및 해당 ID를 나열합니다. <br>단일 세션의 상태를 표시합니다. <br>로그를 로컬 파일에 다운로드하거나 로그를 Elastic Stack과 같은 다른 프로그램에 파이프합니다.  <br>로그를 다운로드하는 데 사용할 수 있는 세션을 작성합니다. <br>세션 ID로 지정된 세션을 삭제합니다. </td>
  </tr>
  <tr>
    <td>뷰어</td>
	  <td>영역 또는 계정 레벨의 로그에 대한 정보를 봅니다. <br>영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 표시합니다. <br>활성 세션 및 해당 ID를 나열합니다. <br>단일 세션의 상태를 표시합니다. </td>
  </tr>
</table>

다음 표는 API 간 관계, 서비스 조치 및 {{site.data.keyword.loganalysisshort}} 서비스에서 사용하는 IAM 역할을 나열합니다.

<table>
  <caption>표 4. API 간 관계, 서비스 조치 및 IAM 역할. </caption>
  <tr>
    <th>API</th>
	<th>조치</th>
	<th>IAM 역할</th>
	<th>설명</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>관리자, 편집자</td>
	<td>로그를 삭제합니다.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>관리자, 편집자, 뷰어</td>
	<td>{{site.data.keyword.Bluemix_notm}} 영역 또는 계정 레벨의 로그에 대한 정보를 봅니다.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>관리자, 편집자</td>
	<td>로그를 로컬 파일에 다운로드하거나 로그를 Elastic Stack과 같은 다른 프로그램에 파이프합니다.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>관리자, 편집자, 뷰어</td>
    <td>{{site.data.keyword.Bluemix_notm}} 영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 표시합니다.</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>관리자, 편집자</td>
    <td>{{site.data.keyword.Bluemix_notm}} 영역 또는 계정에서 사용할 수 있는 로그의 보존 기간을 업데이트합니다.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>관리자, 편집자, 뷰어</td>
    <td>활성 세션 및 해당 ID를 나열합니다.</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>관리자, 편집자</td>
    <td>로그를 다운로드하는 데 사용할 수 있는 세션을 작성합니다.</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>관리자, 편집자</td>
    <td>세션 ID로 지정된 세션을 삭제합니다.</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>관리자, 편집자, 뷰어</td>
    <td>단일 세션의 상태를 표시합니다.</td>
  </tr>
</table>

## API를 사용하여 로그를 관리하는 인증 토큰 가져오기
{: #get_token}

{{site.data.keyword.loganalysisshort}} API를 사용하여 로그를 관리하려면 인증 토큰을 사용해야 합니다. 

**영역 도메인에서 사용할 수 있는 로그에 대한 작업**

* {{site.data.keyword.loganalysisshort}} CLI를 사용하여 UAA 토큰을 가져오십시오. 
* 토큰에는 만료 시간이 있습니다. 

자세한 정보는 [UAA 토큰 가져오기](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)를 참조하십시오.

**계정 도메인에서 사용할 수 있는 로그에 대한 작업**

* {{{site.data.keyword.Bluemix_notm}} CLI를 사용하여 IAM 토큰을 가져오십시오. 
* 토큰에는 만료 시간이 있습니다. 

자세한 정보는 [IAM 토큰 가져오기](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)를 참조하십시오.


## Log Analysis를 사용하여 로그를 보내는 로깅 토큰 가져오기
{: #get_logging_token}

로그를 {{site.data.keyword.loganalysisshort}} 서비스로 보내려면 로깅 토큰이 필요합니다. 

로그를 영역 도메인으로 보내려면 다음 방법 중 하나를 선택하십시오.

* [{{site.data.keyword.Bluemix_notm}} 명령 ibmcloud service를 사용하여 로그를 영역으로 보내는 데 필요한 로깅 토큰 가져오기](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_cloud_cli)
* [Log Analysis CLI를 사용하여 로그를 영역으로 보내는 로깅 토큰 가져오기](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_la_cloud_cli)
* [Log Analysis API를 사용하여 로그를 영역으로 보내는 로깅 토큰 가져오기](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_api)


## 사용자에게 로그에 대한 작업을 수행하기 위한 권한 부여
{: #grant_permissions1}

사용자가 로그를 관리하거나 볼 수 있도록 하려면 {{site.data.keyword.Bluemix_notm}}에서 {{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행하기 위한 권한을 사용자에게 부여해야 합니다.

* 로그 관리에 필요한 권한에 대한 정보는 [로그 관리를 위해 사용자에게 필요한 역할](/docs/services/CloudLogAnalysis/manage_logs.html#roles1)을 참조하십시오.
* 로그 보기에 필요한 권한에 대한 정보는 [로그 보기를 위해 사용자에게 필요한 역할](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#roles)을 참조하십시오.

권한 부여 방법에 대한 자세한 정보는 다음을 참조하십시오.

* [{{site.data.keyword.Bluemix_notm}} UI를 통해 사용자에게 IAM 정책 지정](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions).
* [명령행을 사용하여 사용자에게 IAM 정책 지정](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_commandline).
* [{{site.data.keyword.Bluemix_notm}} UI를 사용하여 사용자에게 영역 로그를 볼 수 있는 권한 부여](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space).


