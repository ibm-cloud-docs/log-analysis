---

copyright:
  years: 2019, 2023
lastupdated: "2023-05-09"

keywords: IBM, Log Analysis, logging, faq

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Frequently asked questions (FAQs)
{: #faq}

Frequently asked questions about {{site.data.keyword.la_full_notm}}.
{: shortdesc}

## Where can I find the list of Cloud services that send logs?
{: #faq_1}
{: faq}

You can find the list of Cloud services that generate logs in the following documentation topic: [Cloud services](/docs/log-analysis?topic=log-analysis-cloud_services).

## Where can I find details about the logs that a Cloud service generates?
{: #faq_2}
{: faq}

You can access more information about the logs that each Cloud service generates from the following documentation topic: [Cloud services](/docs/log-analysis?topic=log-analysis-cloud_services). For each Cloud service, you can link to the logging topic specific to a Cloud service where you can get more information.

## Where can I find the logs that a Cloud service generates?
{: #faq_3}
{: faq}

First, you must [check whether you have enabled **Platform logs** in the location where your Cloud service is available](/docs/log-analysis?topic=log-analysis-config_svc_logs).

Then, check the [Cloud services by location](/docs/log-analysis?topic=log-analysis-cloud_services_locations) documentation to find out the location where the logs are available for analysis.


## How do I configure archiving for my instance?
{: #faq_6}
{: faq}

To configure archiving see [Archiving events to IBM Cloud Object Storage](/docs/log-analysis?topic=log-analysis-archiving).

## How do I access the logging web UI? I cannot see the logging instance in the Observability page.
{: #faq_7}
{: faq}

To lauch the logging web UI, complete the following steps:
1. Check that you have IAM permissions to view the logging instances through the *Logging* dashboard. You must have **viewer** platform role permissions for the {{site.data.keyword.la_full_notm}} service. [Learn more about managing IAM policies and access groups](/docs/log-analysis?topic=log-analysis-work_iam).
2. [Launch the logging web UI](/docs/log-analysis?topic=log-analysis-launch).

## How do I reset an ingestion key?
{: #faq_8}
{: faq}

An ingestion key can be reset or new ones created in the logging web UI or using the API. You can have a maximum of 10 ingestion keys active at the same time in a logging instance.

Learn more about [resetting using the UI](/docs/log-analysis?topic=log-analysis-ingestion_key#reset) or [resetting using the API](/apidocs/log-analysis#list-key ).


## How can I get the ID of a logging instance?
{: #faq_9}
{: faq}

To get the ID of a logging instance, run the following command:

```text
ic resource service-instance <INSTANCE_NAME>
```
{: pre}

To get the name of the logging instance, run the following command `ibmcloud resource service-instances --all-resource-groups`.

## Can I import archived data into the UI?
{: #faq_10}
{: faq}

Archived data cannot be imported to be searched or used in the {{site.data.keyword.la_full_notm}} UI.

Use the [{{site.data.keyword.sqlquery_notm}} service](/docs/sql-query?topic=sql-query-getting-started) to query archive data.


## Why can't I create an API key?
{: #faq_11}
{: faq}

If you are unable to [create an API key](/docs/account?topic=account-userapikey&interface=ui) it could be because you are not authorized to do so.

Make sure your ID has the `User API key creator` permission enabled for the IAM service` as described [here.](/docs/account?topic=account-allow-api-create)

## How can I determine the version of the logging agent that is installed?
{: #faq_12}
{: faq}

The logging agent version that is installed is returned by running `logdna-agent -V`. You might need to run this command from the directory where the agent is installed.


## Can I control the ingested log lines so I can control my service cost?
{: #faq_13}
{: faq}

You can control the volume of log lines that you ingest. Controlling the log lines helps you control your {{site.data.keyword.la_short}} service cost. Logs that are filtered out (excluded) are not archived and are not available for search. You do not pay for log lines that are filtered out.

There are different ways in which you can filter out logs sent to {{site.data.keyword.la_short}}:

* You can [configure the agent to drop logs](/docs/log-analysis?topic=log-analysis-exclude_logs_from_agent) before sending them to the {{site.data.keyword.la_short}} service.

* If you send logs to the {{site.data.keyword.la_short}} service, you can define [exclusion rules](/docs/log-analysis?topic=log-analysis-exclusion_rules) to drop logs before they are stored for search.
   * You can drop the log lines entirely and not see them at all through the UI.

   * You can view the log lines in the UI, but you cannot search on them. However, you can define views and alerts based on the data from these logs.

* You can also configure [usage quotas](/docs/log-analysis?topic=log-analysis-control_usage_quotas) and define conditional usage quota exclusion rules.
