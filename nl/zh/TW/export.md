---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# 將日誌匯出至本端檔案
{: #export}

您可以將 JSONL 格式的日誌資料，從 {{site.data.keyword.la_full_notm}} 實例匯出至本端檔案。您可以透過程式設計方式，或從 IBM Log Analysis Web 使用者介面匯出日誌。
{:shortdesc}

匯出日誌資料時，請考量下列資訊：
* 您匯出一組日誌項目。若要定義您要匯出的資料集，您可以套用過濾器及搜尋。您也可以指定時間範圍。 
* 從 Web 使用者介面中，當您匯出日誌時，會收到傳送至您電子郵件位址的電子郵件，其中含有一個鏈結，連至包含該資料的壓縮檔。若要取得資料，您必須按一下鏈結，然後下載壓縮檔。
* 以程式設計方式匯出日誌時，您可以選擇傳送電子郵件，或者將日誌串流至您的終端機。
* 包含匯出資料的壓縮日誌檔，可用時間最多 48 小時。 
* 您可以匯出的行數上限是 10,000 行。



## 從 Web 使用者介面匯出日誌
{: #ui}

請完成下列步驟來匯出日誌資料：

1. 按一下**視圖**圖示 ![配置圖示](images/views.png)。
2. 選取**所有項目**或視圖。
3. 套用時間範圍、過濾器及搜尋準則，直到您看到要匯出的日誌項目為止。
4. 如果是從**所有項目**視圖開始，請按一下**未儲存的視圖**。如果您在前一個步驟中選取視圖，請按一下視圖名稱。
5. 選取`匯出行`。即會開啟一個新視窗。
6. 請檢查時間範圍。如果您需要變更，請按一下「變更*匯出的時間範圍*」欄位中的預先定義時間範圍。
7. 如果匯出要求超出了行的限制，請選取**偏好較新的行**或**偏好較舊的行**。
8. 查看您的電子郵件。您收到一封來自 **LogDNA** 的電子郵件，其中含有一個鏈結，可下載您已匯出的行。


## 使用 API 以程式設計方式匯出日誌
{: #api}

請完成下列步驟，以程式設計方式匯出日誌：

1. 產生「服務金鑰」。 

    **附註：**您必須具有 {{site.data.keyword.la_full_notm}} 實例或服務的**管理員**角色，才能完成此步驟。如需相關資訊，請參閱[授與許可權以在 LogDNA 中管理日誌及配置警示](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)。

    1. 啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面。如需相關資訊，請參閱[移至 {{site.data.keyword.la_full_notm}} Web 使用者介面](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

    2. 選取**配置**圖示 ![配置圖示](images/admin.png)。然後，選取**組織**。 

    3. 選取 **API 金鑰**。

        您可以看到所建立的服務金鑰。 

    4. 按一下**產生服務金鑰**。

        這時會在清單中新增一個新的金鑰。複製這個金鑰。

2. 匯出日誌。執行下列 cURL 指令：

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    其中 

    * ENDPOINT 代表服務的進入點。每個地區都有不同的 URL。
    * QUERY_PARAMETERS 是參數，定義套用至匯出要求的過濾準則。
    * SERVICE_KEY 是您在前一個步驟中所建立的服務金鑰。

下表列出每個地區的端點：

| 地區         | 端點                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="每個地區的端點" caption-side="top"} 


下表列出您可以設定的查詢參數：

| 查詢參數 | 類型       | 狀態     | 說明 |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | 必要   | 開始時間。設為 UNIX 時間戳記（以秒或毫秒為單位）。|
| `to`        | `int32`      | 必要   | 結束時間。設為 UNIX 時間戳記（以秒或毫秒為單位）。|
| `size`      | `string`     | 選用   | 要包含在匯出中的日誌行數。| 
| `hosts`     | `string`     | 選用   | 以逗點區隔的主機清單。|
| `apps`      | `string`     | 選用   | 以逗點區隔的應用程式清單。|
| `levels`    | `string`     | 選用   | 以逗點區隔的記載層次清單。|
| `query`     | `string`     | 選用   | 搜尋查詢。如需相關資訊，請參閱[搜尋日誌](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)。|
| `prefer`    | `string`     | 選用   | 定義您要匯出的日誌行。有效值為 `head`（第一個日誌行）以及 `tail`（最後一個日誌行）。如果未指定，則預設為 tail。|
| `email`     | `string`     | 選用   | 指定含有匯出之可下載鏈結的電子郵件。依預設，會以串流方式來串流日誌行。|
| `emailSubject` | `string`     | 選用   | 用來設定電子郵件的主旨。</br>使用 `%20` 來代表空格。例如，範例值為 `Export%20logs`。|
{: caption="查詢參數" caption-side="top"} 

例如，若要將日誌行串流至終端機，您可以執行下列指令：

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

若要傳送具有該鏈結的電子郵件，以下載匯出上所指定的日誌行，您可以執行下列指令：

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


若要傳送具有自訂主旨的電子郵件，您可以執行下列指令：

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

