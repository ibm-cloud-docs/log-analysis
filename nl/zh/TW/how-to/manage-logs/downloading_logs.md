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
{: #downloading_logs1}

您可以將日誌下載至本端檔案，或透過管道將資料傳送至另一個程式。您可以在階段作業環境定義內下載日誌。階段作業會指定將下載的日誌。如果日誌下載被岔斷，階段作業會從停止處繼續下載。下載完成之後，您必須刪除階段作業。
{:shortdesc}

請完成下列步驟，以將 {{site.data.keyword.Bluemix_notm}} 空間中可用的日誌資料下載至本端檔案：

## 步驟 1：登入 IBM Cloud

登入 {{site.data.keyword.Bluemix_notm}} 中的地區、組織及空間。 

如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

## 步驟 2：識別可用的日誌
{: #step31}

1. 使用 `ibmcloud cf logging status` 指令，以查看過去 2 週的可用日誌。執行下列指令：

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    例如，這個指令的執行輸出如下：
    
    ```
    +------------+--------+-------+--------------------+------------+
    |    DATE    |  COUNT | SIZE  |       TYPES        | SEARCHABLE |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-24 |    16  | 3020  |        log         |   None     |
    +------------+--------+-------+--------------------+------------+
    | 2017-05-25 |   1224 | 76115 | linux_syslog,log   |    All     |
    +------------+--------+-------+--------------------+------------+
    ```
    {: screen}

    **附註：**{{site.data.keyword.loganalysisshort}} 服務是一項廣域服務，其使用「世界標準時間 (UTC)」。日定義為「世界標準時間」日。若要取得特定當地時間日期的日誌，您可能需要下載多個「世界標準時間」日。


## 步驟 3：建立階段作業
{: #step32}

需要有階段作業，才能定義可供下載的日誌資料範圍，以及保持下載的狀態。 

請使用指令 [cf logging session create](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) 來建立階段作業。您可以選擇指定建立階段作業的開始日期、結束日期及日誌類型：  

* 當您指定開始日期及結束日期時，階段作業可讓您存取這兩個日期（含）之間的日誌。 
* 當您指定日誌類型 (**-t**) 時，階段作業可讓您存取特定類型的日誌。當您管理大規模的日誌時，這是重要特性，因為您可以將階段作業的範圍設定為僅感興趣的小部分日誌。

**附註：**針對每一個階段作業，您最多可以下載 15 天的日誌。

若要建立用來下載日誌類型為 *log* 的階段作業，請執行下列指令：

```
ibmcloud cf logging session create -t log
```
{: codeblock}

此階段作業會傳回下列資訊：

* 要下載的日期範圍。預設值為現行「世界標準時間」日期。
* 要下載的日誌類型。依預設，會包括當您建立階段作業時所指定時段內可用的所有日誌類型。 
* 包括整個帳戶還是只包括現行空間的相關資訊。依預設，您可以取得所登入空間中的日誌。
* 下載日誌所需的階段作業 ID。

例如，

```
$ ibmcloud cf logging session create -t log     
+--------------+--------------------------------------+
|     NAME     |                VALUE                 |
+--------------+--------------------------------------+
| Access-Time  | 2017-05-25T18:04:21.743792338Z       |
| Create-Time  | 2017-05-25T18:04:21.743792338Z       |
| Date-Range   | {                                    |
|              |  "End": "2017-05-25T00:00:00Z",      |
|              |  "Start": "2017-05-25T00:00:00Z"     |
|              | }                                    |
| Id           | -jshdjsunelsssr4566722==             |
| Space        | fdgrghg3-b090-4567-vvfg-afbc436902a3 |
| Type-Account | {                                    |
|              |  "Type": "log"                       |
|              | }                                    |
| Username     | xxx@yyy.com                          |
+--------------+--------------------------------------+
```
{: screen}

**提示：**若要查看作用中階段作業清單，請執行這個指令 [cf logging session list](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_list1)。

## 步驟 4：將日誌資料下載至檔案
{: #step42}

若要下載階段作業參數所指定的日誌，請執行下列指令：

```
ibmcloud cf logging download -o Log_File_Name Session_ID
```
{: codeblock}

其中

* Log_File_Name 是輸出檔的名稱。
* Session_ID 是階段作業的 GUID。您可以在前一個步驟中取得此值。

例如，

```
ibmcloud cf logging download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

下載日誌時，進度指示器會從 0 移至 100%。

**附註：** 

* 下載資料的格式會壓縮為 JSON。如果您解壓縮並開啟 .gz 檔案，則可以看到 JSON 格式的資料。 
* 壓縮的 JSON 適用於 ElasticSearch 或 Logstash 的汲取。如果未給定 -o，則資料將會串流至 stdout，讓您直接透過管道將它傳送至您自己的 ELK Stack。
* 您也可以使用任何可剖析 JSON 的程式來處理資料。 

## 步驟 5：刪除階段作業
{: #step51}

下載完成之後，您必須使用 [cf logging session delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_delete1) 指令來刪除階段作業。 

執行下列指令，以刪除階段作業：

```
ibmcloud cf logging session delete Session_ID
```
{: codeblock}

其中，Session_ID 是您在前一個步驟中所建立之階段作業的 GUID。

例如，

```
ibmcloud cf logging session delete -jshdjsunelsssr4566722==
+---------+------------------------+
|  NAME   |         VALUE          |
+---------+------------------------+
| Message | Delete session success |
+---------+------------------------+
```
{: screen}




