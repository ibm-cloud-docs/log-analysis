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

 
# ローカル・ファイルへのログのエクスポート
{: #export}

ログ・データを JSONL 形式で {{site.data.keyword.la_full_notm}} インスタンスからローカル・ファイル内にエクスポートできます。 ログをプログラマチックにエクスポートするか。 IBM Log Analysis Web UI からエクスポートすることができます。 
{:shortdesc}

ログ・データをエクスポートする際には、以下の情報を考慮してください。
* ログ項目の集合をエクスポートします。 エクスポートしようとしているデータ集合を定義する際に、フィルターと検索を適用できます。 時刻範囲を指定することもできます。 
* Web UI からログをエクスポートする場合は、ご自分の E メール・アドレスに、当該データが含まれる圧縮ファイルへのリンクがある E メールが送信されます。 このデータを取得するには、リンクをクリックし、圧縮ファイルをダウンロードしなければなりません。
* ログをプログラマチックにエクスポートする際には、E メールの送信か、端末へのログのストリーミングを選択できます。
* エクスポートしようとしているデータが含まれる圧縮ログ・ファイルは、最大 48 時間入手可能です。 
* エクスポートできる最大行数は 10,000 です。



## Web UI からログをエクスポートする
{: #ui}

ログ・データをエクスポートするには、以下のステップを実行します。

1. **「ビュー」**アイコン ![構成アイコン](images/views.png) をクリックします。
2. **「すべて (Everything)」**または 1 つのビューを選択します。
3. エクスポートしようとしているログ項目が表示されるまで、時間フレーム、フィルター、検索基準を適用します。
4. **「すべて (Everything)」**ビューから開始している場合は、**「保存されていないビュー (Unsaved View)」**をクリックします。 前のステップでビューを選択した場合は、ビュー名をクリックします。
5. `「行のエクスポート (Export lines)」`を選択します。 新しいウィンドウが開きます。
6. 時刻範囲を確認します。 変更する必要がある場合は、*「エクスポート対象の時刻範囲の変更 (Change the Time Range for export)」*フィールド内で事前定義された時刻範囲をクリックします。
7. エクスポート要求が行の制限を超える場合は、**「新しい行を優先 (Prefer newer lines)」**または**「古い行を優先 (Prefer older lines)」**を選択します。
8. E メールを確認します。 **LogDNA** から、エクスポートされた行をダウンロードするためのリンクがある E メールを受信します。


## API を使用してログをプログラマチックにエクスポートする
{: #api}

ログをプログラマチックにエクスポートするには、以下のステップを実行します。

1. サービス・キーを生成します。 

    **注:** このステップを完了するには、{{site.data.keyword.la_full_notm}} インスタンスまたはサービスに対する**管理者**の役割がなければなりません。 詳しくは、[LogDNA でログを管理しアラートを構成するための許可の付与](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)を参照してください。

    1. {{site.data.keyword.la_full_notm}} Web UI ブラウザーを起動します。 詳しくは、[{{site.data.keyword.la_full_notm}} Web UI への移動](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)を参照してください。

    2. **「構成」**アイコン ![構成アイコン](images/admin.png) を選択します。 次に、**「組織」**を選択します。 

    3. **「API キー」**を選択します。

        作成したサービス・キーが表示されます。 

    4. **「サービス・キーの生成 (Generate Service Key)」**をクリックします。

        リストに新しい鍵が追加されます。 このキーをコピーします。

2. ログをエクスポートします。 次の cURL コマンドを実行します。

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    説明 

    * ENDPOINT は、サービスのエントリー・ポイントを表します。 地域ごとに URL は異なります。
    * QUERY_PARAMETERS は、エクスポート要求に適用されるフィルター基準を定義するパラメーターです。
    * SERVICE_KEY は、前のステップで作成したサービス・キーです。

以下の表は、地域ごとのエンドポイントを示します。

| 地域         | エンドポイント                                             | 
|----------------|------------------------------------------------------|
| `Us-south`       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="地域別のエンドポイント" caption-side="top"} 


以下の表に、設定できる照会パラメーターをリストします。

| 照会パラメーター | タイプ       | 状況     | 説明 |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | 必須   | 開始時刻。 秒単位かミリ秒単位の UNIX タイム・スタンプとして設定します。 |
| `to`        | `int32`      | 必須   | 終了時刻。 秒単位かミリ秒単位の UNIX タイム・スタンプとして設定します。    |
| `size`      | `string`     | オプション   | エクスポートに組み込むログ行の数。  | 
| `hosts`     | `string`     | オプション   | ホストのコンマ区切りリスト。 |
| `apps`      | `string`     | オプション   | アプリケーションのコンマ区切りリスト。 |
| `levels`    | `string`     | オプション   | ログ・レベルのコンマ区切りリスト。 |
| `query`     | `string`     | オプション   | 検索照会。 詳しくは、[検索ログ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)を参照してください。 |
| `prefer`    | `string`     | オプション   | エクスポートするログ行を定義します。 有効な値は `head` (最初のログ行) と `tail` (最後のログ行) です。 指定されていない場合、デフォルトの tail になります。  |
| `email`     | `string`     | オプション   | エクスポート内容をダウンロードできるリンクがある E メールを指定します。 デフォルトでは、ログ行はストリーミングされます。|
| `emailSubject` | `string`     | オプション   | E メールの件名を設定するために使用します。 </br>スペースを表すには、`%20` を使用します。例えば、サンプル値は `Export%20logs` です。 |
{: caption="照会パラメーター" caption-side="top"} 

例えば、ログ行を端末にストリーミングするには、以下のコマンドを実行できます。

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

エクスポートで指定されているログ行をダウンロードするためのリンクがある E メールを送信するには、以下のコマンドを実行できます。

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


件名がカスタマイズされた E メールを送信するには、以下のコマンドを実行できます。

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

