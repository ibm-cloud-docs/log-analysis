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


# 検索割り当て量および日次使用量の計算
{: #quota}

{{site.data.keyword.loganalysisshort}} サービスのログ・ドメインの割り当て量および現在の日次使用量を取得するために、cURL コマンドを実行できます。 
{:shortdesc}

## CLI を使用した検索割り当て量および日次使用量の計算
{: #quota_cli}

以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} にログインします。

    例えば、米国南部にログインするには、次のコマンドを実行します。

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

2. CLI コマンド `ibmcloud logging quota-usage-show` を実行します。 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    各部分の説明: 

    * 有効な RESOURCE_TYPE 値は、space および account です。
    * RESOURCE_ID は、割り当て使用量を取得したいアカウントまたはスペースの GUID です。


例えば、あるアカウントの割り当て使用量を表示するには、次のコマンドを実行します。

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage   
524288000         0   
```
{: screen}

あるスペースの割り当て使用量を表示するには、次のコマンドを実行します。

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage   
524288000         6774014   
```
{: screen}


## CLI を使用した検索割り当て量履歴の取得
{: #quota_history_cli}


以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} にログインします。

    例えば、米国南部にログインするには、次のコマンドを実行します。

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

2. CLI コマンド `ibmcloud logging quota-usage-show` をパラメーター `-s` を指定して実行します。 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    各部分の説明: 

    * 有効な RESOURCE_TYPE 値は、space および account です。
    * RESOURCE_ID は、割り当て使用量を取得したいアカウントまたはスペースの GUID です。

以下に例を示します。

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}



## API を使用したアカウントの検索割り当て量および日次使用量の計算
{: #account}

以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} にログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

2. アカウントの ID を取得します。 次のコマンドを実行します。

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	アカウントとその GUID のリストが表示されます。
	
	アカウント ID をシェル変数にエクスポートします。 例えば次のようにします。
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. UAA トークンを取得します。 

    詳しくは、『[UAA トークンの取得](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)』を参照してください。

    UAA トークンをシェル変数にエクスポートします。 `Bearer` を含めないでください。 例えば次のようにします。
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. ドメインの割り当て量と現在の使用量を取得します。 次のコマンドを実行します。

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	ここで、*ENDPOINT* は地域ごとに異なります。 地域ごとのエンドポイントのリストについては、『[ロギング・エンドポイント](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints)』を参照してください。
	
	例えば、米国南部地域のアカウントの割り当て量を取得するには、次の cURL コマンドを実行します。
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	結果には、日次の割り当て量および使用量についての情報が含まれます。
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}

	
## API を使用したスペースの検索割り当て量および日次使用量の計算
{: #space1}

以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} にログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

2. スペースの ID を取得します。

    詳しくは、『[スペースの GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid)』を参照してください。
	
	スペース ID をシェル変数にエクスポートします。 例えば次のようにします。
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. UAA トークンを取得します。 

    詳しくは、『[UAA トークンの取得](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)』を参照してください。

    UAA トークンをシェル変数にエクスポートします。 `Bearer` を含めないでください。 例えば次のようにします。
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. ドメインの割り当て量と現在の使用量を取得します。 次のコマンドを実行します。

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	ここで、*ENDPOINT* は地域ごとに異なります。 地域ごとのエンドポイントのリストについては、『[ロギング・エンドポイント](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints)』を参照してください。

    例えば、米国南部地域のスペース・ドメインの割り当て量および使用量を取得するには、以下の cURL コマンドを実行します。
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	結果には、日次の割り当て量および使用量についての情報が含まれます。
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}



