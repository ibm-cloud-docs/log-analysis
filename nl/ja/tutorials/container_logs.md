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


# Kubernetes クラスターにデプロイされたアプリに関する Kibana でのログの分析
{: #container_logs}
このチュートリアルを使用して、{{site.data.keyword.Bluemix_notm}} の {{site.data.keyword.loganalysisshort}} サービスにログを転送するためにクラスターを構成する方法を学習します。
{:shortdesc}


## 目標
{: #objectives}

1. クラスター内のロギング構成を構成します。 
2. {{site.data.keyword.Bluemix_notm}} 内の Kubernetes クラスターにデプロイされたアプリのコンテナー・ログを検索および分析します。

このチュートリアルでは、クラスターをプロビジョンし、{{site.data.keyword.Bluemix_notm}} の {{site.data.keyword.loganalysisshort}} サービスにログを送信するためにクラスターを構成し、クラスター内にアプリをデプロイし、Kibana を使用してそのクラスターのコンテナー・ログを表示およびフィルタリングするまでのエンドツーエンドのシナリオを {{site.data.keyword.Bluemix_notm}} 内で機能させるために必要なステップをウォークスルーします。


**注:** このチュートリアルを完了するためには、前提条件を完了しておくほかに、各ステップからリンクされているチュートリアルを実行する必要があります。


## 前提条件
{: #prereq}

1. Kubernetes 標準クラスターの作成、クラスターへのアプリのデプロイ、および Kibana で高度な分析を行うための {{site.data.keyword.Bluemix_notm}} でのログの照会を実行できる権限を持つ、{{site.data.keyword.Bluemix_notm}} アカウントのメンバーまたは所有者になります。

    {{site.data.keyword.Bluemix_notm}} のユーザー ID に、以下のポリシーが割り当てられている必要があります。
    
    * *エディター*、*オペレーター*、または*管理者* の許可が設定された、{{site.data.keyword.containershort}} 用の IAM ポリシー。
    * {{site.data.keyword.loganalysisshort}} サービスがプロビジョンされるスペースの、*開発者* の許可が設定された CF 役割。
    
    詳しくは、[IBM Cloud UI を使用してユーザーに IAM ポリシーを割り当てる](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account)および [IBM Cloud UI を使用して、スペース・ログを表示する許可をユーザーに付与する](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space)を参照してください。

2. コマンド・ラインから Kubernetes クラスターの管理およびアプリのデプロイを実行できる端末セッションを用意します。 このチュートリアルの例では Ubuntu Linux システムを使用しています。

3. {{site.data.keyword.containershort}} および {{site.data.keyword.loganalysisshort}} の処理を行うための CLI を Ubuntu システムにインストールします。

    * {{site.data.keyword.Bluemix_notm}} CLI をインストールします。 {{site.data.keyword.containershort}} での Kubernetes クラスターの作成と管理、およびクラスターへのコンテナー化アプリのデプロイを行うための {{site.data.keyword.containershort}} CLI をインストールします。 詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)を参照してください。
    
    * {{site.data.keyword.loganalysisshort}} CLI をインストールします。 詳しくは、『[Log Analysis CLI の構成 (IBM Cloud プラグイン)](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli)』を参照してください。
    
4. 米国南部地域で、ご使用のアカウント内の **dev** というスペースにアクセスできるようにします。 

    クラスター内で使用可能なログは、このスペースに関連付けられているスペース・ドメインに転送されるように構成されます。 
    
    このスペースで、{{site.data.keyword.loganalysisshort}} サービスをプロビジョンします。
    
    {{site.data.keyword.loganalysisshort}} サービスをプロビジョンできるように、このスペースの**開発者**許可が必要です。
    
    このチュートリアルで使用する組織の名前は、**MyOrg** です。

    
 

## ステップ 1: Kubernetes クラスターをプロビジョンする
{: #step25}

以下のステップを実行します。

1. 標準の Kubernetes クラスターを作成します。

   詳しくは、『[クラスターの作成](/docs/containers?topic=containers-cs_cluster_tutorial#cs_cluster_tutorial)』を参照してください。

2. 端末でクラスター・コンテキストをセットアップします。 コンテキストを設定すると、Kubernetes クラスターを管理し、Kubernetes クラスターにアプリケーションをデプロイできるようになります。

    {{site.data.keyword.Bluemix_notm}}で、作成したクラスターに関連付けられた、地域、組織、およびスペースにログインします。 詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。

	{{site.data.keyword.containershort}} サービス・プラグインを初期化します。

	```
	ibmcloud cs init
	```
	{: codeblock}

    端末コンテキストをクラスターに設定します。
    
	```
	ibmcloud cs cluster-config MyCluster
	```
	{: codeblock}

    このコマンド実行の出力では、構成ファイルへのパスを設定するためにご使用の端末で実行する必要のあるコマンドが示されます。 以下に例を示します。

	```
	export KUBECONFIG=/Users/ibm/.bluemix/plugins/container-service/clusters/MyCluster/kube-config-hou02-MyCluster.yml
	```
	{: codeblock}

    ご使用の端末で環境変数を設定するコマンドをコピーして貼り付け、**Enter** を押します。



## ステップ 2: ログを自動的に {{site.data.keyword.loganalysisshort}} サービスに転送するためにクラスターを構成する
{: #step26}

アプリがデプロイされると、ログは {{site.data.keyword.containershort}} によって自動的に収集されます。 ただし、ログは、自動的には {{site.data.keyword.loganalysisshort}} サービスに転送されません。 以下を定義する 1 つ以上のロギング構成をクラスター内に作成する必要があります。

* ログの転送先。 ログは、アカウント・ドメインまたはスペース・ドメインに転送できます。
* 分析のために {{site.data.keyword.loganalysisshort}} サービスに転送されるログの種類。


ロギング構成を定義する前に、クラスター内の現行ロギング構成定義を確認してください。 次のコマンドを実行します。

```
$ ibmcloud cs logging-config-get ClusterName
```
{: codeblock}

ここで、*ClusterName* はクラスターの名前です。

例えば、クラスター *mycluster* に対して定義されているロギング構成は、以下のようになります。 

```
$ ibmcloud cs logging-config-get mycluster
Retrieving cluster mycluster logging configurations...
OK
Id                                     Source       Namespace   Host                                Port   Org            Space   Protocol   Paths   
13ded2c0-83f5-4cc5-8de7-1e34e1287f34   worker       -           ingest.logging.ng.bluemix.net       9091   Demo_Org       dev     ibm        /var/log/syslog,/var/log/auth.log   
ae249c04-a3a9-4c29-a890-22d8da7bd1b2   container    *           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        -   
31739fc1-42e2-4b66-ac57-6a32091c257a   ingress      -           ingest.logging.ng.bluemix.net       9091   Demo_Org.      dev     ibm        /var/log/alb/ids/*.log,/var/log/alb/ids/*.err,/var/log/alb/customerlogs/*.log,/var/log/alb/customerlogs/*.err   
6b8cfe89-4959-448d-898b-c3b0584eca71   kubernetes   -           ingest-eu-fra.logging.bluemix.net   9091   Demo_Org.      dev     ibm        /var/log/kubelet.log,/var/log/kube-proxy.log   

```
{: screen}

ロギング構成を定義できるログ・ソースのリストを確認するには、[ログ・ソース](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_sources)を参照してください。


### stderr および stdout のログを {{site.data.keyword.loganalysisshort}} サービスに転送するためのクラスターの構成
{: #containerstd}


stdout および stderr のログをスペース・ドメインに送信するには、以下のステップを実行します。ここで、送信先は米国南部地域で、組織名は *MyOrg*、スペース名は *dev* です。

1. クラスター構成を追加する許可がユーザー ID にあることを確認します。 クラスターを管理する許可が設定された {{site.data.keyword.containershort}} の IAM ポリシーを持つユーザーのみが、この機能を有効にすることができます。 *管理者*、*オペレーター* のいずれかの役割が必要です。

    ユーザー ID に、クラスターを管理するために割り当てられた IAM ポリシーがあることを確認するには、以下のステップを実行します。
    
    1. {{site.data.keyword.Bluemix_notm}} コンソールにログインします。 Web ブラウザーを開き、{{site.data.keyword.Bluemix_notm}} ダッシュボード ([http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window}) を起動します。ユーザー ID とパスワードでログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

    2. メニュー・バーから、**「管理」>「アカウント」>「ユーザー」**をクリックします。  「*ユーザー*」ウィンドウに、現在選択されているアカウントにおけるユーザーのリストが、E メール・アドレスと共に表示されます。
	
    3. ユーザー ID を選択し、その ユーザー ID に {{site.data.keyword.containershort}} のポリシーがあることを検証します。

    許可が必要な場合は、アカウント所有者またはアカウント管理者に連絡してください。 アカウント所有者、または、ポリシーを割り当てる許可を持つユーザーのみが、このステップを実行できます。

2. クラスター・ロギング構成を作成します。 *stdout* および *stderr* ログ・ファイルを {{site.data.keyword.loganalysisshort}} サービスに送信するには、以下のコマンドを実行します。

    ```
    ibmcloud cs logging-config-create ClusterName --logsource container --namespace '*' --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    各部分の説明: 

    * *ClusterName* はクラスターの名前です。
    * *EndPoint* は、{{site.data.keyword.loganalysisshort}} サービスがプロビジョンされた地域内のロギング・サービスの URL です。 エンドポイントのリストについては、[エンドポイント](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)を参照してください。
    * *OrgName* は、スペースがある組織の名前です。
    * *SpaceName* は、{{site.data.keyword.loganalysisshort}} サービスがプロビジョンされたスペースの名前です。


例えば、stdout および stderr のログを米国南部地域のスペース dev に転送するロギング構成を作成するには、次のコマンドを実行します。

```
ibmcloud cs logging-config-create mycluster --logsource container --type ibm --namespace '*' --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}




### ワーカー・ログを {{site.data.keyword.loganalysisshort}} サービスに転送するためのクラスターの構成
{: #workerlogs }

ワーカー・ログをスペース・ドメインに送信するには、以下のステップを実行します。ここで、送信先は米国南部地域で、組織名は *MyOrg*、スペース名は *dev* です。

1. クラスター構成を追加する許可がユーザー ID にあることを確認します。 クラスターを管理する許可が設定された {{site.data.keyword.containershort}} の IAM ポリシーを持つユーザーのみが、この機能を有効にすることができます。 *管理者*、*オペレーター* のいずれかの役割が必要です。

    ユーザー ID に、クラスターを管理するために割り当てられた IAM ポリシーがあることを確認するには、以下のステップを実行します。
    
    1. {{site.data.keyword.Bluemix_notm}} コンソールにログインします。 Web ブラウザーを開き、{{site.data.keyword.Bluemix_notm}} ダッシュボード ([http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window}) を起動します。ユーザー ID とパスワードでログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

    2. メニュー・バーから、**「管理」>「アカウント」>「ユーザー」**をクリックします。  「*ユーザー*」ウィンドウに、現在選択されているアカウントにおけるユーザーのリストが、E メール・アドレスと共に表示されます。
	
    3. ユーザー ID を選択し、その ユーザー ID に {{site.data.keyword.containershort}} のポリシーがあることを検証します。

    許可が必要な場合は、アカウント所有者またはアカウント管理者に連絡してください。 アカウント所有者、または、ポリシーを割り当てる許可を持つユーザーのみが、このステップを実行できます。

2. クラスター・ロギング構成を作成します。 */var/log/syslog* および */var/log/auth.log* ログ・ファイルを {{site.data.keyword.loganalysisshort}} サービスに送信するには、以下のコマンドを実行します。

    ```
    ibmcloud cs logging-config-create ClusterName --logsource worker --type ibm --hostname EndPoint --port 9091 --org OrgName --space SpaceName 
    ```
    {: codeblock}

    各部分の説明: 

    * *ClusterName* はクラスターの名前です。
    * *EndPoint* は、{{site.data.keyword.loganalysisshort}} サービスがプロビジョンされた地域内のロギング・サービスの URL です。 エンドポイントのリストについては、[エンドポイント](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls)を参照してください。
    * *OrgName* は、スペースがある組織の名前です。
    * *SpaceName* は、{{site.data.keyword.loganalysisshort}} サービスがプロビジョンされたスペースの名前です。

    
例えば、ワーカー・ログを米国南部地域のスペース・ドメインに転送するロギング構成を作成するには、次のコマンドを実行します。

```
ibmcloud cs logging-config-create mycluster --logsource worker  --type ibm --hostname ingest.logging.ng.bluemix.net --port 9091 --org MyOrg --space dev 
```
{: screen}



## ステップ 3: スペース・ドメイン内のログを表示するための許可をユーザーに付与する
{: #step33}

スペース内のログを表示する許可をユーザーに付与するには、そのユーザーがそのスペース内で {{site.data.keyword.loganalysisshort}} サービスを使用して実行できるアクションを記述した Cloud Foundry 役割をそのユーザーに割り当てる必要があります。 

{{site.data.keyword.loganalysisshort}} サービスを使用して作業する許可をユーザーに付与するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} コンソールにログインします。

    Web ブラウザーを開き、{{site.data.keyword.Bluemix_notm}} ダッシュボード: [http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window} を起動します。
	
	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

2. メニュー・バーから、**「管理」>「アカウント」>「ユーザー」**をクリックします。 

    「*ユーザー*」ウィンドウに、現在選択されているアカウントにおけるユーザーのリストが、E メール・アドレスと共に表示されます。
	
3. ユーザーがアカウントのメンバーである場合、リストからユーザー名を選択するか、または、**「アクション」**メニューから*「ユーザーの管理」*をクリックします。

    ユーザーがアカウントのメンバーでない場合、『[ユーザーの招待](/docs/iam?topic=iam-iamuserinv#iamuserinv)』を参照してください。

4. **「Cloud Foundry アクセス権限」**を選択してから、組織を選択します。

    その組織で使用可能なスペースのリストが表示されます。

5. スペースを選択します。 次に、メニュー・アクションから**「スペースの役割の編集」**を選択します。

    米国南部のスペースが見つからない場合は、続行する前にスペースを作成してください。

6. *開発者* を選択します。

    1 つ以上の役割を選択できます。 
    
    有効な役割は、*管理者*、*開発者*、および*監査員* です。
	
7. **「役割の保存」**をクリックします。


## ステップ 4: {{site.data.keyword.containershort_notm}} キー所有者に許可を付与する
{: #step52}

クラスター・ログがスペースに転送されるためには、{{site.data.keyword.containershort_notm}} キー所有者は以下の許可を持っている必要があります。

* *管理者* 許可が設定された、{{site.data.keyword.loganalysisshort}} サービス用の IAM ポリシー。
* ログが転送される組織およびスペースでの Cloud Foundry (CF) 許可。 コンテナーのキー所有者には、組織の *orgManager* 役割と、スペースの *SpaceManager* および*開発者* の役割が必要です。

以下のステップを実行します。

1. {{site.data.keyword.containershort}} キー所有者であるアカウントのユーザーを識別します。 端末から次のコマンドを実行します。

    ```
    ibmcloud cs api-key-info ClusterName
    ```
    {: codeblock}
    
    ここで、*ClusterName* はクラスターの名前です。

2. {{site.data.keyword.containershort}} キー所有者として識別されたユーザーに、組織の *orgManager* 役割とスペースの *SpaceManager* および*開発者* の役割があることを確認します。

    {{site.data.keyword.Bluemix_notm}} コンソールにログインします。 Web ブラウザーを開き、{{site.data.keyword.Bluemix_notm}} ダッシュボード ([http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window}) を起動します。ユーザー ID とパスワードでログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

    メニュー・バーから、**「管理」>「アカウント」>「ユーザー」**をクリックします。  「*ユーザー*」ウィンドウに、現在選択されているアカウントにおけるユーザーのリストが、E メール・アドレスと共に表示されます。
	
    ユーザーの ID を選択し、ユーザーに組織の *orgManager* 役割とスペースの *SpaceManager* および*開発者* の役割があることを確認します。

    ユーザーに正しい許可がない場合、ユーザーに次の許可を付与します。組織の *orgManager* 役割と、スペースの *SpaceManager* および*開発者* の役割。 詳しくは、[IBM Cloud UI を使用して、スペース・ログを表示する許可をユーザーに付与する](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space)を参照してください。
    
3. {{site.data.keyword.containershort}} キー所有者として識別されたユーザーに、*管理者* の許可が設定された、{{site.data.keyword.loganalysisshort}} サービス用 IAM ポリシーがあることを検証します。

    メニュー・バーから、**「管理」>「アカウント」>「ユーザー」**をクリックします。  「*ユーザー*」ウィンドウに、現在選択されているアカウントにおけるユーザーのリストが、E メール・アドレスと共に表示されます。
	
    ユーザーの ID を選択し、ユーザーに IAM ポリシーが設定されていることを検証します。 

    ユーザーが IAM ポリシーを持っていない場合、『[IBM Cloud UI を使用してユーザーに IAM ポリシーを割り当てる](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account)』を参照してください。

4. ロギング構成を更新します。 次のコマンドを実行します。
    
    ```
    ibmcloud cs logging-config-refresh ClusterName
    ```
    {: codeblock}
        
    ここで、*ClusterName* はクラスターの名前です。
	



## ステップ 5: Kubernetes クラスターにサンプル・アプリをデプロイして、stdout にコンテンツを生成する
{: #step53}

Kubernetes クラスター内でサンプル・アプリをデプロイし、実行します。 [レッスン 1: アプリの 1 つのインスタンスを Kubernetes クラスターにデプロイする](/docs/containers?topic=containers-cs_apps_tutorial#cs_apps_tutorial_lesson1)のチュートリアルにあるステップを実行して、サンプル・アプリをデプロイします。

以下のアプリは Hello World Node.js アプリです。

```
var express = require('express')
var app = express()

app.get('/', function(req, res) {
  res.send('Hello world! Your app is up and running in a cluster!\n')
})
app.listen(8080, function() {
  console.log('Sample app is listening on port 8080.')
})
```
{: screen}

このサンプル・アプリでは、ブラウザーでアプリをテストすると、アプリはメッセージ `Sample app is listening on port 8080.` を標準出力に書き込みます。






## ステップ 6: Kibana でログ・データを表示する
{: #step6}

以下のステップを実行します。

1. ブラウザーで Kibana を起動します。 

    Kibana の起動方法について詳しくは、『[Web ブラウザーから Kibana へのナビゲート](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser)』を参照してください。

    あるクラスターのログ・データを分析するには、そのクラスターが作成された Cloud Public 地域の Kibana にアクセスする必要があります。 
    
    例えば、米国南部地域で Kibana を起動するには、次の URL を入力します。
	
	```
	https://logging.ng.bluemix.net/ 
	```
	{: codeblock}
	
    Kibana が開きます。
    
    **注:** クラスター・ログを転送する地域で Kibana を起動していることを確認してください。 地域ごとの URL については、[ロギング・エンドポイント](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana)を参照してください。
    	
2. スペース・ドメイン内で使用可能なログ・データを表示するには、以下のステップを実行します。

    1. Kibana で、自分のユーザー ID をクリックします。 スペースを設定するためのビューが開きます。
    
    2. スペースを使用できるアカウントを選択します。 
    
    3. ドメイン **space** を選択します。
    
    4. スペースを使用できる組織 *MyOrg* を選択します。
    
    5. スペース *dev* を選択します。
    
    
3. **「Discover」**ページで、表示されるイベントを確認します。 
        
    *「Available fields」*セクションには、フィールドのリストが表示されます。これらのフィールドを使用して、新しい照会を定義したり、ページに表示される表にリストされる項目をフィルター操作したりできます。
    
    以下の表に、アプリケーション・ログを分析するときに新しい検索照会を定義するために使用できるフィールドの一部を示します。 この表には、サンプル・アプリによって生成されるイベントに対応するサンプル値も含まれています。
 
    <table>
              <caption>表 2. コンテナー・ログの共通フィールド </caption>
               <tr>
                <th align="center">フィールド</th>
                <th align="center">説明</th>
                <th align="center">例</th>
              </tr>
              <tr>
                <td>*ibm-containers.region_str*</td>
                <td>このフィールドの値は、このログ項目が収集される {{site.data.keyword.Bluemix_notm}} 地域に対応します。</td>
                <td>us-south</td>
              </tr>
			  <tr>
                <td>*ibm-containers.account_id_str*</td>
                <td>アカウント ID</td>
                <td></td>
              </tr>
			  <tr>
                <td>*ibm-containers.cluster_id_str*</td>
                <td>クラスター ID。</td>
                <td></td>
              </tr>
              <tr>
                <td>*ibm-containers.cluster_name_str*</td>
                <td>クラスター ID</td>
                <td></td>
              </tr>
			  <tr>
                <td>*kubernetes.namespace_name_str*</td>
                <td>名前空間名</td>
                <td>デフォルト値は *default* です。</td>
              </tr>
              <tr>
                <td>*kubernetes.container_name_str*</td>
                <td>コンテナー名</td>
                <td>hello-world-deployment</td>
              </tr>
              <tr>
                <td>*kubernetes.labels.label_name*</td>
                <td>ラベル・フィールドはオプションです。 ラベルはなくてもよく、複数あってもかまいません。 各ラベルは接頭部 `kubernetes.labels.` で始まり、*label_name* が続きます。 </td>
                <td>サンプル・アプリでは、次の 2 つのラベルがあります。 <br>* *kubernetes.labels.pod-template-hash_str* = 3355293961 <br>* *kubernetes.labels.run_str* =	hello-world-deployment  </td>
              </tr>
              <tr>
                <td>*stream_str*</td>
                <td>ログのタイプ。</td>
                <td>*stdout*、*stderr*</td>
              </tr>
        </table>
     
Kubernetes クラスターに関係するその他の検索フィールドについて詳しくは、[ログの検索](/docs/services/CloudLogAnalysis/containers?topic=cloudloganalysis-containers_kubernetes#log_search)を参照してください。


## ステップ 7: Kibana で Kubernetes クラスター名によってデータをフィルタリングする
{: #step7}
    
「*Discovery*」ページに表示される表に、分析に使用できるすべてのエントリーが表示されます。 リストされる項目は、*「Search」*バーに表示される検索照会に対応します。 ページに対して構成された期間内のすべての項目を表示するには、アスタリスク (*) を使用します。
    
例えば、Kubernetes クラスター名によってデータをフィルター操作するために、*「Search」*バーの照会を変更するとします。 この場合、次のようにしてカスタム・フィールド *kubernetes.cluster_name_str* に基づくフィルターを追加します。
    
1. **「Available fields」**セクションで、フィールド *kubernetes.cluster_name_str* を選択します。 このフィールドの有効な値のサブセットが表示されます。    
    
2. ログ分析の対象となるクラスターに対応する値を選択します。 
    
    値を選択すると、*「Search」*バーにフィルターが追加され、表には、選択したばかりの基準に一致する項目のみが表示されるようになります。     
   

**注:** 

クラスター名が表示されない場合は、いずれのクラスター名にも対応するフィルターを追加してください。 次に、フィルターの編集シンボルを選択します。    
    
以下の照会が表示されます。
    
```
	{
        "query": {
          "match": {
            "kubernetes.cluster_name_str": {
              "query": "cluster1",
              "type": "phrase"
            }
          }
        }
      }
```
{: screen}

クラスターの名前 (*cluster1*) を、ログ・データを表示するクラスターの名前 *mycluster* に置き換えます。
        
データが何も表示されない場合は、時間フィルターを変更してみてください。 詳しくは、『[時間フィルターの設定](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)』を参照してください。

詳しくは、『[Kibana でのログのフィルタリング](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#filter_logs)』を参照してください。


## {{site.data.keyword.containershort_notm}} 参照資料
{: reference}

CLI コマンド:

* [ibmcloud cs api-key-info](/docs/containers?topic=containers-cs_cli_reference#cs_api_key_info)
* [ibmcloud cs logging-config-create](/docs/containers?topic=containers-cs_cli_reference#cs_logging_create)
* [ibmcloud cs logging-config-get](/docs/containers?topic=containers-cs_cli_reference#cs_logging_get)
* [ibmcloud cs logging-config-update](/docs/containers?topic=containers-cs_cli_reference#cs_logging_update)
* [ibmcloud cs logging-config-rm](/docs/containers?topic=containers-cs_cli_reference#cs_logging_rm)
* [ibmcloud cs logging-config-refresh](/docs/containers?topic=containers-cs_cli_reference#cs_logging_refresh)

