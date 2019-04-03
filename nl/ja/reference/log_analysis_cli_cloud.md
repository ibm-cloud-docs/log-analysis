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

# Log Analysis CLI ({{site.data.keyword.Bluemix_notm}} プラグイン)
{: #log_analysis_cli}

{{site.data.keyword.loganalysislong}} CLI は、Log Collection に保管されたログを管理するために使用できる {{site.data.keyword.Bluemix_notm}} プラグインです。
{: shortdesc}

**前提条件**
* ロギング・コマンドを実行する前に、`ibmcloud login` コマンドを使用して {{site.data.keyword.Bluemix_notm}} にログインし、アクセス・トークンを生成して、セッションを認証します。

{{site.data.keyword.loganalysisshort}} CLI の使用方法については、『[ログの管理](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#log_analysis_ov)』を参照してください。

<table>
  <caption>ログを管理するためのコマンド</caption>
  <tr>
    <th>コマンド</th>
    <th>いつ使用するか</th>
  </tr>
  <tr>
    <td>[ibmcloud logging](#base)</td>
    <td>この CLI についての情報 (コマンド・リストなど) を取得するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-delete](#delete)</td>
    <td>Log Collection に保管されたログを削除するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-download](#download)</td>
    <td>Log Collection からローカル・ファイルにログをダウンロードするか、または、別のプログラム (例えば Elastic スタック) にログをパイプするには、このコマンドを使用します。 </td>
  </tr>
  <tr>
    <td>[ibmcloud logging log-show](#status)</td>
    <td>スペース、組織、またはアカウントで収集されたログに関する情報を取得するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging help](#help)</td>
    <td>この CLI の使用方法に関するヘルプ、およびすべてのコマンドのリストを取得するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-show](#optionshow)</td>
    <td>スペース、組織、またはアカウント内にあるログの保存期間を表示するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging option-update](#optionupdate)</td>
    <td>スペース、組織、またはアカウント内にあるログの保存期間を設定するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging quota-usage-show](#quotausage)</td>
    <td>スペース、組織、またはアカウントの割り当て使用量情報を取得するには、このコマンドを使用します。 割り当て量の履歴情報を取得することもできます。</td>
  </tr>
  <tr>
    <td>[ibmcloud logging session-create](#session_create)</td>
    <td>新規セッションを作成するには、このコマンドを使用します。</td>
  <tr>
  <tr>
    <td>[ibmcloud logging session-delete](#session_delete)</td>
    <td>セッションを削除するには、このコマンドを使用します。</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging sessions](#session_list)</td>
    <td>アクティブ・セッションおよびその ID をリストするには、このコマンドを使用します。</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging session-show](#session_show)</td>
    <td>単一セッションの状況を表示するには、このコマンドを使用します。</td>
  <tr>  
  <tr>
    <td>[ibmcloud logging token-get](#tokenget)</td>
    <td>ログ・データを {{site.data.keyword.loganalysisshort}} サービスに送信するためのロギング・トークンを取得するには、このコマンドを使用します。</td>
  </tr>
</table>


## ibmcloud logging
{: #base}

CLI に関する一般情報を提供します。

```
ibmcloud logging 
```
{: codeblock}

**例**

コマンドのリストを取得するには、次のコマンドを実行します。

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

Log Collection に保管されたログを削除します。

```
ibmcloud logging log-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-f, --force ]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(オプション) 開始日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、2 週間前に設定されます。
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(オプション) 終了日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、現在日付に設定されます。
  </dd>
  
  <dt>-f, --force </dt>
  <dd>(オプション) アクションに対する確認を行わずにログを削除するには、このオプションを設定します。
  </dd>
</dl>

**例**

2017 年 5 月 25 日のタイプ *linux_syslog* のログを削除するには、次のコマンドを実行します。
```
ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: screen}



## ibmcloud logging log-download 
{: #download3}

Log Collection からローカル・ファイルにログをダウンロードするか、別のプログラム (Elastic スタックなど) にログをパイプします。 

**注:** ファイルをダウンロードするには、まずセッションを作成する必要があります。 セッションは、日付範囲、ログ・タイプ、およびアカウント・タイプに基づいて、ダウンロードするログを定義します。 ログのダウンロードは、1 つのセッションのコンテキスト内で行います。 詳しくは、[ibmcloud logging session create (ベータ)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#session_create) を参照してください。

```
 ibmcloud logging log-download  [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-o, --output OUTPUT] SESSION_ID

```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
 
  <dt>-o, --output OUTPUT</dt>
  <dd>(オプション) ログがダウンロードされるローカル出力ファイルのパスとファイル名を設定します。 <br>デフォルト値はハイフン (-) です。 <br>ログを標準出力に出力するには、このパラメーターをデフォルト値に設定してください。</dd>

</dl>

**引数**

<dl>
  <dt>SESSION_ID</dt>
  <dd>この値は、ログをダウンロードするときに使用する必要のあるセッションの ID を示します。 <br>**注:** `ibmcloud logging session-create` コマンドには、どのログがダウンロードされるのかを制御するパラメーターがあります。 </dd>
</dl>

**注:** ダウンロードが完了した後に同じコマンドを再実行しても何も実行されません。 同じデータをもう一度ダウンロードするには、別のファイルまたは別のセッションを使用する必要があります。

**例**

Linux システムで、mylogs.gz という名前のファイルにログをダウンロードするには、次のコマンドを実行します。

```
ibmcloud logging log-download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

ユーザー独自の Elastic スタックにログをダウンロードするには、次のコマンドを実行します。

```
ibmcloud logging log-download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
```
{: screen}

以下のファイルは、logstash.conf ファイルの例です。

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

コマンドの使用方法に関する情報を提供します。

```
ibmcloud logging help [command] 
```
{: codeblock}

**パラメーター**

<dl>
<dt>コマンド</dt>
<dd>ヘルプを取得したいコマンド名を設定します。
</dd>
</dl>


**例**

ログの状況を表示するためのコマンドの実行方法に関するヘルプを取得するには、次のコマンドを実行します。

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

スペース、組織、またはアカウントで使用可能なログの保存期間を表示します。 

* 期間は日数で設定されます。
* デフォルト値は **-1** です。 

**注:** デフォルトでは、すべてのログが保管されます。 これらのログは、**delete** コマンドを使用して手動で削除する必要があります。 ログを自動的に削除するには、保存ポリシーを設定します。

```
ibmcloud logging option-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>

</dl>

**例**

ログインしているスペースに対するデフォルトの現在の保存期間を表示するには、次のコマンドを実行します。

```
ibmcloud logging option-show
```
{: screen}




## ibmcloud logging option-update
{: #optionupdate}

スペース、組織、またはアカウントで使用可能なログの保存期間を変更します。 

* 期間は日数で設定されます。
* デフォルト値は **-1** です。 

```
ibmcloud logging option-update [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] <-e,--retention RETENTION_VALUE>
```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) 情報を取得する対象のスペース、組織、またはアカウントの ID をこのフィールドで設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
  
  <dt>-e,--retention RETENTION_VALUE</dt>
  <dd>ログが保持される日数を設定します。 </dd>

</dl>

**例**

ログインしているスペースに対する保存期間を 25 日間に変更するには、次のコマンドを実行します。

```
ibmcloud logging option-update -e 25
```
{: screen}


## ibmcloud logging quota-usage-show
{: #quotausage}

スペース、組織、またはアカウントの割り当て使用量について通知します。 これを使用して、使用量の履歴を取得することもできます。

* 期間は日数で設定されます。
* デフォルト値は **-1** です。 

```
ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s,--history]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
  
  <dt>-s,--history</dt>
  <dd>(オプション) 割り当て使用量についての履歴情報を取得するには、このパラメーターを設定します。</dd>

</dl>

**例**

スペース・ドメインの割り当て使用量の履歴を取得するには、次のコマンドを実行します。

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

新規セッションを作成します。

**注:** 1 つのスペースで最大 30 までの並行セッションを保有できます。 セッションは 1 人のユーザーのために作成されます。 スペース内の複数のユーザーでセッションを共有することはできません。

```
ibmcloud logging session-create [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-T, --time, LOG_TIME]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(オプション) 開始日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、2 週間前に設定されます。
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(オプション) 終了日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、現在日付に設定されます。
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(オプション) ログ・タイプを設定します。 <br>例えば、*syslog* は、ログのタイプの 1 つです。 <br>デフォルト値はアスタリスク (*) に設定されます。 <br>各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: *log_type_1,log_type_2,log_type_3*)。
  </dd>

  <dt>-T, --time, LOG_TIME</dt>
  <dd>(オプション) 特定タイプのログを取得したい時刻を設定します。 </br>有効値は 0 から 23 です。 </br>LOG_TYPE と組み合わせて使う必要があります。
  </dd>

</dl>


**返される値**

<dl>

    <dt>ID</dt>
    <dd>セッション ID。</dd>
	
	<dt>リソース・タイプ</dt>
    <dd>リソース ID。</dd>

    <dt>アクセス時刻</dt>
    <dd>セッションが最後に使用された時刻を示すタイム・スタンプ。</dd>

    <dt>作成時刻</dt>
    <dd>セッションが作成された日時に対応するタイム・スタンプ。</dd>
	
	<dt>開始</dt>
    <dd>ログのフィルター操作に使用される最初の日付を示します。 </dd>

    <dt>終了</dt>
    <dd>ログのフィルター操作に使用される最後の日付を示します。</dd>

    <dt>タイプ</dt>
    <dd>セッションを通してダウンロードされるログ・タイプ。</dd>

</dl>


**例**

2017 年 11 月 13 日のログを含むセッションを作成するには、次のコマンドを実行します。

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

セッション ID で指定されたセッションを削除します。

```
ibmcloud session-delete [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID
```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
 
</dl>

**引数**

<dl>
  <dt>SESSION_ID</dt>
  <dd>削除するアクティブ・セッションの ID。</dd>
</dl>

**例**

セッション ID が *cI6hvAa0KR_tyhjxZZz9Uw==* のセッションを削除するには、次のコマンドを実行します。

```
ibmcloud logging session-delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud logging sessions
{: #session_list}

アクティブ・セッションおよびその ID をリストします。

```
ibmcloud logging sessions [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**パラメーター**

<dl>

  <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。 </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。  </dd>
</dl>

**戻り値**

<dl>	
    <dt>SESSION_ID</dt>
    <dd>アクティブ・セッションの ID。</dd>
	   
    <dt>リソース ID</dt>
    <dd>セッションが有効である対象のリソースの ID。</dd>

    <dt>作成時刻</dt>
    <dd>セッションが作成された日時に対応するタイム・スタンプ。</dd>

    <dt>アクセス時刻</dt>
    <dd>セッションが最後に使用された時刻を示すタイム・スタンプ。</dd>
</dl>
 
**例**

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

単一セッションの状況を表示します。

```
ibmcloud logging session-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] SESSION_ID

```
{: codeblock}

**パラメーター**

<dl>
   <dt>-r,--resource-type RESOURCE_TYPE</dt>
      <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。 </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
      <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。  </dd>
</dl>

**引数**

<dl>
   <dt>SESSION_ID</dt>
   <dd>情報を取得したいアクティブ・セッションの ID。</dd>
</dl>

**例**

セッション ID が *cI6hvAa0KR_tyhjxZZz9Uw==* のセッションの詳細を表示するには、次のコマンドを実行します。

```
ibmcloud logging session-show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}

## ibmcloud logging token-get
{: #tokenget}

ログ・データを {{site.data.keyword.loganalysisshort}} に送信するのに必要なロギング・トークンを返します。

```
ibmcloud logging token-get [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) ログ・データの送信を行う予定のリソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
</dl>


**例**

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

{{site.data.keyword.Bluemix_notm}} スペースまたはアカウントで収集されたログに関する情報を返します。

```
ibmcloud logging log-show [-r,--resource-type RESOURCE_TYPE] [-i,--resource-id RESOURCE_ID] [-s, --start START_DATE] [-e, --end END_DATE] [-t, --type, LOG_TYPE] [-l, --list-type-detail]
```
{: codeblock}

* リソース・タイプが指定されていない場合、コマンドは、ユーザーがログインしているリソースの詳細を返します。
* リソース・タイプを指定する場合は、リソース ID を指定する必要があります。
* このコマンドは、開始日および終了日が指定されていない場合、Log Collection に保管された最近 2 週間分のログに関する情報のみを報告します。

**パラメーター**

<dl>
  <dt>-r,--resource-type RESOURCE_TYPE</dt>
  <dd>(オプション) リソースのタイプを設定します。 有効な値は、*space*、*account*、および *org* です。
  </dd>
  
   <dt>-i,--resource-id RESOURCE_ID</dt>
  <dd>(オプション) このフィールドを、スペース、組織、またはアカウントの ID に設定します。 <br>デフォルトでは、このパラメーターが指定されていない場合、コマンドではユーザーがログインしているリソースの ID が使用されます。 
  </dd>
  
  <dt>-s, --start START_DATE</dt>
  <dd>(オプション) 開始日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、2 週間前に設定されます。
  </dd>
  
  <dt>-e, --end END_DATE</dt>
  <dd>(オプション) 終了日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、現在日付に設定されます。
  </dd>
  
  <dt>-t, --type, LOG_TYPE</dt>
  <dd>(オプション) ログ・タイプを設定します。 <br>例えば、*syslog* は、ログのタイプの 1 つです。 <br>デフォルト値はアスタリスク (*) に設定されます。 <br>各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: *log_type_1,log_type_2,log_type_3*)。
  </dd>
  
  <dt>-l, --list-type-detail</dt>
  <dd>(オプション) 各ログ・タイプを個々にリストするには、このパラメーターを設定します。
  </dd>
</dl>


**例**

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
