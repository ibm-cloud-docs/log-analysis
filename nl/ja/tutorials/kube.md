---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial

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


# {{site.data.keyword.la_full_notm}} による Kubernetes クラスター・ログの管理
{: #kube}

{{site.data.keyword.la_full_notm}} サービスを使用して、{{site.data.keyword.containerlong}} でのクラスター・レベル・ロギングを構成します。 
{:shortdesc}

{{site.data.keyword.containerlong_notm}} を使用してクラスターをプロビジョンした瞬間から、クラスター内部で何が起こっているか知る必要があります。 問題をトラブルシューティングしたり、問題に先手を打ったりするためには、ログにアクセスする必要があります。 どのようなときでも、ワーカー・ログ、ポッド・ログ、アプリ・ログ、ネットワーク・ログなど、さまざまなタイプのログにアクセスできる必要があります。 さらに、Kubernetes クラスター内のログ・データのさまざまなソースをモニターする必要があります。 したがって、これらのどのソースのログ・レコードについても管理でき、アクセスできることが重要です。 ログの管理とモニタリングがうまくいくかどうかは、Kubernetes プラットフォームに対するロギング機能をどのように構成するかによって決まります。

Kubernetes クラスターのクラスター・レベル・ロギングを構成するには、以下のことを考慮してください。

* ログ・データ、システム・ログ、コンテナー化アプリケーション・ログを、Kubernetes システム・コンポーネントとは別のストレージに保管できなければなりません。
* クラスター内のどのワーカー・ノードにもロギング・エージェントをデプロイする必要があります。 このエージェントはログを収集し、外部ロギング・バックエンドに転送します。
* 外部ロギング・バックエンドでの分析のためのログ・データを中央管理できなければなりません。


{{site.data.keyword.cloud_notm}} で Kubernetes クラスターのクラスター・レベル・ロギングを構成するには、以下のステップを実行します。

1. {{site.data.keyword.la_full_notm}} サービスのインスタンスをプロビジョンします。 このステップで、ログ・データがホストされる中央ログ管理システムを {{site.data.keyword.cloud_notm}} 上に構成します。
2. {{site.data.keyword.containerlong_notm}} にクラスターをプロビジョンします。 Kubernetes v1.9 以上のクラスターがサポートされています。
3. クラスター内のすべてのワーカー (ノード) に LogDNA エージェントを構成します。

![{{site.data.keyword.cloud_notm}} 上の LogDNA コンポーネントの概要](../images/kube.png "{{site.data.keyword.cloud_notm}} 上の LogDNA コンポーネントの概要")

このチュートリアルではクラスター・レベル・ロギングを構成する方法を学習します。

## 始める前に
{: #kube_prereqs}

[サポート対象地域](/docs/services/Log-Analysis-with-LogDNA/tutorials?topic=LogDNA-about#overview_regions)で作業します。**注:** 同じ地域にある Kubernetes クラスターからでも、異なる地域にある Kubernetes クラスターからでも、データを送信できます。 

{{site.data.keyword.la_full_notm}} についてお読みください。 詳しくは、[製品情報](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)を参照してください。

{{site.data.keyword.cloud_notm}} アカウントのメンバーまたは所有者であるユーザー ID を使用します。 {{site.data.keyword.cloud_notm}} ユーザー ID を取得するには、[「登録」![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} にアクセスしてください。

ご使用の {{site.data.keyword.la_full_notm}} インスタンスがある地域の以下のリソースのそれぞれについて、{{site.data.keyword.IBM_notm}} ID に IAM ポリシーが割り当てられていなければなりません。  

| リソース                             | アクセス・ポリシーの有効範囲 | 役割    | 情報                  |
|--------------------------------------|----------------------------|---------|------------------------------|
| リソース・グループ **Default**           |  リソース・グループ            | ビューアー  | デフォルトのリソース・グループ内のサービス・インスタンスをユーザーが表示できるようにするためには、このポリシーが必要です。    |
| {{site.data.keyword.la_full_notm}} サービス |  リソース・グループ            | エディター  | デフォルトのリソース・グループ内の {{site.data.keyword.la_full_notm}} サービスをユーザーがプロビジョンおよび管理できるようにするためには、このポリシーが必要です。   |
| Kubernetes クラスター・インスタンス          |  リソース                 | エディター  | Kubernetes クラスター内のシークレットおよび LogDNA エージェントを構成するためには、このポリシーが必要です。 |
{: caption="表 1. チュートリアルを実行するために必要な IAM ポリシーのリスト" caption-side="top"} 

{{site.data.keyword.containerlong}} IAM 役割について詳しくは、[ユーザー・アクセス許可](/docs/containers?topic=containers-access_reference#access_reference)を参照してください。

{{site.data.keyword.cloud_notm}} CLI と Kubernetes CLI プラグインをインストールします。 詳しくは、[『{{site.data.keyword.cloud_notm}}CLI のインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)を参照してください。


## 達成目標
{: #kube_objectives}

このチュートリアルでは、{{site.data.keyword.containerlong_notm}} クラスターに対して LogDNA を使用したロギングを構成します。 特に、以下のことを行います。

- {{site.data.keyword.la_full_notm}} をプロビジョンする。 
- LogDNA へのログの送信を開始するようにクラスター内の LogDNA エージェントを構成する。 
- LogDNA ダッシュボードを開いてログを見つける。 


## ステップ 1. {{site.data.keyword.la_full_notm}} サービス・インスタンスをプロビジョンする
{: #kube_step1}

{{site.data.keyword.cloud_notm}} コンソールを使用して {{site.data.keyword.la_full_notm}} のサービス・インスタンスをプロビジョンするには、以下のステップを実行します。

1. Kubernetes クラスターを作成した [{{site.data.keyword.cloud_notm}} アカウント ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login) にログインします。

2. **「カタログ」**をクリックします。 {{site.data.keyword.cloud_notm}} サービスのリストが開きます。

3. 表示されたサービスのリストをフィルタリングするには、**「開発者用ツール」**カテゴリーを選択します。

4. **「{{site.data.keyword.la_full_notm}}」**をクリックします。 **「プログラム識別情報」**ダッシュボードが開きます。

5. **「インスタンスの作成 (Create instance)」**を選択します。 

6. サービス・インスタンスの名前を入力します。

7. クラスターが含まれるリソース・グループを選択します。 デフォルトでは、**Default** リソース・グループが設定されます。 

8. サービス・インスタンスのサービス・プランを選択します。 デフォルトでは、**「ライト」**プランが選択されます。 その他のサービス・プランについて詳しくは、[価格プラン](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)を参照してください。

9. ログインしている {{site.data.keyword.cloud_notm}} リソース・グループに {{site.data.keyword.la_full_notm}} サービスをプロビジョンするには、**「作成」**をクリックします。 **「プログラム識別情報」**ダッシュボードが開き、サービスの詳細が示されます。 

CLI を使用してインスタンスをプロビジョンするには、[{{site.data.keyword.cloud_notm}} CLI によるインスタンスのプロビジョニング](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli)を参照してください。
{: tip}

## ステップ 2. 取り込み鍵を取得する
{: #kube_step2}

取り込み鍵を取得するには、以下の手順を実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. ナビゲーション・メニューで、**「プログラム識別情報」**を選択します。 

3. **「ロギング」**を選択します。 {{site.data.keyword.la_full_notm}} ダッシュボードが開きます。 {{site.data.keyword.cloud_notm}} で使用可能なロギング・インスタンスのリストが表示されています。

3. 取り込み鍵を取得するインスタンスを特定して、**「取り込み鍵の表示 (View ingestion key)」**をクリックします。

4. ウィンドウが開き、そこで**「表示」**をクリックすると取り込み鍵が表示されます。


## ステップ 3: LogDNA インスタンスにログを送信するように Kubernetes クラスターを構成する
{: #kube_step3}

ログを {{site.data.keyword.la_full_notm}} インスタンスに送信するように Kubernetes クラスターを構成するには、クラスターの各ノード上に `logdna-agent` ポッドをインストールしなければなりません。 LogDNA エージェントはそれがインストールされたポッドからログ・ファイルを読み取り、LogDNA インスタンスにログ・データを転送します。

LogDNA インスタンスにログを転送するように Kubernetes クラスターを構成するには、コマンド・ラインから以下のステップを実行します。

1. 端末を開いて、{{site.data.keyword.cloud_notm}} にログインします。

   ```
   ibmcloud login -a cloud.ibm.com
   ```
   {: pre}

   {{site.data.keyword.la_full_notm}} インスタンスをプロビジョンしたアカウントを選択します。

2. ロギングを構成するクラスターを、このセッションのコンテキストとして設定します。

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   構成ファイルのダウンロードが完了すると、そのローカルの Kubernetes 構成ファイルのパスを環境変数として設定するために使用できるコマンドが表示されます。 `KUBECONFIG` 環境変数を設定するためのコマンドとしてターミナルに表示されたものを、コピーして貼り付けます。

   クラスターの作業を行うために {{site.data.keyword.containerlong_notm}} CLI にログインするたびに、このセットアップを実行して、クラスターの構成ファイルのパスをセッション変数として設定する必要があります。 {{site.data.keyword.containerlong_notm}} はこの変数を使用して、クラスターと接続するために必要なローカル構成ファイルと証明書を検索します。
   {: tip}

3. サービス・インスタンスの logDNA 取り込み鍵を保管するための Kubernetes シークレットを作成します。 logDNA 取り込みサーバーに対してセキュア Web ソケットを開く際、およびロギング・エージェントを {{site.data.keyword.la_full_notm}} サービスで認証する際に、LogDNA 取り込み鍵が使用されます。

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
    ```
    {: pre}

4. Kubernetes クラスターのすべてのワーカー・ノードに LogDNA エージェントをデプロイするように設定された Kubernetes デーモンを作成します。 LogDNA エージェントは、ポッドの `/var/log` ディレクトリーに保管されている `*.log` 拡張子のファイルと拡張子のないファイルを使用してログを収集します。 デフォルトでは、`kube-system` を含めすべての名前空間からログが収集され、{{site.data.keyword.la_full_notm}} サービスに自動的に転送されます。

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. LogDNA エージェントが正常にデプロイされたことを確認します。 

   ```
   kubectl get pods
   ```
   {: pre}
   
   LogDNA ポッドが 1 つ以上表示されたらデプロイメントは成功です。 LogDNA ポッドの数は、クラスター内のワーカー・ノードの数と等しくなります。 すべてのポッドが `Running` 状態である必要があります。


## ステップ 4: LogDNA ダッシュボードを起動してログを表示する
{: #kube_step4}

{{site.data.keyword.cloud_notm}} コンソールを使用して LogDNA ダッシュボードを起動するには、以下のステップを実行します。

1. [{{site.data.keyword.cloud_notm}} アカウント ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login) にログインします。

2. メニュー ![メニュー・アイコン](../../../icons/icon_hamburger.svg "メニュー・アイコン") から、**「プログラム識別情報」**を選択します。

3. **「ロギング」**を選択します。 {{site.data.keyword.cloud_notm}} で使用可能な {{site.data.keyword.la_full_notm}} サービス・インスタンスのリストが表示されます。

4. インスタンスを 1 つ選択して、**「LogDNA の表示 (View LogDNA)」**をクリックします。 LogDNA ダッシュボードが開きます。 **注:** **無料**サービス・プランでは、追尾できるのは最新のログのみです。 詳しくは、[ログの表示](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs)を参照してください。

## 次のステップ
{: #kube_next_steps}

- [ログをフィルタリングする](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5)
- [ログを検索する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)
- [ビューを定義する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)
- [アラートを構成する](https://docs.logdna.com/docs/alerts) 

**注:** これらの機能の中にはプランのアップグレードを必要とするものもあります。




