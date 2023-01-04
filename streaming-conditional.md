---

copyright:
  years: 2019, 2023
lastupdated: "2022-07-21"

keywords: IBM Cloud, Log Analysis, streaming

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring conditional streaming
{: #streaming-conditional}

In an {{site.data.keyword.la_full_notm}} instance, you can configure streaming exclusion rules through the UI to filter what data is streamed.
{: shortdesc}

- Log lines that match a streaming exclusion rule are not streamed.

- When log lines are ingested, streaming exclusion rules are applied to log lines that are retained after the ingestion exclusion rules are applied.


You must have manager access to define exclusion rules.
{: note}

Complete the following steps to define an exclusion rule:

Verify that each exclusion rule that you add behaves as expected. Improper configured exclusion rules can result in storing data not intended for storage.
{: important}

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/services/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Configuration icon](images/admin.png "Admin icon"). Then select **Streaming** &gt; **Exclusion Rules**.

3. Select **Add Rule**. The **Create a Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**

5. Enter the exclusion criteria by adding a query. For more information on how to build a query, see [Select the set of events to display through a view by applying a search query](/docs/log-analysis?topic=log-analysis-views#views_step2).

6. Click **Save**.

7. After you configure an exclusion rule, verify that the exclusion rule behaves as you expect.

    Check the query in a custom view by entering the search criteria in the search bar of the *Everything* view, and validating that the data that is displayed is the data that you want excluded.
    {: tip}
