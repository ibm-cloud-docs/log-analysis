---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, alerts

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Creating alerts through the UI
{: #create_alert_ui}

You can create alerts graphically through the UI.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

Complete the following steps to create an alert:


## Prereqs
{: #create_alert_ui_prereqs}

You must grant permissions to users in your account to be able to launch the web UI and create alerts.

You must be an administrator of the {{site.data.keyword.la_full_notm}} service, an administrator of the {{site.data.keyword.la_full_notm}} instance, or have account IAM permissions to grant other users policies.
{: note}

The following table lists the minimum policies that a user must have to be able to launch the {{site.data.keyword.la_full_notm}} Web UI, and view logs:

| Service                               | Role                      | Permission granted            |
|---------------------------------------|---------------------------|-------------------------------|
| `{{site.data.keyword.la_full_notm}}` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `{{site.data.keyword.la_full_notm}}` | Service role: Manager or Standard-member      | Allows the user to launch the Web UI and create alerts.  |
{: caption="Table 1. IAM policies" caption-side="top"}

For more information on how to configure these policies for a user, see [Granting permissions to a user to view logs](/docs/log-analysis?topic=log-analysis-work_iam#user_logdna).


## Step 1. Define the rule
{: #create_alert_ui_step1}

You must define the rule that specifies the scope of the data and save the rule as a view.

Complete the following steps to create a rule:

1. [Launch the {{site.data.keyword.la_full_notm}} UI](/docs/log-analysis?topic=log-analysis-launch).
2. Filter log data by using pre-defined filters.

    You can filter logs by log source, application, and log level.

    * A source can be a host, a computer, a virtual machine, or a Heroku app.

    * An application represents a log file, a program, or a container.

    * Examples of log levels are: INFO, DEBUG, ERROR

    Complete the following steps to filter logs:

    1. Click the **Views** icon ![Views icon](../images/views.png "Views icon").

    2. Select **EVERYTHING** or a view.

    3. Expand **Tags** to see the list of tags that are identified in the logs. Then, choose the ones that you want.

    4. Expand **Sources** to see the list of log sources that are identified in the logs. Then, choose the ones that you want.

    5. Expand **Apps** to see the list of apps that are identified in the logs. Then, choose the ones that you want.

    6. Expand **Levels** to see the list of log levels that are identified in the logs. Then, choose the ones that you want.

    In each section, you can group multiple options into a group. Group tags, log sources, apps, and log levels to reuse these groupings when you filter log data in other custom views. To create a group, select multiple values. Then, click **Save as group**. Enter a name for the group, and save it.

3. Filter log data by adding a search query.

    When you search log data, the search applies any log filters and time queries configured in that view.

    You can do simple searches (single term string search), compound search (multiple search terms and operators), field searches if the log line can be parsed, and others. For more information, see [How to Search Logs](https://docs.logdna.com/docs/search){: external}.

    AND and OR operators are case-sensitive and must be capitalized.

4. Create a view.

    1. Click the **Views** icon ![Views icon](../images/views.png "Views icon").

    2. Select **EVERYTHING** or a view.

    3. Filter log data then click **Save as new view**. The *Create new view* page opens.

    4. Enter a name for the view in the *Name* field.

    5. Optionally, add a category. Enter a name and then click **Add this as new view category**.

    6. Click **Save View**


## Step 2. Create the alert
{: #create_alert_ui_step2}

Next, you must attach an alert to the view.

You can choose any of the following options:
- Create a preset and attach the preset to the view
- Create a specific alert on the view.

You can attach multiple notification channels to a view. You can define different triggering conditions to each notification channel.

### Create an alert by using a preset
{: #config_alert_preset}

Complete the following steps to attach a preset to a view:

1. [Configure a preset (alert template)](/docs/log-analysis?topic=log-analysis-preset_ui#preset_ui_create).

2. Click the **Views** icon ![Views icon](../images/views.png "Views icon"). Select the view name. Then, select **Attach an alert**.

3. In the section **Choose preset**, select a preset.

4. Click **Save alert**.




###  Create an alert on a view
{: #alerts_create_alert}

Complete the following steps to attach an alert to a view:

1. In the web UI, click the **Views** icon ![Views icon](images/views.png "Views icon").
2. Click the view name. Then, select **Attach an alert**.
3. Select **View-specific alert**.
4. Select the type of alert (Slack, Email, Webhook, or PagerDuty).  If you selected the wrong alert type and you want to change it, click **Delete Alert Channel**.
5. Configure when you want the alert to be sent.

   Select if you want the alert to be sent when the condition exists (**Presence**) or does not exist (**Absence**).

   Indicate the logging criteria when an alert should be sent.  For example, when 100 lines matching in the view are logged in an hour.  A graph will help you determine the number of log lines matching your specified criteria.

   Select if the alert should be sent at the end of the selected period or immediately when the number of lines are logged.

   Optionally you can specify a **Custom schedule** with alerting limited to a specified timezone, days of the week, or timeframe. To configure a **Custom schedule**:

    1. Select **on** for **Custom schedule**.

    2. Select the Timezone for the log entries.

    3. Select the days of the week when alerts should be generated.

    4. Optionally specify a time range for the selected days. A graph will help you determine the number of log entries for the timezone and time range.

6. Depending on the type of alert you will also need to configure additional settings:

    **Slack**:  Specify your **Webhook** URL and the desired **Message color**.

    **Email**: Specify the **Recipients** of the email and a **Timezone**. The timezone defines the timestamp value of each event that is included in the email. To see UTC timestamps, you can select **(GMT +00:00) UTC**.

    **PagerDuty**: Specify the **Service**.  If required, you will be prompted to connect to PagerDuty.

    **Webhook**: Specify the **Method & URL**, and the **Headers** and **Body** of the `JSON` used to interact with your webhook.  You can use **Validate JSON** to make sure your `JSON` is correct before creating the alert.

7. You can click **Test** to test that your alert configuration is correct.

    ![Test option](images/alert_test.png "Example dialog showing Test option")

8. Click **Save Alert**.

9. If you want to create an additional alert channel, click **+** and follow the prior steps to create additional channels.  You can create different channel types, for example, an email and a Slack channel.  Or, you can create multiple channels of the same type with different alert criteria.

Alerts will be generated based on your configuration.
