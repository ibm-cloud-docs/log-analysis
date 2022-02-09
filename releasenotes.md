---

copyright:
  years: 2018, 2022
lastupdated: "2022-02-03"

keywords: Log Analysis release notes

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Release notes for {{site.data.keyword.la_full_notm}}
{: #log-analysis-release-notes}

Use these release notes to learn about the latest updates to {{site.data.keyword.la_full}}.  
{: shortdesc}

## 3 February 2022
{: #log-analysis-feb0322}

Changes to Tokyo syslog IP addresses
:   The [IP addresses used for the `syslog-a.jp-tok.logging.cloud.ibm.com` endpoint](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog) have changed. If your service is configured to use specific IP addresses or firewall to a specific IP address, then modification to the new IP addresses will be required. 

## 31 January 2022
{: #log-analysis-jan3122}

Index rate analysis to alert on unexpected data volume spikes
:   You can configure index rates alerts in your {{site.data.keyword.la_full_notm}} instance to monitor and be alerted of unexpected spikes in your data volumes. Use the index rate to analyze and predict costs associated with storage of searchable data.  [Learn more about index rate analysis](/docs/log-analysis?topic=log-analysis-control_usage_index_rate).

Managing and limiting data usage
:   In your {{site.data.keyword.la_full_notm}} instance, you can use the usage quota settings to control how much data is stored so you can manage your data cost while still being able to view and retain the data you need.  [Learn more about usage quotas](/docs/log-analysis?topic=log-analysis-control_usage_quotas).

## 4 October 2021
{: #log-analysis-oct0421}

API for archiving
:   Documentation of API changes supporting archiving is generally available.  [Learn more about the archiving API](https://{DomainName}/apidocs/log-analysis#get-v1-config-archiving){: external}.

## 30 September 2021
{: #log-analysis-sep3021}

API for data streaming
:   Documentation of API changes supporting data streaming is generally available.  [Learn more about the streaming API](/apidocs/log-analysis#post-v1-config-stream).

## 31 August 2021
{: #log-analysis-aug3121}

Support to stream data is generally available
:   Streaming data from an {{site.data.keyword.la_full_notm}} instance to other corporate tools such as Security Information and Event Management (SIEM) tools is generally available. [Learn more about streaming](/docs/log-analysis?topic=log-analysis-streaming).

## 2 July 2021
{: #log-analysis-jul0221}

Support to stream data is available in beta
:   New beta feature released in US-South and Frankfurt to stream data from an {{site.data.keyword.la_full_notm}} instance to other corporate tools such as Security Information and Event Management (SIEM) tools. [Learn more about streaming](/docs/log-analysis?topic=log-analysis-streaming).

## 31 March 2021
{: #log-analysis-mar3121}

New CLI support
:   New CLI added that can be used to list instances and export data from an instance. [Learn 
more about the CLI](/docs/log-analysis?topic=logdna-cli-plugin-logdna-cli).

New API support
:   New API added that can be used to export data from an instance, and manage views and alerts. [Learn more about the API](https://cloud.ibm.com/apidocs/logdna?code=python#introduction){: external}.

## 31 January 2021
{: #log-analysis-jan3121}

Changes to archiving frequency
:   Hourly archiving in Chennai, Tokyo, Sydney, Seoul, London, Washington instead of daily archiving. [Learn more](/docs/log-analysis?topic=log-analysis-archiving).

## 31 December 2020
{: #log-analysis-dec3120}

Addition of configuration support using an API
:   Configuration support using an API, in addition to configuration using the web UI.

Terraform support
:   Support for Terraform to programmatically manage {{site.data.keyword.la_full}} instances and agents and automate their deployment. 

## 9 July 2020
{: #log-analysis-jul0920}

HIPPA service plans available
:   Added support for 30-day search plans for HIPAA workloads.

## 19 July 2019
{: #log-analysis-jul1920}

Enhanced data residency, compliance, and security
:   The following support is now available:

    * Services are available in London and Tokyo.
    * Services in Frankfurt are now available as EU-Managed.
    * Cloud Service endpoint support is available in all regions.


## 27 November 2018
{: #log-analysis-nov2718}
{: release-note}

Introducing {{site.data.keyword.la_full_notm}}
:   You can use {{site.data.keyword.la_full_notm}} to manage system and application logs in the {{site.data.keyword.cloud_notm}}. {{site.data.keyword.la_full_notm}} offers administrators, DevOps teams, and developers advanced features to filter, search, and tail log data, define alerts, and design custom views to monitor application and system logs.   [Learn more](/docs/log-analysis?topic=log-analysis-getting-started#getting-started) 
