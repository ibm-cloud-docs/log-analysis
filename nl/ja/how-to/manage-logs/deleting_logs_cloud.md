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

# ログの削除
{: #deleting_logs}

Log Collection からログを削除するには、[ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) コマンドを使用します。 
{:shortdesc}

* 特定期間内のログを削除できます。
* タイプ別にログを削除できます。 各ログ・ファイルのログ項目のタイプは 1 つであることに注意してください。
* スペースのログを削除したり、組織のログを削除したり、アカウント・ドメインのログを削除したりできます。


## 特定の期間のすべてのログの削除
{: #time_range}

特定の期間にスペース・ドメインに保管されたすべてのログを削除するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 次のコマンドを実行して、Log Collection 内にあるログを表示します。

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    以下に例を示します。
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-abcd-4193-aere-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 特定の日に保管されたログを削除します。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	各部分の説明:
	
	* *-s* は、開始日を協定世界時 (UTC) YYYY-MM-DD で設定します。例えば、2006-01-02 です。
    * *-e* は、終了日を協定世界時 (UTC) YYYY-MM-DD で設定します。
    	
	例えば、2017 年 5 月 25 日のログを削除するには、以下のコマンドを実行します。
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## 特定期間のログ・タイプ別のログの削除 
{: #log_type}

特定期間にスペース・ドメインに保管されたログ・タイプ別のログを削除するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 次のコマンドを実行して、Log Collection 内にあるログを表示します。

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    以下に例を示します。
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 特定の日に保管されたログを削除します。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	各部分の説明:
	
	* *-s* は、開始日を協定世界時 (UTC) YYYY-MM-DD で設定します。例えば、2006-01-02 です。
    * *-e* は、終了日を協定世界時 (UTC) YYYY-MM-DD で設定します。
	* *-t* は、ログ・タイプを設定します。
    	
	例えば、2017 年 5 月 25 日のタイプ linux_syslog のログを削除するには、以下のコマンドを実行します。
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## 特定期間のアカウント・ログ・タイプ別のログの削除 
{: #time_range_acc}

以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
	
2. アカウント ID を取得します。

    詳しくは、『[アカウントの GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)』を参照してください。
    
3. 次のコマンドを実行して、アカウント・レベルで Log Collection 内にあるログを表示します。

    ```
    ibmcloud logging log-show  -r account -i AccountID
    ```
    {: codeblock}
    
    以下に例を示します。
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    All                 default
	2017-05-25   2000       76115   All                 linux_syslog,log
    2017-05-26   195678     17639   All                 default,linux_syslog    
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}
	
4. 特定の日に保管されたログを削除します。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType -r account -i AccountID
	```
	{: codeblock}
	
	各部分の説明:
	
	* *-s* は、開始日を協定世界時 (UTC) YYYY-MM-DD で設定します。例えば、2006-01-02 です。
    * *-e* は、終了日を協定世界時 (UTC) YYYY-MM-DD で設定します。
	* *-t* は、ログ・タイプを設定します。
    	
	例えば、アカウント・レベルで Log Collection に保管された、2017 年 5 月 25 日のタイプ linux_syslog のログを削除するには、以下のコマンドを実行します。
	
	```
	ibmcloud logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -r account -i 123456789123456789567c9c8de6dece
	```
	{: screen}
	












