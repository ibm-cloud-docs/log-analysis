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

# ログのダウンロード
{: #downloading_logs1}

ログをローカル・ファイルにダウンロードしたり、データを別のプログラムにパイプしたりできます。 ログのダウンロードは、1 つのセッションのコンテキスト内で行います。 どのログがダウンロードされるのかをセッションが指定します。 ログのダウンロードが中断された場合、セッションは中断した箇所からのダウンロードの再開を可能にします。 ダウンロードが完了した後、セッションを削除する必要があります。
{:shortdesc}

{{site.data.keyword.Bluemix_notm}} スペースで使用可能なログ・データをローカル・ファイルにダウンロードするには、以下のステップを実行します。

## ステップ 1: IBM Cloud にログインする

{{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

## ステップ 2: 使用可能なログを識別する
{: #step31}

1. `ibmcloud cf logging status` コマンドを使用して、最近 2 週間の使用可能なログを表示します。 次のコマンドを実行します。

    ```
    ibmcloud cf logging status
    ```
    {: codeblock}
    
    例えば、このコマンドの実行による出力は以下のようになります。
    
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

    **注:** {{site.data.keyword.loganalysisshort}} サービスは、協定世界時 (UTC) を使用するグローバル・サービスです。 日付は UTC 日付で定義されます。 特定の現地時間の 1 日のログを取得するために、複数の UTC 日のダウンロードが必要になることがあります。


## ステップ 3: セッションを作成する
{: #step32}

ダウンロードに使用可能なログ・データのスコープを定義するため、および、ダウンロードの状況を保持するために、セッションが必要です。 

セッションを作成するには、コマンド [cf logging session create](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_create1) を使用します。 オプションで、セッションを作成するときに、ログの開始日、終了日、およびタイプを指定することができます。  

* 開始日および終了日を指定すると、セッションはそれらの日付の間 (開始日と終了日を含む) のログへのアクセスを提供します。 
* ログのタイプ (**-t**) を指定すると、セッションは特定タイプのログへのアクセスを提供します。 これは、ログのうち興味のある小さなサブセットのみにセッションのスコープを限定できるため、大量のログを管理する場合に重要な機能です。

**注:** セッションごとに、最長 15 日間分のログがダウンロードできます。

タイプが *log* のログをダウンロードするために使用されるセッションを作成するには、次のコマンドを実行します。

```
ibmcloud cf logging session create -t log
```
{: codeblock}

セッションは、以下の情報を返します。

* ダウンロードされる日付範囲。 デフォルトは、現在の UTC 日付です。
* ダウンロードされるログ・タイプ。 デフォルトでは、セッション作成時に指定した期間の使用可能なすべてのログ・タイプが含まれます。 
* アカウント全体を含めるのか、現行スペースのみを含めるのかに関する情報。 デフォルトでは、ログインしたスペースのログが取得されます。
* ログのダウンロードに必要なセッション ID。

以下に例を示します。

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

**ヒント:** アクティブ・セッションのリストを表示するには、コマンド [cf logging session list](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_list1) を実行します。

## ステップ 4: ログ・データをファイルにダウンロードする
{: #step42}

セッション・パラメーターで指定されたログをダウンロードするには、次のコマンドを実行します。

```
ibmcloud cf logging download -o Log_File_Name Session_ID
```
{: codeblock}

各部分の説明:

* Log_File_Name は、出力ファイルの名前です。
* Session_ID は、セッションの GUID です。 この値は前のステップで取得します。

以下に例を示します。

```
ibmcloud cf logging download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

進行状況表示は、ログがダウンロードされるに従って 0% から 100% に進んでいきます。

**注:** 

* ダウンロードされたデータのフォーマットは、圧縮 JSON です。 .gz ファイルを unzip してから開くと、データは JSON フォーマットで表示されます。 
* 圧縮 JSON は、ElasticSearch または Logstash による取り込みに適しています。 -o が指定されていない場合、データは stdout にストリームされるので、それを直接 ELK スタックにパイプすることができます。
* JSON を構文解析できる任意のプログラムでデータを処理することもできます。 

## ステップ 5: セッションを削除する
{: #step51}

ダウンロードが完了した後、[cf logging session delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#session_delete1) コマンドを使用してセッションを削除する必要があります。 

セッションを削除するには、次のコマンドを実行します。

```
ibmcloud cf logging session delete Session_ID
```
{: codeblock}

ここで、Session_ID は、前のステップで作成したセッションの GUID です。

以下に例を示します。

```
ibmcloud cf logging session delete -jshdjsunelsssr4566722==
+---------+------------------------+
|  NAME   |         VALUE          |
+---------+------------------------+
| Message | Delete session success |
+---------+------------------------+
```
{: screen}




