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

# 下載日誌
{: #downloading_logs}

您可以將日誌下載至本端檔案，或透過管道將資料傳送至另一個程式。您可以在階段作業環境定義內下載日誌。階段作業會指定將下載的日誌。如果日誌下載被岔斷，階段作業會從停止處繼續下載。下載完成之後，您必須刪除階段作業。
{:shortdesc}

若要完成這些步驟，您必須安裝 {{site.data.keyword.loganalysisshort}} CLI。如需相關資訊，請參閱[配置 {{site.data.keyword.loganalysisshort}} CLI](https://console.bluemix.net/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli_)。


請完成下列步驟，以將空間中可用的日誌資料下載至本端檔案：

## 步驟 1：登入 {{site.data.keyword.Bluemix_notm}}
{: #downloading_logs_step1}

登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

## 步驟 2：識別可用的日誌
{: #step21}

1. 使用 `ibmcloud logging log-show` 指令，以查看過去 2 週的可用日誌。執行下列指令：

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如，此指令的執行輸出如下：
    
    ```
    ibmcloud logging log-show 
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size     Count   Searchable   Types   
    2017-11-16   794008   706     All          syslog, default   
	2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}

    **附註：**{{site.data.keyword.loganalysisshort}} 服務是一項廣域服務，其使用「世界標準時間 (UTC)」。日定義為「世界標準時間」日。若要取得特定當地時間日期的日誌，您可能需要下載多個「世界標準時間」日。


## 步驟 3：建立階段作業
{: #step3}

需要有階段作業，才能定義可供下載的日誌資料範圍，以及保持下載的狀態。 

使用指令 [ibmcloud logging session-create](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_create) 來建立階段作業。您可以選擇指定建立階段作業的開始日期、結束日期及日誌類型：  

* 當您指定開始日期及結束日期時，階段作業可讓您存取這兩個日期（含）之間的日誌。 
* 當您指定日誌類型 (**-t**) 時，階段作業可讓您存取特定類型的日誌。當您管理大規模的日誌時，這是重要特性，因為您可以將階段作業的範圍設定為僅感興趣的小部分日誌。

**附註：**針對每一個階段作業，您最多可以下載 15 天的日誌。

若要建立用來下載過去 2 週可用之所有日誌的階段作業，請執行下列指令：

```
ibmcloud logging session-create 
```
{: codeblock}

此階段作業會傳回下列資訊：

* 要下載的日期範圍。預設值為現行「世界標準時間」日期。
* 要下載的日誌類型。依預設，會包括當您建立階段作業時所指定時段內可用的所有日誌類型。 
* 包括整個帳戶還是只包括現行空間的相關資訊。依預設，您可以取得所登入空間中的日誌。
* 下載日誌所需的階段作業 ID。

例如，

```
$ ibmcloud logging session-create
Creating session for lopezdsr@uk.ibm.com resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type
944aec4d-61f4-43d1-8f3b-c040195122da   12345678-1234-5678-abcd-378620d6fab5   2017-11-17T14:17:25.611542863Z   2017-11-17T14:17:25.611542863Z   2017-11-04   2017-11-17   ANY_TYPE
Session: 944aec4d-61f4-43d1-8f3b-c040195122da is created
```
{: screen}

**提示：**若要查看作用中階段作業清單，請執行此指令 [ibmcloud logging sessions](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_list)。

## 步驟 4：將日誌資料下載至檔案
{: #step41}

若要下載階段作業參數所指定的日誌，請執行下列指令：

```
ibmcloud logging log-download -o Log_File_Name Session_ID
```
{: codeblock}

其中

* Log_File_Name 是輸出檔的名稱。
* Session_ID 是階段作業的 GUID。您可以在前一個步驟中取得此值。

例如，

```
ibmcloud logging log-download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

下載日誌時，進度指示器會從 0 移至 100%。

**附註：** 

* 下載資料的格式會壓縮為 JSON。如果您解壓縮並開啟 .gz 檔案，則可以看到 JSON 格式的資料。 
* 壓縮的 JSON 適用於 ElasticSearch 或 Logstash 的汲取。如果未給定 -o，則資料將會串流至 stdout，讓您直接透過管道將它傳送至您自己的 ELK Stack。
* 您也可以使用任何可剖析 JSON 的程式來處理資料。 

## 步驟 5：刪除階段作業
{: #step5}

下載完成之後，您必須使用 [ibmcloud logging session delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) 指令來刪除階段作業。 

執行下列指令，以刪除階段作業：

```
ibmcloud logging session-delete Session_ID
```
{: codeblock}

其中，Session_ID 是您在前一個步驟中所建立之階段作業的 GUID。

例如，

```
ibmcloud logging session-delete -jshdjsunelsssr4566722==
Deleting session: -jshdjsunelsssr4566722== of resource: 12345678-1234-5678-abcd-378620d6fab5 ...
Session: -jshdjsunelsssr4566722== is deleted

```
{: screen}




