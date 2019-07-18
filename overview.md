---

copyright:
  years:  2018, 2019
lastupdated: "2019-06-03"

keywords: LogDNA, IBM, Log Analysis, logging, overview

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

# About {{site.data.keyword.la_full_notm}}
{: #about}

{{site.data.keyword.la_full}} is a third-party service that you can include as part of your {{site.data.keyword.cloud_notm}} architecture to add log management capabilities. {{site.data.keyword.la_full_notm}} is operated by LogDNA in partnership with {{site.data.keyword.IBM_notm}}.
{:shortdesc}

You can use {{site.data.keyword.la_full_notm}} to manage system and application logs in the {{site.data.keyword.cloud_notm}}.

{{site.data.keyword.la_full_notm}} offers administrators, DevOps teams, and developers advanced features to filter, search, and tail log data, define alerts, and design custom views to monitor application and system logs.


## Overview
{: #ov}

To add logging features with LogDNA in the {{site.data.keyword.cloud_notm}}, you must provision an instance of {{site.data.keyword.la_full_notm}}.

Before you provision an instance of {{site.data.keyword.la_full_notm}}, consider the following information:
* Log data is hosted on the {{site.data.keyword.cloud_notm}}.
* Log data is sent to a third party.
* Your users must have platform permissions to create, view, and delete an instance of a service in the {{site.data.keyword.cloud_notm}}.
* Your users must have platform permissions to create resources within the context of the resource group where you plan to provision the LogDNA instance.

You provision an {{site.data.keyword.la_full_notm}} instance within the context of a resource group. You organize your services for access control and billing purposes by using resource groups. You can provision the instance in the *default* resource group or in a custom resource group.

After you provision an instance of {{site.data.keyword.la_full_notm}}, an account is created in LogDNA, and you receive the ingestion key for your account.

Then, you must configure a LogDNA agent for each log source. A log source is a Cloud or on-prem resource that generates logs. For example, a log source can be a Kubernetes cluster. You use the ingestion key to configure the LogDNA agent that is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance.

After the LogDNA agent is deployed in a log source, collection and forwarding of logs to the {{site.data.keyword.la_full_notm}} instance is automatic.

You can launch the {{site.data.keyword.la_full_notm}} Web UI to view, monitor, and manage your logs.

The following figure shows the components overview for the {{site.data.keyword.la_full_notm}} service that is running on {{site.data.keyword.cloud_notm}}:

![{{site.data.keyword.la_full_notm}} component overview on the {{site.data.keyword.cloud_notm}}](images/components.png "{{site.data.keyword.la_full_notm}} component overview on the {{site.data.keyword.cloud_notm}}")


## Data location
{: #overview_data}

{{site.data.keyword.la_full_notm}} collects and aggregates logs in one centralized logging system.

* Log data is hosted on the {{site.data.keyword.cloud_notm}}.
* Data is colocated in the location where the {{site.data.keyword.la_full_notm}} instance is provisioned. For example, log data for an instance that is provisioned in US South is hosted in the US South region.


## Data collection
{: #overview_data_collection}

When you configure a LogDNA agent to collect and forward data to an {{site.data.keyword.la_full_notm}} instance, data is automatically collected and available for analysis through the web UI. 

Log data from {{site.data.keyword.cloud_notm}} services, Cloud Foundry (CF) framework, and CF applications is collected automatically and available for analysis through the web UI. These data is collected and forwarded to the **service platform logs instance*** in the location where the service is available. 

## Data retention
{: #overview_data_retention}

The service plan that you choose for an {{site.data.keyword.la_full_notm}} instance defines the number of days that data is stored and retained in LogDNA. 

For example, if you choose the *Free* plan, data is not stored at all. However, if you choose the 7-day plan, data is stored for 7 days and you have access to it through the LogDNA Web UI.

When you delete an instance of {{site.data.keyword.la_full_notm}} from the {{site.data.keyword.cloud_notm}}, all the data is deleted.

## Data availability
{: #overview_data_availability}

Data is collected and aggregated in each location. Each supported location is a multi-zone region (MZR).


## Features
{: #overview_features}

**Troubleshoot logs in real time to diagnose issues and identify problems.**

By using the *live streaming tail* feature, developers and DevOps teams can diagnose issues, analyze stack traces and exceptions, identify the source of errors, and monitor different log sources through a single view.  This feature is available through the command line and through the web interface. 

**Issue alerts to be notified of important actions.**
 
To act promptly on application and services events that you identify as critical or warning, DevOps teams can configure alert notification integrations to the following systems: email, Slack, HipChat, webHook, PagerDuty, and OpsGenie.

**Export logs to a local file for analysis or to an archive service to meet auditing requirements.**

Export specific log lines to a local copy or archive logs from {{site.data.keyword.la_full_notm}} to IBM Cloud Object Storage.
Log lines are exported in JSON line format. Logs are archived in JSON format and preserve the metadata that is associated with each line. 

**Control logging infrastructure costs by customizing what logs to manage through {{site.data.keyword.la_full_notm}}.**

Control the cost of your logging infrastructure in the IBM Cloud by configuring the log sources for which you want to collect and manage logs. 


## Pricing plans
{: #overview_pricing_plans}

Different pricing plans are available that you can choose for an {{site.data.keyword.la_full_notm}} instance. Each plan defines the number of days that data is retained for search, the number of users allowed to manage the data, and the LogDNA features that are enabled.

| Plan                     | 
|--------------------------|
| `30 days log search`  |
| `14 days log search`  |
| `7-day log search`   |
| `Lite`                  |
{: caption="Table 1. List of service plans" caption-side="top"} 

{{site.data.keyword.la_full_notm}} offers a `Lite` plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.

The following tables outline the different features that are included in each service plan:

| Feature                          | `30 day log search` plan | `14 days log search` plan    | `7 days log search plan     | `Lite` plan | 
|----------------------------------|-------------------------|-------------------------------|-----------------------------|--------------|
| `Logs are stored and searchable` | Yes - for 30 days       | Yes - for 14 days             | Yes - for 7 days            | No           |
| `Live streaming tail`            | Yes                     | Yes                           | Yes                         | Yes          |
| `Archiving`                      | Yes                     | Yes                           | Yes                         | No           |
| `Multi-channel Alerting`         | Yes                     | Yes                           | Yes                         | No           | 
{: caption="Table 2. List of features available for each service plan" caption-side="top"} 




