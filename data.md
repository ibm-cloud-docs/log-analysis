---

copyright:
  years:  2018, 2020
lastupdated: "2020-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, data

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

# Log data
{: #data}

Learn how log data is collected, managed, and deleted within the {{site.data.keyword.la_full}}.
{:shortdesc}


## Data location
{: #data_location}

{{site.data.keyword.la_full_notm}} collects and aggregates logs in one centralized logging system.

* Log data is hosted on the {{site.data.keyword.cloud_notm}}. The {{site.data.keyword.la_full_notm}} service is operated by LogDNA.
* Data is collocated in the location where the {{site.data.keyword.la_full_notm}} instance is provisioned. For example, log data for an instance that is provisioned in `US South` is hosted in the `US South` region.


## Data collection
{: #data_collection}

When you configure a LogDNA agent to collect and forward data to an {{site.data.keyword.la_full_notm}} instance, data is automatically collected and available for analysis through the web UI.

Log data from {{site.data.keyword.cloud_notm}} services, Cloud Foundry (CF) framework, and CF applications is collected automatically and available for analysis through the web UI. These data is collected and forwarded to the **platform service logs instance** in the location where the service is available. [Learn more about the services that send logs to the platform service logs instance](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services).

## Data encryption
{: #data_encryption}

All the data that is hosted in a LogDNA instance is encrypted at rest using **AES 256**.

When a LogDNA agent sends data to a LogDNA instance, data is encrypted in transit over HTTPS.

When a user requests an export, the data is encrypted during transit, and is also encrypted at rest in {{site.data.keyword.cos_full_notm}} (COS).


## Data retention for search
{: #data_retention}

The service plan that you choose for an {{site.data.keyword.la_full_notm}} instance defines the number of days that data is stored and retained in LogDNA. 

For example, if you choose the *Lite* plan, data is not stored at all. However, if you choose the 7-day plan, data is stored for 7 days and you have access to it through the LogDNA Web UI.



## Data availability
{: #data_availability}

Data from {{site.data.keyword.cloud_notm}} services is collected and aggregated in each {{site.data.keyword.cloud_notm}} location where the service is available. 

Data forwarded by a LogDNA agent is collected and aggregated in the location where the LogDNA instance is available.

Each supported location is a multi-zone region (MZR), except Seoul that is a single-zone region (SZR). [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-regions).

## Data archives
{: #data_archives}

You can archive logs from an {{site.data.keyword.la_full_notm}} instance into a bucket in an {{site.data.keyword.cos_full_notm}} (COS) instance. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-archiving).

When data is archived, data going from LogDNA to {{site.data.keyword.cos_full_notm}} (COS) is encrypted in transit over HTTPS.

You must configure archiving to a COS instance if you want to backup your logs for long term storage.

You can use the {{site.data.keyword.sqlquery_short}} service to query data in archive files that are stored in an {{site.data.keyword.cos_short}} (COS) bucket in your account. You can run queries from the {{site.data.keyword.cloud_notm}} UI, or programmatically.

## Data exports
{: #data_exports}

You can export data in JSONL format locally, write data to your terminal, or request an email with a link to the data. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-export).

Consider the following information when you export log data:
* You export a set of log entries. To define the set of data that you want to export, you can apply filter and searches. You can also specify the time range. 
* From the Web UI, when you export logs, you get an email that is sent to your email address, with a link to a compressed file that includes the data. To get the data, you must click the link and download the compressed file. Notice that the link expires automatically after 12 hours. The compressed file is hosted in {{site.data.keyword.cos_full_notm}} (COS).
* When you export logs programmatically, you can choose to send an email, or to write data to the terminal.
* When you export logs, you have a limit of lines that you can export in a request. You can specify to export older lines or newer lines in case you reach the limit in the time range that you specify for the export.


## Data deletion
{: #data_deletion}

When you delete a LogDNA instance, the instance is automatically deactivated, and ingestion of logs is stopped. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-remove).

LogDNA deletes all logs that are already ingested. Deletion is completed within 24 hours after receiving your request.

You are responsible for managing archived data. 


