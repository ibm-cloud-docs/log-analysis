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
{: #configuring_retention_policy1}

Log Collection 内でログが保持される最大日数を定義する保存ポリシーを表示および構成するには、コマンド **cf logging option** を使用します。 デフォルトでは、保存ポリシーは無効にされ、ログは無期限に保持されます。 保存期間を過ぎると、ログは自動的に削除されます。 
{:shortdesc}

複数の保存ポリシーをアカウントに定義できます。 1 つのグローバル・アカウント・ポリシーと、個々のスペース・ポリシーを保有することができます。 アカウント・レベルで設定する保存ポリシーは、ログを保持できる最大日数を設定します。 アカウント・レベルの期間よりも長い期間のスペース保存ポリシーを設定した場合、そのスペースに構成した最新のポリシーが、適用されるポリシーになります。 


## スペースのログ保存ポリシーの無効化
{: #disable_retention_policy_space1}

保存ポリシーを無効化するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 保存期間を無効にするため、保存期間を **-1** に設定します。 コマンドを実行します。

    ```
    ibmcloud cf logging option -r -1
    ```
    {: codeblock}
    
**例**
    
例えば、ID *d35da1e3-b345-475f-8502-cfgh436902a3* のスペースの保存期間を無効にするには、次のコマンドを実行します。

```
ibmcloud cf logging option -r -1
```
{: codeblock}

出力は次のとおりです。

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen} 



## スペースのログ保存ポリシーの確認
{: #check_retention_policy_space1}

スペースに設定されている保存期間を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 保存期間を取得します。 コマンドを実行します。

    ```
    ibmcloud cf logging option
    ```
    {: codeblock}

    出力は次のとおりです。

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## アカウントのすべてのスペースのログ保存ポリシーの確認
{: #check_retention_policy_account}

アカウントの各スペースに設定されている保存期間を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. アカウントの各スペースの保存期間を取得します。 コマンドを実行します。

    ```
    ibmcloud cf logging option -a
    ```
    {: codeblock}

    出力は次のとおりです。

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    | fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## アカウント・レベルのログ保存ポリシーの設定
{: #set_retention_policy_space1}

アカウントの保存期間を表示するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 保存期間を設定します。 コマンドを実行します。

    ```
    ibmcloud cf logging option -r *Number_of_days* - a
    ```
    {: codeblock}
    
    ここで、*Number_of_days* は、ログを保持する日数を定義する整数です。 
    
    
**例**
    
例えば、アカウントのすべてのタイプのログを 15 日間だけ保持するには、次のコマンドを実行します。

```
ibmcloud cf logging option -r 15 -a
```
{: codeblock}

出力では、以下のように、保存期間についての情報を含む項目がアカウントのスペースごとにリストされます。

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        15 |
+--------------------------------------+-----------+
| fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
+--------------------------------------+-----------+
```
{: screen}

## スペースのログ保存ポリシーの設定
{: #set_retention_policy_account}

スペースの保存期間を表示するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 保存期間を設定します。 コマンドを実行します。

    ```
    ibmcloud cf logging option -r *Number_of_days*
    ```
    {: codeblock}
    
    ここで、*Number_of_days* は、ログを保持する日数を定義する整数です。
    
    
**例**
    
例えば、スペースで使用可能なログを 1 年間保持するには、次のコマンドを実行します。

```
ibmcloud cf logging option -r 365
```
{: codeblock}

出力は次のとおりです。

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |       365 |
+--------------------------------------+-----------+
```
{: screen}


