---

copyright:
  years:  2018, 2023
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, services

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Monitoring logs in your account
{: #monitor_logs}

You can monitor logs in your account through the {{site.data.keyword.la_full_notm}} web UI. You can also export sets of logs to analyze them in a different context.
{: shortdesc}

To view logs, you must [launch the web UI](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-launch) in the location where logs are available. Then, you can work with views to monitor those logs. You view logs in your local time.

You can select the logs that are displayed through a view by applying a timestamp, a search query, or both.

* You can apply a search query, and save it as a custom view.
* You can apply a timestamp to jump to a specific time in your event log.

When you apply a search query, you can save that view for reuse later. However, timestamps are not saved.

Notice that instances might have different service plans, and consequently different data retention periods that determine the number of days that you have data available for search though the web UI. You can only monitor logs within your retention period. Different [service plans](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-service_plan) have different retention periods.




## Monitoring logs through the default view
{: #mon_def_view}

The default view is named **Everything**.

As soon as you open the web UI in a location, this is the view that you see.

All logs in your instance are displayed through this view.

To learn how to view logs through this view, see [Monitoring events through the default view](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-view_events#view_events_step1).

## Monitoring logs through custom views
{: #mon_cus_view}

You might want to monitor a set of logs in your account. To anayze a subset of logs, you can create custom views.

You create a custom view by applying a search query that defines what logs to display through the view. [Learn more](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-view_events#view_events_step2).

You can also run any of the following tasks:

* [Attach an alert](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-alerts) to a custom view
* [Export data](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-export) from a custom view
* [Rename, and add or modify the description of a view](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-views#views_step5)
* [Apply a line template](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-views#views_step4) to a view to customize how the data is displayed
* Organize views by grouping them into **categories**


## Monitoring logs by applying a timeframe
{: #mon_time_view}

You might want to see logs within a specific timeframe.

You can select the logs that are displayed through a view by [applying a timeframe](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-view_events#view_events_step3).

You can apply a timestamp by specifying an absolute time, a relative time, or a time range.

* An abosute time specifies a precise point in time in your event log, such as `May 20 7:00pm`.

* A relative time specifies a timeframe that is not precise, such as `2 days ago`.

* A time range specified an interval of time, such as `yesterday 10am to yesterday 11am`.



## Configuring alerts
{: #mon_alerts}

There are scenarios where you might want to be notified if specific logs are generated in your account. For example, you might want to be notified if the number of actions that fail are greater than a threshold that you specify.

Through the {{site.data.keyword.la_full_notm}} web UI, you can apply search queries to define the logs that are displayed through a custom view. Then, you can attach an alert to that view to be notified when a condition occurs. A bell icon is displayed with the view to indicate that this view has an alert attached to it.

Consider the following information when you configure alerts:
* You can [attach one alert](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-alerts) per custom view.

* There are 2 types of alerts: presence alert and absence alert.

* You can configure conditions that are based on the number of event lines that meet the search query in the view, on a time frequency, or both.

* The time frequency that is specified as part of the condition defines the reset time of an alert after it is triggered.

* You can define multiple notification channels for an alert. For information about the supported channels, see [Alert notification channels](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-channels).

* You can [define **presets**](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-alerts#alerts_step3). A preset is an alert template that users can attach to any number of views. Service administrators define presets. Notice that when you delete a preset, any alerts that are defined by using this preset are automatically deleted.

* You can enable or disable the feature on alerts that allow a user to mute an alert for a period of time. This feature only applies to email notification channels.

* You can [detach an alert](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-alerts#alerts_delete_view) from a view.

* The timestamp that you see in a notification is set to UTC. For email notifications, you can set the **Timezone** to define a different timestamp value such as local time, for example.




### Presence alert
{: #mon_alerts_presence}

Configure a presence alert to notify when the number of logs that show in a view is more than what you expect.

For example, you might have a view that shows logs that report the deletion of service instances in your account. You are not expecting the deletion of service instances. You can configure a **presence alert** that triggers an alert when 1 or more logs show in the view.


### Absence alert
{: #mon_alerts_absences}

Configure an absence alert to notify when the number of logs that show in a view is less than what you expect, or none.

Consider the following information when you configure an absence alert:
- An absence alert is enabled when the view receives at least 1 log line.
- An absence alert is triggered when the view that has an absence alert attached to it is active. A view is active when the view receives logs within the last 24 hours.

For example, you might have a view that does not get any logs for 2 days. Therefore, this view is not active. You have an absence alert attached to this view that is configured to send a notification after 30 minutes. Because the view is not active, the absence alert is muted and you do not get notifications. To make the view active and get notifications for the absence condition, logs need to start flowing into the view.


### Alert conditions
{: #mon_alerts_conditions}

You can configure any of the following conditions for an alert:

* **Time frequency**: You set this condition to specify how often to trigger an alert. Valid values are: 30 seconds, 1 minute, 5 minutes, 15 minutes, 30 minutes, 1 hour, 6 hours, 12 hours, 24 hours
* **Event lines counter**: You set this condition to specify the number of event lines that match the view's filtering and search criteria. When the number of event lines is reached, an alert is triggered.

You can decide whether both conditions are checked or only one. If both conditions are set, an alert is triggered when any of the thresholds is reached.

If you set the *Event lines counter* to be the only condition that triggers an alert, notice that the time frequency that is set when you configure the condition determines the time that it takes for the alert condition to be reset after the alert is triggered.
{: note}

For example, you can configure an alert that is triggered after 30 seconds, or when a 100 event lines that match the view's filtering and search criteria are collected.


### Mute alert notifications
{: #mon_alerts_mute}

By default, the feature that controls the ability of a user to mute notifications is enabled when you configure an alert on a custom view. The **Muteable** feature applies to email notifications only.

When the **mutable** feature is enabled on an alert, a user can pause notifications for a period of time. A user can choose to mute an alert for a period of 1 hour, 6 hours, 12 hours, or 1 day.






## Exporting logs
{: #mon_export}

You might need access to a set of logs outside the web UI to investigate an issue in more detail.

You can export data in JSONL format from an {{site.data.keyword.la_full_notm}} instance into a local file.

You can export logs through a view in the web UI, or programmatically by using a REST API.

Consider the following information when you export logs:
* You export a set of event entries.
* To define the set of data that you want to export, you can apply filter and searches. You can also specify the time range.
* The maximum number of lines that you can export is 20,000.



### By using the REST API
{: #mon_export_api}

You can export logs programmatically by using the logging REST API. [Learn more](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-export_api).

When you export logs programmatically, consider the following information:

* You can choose to send an email or to stream logs in to your terminal.
* You must use a service key that is used to pass the credentials that must be used when you make an export REST API call.

    You must have **manager** role for the {{site.data.keyword.la_full_notm}} instance or service to view and generate service keys in the web UI.


### Through a view in the web UI
{: #mon_export_ui}

You can export logs through a view in the web UI.

In the web UI, you can select a view that displays the data that you want to export. For this view, you must choose the task to **Export Lines**. You must specify a time range, and whether to export newer lines or older lines. Then, you can request the export.

After you submit a request, you get an email that is sent to your email address, with a link to a compressed file that includes the data.
* To get the data, you must click the link and download the compressed file.
* The compressed file that contains the data that you want to export is available for a maximum of 48 hours.

[Learn more about exporting logs through the web UI](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-export).
