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


# ロギング・トークンの取得
{: #logging_token}

ログを {{site.data.keyword.loganalysisshort}} サービスに送信するには、ロギング・トークンを取得します。 
{:shortdesc}


## {{site.data.keyword.loganalysisshort}} CLI を使用して、ログをスペースに送信するためのロギング・トークンを取得する 
{: #logging_token_la_cloud_cli}

{{site.data.keyword.loganalysisshort}} サービスにログを送信するために使用できるロギング・トークンを取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のダウンロードとインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)を参照してください。
   
   CLI がインストールされている場合は、次のステップに進みます。
    
2. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。
	
3. 次のコマンドを実行します。

    ```
	ibmcloud logging token-get
	```
	{: codeblock}

出力でロギング・トークンが返されます。


## {{site.data.keyword.Bluemix_notm}} CLI を使用して、ログをスペースに送信するためのロギング・トークンを取得する 
{: #logging_token_cloud_cli}

{{site.data.keyword.loganalysisshort}} サービスにログを送信するために使用できるロギング・トークンを取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のダウンロードとインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)を参照してください。
   
   CLI がインストールされている場合は、次のステップに進みます。
    
2. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。
	
3. {{site.data.keyword.loganalysisshort}} サービスがプロビジョンされたスペース内でサービス・キーを作成します。 次のコマンドを実行します。

    スペース内の {{site.data.keyword.loganalysisshort}} インスタンスの名前を取得するため、サービスをリストします。
	
    ```
	ibmcloud service list
	```
	{: codeblock}
	
	例えば次のようにします。
	
	```
	ibmcloud service list
    Invoking 'cf services'...

    Getting services in org lopezdsr_org / space dev as xxx@yyyy...
    OK

    name              service          plan       bound apps   last operation
    Log Analysis-vg   ibmloganalysis   standard                create succeeded
    ```
	{: screen}
	
	キーを作成します。 servicename には **name** の値を使用し、キーの名前を入力してください。
	
	```
	ibmcloud service key-create servicename KeyName 
	```
	{: codeblock}
	
	以下に例を示します。
	
	```
	ibmcloud service key-create "Log Analysis-vg" mykey2
    Invoking 'cf create-service-key Log Analysis-vg mykey2'...

    Creating service key mykey2 for service instance Log Analysis-vg as xxx@yyyy...
    OK
    ```
	{: screen}
	
4. ロギング・トークンを取得します。 次のコマンドを実行します。
	
	```
	ibmcloud service key-show name Keyname
	```
	{: codeblock}
	
	以下に例を示します。 
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" 
    Invoking 'cf service-key Log Analysis-vg mykey2'...

    Getting key mykey2 for service instance Log Analysis-vg as xxx@yyyy...

    {
     "LOG_INGESTION_MTLJ_URL": "https://ingest-eu-fra.logging.bluemix.net:9091",
     "logging_token": "sdtghyrtfde4",
     "space_id": "12345678-avfg-erft-b1f2-2efrtgcb1744"
    }
    ```
	{: screen}
	
	ロギング・トークンを取得するため、以下のコマンドを実行できます。
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" | tail -n +4 | jq -r .logging_token
    sdtghyrtfde4
	```
	{: screen}


	
## Log Analysis API を使用して、ログをスペースに送信するためのロギング・トークンを取得する
{: #logging_token_api}


{{site.data.keyword.loganalysisshort}} サービスにログを送信するために使用できるロギング・トークンを取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} CLI をインストールします。

   詳しくは、[『{{site.data.keyword.Bluemix_notm}}CLI のダウンロードとインストール』](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)を参照してください。
   
   CLI がインストールされている場合は、次のステップに進みます。
    
2. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)』を参照してください。
	
3. [UAA トークン](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#uaa_cli)を取得します。

    例えば、`ibmcloud cf oauth-token` コマンドを実行して、UAA トークンを取得します。

    ```
	ibmcloud cf oauth-token
	```
	{: codeblock}
	
	この出力は、そのスペースおよび組織でユーザー ID を認証するために使用する必要がある UAA トークンを返します。

4. スペースの GUID を取得します。

   詳しくは、『[スペースの GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#space_guid2)』を参照してください。  
	
5. 変数 TOKEN および SPACEID をエクスポートします。

    * *TOKEN* は、前のステップで取得した OAuth トークン (Bearer を除く) です。
	
	* *SPACEID* は、前のステップで取得した、スペースの GUID です。 
		
	以下に例を示します。
	
	```
	export TOKEN="eyJhbGciOiJI....cGFzc3dvcmQiLCJjZiIsInVhYSIsIm9wZW5pZCJdfQ.JaoaVudG4jqjeXz6q3JQL_SJJfoIFvY8m-rGlxryWS8"
	export SPACEID="667fb895-abcd-defg-aaaa-cf4587341095"
	```
	{: screen}
	
6. ロギング・トークンを取得します。 次のコマンドを実行します。
 
    ```
	curl -k -X GET  --header "X-Auth-Token: ${TOKEN}"  --header "X-Auth-Project-Id: s-${SPACEID}"  LOGGING_ENDPOINT/token
    ```
    {: codeblock}	
	
	各部分の説明:
	* SPACEID は、サービスが実行されているスペースの GUID です。
	* TOKEN は、前のステップで取得した UAA トークンから bearer 接頭部を除外したものです。
	* LOGGING_ENDPOINT は、組織およびスペースが使用可能な {{site.data.keyword.Bluemix_notm}} 地域の {{site.data.keyword.loganalysisshort}} エンドポイントです。 LOGGING_ENDPOINT は地域ごとに異なります。 様々なエンドポイントの URL を確認するには、『[エンドポイント](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#endpoints)』を参照してください。.
	
    このコマンドは、そのスペースにログを送信するめに使用する必要のあるロギング・トークンを返します。
	
