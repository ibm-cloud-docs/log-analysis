---

copyright:
  years:  2018, 2020
lastupdated: "2020-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# Excluding log data by using exclusion rules in the web UI
{: #exclusion rules}

In an {{site.data.keyword.la_full_notm}} instance, you can configure exclusion rules through the LogDNA web UI to stop logs from counting against your data usage quota and from being stored for search.
{:shortdesc}


Complete the following steps to define an exclusion rule:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Select the **Settings** icon ![Configuration icon](images/admin.png "Admin icon"). Then select **Usage** &gt; **Exclusion Rules**. 

3. Select **Add Rule**. The **Create Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**.

5. Enter the exclusion criteria. You can select 1 or more sources, 1 or more apps, enter a query, or a combination of sources, apps and query.

    For example, to exclude all the lines from a specific source, select that source and leave the apps and query fields blank.

    You might want to exclude logs from an app, then leave the sources and query fields blank, and enter an app. 

    You might want to exclude all the logs that are coming from a specific source and app. You must choose the source and app, and leave blank the query field.

    You can enter a query to define the exclusion rule, or to refine the exclusion rule when you specify a source, an app, or both.

6. Select **Preserve these lines for live-tail and alerting ** to show through the live tail the log lines that are excluded. Notice that you can still use these log lines to set up an alert.

7. Click **Save**.


## Exclude syslog data for a worker while keeping entries that report errors only
{: #exclusion rules_sample}

You will configure the rule so that you are able to see all log data through views and be able to define alerts on all the data.

Complete the following steps to define the exclusion rule:

Prereq: You must have a cluster configured to forward logs to a LogDNA instance. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-config_agent_kube_cluster).

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Select the **Settings** icon ![Configuration icon](images/admin.png "Admin icon"). Then select **Usage** &gt; **Exclusion Rules**. 

3. Select **Add Rule**. The **Create Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**. For example, enter *Worker X no syslog data*.

5. Enter the exclusion criteria. You can select 1 or more sources, 1 or more apps, enter a query, or a combination of sources, apps and query.

    Click the *Sources* field. The list of options is displayed. Choose a worker. You can choose more than 1 source by clicking the field again and choosing a different source.

    Click the *Apps* field. The list of options is displayed. Choose **syslog**. 

    In the Query section, enter **-level:error** to exclude all lines except the ones that report an error.

6. Select **Preserve these lines for live-tail and alerting ** to show through the live tail the log lines that are excluded. Notice that you can still use these log lines to set up an alert.

7. Click **Save**.




## Exclude kube-system data from the cluster while keeping entries that report errors only
{: #exclusion rules_sample2}

You will configure the rule so that you are not able to see excluded log data through views.

Complete the following steps to define the exclusion rule:

Prereq: You must have a cluster configured to forward logs to a LogDNA instance. [Learn more](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-config_agent_kube_cluster).

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Select the **Settings** icon ![Configuration icon](images/admin.png "Admin icon"). Then select **Usage** &gt; **Exclusion Rules**. 

3. Select **Add Rule**. The **Create Rule** section opens.

4. Enter a name for the rule in the section **What is this rule for?**. For example, enter *Exclude log records from the namespace kube-system except error ones*.

5. Enter the exclusion criteria. You can select 1 or more sources, 1 or more apps, enter a query, or a combination of sources, apps and query.

    In the Query section, enter **Namespace:kube-system -level:error** to exclude all lines except the ones that report an error.

6. Leave unchecked the option **Preserve these lines for live-tail and alerting**. 

7. Click **Save**.


