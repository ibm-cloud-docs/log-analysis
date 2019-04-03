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

# Kibana ログ・フォーマット
{: #kibana_formats}

ログ項目ごとに異なるフィールドを「*Discover*」ページで表示するように Kibana を構成できます。
{:shortdesc}



## Cloud Foundry アプリケーションの Kibana ログ・フォーマット
{: #kibana_log_format_cf}

各ログ項目の以下のフィールドを「*Discover*」ページで表示するように Kibana を構成できます。

| フィールド | 説明 |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> ログに記録されたイベントの時刻。 <br> タイム・スタンプは、ミリ秒単位まで定義されます。 |
| @version | イベントのバージョン。 |
| ALCH_TENANT_ID | {{site.data.keyword.Bluemix_notm}} スペースの ID。 |
| \_id | ログ文書の固有 ID。 |
| \_index | ログ項目のインデックス。 |
| \_type | ログのタイプ (例: *syslog*)。 |
| app_name | アプリケーションの名前。 |
| application_id | アプリケーションの固有 ID。 |
| ホスト (host) | ログ・データを生成したアプリケーションの名前。 |
| instance_id | ログ・データを生成したアプリケーション・インスタンスのインスタンス ID。 |
| loglevel | ログに記録されたイベントの重大度。 |
| message | コンポーネントによって発行されたメッセージ。 <br> メッセージは、コンテキストによって異なります。 |
| message_type | ログ・メッセージが書き込まれたストリーム。 <br> * **OUT** は、STDOUT ストリームを指します。 <br> * **ERR** は、STDERR ストリームを指します。 |
| org_id | {{site.data.keyword.Bluemix_notm}} 組織の固有 ID。 |
| org_name | アプリがステージ化されている {{site.data.keyword.Bluemix_notm}} 組織の名前。 |
| origin | イベントの発生元コンポーネント。 |
| source_id | ログを生成したコンポーネント。 <br> 各コンポーネントからのログは、以下のリストのとおりです。 <br> * **API**: アプリ状況の変更を要求する API 呼び出しへの応答がログに記録されます。 <br> * **APP**: アプリからの応答がログに記録されます。 <br> * **CELL**: アプリの開始、停止、またはクラッシュがいつ起こったのかを示す Diego セルからの応答がログに記録されます。 <br> * **LGR**: ロギング処理での問題を示す Loggregator からの応答がログに記録されます。 <br> * **RTR**: ルーターが HTTP 要求をアプリに転送したときのルーターからの応答がログに記録されます。 <br> * **SSH**: ユーザーが `cf ssh` コマンドを使用してアプリ・コンテナーにアクセスしたときの Diego セルからの応答がログに記録されます。 <br> * **STG**: アプリがステージ化または再ステージ化されたときの Diego セルまたは Droplet Execution Agent からの応答がログに記録されます。 |
| space_name | アプリがステージ化されている {{site.data.keyword.Bluemix_notm}} スペースの名前。 |
| timestamp | ログに記録されたイベントの時刻。 タイム・スタンプは、ミリ秒単位まで定義されます。 |
{: caption="表 1. CF アプリ用のフィールド" caption-side="top"}



## Kubernetes クラスターにデプロイされた Docker コンテナーの Kibana ログ・フォーマット
{: #kibana_log_format_containers_kubernetes}

各ログ項目の以下のフィールドを「*Discover*」ページで表示するように Kibana を構成できます。 これらのフィールドは、{{site.data.keyword.IBM}} によって設定され、ユーザーのメッセージ・データを含んでいます。 

| フィールド | 説明 | その他の情報 |
|-------|-------------|---------------------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> ログに記録されたイベントの時刻。 <br> タイム・スタンプは、ミリ秒単位まで定義されます。 | |
| @version | イベントのバージョン。 | |
| ALCH_TENANT_ID | {{site.data.keyword.Bluemix_notm}} スペースの ID。 | |
| \_id | ログ文書の固有 ID。 | |
| \_index | ログ項目のインデックス。 | |
| \_score |  |  |
| \_type | ログのタイプ (例、*logs*)。 | |
| crn_str | ログのソースについての情報。 | デフォルトでは、このフィールドは {{site.data.keyword.IBM_notm}} によって設定されます。 <br> **注:** 有効な JSON フォーマットでログ・メッセージが送信され、フィールドの 1 つが `crn` という名前である場合、フィールドの値はメッセージ中に設定されている値で上書きされます。  |  
| docker.container_id_str | ポッド内で実行されているコンテナーの GUID。 | |
| ibm-containers.account_str | {{site.data.keyword.Bluemix_notm}} アカウントの GUID。  |  |
| ibm-containers.cluster_id_str | Kubernetes クラスターの GUID。  |  |
| ibm-containers.cluster_type_str |  | {{site.data.keyword.IBM_notm}} 内部使用のための予約済みの値。 |
| ibm-containers.region_str | {{site.data.keyword.Bluemix_notm}} の地域。  |  |
| kubernetes.container_name_str | アプリがデプロイされたコンテナーの名前。  |  |
| kubernetes.host | コンテナーが実行されているワーカーのパブリック IP アドレス。 |  |
| kubernetes.labels.*example_label_name*\_str | ポッドなどの Kubernetes オブジェクトに付加するキーと値のペア。 | Kubernetes オブジェクトに付加する各ラベルが、Kibana で表示されるログ項目内で 1 つのフィールドとしてリストされます。 <br> ラベルはなくてもよく、複数あってもかまいません。 |
| kubernetes.namespace_name_str | コンテナーがデプロイされた Kubernetes 名前空間。 |  |
| kubernetes.pod_id_str | コンテナーがデプロイされたポッドの GUID。 |  |
| kubernetes.pod_name_str | ポッドの名前。 |  |
| message | 完全なメッセージ。 | 有効な JSON フォーマットのメッセージを送信すると、Kibana では各フィールドが個別に構文解析されて表示されます。  |
| stream_str |  | {{site.data.keyword.IBM_notm}} 内部使用のための予約済みの値。 |
|tag_str |  | {{site.data.keyword.IBM_notm}} 内部使用のための予約済みの値。 |
{: caption="表 3. Docker コンテナー用のフィールド" caption-side="top"}


## Message Hub の Kibana ログ・フォーマット
{: #kibana_log_format_messagehub}

各ログ項目の以下のフィールドを「*Discover*」ページで表示するように Kibana を構成できます。

| フィールド | 説明 |
|-------|-------------|
| @timestamp | `yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> ログに記録されたイベントの時刻。 <br> タイム・スタンプは、ミリ秒単位まで定義されます。 |
| @version | イベントのバージョン。 |
| ALCH_TENANT_ID | {{site.data.keyword.Bluemix_notm}} スペースの ID。 |
| \_id | ログ文書の固有 ID。 |
| \_index | ログ項目のインデックス。 |
| \_type | ログのタイプ (例: *syslog*)。 |
| loglevel | ログに記録するイベントの重大度 (例えば、**Info**)。 |
| module | このフィールドは、**MessageHub** に設定されます。 |
{: caption="表 4. Message Hub イベント用のフィールド" caption-side="top"}

ログ項目の例:

```
March 8th 2017, 17:15:16.454	

message:
    Creating topic ABC
@version:
    1
@timestamp:
    March 8th 2017, 17:15:16.454
loglevel:
    Info
module:
    MessageHub
ALCH_TENANT_ID:
    3d8d2eae-f3f0-44f6-9717-126113a00b51
&#95;id:
    AVqu6vJl1zcfr8KYMI95
&#95;type:
    logs
&#95;index:
    logstash-2017.03.08
```
{: screen}


