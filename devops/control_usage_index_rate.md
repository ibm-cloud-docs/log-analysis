---

copyright:
  years: 2019, 2024
lastupdated: "2024-05-24"

keywords: IBM Cloud, Log Analysis, auditing, index alerts, spike protection

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Managing volume spike protection and costs
{: #control_usage_index_rate}

Configure index rates alerts in your {{site.data.keyword.la_full}} instance to monitor and be alerted of unexpected spikes in your data volumes. Use the index rate to analyze and predict costs associated with storage of searchable data.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

Index rates are calculated based on data that is ingested over the last 30 days and collected in 5 minute intervals.

Data collection commences on January 31, 2022 for existing instances. For new instances, data collection starts from the day that the instance is provisioned.
{: important}

The `standard hourly index rate` is used to identify spikes or deviations in data volumes. The standard deviation is calculated by comparing the average hourly index rate with the average of the same hour over a rolling 30 day period. The severity of a spike is measured in `standard deviations`.

The `z-score` represents the count of standard deviations. You can use it to predict costs associated with storage of searchable data.


## How are index rates calculated
{: #control_usage_index_rate_how}

The number of log lines that are indexed, that is, the number of log lines that are available for search, are collected every 5 minutes.

A day is based on a 24 hour period that is based on UTC time zone.

To calculate the `daily average index rate`, the following formula is applied:
1. The total number of indexed lines for the past hour, that is, the number of log lines over 1 hour rolling period, is collected.
2. The total number of indexed lines per hour is then divided by 60 to get the average of log lines per minute.
3. The average log lines per minute is then divided by 60 to get the average of log lines per second.
4. The index rate is calculated as the average value of all index rates that are calculated over 24 hours.

To calculate the `hourly average index rate`, also known as the `standard hourly index rate`, the following formula is applied:
1. The total number of indexed lines for the past hour, that is, the number of log lines over 1 hour rolling period, is collected.
2. The total number of indexed lines per hour is then divided by 60 to get the average of log lines per minute.
3. The average log lines per minute is then divided by 60 to get the average of log lines per second.
4. The index rate is calculated as the average value of all index rates that are calculated over the last hour by using  5 minutes increments.

The `daily min index rate` is the lowest index rate calculated over a 24 hour period.

The `daily max index rate` is the highest index rate calculated over a 24 hour period.

The `max lines threshold` indicates the maximum number of lines per second that you configure for your instance. This number represents the maximum number of lines that you expect to ingest per second for that instance.

If no log lines are ingested for over a 60-minute period, you get a **Check Later** message instead of the index rate value. When the ingestion of log lines is resumed, you get the index rate value. Measurements are taken every five minutes, therefore, the first measurement of ingested log lines for that five minutes will be averaged out for the full hour. Wait at least 1 hour before using the index rate value for analysis.

Only one alert for each alert channel will be sent until the hour or day has elapsed.  This alert will show all thresholds that have been exceeded during the period. If index rate alerts are configured on each separate threshold, an alert will be sent indicating the first threshold crossed (either `Max lines/s`, `Max z-score`, or both).

## Types of index rate alerts
{: #control_usage_index_rate_type}

There are two types of index rate alerts:

- **Max lines/s alerts**: Use this alert to monitor and control the number of log lines per second that are indexed and stored for search.

    - To monitor high flow rates, set an index rate threshold by configuring the `max lines alert` field so that you can get an alert when the value of lines per second is exceeded.

    - When the average index rate changes over time, you must review and configure the threshold accordingly.
    {: important}

- **Max z-score alerts**: Use this alert to monitor and control anomalous flow rates.

    - To monitor for spikes on logs and anomalous flow rates, set a threshold value by configuring the `max z-score` field so that you can get an alert when the hourly index rate is significantly higher than the monthly mean.

    - The baseline value is calculated using data from the last 30 days.

    After you provision an instance, you must wait a minimum of 30 days of data that has been indexed to use this feature.
    {: note}

    - Each z-score represents 1 standard deviation that is based on the distribution of index rates as seen over the past 30 days.

        0, 1 indicates a small spike of data.

        3 indicates a spike of data that requires troubleshooting and control.

        5 indicates a spike of data that requires quick action such as defining exclusion rules while you find out what source and app are causing a spike of data.

    Setting a maximum of 3 standard deviations is a good starting point for alert triggering.  You can then refine your alerting based on your needs.
    {: note}

## Launch the index rate alert page
{: #control_usage_index_rate_launch}

The index rate alert page offers an overview of your account's current rate of ingestion and indexing of searchable data. Through this page, you can see the ratio between the log lines that are ingested versus the number of log lines that are being stored.

To use the index rate feature on an instance, an administrator of the service must turn on the feature.

Complete the following steps to view the index rate dashboard and enable the feature:

1. [Navigating to the web UI](/docs/activity-tracker?topic=activity-tracker-launch).

2. Select the **settings** icon.

3. In the section **Usage**, select **Index Rate Alerts**.

4. Enable the feature.


When the feature is enabled, the *index rate alert page* is displayed.
- You can use the index rate alerts page to monitor the daily average index rates or the standard deviation from the past 30 days.
- You can toggle between viewing index rates or standard deviations for the past 30 days, the past 7 days, or the past 1 day.
- If no log lines are ingested in a 60 minute period, **Check Later** will be displayed instead of the index rate value.  Since measurements are taken every five minutes, the first measurement of ingested log lines for that five minutes will be averaged for the first hour.  Wait at least an hour before using the index rate value for analysis any time there has been an ingestion interruption.



## Activate the index rate alert feature
{: #control_usage_index_rate_activate}

You must set at least 1 threshold to activate the index rate alert feature.
{: important}

By default the index rate alert feature is disabled.

## Configure index rate alerts
{: #control_usage_index_rate_configure}

When you configure index rate alerts, you can gain insight into which applications, sources, or tags produce data spikes, as well as any recently added sources.
The alert message that is sent includes the following information:
- The top 20 sources and apps that have had the largest index rate growth in the past 2 hours.
- The list of the 20 newest sources added.
- A link to download generated lists of all applications and sources. You can view the “Manage Usage” Dashboard to download these lists at any time.

Complete the following steps:

### Step 1. Configure 1 or more rules
{: #control_usage_index_rate_configure_1}

Choose 1 or more of the following options to activate the index rate alert feature:
- `Max lines/s`: Set an index rate threshold by configuring the `max lines alert` field so that you can get an alert when the value of lines per second is exceeded.

- `Max z-score`: Set a threshold value by configuring the `max z-score` field so that you can get an alert when the hourly index rate is significantly higher than the monthly mean.


### Step 2. Configure the notification channels
{: #control_usage_index_rate_configure_2}

Choose 1 or more notification channels to receive an alert when the threshold of a rule is exceeded:

- Configure the email notification channel by selecting **Add email** and entering 1 or more emails.
- Configure the Slack notification channel by selecting **Add slack** and configuring the channel details.
- Configure the PagerDuty notification channel by selecting **Add PagerDuty** and entering the credentials.
- Configure the Webhook notification channel by selecting **Add Webhook** and entering the credentials.


### Step 3. Configure the notification frequency
{: #control_usage_index_rate_configure_3}

Choose the notification frequency. Valid options are:
- Hourly notifications
- Daily notifications at midnight UTC

Notifications are sent until the index rate repo-rts a value that is below the thresholds that you have configured.

Individual recipients may mute alert emails.

You can also configure a custom schedule to set the days and hours that you want alerts to be send if the thresholds are exceeded.
