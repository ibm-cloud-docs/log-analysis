---

copyright:
  years: 2019, 2023
lastupdated: "2023-02-20"

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

You can find the list of services that generate logs in the following documentation topic: [Cloud services](/docs/log-analysis?topic=log-analysis-cloud_services).

## Where can I find details about the logs that a service generates?
{: #faq_2}
{: faq}

You can access more information about the logs that each service generates from the following documentation topic: [Cloud services](/docs/log-analysis?topic=log-analysis-cloud_services). For each service, you can link to the logging topic specific to a service where you can get more information.

## Where can I find the logs that a service generates?
{: #faq_3}
{: faq}

First, you must [check whether you have enabled **Platform logs** in the location where your service is available](/docs/log-analysis?topic=log-analysis-config_svc_logs).

Then, check the [Cloud services by location](/docs/log-analysis?topic=log-analysis-cloud_services_locations) documentation to find out the location where the logs are available for analysis.


## Can I import archived data back into the logging web UI?
{: #faq_5}
{: faq}

You cannot import archived data into the logging web UI.

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

An ingestion key can only be reset or new ones created in the logging web UI. You can have a maximum of 10 ingestion keys active at the same time in a logging instance.

[Learn more](/docs/log-analysis?topic=log-analysis-ingestion_key#reset).


## How can I get the ID of an instance?
{: #faq_9}
{: faq}

To get the ID of a logging instance, run the following command:

```text
ic resource service-instance <INSTANCE_NAME>
```
{: pre}

To get the name of the instance, run the following command `ibmcloud resource service-instances --all-resource-groups`.

## Can I import archived data into the UI?
{: #faq_10}
{: faq}

Archived data cannot be imported to be searched or used in the {{site.data.keyword.la_full_notm}} UI.

Use the [{{site.data.keyword.sqlquery_notm}} service](/docs/sql-query?topic=sql-query-getting-started) to query archive data.


## Why can't I create an API key?
{: #faq_11}
{: faq}

If you are unable to [create an API key](/docs/account?topic=account-userapikey&interface=ui) it could be because you are not authorized to do so.

Make sure your ID has the [`User API key creator` permission enabled for the `IAM Identity Service`.](/docs/account?topic=account-allow-api-create)

## How can I determine the version of the logging agent that is installed?
{: #faq_12}
{: faq}

The logging agent version that is installed is returned by running `logdna-agent -V`. You might need to run this command from the directory where the agent is installed.
