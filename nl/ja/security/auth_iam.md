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


# IAM トークンの取得
{: #auth_iam1}

アカウント・ドメイン内にあるログを {{site.data.keyword.loganalysisshort}} API を使用して管理するには、認証トークンを使用する必要があります。 {{{site.data.keyword.Bluemix_notm}} CLI を使用して IAM トークンを取得します。 トークンには有効期限があります。 
{:shortdesc}


## IAM トークンの取得
{: #iam_token_cli}

{{site.data.keyword.Bluemix_notm}} CLI を使用して許可トークンを取得するには、端末から以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix}}CLI のダウンロードとインストール』](/docs/cli/index.html#overview)を参照してください。
   
   CLI がインストールされている場合は、次のステップに進みます。
    
2. {{site.data.keyword.Bluemix_notm}} の地域にログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
	
3. `ibmcloud iam oauth-tokens` コマンドを実行して、IAM トークンを取得します。

    ```
	ibmcloud iam oauth-tokens
	```
	{: codeblock}
	
	この出力は、そのスペースおよび組織でユーザー ID を認証するために使用する必要がある IAM トークンを返します。 この IAM トークンを「`$iam_token`」などのシェル変数にエクスポートできます。



**注:** トークンを使用する場合、API 呼び出しで渡すトークンの値から *Bearer* を削除してください。

