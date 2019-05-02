---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion 

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

 
# 发送日志
{: #ingest}

您可以将日志数据发送到 {{site.data.keyword.la_full_notm}} 实例。
{:shortdesc}

要以编程方式发送日志，请完成以下步骤：

## 步骤 1. 获取摄入 API 密钥 
{: #ingest_step1}

**注：**您必须具有对 {{site.data.keyword.la_full_notm}} 实例或服务的**管理者**角色才能完成此步骤。有关更多信息，请参阅[授予在 LogDNA 中管理日志和配置警报的许可权](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)。

要获取摄入密钥，请完成以下步骤：
    
1. 启动 {{site.data.keyword.la_full_notm}} Web UI。有关更多信息，请参阅[转至 {{site.data.keyword.la_full_notm}} Web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2)。

2. 选择**配置**图标 ![“配置”图标](images/admin.png)。然后，选择**组织**。 

3. 选择 **API 密钥**。

    您可以看到已创建的摄入密钥。 

4. 使用现有摄入密钥，或单击**生成摄入密钥**以创建新的摄入密钥。

    新的密钥会添加到列表中。复制该密钥。


## 步骤 2. 发送日志
{: #ingest_step2}

要发送日志，请运行以下 cURL 命令：

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

其中： 

* ENDPOINT 表示服务的入口点。每个区域都有不同的 URL。
* QUERY_PARAMETERS 是用于定义应用于摄入请求的过滤条件的参数。
* LOG_LINES 描述要发送的一组日志行。此项定义为对象的数组。
* INGESTION_KEY 是您在上一步中创建的密钥。

下表列出了每个区域的端点：

|区域|端点| 
|----------------|------------------------------------------------------|
|`Us-south`|`https://logs.us-south.logging.cloud.ibm.com`|
{: caption="每个区域的端点" caption-side="top"} 


下表列出了查询参数：

|查询参数|类型|状态|描述|
|-----------------|------------|------------|-------------|
|`hostname`|`string`|必需|源的主机名。|
|`mac`|`string`|可选|主计算机的网络 MAC 地址。|
|`ip`|`string`|可选|主计算机的本地 IP 地址。| 
|`now`|`date-time`|可选|请求时的源 UNIX 时间戳记（以毫秒为单位）。用于计算时间漂移。|
|`tags`|`string`|可选|用于对主机动态分组的标记。|
{: caption="查询参数" caption-side="top"} 



下表列出了每个日志行所需的数据：

|参数|类型|描述|
|----------------|------------|-----------------------------------------------|
|`timestamp`|            |记录日志条目时的 UNIX 时间戳记，包括毫秒。| 
|`line`|`string`|日志行的文本。|
|`app`|`string`|生成日志行的应用程序的名称。|
|`level`|`string`|设置级别的值。例如，此参数的样本值为 `INFO`、`WARNING` 和 `ERROR`。|
|`meta`|            |此字段已保留用于与日志行关联的定制信息。要向 API 调用添加元数据，请指定行对象下的元字段。可以在该行的上下文中查看元数据。|
{: caption="行对象字段" caption-side="top"} 

例如，以下样本显示了要摄入的日志行的 JSON：

```
{ 
  "lines": [ 
    { 
      "timestamp": 2018-11-02T10:53:06+00:00, 
      "line":"This is my first log line.", 
      "app":"myapp",
      "level": "INFO",
      "meta": {
        "customfield": {"nestedfield": "nestedvalue"}
      }
    }
  ] 
}
```
{: screen}


## 示例
{: #ingest_example}

以下样本显示了用于将 1 个日志行发送到 {{site.data.keyword.la_full_notm}} 服务实例的 cURL 命令： 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

