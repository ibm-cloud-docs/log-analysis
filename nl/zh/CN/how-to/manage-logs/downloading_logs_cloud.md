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

# 下载日志
{: #downloading_logs}

可以将日志下载到本地文件或通过管道将数据传递到其他程序。您将在会话上下文中下载日志。会话指定将下载哪些日志。如果日志下载中断，会话支持从其中断的地方恢复下载。下载完成后，必须删除会话。
{:shortdesc}

要完成这些步骤，请安装 {{site.data.keyword.loganalysisshort}} CLI。有关更多信息，请参阅[配置 {{site.data.keyword.loganalysisshort}} CLI](https://console.bluemix.net/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli_)。


要将空间中可用的日志数据下载到本地文件中，请完成以下步骤：

## 步骤 1：登录到 {{site.data.keyword.Bluemix_notm}}
{: #downloading_logs_step1}

登录到 {{site.data.keyword.Bluemix_notm}} 中的区域、组织和空间。 

有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。

## 步骤 2：确定可用的日志
{: #step21}

1. 使用 `ibmcloud logging log-show` 命令可查看最近 2 周可用的日志。运行以下命令：

    ```
    ibmcloud logging log-show
    ```
    {: codeblock}
    
    例如，运行此命令的输出为：
    
    ```
    ibmcloud logging log-show 
    Showing log status of resource: cedc73c5-1234-5678-abcd-378620d6fab5 ...

    Date         Size       Count   Searchable          Types   
    2017-11-16   794008   706     All          syslog, default   
	2017-11-17   794008   706     All          default   
    Logs of resource cedc73c5-1234-5678-abcd-378620d6fab5 is showed
    OK
    ```
    {: screen}

    **注**：{{site.data.keyword.loganalysisshort}} 服务是一种全球服务，使用全球标准时间 (UTC）。日期定义为 UTC 日期。要获取特定本地时间日期的日志，可能需要下载多个 UTC 日期。


## 步骤 3：创建会话
{: #step3}

要定义可供下载的日志数据的作用域，并保持下载的状态，会话是必需的。 

使用 [ibmcloud logging session-create](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_create) 命令来创建会话。（可选）创建会话时，可以指定开始日期、结束日期和日志类型：  

* 指定开始日期和结束日期时，会话会提供对这两个日期之间（含这两个日期）的日志的访问权。 
* 指定日志类型 (**-t**) 时，会话会提供对特定类型日志的访问权。在管理大量日志时，这是非常重要的功能，因为可以将会话的作用域仅限为您关注的一小部分日志。

**注：**对于每个会话，可下载最长 15 天的日志。

要创建会话以用于下载过去两周可用的所有日志，请运行以下命令：

```
ibmcloud logging session-create 
```
{: codeblock}

该会话返回以下信息：

* 要下载的日期范围。缺省值为当前 UTC 日期。
* 要下载的日志类型。缺省情况下，包含创建会话时指定的时间段内可用的所有日志类型。 
* 有关是包含整个帐户还是仅包含当前空间的信息。缺省情况下，将获取所登录到的空间中的日志。
* 会话标识，下载日志时需要此标识。

例如：

```
$ ibmcloud logging session-create
Creating session for lopezdsr@uk.ibm.com resource: cedc73c5-6d55-4193-a9de-378620d6fab5 ...

ID                                     Space                                  CreateTime                       AccessTime                       Start        End          Type   
944aec4d-61f4-43d1-8f3b-c040195122da   12345678-1234-5678-abcd-378620d6fab5   2017-11-17T14:17:25.611542863Z   2017-11-17T14:17:25.611542863Z   2017-11-04   2017-11-17   ANY_TYPE   
Session: 944aec4d-61f4-43d1-8f3b-c040195122da is created
```
{: screen}

**提示**：要查看活动会话的列表，请运行 [ibmcloud logging sessions](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#session_list) 命令。

## 步骤 4：将日志数据下载到文件
{: #step41}

要下载会话参数指定的日志，请运行以下命令：

```
ibmcloud logging log-download -o Log_File_Name Session_ID
```
{: codeblock}

其中

* Log_File_Name 是输出文件的名称。
* Session_ID 是会话的 GUID。您在上一步中已获取此值。

例如：

```
ibmcloud logging log-download -o helloLogs.gz -jshdjsunelsssr4566722==
 160.00 KB / 380.33 KB [==============>------------------------]  42.07% 20.99 KB/s 10s
```
{: screen}

随着日志下载，进度指示器将从 0 逐渐移至 100%。

**注：** 

* 所下载数据的格式为压缩的 JSON。如果将 .gz 文件解压缩并打开该文件，那么可以看到 JSON 格式的数据。 
* 压缩的 JSON 适合由 ElasticSearch 或 Logstash 获取。如果未提供 -o，那么数据将流式传输到 stdout，以便您可以将其通过管道传递到自己的 ELK 堆栈中。
* 还可以使用能解析 JSON 的任何程序来处理这些数据。 

## 步骤 5：删除会话
{: #step5}

下载完成后，必须使用 [ibmcloud logging session delete](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#delete) 命令来删除会话。 

运行以下命令来删除会话：

```
ibmcloud logging session-delete Session_ID
```
{: codeblock}

其中，Session_ID 是先前步骤中创建的会话的 GUID。

例如：

```
ibmcloud logging session-delete -jshdjsunelsssr4566722==
Deleting session: -jshdjsunelsssr4566722== of resource: 12345678-1234-5678-abcd-378620d6fab5 ...
Session: -jshdjsunelsssr4566722== is deleted

```
{: screen}




