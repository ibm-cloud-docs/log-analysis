---

copyright:
  years:  2018, 2024
lastupdated: "2024-03-27"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Excluding log data by using exclusion rules in the web UI
{: #exclusion_rules}

In an {{site.data.keyword.la_full_notm}} instance, you can configure exclusion rules through the logging web UI to stop logs from counting against your data usage quota and from being stored for search.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

Complete the following steps to define an exclusion rule:

Verify that each exclusion rule that you add behaves as expected. Improper configured exclusion rules can result in storing data not intended for storage.
{: important}

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Usage** &gt; **Exclusion Rules**.

3. Select **Add Rule**. The **Create Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**.

5. Enter the exclusion criteria. You can select 1 or more sources, 1 or more apps, enter a query, or a combination of sources, apps and query.

    For example, to exclude all the lines from a specific source, select that source and leave the apps and query fields blank.

    You might want to exclude logs from an app, then leave the sources and query fields blank, and enter an app.

    You might want to exclude all the logs that are coming from a specific source and app. You must choose the source and app, and leave blank the query field.

    You can enter a query to define the exclusion rule, or to refine the exclusion rule when you specify a source, an app, or both.

6. Select **Preserve these lines for live-tail and alerting ** to show through the live tail the log lines that are excluded. Notice that you can still use these log lines to set up an alert.

7. Click **Save**.

8. After you configure an exclusion rule, verify that the exclusion rule behaves as you expect.

    Check the query in a custom view by entering the search criteria in the search bar of the *Everything* view, and validating that the data that is displayed is the data that you want excluded.
    {: tip}


## Sample 1: Exclude syslog data for a worker while keeping entries that report errors only
{: #exclusion_rules_sample}

You will configure the rule so that you are able to see all log data through views and be able to define alerts on all the data.

Complete the following steps to define the exclusion rule:

Prereq: You must have a cluster configured to forward logs to a logging instance. [Learn more](/docs/log-analysis?topic=log-analysis-config_agent_kube_cluster).

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Usage** &gt; **Exclusion Rules**.

3. Select **Add Rule**. The **Create Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**. For example, enter *Worker X no syslog data*.

5. Enter the exclusion criteria. You can select 1 or more sources, 1 or more apps, enter a query, or a combination of sources, apps and query.

    Click the *Sources* field. The list of options is displayed. Choose a worker. You can choose more than 1 source by clicking the field again and choosing a different source.

    Click the *Apps* field. The list of options is displayed. Choose **syslog**.

    In the Query section, enter **-level:error** to exclude all lines except the ones that report an error.

6. Select **Preserve these lines for live-tail and alerting ** to show through the live tail the log lines that are excluded. Notice that you can still use these log lines to set up an alert.

7. Click **Save**.

    Check the query in a custom view by entering the search criteria in the search bar of the *Everything* view, and validating that the data that is displayed is the data that you want excluded.
    {: tip}


## Sample 2: Exclude kube-system data from the cluster while keeping entries that report errors only
{: #exclusion_rules_sample2}

You will configure the rule so that you are not able to see excluded log data through views.

Complete the following steps to define the exclusion rule:

Prereq: You must have a cluster configured to forward logs to a logging instance. [Learn more](/docs/log-analysis?topic=log-analysis-config_agent_kube_cluster).

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Configuration icon](../images/admin.png "Configuration icon"). Then select **Usage** &gt; **Exclusion Rules**.

3. Select **Add Rule**. The **Create Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**. For example, enter *Exclude log records from the namespace kube-system except error ones*.

5. Enter the exclusion criteria. You can select 1 or more sources, 1 or more apps, enter a query, or a combination of sources, apps and query.

    In the Query section, enter **Namespace:kube-system -level:error** to exclude all lines except the ones that report an error.

6. Leave unchecked the option **Preserve these lines for live-tail and alerting**.

7. Click **Save**.

    Check the query in a custom view by entering the search criteria in the search bar of the *Everything* view, and validating that the data that is displayed is the data that you want excluded.
    {: tip}
