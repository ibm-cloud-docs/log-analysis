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

# ログ情報の表示
{: #viewing_log_status1}

収集されて Log Collection に保管されたログに関する情報を取得するには、[ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#status) コマンドを使用します。 取得できる情報は、サイズ、レコード数、ログ・タイプ、および、ログが Kibana での分析に使用可能かどうかです。
{:shortdesc}

## 特定の期間のログに関する情報の取得
{: #viewing_logs}

オプション **-s** で開始日を、**-e** で終了日を設定して、`ibmcloud logging log-show` コマンドを使用します。 例えば次のようにします。

* `ibmcloud logging log-show` を使用すると、最近 2 週間の情報が提供されます。
* `ibmcloud logging log-show -s 2017-05-03` を使用すると、2017 年 5 月 3 日から現在日付までの情報が提供されます。
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` を使用すると、2017 年 5 月 3 日から 2017 年 5 月 8 日までの情報が提供されます。 

スペースに保管されたログに関する情報を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 次のコマンドを実行します。

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    以下に例を示します。
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## 特定の期間のログのタイプに関する情報の取得
{: #viewing_logs_by_log_type}

特定の期間のログのタイプに関する情報を取得するには、`ibmcloud logging log-show` コマンドを使用し、その際、オプション **-t** でログのタイプを指定し、**-s** で開始日を、**-e** で終了日を設定します。 以下に例を示します。

* `ibmcloud logging log-show -t syslog` を使用すると、タイプ *syslog* の最近 2 週間のログに関する情報が提供されます。
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` を使用すると、タイプ *syslog* の 2017 年 5 月 3 日から現在日付までのログに関する情報が提供されます。
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` を使用すると、タイプ *syslog* の 2017 年 5 月 3 日から 2017 年 5 月 8 日までのログに関する情報が提供されます。 

特定の期間内の特定のタイプのログに関する情報を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. 次のコマンドを実行します。

    ```
    ibmcloud logging log-show -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    各部分の説明:
    
    * *-s* は、開始日を協定世界時 (UTC) で設定するために使用されます: *YYYY-MM-DD*
    * *-e* は、終了日を協定世界時 (UTC) で設定するために使用されます: *YYYY-MM-DD*
    * *-t* は、ログ・タイプを設定するために使用されます。
    
    各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: **log_type_1,log_type_2,log_type_3**)。 
    
    以下に例を示します。
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## アカウント・レベルのログに関する情報の取得
{: #viewing_logs_account}

特定期間にアカウント・レベルで使用可能なログに関する情報を取得するには、`ibmcloud logging log-show` コマンドを使用し、その際、オプション **-r account** および **-i** でアカウントの ID を設定します。 オプション **-t** でログのタイプを指定し、**-s** で開始日を、**-e** で終了日を設定することもできます。 

ログに関するアカウント情報を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
	
2. アカウント ID を取得します。

    詳しくは、『[アカウントの GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)』を参照してください。
    
3. 次のコマンドを実行します。

    ```
    ibmcloud logging log-show -r account -i AccountID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    各部分の説明:
    
    * *-r account* は、ログに関する情報を取得したいドメインを設定するために使用されます。
    * *-i AccountID* は、アカウントの ID を設定するために使用されます。
    * *-s* は、開始日を協定世界時 (UTC) で設定するために使用されます: *YYYY-MM-DD*
    * *-e* は、終了日を協定世界時 (UTC) で設定するために使用されます: *YYYY-MM-DD*
    * *-t* は、ログ・タイプを設定するために使用されます。

    各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: **log_type_1,log_type_2,log_type_3**)。 
 
    例えば、アカウント *123456789123456789567c9c8de6dece* のアカウント・ドメインで 2017 年 11 月 17 日に保管されたログに関する情報を表示するには、以下のコマンドを実行します。
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## 組織レベルのログに関する情報の取得
{: #viewing_logs_org}

特定期間に組織レベルで使用可能なログに関する情報を取得するには、`ibmcloud logging log-show` コマンドを使用し、その際、オプション **-r org** および **-i** で組織の ID を設定します。 オプション **-t** でログのタイプを指定し、**-s** で開始日を、**-e** で終了日を設定することもできます。 

ログに関するアカウント情報を取得するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
	
2. アカウント ID を取得します。

    詳しくは、『[組織の GUID の取得方法を教えてください](/docs/services/CloudLogAnalysis/qa/cli_qa.html#org_guid)』を参照してください。
    
3. 次のコマンドを実行します。

    ```
    ibmcloud logging log-show -r org -i OrgID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    各部分の説明:
    
    * *-r org* は、ログに関する情報を取得したいドメインを設定するために使用されます。
    * *-i OrgID* は、組織の ID を設定するために使用されます。
    * *-s* は、開始日を協定世界時 (UTC) で設定するために使用されます: *YYYY-MM-DD*
    * *-e* は、終了日を協定世界時 (UTC) で設定するために使用されます: *YYYY-MM-DD*
    * *-t* は、ログ・タイプを設定するために使用されます。
    
    各タイプをコンマで区切ることによって複数のログ・タイプを指定できます (例: **log_type_1,log_type_2,log_type_3**)。 
 
    例えば、ID *abcd56789123456789567c9c8de6dece* の組織の組織ドメインで 2017 年 11 月 17 日に保管されたログに関する情報を表示するには、以下のコマンドを実行します。
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








