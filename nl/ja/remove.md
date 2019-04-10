---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# インスタンスの削除
{: #remove}

{{site.data.keyword.Bluemix}} UI から、またはコマンド・ラインによって、{{site.data.keyword.la_full_notm}} サービスのインスタンスを削除できます。
{:shortdesc}

インスタンスを {{site.data.keyword.cloud_notm}} から削除するときは、以下のタスクを実行してクリーンアップしてください。

1. 削除する {{site.data.keyword.la_full_notm}} インスタンスにメトリックを転送するソースのリストを書き出します。 各ソースから LogDNA エージェントを削除する必要があります。
2. そのインスタンスを処理するためにユーザーに付与されている許可を削除します。 

    特定のインスタンスを処理するための専用アクセス・グループを使用してアクセス権限を管理している場合、それらのアクセス・グループを削除する必要があります。

    アクセス・グループを使用して複数のロギング・インスタンスに対するアクセス権限を管理している場合、削除するインスタンスに許可を付与するポリシーを削除する必要があります。
    
    個別のポリシーをユーザーに付与する場合、そのインスタンスを処理するための許可を持つユーザーのリストを収集する必要があります。 その後、識別したユーザーごとに、削除するインスタンスに関連したポリシーを削除する必要があります。


その後、{{site.data.keyword.cloud_notm}} ダッシュボードからインスタンスを削除します。


## {{site.data.keyword.cloud_notm}} UI によるインスタンスの削除
{: #remove_ui}

{{site.data.keyword.cloud_notm}} UI を使用して {{site.data.keyword.la_full_notm}} のインスタンスを削除するには、以下の手順を実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. メニュー・アイコン ![メニュー・アイコン](../../icons/icon_hamburger.svg) &gt;**「プログラム識別情報」**に移動して、*プログラム識別情報*ダッシュボードにアクセスします。

3. **「ロギング」**を選択します。 ロギングするインスタンスのリストが表示されます。

4. 削除するインスタンスを選択します。

5. *「アクション」*メニューから、**「削除」**を選択します。


## CLI によるインスタンスの削除
{: #remove_cli}

コマンド・ラインによって {{site.data.keyword.la_full_notm}} のインスタンスを削除するには、以下の手順を実行します。

1. [前提条件] {{site.data.keyword.cloud_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.cloud_notm}}CLI のインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)を参照してください。

   CLI がインストールされている場合は、次のステップに進みます。

2. インスタンスをプロビジョンしたい、{{site.data.keyword.cloud_notm}} の地域にログインします。 次のコマンドを実行します。 [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. インスタンスがプロビジョンされるリソース・グループを設定します。 次のコマンドを実行します。 [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    デフォルトでは、*default* リソース・グループが設定されます。

4. インスタンスを削除します。 次の [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) コマンドを実行します。

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    ここで、NAME は、インスタンスの名前です。

    例えば、インスタンスを削除するために、以下のコマンドを実行します。

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



