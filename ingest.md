---

copyright:
  years:  2018
lastupdated: "2018-11-02"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

 
# Sending logs
{: #ingest}

You can send log data to an IBM Log Analysis with LogDNA instance. 
{:shortdesc}

Consider the following information when you send log data:
* 



## Sending logs programmatically by using the API
{: #api}

Complete the following steps to send logs programmatically:

1. Obtain the ingestion key. 

    **Note:** You must have **manager** role for the IBM Log Analysis with LogDNA instance or service to complete this step. For more information, see [Granting permissions to manage logs and configure alerts in LogDNA](/docs/services/Log-Analysis-with-LogDNA/work_iam.html#admin_user_logdna).

    1. Launch the IBM Log Analysis with LogDNA web UI. For more information, see [Launching the IBM Log Analysis with LogDNA Web UI](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step2).

    2. Select the **Configuration** icon ![Configuration icon](images/admin.png). Then, select **Organization**. 

    3. Select **API keys**.

        You can see the service keys that have been created. 

    4. Select **Generate Service Key**.

        A new key is added to the list.

2. Export logs. Run the following cURL command:

    ```
    curl "ENDPOINT/v1/export?QUERY_PARAMETERS" -u SERVICE_KEY:
    ```
    {: codeblock}

    where 

    * ENDPOINT represents the entry point to the service. Each region has a different URL.
    * QUERY_PARAMETERS are parameters that define the filtering criteria applied to the export request.
    * SERVICE_KEY is the service key that you created in the previous step.

The following table lists the endpoints per region:

| Region         | Endpoint                                             | 
|----------------|------------------------------------------------------|
| us-south       | `https://api.us-south.logging.cloud.ibm.com `        |
{: caption="Endpoints per region" caption-side="top"} 


The following table lists the query parameters that you can set:

| Query parameter | Type       | Status     | Description |
|-----------|------------|------------|-------------|
| from      | int32      | required   | Start time. Set as Unix timestamp in seconds or milliseconds. |
| to        | int32      | required   | End time. Set asUnix timestamp in seconds or milliseconds.    |
| size      | string     | optional   | Number of log lines to include in the export.  | 
| hosts     | string     | optional   | Comma separated list of hosts. |
| apps      | string     | optional   | Comma separated list of applications. |
| levels    | string     | optional   | Comma separated list of log levels. |
| query     | string     | optional   | Search query. For more information, see [Search Logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step6). |
| prefer    | string     | optional   | Defines the log lines that you want to export. Valid values are `head`, first log lines, and `tail`, last log lines. If not specified, defaults to tail.  |
| email     | string     | optional   | Specifies the email with the downloadable link of your export. By default, the log lines are streamed.|
| emailSubject | string     | optional   | Use to set the subject of the email. </br>Use `%20` to represent a space. For example: Export%20logs |
{: caption="Query parameters" caption-side="top"} 

For example, to stream log lines into the terminal, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info" -u e08c0c759663491880b0d61712346789:
```
{: screen}

To send an email with the link to download the log lines specified on the export, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=joe@ibm.com" -u e08c0c759663491880b0d61712346789:
```
{: screen}


To send an email with a custom subject, you can run the following command:

```
curl "https://api.us-south.logging.cloud.ibm.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=info&email=lopezdsr@uk.ibm.com&emailSubject=Export%20test" -u e08c0c759663491880b0d61712346789:
```
{: screen}

