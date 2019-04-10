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

 
# ログの送信
{: #ingest}

ログ・データを {{site.data.keyword.la_full_notm}} インスタンスに送信できます。 
{:shortdesc}

プログラムでログを送信するには、以下の手順を実行します。

## ステップ 1. 取り込み API 鍵の取得 
{: #ingest_step1}

**注:** このステップを完了するには、{{site.data.keyword.la_full_notm}} インスタンスまたはサービスに対する**管理者**の役割がなければなりません。 詳しくは、[LogDNA でログを管理しアラートを構成するための許可の付与](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)を参照してください。

取り込み鍵を取得するには、以下の手順を実行します。
    
1. {{site.data.keyword.la_full_notm}} Web UI ブラウザーを起動します。 詳しくは、[{{site.data.keyword.la_full_notm}} Web UI への移動](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)を参照してください。

2. **「構成」**アイコン ![構成アイコン](images/admin.png) を選択します。 次に、**「組織」**を選択します。 

3. **「API キー」**を選択します。

    作成された取り込み鍵が表示されます。 

4. 既存の取り込み鍵を使用するか、**「取り込み鍵の生成 (Generate Ingestion Key)」**をクリックして新規に作成します。

    リストに新しい鍵が追加されます。 その鍵をコピーします。


## ステップ 2. ログの送信
{: #ingest_step2}

ログを送信するには、以下の cURL コマンドを実行します。

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

説明 

* ENDPOINT は、サービスのエントリー・ポイントを表します。 地域ごとに URL は異なります。
* QUERY_PARAMETERS は、取り込み要求に適用されるフィルタリング基準を定義するパラメーターです。
* LOG_LINES は、送信するログ行の組み合わせについて記述します。 これはオブジェクトの配列として定義されます。
* INGESTION_KEY は、前の手順で作成したキーです。

以下の表は、地域ごとのエンドポイントを示します。

| 地域         | エンドポイント                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="地域別のエンドポイント" caption-side="top"} 


以下の表に、照会パラメーターをリストします。

| 照会パラメーター | タイプ       | 状況     | 説明 |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | 必須   | ソースのホスト名。 |
| `mac`           | `string`     | オプション   | ホスト・コンピューターのネットワーク mac アドレス。    |
| `ip`            | `string`     | オプション   | ホスト・コンピューターのローカル IP アドレス。  | 
| `now`           | `date-time`  | オプション   | 要求時のソース UNIX タイム・スタンプ (ミリ秒)。 時間ドリフトの計算に使用されます。|
| `tags`          | `string`     | オプション   | ホストを動的にグループ化するために使用されるタグ。 |
{: caption="照会パラメーター" caption-side="top"} 



以下の表に、ログ行ごとに必要なデータをリストします。

| パラメーター     | タイプ       | 説明                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | ログ項目の記録時の UNIX タイム・スタンプ (ミリ秒を含む)。       | 
| `line`           | `string`     | ログ行のテキスト。                                     |
| `app`            | `string`     | ログ行を生成するアプリケーションの名前。  |
| `level`          | `string`     | レベルの値を設定します。 例えば、このパラメーターのサンプル値は `INFO`、`WARNING`、`ERROR` です。 |
| `meta`           |            | このフィールドは、ログ行に関連付けられたカスタム情報用に予約済みです。 API 呼び出しにメタデータを追加するには、行オブジェクトの下にメタ・フィールドを指定します。 メタデータは、その行のコンテキスト内に示されます。                      |
{: caption="行オブジェクト・フィールド" caption-side="top"} 

例えば、以下のサンプルは、取り込むログ行の JSON を示しています。

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


## 例
{: #ingest_example}

以下のサンプルは、{{site.data.keyword.la_full_notm}} サービスのインスタンスに 1 つのログ行を送信する cURL コマンドを示しています。 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

