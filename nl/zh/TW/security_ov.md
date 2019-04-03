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

# 安全
{: #security_ov}

若要控制容許使用者執行的 {{site.data.keyword.loganalysisshort}} 動作，您可以將一個以上的角色指派給使用者。
{:shortdesc}

若要使用 {{site.data.keyword.loganalysisshort}} 服務 API，您需要使用 UAA 記號或 IAM 記號。若要將日誌傳送至 {{site.data.keyword.loganalysisshort}} 服務，您需要記載記號。


## 鑑別模型
{: #auth1}

若要透過 CLI 或 API 使用 {{site.data.keyword.loganalysisshort}} 服務，您需要鑑別記號。

{{site.data.keyword.loganalysisshort}} 服務支援下列鑑別模型：

* [UAA 鑑別](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)

    您只能使用 CLI 來管理 UAA 記號。
	
* [IAM 鑑別](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)

    IAM 鑑別模型提供使用者介面、CLI 或 API 管理功能。 

**附註：**UAA 記號及 IAM 記號會在一段時間後過期。 

## 角色
{: #roles3}

{{site.data.keyword.Bluemix_notm}} 中有兩種類型的角色可控制使用者在使用 {{site.data.keyword.loganalysisshort}} 服務時可執行的動作：

* Cloud Foundry (CF) 角色：您可以指派一個以上的 CF 角色，來控制使用者可執行的 {{site.data.keyword.loganalysisshort}} 動作。使用這些角色，您可以控制使用者檢視及管理空間或組織中日誌的許可權。
* IAM 角色：您可以指派一個以上的 IAM 角色，來控制使用者可執行的 {{site.data.keyword.loganalysisshort}} 動作。使用這些角色，您可以控制使用者檢視及管理帳戶日誌的許可權。 


下表列出角色類型以及 {{site.data.keyword.Bluemix_notm}} 中角色可控制的網域：

<table>
  <caption>表 1. 控制每個網域動作的角色類型</caption>
  <tr>
    <th></th>
	<th align="right">帳戶</th>
    <th align="right">組織</th>
    <th align="right">空間</th>	
  </tr>
  <tr>
    <td align="left">CF 角色</td>
	<td align="center">否</td>
	<td align="center">是</td>
	<td align="center">是</td>
  </tr>
  <tr>
    <td align="left">IAM 角色</td>
	<td align="center">是</td>
	<td align="center">否</td>
	<td align="center">否</td>
  </tr>
</table>


## CF 角色
{: #bmx_roles}

下表列出每一個 CF 角色使用 {{site.data.keyword.loganalysisshort}} 服務的專用權：

<table>
  <caption>表 2. 使用 {{site.data.keyword.loganalysisshort}} 服務的 Cloud Foundry 角色及專用權。</caption>
  <tr>
    <th>角色</th>
	<th>網域</th>
	<th>存取權</th>
  </tr>
  <tr>
    <td>管理員</td>
	<td>組織<br>空間</td>
	<td>所有 RESTful API</td>
  </tr>
  <tr>
    <td>開發人員</td>
	<td>空間</td>
	<td>所有 RESTful API</td>
  </tr>
  <tr>
    <td>審核員</td>
	<td>組織<br>空間</td>
	<td>僅限執行唯讀作業（例如查詢日誌）的 RESTful API。</td>
  </tr>
</table>


## IAM 角色
{: #iam_roles}

下表列出每一個 IAM 角色使用 {{site.data.keyword.loganalysisshort}} 服務的專用權：

<table>
  <caption>表 3. 使用 {{site.data.keyword.loganalysisshort}} 服務的 IAM 角色及專用權。</caption>
  <tr>
    <th>角色</th>
	<th>專用權</th>
  </tr>
  <tr>
    <td>管理者</td>
	  <td>檢視空間中或帳戶層次之日誌的相關資訊。<br>將日誌下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。<br>顯示空間或帳戶中可用日誌的保留期間。<br>更新空間或帳戶中可用日誌的保留期間。<br>列出作用中階段作業及其 ID。<br>建立您可用來下載日誌的階段作業。<br>刪除依階段作業 ID 所指定的階段作業。<br>顯示單一階段作業的狀態。<br>刪除日誌。</td>
  </tr>
  <tr>
    <td>編輯者</td>
	  <td>檢視空間中或帳戶層次之日誌的相關資訊。<br>將日誌下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。<br>顯示空間或帳戶中可用日誌的保留期間。<br>更新空間或帳戶中可用日誌的保留期間。<br>列出作用中階段作業及其 ID。<br>建立您可用來下載日誌的階段作業。<br>刪除依階段作業 ID 所指定的階段作業。<br>顯示單一階段作業的狀態。<br>刪除日誌。</td>
  </tr>
  <tr>
    <td>操作員</td>
	  <td>檢視空間中或帳戶層次之日誌的相關資訊。<br>顯示空間或帳戶中可用日誌的保留期間。<br>列出作用中階段作業及其 ID。<br>顯示單一階段作業的狀態。<br>將日誌下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。<br>建立您可用來下載日誌的階段作業。<br>刪除依階段作業 ID 所指定的階段作業。</td>
  </tr>
  <tr>
    <td>檢視者</td>
	  <td>檢視空間中或帳戶層次之日誌的相關資訊。<br>顯示空間或帳戶中可用日誌的保留期間。<br>列出作用中階段作業及其 ID。<br>顯示單一階段作業的狀態。</td>
  </tr>
</table>

下表列出 API、服務動作與 {{site.data.keyword.loganalysisshort}} 服務所使用的 IAM 角色之間的關係。

<table>
  <caption>表 4. API、服務動作與 IAM 角色之間的關係。</caption>
  <tr>
    <th>API</th>
	<th>動作</th>
	<th>IAM 角色</th>
	<th>說明</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>管理者、編輯者</td>
	<td>刪除日誌。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>管理者、編輯者、檢視者</td>
	<td>檢視 {{site.data.keyword.Bluemix_notm}} 空間中或帳戶層次之日誌的相關資訊。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>管理者、編輯者</td>
	<td>將日誌下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>管理者、編輯者、檢視者</td>
    <td>顯示 {{site.data.keyword.Bluemix_notm}} 空間或帳戶中可用日誌的保留期間。</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>管理者、編輯者</td>
    <td>更新 {{site.data.keyword.Bluemix_notm}} 空間或帳戶中可用日誌的保留期間。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>管理者、編輯者、檢視者</td>
    <td>列出作用中階段作業及其 ID。</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>管理者、編輯者</td>
    <td>建立您可用來下載日誌的階段作業。</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>管理者、編輯者</td>
    <td>刪除依階段作業 ID 所指定的階段作業。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>管理者、編輯者、檢視者</td>
    <td>顯示單一階段作業的狀態。</td>
  </tr>
</table>

## 取得鑑別記號以使用 API 來管理日誌
{: #get_token}

若要使用 {{site.data.keyword.loganalysisshort}} API 來管理日誌，您必須使用鑑別記號。 

**使用空間網域中可用的日誌**

* 使用 {{site.data.keyword.loganalysisshort}} CLI 來取得 UAA 記號。 
* 記號具有有效期限。 

如需相關資訊，請參閱[取得 UAA 記號](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)。

**使用帳戶網域中可用的日誌**

* 使用 {{site.data.keyword.Bluemix_notm}} CLI 來取得 IAM 記號。 
* 記號具有有效期限。 

如需相關資訊，請參閱[取得 IAM 記號](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)。


## 取得記載記號以將日誌傳送至 Log Analysis
{: #get_logging_token}

若要將日誌傳送至 {{site.data.keyword.loganalysisshort}} 服務，您需要記載記號。 

若要將日誌傳送至空間網域，請選擇下列任一方法：

* [取得記載記號，以使用 {{site.data.keyword.Bluemix_notm}} 指令 ibmcloud service 將日誌傳送至空間](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_cloud_cli)
* [取得記載記號，以使用 Log Analysis CLI 將日誌傳送至空間](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_la_cloud_cli)
* [取得記載記號，以使用 Log Analysis API 將日誌傳送至空間](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_api)


## 將日誌使用許可權授與使用者
{: #grant_permissions1}

若要讓使用者可以管理日誌或檢視日誌，必須將在 {{site.data.keyword.Bluemix_notm}} 中使用 {{site.data.keyword.loganalysisshort}} 服務的許可權授與使用者。

* 如需管理日誌所需許可權的相關資訊，請參閱[使用者管理日誌所需的角色](/docs/services/CloudLogAnalysis/manage_logs.html#roles1)。
* 如需檢視日誌所需許可權的相關資訊，請參閱[使用者檢視日誌所需的角色](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#roles)。

如需如何授與許可權的相關資訊，請參閱：

* [透過 {{site.data.keyword.Bluemix_notm}} 使用者介面將 IAM 原則指派給使用者](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions)。
* [使用指令行將 IAM 原則指派給使用者](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_commandline)。
* [使用 {{site.data.keyword.Bluemix_notm}} 使用者介面將檢視空間日誌許可權授與使用者](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space)。


