---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, config agent

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


# Controlling data usage
{: #control_usage}

In {{site.data.keyword.la_full_notm}}, you can control the data that is collected and available for analysis through a logging instance. You can define exclusion rules in the UI that apply to data collected in that instance. You can also configure logging agents and customize them to collect and forward specific log data. In addition, you can define an alert that is triggered when the data usage threshold that you define for that logging instance is reached.
{:shortdesc}


## Controlling data by excluding log files through the logging agent
{: #control_usage_agent}

You can stop logs from being forwarded to your logging instance by customizing the logging agent to exclude any files that you do not want the logging agent to monitor. 

* By default, the agent monitors all files with extension *.log*,  and extensionless files under */var/log/*.
* You must configure the **EXCLUDE** parameter in the logging agent configuration file to exclude files that are located in any of the paths that are defined through the **logdir** parameter. 
* To define the files that you want to exclude, you can separate multiple files by using commas. You can use glob patterns. You can also configure specific files.

[Learn more](/docs/log-analysis?topic=log-analysis-exclude_logs_from_agent).



## Controlling data by using exclusion rules
{: #control_usage_rule}

You can configure exclusion rules through the logging web UI to stop logs from counting against your data usage quota and from being stored for search. For example, you might want to collect and forward all logs from a source to a logging instance. However, you might be interested in a subset of those logs such as error logs. 

Logs that are excluded do not count towards your data usage quota. Also, logs that match the exclusion rule are not archived.
{: note}

When you exclude logs through an exclusion rule, you can choose to **Preserve these lines for live-tail and alerting**. When you check this option, log lines that match the exclusion rule are shown through the live tail and you can set up an alert for that data.

[Learn more](/docs/log-analysis?topic=log-analysis-exclusion_rules).

​


## Configuring an alert to notify when a data threshold is reached
{: #control_usage_alert}

In a {{site.data.keyword.la_full_notm}} instance, you can define an alert to notify when the data usage in the instance reaches the data usage threshold that you set for the instance.
{:shortdesc}

Complete the following steps to configure an alert that informs you when you reach a specific data volume in the instance:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Select the **Settings** icon ![Configuration icon](../images/admin.png "Admin icon"). Then select **Usage**.

    In the **Dashboard** section, you can see your data usage.

3. Define a **Usage Alert** to set the threshold for data usage in the instance. When the threshold is reached, you are notified. Enter a value to set the data usage threshold.

4. In the **Add recipient** section, enter one or more emails where the notification will be sent.



