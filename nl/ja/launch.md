---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# Web UI へのナビゲート
{: #launch}

{{site.data.keyword.la_full_notm}} サービスのインスタンスを {{site.data.keyword.cloud_notm}} にプロビジョンし、ログ・データ・ソース用の LogDNA エージェントを構成したら、{{site.data.keyword.la_full_notm}} Web UI によってログを表示、モニター、および管理できます。
{:shortdesc}


## データを表示するための IAM ポリシーをユーザーに付与する 
{: #step1}

**注:** 他のユーザーにポリシーを付与するには、{{site.data.keyword.la_full_notm}} サービスの管理者または {{site.data.keyword.la_full_notm}} インスタンスの管理者であるか、アカウント IAM 許可を所持している必要があります。

以下の表に、Web UI を起動してデータを表示するために必要な最小ポリシーをリストします。

| サービス                              | 役割                      | 付与される許可       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | プラットフォーム役割: ビューアー     | ユーザーが「プログラム識別情報ロギング (Observability Logging)」ダッシュボードでサービス・インスタンスのリストを表示できるようにします。 |
| `{{site.data.keyword.la_full_notm}}` | サービス役割: ライター      | ユーザーが Web UI を起動して Web UI にログを表示できるようにします。    |
{: caption="表 1. IAM ポリシー" caption-side="top"} 

ユーザーに対してこれらのポリシーを構成する方法について詳しくは、[ログの表示許可をユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)を参照してください。


## {{site.data.keyword.cloud_notm}} UI による Web UI の起動
{: #launch_step2}

{{site.data.keyword.cloud_notm}} UI から {{site.data.keyword.la_full_notm}} インスタンスのコンテキスト内で Web UI を起動します。 

Web UI を起動するには、以下の手順を実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} ダッシュボードが開きます。

2. ナビゲーション・メニューで、**「プログラム識別情報」**を選択します。 

3. **「ロギング」**を選択します。 

    {{site.data.keyword.cloud_notm}} で使用可能なインスタンスのリストが表示されます。

4. インスタンスを 1 つ選択します。 次に、**「LogDNA の表示 (View LogDNA)」**をクリックします。

Web UI が開きます。


## {{site.data.keyword.cloud_notm}} からの Web UI URL の取得
{: #launch_get}

Web UI URL を取得するには、端末から以下の手順を実行します。

1. {{site.data.keyword.la_full_notm}} インスタンスがプロビジョンされるリソース・グループを設定します。

    ```
    export logdna_rg_name=<Resource_Group_Name_Where_LogDNA_Instance_Is_Created>
    ```
    {: codeblock}

2. {{site.data.keyword.la_full_notm}} インスタンス名を設定します。

    ```
    export logdna_instance_name=<Your_LogDNA_Instance_Name>
    ```
    {: codeblock}

3. エンドポイントを設定します。

    ```
    export rc_endpoint=resource-controller.cloud.ibm.com
    ```
    {: codeblock}

4. IAM トークンを設定します。

    ```
    export iam_token=$(ibmcloud iam oauth-tokens | grep IAM | grep -oP  "eyJ.*")
    ```
    {: codeblock}

    **注:** MacOS 端末で作業している場合、コマンドは次のようになります。`export iam_token=$(ic iam oauth-tokens | grep IAM | grep -o  "eyJ.*")`

5. リソース・グループ ID を設定します。

    ```
    export resource_group_id=$(ibmcloud resource groups | grep "^$logdna_rg_name" | awk '{print $2}')
    ```
    {: codeblock}

6. 変数に Web UI URL を設定します。

    ```
    export dashboard_url=$(curl -H "Accept: application/json" -H "Authorization: Bearer $iam_token" "https://$rc_endpoint/v1/resource_instances?resource_group_id=$resource_group_id&type=service_instance" | jq ".resources[] | select(.name==\"$logdna_instance_name\") | .dashboard_url")
    ```
    {: codeblock}

7. Web UI URL を取得します。

    ```
    echo $dashboard_url
    ```
    {: codeblock}

    

