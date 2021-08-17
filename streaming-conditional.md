---

copyright:
  years: 2019, 2021
lastupdated: "2021-07-01"

keywords: IBM Cloud, Activity Tracker, streaming

subcollection: log-analysis

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
{:external: target="_blank" .external}
{:deprecated: .deprecated}

# Configuring conditional streaming
{: #streaming-conditional}

In an {{site.data.keyword.la_full_notm}} instance, you can configure streaming exclusion rules through the UI to filter what data is streamed.
{:shortdesc}

You must have manager access to define exclusion rules.
{: note}

Complete the following steps to define an exclusion rule:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/services/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Configuration icon](images/admin.png "Admin icon"). Then select **Streaming** &gt; **Exclusion Rules**. 

3. Select **Add Rule**. The **Create a Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**

5. Enter the exclusion criteria by adding a query. For more information on how to build a query, see [Select the set of events to display through a view by applying a search query](/docs/log-analysis?topic=log-analysis-views#views_step2).

7. Click **Save**.







