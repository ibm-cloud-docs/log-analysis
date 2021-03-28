---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: LogDNA, IBM, Log Analysis, logging, export logs, api

subcollection: Log-Analysis-with-LogDNA

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
{:external: target="_blank" .external}

 
# Exporting logs programmatically
{: #export_api}

From an {{site.data.keyword.la_full_notm}} instance, you can export logs programmatically by using the logging REST API. 
{:shortdesc}

Consider the following information when you export log data:
* You export a set of log entries. To define the set of data that you want to export, you can apply filter and searches. You can also specify the time range. 
* When you export logs programmatically, you can choose to send an email or to write logs into your terminal.
* The compressed log file that contains the data that you want to export is available for a maximum of 12 hours. 
* When you export logs, you have a limit of lines that you can export in a request. You can specify to export older lines or newer lines in case you reach the limit in the time range that you specify for the export. The maximum number of lines that you can export per API request is `500.000` lines.


## Prerequisites
{: #export_api_prereqs}

To export logs, consider the following information:

* **You must have a paid service plan** for the {{site.data.keyword.la_full_notm}} service. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-service_plans). 

* Check that your user ID has permissions to launch the web UI, view or manage service keys, and view logs. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs).

* Check that the logging instance has the export feature enabled. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-export_config).


## Export API
{: #export_api_info}

Use `ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:` to export logs.
{: note}

*ENDPOINT* represents the entry point to the service. Each region has a different URL. To export logs from an auditing instance, see [Endpoints](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-endpoints).

*QUERY_PARAMETERS* are parameters that define the filtering criteria that is applied to the export request.

*SERVICE_KEY* is an API key that you must use to validate your credentials with the auditing instance.

Add `:` after *SERVICE_KEY*.
{: important}


## Query parameters
{: #export_api_info_parameters}

You can define query parameters to refine the logs that you want to export.

The following table lists the query parameters that you can set:

| Query parameter | Type       | Status     | Description |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | Required   | Start time. Set as UNIX timestamp in seconds or milliseconds. |
| `to`        | `int32`      | Required   | End time. Set as UNIX timestamp in seconds or milliseconds.    |
| `size`      | `string`     | Optional   | Number of log lines to include in the export.  | 
| `hosts`     | `string`     | Optional   | Comma-separated list of hosts. |
| `apps`      | `string`     | Optional   | Comma-separated list of applications. |
| `levels`    | `string`     | Optional   | Comma-separated list of log levels. |
| `query`     | `string`     | Optional   | Search query. For more information, see [Search Logs](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step6). |
| `prefer`    | `string`     | Optional   | Defines the log lines that you want to export. Valid values are `head`, first log lines, and `tail`, last log lines. If not specified, defaults to tail.  |
| `email`     | `string`     | Optional   | Specifies the email with the downloadable link of your export. By default, the log lines are streamed.|
| `emailSubject` | `string`     | Optional   | Use to set the subject of the email. </br>Use `%20` to represent a space. For example, a sample value is `Export%20logs`. |
{: caption="Query parameters" caption-side="top"} 


When you include a query or a subject to an email, use `%20` to represent a space.
{: important}

For example, you can define a set of parameters to include information:

```
ENDPOINT/v1/export?to=START_TIME&from=END_TIME&hosts=LIST_OF_HOSTS&levels=LIST_OF_LEVELS&size=N&query=(SEARCH_QUERY)" -u $TOKEN:
```
{: pre}


## Exporting logs
{: #export_api_logs}

Complete the following steps to export logs programmatically:


### Step 1. Get a service key
{: #export_api_step_1}

[Get a service key](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-service_keys). 


### Step 2. Identify the data to pass through the export parameters
{: #export_api_step_2}

To verify that the query that you use in the export returns the set of logs that you are looking for, define the search query through the logging web UI. Refine the query until you can only see the logs that you want to export. Then, map the data to the query parameters.

Notice that when you copy the query from the logging web UI, you must replace every space with `%20`.
{: important}




### Step 3. Export the logs
{: #export_api_step_3}

Run the following cURL command to export logs:

```
curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
```
{: pre}

Where 

* ENDPOINT represents the entry point to the service. Each region has a different URL. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-endpoints).
* QUERY_PARAMETERS are parameters that define the filtering criteria that is applied to the export request.
* SERVICE_KEY is the service key that you created in the previous step.


## Samples
{: #export_api_samples}

For example, to write log lines into the terminal, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: pre}

To send an email with the link to download the log lines specified on the export, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=xxx@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: pre}


To send an email with a custom subject, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=xxx@ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: pre}

To use the query parameter to find all log lines with a level of `info`, you can run the following command:

```
curl -s "https://api.us-south.logging.cloud.ibm.com/v1/export?query=test_query&levels=info" -u :
```
{: pre}

