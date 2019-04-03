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

# IBM Cloud Log Analysis CLI（CF 外掛程式）
{: #logging_cli}

{{site.data.keyword.loganalysislong}} CLI 是一種外掛程式，可管理在 {{site.data.keyword.Bluemix}} 組織空間中執行之雲端資源的日誌。
{: shortdesc}

**必要條件**
* 在執行記載指令之前，請先使用 `ibmcloud login` 指令來登入 {{site.data.keyword.Bluemix_notm}}，以產生 {{site.data.keyword.Bluemix_short}} 存取記號，並鑑別您的階段作業。如需相關資訊，請參閱[如何登入 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

若要瞭解如何使用 {{site.data.keyword.loganalysisshort}} CLI，請參閱[管理日誌](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov)。

<table>
  <caption>用來管理日誌的指令</caption>
  <tr>
    <th>指令</th>
    <th>使用時機</th>
  </tr>
  <tr>
    <td>[ibmcloud cf logging](#base)</td>
    <td>使用這個指令，以取得 CLI 的相關資訊（例如版本或指令清單）。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging auth](#auth)</td>
    <td>使用這個指令，以取得用來將日誌傳送至 {{site.data.keyword.loganalysisshort}} 服務的記載記號。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging delete](#delete)</td>
    <td>使用這個指令，以刪除「日誌收集」中所儲存的日誌。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging download（測試版）](#download)</td>
    <td>使用這個指令，以將日誌從「日誌收集」下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging help](#help)</td>
    <td>使用這個指令，以取得如何使用 CLI 的協助以及所有指令的清單。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging option](#option)</td>
    <td>使用這個指令，以檢視或設定空間或帳戶中可用日誌的保留期間。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging session create（測試版）](#session_create1)</td>
    <td>使用這個指令，以建立新的階段作業。</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete（測試版）](#session_delete1)</td>
    <td>使用這個指令，以刪除階段作業。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session list（測試版）](#session_list1)</td>
    <td>使用這個指令，以列出作用中階段作業及其 ID。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session show（測試版）](#session_show1)</td>
    <td>使用這個指令，以顯示單一階段作業的狀態。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging status](#status1)</td>
    <td>使用這個指令，以取得空間或帳戶中所收集日誌的相關資訊。</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

提供 CLI 版本及如何使用 CLI 的相關資訊。

```
ibmcloud cf logging [parameters]
```
{: codeblock}

**參數**

<dl>
<dt>--help, -h</dt>
<dd>設定這個參數可顯示指令清單，或取得某個指令的說明。
</dd>

<dt>--version, -v</dt>
<dd>設定這個參數可列印 CLI 版本。</dd>
</dl>

**範例**

若要取得指令清單，請執行下列指令：

```
ibmcloud cf logging --help
```
{: codeblock}

若要取得 CLI 版本，請執行下列指令：

```
ibmcloud cf logging --version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

傳回可用來將日誌傳送至 {{site.data.keyword.loganalysisshort}} 服務的記載記號。 

**附註：**記號不會到期。

```
ibmcloud cf logging auth
```
{: codeblock}

**傳回**

<dl>
  <dt>記載記號</dt>
  <dd>例如，`jec8BmipiEZc`。
  </dd>
  
  <dt>組織 ID</dt>
  <dd>您所登入之 {{site.data.keyword.Bluemix_notm}} 組織的 GUID。
  </dd>
  
  <dt>空間 ID</dt>
  <dd>您所登入之組織內空間的 GUID。
  </dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

刪除「日誌收集」中所儲存的日誌。

```
ibmcloud cf logging delete [parameters]
```
{: codeblock}

**參數**

<dl>
  <dt>--start value, -s value</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為 2 週以前。
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD* <br>UTC 格式的日期為 **YYYY-MM-DD**（例如，`2006-01-02`）。<br>預設值設為現行日期。
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>（選用）設定日誌類型。<br>例如，*syslog* 是日誌類型。<br>預設值設為 **\***。<br>您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如 *log_type_1,log_type_2,log_type_3*。</dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>（選用）設定提供給帳戶層次的日誌資訊範圍。<br>如果未指定這個參數，預設值會設為僅提供現行空間的日誌資訊。
  </dd>
</dl>

**範例**

若要刪除 2017 年 5 月 25 日類型為 *linux_syslog* 的日誌，請執行下列指令：
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download（測試版）
{: #download4}

將日誌從「日誌收集」下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。 

**附註：**若要下載檔案，您需要先建立階段作業。階段作業會根據日期範圍、日誌類型及帳戶類型來定義要下載的日誌。您可以在階段作業環境定義內下載日誌。如需相關資訊，請參閱 [ibmcloud cf logging session create（測試版）](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#session_create1)。

```
ibmcloud cf logging download [parameters] [arguments]
```
{: codeblock}

**參數**

<dl>
<dt>--output value, -o value</dt>
<dd>（選用）設定已下載日誌的本端輸出檔的路徑及檔名。<br>預設值為連字號 (-)。<br>將這個參數設為預設值，以將日誌輸出至標準輸出。</dd>
</dl>

**引數**

<dl>
<dt>session_ID</dt>
<dd>設為當您執行指令 `ibmcloud cf logging session create` 時所取得的階段作業 ID 值。此值指出要在下載日誌時使用的階段作業。<br>**附註：**`ibmcloud cf logging session create` 指令提供參數來控制下載哪些日誌。</dd>
</dl>

**附註：**下載完成之後，重新執行相同的指令將會拒絕執行任何作業。若要重新下載相同的資料，您必須使用不同的檔案或不同的階段作業。

**範例**

在 Linux 系統中，若要將日誌下載至稱為 mylogs.gz 的檔案，請執行下列指令：

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

若要將日誌下載至您自己的 Elastic Stack，請執行下列指令：

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

下列檔案是 logstash.conf 檔案的範例：

```
input {
  stdin {
    codec => json_lines {}
  }
}
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
  }
}
```
{: screen}


## ibmcloud cf logging help
{: #help1}

提供如何使用指令的相關資訊。

```
ibmcloud cf logging help [command]
```
{: codeblock}

**參數**

<dl>
<dt>指令</dt>
<dd>設定您要取得協助的指令名稱。
</dd>
</dl>


**範例**

若要取得如何執行指令以檢視日誌狀態的協助，請執行下列指令：

```
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

顯示或變更空間或帳戶中可用日誌的保留期間。 

* 期間的設定單位是天數。
* 預設值為 **-1**。 

**附註：**依預設，會儲存所有日誌。您必須使用 **delete** 指令手動刪除它們。請設定保留原則，以自動刪除日誌。

```
ibmcloud cf logging option [parameters]
```
{: codeblock}

**參數**

<dl>
<dt>--retention value, -r value</dt>
<dd>（選用）設定保留天數。<br> 預設值為 *-1* 天。</dd>

<dt>--at-account-level, -a </dt>
  <dd>（選用）將範圍設為帳戶層次。<br>如果未指定這個參數，現行空間的預設值會設為 *-1*，而現行空間就是您使用 `ibmcloud cf login` 指令所登入的空間。
  </dd>
</dl>

**範例**

若要查看所登入空間的預設現行保留期間，請執行下列指令：

```
ibmcloud cf logging option
```
{: codeblock}

輸出如下：

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


若要將所登入空間的保留期間變更為 25 天，請執行下列指令：

```
ibmcloud cf logging option -r 25
```
{: codeblock}

輸出如下：

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create（測試版）
{: #session_create1}

建立新的階段作業。

**附註：**一個空間最多可以有 30 個並行階段作業。階段作業是為使用者而建立。空間中的使用者之間無法共用階段作業。

```
ibmcloud cf logging session create [parameters]
```
{: codeblock}

**參數**

<dl>
  <dt>--start value, -s value</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為 2 週以前。
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為現行日期。
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>（選用）設定日誌類型。<br>例如，*syslog* 是日誌類型。<br>預設值設為星號 (*)。<br>您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，*log_type_1,log_type_2,log_type_3*。
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>（選用）將範圍設為帳戶層次。<br>如果未指定這個參數，預設值會設為僅限現行空間，即您使用 `ibmcloud cf login` 指令所登入的空間。
  </dd>
</dl>

**傳回的值**

<dl>
<dt>Access-Time</dt>
<dd>指出前次使用階段作業的時間戳記。</dd>

<dt>Create-Time</dt>
<dd>對應於階段作業建立日期和時間的時間戳記。</dd>

<dt>Date-Range</dt>
<dd>指出用來過濾日誌的天數。此日期範圍中所識別的日誌，可透過階段作業進行管理。</dd>

<dt>ID</dt>
<dd>階段作業 ID。</dd>

<dt>Space</dt>
<dd>階段作業作用中的空間 ID。</dd>

<dt>Type-Account</dt>
<dd>透過階段作業下載的日誌類型。</dd>

<dt>Username</dt>
<dd>建立階段作業之使用者的 {{site.data.keyword.IBM_notm}} ID。</dd>
</dl>


**範例**

若要建立一個階段作業，其中包括 2017 年 5 月 20 日與 2017 年 5 月 26 日之間日誌類型為 *log* 的日誌，請執行下列指令：

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete（測試版）
{: #session_delete1}

刪除依階段作業 ID 所指定的階段作業。

```
ibmcloud cf logging session delete [arguments]
```
{: codeblock}

**引數**

<dl>
<dt>session ID</dt>
<dd>您要刪除之階段作業的 ID。<br>您可以使用 `ibmcloud cf logging session list` 指令來取得所有作用中階段作業 ID。</dd>
</dl>

**範例**

若要刪除階段作業 ID 為 *cI6hvAa0KR_tyhjxZZz9Uw==* 的階段作業，請執行下列指令：

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list（測試版）
{: #session_list1}

列出作用中階段作業及其 ID。

```
ibmcloud cf logging session list 
```
{: codeblock}

**傳回的值**

<dl>
<dt>ID</dt>
<dd>階段作業 ID。</dd>

<dt>SPACE</dt>
<dd>階段作業作用中的空間 ID。</dd>

<dt>USERNAME</dt>
<dd>建立階段作業之使用者的 {{site.data.keyword.IBM_notm}} ID。</dd>

<dt>CREATE-TIME</dt>
<dd>對應於階段作業建立日期和時間的時間戳記。</dd>

<dt>ACCESS-TIME</dt>
<dd>指出前次使用階段作業的時間戳記。</dd>
</dl>
 

## ibmcloud cf logging session show（測試版）
{: #session_show1}

顯示單一階段作業的狀態。

```
ibmcloud cf logging session show [arguments]
```
{: codeblock}

**引數**

<dl>
<dt>session_ID</dt>
<dd>您要取得其資訊的作用中階段作業的 ID。</dd>
</dl>

**傳回的值**

<dl>
<dt>Access-Time</dt>
<dd></dd>

<dt>Create-Time</dt>
<dd>對應於階段作業建立日期和時間的時間戳記。</dd>

<dt>Date-Range</dt>
<dd>指出用來過濾日誌的天數。此日期範圍中所識別的日誌，可透過階段作業進行管理。</dd>

<dt>ID</dt>
<dd>階段作業 ID。</dd>

<dt>Space</dt>
<dd>階段作業作用中的空間 ID。</dd>

<dt>Type-Account</dt>
<dd>透過階段作業下載的日誌類型。</dd>

<dt>Username</dt>
<dd>建立階段作業之使用者的 {{site.data.keyword.IBM_notm}} ID。</dd>
</dl>

**範例**

若要顯示階段作業 ID 為 *cI6hvAa0KR_tyhjxZZz9Uw==* 的階段作業的詳細資料，請執行下列指令：

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

傳回空間或帳戶中所收集日誌的相關資訊。

```
ibmcloud cf logging status [parameters]
```
{: codeblock}

**參數**

<dl>
  <dt>--start value, -s value</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為 2 週以前。
  </dd>
  
  <dt>--end value, -e value</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為現行日期。
  </dd>
  
  <dt>--type value, -t value</dt>
  <dd>（選用）設定日誌類型。<br>例如，*syslog* 是日誌類型。<br>預設值設為星號 (*)。<br>您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，*log_type_1,log_type_2,log_type_3*。
  </dd>
  
  <dt>--at-account-level, -a </dt>
  <dd>（選用）將範圍設為帳戶層次。<br> **附註：**請設定這個值以取得帳戶資訊。<br>如果未指定這個參數，預設值會設為僅限現行空間，即您使用 `ibmcloud cf login` 指令所登入的空間。
  </dd>
  
  <dt>--list-type-detail, -l</dt>
  <dd>（選用）設定這個參數來列出每天的日誌類型小計。
  </dd>
</dl>

**附註：**未指定開始及結束日期時，`ibmcloud cf logging status` 指令只會報告過去 2 週儲存在「日誌收集」中的日誌。


