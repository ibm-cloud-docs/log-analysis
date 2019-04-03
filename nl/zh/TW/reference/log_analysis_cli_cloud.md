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

# Log Analysis CLI（{{site.data.keyword.Bluemix_notm}} 外掛程式）
{: #log_analysis_cli}

{{site.data.keyword.loganalysislong}} CLI 是一種 {{site.data.keyword.Bluemix_notm}} 外掛程式，可用來管理「日誌收集」中所儲存的日誌。
{: shortdesc}

**必要條件**
* 在執行記載指令之前，請先使用 `ibmcloud login` 指令來登入 {{site.data.keyword.Bluemix_notm}}，以產生存取記號，並鑑別您的階段作業。

若要瞭解如何使用 {{site.data.keyword.loganalysisshort}} CLI，請參閱[管理日誌](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov)。

<table>
  <caption>用來管理日誌的指令</caption>
  <tr>
    <th>指令</th>
    <th>使用時機</th>
  </tr>
  <tr>
    <td>[ibmcloud logging](#base)</td>
    <td>使用這個指令，以取得 CLI 的相關資訊（例如指令清單）。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-delete](#delete)</td>
    <td>使用這個指令，以刪除「日誌收集」中所儲存的日誌。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-download](#download)</td>
    <td>使用這個指令，以將日誌從「日誌收集」下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-show](#status)</td>
    <td>使用這個指令，以取得空間、組織或帳戶中所收集日誌的相關資訊。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging help](#help)</td>
    <td>使用這個指令，以取得如何使用 CLI 的協助以及所有指令的清單。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-show](#optionshow)</td>
    <td>使用這個指令，以檢視空間、組織或帳戶中可用日誌的保留期間。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-update](#optionupdate)</td>
    <td>使用這個指令，以設定空間、組織或帳戶中可用日誌的保留期間。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging quota-usage-show](#quotausage)</td>
    <td>使用這個指令，以取得空間、組織或帳戶的配額用量資訊。您也可以取得配額歷程資訊。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging session-create](#session_create)</td>
    <td>使用這個指令，以建立新的階段作業。</td>
  <tr>
  <tr>
    <td>[ibmcloud logging session-delete](#session_delete)</td>
    <td>使用這個指令，以刪除階段作業。</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging sessions](#session_list)</td>
    <td>使用這個指令，以列出作用中階段作業及其 ID。</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging session-show](#session_show)</td>
    <td>使用這個指令，以顯示單一階段作業的狀態。</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging token-get](#tokenget)</td>
    <td>使用這個指令，以取得用來將日誌資料傳送至 {{site.data.keyword.loganalysisshort}} 服務的記載記號。</td>
  </tr>
</table>


## ibmcloud logging
{: #base}

提供 CLI 的一般資訊。

```
ibmcloud logging 
```
{: codeblock}

**範例**

若要取得指令清單，請執行下列指令：

```
ibmcloud logging 
NAME:
   ibmcloud logging - IBM Cloud Log Analysis Service
USAGE:
   ibmcloud logging command [arguments...] [command options]

COMMANDS:
COMMANDS:
   log-delete         Delete log
   log-download       Download a log
   log-show           Show the count, size, and type of logs per day
   session-create     Create a session
   session-delete     Delete session
   sessions           List sessions info
   session-show       Show a session info
   option-show        Show the log retention
   option-update      Show the log options
   token-get          Get a logging token for sending logs
   quota-usage-show   Show quota usage info
   help             
   
Enter 'ibmcloud logging help [command]' for more information about a command.
```
{: codeblock}




## ibmcloud logging log-delete
{: #delete3}

刪除「日誌收集」中所儲存的日誌。

```
ibmcloud logging log-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-f, --force ]
```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為 2 週以前。
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為現行日期。
  </dd>
  
  <dt>-f, --force </dt>
  <dd>（選用）設定此選項，以刪除日誌，而不需要確認動作。
  </dd>
</dl>

**範例**

若要刪除 2017 年 5 月 25 日類型為 *linux_syslog* 的日誌，請執行下列指令：
```
ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: screen}



## ibmcloud logging log-download 
{: #download3}

將日誌從「日誌收集」下載至本端檔案，或透過管道將日誌傳送至另一個程式（例如 Elastic Stack）。 

**附註：**若要下載檔案，您需要先建立階段作業。階段作業會根據日期範圍、日誌類型及帳戶類型來定義要下載的日誌。您可以在階段作業環境定義內下載日誌。如需相關資訊，請參閱 [ibmcloud logging session create（測試版）](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#session_create)。

```
 ibmcloud logging log-download  [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-o, --output OUTPUT] SESSION_ID

```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
 
  <dt>-o, --output OUTPUT</dt>
  <dd>（選用）設定已下載日誌的本端輸出檔的路徑及檔名。<br>預設值為連字號 (-)。<br>將這個參數設為預設值，以將日誌輸出至標準輸出。</dd>

</dl>

**引數**

<dl>
  <dt>SESSION_ID</dt>
  <dd>此值指出您在下載日誌時必須使用的階段作業 ID。<br>**附註：**`ibmcloud logging session-create` 指令提供參數來控制下載哪些日誌。</dd>
</dl>

**附註：**下載完成之後，重新執行相同的指令將會拒絕執行任何作業。若要重新下載相同的資料，您必須使用不同的檔案或不同的階段作業。

**範例**

在 Linux 系統中，若要將日誌下載至稱為 mylogs.gz 的檔案，請執行下列指令：

```
ibmcloud logging log-download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

若要將日誌下載至您自己的 Elastic Stack，請執行下列指令：

```
ibmcloud logging log-download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
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


## ibmcloud logging help
{: #help}

提供如何使用指令的相關資訊。

```
ibmcloud logging help [command] 
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
ibmcloud logging help log-show
NAME:
   log-show - Show the count, size, and type of logs per day

USAGE:
   ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]

OPTIONS:
   -r, --resource-type     Resource type, the valid resource type is account, org, or space
   -i, --resource-id       Resource id, the target resource id
   -s, --start             Start Date, UTC time value included in format YYYY-MM-DD
   -e, --end               End Date, UTC time value included in format YYYY-MM-DD
   -t, --type              Log Type, for example "syslog"
   -l, --list-type-detail  List the detailed type

```
{: screen}


## ibmcloud logging option-show
{: #optionshow}

顯示空間、組織或帳戶中可用日誌的保留期間。 

* 期間的設定單位是天數。
* 預設值為 **-1**。 

**附註：**依預設，會儲存所有日誌。您必須使用 **delete** 指令手動刪除它們。請設定保留原則，以自動刪除日誌。

```
ibmcloud logging option-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>

</dl>

**範例**

若要查看所登入空間的預設現行保留期間，請執行下列指令：

```
ibmcloud logging option-show
```
{: screen}




## ibmcloud logging option-update
{: #optionupdate}

變更空間、組織或帳戶中可用日誌的保留期間。 

* 期間的設定單位是天數。
* 預設值為 **-1**。 

```
ibmcloud logging option-update [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] <-e,--retention RETENTION_VALUE>
```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為要取得其資訊的空間、組織或帳戶 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
  
  <dt>-e,--retention RETENTION_VALUE</dt>
  <dd>設定日誌的保留天數。</dd>

</dl>

**範例**

若要將所登入空間的保留期間變更為 25 天，請執行下列指令：

```
ibmcloud logging option-update -e 25
```
{: screen}


## ibmcloud logging quota-usage-show
{: #quotausage}

通知空間、組織或帳戶的配額用量。您也可以用它來取得歷程用量。

* 期間的設定單位是天數。
* 預設值為 **-1**。 

```
ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s,--history]
```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
  
  <dt>-s,--history</dt>
  <dd>（選用）設定此參數，以取得配額用量的相關歷程資訊。</dd>

</dl>

**範例**

若要取得空間網域的歷程配額用量，請執行下列指令：

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}

## ibmcloud logging session-create
{: #session_create}

建立新的階段作業。

**附註：**一個空間最多可以有 30 個並行階段作業。階段作業是為使用者而建立。空間中的使用者之間無法共用階段作業。

```
ibmcloud logging session-create [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-T, --time, LOG_TIME]
```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為 2 週以前。
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為現行日期。
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>（選用）設定日誌類型。<br>例如，*syslog* 是日誌類型。<br>預設值設為星號 (*)。<br>您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，*log_type_1,log_type_2,log_type_3*。
  </dd>

  <dt>-T, --time, LOG_TIME</dt>
  <dd>（選用）設定您要取得特定類型日誌的當日小時。</br>有效值為 0-23。</br>它應該結合 LOG_TYPE 一起使用。
  </dd>

</dl>


**傳回的值**

<dl>

    <dt>ID</dt>
    <dd>階段作業 ID。</dd>
	
	<dt>資源類型</dt>
    <dd>資源 ID。</dd>

    <dt>AccessTime</dt>
    <dd>指出前次使用階段作業的時間戳記。</dd>

    <dt>CreateTime</dt>
    <dd>對應於階段作業建立日期和時間的時間戳記。</dd>
	
	<dt>Start</dt>
    <dd>指出用來過濾日誌的第一天。</dd>

    <dt>End</dt>
    <dd>指出用來過濾日誌的最後一天。</dd>

    <dt>類型</dt>
    <dd>透過階段作業下載的日誌類型。</dd>

</dl>


**範例**

若要建立包含 2017 年 11 月 13 日之日誌的階段作業，請執行下列指令：

```
ibmcloud logging session-create -s 2017-11-13 -e 2017-11-13
Creating session for xxxxx@yyy.com resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   2017-11-13   2017-11-13   ANY_TYPE   
Session: 1ef776d1-4d25-4297-9693-882606c725c8 is created
```
{: screen}


## ibmcloud logging session-delete 
{: #session_delete}

刪除依階段作業 ID 所指定的階段作業。

```
ibmcloud session-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID
```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
 
</dl>

**引數**

<dl>
  <dt>SESSION_ID</dt>
  <dd>您要刪除之作用中階段作業的 ID。</dd>
</dl>

**範例**

若要刪除階段作業 ID 為 *cI6hvAa0KR_tyhjxZZz9Uw==* 的階段作業，請執行下列指令：

```
ibmcloud logging session-delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud logging sessions
{: #session_list}

列出作用中階段作業及其 ID。

```
ibmcloud logging sessions [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**參數**

<dl>

  <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
      </dd>
</dl>

**回覆值**

<dl>	
    <dt>SESSION_ID</dt>
    <dd>作用中階段作業的 ID。</dd>
	   
    <dt>資源 ID</dt>
    <dd>階段作業有效的資源 ID。</dd>

    <dt>CreateTime</dt>
    <dd>對應於階段作業建立日期和時間的時間戳記。</dd>

    <dt>AccessTime</dt>
    <dd>指出前次使用階段作業的時間戳記。</dd>
</dl>
 
**範例**

```
ibmcloud logging sessions
Listing sessions of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

ID                                     Space                                  CreateTime                       AccessTime   
1ef776d1-4d25-4297-9693-882606c725c8   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   2017-11-16T11:52:06.376125207Z   2017-11-16T11:52:06.376125207Z   
Listed the sessions of resource xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 
```
:{ screen}





## ibmcloud logging session-show
{: #session_show}

顯示單一階段作業的狀態。

```
ibmcloud logging session-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID

```
{: codeblock}

**參數**

<dl>
   <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
      </dd>
</dl>

**引數**

<dl>
   <dt>SESSION_ID</dt>
   <dd>您要取得其資訊的作用中階段作業的 ID。</dd>
</dl>

**範例**

若要顯示階段作業 ID 為 *cI6hvAa0KR_tyhjxZZz9Uw==* 的階段作業的詳細資料，請執行下列指令：

```
ibmcloud logging session-show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}

## ibmcloud logging token-get
{: #tokenget}

傳回用來將日誌資料傳送至 {{site.data.keyword.loganalysisshort}} 所需的記載記號。

```
ibmcloud logging token-get [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定您計劃傳送日誌資料的資源類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
</dl>


**範例**

```
ibmcloud logging token-get -r space -i js7ydf98-8682-430d-bav4-36b712341744
Getting log token of resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Tenant Id                              Logging Token   
js7ydf98-8682-430d-bav4-36b712341744   xxxxxxxxxx   
```
{: screen}


## ibmcloud logging log-show
{: #status}

傳回 {{site.data.keyword.Bluemix_notm}} 空間或帳戶中所收集日誌的相關資訊。

```
ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]
```
{: codeblock}

* 未指定資源類型時，指令會傳回所登入資源的詳細資料。
* 如果您指定資源類型，則必須指定資源 ID。
* 未指定開始及結束日期時，此指令只會報告過去 2 週儲存在「日誌收集」中日誌的相關資訊。

**參數**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>（選用）設定資源的類型。有效值為：*space*、*account* 及 *org*
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>（選用）將此欄位設為空間、組織或帳戶的 ID。<br>依預設，如果您未指定此參數，則指令會使用所登入資源的 ID。
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的開始日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為 2 週以前。
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>（選用）設定「世界標準時間 (UTC)」格式的結束日期：*YYYY-MM-DD*（例如，`2006-01-02`）。<br>預設值設為現行日期。
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>（選用）設定日誌類型。<br>例如，*syslog* 是日誌類型。<br>預設值設為星號 (*)。<br>您可以指定多種日誌類型，作法是使用逗點來區隔每一種類型，例如，*log_type_1,log_type_2,log_type_3*。
  </dd>
  
  <dt>-l, --list-type-detail</dt>
  <dd>（選用）設定此參數，以個別列出每一個日誌類型。
  </dd>
</dl>


**範例**

```
ibmcloud logging log-show
Showing log status of resource: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx ...

Date         Size        Count    Searchable   Types   
2017-11-07   1878197     1333     None         default   
2017-11-13   201653512   179391   All          default,linux_syslog   
2017-11-14   32134119    30425    All          default,linux_syslog   
2017-11-15   303901156   269689   All          linux_syslog,default   
2017-11-16   107253679   96648    All          default,linux_syslog   
```
{: screen}

```
 ibmcloud logging log-show -l
Showing log status of resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

Date         Size        Count    Searchable   Type   
2017-11-14   30146764    26611    true         default   
2017-11-14   1987355     3814     true         linux_syslog   
2017-11-15   303004895   267890   true         default   
2017-11-15   896261      1799     true         linux_syslog   
2017-11-16   107918249   96278    true         default   
2017-11-16   912890      1794     true         linux_syslog   
```
{: screen}
