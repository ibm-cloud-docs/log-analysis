---

copyright:
  years:  2018, 2019
lastupdated: "2019-07-18"

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

# Data security
{: #data_security}

Across every industry, organizations require tighter controls and visibility into where their data is stored and processed in the {{site.data.keyword.cloud_notm}}. The {{site.data.keyword.la_full}} service offers EUprotecting the privacy of your data.  
{:shortdesc}

data residency
data protection
regulatory and compliance requirements including the General Data Protection Regulation (GDPR).


Concerns about data residency, security and personal data protection are at an all-time high as businesses prepare for pending regulatory and compliance requirements including the General Data Protection Regulation (GDPR).


## Data residency
{: #data_residency}

{{site.data.keyword.la_full_notm}} collects and aggregates logs in one centralized logging system.

* Log data is hosted on the {{site.data.keyword.cloud_notm}}.
* Data is colocated in the location where the {{site.data.keyword.la_full_notm}} instance is provisioned. For example, log data for an instance that is provisioned in US South is hosted in the US South region.

## Data protection
{: #data_protection}



## Data privacy
{: #data_privacy}



, and protect the privacy of your data,

IBM is taking that a step further to ensure access is restricted and to give clients control over and transparency with where their data lives, who has access to it and what they can do with this access.

Every enterprise is responsible for protecting its data. This includes knowing who has access to it and when. IBM will roll out new controls to ensure access to client content (including client personal data and special personal data) is restricted to and controlled by EU-based IBM employees only. These employees will play a critical role in IBM incident and change management processes by reviewing and approving all changes from non-EU based employees that could affect client data.

In a move that is unique to only IBM Cloud’s dedicated environments in Frankfurt, clients will review and approve all non-EU access requests to their content if an instance requires support or access from a non-EU based employee. If granted, this access is temporary and the client will be notified when the temporary access is revoked. Logs that track access are made available to the client.

To better support our EU clients, IBM is growing its customer support teams in Europe to provide 24×7 in-region operations and support. 


You can use {{site.data.keyword.la_full_notm}} to manage system and application logs in the {{site.data.keyword.cloud_notm}}.

## Enable “EU Supported” in IBM Cloud

## Deploy “EU supported” Apps and Services
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

