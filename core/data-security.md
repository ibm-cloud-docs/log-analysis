---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, overview, personal data, data deletion, PHI, data, data security, log-analysis

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Securing your data
{: #mng-data}

To ensure that you can securely manage your data when you use {{site.data.keyword.la_full_notm}}, it is important to know exactly what data is stored and encrypted, and how you can delete any stored personal data.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

## How your data is collected in {{site.data.keyword.la_full_notm}}
{: #data-collection}

### Platform logs
{: #data-collection-platform}

Log data from {{site.data.keyword.cloud_notm}} services is collected automatically and available for analysis through the web UI. This data is collected and forwarded to the **platform logs instance** in the location where the service is available. [Learn more about the services that send logs to the platform service logs instance](/docs/log-analysis?topic=log-analysis-cloud_services).

### Logging agent
{: #data-collection-agent}

When you configure a logging agent to collect and forward data to an {{site.data.keyword.la_full_notm}} instance, data is automatically collected and available for analysis through the web UI. You can configure the logging agent to connect to the logging instance via the public network and the private network.

By default, you connect to resources in your account over the {{site.data.keyword.cloud_notm}} public network. To configure an agent to send logs by using a public endpoint, the environment where the agent is running requires internet access to use the public endpoint.

You can enable virtual routing and forwarding (VRF) to move IP routing for your account and all of its resources into a separate routing table. If VRF is enabled, you can then enable {{site.data.keyword.cloud_notm}} service endpoints to connect directly to resources without using the public network. To configure an agent to send logs by using a private endpoint, you must [enable virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint) for your account. Once the account is VRF and service endpoint enabled, the logging agent can be configured to use the private network by using the [Private Endpoint](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api) as the ingestion URL.
* Private endpoints are not accessible from the public internet.
* All traffic is routed to the {{site.data.keyword.cloud_notm}} private network.



## How your data is stored in {{site.data.keyword.la_full_notm}}
{: #data-storage}

{{site.data.keyword.la_full_notm}} collects and aggregates logs.

### Data location
{: #data_storage_location}

{{site.data.keyword.la_full_notm}} collects and aggregates logs in one centralized logging system.

* Log data is hosted on the {{site.data.keyword.cloud_notm}}.
* Data is collocated in the location where the {{site.data.keyword.la_full_notm}} instance is provisioned. For example, log data for an instance that is provisioned in `US South` is hosted in the `US South` region.
* Data from {{site.data.keyword.cloud_notm}} services is collected and aggregated in each {{site.data.keyword.cloud_notm}} location where the service is available.
* Data forwarded by a logging agent is collected and aggregated in the location where the logging instance configured for an agent is available.


### Data encryption
{: #data_storage_encryption}

All the data that is hosted in a logging instance is encrypted at rest using **AES 256**.

When a logging agent sends data to a logging instance, data is encrypted in transit over HTTPS.

When a user requests an export, the data is encrypted during transit, and is also encrypted at rest in {{site.data.keyword.cos_full_notm}} (COS).


### Data retention
{: #data_storage_retention}

The service plan that you choose for an {{site.data.keyword.la_full_notm}} instance defines the number of days that data is stored and retained.

For example, if you choose the *Lite* plan, data is not stored at all. However, if you choose the 7-day plan, data is stored for 7 days and you have access to it through the logging Web UI.



## Data archives
{: #data_archives}

You can archive logs from an {{site.data.keyword.la_full_notm}} instance into a bucket in an {{site.data.keyword.cos_full_notm}} (COS) instance. [Learn more](/docs/log-analysis?topic=log-analysis-archiving).

When data is archived, data going from logging to {{site.data.keyword.cos_full_notm}} (COS) is encrypted in transit over HTTPS.

You must configure archiving to a COS instance if you want to backup your logs for long term storage.

You can use the {{site.data.keyword.sqlquery_short}} service to query data in archive files that are stored in an {{site.data.keyword.cos_short}} (COS) bucket in your account. You can run queries from the {{site.data.keyword.cloud_notm}} UI, or programmatically.

## Data exports
{: #data_exports}

You can export data in JSONL format locally, write data to your terminal, or request an email with a link to the data. [Learn more](/docs/log-analysis?topic=log-analysis-export).

Consider the following information when you export log data:
* You export a set of log entries. To define the set of data that you want to export, you can apply filter and searches. You can also specify the time range.
* From the Web UI, when you export logs, you get an email that is sent to your email address, with a link to a compressed file that includes the data. To get the data, you must click the link and download the compressed file. Notice that the link expires automatically after 12 hours. The compressed file is hosted in {{site.data.keyword.cos_full_notm}} (COS).
* When you export logs programmatically, you can choose to send an email, or to write data to the terminal.
* When you export logs, you have a limit of lines that you can export in a request. You can specify to export older lines or newer lines in case you reach the limit in the time range that you specify for the export.



## Deleting your data
{: #data-delete}

### Deleting logs when an instance is deleted
{: #service-delete-logs}

When you delete a logging instance, the instance is automatically deactivated, and ingestion of logs is stopped. [Learn more](/docs/log-analysis?topic=log-analysis-remove).

logging deletes all logs that are already ingested. Deletion is completed within 24 hours after receiving your request.

You are responsible for deleting archived logs.


### Deleting metadata when an instance is deleted
{: #service-delete-metadata}

When you delete a logging instance, user metadata such as views, alerts, dashboards, screens, and templates, is never deleted.

You must open a case through support to request the data to be deleted. For more information, see [Open a support ticket](/docs/get-support).

You are responsible for deleting archived metadata.

### Deleting metadata from an instance
{: #service-delete-metadata1}

You can delete metadata such as views, dashboards, screens, templates, and alerts at any time.

### Deleting subsets of logs from an instance
{: #service-delete-subset}

Deletion of a subset of logs is not supported.

For example, you cannot delete logs from one logging agent. You cannot delete data for a specific service. You cannot delete data that match a particular query.
