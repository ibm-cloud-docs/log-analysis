---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, control usage

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Controlling data usage
{: #control_usage}

In {{site.data.keyword.la_full_notm}}, you can control the data that is collected and available for analysis through a logging instance. You can define exclusion rules in the UI that apply to data collected in that instance. You can also configure logging agents and customize them to collect and forward specific log data. In addition, you can define an alert that is triggered when the data usage threshold that you define for that logging instance is reached.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}


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


## Configuring the usage alert
{: #control_usage_alert}

In a {{site.data.keyword.la_full_notm}} instance, you can define an alert to notify when the data usage in the instance reaches the data usage threshold that you set for the instance.
{: shortdesc}

Complete the following steps to configure an alert that informs you when you reach a specific data volume in the instance:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Usage** icon ![Usage icon](../images/usage.png "Usage").

    In the **Dashboard** section, you can see your data usage.

3. Define a **Usage Alert** to set the threshold for data usage in the instance. When the threshold is reached, you are notified. Enter a value to set the data usage threshold.

4. In the **Add recipient** section, enter one or more emails where the notification will be sent.


## Configuring an ingestion alert
{: #control_usage_3}

In {{site.data.keyword.la_full_notm}}, you can define an alert to notify when the data collected reaches a threshold within a period of time that you can customize.

[Learn more](/docs/log-analysis?topic=log-analysis-control_usage_instance).

## Analyzing event data trends
{: #control_usage_4}

In {{site.data.keyword.la_full_notm}}, you can query your logging instance by using the *Usage API* and identify trends over a period of time.

You can analyze event data trends to assess the growth or decline of logging data over time for services running in your account. You can monitor data trends to identify patterns and make predictions of how services are used in the account.

When you use the *Usage* API, consider the following information:
- Analyze 3 or more months worth of logging data to identify patterns and trends.
- You can use the API to monitor the number of lines that are collected per host, app or tag over a period of time.
- You can use the API to find out the top sources, apps, or tags that are driving the main load of data in a region.
- If you have exclusion rules defined, these lines are not included in the usage data response. The API reports number of lines that are ingested and not excluded via exclusion rules.

You can query data usage for up to 6 months.
{: note}

[Learn more](/docs/log-analysis?topic=log-analysis-control_usage_api).
