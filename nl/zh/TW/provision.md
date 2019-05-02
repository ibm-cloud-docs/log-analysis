---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# 佈建實例
{: #provision}

您必須先在 {{site.data.keyword.cloud_notm}} 中佈建服務的實例，才能使用 {{site.data.keyword.la_full_notm}} 來監視及管理日誌資料。
{:shortdesc}

若要在「公用雲端」地區中佈建 {{site.data.keyword.la_full_notm}} 實例，您必須選取與該實例相關聯的服務方案、從中收集日誌的地區，以及決定日誌保留期間的方案。保留期間可以選擇 7、14 或 30 天。

另外，{{site.data.keyword.la_full_notm}} 還提供`精簡`方案，可用來檢視通過系統的日誌。您可以使用日誌追蹤來檢視日誌。您也可以設計過濾器，以準備升級至較長的保留期間方案。此方案的保留期間為 0 天。


## 透過觀察儀表板來佈建實例
{: #provision_ui}

若要從 {{site.data.keyword.cloud_notm}} 的「觀察」儀表板中佈建實例，請完成下列步驟：

1. 登入您的 {{site.data.keyword.cloud_notm}} 帳戶。

    {{site.data.keyword.cloud_notm}} 儀表板位於：[{{site.data.keyword.cloud_notm}} 儀表板 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}。

	使用您的使用者 ID 和密碼登入之後，即會開啟 {{site.data.keyword.cloud_notm}} 使用者介面。

2. 移至功能表圖示 ![功能表圖示](../../icons/icon_hamburger.svg)。然後，選取**觀察**，以存取*觀察* 儀表板。

3. 選取**記載**，然後按一下**建立實例**。 

4. 輸入服務實例的名稱。

5. 選取資源群組。 

    依預設，會設定 **Default** 資源群組。

    **附註：**如果您無法選取資源群組，請檢查您是否具有要在其中佈建實例之資源群組的編輯權限。

6. 選取`精簡`服務方案。 

    依預設，會設定精簡方案。

    如需其他服務方案的相關資訊，請參閱[定價方案](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)。

7. 按一下**建立**。

佈建實例之後，即會開啟*記載* 儀表板。 

接下來，新增 LogDNA 代理程式以配置日誌來源。此代理程式負責收集日誌並將其轉遞至您的實例。 



## 透過型錄來佈建實例
{: #provision_catalog}

若要透過 {{site.data.keyword.cloud_notm}} 型錄來佈建 {{site.data.keyword.la_full_notm}} 的實例，請完成下列步驟：

1. 登入您的 {{site.data.keyword.cloud_notm}} 帳戶。

    按一下 [{{site.data.keyword.cloud_notm}} 儀表板 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}，以啟動 {{site.data.keyword.cloud_notm}} 儀表板。

	使用您的使用者 ID 和密碼登入之後，即會開啟 {{site.data.keyword.cloud_notm}} 使用者介面。

2. 按一下**型錄**。即會開啟 {{site.data.keyword.cloud_notm}} 中可用的服務清單。

3. 若要過濾顯示的服務清單，請選取**開發人員工具**種類。

4. 按一下 **{{site.data.keyword.la_full_notm}}** 磚。 

5. 輸入服務實例的名稱。

6. 選取資源群組。 

    依預設，會設定 **Default** 資源群組。

    **附註：**如果您無法選取資源群組，請檢查您是否具有要在其中佈建實例之資源群組的編輯權限。

7. 選取`精簡`服務方案。 

    依預設，會設定精簡方案。

    如需其他服務方案的相關資訊，請參閱[定價方案](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)。

8. 按一下**建立**。

佈建實例之後，即會開啟*記載* 儀表板。 

接下來，新增 LogDNA 代理程式以配置日誌來源。此代理程式負責收集日誌並將其轉遞至您的實例。 



## 透過 CLI 佈建實例
{: #provision_cli}

若要透過指令行來佈建 {{site.data.keyword.la_full_notm}} 的實例，請完成下列步驟：

1. [必要條件] 安裝 {{site.data.keyword.cloud_notm}} CLI。

   如需相關資訊，請參閱[安裝 {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)。

   如果已安裝 CLI，請繼續進行下一步。

2. 登入 {{site.data.keyword.cloud_notm}} 中要佈建實例的地區。執行下列指令：[`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. 設定您要在其中佈建實例的資源群組。執行下列指令：[`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    依預設，會設定 `default` 資源群組。

4. 建立實例。執行 [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) 指令：

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    其中

    NAME 是實例的名稱

    值 *logdna* 是 {{site.data.keyword.cloud_notm}} 中 {{site.data.keyword.la_full_notm}} 服務的名稱

    SERVICE_PLAN_NAME 是方案的類型。有效值為 *lite*、*7-days*、*14-days*、*30-days*
    
    LOCATION 是建立 LogDNA 實例的地區。有效值為 *us-south*

    例如，若要佈建 7 天保留方案的實例，請執行下列指令：

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}

5. 建立服務金鑰，其具有可操作實例的**管理者**許可權。執行 [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create) 指令：

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    其中

    NAME 是 API 金鑰的名稱。您可以將 API 金鑰命名為 {{site.data.keyword.la_full_notm}} 實例，以協助您稍後識別 API 金鑰。

    ROLE_NAME 是定義已啟用之許可權的角色。有效值為 *editor*、*operator*、*administrator*

    SERVICE_INSTANCE_NAME 是 {{site.data.keyword.cloud_notm}} 中實例的名稱

    例如，若要建立實例 *logdna-instance-01* 的 API 金鑰，其具有服務實例的 *administrator* 許可權，請執行下列指令：

    ```
    ibmcloud resource service-key-create logdna-instance-01 Administrator --instance-name logdna-instance-01
    ```
    {: pre}

    這個指令的輸出包括不同的值，例如，實例的 `crn` 值，以及 LogDNA 汲取金鑰。


