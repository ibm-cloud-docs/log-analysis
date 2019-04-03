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

# ログ保存ポリシーの構成
{: #configuring_retention_policy}

デフォルトでは、保存ポリシーは無効にされ、ログは無期限に保持されます。 保存ポリシーを変更するには、コマンド **ibmcloud logging option-update** を使用します。
{:shortdesc}

**ibmcloud logging option-show** コマンドを使用して、Log Collection 内にログが保持される最大日数を定義する保存ポリシーを表示できます。 

保存ポリシーを設定した場合、保存期間を過ぎると、ログは自動的に削除されます。


## アカウントのログ保存ポリシーの無効化
{: #disable_retention_policy_acc}

保存ポリシーを無効にすると、すべてのログが保持されます。 

保存ポリシーを無効化するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
	
2. アカウント ID を取得します。

    詳しくは、『[アカウントの GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)』を参照してください。
    
3. 保存期間を無効にするため、保存期間を **-1** に設定します。 コマンドを実行します。

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE は、日数を定義する数値です。
    
**例**
    
例えば、ID「*12345677fgh436902a3*」のアカウントの保存期間を無効にするには、次のコマンドを実行します。

```
ibmcloud logging option-update -r account -i 12345677fgh436902a3 -e -1
```
{: codeblock}


## スペースのログ保存ポリシーの無効化
{: #disable_retention_policy_space}

保存ポリシーを無効にすると、すべてのログが保持されます。  

保存ポリシーを無効化するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 保存期間を無効にするため、保存期間を **-1** に設定します。 コマンドを実行します。

    ```
    ibmcloud logging option-show -e RETENTION_VALUE
	```
    {: codeblock}
	
	RETENTION_VALUE は、日数を定義する数値です。
    
**例**
    
例えば、ID *d35da1e3-b345-475f-8502-cfgh436902a3* のスペースの保存期間を無効にするには、次のコマンドを実行します。

```
ibmcloud logging option-update -e -1
```
{: codeblock}


## アカウントのログ保存ポリシーの確認
{: #check_retention_policy_acc}

アカウントに設定されている保存期間を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

2. アカウント ID を取得します。

    詳しくは、『[アカウントの GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)』を参照してください。
    
3. 保存期間を取得します。 コマンドを実行します。

    ```
    ibmcloud logging option-show -r account -i AccountID
    ```
    {: codeblock}

    出力は次のとおりです。

    ```
    ibmcloud logging option-show -r account -i kjskdsjfksjdflkjdsfbbd06461b066
    Showing log options of resource: kjskdsjfksjdflkjdsfbbd06461b066 ...

    Resource ID                              Retention   
    a:kjskdsjfksjdflkjdsfbbd06461b066       30   
	```
    {: screen}
	
## スペースのログ保存ポリシーの確認
{: #check_retention_policy_space}

スペースに設定されている保存期間を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 保存期間を取得します。 コマンドを実行します。

    ```
    ibmcloud logging option-show
    ```
    {: codeblock}

    出力は次のとおりです。

    ```
    ibmcloud logging option-show
    Showing log options of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    SpaceId                                Retention   
    12345678-1234-2edr-a9de-378620d6fab5   30   
	```
    {: screen}
    


## アカウント・レベルのログ保存ポリシーの設定
{: #set_retention_policy_acc}

以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

2. アカウント ID を取得します。

    詳しくは、『[アカウントの GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)』を参照してください。
    
3. 保存期間を設定します。 コマンドを実行します。

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
    ```
    {: codeblock}
    
    ここで、「*RETENTION_VALUE*」は、ログを保持する日数を定義する整数です。 
    
    
**例**
    
例えば、アカウントのすべてのタイプのログを 15 日間だけ保持するには、次のコマンドを実行します。

```
ibmcloud logging option-update -r account -i AccountID -e 15
```
{: codeblock}



## スペースのログ保存ポリシーの設定
{: #set_retention_policy_space}

スペースの保存期間を表示するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 保存期間を設定します。 コマンドを実行します。

    ```
    ibmcloud logging option-update -e RETENTION_VALUE
    ```
    {: codeblock}
    
    ここで、「*RETENTION_VALUE*」は、ログを保持する日数を定義する整数です。
    
    
**例**
    
例えば、スペースで使用可能なログを 1 年間保持するには、次のコマンドを実行します。

```
ibmcloud logging option-update -e 365
```
{: codeblock}




