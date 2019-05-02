---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

subcollection: LogDNA

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

 
# 将日志导出为本地文件
{: #export}

您可以将 JSONL 格式的日志数据从 {{site.data.keyword.la_full_notm}} 实例导出为本地文件。也可以通过编程方式或通过 IBM Log Analysis Web UI 导出日志。
{:shortdesc}

导出日志数据时，请考虑以下信息：
* 可导出一组日志条目。要定义需要导出的数据集，可以应用过滤器和搜索。还可以指定时间范围。 
* 在 Web UI 中，导出日志时，您会收到一封发送到您的电子邮件地址的电子邮件，其中包含一个链接，指向含有数据的压缩文件。要获取数据，必须单击该链接并下载该压缩文件。
* 以编程方式导出日志时，可以选择发送电子邮件或将日志流式传输到终端。
* 包含要导出的数据的压缩日志文件可供下载的最长时间为 48 小时。 
* 可以导出的最大行数为 10,000 行。



## 通过 Web UI 导出日志
{: #ui}

要导出日志数据，请完成以下步骤：

1. 单击**视图**图标 ![“配置”图标](images/views.png)。
2. 选择**全部内容**或视图。
3. 应用时间范围、过滤器和搜索条件，直到看到要导出的日志条目。
4. 如果是从**全部内容**视图开始，请单击**未保存的视图**。如果在上一步中选择了视图，请单击视图名称。
5. 选择`导出行`。这将打开一个新窗口。
6. 检查时间范围。如果需要更改时间范围，请单击*更改导出时间范围*字段中的预定义时间范围。
7. 选择**首选较新的行**或**首选较旧的行**，以防导出请求超过行限制。
8. 查看您的电子邮件。您会从 **LogDNA** 收到一封电子邮件，其中包含用于下载导出行的链接。


## 使用 API 以编程方式导出日志
{: #api}

要以编程方式导出日志，请完成以下步骤：

1. 生成服务密钥。 

    **注：**您必须具有对 {{site.data.keyword.la_full_notm}} 实例或服务的**管理者**角色才能完成此步骤。有关更多信息，请参阅[授予在 LogDNA 中管理日志和配置警报的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)。

    1. 启动 {{site.data.keyword.la_full_notm}} Web UI。有关更多信息，请参阅[转至 {{site.data.keyword.la_full_notm}} Web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

    2. 选择**配置**图标 ![“配置”图标](images/admin.png)。然后，选择**组织**。 

    3. 选择 **API 密钥**。

        您可以看到已创建的服务密钥。 

    4. 单击**生成服务密钥**。

        新的密钥会添加到列表中。复制此密钥。

2. 导出日志。运行以下 cURL 命令：

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    其中： 

    * ENDPOINT 表示服务的入口点。每个区域都有不同的 URL。
    * QUERY_PARAMETERS 是用于定义应用于导出请求的过滤条件的参数。
    * SERVICE_KEY 是您在上一步中创建的服务密钥。

下表列出了每个区域的端点：

|区域|端点| 
|----------------|------------------------------------------------------|
|`Us-south`|`https://api.us-south.logging.cloud.ibm.com `|
{: caption="每个区域的端点" caption-side="top"} 


下表列出了可以设置的查询参数：

|查询参数|类型|状态|描述|
|-----------|------------|------------|-------------|
|`from`|`int32`|必需|开始时间。设置为 UNIX 时间戳记（以秒或毫秒为单位）。|
|`to`|`int32`|必需|结束时间。设置为 UNIX 时间戳记（以秒或毫秒为单位）。|
|`size`|`string`|可选|要包含在导出中的日志行数。| 
|`hosts`|`string`|可选|以逗号分隔的主机列表。|
|`apps`|`string`|可选|以逗号分隔的应用程序列表。|
|`levels`|`string`|可选|以逗号分隔的日志级别列表。|
|`query`|`string`|可选|搜索查询。有关更多信息，请参阅[搜索日志](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)。 |
|`prefer`|`string`|可选|定义要导出的日志行。有效值为 `head`（从头开始的日志行数）和 `tail`（最后的日志行数）。如果未指定，缺省值为 tail。|
|`email`|`string`|可选|指定包含可下载的导出链接的电子邮件。缺省情况下，日志行将流式传输。|
|`emailSubject`|`string`|可选|用于设置电子邮件的主题。</br>使用 `%20` 表示空格。例如，样本值为 `Export%20logs`。|
{: caption="查询参数" caption-side="top"} 

例如，要将日志行流式传输到终端，可以运行以下命令：

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

要发送电子邮件，其中包含用于下载导出上所指定的日志行的链接，可以运行以下命令：

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


要发送使用定制主题的电子邮件，可以运行以下命令：

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

