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


# プランの変更
{: #change_plan}

{{site.data.keyword.Bluemix_notm}} UI を介して、または、`ibmcloud service update` コマンドを実行することによって、{{site.data.keyword.loganalysisshort}} サービス・プランを変更できます。 プランはいつでもアップグレードまたは削減することができます。
{:shortdesc}

## UI を使用したサービス・プランの変更
{: #change_plan_ui}

{{site.data.keyword.Bluemix_notm}} UI でサービス・プランを変更するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} ([http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window}) にログインします。 

2. {{site.data.keyword.loganalysisshort}} サービスを使用可能な地域、組織、およびスペースを選択します。  

3. {{site.data.keyword.Bluemix_notm}} *ダッシュボード*から {{site.data.keyword.loganalysisshort}} サービス・インスタンスをクリックします。 
    
4. {{site.data.keyword.loganalysisshort}} ダッシュボードで**「プラン」**タブを選択します。

    現在のプランに関する情報が表示されます。
	
5. プランをアップグレードまたは削減するため、新しいプランを選択します。 

6. **「保存」**をクリックします。




## CLI を使用したサービス・プランの変更
{: #change_plan_cli}

Bluemix で CLI を介してサービス・プランを変更するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
	
2. `ibmcloud service list` コマンドを実行して、現在のプランを確認し、スペースで使用可能なサービスのリストから {{site.data.keyword.loganalysisshort}} サービス名を取得します。 

    プランを変更する際、**name** フィールドの値を使用する必要があります。 

    以下に例を示します。
	
	```
	$ ibmcloud service list
    Invoking 'cf services'...

    Getting services in org MyOrg / space dev as xxx@ibm.com...
    OK

    name                           service                  plan             bound apps            last operation
    Log Analysis-m2                ibmLogAnalysis           premium                                update succeeded
    ```
	{: screen}
    
3. プランをアップグレードまたは削減します。 `ibmcloud service update` コマンドを実行します。
    
	```
	ibmcloud service update service_name [-p new_plan]
	```
	{: codeblock}
	
	各部分の説明: 
	
	* *service_name* は、サービスの名前です。 `ibmcloud service list` コマンドを実行して値を取得できます。
	* *new_plan* は、プランの名前です。
	
	次の表に、各種プランおよびサポートされている値を示します。
	
	<table>
	  <caption>表 1. プランのリスト</caption>
	  <tr>
	    <th>プラン</th>
	    <th>名前</th>
	  </tr>
	  <tr>
	    <td>ライト</td>
	    <td>standard</td>
	  </tr>
	  <tr>
	    <td>Log Collection</td>
	    <td>premium</td>
	  </tr>
	  <tr>
	    <td>Log Collectionと 2 GB/日の検索</td>
	    <td>premiumsearch2</td>
	  </tr>
	  <tr>
	    <td>Log Collectionと 5 GB/日の検索</td>
	    <td>premiumsearch5</td>
	  </tr>
	  <tr>
	    <td>Log Collectionと 10 GB/日の検索</td>
	    <td>premiumsearch10</td>
	  </tr>
	</table>
	
	例えば、プランを削減して*ライト*・プランにするには、次のコマンドを実行します。
	
	```
	ibmcloud service update "Log Analysis-m2" -p standard
    Updating service instance Log Analysis-m2 as xxx@ibm.com...
    OK
	```
	{: screen}

4. 新規プランに変更されたことを検証します。 `ibmcloud service list` コマンドを実行します。

  ```
	ibmcloud service list
	```
	{: codeblock}






