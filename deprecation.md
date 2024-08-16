---

copyright:
  years:  2018, 2024
lastupdated: "2024-07-31"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Deprecation of {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}
{: #deprecation}

{{site.data.keyword.logs_full_notm}} replaces {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} providing the functions of those services, and more.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

{{site.data.keyword.at_full_notm}} is being deprecated, but activity tracking events will be supported in both the new {{site.data.keyword.logs_full_notm}} service and with the existing [{{site.data.keyword.atracker_full_notm}}](/docs/atracker) service.
{: important}

{{site.data.keyword.cloud_notm}} has deprecated and will end support of {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} on 30 March 2025. These two services are being replaced with the new {{site.data.keyword.logs_full_notm}} service.

[{{site.data.keyword.logs_full_notm}}](http://ibm.biz/cloudlogsannounce) replaces both {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}}. The {{site.data.keyword.logs_full_notm}} service has the capabilities that both services offer and provides enhanced functions in a single service. You have a choice to maintain separate {{site.data.keyword.logs_full_notm}} instances for log data and activity event data. Or, you could combine the data into a single service instance for operational simplicity and expanded observability.  Tools will be provided to help you migrate your {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} configurations to {{site.data.keyword.logs_full_notm}}.

At the {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} end of support date, any existing instance of both services will be permanently disabled and de-provisioned. Service data is saved if archiving was enabled prior to the end of support date. 

For information on archiving, see:
{: #laat-archive}

* [{{site.data.keyword.la_full}} archiving](/docs/log-analysis?topic=log-analysis-archiving-ov)
* [{{site.data.keyword.at_full_notm}} archiving](/docs/activity-tracker?topic=activity-tracker-archiving-ov)

## Why {{site.data.keyword.logs_full_notm}}?
{: #cloud-logs-intro}

The volume of application data generated and processed is increasing exponentially.  As businesses increasing rely on cloud services for data insights, the cost of downtime, slow performance, and customer satisfaction becomes an increasing challenge. The tools and techniques available for this increased workload observability must be balanced against the volume of data processed to have the right cost control balance. {{site.data.keyword.logs_full_notm}} gives you increased insights into the ever increasing generated data and provides tools to manage data growth against your budget.

{{site.data.keyword.logs_full_notm}} gives you flexibility in how your data is processed for insights and trends, and where data is stored for high-speed search and long term trend analysis. It provides the tools for you to maximize the value obtained while maintaining control on the total cost at all times:

* Data required primarily for long term retention could be sent directly to {{site.data.keyword.cos_full_notm}} buckets. You will have the ability to search the data in the bucket, regardless of the age of the data.

* Data required for analysis and alerting can be processed for alerts, real-time visualization, metrics, and analytics.

* Key data for operational insights could be directed to high-speed search for the fastest query results and the handling complex queries during analysis.

Control of your data consumption and cost is managed through the service’s TCO Optimizer. Using the TCO Optimizer you can configure rules to control how your data is processed in the service. Optimizer rules are configured to control how data is processed allowing you to balance expanding data consumption within your existing budgets.

{{site.data.keyword.logs_full_notm}} goes beyond existing logging capabilities to put expanded capabilities into your hands without sacrificing core logging performance.

As IBM Cloud transitions from {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}}, IBM endeavors to protect your investment in {{site.data.keyword.cloud_notm}} observability.

### Additional benefits of {{site.data.keyword.logs_full_notm}}
{: #cloud-logs-additional}

{{site.data.keyword.logs_full_notm}} adds expanded observability functions:

* Increase data insights with client-defined parsing rules to enrich and restructure data in real-time.

* Build not a single alert, but a flow of multiple alerts, enabling you to more quickly define the root cause of the issue.

   * {{site.data.keyword.logs_full_notm}} alerts can integrate with the {{site.data.keyword.en_full_notm}} service where clients might centralize alert routing with other {{site.data.keyword.cloud_notm}} alerts.

   * Do alert incident management within {{site.data.keyword.logs_full_notm}}.

* Alert incidents are managed within the {{site.data.keyword.logs_full_notm}} console. This allows you to easily manage application environments and workloads and reduce the number of tools necessary to meet SLA objectives. 

* Define metrics from incoming log and event data to quickly visualize data for trend analysis.

* Apply machine learning analytics templates to incoming data for log aggregation and anomaly detection.

* Search that spans all your log data, on-demand.

A migration tool is provided to move many key configuration attributes from {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}}.

If you plan to migrate using the migration tool, you must do so before {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} are de-provisioned and deleted on 30 March 2025.
{: important}



Full information about the new service is available in the [{{site.data.keyword.logs_full_notm}} documentation.](/docs/cloud-logs)

## Deprecation timeline
{: #deprecation-timeline}

| Date | Event |
|------|-------|
| 28 March 2024 | Announcement of the deprecation of {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} |
| 24 June 2024 | General availability of {{site.data.keyword.logs_full_notm}}.  \n  \n Deployment to {{site.data.keyword.cloud_notm}} regions will occur over time. Migration to {{site.data.keyword.logs_full_notm}} can begin in an MZR when {{site.data.keyword.logs_full_notm}} is available in the region. |
| Ongoing | End of marketing for new users.  \n  \n Once {{site.data.keyword.logs_full_notm}} is available in a region, users who do not have an existing {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instance in that region will be unable to provision a new {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instance 30 days after {{site.data.keyword.logs_full_notm}} is available in that region. See [Locations](/docs/cloud-logs?topic=cloud-logs-regions) for the regions where {{site.data.keyword.logs_full_notm}} is available.  \n  \n Users that have existing {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instances can continue to deploy instances in all regions as required. |
| 30 November 2024 | End of marketing for existing {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} user.  \n  \n Users with existing {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instances will not be able to provision new instances.
| 30 March 2025| End of support and end of life of {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}.  \n  \n Any {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instances still existing will be stopped and deleted.  \n  \n [Archived data](#laat-archive) is retained in the {{site.data.keyword.cos_full_notm}} bucket under the customer's control. |
{: caption="Table 2. Deprecation timeline" caption-side="bottom"}


