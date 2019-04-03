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

# IBM Cloud Log Analysis CLI (CF プラグイン)
{: #logging_cli}

{{site.data.keyword.loganalysislong}} CLI は、{{site.data.keyword.Bluemix}} 組織のスペース内で稼働しているクラウド・リソースのログを管理するためのプラグインです。
{: shortdesc}

**前提条件**
* ロギング・コマンドを実行する前に、`ibmcloud login` コマンドを使用して {{site.data.keyword.Bluemix_notm}} にログインし、{{site.data.keyword.Bluemix_short}} アクセス・トークンを生成して、セッションを認証します。 詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

{{site.data.keyword.loganalysisshort}} CLI の使用方法については、『[ログの管理](/docs/services/CloudLogAnalysis/log_analysis_ov.html#log_analysis_ov)』を参照してください。

<table>
  <caption>ログを管理するためのコマンド</caption>
  <tr>
    <th>コマンド</th>
    <th>いつ使用するか</th>
  </tr>
  <tr>
    <td>[ibmcloud cf logging](#base)</td>
    <td>この CLI についての情報 (バージョンまたはコマンド・リストなど) を取得するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging auth](#auth)</td>
    <td>{{site.data.keyword.loganalysisshort}} サービスにログを送信するために使用できるロギング・トークンを取得するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging delete](#delete)</td>
    <td>Log Collection に保管されたログを削除するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging download (ベータ)](#download)</td>
    <td>Log Collection からローカル・ファイルにログをダウンロードするか、または、別のプログラム (例えば Elastic スタック) にログをパイプするには、このコマンドを使用します。 </td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging help](#help)</td>
    <td>この CLI の使用方法に関するヘルプ、およびすべてのコマンドのリストを取得するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging option](#option)</td>
    <td>スペースまたはアカウントで使用可能なログの保存期間を表示または設定するには、このコマンドを使用します。</td>
  </tr>
  <tr>
    <td>[ibmcloud cf logging session create (ベータ)](#session_create1)</td>
    <td>新規セッションを作成するには、このコマンドを使用します。</td>
  <tr>
  <tr>
    <td>[ibmcloud cf logging session delete (ベータ)](#session_delete1)</td>
    <td>セッションを削除するには、このコマンドを使用します。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session list (ベータ)](#session_list1)</td>
    <td>アクティブ・セッションおよびその ID をリストするには、このコマンドを使用します。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging session show (ベータ)](#session_show1)</td>
    <td>単一セッションの状況を表示するには、このコマンドを使用します。</td>
  <tr>  
  <tr>
    <td>[ibmcloud cf logging status](#status1)</td>
    <td>スペースまたはアカウントで収集されたログに関する情報を取得するには、このコマンドを使用します。</td>
  </tr>
  </table>


## ibmcloud cf logging
{: #base1}

CLI のバージョンおよび CLI の使用方法についての情報を提供します。

```
ibmcloud cf logging [parameters]
```
{: codeblock}

**パラメーター**

<dl>
<dt>--help、-h</dt>
<dd>コマンドのリストを表示するか、または 1 つのコマンドのヘルプを取得するには、このパラメーターを設定します。
</dd>

<dt>--version、-v</dt>
<dd>CLI のバージョンを表示するには、このパラメーターを設定します。</dd>
</dl>

**例**

コマンドのリストを取得するには、次のコマンドを実行します。

```
ibmcloud cf logging --help
```
{: codeblock}

CLI のバージョンを取得するには、次のコマンドを実行します。

```
ibmcloud cf logging --version
```
{: codeblock}


## ibmcloud cf logging auth
{: #auth}

{{site.data.keyword.loganalysisshort}} サービスにログを送信するために使用できるロギング・トークンを返します。 

**注:** このトークンは期限切れになりません。

```
ibmcloud cf logging auth
```
{: codeblock}

**返される内容**

<dl>
  <dt>ロギング・トークン</dt>
  <dd>例えば、`jec8BmipiEZc` などです。
  </dd>
  
  <dt>組織 ID</dt>
  <dd>ログインした {{site.data.keyword.Bluemix_notm}} 組織の GUID。
  </dd>
  
  <dt>スペース ID</dt>
  <dd>ログインした組織内のスペースの GUID。
  </dd>
</dl>

## ibmcloud cf logging delete
{: #delete2}

Log Collection に保管されたログを削除します。

```
ibmcloud cf logging delete [parameters]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>--start value、-s value</dt>
  <dd>(オプション) 開始日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、2 週間前に設定されます。
  </dd>
  
  <dt>--end value、-e value</dt>
  <dd>(オプション) 終了日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。 <br>日付の UTC フォーマットは **YYYY-MM-DD** です (例: `2006-01-02`)。 <br>デフォルト値は、現在日付に設定されます。
  </dd>
  
  <dt>--type value、-t value</dt>
  <dd>(オプション) ログ・タイプを設定します。 <br>例えば、*syslog* は、ログのタイプの 1 つです。 <br>デフォルト値は、**\*** に設定されます。 <br>各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: **log_type_1,log_type_2,log_type_3*)。
  </dd>
  
  <dt>--at-account-level、-a </dt>
  <dd>(オプション) 提供されるログ情報のスコープをアカウント・レベルに設定します。 <br>このパラメーターが指定されていない場合、デフォルト値は、現行スペースのみについてのログ情報を提供するように設定されます。
  </dd>
</dl>

**例**

2017 年 5 月 25 日のタイプ *linux_syslog* のログを削除するには、次のコマンドを実行します。
```
ibmcloud cf logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
```
{: codeblock}



## ibmcloud cf logging download (ベータ)
{: #download4}

Log Collection からローカル・ファイルにログをダウンロードするか、別のプログラム (Elastic スタックなど) にログをパイプします。 

**注:** ファイルをダウンロードするには、まずセッションを作成する必要があります。 セッションは、日付範囲、ログ・タイプ、およびアカウント・タイプに基づいて、ダウンロードするログを定義します。 ログのダウンロードは、1 つのセッションのコンテキスト内で行います。 詳しくは、[ibmcloud cf logging session create (ベータ)](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) を参照してください。

```
ibmcloud cf logging download [parameters] [arguments]
```
{: codeblock}

**パラメーター**

<dl>
<dt>--output value、-o value</dt>
<dd>(オプション) ログがダウンロードされるローカル出力ファイルのパスとファイル名を設定します。 <br>デフォルト値はハイフン (-) です。 <br>ログを標準出力に出力するには、このパラメーターをデフォルト値に設定してください。</dd>
</dl>

**引数**

<dl>
<dt>セッション ID</dt>
<dd>`ibmcloud cf logging session create` コマンドの実行時に取得したセッション ID 値に設定します。 この値は、ログをダウンロードするときに使用するセッションを指示します。 <br>**注:** `ibmcloud cf logging session create` コマンドには、どのログがダウンロードされるのかを制御するパラメーターがあります。 </dd>
</dl>

**注:** ダウンロードが完了した後に同じコマンドを再実行しても何も実行されません。 同じデータをもう一度ダウンロードするには、別のファイルまたは別のセッションを使用する必要があります。

**例**

Linux システムで、mylogs.gz という名前のファイルにログをダウンロードするには、次のコマンドを実行します。

```
ibmcloud cf logging download -o mylogs.gz guBeZTIuYtreOPi-WMnbUg==
```
{: screen}

ユーザー独自の Elastic スタックにログをダウンロードするには、次のコマンドを実行します。

```
ibmcloud cf logging download guBeZTIuYtreOPi-WMnbUg== | gunzip | logstash -f logstash.conf
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


## ibmcloud cf logging help
{: #help1}

コマンドの使用方法に関する情報を提供します。

```
ibmcloud cf logging help [command]
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
ibmcloud cf logging help status
```
{: codeblock}


## ibmcloud cf logging option
{: #option}

スペースまたはアカウントで使用可能なログの保存期間を表示または変更します。 

* 期間は日数で設定されます。
* デフォルト値は **-1** です。 

**注:** デフォルトでは、すべてのログが保管されます。 これらのログは、**delete** コマンドを使用して手動で削除する必要があります。 ログを自動的に削除するには、保存ポリシーを設定します。

```
ibmcloud cf logging option [parameters]
```
{: codeblock}

**パラメーター**

<dl>
<dt>--retention value、-r value</dt>
<dd>(オプション) 保存日数を設定します。 <br> デフォルト値は *-1* 日です。</dd>

<dt>--at-account-level、-a </dt>
  <dd>(オプション) スコープをアカウント・レベルに設定します。 <br>このパラメーターが指定されていない場合、デフォルト値は、現行スペース (`ibmcloud cf login` コマンドを使用してログインしたスペース) では *-1* に設定されます。
  </dd>
</dl>

**例**

ログインしているスペースに対するデフォルトの現在の保存期間を表示するには、次のコマンドを実行します。

```
ibmcloud cf logging option
```
{: codeblock}

出力は次のとおりです。

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen}


ログインしているスペースに対する保存期間を 25 日間に変更するには、次のコマンドを実行します。

```
ibmcloud cf logging option -r 25
```
{: codeblock}

出力は次のとおりです。

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-ibmcloud cfgh436902a3 |        25 |
+--------------------------------------+-----------+
```
{: screen}


## ibmcloud cf logging session create (ベータ)
{: #session_create1}

新規セッションを作成します。

**注:** 1 つのスペースで最大 30 までの並行セッションを保有できます。 セッションは 1 人のユーザーのために作成されます。 スペース内の複数のユーザーでセッションを共有することはできません。

```
ibmcloud cf logging session create [parameters]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>--start value、-s value</dt>
  <dd>(オプション) 開始日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、2 週間前に設定されます。
  </dd>
  
  <dt>--end value、-e value</dt>
  <dd>(オプション) 終了日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、現在日付に設定されます。
  </dd>
  
  <dt>--type value、-t value</dt>
  <dd>(オプション) ログ・タイプを設定します。 <br>例えば、*syslog* は、ログのタイプの 1 つです。 <br>デフォルト値はアスタリスク (*) に設定されます。 <br>各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: *log_type_1,log_type_2,log_type_3*)。
  </dd>
  
  <dt>--at-account-level、-a </dt>
  <dd>(オプション) スコープをアカウント・レベルに設定します。 <br>このパラメーターが指定されていない場合、デフォルト値は、現行スペース (つまり、`ibmcloud cf login` コマンドを使用してログインしたスペース) のみに設定されます。
  </dd>
</dl>

**返される値**

<dl>
<dt>アクセス時刻</dt>
<dd>セッションが最後に使用された時刻を示すタイム・スタンプ。</dd>

<dt>作成時刻</dt>
<dd>セッションが作成された日時に対応するタイム・スタンプ。</dd>

<dt>日付範囲</dt>
<dd>ログのフィルタリングに使用される日付を示します。 この日付範囲内で識別されたログが、セッションを通した管理に使用可能です。</dd>

<dt>ID</dt>
<dd>セッション ID。</dd>

<dt>スペース</dt>
<dd>セッションがアクティブであるスペースの ID。</dd>

<dt>タイプ・アカウント</dt>
<dd>セッションを通してダウンロードされるログ・タイプ。</dd>

<dt>ユーザー名</dt>
<dd>セッションを作成したユーザーの {{site.data.keyword.IBM_notm}} ID。</dd>
</dl>


**例**

2017 年 5 月 20 日から 2017 年 5 月 26 日までの間にあり、ログ・タイプが *log* のログを含むセッションを作成するには、次のコマンドを実行します。

```
ibmcloud cf logging session create -s 2017-05-20 -e 2017-05-26 -t log
```
{: screen}


## ibmcloud cf logging session delete (ベータ)
{: #session_delete1}

セッション ID で指定されたセッションを削除します。

```
ibmcloud cf logging session delete [arguments]
```
{: codeblock}

**引数**

<dl>
<dt>セッション ID</dt>
<dd>削除するセッションの ID。 <br>`ibmcloud cf logging session list` コマンドを使用して、すべてのアクティブ・セッションの ID を取得できます。</dd>
</dl>

**例**

セッション ID が *cI6hvAa0KR_tyhjxZZz9Uw==* のセッションを削除するには、次のコマンドを実行します。

```
ibmcloud cf logging session delete cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}



## ibmcloud cf logging session list (ベータ)
{: #session_list1}

アクティブ・セッションおよびその ID をリストします。

```
ibmcloud cf logging session list 
```
{: codeblock}

**返される値**

<dl>
<dt>ID</dt>
<dd>セッション ID。</dd>

<dt>SPACE</dt>
<dd>セッションがアクティブであるスペースの ID。</dd>

<dt>USERNAME</dt>
<dd>セッションを作成したユーザーの {{site.data.keyword.IBM_notm}} ID。</dd>

<dt>CREATE-TIME</dt>
<dd>セッションが作成された日時に対応するタイム・スタンプ。</dd>

<dt>ACCESS-TIME</dt>
<dd>セッションが最後に使用された時刻を示すタイム・スタンプ。</dd>
</dl>
 

## ibmcloud cf logging session show (ベータ)
{: #session_show1}

単一セッションの状況を表示します。

```
ibmcloud cf logging session show [arguments]
```
{: codeblock}

**引数**

<dl>
<dt>セッション ID</dt>
<dd>情報を取得したいアクティブ・セッションの ID。</dd>
</dl>

**返される値**

<dl>
<dt>アクセス時刻</dt>
<dd></dd>

<dt>作成時刻</dt>
<dd>セッションが作成された日時に対応するタイム・スタンプ。</dd>

<dt>日付範囲</dt>
<dd>ログのフィルタリングに使用される日付を示します。 この日付範囲内で識別されたログが、セッションを通した管理に使用可能です。</dd>

<dt>ID</dt>
<dd>セッション ID。</dd>

<dt>スペース</dt>
<dd>セッションがアクティブであるスペースの ID。</dd>

<dt>タイプ・アカウント</dt>
<dd>セッションを通してダウンロードされるログ・タイプ。</dd>

<dt>ユーザー名</dt>
<dd>セッションを作成したユーザーの {{site.data.keyword.IBM_notm}} ID。</dd>
</dl>

**例**

セッション ID が *cI6hvAa0KR_tyhjxZZz9Uw==* のセッションの詳細を表示するには、次のコマンドを実行します。

```
ibmcloud cf logging session show cI6hvAa0KR_tyhjxZZz9Uw==
```
{: screen}


## ibmcloud cf logging status
{: #status1}

スペースまたはアカウントで収集されたログに関する情報を返します。

```
ibmcloud cf logging status [parameters]
```
{: codeblock}

**パラメーター**

<dl>
  <dt>--start value、-s value</dt>
  <dd>(オプション) 開始日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、2 週間前に設定されます。
  </dd>
  
  <dt>--end value、-e value</dt>
  <dd>(オプション) 終了日を協定世界時 (UTC) *YYYY-MM-DD* で設定します。例えば、`2006-01-02` です。 <br>デフォルト値は、現在日付に設定されます。
  </dd>
  
  <dt>--type value、-t value</dt>
  <dd>(オプション) ログ・タイプを設定します。 <br>例えば、*syslog* は、ログのタイプの 1 つです。 <br>デフォルト値はアスタリスク (*) に設定されます。 <br>各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: *log_type_1,log_type_2,log_type_3*)。
  </dd>
  
  <dt>--at-account-level、-a </dt>
  <dd>(オプション) スコープをアカウント・レベルに設定します。 <br> **注:** アカウント情報を取得するには、この値を設定します。 <br>このパラメーターが指定されていない場合、デフォルト値は、現行スペース (つまり、`ibmcloud cf login` コマンドを使用してログインしたスペース) のみに設定されます。
  </dd>
  
  <dt>--list-type-detail、-l</dt>
  <dd>(オプション) 日ごとにログ・タイプの小計をリストするには、このパラメーターを設定します。
  </dd>
</dl>

**注:** `ibmcloud cf logging status` コマンドは、開始日および終了日が指定されていない場合、Log Collection に保管された最近 2 週間分のログのみを報告します。


