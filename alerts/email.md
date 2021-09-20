---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, alerts

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

 
# Integrating with email
{: #email}

You can send alerts to 1 or more email addresses.
{: shortdesc}


## Configuring email
{: #email-config}

When you [configure an alert](/docs/log-analysis?topic=log-analysis-alerts) you can have that alert sent to 1 or more email addresses.

1. When configuring your alert, click ![email icon](images/email.png "email icon").

2. Select if you want the alert to be sent when the condition exists (**Presence**) or does not exist (**Absence**).

3. Indicate the logging criteria when an alert should be sent.  For example, when 100 lines matching in the view are logged in an hour.  A graph will help you determine the number of log lines matching your specified criteria.

4. Select if the alert should be sent at the end of the selected period or immediately when the number of lines are logged.

5. Optionally you can specify a **Custom schedule** with alerting limited to a specified timezone, days of the week, or timeframe. To configure a **Custom schedule**:

    1. Select **on** for **Custom schedule**.
    2. Select the Timezone for the log entries. 
    3. Select the days of the week when alerts should be generated.
    4. Optionally specify a time range for the selected days. A graph will help you determine the number of log entries for the timezone and time range.

6. Specify 1 or more email addresses.

7. Optional: You can click **Test** to test that your alert configuration is correct.

8. Click **Save Alert**.


## Muting an alert
{: #email_mute}

This section only applies to email alerts.
{: note}

After you configure an alert on a view and receive a notification email, complete the following steps to mute the alert a period of time:

1. Go to the email account where you receive email notifications.

2. Open a notification email for a view that you want to mute. 

    Look for emails that are sent by {{site.data.keyword.at_full_notm}}. The subject includes the name of the view.

    In the email, there is a section that includes the following text: 

    ```
     Mute these alerts for   [1 Hour] [6 Hours] [12 Hours] [1 Day]
    ```
    {: screen}

3. Choose a period of time.

    A window opens. The information provided indicates the view, the notification that is muted, and the time period that is muted for.

    For example, you can get a message that indicates the following:

    ```
    Email alerting for MyView has been muted for an hour.

    Unmute

    Alerting is scheduled to resume at Jun 14, 11:59am.

    Manage Alerts
    ```
    {: screen}

    From this page, you can select **Unmute** to enable notifications on the view. You can also select **Manage** to go to the **ALERTS** dashboard in the web UI.


## Unmuting a muted alert
{: #email_unmute}

You can manage alerts through the **ALERTS** dashboard.

1. In the web UI, select the **Settings** icon ![Settings icon](images/admin.png "Admin icon").

2. Select **ALERTS**.

    You can see the list of alerts that are muted. Each entry informs about the view where notifications are muted, the user who requested the action, and the UTC time when notifications will be enabled. 

2. Select an alert that you want to unmute.

3. Click **Unmute**.


