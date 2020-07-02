---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-02"

keywords: LogDNA, IBM, Log Analysis, logging, logs

subcollection: Log-Analysis-with-LogDNA

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
{:external: target="_blank" .external}

# Viewing logs
{: #view_logs}

After you provision an instance of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}}, and configure a LogDNA agent for a log source, you can view, monitor, and manage log data through the {{site.data.keyword.la_full_notm}} Web UI.
{:shortdesc}

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
| `{{site.data.keyword.la_full_notm}} ` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `{{site.data.keyword.la_full_notm}} ` | Service role: Reader      | Allows the user to launch the Web UI and view logs in the Web UI.  |
{: caption="Table 1. IAM policies" caption-side="top"} 

For more information on how to configure these policies for a user, see [Granting permissions to a user to view logs in LogDNA](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#user_logdna).


## Step 2. Navigate to the web UI through the {{site.data.keyword.cloud_notm}} UI
{: #view_logs_step2}

To launch the {{site.data.keyword.la_full_notm}}  UI through the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} *Dashboard* opens.

2. Click the **Menu** icon ![Menu icon](images/icon_hamburger.svg) &gt; **Observability**. 

3. Select **Logging**. 

    The list of {{site.data.keyword.la_full_notm}} instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select one instance. Then, click **View LogDNA**.

The {{site.data.keyword.la_full_notm}} web UI opens and displays logs forwarded to that instance.


## Step 3. Customize your default view
{: #view_logs_step3}

In the **USER PREFERENCES** section, you can modify the order of the data fields that are displayed per line.

Complete the following steps to modify the format of a log line:

1. Select the **Configuration** icon ![Configuration icon](images/admin.png "Admin icon").
2. Select **USER PREFERENCES**. A new window opens.
3. Select **Log Format**.
4. Modify the *Line Format* section to match your requirements. Drag boxes.


## Step 4. Look into a log line
{: #view_logs_step4}

At any time, you can view each log line in context.

Complete the following steps: 

1. Click the **Views** icon ![Configuration icon](images/views.png "Configuration icon").
2. Select **Everything** or a view.
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
* Examples of log levels are: INFO, DEBUG, ERROR

Complete the following steps to filter logs:

1. Click the **Views** icon ![Configuration icon](images/views.png "Configuration icon").
2. Select **Everything** or a view.
3. Expand **All Tags** to see the list of tags that are identified in the logs. Then, choose the ones that you want.
4. Expand **All Sources** to see the list of log sources that are identified in the logs. Then, choose the ones that you want.
5. Expand **All Apps** to see the list of apps that are identified in the logs. Then, choose the ones that you want.
6. Expand **All Levels** to see the list of log levels that are identified in the logs. Then, choose the ones that you want.


**Note:** In each section, you can group multiple options into a group. Group tags, log sources, apps, and log levels to reuse these groupings when you filter log data in other custom views.

To create a group, select multiple values. Then, click **Save as group**. Enter a name for the group, and save it.


## Step 6. Search logs
{: #view_logs_step6}

When you search log data, the search applies any log filters and time queries configured in that view.

You can do simple searches (single term string search), compound search (multiple search terms and operators), field searches if the log line can be parsed, and others. For more information, see [How to Search Logs in LogDNA docs](https://docs.logdna.com/docs/search){: external}.

**Note:** AND and OR operators are case-sensitive and must be capitalized.



## Step 7. Create views
{: #view_logs_step7}


Complete the following steps to create a view:

1. Click the **Views** icon ![Configuration icon](images/views.png "Configuration icon").
2. Select **Everything** or a view.
3. Filter log data then click **Save as new view / alert**.

    The *Create new view* page opens.

4. Enter a name for the view in the *Name* field.

5. Optionally, add a category. Enter a name and then click **Add this as new view category**.

6. Optionally, attach an alert. A new section is displayed for you to configure the alert.

7. Click **Save View**