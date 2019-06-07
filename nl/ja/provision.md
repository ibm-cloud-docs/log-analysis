---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# インスタンスのプロビジョニング
{: #provision}

{{site.data.keyword.la_full_notm}} でログ・データのモニターと管理を行うには、その前に、まずサービスのインスタンスを {{site.data.keyword.cloud_notm}} 内にプロビジョンする必要があります。
{:shortdesc}

{{site.data.keyword.la_full_notm}} インスタンスを Public Cloud リージョンにプロビジョンするには、インスタンスに関連付けられたサービス・プラン、ログが収集される地域、およびログの保存期間を決定するプランを選択する必要があります。 保存期間は、7、14、または 30 日から選択できます。

代わりに、{{site.data.keyword.la_full_notm}} は、ログがシステムを通過する際にそれを表示するために使用できる、`「ライト」`プランも提供しています。 ログ追尾を使用してログを表示できます。 また、より長期の保存期間プランにアップグレードするための準備として、フィルターを設計することもできます。 このプランの保存期間は 0 日です。


## プログラム識別情報ダッシュボードによるインスタンスのプロビジョニング
{: #provision_ui}

{{site.data.keyword.cloud_notm}} のプログラム識別情報ダッシュボードからインスタンスをプロビジョンするには、以下の手順を実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    {{site.data.keyword.cloud_notm}} ダッシュボードは、[{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} にあります。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. メニュー・アイコン ![メニュー・アイコン](../../icons/icon_hamburger.svg) に移動します。 その後、**「プログラム識別情報」**を選択して、*「プログラム識別情報」*ダッシュボードにアクセスします。

3. **「ロギング」**を選択してから、**「インスタンスの作成 (Create instance)」**をクリックします。 

4. サービス・インスタンスの名前を入力します。

5. リソース・グループを選択します。 

    デフォルトでは、**Default** リソース・グループが設定されます。

    **注:** リソース・グループを選択できない場合、インスタンスをプロビジョンするリソース・グループでの編集許可があることを確認してください。

6. `「ライト」`サービス・プランを選択します。 

    デフォルトでは、ライト・プランが設定されます。

    その他のサービス・プランについて詳しくは、[価格プラン](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)を参照してください。

7. **「作成」**をクリックします。

インスタンスをプロビジョンすると、*「ロギング」*ダッシュボードが開きます。 

次に、LogDNA エージェントを追加してログ・ソースを構成します。 このエージェントは、ログの収集とインスタンスへの転送を行います。 



## カタログによるインスタンスのプロビジョニング
{: #provision_catalog}

{{site.data.keyword.cloud_notm}} カタログによって {{site.data.keyword.la_full_notm}} のインスタンスをプロビジョンするには、以下の手順を実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. **「カタログ」**をクリックします。 {{site.data.keyword.cloud_notm}} で使用可能なサービスのリストが開きます。

3. 表示されたサービスのリストをフィルタリングするには、**「開発者用ツール」**カテゴリーを選択します。

4. **「{{site.data.keyword.la_full_notm}}」**タイルをクリックします。 

5. サービス・インスタンスの名前を入力します。

6. リソース・グループを選択します。 

    デフォルトでは、**Default** リソース・グループが設定されます。

    **注:** リソース・グループを選択できない場合、インスタンスをプロビジョンするリソース・グループでの編集許可があることを確認してください。

7. `「ライト」`サービス・プランを選択します。 

    デフォルトでは、ライト・プランが設定されます。

    その他のサービス・プランについて詳しくは、[価格プラン](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)を参照してください。

8. **「作成」**をクリックします。

インスタンスをプロビジョンすると、*「ロギング」*ダッシュボードが開きます。 

次に、LogDNA エージェントを追加してログ・ソースを構成します。 このエージェントは、ログの収集とインスタンスへの転送を行います。 



## CLI によるインスタンスのプロビジョニング
{: #provision_cli}

コマンド・ラインによって {{site.data.keyword.la_full_notm}} のインスタンスをプロビジョンするには、以下の手順を実行します。

1. [前提条件] {{site.data.keyword.cloud_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.cloud_notm}}CLI のインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)を参照してください。

   CLI がインストールされている場合は、次のステップに進みます。

2. インスタンスをプロビジョンしたい、{{site.data.keyword.cloud_notm}} の地域にログインします。 次のコマンドを実行します。 [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. インスタンスをプロビジョンするリソース・グループを設定します。 次のコマンドを実行します。 [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    デフォルトでは、`default` リソース・グループが設定されます。

4. インスタンスを作成します。 次の [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) コマンドを実行します。

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    説明

    NAME はインスタンスの名前です

    値 *logdna* は、{{site.data.keyword.cloud_notm}} での {{site.data.keyword.la_full_notm}} サービスの名前です。

    SERVICE_PLAN_NAME はプランのタイプです。 有効値は、*lite*、*7-days*、*14-days*、*30-days* です。
    
    LOCATION は LogDNA インスタンスが作成される地域です。 有効値は、*us-south*、*eu-de* です。

    例えば、7 日間の保存プランでインスタンスをプロビジョンするには、以下のコマンドを実行します。

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}




