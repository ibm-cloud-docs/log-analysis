---

copyright:
  years: 2018, 2023
lastupdated: "2022-12-13"

keywords: Log Analysis release notes

subcollection: log-analysis

content-type: release-note

---

{{site.data.keyword.attribute-definition-list}}

# Release notes for {{site.data.keyword.la_full_notm}}
{: #log-analysis-release-notes}

Use these release notes to learn about the latest updates to {{site.data.keyword.la_full}}.
{: shortdesc}

## 14 December 2022
{: #log-analysis-dec1422}
{: release-note}

Upcoming changes to endpoint IP addresses
:   Several [endpoint IP addresses](/docs/log-analysis?topic=log-analysis-endpoints) will be changing in after 15 January 2023. If your service is configured to use specific IP addresses or firewall to a specific IP address, then modification to the new IP addresses might be required. Allowlisted IP addresses can be configured in advance of the change to avoid service interruptions. For more information on the endpoint changes, see [Service IP changes.](/docs/log-analysis?topic=log-analysis-service-ip-changes#endpoint-changes-01Jan2022)

## 08 December 2022
{: #log-analysis-dec0822}
{: release-note}

Changes to endpoint IP addresses
:   Several [endpoint IP addresses](/docs/log-analysis?topic=log-analysis-endpoints) have changed. If your service is configured to use specific IP addresses or firewall to a specific IP address, then modification to the new IP addresses might be required. For more information on the endpoint changes, see [Service IP changes.](/docs/log-analysis?topic=log-analysis-service-ip-changes#endpoint-changes-08Dec2022)

## 03 October 2022
{: #log-analysis-oct0322}
{: release-note}

Availability of the {{site.data.keyword.la_full_notm}} agent 3.6

:   Windows logging agent 3.6 is now available. This agent is a rust agent that includes Windows File Logging support.

    `MZ_` environment variables are available.

    [For more information about the agent.](https://docs.mezmo.com/changelog/mezmo-agent-3-6--ga-){: external} [Learn about configuring the agent.](/docs/log-analysis?topic=log-analysis-config_agent_windows_v3)


## 06 May 2022
{: #log-analysis-may0622}
{: release-note}

Changes to endpoint IP addresses
:   Several [endpoint IP addresses](/docs/log-analysis?topic=log-analysis-endpoints) have changed. If your service is configured to use specific IP addresses or firewall to a specific IP address, then modification to the new IP addresses will be required.  Until 23 May 2022 the [original endpoints are in effect.](/docs/log-analysis?topic=log-analysis-service-ip-changes#endpoint-changes-09May2022)

## 24 March 2022
{: #log-analysis-mar2422}
{: release-note}

Ability to limit access to private endpoints only
:   You can limit access to an {{site.data.keyword.la_full}} instance to private endpoints only.    [Learn more](/docs/log-analysis?topic=log-analysis-private_endpoints_only).

## 11 February 2022
{: #log-analysis-feb1122}
{: release-note}

Support for syslog private endpoints
:   {{site.data.keyword.la_full_notm}} now supports syslog private endoints.  [Learn more about syslog private endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog_private_endpoints).

## 3 February 2022
{: #log-analysis-feb0322}
{: release-note}

Changes to Tokyo syslog IP addresses
:   The [IP addresses used for the `syslog-a.jp-tok.logging.cloud.ibm.com` endpoint](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog) have changed. If your service is configured to use specific IP addresses or firewall to a specific IP address, then modification to the new IP addresses will be required.

## 31 January 2022
{: #log-analysis-jan3122}
{: release-note}

Index rate analysis to alert on unexpected data volume spikes
:   You can configure index rates alerts in your {{site.data.keyword.la_full_notm}} instance to monitor and be alerted of unexpected spikes in your data volumes. Use the index rate to analyze and predict costs associated with storage of searchable data.  [Learn more about index rate analysis](/docs/log-analysis?topic=log-analysis-control_usage_index_rate).

Managing and limiting data usage
:   In your {{site.data.keyword.la_full_notm}} instance, you can use the usage quota settings to control how much data is stored so you can manage your data cost while still being able to view and retain the data you need.  [Learn more about usage quotas](/docs/log-analysis?topic=log-analysis-control_usage_quotas).

## 4 October 2021
{: #log-analysis-oct0421}
{: release-note}

API for archiving
:   Documentation of API changes supporting archiving is generally available.  [Learn more about the archiving API](https://{DomainName}/apidocs/log-analysis#get-v1-config-archiving){: external}.

## 30 September 2021
{: #log-analysis-sep3021}
{: release-note}

API for data streaming
:   Documentation of API changes supporting data streaming is generally available.  [Learn more about the streaming API](/apidocs/log-analysis#post-v1-config-stream).

## 31 August 2021
{: #log-analysis-aug3121}
{: release-note}

Support to stream data is generally available
:   Streaming data from an {{site.data.keyword.la_full_notm}} instance to other corporate tools such as Security Information and Event Management (SIEM) tools is generally available. [Learn more about streaming](/docs/log-analysis?topic=log-analysis-streaming).

## 2 July 2021
{: #log-analysis-jul0221}
{: release-note}

Support to stream data is available in beta
:   New beta feature released in US-South and Frankfurt to stream data from an {{site.data.keyword.la_full_notm}} instance to other corporate tools such as Security Information and Event Management (SIEM) tools. [Learn more about streaming](/docs/log-analysis?topic=log-analysis-streaming).

## 31 March 2021
{: #log-analysis-mar3121}
{: release-note}

New CLI support
:   New CLI added that can be used to list instances and export data from an instance. [Learn
more about the CLI](/docs/log-analysis?topic=logdna-cli-plugin-logdna-cli).

New API support
:   New API added that can be used to export data from an instance, and manage views and alerts. [Learn more about the API](https://cloud.ibm.com/apidocs/logdna?code=python#introduction){: external}.

## 31 January 2021
{: #log-analysis-jan3121}
{: release-note}

Changes to archiving frequency
:   Hourly archiving in Chennai, Tokyo, Sydney, Seoul, London, Washington instead of daily archiving. [Learn more](/docs/log-analysis?topic=log-analysis-archiving).

## 31 December 2020
{: #log-analysis-dec3120}
{: release-note}

Addition of configuration support using an API
:   Configuration support using an API, in addition to configuration using the web UI.

Terraform support
:   Support for Terraform to programmatically manage {{site.data.keyword.la_full}} instances and agents and automate their deployment.

## 9 July 2020
{: #log-analysis-jul0920}
{: release-note}

HIPPA service plans available
:   Added support for 30-day search plans for HIPAA workloads.

## 19 July 2019
{: #log-analysis-jul1920}
{: release-note}

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
