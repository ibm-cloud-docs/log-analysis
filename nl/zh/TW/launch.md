---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# 導覽至 Web 使用者介面
{: #launch}

在 {{site.data.keyword.cloud_notm}} 中佈建 {{site.data.keyword.la_full_notm}} 服務的實例，並為日誌資料來源配置 LogDNA 代理程式之後，即可透過 {{site.data.keyword.la_full_notm}} Web 使用者介面，來檢視、監視及管理日誌。
{:shortdesc}


## 將 IAM 原則授與使用者以檢視資料 
{: #step1}

**附註：**您必須是 {{site.data.keyword.la_full_notm}} 服務的管理者、{{site.data.keyword.la_full_notm}} 實例的管理者，或者具有帳戶 IAM 許可權，才能將原則授與其他使用者。

下表列出使用者必須擁有才能夠啟動 Web 使用者介面及檢視資料的最低原則：

| 服務                              | 角色                      | 授與的許可權       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | 平台角色：檢視者     | 容許使用者檢視「觀察記載」儀表板中的服務實例清單。|
| `{{site.data.keyword.la_full_notm}}` | 服務角色：作者      | 容許使用者啟動 Web 使用者介面，以及在 Web 使用者介面中檢視日誌。|
{: caption="表 1. IAM 原則" caption-side="top"} 

如需如何為使用者配置這些原則的相關資訊，請參閱[將許可權授與使用者以檢視日誌](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)。


## 透過 {{site.data.keyword.cloud_notm}} 使用者介面啟動 Web 使用者介面
{: #launch_step2}

您可以從 {{site.data.keyword.cloud_notm}} 使用者介面，在 {{site.data.keyword.la_full_notm}}實例的環境定義內啟動 Web 使用者介面。 

請完成下列步驟來啟動 Web 使用者介面：

1. 登入您的 {{site.data.keyword.cloud_notm}} 帳戶。

    按一下 [{{site.data.keyword.cloud_notm}} 儀表板 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}，以啟動 {{site.data.keyword.cloud_notm}} 儀表板。

	使用您的使用者 ID 和密碼登入之後，即會開啟 {{site.data.keyword.cloud_notm}} 儀表板。

2. 在導覽功能表中，選取**觀察**。 

3. 選取**記載**。 

    即會顯示 {{site.data.keyword.cloud_notm}} 上可用的實例清單。

4. 選取一個實例。然後，按一下**檢視 LogDNA**。

即會開啟 Web 使用者介面。


## 從 {{site.data.keyword.cloud_notm}} 取得 Web 使用者介面 URL
{: #launch_get}

若要取得 Web 使用者介面 URL，請從終端機完成下列步驟：

1. 設定在其中佈建 {{site.data.keyword.la_full_notm}} 實例的資源群組。

    ```
    export logdna_rg_name=<Resource_Group_Name_Where_LogDNA_Instance_Is_Created>
    ```
    {: codeblock}

2. 設定 {{site.data.keyword.la_full_notm}} 實例名稱。

    ```
    export logdna_instance_name=<Your_LogDNA_Instance_Name>
    ```
    {: codeblock}

3. 設定端點。

    ```
    export rc_endpoint=resource-controller.cloud.ibm.com
    ```
    {: codeblock}

4. 設定 IAM 記號。

    ```
    export iam_token=$(ibmcloud iam oauth-tokens | grep IAM | grep -oP  "eyJ.*")
    ```
    {: codeblock}

    **附註：**如果您在 MacOS 終端機上作業，則指令如下所示：`export iam_token=$(ic iam oauth-tokens | grep IAM | grep -o  "eyJ.*")`

5. 設定資源群組 ID。

    ```
    export resource_group_id=$(ibmcloud resource groups | grep "^$logdna_rg_name" | awk '{print $2}')
    ```
    {: codeblock}

6. 在變數中設定 Web 使用者介面 URL。

    ```
    export dashboard_url=$(curl -H "Accept: application/json" -H "Authorization: Bearer $iam_token" "https://$rc_endpoint/v1/resource_instances?resource_group_id=$resource_group_id&type=service_instance" | jq ".resources[] | select(.name==\"$logdna_instance_name\") | .dashboard_url")
    ```
    {: codeblock}

7. 取得 Web 使用者介面 URL。

    ```
    echo $dashboard_url
    ```
    {: codeblock}

    

