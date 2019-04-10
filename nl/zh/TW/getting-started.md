---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

subcollection: LogDNA

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

# 入門指導教學
{: #getting-started}

使用 {{site.data.keyword.la_full}} 將日誌管理功能新增至您的 {{site.data.keyword.cloud_notm}} 架構。{{site.data.keyword.la_full_notm}} 由 LogDNA 所操作，其與 {{site.data.keyword.IBM_notm}} 存在夥伴關係。
{:shortdesc}


## 步驟 1. 開始之前
{: #getting-started_prereqs}

* 閱讀 {{site.data.keyword.la_full_notm}} 的相關資訊。如需相關資訊，請參閱[關於 {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)。
* 檢查可以使用服務的地區。如需相關資訊，請參閱[地區](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions)。
* 取得 {{site.data.keyword.cloud_notm}} 帳戶之成員或擁有者的使用者 ID。 

    若要取得 {{site.data.keyword.cloud_notm}} 使用者 ID，請按一下[登錄 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}。



## 步驟 2. 開始使用
{: #getting-started_step2}

選擇您要管理其日誌的雲端資源。然後，配置這個日誌來源，讓您可以透過 {{site.data.keyword.la_full_notm}} 服務來監視其日誌。日誌來源可以位於您佈建 {{site.data.keyword.la_full_notm}} 實例的相同地區中，或者不同地區中。

下表列出雲端資源的範例，您可以配置為使用 {{site.data.keyword.la_full_notm}} 服務來儲存及管理日誌。請完成資源的指導教學，以開始使用 {{site.data.keyword.loganalysisshort}} 服務：

<table>
  <caption>開始使用 {{site.data.keyword.la_full_notm}} 服務的指導教學</caption>
  <tr>
    <th>資源</th>
    <th>指導教學</th>
    <th>環境</th>
    <th>情境</th>
  </tr>
  <tr>
    <td>在 {{site.data.keyword.containershort}} 上執行的儲存器</td>
    <td>[Managing Kubernetes cluster logs with {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} Public </td>
    <td>![{{site.data.keyword.containershort}} 及 {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} 及 {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu、Linux Debian</td>
    <td>[Managing Linux Ubuntu logs with {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>在內部部署時</td>
    <td>![Ubuntu 伺服器及 {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Ubuntu 伺服器及 {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## 步驟 3. 升級方案
{: #getting-started_step3}

啟用更多記載特性。

將 {{site.data.keyword.la_full_notm}} 服務方案升級至付款方案，以便能夠[過濾日誌](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5)、[搜尋日誌](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)、[定義視圖](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)，以及[配置警示](https://docs.logdna.com/docs/alerts)。如需 {{site.data.keyword.la_full_notm}} 服務方案的相關資訊，請參閱[定價方案](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)。

## 步驟 4. 後續步驟 
{: #getting-started_iam}

接下來，使用 IAM 管理使用者存取權。

識別使用者使用 {{site.data.keyword.la_full_notm}} 服務時所需的 IAM 原則。

若要進一步瞭解 IAM 與 {{site.data.keyword.la_full_notm}} 服務的整合，請參閱[使用 IAM 管理使用者存取權](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam)。

例如，選擇一個使用者角色，以學習如何將許可權授與該使用者來使用 {{site.data.keyword.la_full_notm}} 服務。 

| {{site.data.keyword.cloud_notm}} 中的使用者角色 | 取得相關資訊                     |
|-----------------------------------------------------|------------------------------------------|
| 帳戶擁有者                                       | [將許可權授與使用者以成為 {{site.data.keyword.cloud_notm}} 帳戶中服務的管理者](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| 帳戶中的平台服務管理者       | [將許可權授與使用者以成為 {{site.data.keyword.cloud_notm}} 帳戶中服務的管理者](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| 資源群組中的平台服務管理者  | [將許可權授與使用者以成為資源群組內服務的管理者](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg) |
| 帳戶中的平台 DevOps 操作員           | [將許可權授與 DevOps 使用者以管理 {{site.data.keyword.cloud_notm}} 帳戶中的服務](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account) |
| 資源群組中的平台 DevOps 操作員        | [將許可權授與 DevOps 使用者以管理資源群組內的服務](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg) |
| LogDNA 中的服務管理者                     | [授與許可權以在 LogDNA 中管理日誌及配置警示](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)              |
| 使用者 / 開發人員                                    | [將許可權授與使用者以在 LogDNA 中檢視及管理日誌](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)               |
{: caption="表 2. {{site.data.keyword.cloud_notm}} 中的雲端角色" caption-side="top"}


