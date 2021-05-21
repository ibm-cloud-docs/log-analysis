---

copyright:
  years: 2019, 2021
lastupdated: "2021-05-21"

keywords: IBM, Log Analysis, logging, faq

subcollection: log-analysis

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:note: .note}
{:important: .important}
{:deprecated: .deprecated}
{:download: .download}
{:faq: data-hd-content-type='faq'}
{:term: .term}
{:external: target="_blank" .external}

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

Then, check the [Cloud services by location](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-event_types#event_types_location) documentation to find out the location where the logs are available for analysis.  


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
1. Check that you have IAM permissions to view the logging instances through the *Logging* dashboard. You must have **viewer** platform role permissions for the {{site.data.keyword.la_full_notm}} service. [Learn more about managing IAM policies and access groups](/docs/log-analysis?topic=log-analysis-work_iam)
.
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

```
ic resource service-instance <INSTANCE_NAME>
```
{: pre}

To get the name of the instance, run the following command `ibmcloud resource service-instances --all-resource-groups`. 

