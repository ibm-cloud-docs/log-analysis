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


# 管理日誌
{: #manage_logs}

您可以使用 {{site.data.keyword.loganalysisshort}} CLI 及 {{site.data.keyword.loganalysisshort}} API 來管理「日誌收集」中所儲存的日誌。
{:shortdesc}

若要管理日誌，請考量下列資訊：

1. 使用者 ID 必須已在 {{site.data.keyword.cloud_notm}} 中針對 {{site.data.keyword.loganalysisshort}} 指派原則，並具有管理日誌許可權。 

    如需 IAM 角色及每個角色之作業的清單，請參閱 [IAM 角色](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles)。 
	
	如需如何指派原則的相關資訊，請參閱[透過 {{site.data.keyword.cloud_notm}} 使用者介面將 IAM 原則指派給使用者](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account)。
	
2. 此特性僅適用於容許日誌保留的服務方案。 

    如需服務方案的相關資訊，請參閱[服務方案](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。

{{site.data.keyword.loganalysisshort}} 服務提供兩個可用來管理日誌的 CLI：

* {{site.data.keyword.loganalysisshort}} {{site.data.keyword.cloud_notm}} 外掛程式。如需 CLI 的相關資訊，請參閱 [{{site.data.keyword.loganalysisshort}} CLI（{{site.data.keyword.cloud_notm}} 外掛程式）](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli)。
* {{site.data.keyword.loganalysisshort}} CF 外掛程式（已淘汰）。如需 CLI 的相關資訊，請參閱[配置 Log Analysis CLI（CF 外掛程式）](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#logging_cli)。


## 配置日誌保留原則
{: #log_retention_policy}

您可以使用 {{site.data.keyword.loganalysisshort}} CLI 來檢視及配置日誌保留原則。此原則指定將日誌保留在「日誌收集」中的天數。 

* 依預設，當您選取付費方案時，會收集日誌，並將其保留在「日誌收集」中。 
* 當您設定保留期間時，保留期間到期之後，會自動刪除「日誌收集」中的日誌，而且無法進行回復。
* 您可以指定帳戶的保留期間。會自動配置該帳戶中所有空間的保留期間。 
* 您可以指定空間的保留期間。
* 您隨時都可以變更保留原則。
* 停用此原則的方式是將其值設為 *-1*。 

**附註：**當您停用日誌保留原則時，必須在「日誌收集」中維護日誌。您可以使用 CLI 指令 [cf logging delete](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#delete4) 來刪除舊日誌。

如需相關資訊，請參閱：

* [使用 {{site.data.keyword.cloud_notm}} 外掛程式檢視及配置日誌保留原則](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy)。
* [使用 CF 外掛程式檢視及配置日誌保留原則](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy1#configuring_retention_policy)。


## 刪除日誌
{: #log_deletion}

在 3 天後，即會刪除「日誌搜尋」中所儲存的日誌。

除非您配置保留原則，或手動予以刪除，否則會保留「日誌收集」中所儲存的日誌。 

* 您可以配置日誌保留原則，以定義您要將日誌保留在「日誌收集」中的天數。如需相關資訊，請參閱[使用 {{site.data.keyword.cloud_notm}} 外掛程式檢視及配置日誌保留原則](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy)。

* 您可以使用[日誌收集 API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} 或[日誌收集 CLI](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window}，手動刪除「日誌收集」中的日誌。 

* 您可以使用 CLI。如需透過 CLI 手動刪除日誌的相關資訊，請參閱[使用 {{site.data.keyword.cloud_notm}} 外掛程式來執行 ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs)。
    


## 下載日誌
{: #download_logs2}

您可以在 Kibana 中搜尋過去 3 天的日誌。若要可以分析舊日誌資料，您可以將日誌下載至本端檔案，或透過管道將這些日誌輸入至其他程式（例如本端 Elastic Stack）。 

如需相關資訊，請參閱：

* [使用 {{site.data.keyword.cloud_notm}} 外掛程式下載日誌](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs#downloading_logs)。
* [使用 CF 外掛程式下載日誌](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs1#downloading_logs1)。



## 取得日誌的相關資訊
{: #info_about_logs}

若要取得日誌的一般資訊，請使用 `ibmcloud logging log-show` 或 `cf logging status` 指令。如需相關資訊，請參閱：

* [使用 {{site.data.keyword.cloud_notm}} 外掛程式檢視日誌資訊](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status1#viewing_log_status1)
* [使用 CF 外掛程式檢視日誌資訊](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status#viewing_log_status1)。

例如，若要持續控制成本，您可能要監視一段時間內的應用程式日誌大小。例如，您可能要知道 {{site.data.keyword.cloud_notm}} 空間一週內每一種日誌類型的大小，才能識別是否有任何應用程式或服務所產生的日誌超出預期。若要檢查日誌大小，請使用 `ibmcloud logging log-show` 或 `cf logging status` 指令。

您可以檢視空間網域、組織網域或帳戶網域中所儲存日誌的相關資訊。



## 安裝 {{site.data.keyword.loganalysisshort_notm}} CLI（{{site.data.keyword.cloud_notm}} 外掛程式）
{: #install_cli2}

若要瞭解如何安裝 CLI，請參閱[安裝記載 CLI](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli)。

若要檢查 CLI 版本，請執行指令 `ibmcloud plugin list`。

若要取得如何執行指令的協助，請參閱[取得執行指令的指令行協助](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#command_cli_help)。


## 記載端點
{: #endpoints}

下表列出每個地區的記載 URL：

<table>
    <caption>每個地區的端點</caption>
    <tr>
      <th>地區</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>法蘭克福</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>雪梨</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td>英國</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>美國南部</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## 使用者管理日誌所需的角色
{: #roles1}

在 {{site.data.keyword.cloud_notm}} 中，您可以將一個以上的角色指派給使用者。這些角色定義針對該使用者啟用以使用 {{site.data.keyword.loganalysisshort}} 服務的作業。 

下列各表列出使用者管理日誌必須具備的角色：

<table>
  <caption>**帳戶擁有者**管理日誌所需的許可權</caption>
  <tr>
	<th>IAM 角色</th>
	<th>動作</th>
  </tr>
  <tr>
    <td>*管理者*</td>
    <td>檢查日誌的狀態</br>下載日誌</br>刪除日誌</br>變更日誌保留原則</br>管理階段作業</td>
</table>

<table>
  <caption>**審核員**管理日誌所需的許可權</caption>
  <tr>
	<th>IAM 角色</th>
	<th>動作</th>
  </tr>
  <tr>
    <td>*檢視者*</td>
    <td>取得「日誌收集」中所管理日誌的相關資訊。</br>取得已配置之日誌保留原則的相關資訊。</td>
</table>

<table>
  <caption>**管理者**管理日誌所需的許可權</caption>
  <tr>
	<th>IAM 角色</th>
	<th>動作</th>
  </tr>
  <tr>
    <td>*管理者*</td>
    <td>檢查日誌的狀態</br>下載日誌</br>刪除日誌</br>變更日誌保留原則</br>管理階段作業</td>
</table>

<table>
  <caption>**開發人員**管理日誌所需的許可權。</caption>
  <tr>
	<th>IAM 角色</th>
	<th>動作</th>
  </tr>
  <tr>
    <td>*編輯者*</td>
    <td>檢查日誌的狀態</br>下載日誌</br>刪除日誌</br>變更日誌保留原則</br>管理階段作業</td>
</table>

