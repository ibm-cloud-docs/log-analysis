---

copyright:
  years: 2018, 2020
lastupdated: "2020-01-08"

keywords: LogDNA, IBM, Log Analysis, logging, alerts

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

 
# Working with alerts
{: #alerts}

You can attach one or more alerts to a view. You can define multiple notification channels for an alert. You can mute alerts. You can detach alerts from a view.
{:shortdesc}

You can configure any of the following conditions for an alert:

* *Time frequency*: Specify how often to trigger an alert. Valid values are: 30 seconds, 1 minute, 5 minutes, 15 minutes, 30 minutes, 1 hour, 6 hours, 12 hours, 24 hours
* *Log lines counter*: Specify the number of log lines that match the view's filtering and search criteria. When the number of log lines is reached, an alert is triggered.

You can decide whether both conditions are checked or only one. If both conditions are set, an alert is triggered when any of the thresholds is reached. 

For example, you can configure an alert that is triggered after 30 seconds, or when a 100 log lines that match the view's filtering and search criteria are collected.

You can configure multiple notification channels. Valid channels are: `email`, `Slack`, `PagerDuty`, `Webhook`, `OpsGenie`, `Datadog`, `AppOptics`, `VictorOps`

You can also define a **preset**. A preset is an alert template that you can attach to any number of views. 

To reuse an alert configuration with different views, configure an **alert preset**.
{: tip}

A bell icon is displayed with the view to indicate that this view has an alert attached to it.



## Configure a preset (alert template)
{: #config_preset}

Complete the following steps to configure a preset:

1. Select the **Settings** icon ![Configuration icon](images/admin.png "Admin icon").
2. Select **Alerts**.
3. Select **Add a preset alert**.
4. Choose a notification channel. 
5. Define the threshold conditions.

    1. Select a time frequency. For example, 12 hours.

    2. Enter the number of log lines after which you want the alert to trigger.

    3. Select whether you want both conditions to be checked or just one.

6. Add the details for the notification channel that you have chosen.

    For example, for the email notification channel, add one or more recipients, and optionally a time zone.

7. Click **Save alert**.



## Configure an alert by using a preset
{: #config_alert_preset}

Complete the following steps to attach a preset to a view:

1. Click the **Views** icon ![Configuration icon](images/views.png).
2. Create a view. 

    Apply a time frame, filters and search criteria to filter the log lines that are displayed through the view. 

    For more information, see [Creating views](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Click the view name. Then, select **Attach an alert**.

4. Choose a preset to reuse an alert definition. 

5. Click **Save alert**. 




## Configure a view-specific alert
{: #config_alert_view}

Complete the following steps to attach an alert to a view:

1. Click the **Views** icon ![Configuration icon](images/views.png).
2. Create a view. 

    Apply a time frame, filters and search criteria to filter the log lines that are displayed through the view. 

    For more information, see [Creating views](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Click the view name. Then, select **Attach an alert**.

4. Choose **view-specific alert**.

5. Choose a notification channel. 

6. Define the threshold conditions.

    1. Select a time frequency. For example, 12 hours.

    2. Enter the number of log lines after which you want the alert to trigger.

    3. Select whether you want both conditions to be checked or just one.

7. Add the details for the notification channel that you have chosen.

    For example, for the email notification channel, add one or more recipients, and optionally a time zone.

8. Click **Save alert**.



## Delete a preset (alert template)
{: #delete_preset}

Complete the following steps to delete a preset:

1. Select the **Configuration** icon ![Configuration icon](images/admin.png "Admin icon").
2. Select **Alerts**.
3. Hover the mouse over the *edit* button of the preset that you want to delete. The *delete* option shows.
4. Select **Delete**.
5. Confirm that you want to delete the preset. Click **Delete**.

## Detach a view-specific alert from a view
{: #delete_alert}

Complete the following steps to detach a preset:

1. Select the **Configuration** icon ![Configuration icon](images/admin.png "Admin icon").
2. Select **Alerts**.
3. Hover the mouse over the *edit* button of the alert that you want to delete. The *delete* option shows.
4. Select **Detach**.
5. Confirm that you want to delete the alert. Click **Detach**.



## Notification channels
{: #channels}

The following table lists the notification channels that you can configure when an alert is triggered:

| Channel           | Configuration details | 
|-------------------|-----------------------|
| `email`             | You can configure one or more email addresses.  | 
| `Slack`             | You can configure a slack channel. |
| `Webhook`           | You can configure a web hook URL. |
| `PagerDuty`         | You can configure connection details to your PagerDuty system, and select a service.|
| `OpsGenie`          | You can configure the API key to connect to your OpsGenie system. |
| `Datadog`           | You can configure the API key to connect to your `Datadog` system. |
| `AppOptics/Librato` | You can configure the API key to connect to your AppOptics/Librato system. |
| `VictorOps`         | You can configure the URL to notify when an alert is triggered, the routing key, and an alert type. Valid alert types are: `info`, `warning`, `critical` |
{: caption="Notification channels" caption-side="top"} 


