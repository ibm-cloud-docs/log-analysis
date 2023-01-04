---

copyright:
  years:  2018, 2023
lastupdated: "2021-12-02"

keywords: IBM, Log Analysis, logging, export logs, api, v2

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Exporting logs programmatically using the V2 API
{: #export_api_v2}

From an {{site.data.keyword.la_full_notm}} instance, you can export logs programmatically by using the V2 logging REST API.
{: shortdesc}

The V2 logging REST API does not support sending the logs by email.  If you need email support, you will need to use the [V1 logging REST API](/docs/log-analysis?topic=log-analysis-export_api).
{: note}

Consider the following information when you export log data:
* You export a set of log entries. To define the set of data that you want to export, you can apply filter and searches. You can also specify the time range.
* The compressed log file that contains the data that you want to export is available for a maximum of 12 hours.
* When you export logs, you have a limit of lines that you can export in a request. You can specify to export older lines or newer lines in case you reach the limit in the time range that you specify for the export. The maximum number of lines that you can export per page is `10,000` lines with no limit on the number of pages.

## Prerequisites
{: #export_api_prereqs_v2}

To export logs, consider the following information:

* **You must have a paid service plan** for the {{site.data.keyword.la_full_notm}} service. [Learn more](/docs/log-analysis?topic=log-analysis-service_plans).

* Check that your user ID has permissions to launch the web UI, view or manage service keys, and view logs. [Learn more](/docs/log-analysis?topic=log-analysis-view_logs).

* Check that the logging instance has the export feature enabled. [Learn more](/docs/log-analysis?topic=log-analysis-export_config).


## Export API
{: #export_api_info_v2}

Use `ENDPOINT/v2/export?QUERY_PARAMETERS" -u SERVICE_KEY:` to export logs.
{: note}

*ENDPOINT* represents the entry point to the service. Each region has a different URL. To export logs from a logging instance, see [Endpoints](/docs/log-analysis?topic=log-analysis-endpoints).

*QUERY_PARAMETERS* are parameters that define the filtering criteria that is applied to the export request.

*SERVICE_KEY* is an API key that you must use to validate your credentials with the logging instance. For more information on how to get a service key, see [Service keys by using the API](/docs/log-analysis?topic=log-analysis-service_keys#service_keys_api).

Add `:` after *SERVICE_KEY*.
{: important}


## Query parameters
{: #export_api_info_parameters_v2}

You can define query parameters to refine the logs that you want to export.

The following table lists the query parameters that you can set:

| Query parameter | Type       | Status     | Description |
|-----------|------------|------------|-------------|
| `from`      | `int32`      | Required   | Start time. Set as UNIX timestamp in seconds or Javascript (milliseconds). |
| `to`        | `int32`      | Required   | End time. Set as UNIX timestamp in seconds or Javascript (milliseconds).    |
| `size`      | `int32`     | Optional   | Number of log lines to include in each page of the export. The maximum and default is `10000`. |
| `hosts`     | `string`     | Optional   | Comma-separated list of hosts. |
| `apps`      | `string`     | Optional   | Comma-separated list of applications. |
| `levels`    | `string`     | Optional   | Comma-separated list of log levels. |
| `tags`    | `string`     | Optional   | Comma-separated list of tags. |
| `query`     | `string`     | Optional   | Search query. For more information, see [Search Logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step6). |
| `prefer`    | `string`     | Optional   | Defines the log lines that you want to export. Valid values are `head`, first log lines, and `tail`, last log lines. If not specified, defaults to tail.  |
| `pagination_id`     | `string`     | Optional   | Indicates which page of results is retrieved from an export. For the initial export request, this parameter should be omitted. Subsequent requests for pagination should provide the token sent in the response to this parameter.|
{: caption="Query parameters" caption-side="top"}


For example, you can define a set of parameters to include information:

```text
ENDPOINT/v2/export?to=START_TIME&from=END_TIME&hosts=LIST_OF_HOSTS&levels=LIST_OF_LEVELS&size=N&query=(SEARCH_QUERY)" -u $TOKEN:
```
{: pre}


## Exporting logs
{: #export_api_logs_v2}

Complete the following steps to export logs programmatically:


### Step 1. Get a service key
{: #export_api_v2_step_1}

[Get a service key](/docs/log-analysis?topic=log-analysis-service_keys).


### Step 2. Identify the data to pass through the export parameters
{: #export_api_v2_step_2}

To verify that the query that you use in the export returns the set of logs that you are looking for, define the search query through the logging web UI. Refine the query until you can only see the logs that you want to export. Then, map the data to the query parameters.

Notice that when you copy the query from the logging web UI, you must replace every space with `%20`.
{: important}




### Step 3. Export the logs
{: #export_api_v2_step_3}

Run the following cURL command to export logs:

```text
curl "ENDPOINT/v2/export?QUERY_PARAMETERS" -u SERVICE_KEY:
```
{: pre}

Where

* ENDPOINT represents the entry point to the service. Each region has a different URL. [Learn more](/docs/log-analysis?topic=log-analysis-endpoints).
* QUERY_PARAMETERS are parameters that define the filtering criteria that is applied to the export request.
* SERVICE_KEY is the service key that you created in the previous step.


## Samples
{: #export_api_v2_samples}

For example, to write log lines into the terminal, you can run the following command:

```text
curl "https://api.us-south.logging.cloud.ibm.com/v2/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: pre}


To use the query parameter to find all log lines with a level of `info`, you can run the following command:

```text
curl -s "https://api.us-south.logging.cloud.ibm.com/v2/export?query=test_query&levels=info" -u :
```
{: pre}
