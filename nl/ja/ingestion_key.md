---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# 取り込み鍵の処理
{: #ingestion_key}

取り込み鍵は、LogDNA エージェントを構成して {{site.data.keyword.cloud_notm}} 内の {{site.data.keyword.la_full_notm}} インスタンスにログを正常に転送するために使用する必要のあるセキュリティー・キーです。 インスタンスをプロビジョンすると、取り込み鍵を自動的に取得します。 代わりに、インスタンスのためのサービス ID を作成して取り込み鍵を取得することもできます。 
{:shortdesc}

**注:** 

* {{site.data.keyword.la_full_notm}} Web UI によって取り込み鍵を処理するには、{{site.data.keyword.la_full_notm}} サービスに対して、プラットフォーム役割の**ビューアー**とサービス役割の**管理者**を持つ IAM ポリシーが必要です。 
* {{site.data.keyword.cloud_notm}} UI によって取り込み鍵を処理するには、{{site.data.keyword.la_full_notm}} サービスに対して、プラットフォーム役割の**エディター**とサービス役割の**管理者**を持つ IAM ポリシーが必要です。 


## {{site.data.keyword.cloud_notm}} UI による取り込み鍵の取得
{: #ibm_cloud_ui}

{{site.data.keyword.cloud_notm}} UI を使用して {{site.data.keyword.la_full_notm}} インスタンスの取り込み鍵を取得するには、以下の手順を実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. ナビゲーション・メニューで、**「プログラム識別情報」**を選択します。 

3. **「ロギング」**を選択します。 {{site.data.keyword.la_full_notm}} ダッシュボードが開きます。 {{site.data.keyword.cloud_notm}} で使用可能なロギング・インスタンスのリストが表示されています。

3. 取り込み鍵を取得するインスタンスを特定して、**「取り込み鍵の表示 (View ingestion key)」**をクリックします。

4. ウィンドウが開き、そこで**「表示」**をクリックすると取り込み鍵が表示されます。


## {{site.data.keyword.la_full_notm}} Web UI による取り込み鍵の取得
{: #logdna_ui}

{{site.data.keyword.la_full_notm}} Web UI を使用して {{site.data.keyword.la_full_notm}} インスタンスの取り込み鍵を取得するには、以下の手順を実行します。

1. {{site.data.keyword.la_full_notm}} Web UI ブラウザーを起動します。 詳しくは、[{{site.data.keyword.la_full_notm}} Web UI の起動](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)を参照してください。

2. **「構成」**アイコンを選択します。 次に、**「組織」**を選択します。 

3. **「API キー」**を選択します。

作成された取り込み鍵が表示されます。 

**注:** 一度に 1 つの取り込み鍵だけをアクティブにすることができます。 


## {{site.data.keyword.cloud_notm}} CLI による取り込み鍵の取得
{: #ibm_cloud_cli}

コマンド・ラインによって {{site.data.keyword.la_full_notm}} インスタンスの取り込み鍵を取得するには、以下の手順を実行します。

1. [前提条件] {{site.data.keyword.cloud_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.cloud_notm}}CLI のインストール』](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)を参照してください。

   CLI がインストールされている場合は、次のステップに進みます。

2. インスタンスが実行中の {{site.data.keyword.cloud_notm}} の地域にログインします。 次のコマンドを実行します。 [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. {{site.data.keyword.la_full_notm}} インスタンスが実行中のリソース・グループを設定します。 コマンド [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target) にオプション `-g` を指定して実行します。

    デフォルトでは、`default` リソース・グループが設定されます。

4. {{site.data.keyword.la_full_notm}} インスタンスに関連付けられた API 鍵の名前を取得します。 次の [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) コマンドを実行します。

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    インスタンスに関連付けられたサービス・キーを識別します。

5. 取り込み鍵を取得します。 次の [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) コマンドを実行します。

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    APIKEY_NAME は API 鍵の名前です
 
    このコマンドの出力には、インスタンスの取り込み鍵を含むフィールド **ingestion_key** があります。


## 取り込み鍵のリセット 
{: #reset}

取り込み鍵が漏えいした場合や、それを数日後に更新するポリシーがある場合は、新しい鍵を生成して古い鍵を削除できます。

{{site.data.keyword.la_full_notm}} Web UI を使用して {{site.data.keyword.la_full_notm}} インスタンスの取り込み鍵を更新するには、以下の手順を実行します。

1. {{site.data.keyword.la_full_notm}} Web UI ブラウザーを起動します。 詳しくは、[{{site.data.keyword.la_full_notm}} Web UI の起動](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)を参照してください。

2. **「構成」**アイコンを選択します。 次に、**「組織」**を選択します。 

3. **「API キー」**を選択します。

    作成された取り込み鍵が表示されます。 

4. **「取り込み鍵の生成 (Generate Ingestion Key)」**を選択します。

    リストに新しい鍵が追加されます。

5. これまでの取り込み鍵を削除します。 **「削除」**をクリックします。

**注:** 取り込み鍵をリセットした後に、ログがこの {{site.data.keyword.la_full_notm}} インスタンスに転送されるように構成したすべてのログ・ソースの取り込み鍵を更新する必要があります。



