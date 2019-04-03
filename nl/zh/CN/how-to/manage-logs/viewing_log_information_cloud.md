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

# 查看日志信息
{: #viewing_log_status1}

使用 [ibmcloud logging log-show](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#status) 命令可获取有关在“日志收集”中收集并存储的日志的信息。
您可以获取有关大小、记录数、日志类型以及日志是否可用于在 Kibana 中进行分析的信息。
{:shortdesc}

## 获取有关日志在一段时间内的信息
{: #viewing_logs}

将 `ibmcloud logging log-show` 命令与选项 **-s**（用于设置开始日期）和 **-e**（用于设置结束日期）一起使用。例如：

* `ibmcloud logging log-show` 提供最近 2 周的信息。
* `ibmcloud logging log-show -s 2017-05-03` 提供从 2017 年 5 月 3 日一直到当前日期的信息。
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08` 提供从 2017 年 5 月 3 日到 2017 年 5 月 8 日的信息。 

要获取空间中存储的日志的相关信息，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 运行以下命令：

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如：
    
    ```
    $ ibmcloud logging log-show -s 2017-11-17 -e 2017-11-17
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}


## 获取有关某个日志类型在一段时间内的信息
{: #viewing_logs_by_log_type}

要获取有关一段时间内某个日志类型的信息，请将 `ibmcloud logging log-show` 命令与选项 **-t**（用于指定日志类型）、**-s**（用于设置开始日期）和 **-e**（用于设置结束日期）一起使用。例如：

* `ibmcloud logging log-show -t syslog` 提供有关类型为 *syslog* 的日志最近 2 周的信息。
* `ibmcloud logging log-show -s 2017-05-03 -t syslog` 提供有关类型为 *syslog* 的日志从 2017 年 5 月 3 日一直到当前日期的信息。
* `ibmcloud logging log-show -s 2017-05-03 -e 2017-05-08 -t syslog` 提供有关类型为 *syslog* 的日志从 2017 年 5 月 3 日到 2017 年 5 月 8 日的信息。 

要获取有关某个日志类型在一段时间内的信息，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
    
2. 运行以下命令：

    ```
    ibmcloud logging log-show -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-s* 用于设置开始日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*
    * *-e* 用于设置结束日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*
    * *-t* 用于设置日志类型。
    
    可以通过用逗号分隔各个类型来指定多种日志类型，例如 **log_type_1,log_type_2,log_type_3**。 
    
    例如：
    
    ```
    $ ibmcloud logging log-show -s 2017-05-24 -e 2017-05-25 -t syslog
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-17   794008   706     All          syslog   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}



## 获取有关帐户级别的日志的信息
{: #viewing_logs_account}

要获取有关一段时间内可在帐户级别使用的日志的信息，请使用 `ibmcloud logging log-show` 命令与选项 **-r account** 和 **-i** 来设置帐户的标识。您还可以指定选项 **-t**（用于指定日志类型）、**-s**（用于设置开始日期）和 **-e**（用于设置结束日期）。 

要获取日志的帐户信息，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
2. 获取帐户标识。

    有关更多信息，请参阅[如何获取帐户的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid)。
    
3. 运行以下命令：

    ```
    ibmcloud logging log-show -r account -i AccountID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-r account* 用于设置要从中获取日志信息的域。
    * *-i AccountID* 用于设置帐户的标识。
    * *-s* 用于设置开始日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*
    * *-e* 用于设置结束日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*
    * *-t* 用于设置日志类型。

    可以通过用逗号分隔各个类型来指定多种日志类型，例如 **log_type_1,log_type_2,log_type_3**。 
 
    例如，要针对帐户 *123456789123456789567c9c8de6dece* 显示 2017 年 11 月 17 日在帐户域存储的日志的信息，请运行以下命令：
    
    ```
    $ ibmcloud logging log-show -r account -i 123456789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: 123456789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource 123456789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}


## 获取有关组织级别的日志的信息
{: #viewing_logs_org}

要获取有关一段时间内可在组织级别使用的日志的信息，请使用 `ibmcloud logging log-show` 命令与选项 **-r org** 和 **-i** 来设置组织的标识。您还可以指定选项 **-t**（用于指定日志类型）、**-s**（用于设置开始日期）和 **-e**（用于设置结束日期）。 

要获取日志的帐户信息，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
2. 获取帐户标识。

    有关更多信息，请参阅[如何获取组织的 GUID](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#org_guid)。
    
3. 运行以下命令：

    ```
    ibmcloud logging log-show -r org -i OrgID -s YYYY-MM-DD -e YYYY-MM-DD -t *Log_Type*
    ```
    {: codeblock}
    
    其中
    
    * *-r org* 用于设置要从中获取日志信息的域。
    * *-i OrgID* 用于设置组织的标识。
    * *-s* 用于设置开始日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*
    * *-e* 用于设置结束日期，格式为全球标准时间 (UTC)：*YYYY-MM-DD*
    * *-t* 用于设置日志类型。
    
    可以通过用逗号分隔各个类型来指定多种日志类型，例如 **log_type_1,log_type_2,log_type_3**。 
 
    例如，要针对标识为 *abcd56789123456789567c9c8de6dece* 的组织显示 2017 年 11 月 17 日在组织域存储的日志的信息，请运行以下命令：
    
    ```
    $ ibmcloud logging log-show -r org -i abcd56789123456789567c9c8de6dece -s 2017-05-24 -e 2017-05-25
	Showing log status of resource: abcd56789123456789567c9c8de6dece ...

    Date         Size       Count   Searchable          Types   
	2017-11-17   794008    200     All          syslog  
    Logs of resource abcd56789123456789567c9c8de6dece is showed
    OK
    ```
    {: screen}








