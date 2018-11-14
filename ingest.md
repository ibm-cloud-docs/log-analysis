---

copyright:
  years:  2018
lastupdated: "2018-11-15"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

 
# Sending logs programmatically by using the API
{: #ingest}

You can send log data to an IBM Log Analysis with LogDNA instance. 
{:shortdesc}

Complete the following steps to send logs programmatically:

## Step 1: Get the ingestion API key 
{: #step1}

**Note:** You must have **manager** role for the IBM Log Analysis with LogDNA instance or service to complete this step. For more information, see [Granting permissions to manage logs and configure alerts in LogDNA](/docs/services/Log-Analysis-with-LogDNA/work_iam.html#admin_user_logdna).

    
1. Launch the IBM Log Analysis with LogDNA web UI. For more information, see [Launching the IBM Log Analysis with LogDNA Web UI](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step2).

2. Select the **Configuration** icon ![Configuration icon](images/admin.png). Then, select **Organization**. 

3. Select **API keys**.

    You can see the service keys that have been created. 

4. Select **Generate Service Key**.

    A new key is added to the list. Copy the key.


## Step 2: Send logs
{: #step2}

To send logs, run the following cURL command:

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u SERVICE_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}

where 

* ENDPOINT represents the entry point to the service. Each region has a different URL.
* QUERY_PARAMETERS are parameters that define the filtering criteria applied to the ingestion request.
* LOG_LINES describe the set of log lines that you want to send. It is defined as an array of objects.
* SERVICE_KEY is the API key that you created in the previous step.

The following table lists the endpoints per region:

| Region         | Endpoint                                             | 
|----------------|------------------------------------------------------|
| us-south       | `https://logs.us-south.logging.cloud.ibm.com`        |
{: caption="Endpoints per region" caption-side="top"} 


The following table lists the query parameters:

| Query parameter | Type       | Status     | Description |
|-----------------|------------|------------|-------------|
| hostname        | string     | required   | Host name of the source. |
| mac             | string     | optional   | The network mac address of the host computer.    |
| ip              | string     | optional   | The local IP address of the host computer.  | 
| now             | date-time  | optional   | The source unix timestamp in milliseconds at the time of the request. Used to calculate time drift.|
| tags            | string     | optional   | Tags used to dynamically group hosts. |
{: caption="Query parameters" caption-side="top"} 



The following table lists the data that is required per log line:

| Parameters     | Type       | Description                                   |
|----------------|------------|-----------------------------------------------|
| timestamp      |            | Unix timestamp, including milliseconds, when the log entry was recorded.       | 
| line           | string     | Text of the log line.                                     |
| app            | string     | Name of the application that generates the log line.  |
| level          | string     | Set a vlaue for the level. For example: `INFO`, `WARNING`, `ERROR` |
| meta           |            | This field is reserved for custom information associated with a log line. To add metadata to an API call, specify the meta field under the lines object. Metadata can be viewed inside that line's context.                      |
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
{: #example}

The following sample shows the cURL command to send one log line to an instance of the IBM Log Analysis with LogDNA service: 

```
curl "https://logs.us-south.logging.cloud.ibm.com/logs/ingest?hostname=MYHOST&now=$(date +%s)000" -u xxxxxxxxxxxxxxxxxxxxxxx: --header "Content-Type: application/json; charset=UTF-8" -d "{\"lines\":[{\"line\":\"This is a sample test log statement\",\"timestamp\":\"2018-11-02T10:53:06+00:00\",\"level\":\"INFO\",\"app\":\"myapp\"}]}"
```
{: screen}

