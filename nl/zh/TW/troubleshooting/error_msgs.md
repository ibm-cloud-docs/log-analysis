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


# 錯誤訊息
{: #error_msgs}

使用 {{site.data.keyword.Bluemix}} 上的 {{site.data.keyword.loganalysisshort}} 服務時可能會看到這些錯誤訊息：
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**訊息說明**

您已達到配置給 Bluemix 空間、針對 {{site.data.keyword.loganalysisfull}} 實例 {Instance GUID} 的每日配額。您的現行每日配額是日誌搜尋儲存空間 500 MB，這會保留在日誌搜尋儲存空間中 3 天的期間，在此期間內可以在 Kibana 中搜尋它。若要升級您的方案，以便每天能在日誌搜尋儲存空間中儲存更多資料，同時也將所有日誌保留在日誌收集儲存空間中，請升級此空間的 {{site.data.keyword.loganalysisshort}} 服務方案。如需服務方案及如何升級方案的相關資訊，請參閱[方案](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。


**訊息說明** 

當您達到針對精簡服務方案配置的日誌搜尋儲存空間配額時，可能會收到 ID *BXNLG020001W* 的訊息。精簡方案是您在空間佈建 {{site.data.keyword.loganalysisshort}} 服務時，依預設設定的補充服務方案。您的現行每日配額是日誌搜尋儲存空間 500 MB，這會保留在日誌搜尋儲存空間中 3 天的期間，在此期間內可以在 Kibana 中搜尋它。

**回復**

若要升級您的方案，以便每天能在日誌搜尋儲存空間中儲存更多資料，同時也將所有日誌保留在日誌收集儲存空間中，請升級此空間的 {{site.data.keyword.loganalysisshort}} 服務方案。如需服務方案及如何升級方案的相關資訊，請參閱[方案](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。


## BXNLG020002W 
{: #BXNLG020002W}


**訊息說明**

您已達到配置給 Bluemix 空間、針對 {{site.data.keyword.loganalysisfull}} 實例 {Instance GUID} 的每日配額。您的現行每日配額是日誌搜尋儲存空間 XXX，這會保留 3 天的期間，在此期間內可以在 Kibana 中搜尋它。這不會影響日誌收集儲存空間中的日誌保留原則。若要升級您的方案，以便每天能在日誌搜尋儲存空間中儲存更多資料，請升級此空間的 {{site.data.keyword.loganalysisshort}} 服務方案。如需服務方案及如何升級方案的相關資訊，請參閱[方案](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。

XXX 代表您的現行方案的可搜尋資料大小。

**訊息說明** 

您已達到配置給 {{site.data.keyword.loganalysisfull}} 實例 {Instance GUID} 的空間 {Space GUID} 的每日配額。您的現行每日配額是日誌搜尋儲存空間 500 MB、2 GB、5 GB 或 10 GB，這會保留 3 天的期間，在此期間內可以在 Kibana 中搜尋它。這不會影響日誌收集儲存空間中的日誌保留原則。

**回復**

若要升級您的方案，以便每天能在日誌搜尋儲存空間中儲存更多資料，請升級此空間的 {{site.data.keyword.loganalysisshort}} 服務方案。如需服務方案及如何升級方案的相關資訊，請參閱[方案](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)。




