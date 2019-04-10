---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# インスタンスからの LogDNA エージェントのデタッチ
{: #detach_agent}

ログの収集を停止するために、LogDNA エージェントをロギング・インスタンスからデタッチします。
{:shortdesc}

## Kubernetes クラスターからの a LogDNA エージェントのデタッチ
{: #detach_agent_kube}

Kubernetes クラスターが {{site.data.keyword.la_full_notm}} インスタンスにログを送信するのを停止するには、LogDNA エージェントをクラスターから除去する必要があります。 

Kubernetes クラスターが LogDNA インスタンスにログを転送するのを停止するには、コマンド・ラインから以下のステップを実行します。

1. 端末を開きます。 次に、[{{site.data.keyword.cloud_notm}} ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} にログインし、プロンプトに従います。

    {{site.data.keyword.la_full_notm}} インスタンスをプロビジョンしたアカウントを選択します。

2. クラスター環境をセットアップします。 次のコマンドを実行します。

    最初に、環境変数を設定して Kubernetes 構成ファイルをダウンロードするためのコマンドを取得します。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    構成ファイルのダウンロードが完了すると、そのローカルの Kubernetes 構成ファイルのパスを環境変数として設定するために使用できるコマンドが表示されます。

    次に、`KUBECONFIG` 環境変数を設定するためのコマンドとしてターミナルに表示されたものを、コピーして貼り付けます。

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




