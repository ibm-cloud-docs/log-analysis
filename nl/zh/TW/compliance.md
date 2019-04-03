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


# 規範
{: #compliance}

[{{site.data.keyword.Bluemix}} 提供了一個遵照 IBM 的嚴格安全標準而建置的雲端平台及服務。](/docs/security/compliance.html#compliance){{site.data.keyword.loganalysislong}} 服務是針對 {{site.data.keyword.Bluemix_notm}} 而建置的 DevOps Services。
{:shortdesc}


## 一般資料保護規範

「一般資料保護規範 (GDPR)」嘗試建立跨歐盟的協調資料保護法律架構，而且目的是將居民的個人資料控制權還給居民，同時對於在全球任何位置管理及「處理」此資料的人員強制施行嚴格的規則。此「規範」也會建立與在歐盟內外部自由移動個人資料有關的規則。 

**免責聲明：**{{site.data.keyword.loganalysisshort}} 服務會儲存及顯示在 {{site.data.keyword.Bluemix_notm}} 中在您的帳戶中執行的雲端資源中的日誌記錄，以及您在 {{site.data.keyword.Bluemix_notm}} 外部傳送的日誌中的日誌記錄。「個人資訊 (PI)」不得內含在 {{site.data.keyword.loganalysisshort}} 儲存的任何日誌項目中，因為您企業內的其他使用者能夠存取此資料，而且 {{site.data.keyword.IBM_notm}} 為了能夠支援雲端服務也能存取此資料。

### 地區
{: #regions}

{{site.data.keyword.loganalysisshort}} 服務在提供該服務的「{{site.data.keyword.Bluemix_notm}} 公用」地區中遵循 GDPR。


### 資料保留
{: #data_retention}

{{site.data.keyword.loganalysisshort}} 服務包括可以儲存您資料的 2 個資料儲存庫： 

* 日誌搜尋，用於管理可透過 Kibana 進行分析的日誌資料。
* 日誌收集，用於管理日誌資料以進行長期儲存。

取決於 {{site.data.keyword.loganalysisshort}} 服務方案，資料會儲存在「日誌搜尋」中，或儲存在「日誌搜尋」及「日誌收集」中。標準或精簡方案僅將資料儲存在「日誌搜尋」中。其他方案則會將資料儲存在「日誌搜尋」及「日誌收集」中。

* 儲存在「日誌搜尋」中的日誌會保留 3 天。
* 除非您配置保留原則，或手動予以刪除，否則會保留「日誌收集」中所儲存的日誌。依預設，日誌會無限期地保留在「日誌收集」中。



### 資料刪除
{: #data_deletion}

請考量下列資訊：

* 在 3 天後，即會刪除「日誌搜尋」中所儲存的日誌。

* 儲存在「日誌收集」中的日誌，會在您配置保留原則或手動予以刪除的幾天之後被刪除。 

    您可以配置日誌保留原則，以定義您要將日誌保留在「日誌收集」中的天數。如需相關資訊，請參閱[使用 {{site.data.keyword.Bluemix_notm}} 外掛程式檢視及配置日誌保留原則](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy)。

    您可以使用[日誌收集 API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} 或[日誌收集 CLI](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window}，手動刪除「日誌收集」中的日誌。 

    您可以使用 CLI，手動刪除「日誌收集」中的日誌。如需相關資訊，請參閱[使用 {{site.data.keyword.Bluemix_notm}} 外掛程式來執行 ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs)。


如果您從付費方案變更為標準或精簡方案，則「日誌收集」中的日誌將在大約一天內被刪除。

您隨時都可以開立支援問題單，並要求從「日誌搜尋」及「日誌收集」刪除所有資料。如需開立 IBM 支援問題單的相關資訊，請參閱[與支援中心聯絡](/docs/get-support/howtogetsupport.html#getting-customer-support)。



### 相關資訊 
{: #info}

如需相關資訊，請參閱：

[{{site.data.keyword.Bluemix_notm}} 安全規範](/docs/security/compliance.html#compliance)

[GDPR - {{site.data.keyword.IBM_notm}} 官方頁面](https://www.ibm.com/data-responsibility/gdpr/)



