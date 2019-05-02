---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# LogDNA エージェントの構成
{: #config_agent}

LogDNA エージェントは、ログの収集と {{site.data.keyword.la_full_notm}} インスタンスへの転送を担当します。 {{site.data.keyword.la_full}} のインスタンスのプロビジョン後に、モニターしようとしているログ・ソースごとに LogDNA エージェントを構成しなければなりません。
{:shortdesc}

* LogDNA エージェントは、LogDNA 取り込み鍵を使用して認証し、{{site.data.keyword.la_full_notm}} 取り込みサーバーに対するセキュアな Web ソケットを開きます。 
* デフォルトでは、エージェントは */var/log/* の下にある、拡張子が *.log* のファイルと、拡張子がないファイルをすべてモニターします。
* エージェントは、新しいログ・データを追尾し、新しいファイルを検索してモニター対象のロギング・ディレクトリーに追加します。

LogDNA エージェントにより、以下のパラメーターを構成できます。 

| パラメーター | 説明 |
|-----------|-------------|
| `tags`    | ホストを動的グループに自動的にグループ化するタグを定義します。 |
| `logdir`  | エージェントがモニターするカスタム・パスを定義します。 </br>複数のパスはコンマを使用して区切ります。 glob パターンを使用できます。 特定のファイルを構成できます。 glob パターンは、二重引用符を使用して入力します。 |
| `exclude` | LogDNA エージェントがモニターしないファイルを定義します。 **注:** これらのファイルは、logdir パラメーターで定義しているいずれかのパス内に配置できます。 </br>複数のファイルはコンマを使用して区切ります。 glob パターンを使用できます。 特定のファイルを構成できます。 |
| `exclude_regex` | パターンと一致する行をフィルターで除外する正規表現パターンを定義します。 前後に `/` を含めないでください。 |
| `hostname` | ホスト名を定義します。 この値は、オペレーティング・システムのホスト名をオーバーライドします。 |
| `autoupdate` | パブリック・リポジトリー・エージェント定義の更新時にエージェントを自動的に更新するには、`1` に設定します。 このフィーチャーを無効にするには、`0` に設定します。 |  
{: caption="表 1. LogDNA エージェントをカスタマイズするパラメーター" caption-side="top"} 



## スクリプトを使用して Kubernetes クラスター上で LogDNA エージェントを構成する
{: #config_agent_kube_script}

ログを {{site.data.keyword.la_full_notm}} インスタンスに送信するように Kubernetes クラスターを構成するには、クラスターの各ノード上に *logdna-agent* ポッドをインストールしなければなりません。 LogDNA エージェントはそれがインストールされたポッドからログ・ファイルを読み取り、LogDNA インスタンスにログ・データを転送します。

LogDNA インスタンスにログを転送するように Kubernetes クラスターを構成するには、コマンド・ラインから以下のステップを実行します。

1. 端末を開いて、{{site.data.keyword.cloud_notm}} にログインします。

   ```
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   {{site.data.keyword.la_full_notm}} インスタンスをプロビジョンしたアカウントを選択します。

2. ロギングを構成するクラスターを、このセッションのコンテキストとして設定します。

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   構成ファイルのダウンロードが完了すると、そのローカルの Kubernetes 構成ファイルのパスを環境変数として設定するために使用できるコマンドが表示されます。 `KUBECONFIG` 環境変数を設定するためのコマンドとしてターミナルに表示されたものを、コピーして貼り付けます。

3. サービス・インスタンスの logDNA 取り込み鍵を保管するための Kubernetes シークレットを作成します。 logDNA 取り込みサーバーに対してセキュア Web ソケットを開く際、およびロギング・エージェントを {{site.data.keyword.la_full_notm}} サービスで認証する際に、LogDNA 取り込み鍵が使用されます。

   ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
   {: pre}

4. Kubernetes クラスターのすべてのワーカー・ノードに LogDNA エージェントをデプロイするように設定された Kubernetesデーモンを作成します。 LogDNA エージェントは、ポッドの `/var/log` ディレクトリーに保管されている `*.log` 拡張子のファイルと拡張子のないファイルを使用してログを収集します。 デフォルトでは、`kube-system` を含めすべての名前空間からログが収集され、{{site.data.keyword.la_full_notm}} サービスに自動的に転送されます。

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. LogDNA エージェントが正常にデプロイされたことを確認します。 

   ```
   kubectl get pods
   ```
   {: pre}
   

LogDNA ポッドが 1 つ以上表示されたらデプロイメントは成功です。
* **LogDNA ポッドの数は、クラスター内のワーカー・ノードの数と等しくなります。 ** 
* すべてのポッドが `Running` 状態である必要があります。
* *Stdout* と *stderr* はすべてのコンテナーから自動的に収集されて転送されます。 ログ・データにはアプリケーション・ログとワーカー・ログが含まれます。 
* デフォルトでは、ワーカー上で稼働する LogDNA エージェント・ポッドは、そのノード上のすべての名前空間から kube-system ログを含むログを収集します。



## Kubernetes クラスター上で LogDNA エージェントにタグを追加する
{: #config_agent_kube_tags}

タグを追加するには、以下のステップを実行します。

1. クラスター環境をセットアップします。 次のコマンドを実行します。

    最初に、環境変数を設定して Kubernetes 構成ファイルをダウンロードするためのコマンドを取得します。

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    構成ファイルのダウンロードが完了すると、そのローカルの Kubernetes 構成ファイルのパスを環境変数として設定するために使用できるコマンドが表示されます。

    次に、KUBECONFIG 環境変数を設定するためのコマンドとしてターミナルに表示されたものを、コピーして貼り付けます。

2. DaemonSet の更新予定を確認します。 次に、*kubectl apply* か *kubectl edit* のどちらを使用してエージェントの構成ファイルを変更するかを選択します。

    更新予定を確認するには、以下のコマンドを実行します。

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    更新予定が *OnDelete* に設定されている場合や、バージョン管理システムで管理される構成ファイルがある場合は、*kubectl apply* を使用して、ローカル構成ファイルを更新して LogDNA エージェントに変更を適用します。

    更新予定が *RollingUpdate* に設定されている場合は、*kubectl edit* を使用して、更新して LogDNA エージェントに変更を適用できます。

3. `logdna-agent-configmap.yaml` ファイルを編集します。 

    ローカル・コピーを変更して、構成ファイルを更新します。 **注:** 以下のコマンドを実行して、エージェントの構成ファイルを生成することもできます。

    ```
    kubectl get configmap logdna-agent -o=yaml > prod-logdna-agent-configmap.yaml
    ```
    {: codeblock}

    あるいは、*kubectl edit* を使用して構成ファイルを更新します。

    ```
    kubectl edit configmap logdna-agent
    ```
    {: codeblock}

4. 変更を加えます。 セクション **LOGDNA_TAGS** を追加します。

    ```
    - name: LOGDNA_TAGS
        value: tag1,tag2,tag3
    ```
    {: codeblock}

    例えば、以下のセクションは構成ファイル内のタグの追加場所を示しています。

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - name: LOGDNA_TAGS
              value: tag1,tag2,tag3
    ```
    {: screen}

5. ファイルをローカルに編集している場合は、構成変更を適用します。 

    ```
    kubectl apply -f logdna-agent-configmap.yaml
    ```
    {: codeblock}
    
    **注:** *kubectl edit* を使用する場合、変更の保存時に変更内容が自動的に適用されます。


## Linux Ubuntu または Debian 上で LogDNA エージェントを構成する
{: #config_agent_linux}

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

6. 必要に応じて、ホストにタグ付けするように LogDNA エージェントを構成します。 


## Linux Ubuntu または Debian 上で LogDNA エージェントにタグを追加する
{: #config_agent-linux_tags}
 

LogDNA エージェントにさらにタグを追加するには、以下のステップを実行します。

1. LogDNA エージェントが稼働中であることを確認します。

2. 1 つ以上のタグを追加します。

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}


LogDNA 構成ファイルを編集してタグを追加することもできます。 構成ファイルは */etc/logdna.conf* 内にあります。

1. ファイルを編集します。

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. タグを追加します。

3. LogDNA エージェントを再始動します。

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














