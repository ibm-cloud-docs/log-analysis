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


# Log Analysis サービスのプロビジョン
{: #provision}

{{site.data.keyword.loganalysisshort}} サービスは、{{site.data.keyword.Bluemix}} UI かコマンド・ラインからプロビジョンできます。
{:shortdesc}


## UI からのプロビジョン
{: #ui}

{{site.data.keyword.Bluemix_notm}} で {{site.data.keyword.loganalysisshort}} サービスのインスタンスをプロビジョンするには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} アカウントにログインします。

    {{site.data.keyword.Bluemix_notm}} ダッシュボードは、[http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window} にあります。
    
	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

2. **「カタログ」**をクリックします。 {{site.data.keyword.Bluemix_notm}} で使用可能なサービスのリストが開きます。

3. **「開発者用ツール」**カテゴリーを選択して、表示されたサービスのリストをフィルタリングします。

4. **「Log Analysis」**タイルをクリックします。

5. サービス・プランを選択します。 デフォルトでは、**「ライト」**プランが設定されています。

    サービス・プランについて詳しくは、『[サービス・プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。
	
6. **「作成」**をクリックして、ログインしている {{site.data.keyword.Bluemix_notm}} スペースで {{site.data.keyword.loganalysisshort}} サービスをプロビジョンします。
  
 

## CLI からのプロビジョン
{: #cli}

{{site.data.keyword.Bluemix_notm}} でコマンド・ラインを使用して {{site.data.keyword.loganalysisshort}} サービスのインスタンスをプロビジョンするには、以下のステップを実行します。

1. [前提条件] {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のインストール』](/docs/cli/index.html#overview)を参照してください。
   
   CLI がインストールされている場合は、次のステップに進みます。
    
2. サービスをプロビジョンしたい、{{site.data.keyword.Bluemix_notm}} の地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
	
3. `ibmcloud service create` コマンドを実行して、インスタンスをプロビジョンします。

    ```
	ibmcloud service create service_name service_plan service_instance_name
	```
	{: codeblock}
	
	説明
	
	* service_name はサービスの名前 (**ibmLogAnalysis**) です。
	* service_plan はサービス・プラン名です。 プランのリストについては、『[サービス・プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。
	* service_instance_name は、作成する新規サービス・インスタンスに使用する名前です。

	例えば、ライト・プランで {{site.data.keyword.loganalysisshort}} サービスのインスタンスを作成するには、以下のコマンドを実行します。
	
	```
	ibmcloud service create ibmLogAnalysis standard my_logging_svc
	```
	{: codeblock}
	
4. サービスが正常に作成されたことを確認します。 次のコマンドを実行します。

    ```	
	ibmcloud service list
	```
	{: codeblock}
	
	このコマンドの実行による出力は以下のようになります。
	
	```
    Getting services in org MyOrg / space MySpace as xxx@yyy.com...
    OK
    
    name                           service                  plan                   bound apps              last operation
    my_logging_svc                ibmLogAnalysis           standard                                        create succeeded
	```
	{: screen}

	



