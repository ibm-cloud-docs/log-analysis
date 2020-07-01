---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-01"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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

 
# Exporting events programmatically
{: #export_api}

From an {{site.data.keyword.la_full_notm}} instance, you can export events programmatically by using the LogDNA REST API. 
{:shortdesc}


## Prerequisites
{: #export_api_prereqs}

To export events, consider the following information:

* **You must have a paid service plan** for the {{site.data.keyword.la_full_notm}} service. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-service_plans). 

* Check that your user ID has permissions to launch the web UI, view or manage service keys, and view events. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs).

* Check that the LogDNA instance has the export feature enabled. 


## Export API
{: #export_api_info}

Use `ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:` to export events.
{: note}

*ENDPOINT* represents the entry point to the service. Each region has a different URL. To export events from an auditing instance, see [Endpoints](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-endpoints).

*QUERY_PARAMETERS* are parameters that define the filtering criteria that is applied to the export request.

*SERVICE_KEY* is an API key that you must use to validate your credentials with the auditing instance.

Add `:` after *SERVICE_KEY*.
{: important}


## Query parameters
{: #export_api_info_parameters}

You can define query parameters to refine the events that you want to export.




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




## Exporting events
{: #export_api_events}

Complete the following steps to export events programmatically:


### Step 1. Get a service key
{: #export_api_step_1}

[Get a service key](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-service_keys). 


### Step 2. Identify the data to pass through the export parameters
{: #export_api_step_2}

When you use the export API, you might define 1 or more parameters to refine the set of events that you export. For example, consider the following parameters:
* `levels`: This parameter is used to filter events based on the criticality of a request.
* `query`: This parameter is used to define the search query that is used to filter events.
* `hosts`: This parameter is used to list the services from which you want to export data. 

To verify that the query that you enter returns the set of events that you are looking for, define the search query through the LogDNA web UI.
{: tip}

Consider the following information when you define the search query through the LogDNA web UI 
1. Select the sources. 

    Sources represent {{site.data.keyword.cloud_notm}} services. 
    
    The values that you identify will be required to set the *hosts* parameter. 

    If you set the host field in the query, this parameter is not required.
    {: note}

2. Select the levels.

    In Activity Tracker, level maps to the [severity event field](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-event#severity). Severity defines the level of threat an action may have on the {{site.data.keyword.cloud_notm}}.

    Valid severity values are *critical*, *warning*, and *normal*.

    If you set the field severity in the query, this parameter is not required.
    {: note}

3. Define the search query. 

    To get more informatiomn on how to search, see [Searching Your Logs](https://docs.logdna.com/docs/search){: external}.

    Refine the query until you can only see the events that you want to export.
    {: tip}



### Step 3. Map the data to the query parameters
{: #export_api_step_3}

To define the parameters that you need for the export request, complete the following steps:

1. Map your sources to the hosts parameter. The `hosts` parameter is a comma-separated list of services.

2. Map the severity to the `levels` parameter. The `levels` parameter is a comma-separated list of severity values.

3. Map the query to the query parameter. 

    Notice that when you copy the query from the LogDNA web UI, you must replace every space with %20.
    {: important}




### Step 4. Export the events
{: #export_api_step_4}

Run the following cURL command to export events:

```
curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
```
{: codeblock}

Where 

* ENDPOINT represents the entry point to the service. Each region has a different URL. [Learn more](/docs/services/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-endpoints#endpoints).
* QUERY_PARAMETERS are parameters that define the filtering criteria that is applied to the export request.
* SERVICE_KEY is the service key that you created in the previous step.


## Samples
{: #export_api_samples}

To query events for a service in us-south, you can run the following command:

```
curl 'https://api.us-south.logging.cloud.ibm.com/v1/export?to=1592337600&from=1592179200&hosts=kms&size=10&query=(target.id:crn:v1:bluemix:public:kms:us-south:a/xxxxxxx:xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx%20(action:kms.secrets.create%20%20OR%20action:kms.secrets.delete%20))' -u $TOKEN:
```
{: codeblock}

To write events into the terminal, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000" -u $TOKEN:
```
{: codeblock}

To send an email with the link to download the events that are specified on the export, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&email=joe@ibm.com" -u $TOKEN:
```
{: codeblock}


To send an email with a custom subject, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&email=joe@ibm.com&emailSubject=Export%20test" -u $TOKEN:
```
{: codeblock}


