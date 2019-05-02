---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# {{site.data.keyword.la_full_notm}} インスタンスにログを転送するために Kubernetes クラスターによって使用される取り込み鍵の再設定
{: #kube_reset}

{{site.data.keyword.cloud_notm}} でクラスターから {{site.data.keyword.la_full_notm}} インスタンスにログを転送するために使用する取り込み鍵が暗号漏えいした場合は、鍵を再設定し、その新しい取り込み鍵を使用するように Kubernetes クラスター構成を更新する必要があります。 
{:shortdesc}

## 始める前に
{: #kube_reset_prereqs}

米国南部地域で作業します。 {{site.data.keyword.la_full_notm}} インスタンスと Kubernetes クラスターの両方のリソースが同じアカウントで実行されていなければなりません。

{{site.data.keyword.la_full_notm}} インスタンスは **Default** リソース・グループにプロビジョンされます。

{{site.data.keyword.la_full_notm}} についてお読みください。 詳しくは、[LogDNA について](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)を参照してください。

このチュートリアルのステップを実行するには、以下のリソースのそれぞれについて、{{site.data.keyword.IBM_notm}}ID に IAM ポリシーが割り当てられていなければなりません。 

| リソース                             | アクセス・ポリシーの有効範囲 | 役割    | 地域    | 情報                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| リソース・グループ **Default**           |  リソース・グループ            | ビューアー  | us-south  | デフォルトのリソース・グループ内のサービス・インスタンスをユーザーが表示できるようにするためには、このポリシーが必要です。    |
| {{site.data.keyword.la_full_notm}} サービス |  リソース・グループ            | エディター </br>管理者  | us-south  | 取り込み鍵をユーザーが再設定できるようにするためには、このポリシーが必要です。   |
| Kubernetes クラスター・インスタンス          |  リソース                  | エディター  | us-south  | Kubernetes クラスター内のシークレットと LogDNA エージェントを削除および構成するためには、このポリシーが必要です。 |
{: caption="表 1. チュートリアルを実行するために必要な IAM ポリシーのリスト" caption-side="top"} 

{{site.data.keyword.containerlong}} IAM 役割について詳しくは、[ユーザー・アクセス許可](/docs/containers?topic=containers-access_reference#access_reference)を参照してください。

{{site.data.keyword.cloud_notm}} CLI と Kubernetes CLI プラグインをインストールします。 詳しくは、[『{{site.data.keyword.cloud_notm}}CLI のインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli)を参照してください。


## ステップ 1: 取り込み鍵を再設定する
{: #kube_reset_step1}

{{site.data.keyword.la_full_notm}} Web UI を使用して {{site.data.keyword.la_full_notm}} インスタンスの取り込み鍵を更新するには、以下の手順を実行します。

1. {{site.data.keyword.la_full_notm}} Web UI ブラウザーを起動します。 詳しくは、[{{site.data.keyword.la_full_notm}} Web UI の起動](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)を参照してください。

2. **「構成」**アイコンを選択します。 次に、**「組織」**を選択します。 

3. **「API キー」**を選択します。

    作成された取り込み鍵が表示されます。 

4. **「取り込み鍵の生成 (Generate Ingestion Key)」**を選択します。

    リストに新しい鍵が追加されます。

5. これまでの取り込み鍵を削除します。 **「削除」**をクリックします。


## ステップ 2: これまでの取り込み鍵を使用しているクラスターの構成を削除する
{: #kube_reset_step2}

以下のステップを実行します。

1. 端末を開きます。 次に、{{site.data.keyword.cloud_notm}} にログインします。 次のコマンドを実行して、プロンプトに従います。

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    {{site.data.keyword.la_full_notm}} インスタンスをプロビジョンしたアカウントを選択します。

2. クラスター環境をセットアップします。 次のコマンドを実行します。

    最初に、環境変数を設定して Kubernetes 構成ファイルをダウンロードするためのコマンドを取得します。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    構成ファイルのダウンロードが完了すると、そのローカルの Kubernetes 構成ファイルのパスを環境変数として設定するために使用できるコマンドが表示されます。

    次に、KUBECONFIG 環境変数を設定するためのコマンドとしてターミナルに表示されたものを、コピーして貼り付けます。

    **注:** クラスターの作業を行うために {{site.data.keyword.containerlong}} CLI にログインするたびに、これらのコマンドを実行して、クラスターの構成ファイルのパスをセッション変数として設定する必要があります。 Kubernetes CLI はこの変数を使用して、{{site.data.keyword.cloud_notm}} 内のクラスターと接続するために必要なローカル構成ファイルと証明書を検索します。

3. Kubernetes クラスターからシークレットを削除します。 Kubernetes シークレットには LogDNA 取り込み鍵が含まれています。 次のコマンドを実行します。

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Kubernetes クラスターのすべてのワーカー (ノード) 上の LogDNA エージェントを削除します。 LogDNA エージェントはログの収集と転送を行います。 次のコマンドを実行します。

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. LogDNA エージェントが正常に削除されたことを確認します。 次のコマンドを実行します。

    ```
    kubectl get pods
    ```
    {: codeblock}

    LogDNA ポッドは表示されないはずです。


## ステップ 3: 新しい取り込み鍵を Kubernetes クラスターに構成する
{: #kube_reset_step3}

LogDNA インスタンスにログを転送するように Kubernetes クラスターを構成するには、コマンド・ラインから以下のステップを実行します。

1. 端末を開きます。 次に、{{site.data.keyword.cloud_notm}} にログインします。 次のコマンドを実行して、プロンプトに従います。

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    {{site.data.keyword.la_full_notm}} インスタンスをプロビジョンしたアカウントを選択します。

2. クラスター環境をセットアップします。 次のコマンドを実行します。

    最初に、環境変数を設定して Kubernetes 構成ファイルをダウンロードするためのコマンドを取得します。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    構成ファイルのダウンロードが完了すると、そのローカルの Kubernetes 構成ファイルのパスを環境変数として設定するために使用できるコマンドが表示されます。

    次に、KUBECONFIG 環境変数を設定するためのコマンドとしてターミナルに表示されたものを、コピーして貼り付けます。

    **注:** クラスターの作業を行うために {{site.data.keyword.containerlong}} CLI にログインするたびに、これらのコマンドを実行して、クラスターの構成ファイルのパスをセッション変数として設定する必要があります。 Kubernetes CLI はこの変数を使用して、{{site.data.keyword.cloud_notm}} 内のクラスターと接続するために必要なローカル構成ファイルと証明書を検索します。

3. Kubernetes クラスターにシークレットを追加します。 次のコマンドを実行します。

    ```
    kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE は、インスタンスの LogDNA 取り込み鍵を示しています。

    Kubernetes シークレットには LogDNA 取り込み鍵が含まれています。 LogDNA 取り込み鍵は、ロギング・エージェントを {{site.data.keyword.la_full_notm}} サービスで認証する際に使用されます。 ロギング・バックエンド・システム上の取り込みサーバーに対してセキュア Web ソケットを開くためにも使用されます。

4. Kubernetes クラスターのすべてのワーカー (ノード) 上に LogDNA エージェントを構成します。 次のコマンドを実行します。

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    LogDNA エージェントはログの収集と転送を行います。

    エージェントは、/var/log の下にある *.log 拡張子のファイルと拡張子のないファイルを使用して、自動的にログを収集します。 デフォルトでは、kube-system を含めすべての名前空間からログが収集されます。

5. LogDNA エージェントが正常に作成されたこととその状況を確認します。 次のコマンドを実行します。

    ```
    kubectl get pods
    ```
    {: codeblock}


## ステップ 4: LogDNA Web UI を起動する
{: #kube_reset_step4}

{{site.data.keyword.cloud_notm}} UI を使用して IBM Log Analysis with LogDNA ダッシュボードを起動するには、以下のステップを実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} ダッシュボードが開きます。

2. ナビゲーション・メニューで、**「プログラム識別情報」**を選択します。 

3. **「ロギング」**を選択します。 

    {{site.data.keyword.cloud_notm}} で使用可能な {{site.data.keyword.la_full_notm}} インスタンスのリストが表示されます。

3. インスタンスを 1 つ選択します。 次に、**「ログの表示」**をクリックします。

    LogDNA Web UI が開き、クラスター・ログが表示されます。


## ステップ 5: ログを表示する
{: #kube_reset_step5}

LogDNA Web UI から、システムをパススルーしているログを表示できます。 ログ追尾を使用してログを表示します。 

**注:** **無料**サービス・プランでは、追尾できるのは最新のログのみです。



## 次のステップ
{: #kube_reset_next_steps}

  [クラスター・ログのフィルタリング](https://docs.logdna.com/docs/filters)、[クラスター・ログの検索](https://docs.logdna.com/docs/search)、[ビューの定義](https://docs.logdna.com/docs/views)、[アラートの構成](https://docs.logdna.com/docs/alerts)を行う場合は、{{site.data.keyword.la_full_notm}} プランを有料プランにアップグレードする必要があります。



