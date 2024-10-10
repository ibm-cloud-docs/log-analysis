---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, logs

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Viewing logs
{: #view_logs}

After you provision an instance of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}}, and configure a logging agent for a log source, you can view, monitor, and manage log data through the {{site.data.keyword.la_full_notm}} Web UI.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

When you launch the {{site.data.keyword.la_full_notm}} web UI, log entries are displayed with a predefined format. You can modify in the **User Preferences** section how the information in each log line is displayed. You can also filter logs and modify search settings, then bookmark the result as a *view*. You can attach and detach one or more alerts to a view. You can define a custom format for how your lines are shown in the view. You can expand a log line and see the data parsed.


Complete the following steps to view logs:


## Step 1. Grant IAM policies to a user to view logs
{: #view_logs_step1}

You must grant permissions to users in your account to be able to launch the web UI and view logs.

You must be an administrator of the {{site.data.keyword.la_full_notm}} service, an administrator of the {{site.data.keyword.la_full_notm}} instance, or have account IAM permissions to grant other users policies.
{: note}

The following table lists the minimum policies that a user must have to be able to launch the {{site.data.keyword.la_full_notm}} Web UI, and view logs:

| Service                               | Role                      | Permission granted            |
|---------------------------------------|---------------------------|-------------------------------|
| `{{site.data.keyword.la_full_notm}}` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `{{site.data.keyword.la_full_notm}}` | Service role: Reader      | Allows the user to launch the Web UI and view logs in the Web UI.  |
{: caption="IAM policies" caption-side="top"}

For more information on how to configure these policies for a user, see [Granting permissions to a user to view logs](/docs/log-analysis?topic=log-analysis-work_iam#user_logdna).


## Step 2. Navigate to the web UI through the {{site.data.keyword.cloud_notm}} UI
{: #view_logs_step2}

To launch the {{site.data.keyword.la_full_notm}}  UI through the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} *Dashboard* opens.

2. Click the **Menu** icon ![Menu icon](../../icons/icon_hamburger.svg) &gt; **Observability**.

3. Click **Logging**.

    The list of {{site.data.keyword.la_full_notm}} instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select one instance. Then, click **Open dashboard**.

The {{site.data.keyword.la_full_notm}} web UI opens and displays logs forwarded to that instance.


## Step 3. Customize your default view
{: #view_logs_step3}

In the **User preferrences** section, you can modify the order of the data fields that are displayed per line.

Complete the following steps to modify the format of a log line:

1. Click the **User preferences** icon.
2. Select **User preferences**. A new window opens.
3. Select **Log Format**.
4. Modify the *Line Format* section to match your requirements. Drag boxes.


## Step 4. Look into a log line
{: #view_logs_step4}

At any time, you can view each log line in context.

Complete the following steps:

1. Click the **Views** icon ![Views icon](../images/views.png "Views icon").
2. Select **EVERYTHING** or a view.
3. Identify a line in the log that you want to explore.
4. Expand the log line.

    Information about line identifiers, tags, and labels is displayed.

5. Click **View in Context** to see the log line in context of other log lines from that host, app, or both.

6. Click **Copy to clipboard** to copy the message field to the clipboard.

When you are finished, close the line.


## Step 5. Filter logs
{: #view_logs_step5}

You can filter logs by log source, application, and log level.

* A source can be a host, a computer, a virtual machine, or a Heroku app.
* An application represents a log file, a program, or a container.
* Examples of log levels are: INFO, DEBUG, ERROR.

Complete the following steps to filter logs:

1. Click the **Views** icon ![Views icon](../images/views.png "Views icon").
2. Select **EVERYTHING** or a view.
3. Expand **Tags** to see the list of tags that are identified in the logs. Then, choose the ones that you want.
4. Expand **Sources** to see the list of log sources that are identified in the logs. Then, choose the ones that you want.
5. Expand **Apps** to see the list of apps that are identified in the logs. Then, choose the ones that you want.
6. Expand **Levels** to see the list of log levels that are identified in the logs. Then, choose the ones that you want.

In each section, you can group multiple options into a group. Group tags, log sources, apps, and log levels to reuse these groupings when you filter log data in other custom views.
{: note}

To create a group, select multiple values. Then, click **Save as group**. Enter a name for the group, and save it.


## Step 6. Search logs
{: #view_logs_step6}

When you search log data, the search applies any log filters and time queries configured in that view.

You can do simple searches (single term string search), compound search (multiple search terms and operators), field searches if the log line can be parsed, and others. For more information, see [How to Search Logs](https://docs.logdna.com/docs/search){: external}.

**Note:** AND and OR operators are case-sensitive and must be capitalized.



## Step 7. Create views
{: #view_logs_step7}


Complete the following steps to create a view:

1. Click the **Views** icon ![Views icon](../images/views.png "Views icon").
2. Select **EVERYTHING** or a view.
3. Filter log data then click **Save as new view**.

    The *Create new view* page opens.

4. Enter a name for the view in the *Name* field.

5. Optionally, add a category. Enter a name and then click **Add this as new view category**.

6. Optionally, attach an alert. A new section is displayed for you to configure the alert.

7. Click **Save View**


## Step 8. Customize how event lines are displayed through a view
{: #views_step8}

There are different options to customize how you see data in a view:
* You can modify the properties of a view.
* You can rename a view, add or modify its description, and apply a specific line format.
* You can change the `log format` in the *User preferences* section.
* You can apply a line template from the *Tools* section. Notice that this overrides any other line configuration. If you select **Persist these settings**, all views in the UI will show data per the line format that is specified in this section.
* You can apply color to terms or strings by setting **Highlight Terms** in the **Tools** section.



### Change the line format through the view properties page
{: #views_step8_1}

Complete the following steps to modify the format of an event line in a single view:

1. In your view, select **Edit View Properties**. The *Edit View Properties* page opens.

2. Enter a custom line format in the **Custom %LINE Template** section. The default is set to `{{line}}`.

    For more information about the line template guidelines, see [Guidelines](#views_line).

3. Click **Save properties**.



### Change the line format through the user preferences section
{: #views_step8_2}

In the **User preferences** section, you can modify the order of the data fields that are displayed per line.

Complete the following steps to modify the format of an event line:

1. In the web UI, click the **Configuration** icon ![Configuration icon](../images/admin.png "Admin icon").
2. Select **User preferences**. A new window opens.
3. Select **Log Format**.
4. Modify the *Line Format* section to match your requirements by dragging the boxes to the desired location.


### Change the line format through the line template in the tools section
{: #views_step8_3}

Complete the following steps to modify the format of an event line:

1. In the view, click the **Tools** icon ![Tools icon](../images/tool.png "Tools icon").
2. In the **Line Template** field, enter your custom line format. For more information about the line template guidelines, see [Guidelines](#views_line).
3. Optionally, click **Persist these settings** to apply the line format to all views.



### Highlight terms
{: #view_events_step8_4}

Complete the following steps to highlight terms in a view:

1. In the view, click the **Tools** icon ![Tools icon](../images/tool.png "Tools icon").
2. In the **Line Template** field, enter a word or string in the **Highlight Terms** section.
3. Optionally, click **Persist these settings** to apply these setting to all views.





## Guidelines defining line templates
{: #views_line}

Consider the following guidelines that you must apply when you define a line template:
* Use mustache style `{{field.name}}` or bash style `${field.name}` variables to construct your template.
* Use `{{line}}` or `$@` to reference the original line.
* All other characters or strings are interpreted as a text literal.


For example, you can define a line template as `{{initiator.id}} -- {{action}} -- {{message}}` to see these fields for each event in a view.


## Change the name and description of a custom view
{: #views_step5}

You can rename a view. You can add or modify the description of a view.


Complete the following steps:

1. In your view, select **Edit View Properties**. The *Edit View Properties* page opens.

    You can rename the view, add or modify the description of the view, and apply a custom line format.

2. Enter a new name in the **Rename View** section to rename the view.

3. Enter or modify the description in the **Description** section.

4. Click **Save properties**.
