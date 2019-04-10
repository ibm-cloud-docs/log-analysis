---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ubuntu, tutorial

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


# {{site.data.keyword.la_full_notm}} による Ubuntu ログの管理
{: #ubuntu}

{{site.data.keyword.la_full}} サービスを使用して、{{site.data.keyword.cloud_notm}} 上の中央ロギング・システム内の Ubuntu ログをモニターして管理します。 
{:shortdesc}

システム・ログとアプリケーション・ログを収集してモニターできます。 

デフォルトでは、Ubuntu 用 LogDNA エージェントは **/var/log** ディレクトリー内のログ・ファイルをモニターします。 例えば、Ubuntu システム・ログ (*/var/log/syslog*) はデフォルトでモニターされます。

{{site.data.keyword.cloud_notm}} で {{site.data.keyword.la_full_notm}} インスタンスにログを転送するように Ubuntu サーバーを構成するには、以下のステップを実行する必要があります。

1. {{site.data.keyword.la_full_notm}} サービスのインスタンスをプロビジョンします。 
2. Ubuntu サーバーに LogDNA エージェントを構成します。
3. 必要に応じて、エージェントがモニターするディレクトリーをさらに追加します。

![{{site.data.keyword.cloud_notm}} 上のコンポーネントの概要](../images/ubuntu.png "{{site.data.keyword.cloud_notm}} 上のコンポーネントの概要")

このチュートリアルでは、{{site.data.keyword.la_full_notm}} インスタンスにログを転送するように Ubuntu サーバーを構成する方法を学習します。

## 始める前に
{: #ubuntu_prereqs}

{{site.data.keyword.la_full_notm}} についてお読みください。 詳しくは、[LogDNA について](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)を参照してください。

米国南部地域で作業します。 {{site.data.keyword.la_full_notm}} は現在、米国南部地域で使用可能です。 **注:** 同じ地域にある Ubuntu サーバーからでも、異なる地域にある Ubuntu サーバーからでも、データを送信できます。 

{{site.data.keyword.cloud_notm}} アカウントのメンバーまたは所有者であるユーザー ID を使用します。 {{site.data.keyword.cloud_notm}} ユーザー ID を取得するには、[「登録」![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} にアクセスしてください。

以下のリソースのそれぞれについて、{{site.data.keyword.IBM_notm}}ID に IAM ポリシーが割り当てられていなければなりません。 

| リソース                             | アクセス・ポリシーの有効範囲 | 役割    | 地域    | 情報                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| リソース・グループ **Default**           |  リソース・グループ            | ビューアー  | us-south  | デフォルトのリソース・グループ内のサービス・インスタンスをユーザーが表示できるようにするためには、このポリシーが必要です。    |
| {{site.data.keyword.la_full_notm}} サービス |  リソース・グループ            | エディター  | us-south  | デフォルトのリソース・グループ内の {{site.data.keyword.la_full_notm}} サービスをユーザーがプロビジョンおよび管理できるようにするためには、このポリシーが必要です。   |
{: caption="表 1. チュートリアルを実行するために必要な IAM ポリシーのリスト" caption-side="top"} 

{{site.data.keyword.cloud_notm}} CLI をインストールします。 詳しくは、[『{{site.data.keyword.cloud_notm}}CLI のインストール』](/docs/cli/index.html#overview)を参照してください。



## ステップ 1. {{site.data.keyword.la_full_notm}} インスタンスをプロビジョンする
{: #ubuntu_step1}

{{site.data.keyword.cloud_notm}} UI を使用して {{site.data.keyword.la_full_notm}} のインスタンスをプロビジョンするには、以下のステップを実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. **「カタログ」**をクリックします。 {{site.data.keyword.cloud_notm}} で使用可能なサービスのリストが開きます。

3. 表示されたサービスのリストをフィルタリングするには、**「開発者用ツール」**カテゴリーを選択します。

4. **「{{site.data.keyword.la_full_notm}}」**タイルをクリックします。

5. サービス・インスタンスの名前を入力します。

6. **Default** リソース・グループを選択します。 

    デフォルトでは、**Default** リソース・グループが設定されます。

7. **「ライト」**サービス・プランを選択します。 

    デフォルトでは、**「ライト」**プランが設定されます。

    その他のサービス・プランについて詳しくは、[価格プラン](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)を参照してください。

8. ログインしている {{site.data.keyword.cloud_notm}} リソース・グループに {{site.data.keyword.la_full_notm}} サービスをプロビジョンするには、**「作成」**をクリックします。

インスタンスをプロビジョンすると、{{site.data.keyword.la_full_notm}} ダッシュボードが開きます。 


**注:** CLI を使用して LogDNA のインスタンスをプロビジョンするには、[{{site.data.keyword.cloud_notm}} CLI による LogDNA のプロビジョニング](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli) を参照してください。


## ステップ 2. インスタンスにログを送信するように Ubuntu サーバーを構成する
{: #ubuntu_step2}

ログを {{site.data.keyword.la_full_notm}} インスタンスに送信するように Ubuntu サーバーを構成するには、`logdna-agent` をインストールしなければなりません。 LogDNA エージェントは、*/var/log* からログ・ファイルを読み取り、ログ・データを LogDNA インスタンスに転送します。

LogDNA インスタンスにログを転送するように Ubuntu サーバーを構成するには、Ubuntu 端末から以下のステップを実行します。

1. LogDNA エージェントをインストールします。 次のコマンドを実行します。

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. {{site.data.keyword.la_full_notm}} インスタンスにログを転送するために LogDNA エージェントが使用する必要のある取り込み鍵を設定します。  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    ここで、INGESTION_KEY には、ログの転送先として構成している {{site.data.keyword.la_full_notm}} インスタンスのアクティブな取り込み鍵が含まれます。

3. 認証エンドポイントを設定します。 LogDNA エージェントはこのホストを使用して認証され、ログを転送するためのトークンを取得します。

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. 取り込みエンドポイントを設定します。

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. モニターする他のログ・パスを定義します。 次のコマンドを実行します。 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    デフォルトでは、**/var/log** がモニターされます。

6. 必要に応じて、ホストにタグ付けするように LogDNA エージェントを構成します。 次のコマンドを実行します。

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}


## ステップ 3. LogDNA Web UI を起動する
{: #ubuntu_step3}

{{site.data.keyword.cloud_notm}} UI を使用して IBM Log Analysis with LogDNA ダッシュボードを起動するには、以下のステップを実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} ダッシュボードが開きます。

2. ナビゲーション・メニューで、**「プログラム識別情報」**を選択します。 

3. **「ロギング」**を選択します。 

    {{site.data.keyword.cloud_notm}} で使用可能な {{site.data.keyword.la_full_notm}} インスタンスのリストが表示されます。

3. インスタンスを 1 つ選択します。 次に、**「LogDNA の表示 (View LogDNA)」**をクリックします。

    LogDNA Web UI が開き、クラスター・ログが表示されます。


## ステップ 4. ログを表示する
{: #ubuntu_step4}

LogDNA Web UI から、システムをパススルーしているログを表示できます。 ログ追尾を使用してログを表示します。 

**注:** **無料**サービス・プランでは、追尾できるのは最新のログのみです。

詳しくは、[ログの表示](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs)を参照してください。


## 次のステップ
{: #ubuntu_next_steps}

[ログのフィルタリング](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5)、[ログの検索](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)、[ビューの定義](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)、[アラートの構成](https://docs.logdna.com/docs/alerts)を行います。 

**注:** これらの機能のいずれかを使用するには、{{site.data.keyword.la_full_notm}} プランを有料プランにアップグレードする必要があります。

