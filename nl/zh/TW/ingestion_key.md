---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# 使用汲取金鑰
{: #ingestion_key}

汲取金鑰是一個安全金鑰，您必須使用它來配置 LogDNA 代理程式，並順利將日誌轉遞至 {{site.data.keyword.cloud_notm}} 中的 {{site.data.keyword.la_full_notm}} 實例。當您佈建實例時，會自動取得汲取金鑰。或者，您也可以透過建立實例的服務 ID，來取得汲取金鑰。
{:shortdesc}

**附註：** 

* 若要透過 {{site.data.keyword.la_full_notm}} Web 使用者介面來使用汲取金鑰，您必須具有平台角色**檢視者**及服務角色**管理員**對 {{site.data.keyword.la_full_notm}} 服務的 IAM 原則。 
* 若要透過 {{site.data.keyword.cloud_notm}} 使用者介面來使用汲取金鑰，您必須具有平台角色**編輯者**及服務角色**管理員**對 {{site.data.keyword.la_full_notm}} 服務的 IAM 原則。 


## 透過 {{site.data.keyword.cloud_notm}} 使用者介面取得汲取金鑰
{: #ibm_cloud_ui}

若要使用 {{site.data.keyword.cloud_notm}} 使用者介面取得 {{site.data.keyword.la_full_notm}} 實例的汲取金鑰，請完成下列步驟：

1. 登入您的 {{site.data.keyword.cloud_notm}} 帳戶。

    按一下 [{{site.data.keyword.cloud_notm}} 儀表板 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}，以啟動 {{site.data.keyword.cloud_notm}} 儀表板。

	使用您的使用者 ID 和密碼登入之後，即會開啟 {{site.data.keyword.cloud_notm}} 使用者介面。

2. 在導覽功能表中，選取**觀察**。 

3. 選取**記載**。即會開啟 {{site.data.keyword.la_full_notm}} 儀表板。您可以看到 {{site.data.keyword.cloud_notm}} 上可用的記載實例清單。

3. 識別您要取得其汲取金鑰的實例，然後按一下**檢視汲取金鑰**。

4. 這時會開啟一個視窗，您可以在其中按一下**顯示**來檢視汲取金鑰。


## 透過 {{site.data.keyword.la_full_notm}} Web 使用者介面取得汲取金鑰
{: #logdna_ui}

若要使用 {{site.data.keyword.la_full_notm}} Web 使用者介面取得 {{site.data.keyword.la_full_notm}} 實例的汲取金鑰，請完成下列步驟：

1. 啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面。如需相關資訊，請參閱[啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 選取**配置**圖示。然後，選取**組織**。 

3. 選取 **API 金鑰**。

您可以看到已建立的汲取金鑰。 

**附註：**一次只會有一個汲取金鑰作用中。 


## 透過 {{site.data.keyword.cloud_notm}} CLI 取得汲取金鑰
{: #ibm_cloud_cli}

若要透過指令行來取得 {{site.data.keyword.la_full_notm}} 實例的汲取金鑰，請完成下列步驟：

1. [必要條件] 安裝 {{site.data.keyword.cloud_notm}} CLI。

   如需相關資訊，請參閱[安裝 {{site.data.keyword.cloud_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)。

   如果已安裝 CLI，請繼續進行下一步。

2. 登入 {{site.data.keyword.cloud_notm}} 中執行實例的地區。執行下列指令：[`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. 設定執行 {{site.data.keyword.la_full_notm}} 實例的資源群組。執行下列指令：[`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)，同時指定選項 `-g`。

    依預設，會設定 `default` 資源群組。

4. 取得與 {{site.data.keyword.la_full_notm}} 實例相關聯之 API 金鑰的名稱。執行 [`ibmcloudresource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) 指令：

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    識別與您實例相關聯的服務金鑰。

5. 取得汲取金鑰。執行 [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) 指令：

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    其中，APIKEY_NAME 是 API 金鑰的名稱
 
    這個指令的輸出包括 **ingestion_key** 欄位，其中包含實例的汲取金鑰。


## 重設汲取金鑰 
{: #reset}

如果汲取金鑰已遭洩露，或者您有原則可以在幾天之後更新該金鑰，則可以產生新的金鑰並刪除舊金鑰。

若要使用 {{site.data.keyword.la_full_notm}} Web 使用者介面更新 {{site.data.keyword.la_full_notm}} 實例的汲取金鑰，請完成下列步驟：

1. 啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面。如需相關資訊，請參閱[啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 選取**配置**圖示。然後，選取**組織**。 

3. 選取 **API 金鑰**。

    您可以看到已建立的汲取金鑰。 

4. 選取**產生汲取金鑰**。

    這時會在清單中新增一個新的金鑰。

5. 刪除舊的汲取金鑰。按一下**刪除**。

**附註：**重設汲取金鑰之後，對於已配置為將日誌轉遞至此 {{site.data.keyword.la_full_notm}} 實例的任何日誌來源，您必須更新其汲取金鑰。



