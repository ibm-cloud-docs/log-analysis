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


# UAA トークンの取得
{: #auth_uaa}

スペース・内にあるログを {{site.data.keyword.loganalysisshort}} API を使用して管理するには、認証トークンを使用する必要があります。
{:shortdesc}

		
## UAA トークンの取得
{: #uaa_cli}


許可トークンを取得するには、以下の手順を実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix}}CLI のダウンロードとインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)を参照してください。
   
   CLI がインストールされている場合は、次のステップに進みます。
    
2. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。
	
3. `ibmcloud iam oauth-token` コマンドを実行して、{{site.data.keyword.Bluemix_notm}} UAA トークンを取得します。

    ```
	ibmcloud iam oauth-token
	```
	{: codeblock}
	
	この出力は、そのスペースおよび組織でユーザー ID を認証するために使用する必要がある UAA トークンを返します。
	

**注:** トークンを使用する場合、API 呼び出しで渡すトークンの値から *Bearer* を削除してください。
