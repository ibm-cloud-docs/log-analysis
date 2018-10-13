---

copyright:
  years: 2018
lastupdated: "2018-10-22"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}


# About IBM Log Analysis with LogDNA
{: #about}

IBM Log Analysis with LogDNA is a third-party service that you can include as part of your {{site.data.keyword.Bluemix}} architecture to add log management capabilities. IBM Log Analysis with LogDNA is operated by LogDNA in partnership with {{site.data.keyword.IBM_notm}}.
{:shortdesc}

You can use IBM Log Analysis with LogDNA to manage system and application logs in the {{site.data.keyword.Bluemix_notm}}.

IBM Log Analysis with LogDNA offers administrators, DevOps teams, and developers advanced features to filter, search, and tail log data, define alerts, and design custom views to monitor application and system logs.

For more information about LogDNA, see [Log Management & Log Analysis Docs ![External link icon](../icons/launch-glyph.svg "External link icon")](https://docs.logdna.com/docs){: new_window}.


## Overview
{: #ov}

To add logging features with LogDNA in the {{site.data.keyword.Bluemix_notm}}, you must provision an instance of IBM Log Analysis with LogDNA.

Before you provision an instance of IBM Log Analysis with LogDNA, consider the following information:

* You must accept the terms and conditions that specify that your data is sent to a third party.
* Your users must have platform permissions to create, view, and delete an instance of a service in the {{site.data.keyword.Bluemix_notm}}.
* Your users must have platform permissions to create resources within the context of the resource group where you plan to provision the LogDNA instance.

You provision an IBM Log Analysis with LogDNA instance within the context of a resource group. A resource group lets you organize your services for access control and billing purposes. You can provision the instance in the *default* resource group or in a custom resource group.

After you provision an instance of IBM Log Analysis with LogDNA, an account in created in LogDNA, and you receive the ingestion key for your account.

Then, you must configure a LogDNA agent for each log source. A log source is a cloud resource that generates logs. For example, a log source can be a Kubernetes cluster. You use the ingestion key to configure the LogDNA agent that is responsible for collecting and forwarding logs to your LogDNA instance.

After the LogDNA agent is deployed in a log source, collection and forwarding of logs to the LogDNA instance is automatic.

You can launch the LogDNA Web UI to view, monitor, and manage your logs.

The following figure shows the components overview for the LogDNA service that is running on {{site.data.keyword.Bluemix_notm}}:

![LogDNA component overview on the {{site.data.keyword.Bluemix_notm}}](images/components.png "LogDNA component overview on the {{site.data.keyword.Bluemix_notm}}")


## Log data
{: #data}

IBM Log Analysis with LogDNA collects and aggregates logs in one centralized logging system.

* Log data is hosted on the {{site.data.keyword.Bluemix_notm}}.
* Data is colocated in the region where the IBM Log Analysis with LogDNA instance is provisioned. For example, log data for an instance provisioned in US South is hosted in the US South region.

The service plan that you choose for an IBM Log Analysis with LogDNA instance defines the number of days that data is stored and retained in LogDNA. For example, if you choose the *Free* plan, data is not stored at all. However, if you choose the 7 day plan, data is stored for 7 days and you have access to it through the LogDNA Web UI.

When you delete an instance of IBM Log Analysis with LogDNA from the {{site.data.keyword.Bluemix_notm}, all the data is deleted.



## Features
{: #features}

**Troubleshoot logs in real-time to diagnose issues and identify problems.**

By using the *live streaming tail* feature, developers and DevOps teams can diagnose issues, analyze stack traces and exceptions, identify the source of errors, and monitor different log sources through a single view.  This feature is available through the command line and through the web interface. 

**Issue alerts to be notified of important actions.**
 
To act promptly on application and services events that you identify as critical or warning, DevOps teams can configure alert notification integrations to the following systems: email, Slack, HipChat, WebHook, PagerDuty, and OpsGenie.

**Export logs to a local file for analysis or to an archive service to meet auditing requirements.**

Export specific log lines to a local copy or archive logs from IBM Log Analysis with LogDNA to IBM Cloud Object Storage.
Log lines are exported in JSON line format. Logs are archived in JSON format and preserve the metadata that is associated with each line. 

**Control logging infrastructure costs by customizing what logs to manage through IBM Log Analysis with LogDNA.**

Control the cost of your logging infrastructure in the IBM Cloud by configuring the log sources for which you want to collect and manage logs. 


## Pricing plans
{: #pricing_plans}

Different pricing plans are available that you can choose for an IBM Log Analysis with LogDNA instance. Each plan defines the number of days that data is retained, the number of users allowed to manage the data, and the LogDNA features that are enabled.

| Plan                 | 
|----------------------|
| `30 days log search` |
| `14 days log search` |
| `7 days log search`  |
| `Free LogDNA plan`   |
{: caption="Table 1. List of service plans" caption-side="top"} 

IBM Log Analysis with LogDNA offers a **Free** plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.

## Regions
{: #regions}

Logging with IBM Log Analysis with LogDNA is available in the **US South** region only. The **US South** region is also known as the **Dallas** region.


