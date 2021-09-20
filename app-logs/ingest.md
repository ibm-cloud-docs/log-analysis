---

copyright:
  years:  2018, 2021
lastupdated: "2021-04-12"

keywords: IBM, Log Analysis, logging, ingestion 

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

 
# Sending logs by using the REST API
{: #ingest}

You can send logs to an {{site.data.keyword.la_full_notm}} instance by using the Ingestion REST API. 
{: shortdesc}

Complete the following steps to send logs programmatically by using the REST API:

## Step 1. Get the ingestion API key 
{: #ingest_step1}

**Note:** You must have **manager** role for the {{site.data.keyword.la_full_notm}} instance or service to complete this step. For more information, see [Granting permissions to manage logs and configure alerts](/docs/log-analysis?topic=log-analysis-work_iam#admin_user_logdna).

Complete the following steps to get the ingestion key:
    
1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Settings icon](../images/admin.png) &gt; **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that have been created. 

4. Copy a key. You can use an existing ingestion key or click **Generate Ingestion Key** to create a new one. When you generate a key, the key is added to the list. 


## Step 2. Send logs
{: #ingest_step2}

To send logs, run the following cURL command:

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

Where 

* ENDPOINT represents the entry point to the service. Each region has a different URL. To get the endpoint for a location, see [Ingestion endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_ingestion).
* QUERY_PARAMETERS are parameters that define the filtering criteria that are applied to the ingestion request.
* LOG_LINES describe the set of log lines that you want to send. It is defined as an array of objects.
* INGESTION_KEY is the key that you created in the previous step.


The following table lists the query parameters:

| Query parameter | Type       | Status     | Description |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | required   | Host name of the source. |
| `mac`           | `string`     | optional   | The network mac address of the host computer.    |
| `ip`            | `string`     | optional   | The local IP address of the host computer.  | 
| `now`           | `date-time`  | optional   | The source UNIX timestamp in milliseconds at the time of the request. Used to calculate time drift.|
| `tags`          | `string`     | optional   | Tags that are used to dynamically group hosts. |
{: caption="Query parameters" caption-side="top"} 



The following table lists the data that is required per log line:

| Parameters     | Type       | Description                                   |
|----------------|------------|-----------------------------------------------|
| `timestamp`      |            | UNIX timestamp, including milliseconds, when the log entry was recorded.       | 
| `line`           | `string`     | Text of the log line.                                     |
| `app`            | `string`     | Name of the application that generates the log line.  |
| `level`          | `string`     | Set a value for the level. For example, sample values for this parameter are `INFO`, `WARNING`, `ERROR`. |
| `meta`           |            | This field is reserved for custom information that is associated with a log line. To add metadata to an API call, specify the meta field under the lines object. Metadata can be viewed inside that line's context.                      |
{: caption="Line object fields" caption-side="top"} 

For example, the following sample shows the JSON for a log line that you want to ingest:

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


## Example
{: #ingest_example}

The following sample shows the cURL command to send 1 log line to an instance of the {{site.data.keyword.la_full_notm}} service: 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}


## Limits when you send logs
{: #ingest_limits}

Consider the following limits when you send logs to an {{site.data.keyword.la_full_notm}} instance:

- `Body size`: Maximum size of 10 MB at ingestion.
- `Message size`: Maximum size of 16 KB at ingestion. After 16K, the data is truncated at ingestion.
- `Metadata size`: Maximum size of 32 KB.
- `Hostname length`: Maximum size of 256 characters.
- `App name length`: Maximum size of 512 characters.
- `Log Level`: Maximum size of 80 characters.
- `Tags`: Maximum size of 80 characters.
- `Depth of nested fields`: 3 is the maximum number of nested fields that are parsed at ingestion.
- `Number of unique fields`: A maximum of 500 fields are indexed per day. 

