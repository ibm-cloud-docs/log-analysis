---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

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

 
# 傳送日誌
{: #ingest}

您可以將日誌資料傳送至 {{site.data.keyword.la_full_notm}} 實例。
{:shortdesc}

請完成下列步驟，以程式設計方式傳送日誌：

## 步驟 1. 取得汲取 API 金鑰 
{: #ingest_step1}

**附註：**您必須具有 {{site.data.keyword.la_full_notm}} 實例或服務的**管理員**角色，才能完成此步驟。如需相關資訊，請參閱[授與許可權以在 LogDNA 中管理日誌及配置警示](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)。

請完成下列步驟來取得汲取金鑰：
    
1. 啟動 {{site.data.keyword.la_full_notm}} Web 使用者介面。如需相關資訊，請參閱[移至 {{site.data.keyword.la_full_notm}} Web 使用者介面](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 選取**配置**圖示 ![配置圖示](images/admin.png)。然後，選取**組織**。 

3. 選取 **API 金鑰**。

    您可以看到已建立的汲取金鑰。 

4. 使用現有的汲取金鑰，或按一下**產生汲取金鑰**來建立新的汲取金鑰。

    這時會在清單中新增一個新的金鑰。複製金鑰。


## 步驟 2. 傳送日誌
{: #ingest_step2}

若要傳送日誌，請執行下列 cURL 指令：

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

其中 

* ENDPOINT 代表服務的進入點。每個地區都有不同的 URL。
* QUERY_PARAMETERS 是參數，定義套用至汲取要求的過濾準則。
* LOG_LINES 說明您要傳送的那組日誌行。其定義為物件的陣列。
* INGESTION_KEY 是您在前一個步驟中所建立的金鑰。

下表列出每個地區的端點：

| 地區         | 端點                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="每個地區的端點" caption-side="top"} 


下表列出查詢參數：

| 查詢參數 | 類型       | 狀態     | 說明 |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | 必要   | 來源的主機名稱。|
| `mac`           | `string`     | 選用   | 主機的網路 MAC 位址。|
| `ip`            | `string`     | 選用   | 主機的本端 IP 位址。| 
| `now`           | `date-time`  | 選用   | 要求時的來源 UNIX 時間戳記（以毫秒為單位）。用來計算時間漂移。|
| `tags`          | `string`     | 選用   | 用來動態分組主機的標籤。|
{: caption="查詢參數" caption-side="top"} 



下表列出每個日誌行所需的資料：

| 參數     | 類型       | 說明                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | 記錄日誌項目時的 UNIX 時間戳記（包括毫秒）。| 
| `line`           | `string`     | 日誌行的文字。|
| `app`            | `string`     | 產生日誌行的應用程式名稱。|
| `level`          | `string`     | 設定層次的值。例如，此參數的範例值為 `INFO`、`WARNING`、`ERROR`。|
| `meta`           |            | 此欄位保留給與日誌行相關聯的自訂資訊。若要將 meta 資料新增至 API 呼叫，請在行物件下面指定 meta 欄位。可以在該行的環境定義內檢視 meta 資料。|
{: caption="行物件欄位" caption-side="top"} 

例如，下列範例顯示您要汲取之日誌行的 JSON：

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00, 
      "line":"This is my first log line.", 
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## 範例
{: #ingest_example}

下列範例顯示 cURL 指令，其可將 1 個日誌行傳送至 {{site.data.keyword.la_full_notm}} 服務的實例： 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

