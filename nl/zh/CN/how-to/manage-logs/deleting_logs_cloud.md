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

# 删除日志
{: #deleting_logs}

使用 [ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) 命令从“日志收集”删除日志。
{:shortdesc}

* 您可以删除特定时间范围内的日志。
* 您可以按类型删除日志。请注意，每个日志文件仅有一种类型的日志条目。
* 您可以删除空间、组织或帐户域中的日志。


## 删除特定时间段的所有日志
{: #time_range}

完成以下步骤，以删除特定时间段存储在空间域中的所有日志：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 运行以下命令以查看“日志收集”中可用的日志。

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如：
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-abcd-4193-aere-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 删除在特定日期存储的日志。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate
	```
	{: codeblock}
	
	其中
	
	* *-s* 设置开始日期，格式为全球标准时间 (UTC)：YYYY-MM-DD，例如 2006-01-02。
    * *-e* 设置结束日期，格式为全球标准时间 (UTC)：YYYY-MM-DD
    	
	例如，要删除 2017 年 5 月 25 日的日志，请运行以下命令：
	
	
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25
	```
	{: screen}

	
## 按日志类型删除特定时间段的日志 
{: #log_type}

要按日志类型删除特定时间段存储在空间域中的日志，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
    
2. 运行以下命令以查看“日志收集”中可用的日志。

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如：
    
    ```
    $ ibmcloud logging log-show
    Showing log status of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
	2017-05-24   16         3020    None                default
	2017-05-25   1224       76115   All                 linux_syslog,log
    2017-05-26   19663113   17639   All                 default,linux_syslog  
    ```
    {: screen}
	
3. 删除在特定日期存储的日志。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType
	```
	{: codeblock}
	
	其中
	
	* *-s* 设置开始日期，格式为全球标准时间 (UTC)：YYYY-MM-DD，例如 2006-01-02。
    * *-e* 设置结束日期，格式为全球标准时间 (UTC)：YYYY-MM-DD
	* *-t* 设置日志类型。
    	
	例如，要删除 2017 年 5 月 25 日类型为 linux_syslog 的日志，请运行以下命令：
	
	
	
	```
	ibmcloud logging log-delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog
	```
	{: screen}

		
	
## 按日志类型删除特定时间段的帐户日志 
{: #time_range_acc}

请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
	
2. 获取帐户标识。

    有关更多信息，请参阅[如何获取帐户的 GUID](/docs/services/CloudLogAnalysis/qa/cli_qa.html#account_guid)。
    
3. 运行以下命令，以在帐户级别查看“日志收集”中可用的日志。

    ```
    ibmcloud logging log-show  -r account -i AccountID
    ```
    {: codeblock}
    
    例如：
    
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
	
4. 删除在特定日期存储的日志。

    ```
	ibmcloud logging log-delete -s StartDate -e EndDate -t LogType -r account -i AccountID
	```
	{: codeblock}
	
	其中
	
	* *-s* 设置开始日期，格式为全球标准时间 (UTC)：YYYY-MM-DD，例如 2006-01-02。
    * *-e* 设置结束日期，格式为全球标准时间 (UTC)：YYYY-MM-DD
	* *-t* 设置日志类型。
    	
	例如，要删除 2017 年 5 月 25 日在帐户级别存储在“日志收集”中且类型为 linux_syslog 的日志，请运行以下命令：
	
	
	
	```
	ibmcloud logging delete -s 2017-05-25 -e 2017-05-25 -t linux_syslog -r account -i 123456789123456789567c9c8de6dece
	```
	{: screen}
	












