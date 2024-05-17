---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords: IBM Cloud, Log Analysis, Kubernetes logs

subcollection: log-analysis

content-type: tutorial
services: log-analysis
account-plan: lite
completion-time: 1h



---

{{site.data.keyword.attribute-definition-list}}


# Use the {{site.data.keyword.la_short}} web UI
{: #tutorial-use-logdna}
{: toc-content-type="tutorial"}
{: toc-services-"log-analysis"}
{: toc-completion-time="1h"}


In this tutorial, you learn how to use the {{site.data.keyword.la_full}} web UI to create parsing rules that you can use to enhance your searches, views for monitoring Kubernetes log data, alerts to be notified of anomalous situations, and dashboards and screens to monitor your data.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

You can use {{site.data.keyword.la_full_notm}} to add log management capabilities to your {{site.data.keyword.cloud_notm}} architecture. {{site.data.keyword.la_full_notm}} offers administrators, DevOps teams, and developers advanced features to filter, search, and tail log data, define alerts, and design custom views to monitor
application and system logs.


## Before you begin
{: #LA-use-logdna-prereqs}

- Make sure you have a logging instance that is collecting logs.

    - You can have a logging agent configured to collect logs from a VPC instance. See [Logging in Linux VPC server instances](/docs/log-analysis?topic=log-analysis-ubuntu).

    - You can have a logging agent configured to collect logs from a Kubernetes cluster. See [Logging in Kubernetes clusters (cluster-level logging)](/docs/log-analysis?topic=log-analysis-kube).

- Check you have permissions to launch the logging web UI. See [Granting IAM policies to a user to launch the web UI](/docs/log-analysis?topic=log-analysis-launch#launch_iam).


## Launch the {{site.data.keyword.la_full_notm}} web UI
{: #LA-launch-ui}
{: step}

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](../../icons/icon_hamburger.svg) &gt; **Observability**.

4. Click **Logging**.

5. For your instance, click **Open dashboard**. The logging web UI will be displayed.


## Create a custom view
{: #LA-create-custom-view}
{: step}

In {{site.data.keyword.la_full_notm}}, you can configure custom views to monitor a subset of data. For example, you configure your cluster to forward specific logs to the logging instance and you can filter those logs for analysis.

This tutorial will show you how to create a view that shows only a specific log.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **EVERYTHING** view.

   ![EVERYTHING view](../images/everything.png "EVERYTHING view")

3. Click **Apps** and select the log you want to view.

4. Click **Apply**.

   The view changes to only show your selected logs and the tab changes to **Unsaved View**.

   ![Unsaved view](../images/unsaved.png "Heading showing changed to Unsaved View")

5. Click **Unsaved View** > **Save as new view**.

6. Enter a **Name** for your view.  Optionally, you can select a **Category** and **Alert** value.  Click **Save View**.

   Your view is listed under your selected category.  If you didn't select a category, it will be listed under **UNCATEGORIZED**.

## Customize the log format
{: #LA-customize-log-format}
{: step}

When you launch the {{site.data.keyword.la_full_notm}} web UI, log entries are displayed in a predefined format. You can modify how the log entries are displayed.

These configuration changes will affect all defined views.
{: note}

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Settings** icon ![Settings icon](../images/config.png "Settings icon").

3. Click **USER PREFERENCES**.

4. Click **Log Format**.

5. Modify the log format as desired.

   Change the log viewer text size by using the slider.

   To add items to the log view, drag the available items and add them in your desired order to the view.

6. Click **Done** to save your changes.  To cancel without making changes, press **Esc**.


## Customize the data displayed for a view
{: #LA-customize-data-display}
{: step}

You can customize the fields that are displayed in a custom view.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. [Make sure you have a custom view defined](#LA-create-custom-view).

3. Select the view to change in the navigation.  Your view will be listed under the category where it was created, or under **UNCATEGORIZED** if you didn't specify a category when the view was created. For example, the following shows a view named "My View" that was created without an assigned category.

   ![Navigation example](../images/uncategorized_myview.png "An uncategorized view named My View in the navigation")

4. Click the selected view name.  The following example shows the view named "My View".

   ![My View view](../images/myview.png "Heading showing the My View view")

5. Click the view name.  The menu is displayed.  Click **Edit view properties**.

   ![Edit view properties](../images/editviewproperties.png "Edit view properties")

6. In the **Custom Template** you can change how you want the log line formatted for the view by including static text and fields from the log.

   * To determine the possible fields, click the down arrow on a log line in the view.

      ![Open log entry](../images/loglinedropdown.png "Open log entry twistie")

   * Click **Extract Fields** ![Extract Fields](../images/extractfields.png "Extract Fields")

      The log fields that can be used are displayed in the **Reference line** along with the specific values from the selected log entry.  For example:

      ```text
      {"logSourceCRN":"crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy::","saveServiceCopy":true,"message":"Cluster yyyyy health status set to All Workers Normal"}
      ```
      {: codeblock}

      In this case, the following fields can be used in the **Custom Template**: `logSourceCRN` and `message`.

      The `saveServiceCopy` field value cannot be used because it is a boolean value.  Boolean field values will not display in a **Custom Template**.
      {: important}

   * In the **Custom Template**, specify the fields and static text in the way you want them displayed. Fields need to be enclosed in double braces `{{field}}` or in BASH format `${field}`.  All other specified characters will be rendered as plain text.

      For example, if you have log entries similar to the following:

      ```text
      Nov 16 13:59:02 containers-kubernetes crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy:: Cluster yyyyy health status set to All Workers Normal
      ```
      {: codeblock}

      And you want them formatted like this:

      ```text
      SOURCE: Nov 16 13:59:02 containers-kubernetes crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy::
      MESSAGE: Cluster yyyyy health status set to All Workers Normal
      ```
      {: codeblock}

      And the extracted reference line is:

      ```text
      {"logSourceCRN":"crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy::","saveServiceCopy":true,"message":"Cluster yyyy health status set to All Workers Normal"}
      ```
      {: codeblock}

      Then your **Custom Template** would be:

      ```text
      SOURCE: {{logSourceCRN}}
      MESSAGE: {{message}}
      ```
      {: codeblock}

      The original log line will be displayed followed by the custom formatting.


## Create a parsing rule
{: #LA-create-parsing rule}
{: step}

There are occasions when you might want to reference information that is available in log records. Parsing rules maps information from a log line to a field that can be used in other configuration settings.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Settings** icon ![Settings icon](../images/config.png "Settings icon").

3. Click **PARSING**.

4. Click **Create Template**. The template wizard opens.

5. For this tutorial, for **Choose a sample log line to begin building your template** select *Find an existing log line*. Enter a search term that will match a field in your log. See [Customize the data displayed for a view](#LA-customize-log-format) for information on extracting log fields.

6. Scroll to the end of the page and click **Build Parsing Template**. A **Reference Line** for your log records is displayed.

7. Click the the **Pencil** icon ![Pencil icon](../images/pencil.png "Pencil icon") and enter a name for your parsing rule.

   If you name a template before you click **Build Parsing Template**, the name is not changed.
   {: note}

8. Choose the **Extract values by delimiter** extractor.

9. For **Delimiter** specify a `,` (comma). A preview of the output delimited by a comma is presented for your review.

10. Choose one of the entries.  For example, if your log contains a field called `message` you might select that line.

11.  For **Choose an Operator** select **Extract Values by Delimiter**.

12. For **Delimiter** specify a delimiter that makes sense for your selected entry. For example, a reasonable delimiter might be a `:` (colon).  A preview of the delimited output is presented for your review.

13. Select an entry containing a date value.

14. For **Choose an Operator** select **Trim Value**. Using the index range specify a starting and ending character position so only the date is retained in the displayed output.

15. For **Choose an Operator** select **Capture in Field** to set the name of the field that will capture this information.

16. For **Field Name** specify a name that you will use to reference this type of information.

17. At the end of the page click **Proceed to Validation**.

18. For **Set a query and verify parsed output with different sample lines** enter a search that will return multiple records.  For example, `message`.

19. If all log lines returned match the rule you specified, click **Mark as Valid** for each and then click **Activate** at the end of the page.

    Until you validate all results, the **Activate** option will be disabled.
    {: note}

The rule will take affect in approximately 15 minutes.


## Analyze the log line
{: #LA-analyze-log}
{: step}

You might want to view a log line in context.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Views** icon ![Views icon](../images/views.png "Views icon").

3. Select a log view. You might want to use the [custom view you created](#LA-create-custom-view).

4. Identify a log line you want to explore.

5. Open the log entry by clicking the down arrow. Information about line identifiers, tags, and labels is displayed.

   ![Log entry dropdown](../images/loglinedropdown.png "Log entry dropdown").

6. Click ![**View in context**](../images/viewincontext.png "View in context"). The log line is displayed in context of other log lines from that host, app, or both. This information is helpful when troubleshooting a problem.

7. Explore the selected log line by using the following options.

   **By Everything** displays the log line in context of all log records that are available in the {{site.data.keyword.la_full_notm}} instance.

   **By source** displays the log line in context of the log lines for the same source.

   **By App** displays the log line in context of the log lines of the app.

   **By Source & App** displays the log line in the combined context of the app and source.

8. Click **Continue in New Viewer** to open the view as a new **Unsaved View**. Keeping multiple views can help troubleshoot problems.

## Filtering to a specific timeframe
{: #LA-timeframe}
{: step}

You can search for events occurring in a specified timeframe.

The timeframe can be an absolute time, relative time, or a time range.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Views icon** ![Views icon](../images/views.png "Views icon").

3. Select a log view.  You might want to use the [custom view you created](#LA-create-custom-view).

4. In the **Jump to timeframe** field ![Jump to timeframe field](../images/jumptotimeframe.png "Jump to timeframe field") enter a timeframe to filter the log.

   1. Specify a specific date or date time. For example, `Nov 16` will jump to log entries starting with that date. You can also specify a date and time.  For example, `Nov 16 22:29`.

   2. Specify a value relative to the current time. For example, `1 day ago` or `5 hours ago`.

   3. Specify a date, or date and time range. For example, `Nov 14 to Nov 15` or `Nov 14 12:00 to Nov 14 23:59`. Ranges can also be relative to the current time.  For example, `Yesterday 10am to Yesterday 11am`.

If you get a “Your request is taking longer than expected, try refreshing your browser in a bit as we try to catch up” error message, the timeframe you specified might not have any available data. Change your timeframe and retry.
{: tip}

## Create dashboard
{: #LA-dashboard}
{: step}

A dashboard provides interactive graphs that help you monitor your app. For example, graphs can help you analyze patterns and trends over a period of time.

The following will help you create a dashboard.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Boards** icon ![Boards icon](../images/boards.png "Boards icon").

3. Click **NEW BOARD**.

4. Click **Add Graph**.

5. Select *app* For **Field**.

6. Select *ANY* for **Field Value**.

7. Click **Add Graph**.  A trend line showing the count of app log events is listed.

8. Click the graph line and click **Show logs** to see the log at point in time.

9. Open the subplot view ![Open the subplot view](../images/opensubplot.png) and select *Histogram* for **Choose breakdown type** and *host* for **SYSTEM FIELD**.

10. Click **Add Breakdown**.  A histogram of the data by *host* is added to the dashboard.

11. Click **Add** and add an additional histogram and specify *verb* for **SYSTEM FIELD**.

12. Try adding additional plots by clicking **Add Plot**.

13. Multiple plot lines can be hidden or displayed on the graph. Select your plot and click **Show** to show the line or **Hide** to hide it.

14. Click the **Filter** icon ![Filter icon](../images/filter.png "Filter icon") to filter the graph by a specific field's data. For example, `host:myhost`.

15. Click the **Pencil** icon ![Pencil icon](../images/pencil.png "Pencil icon") and enter a name for your dashboard. Specify a **Category** if desired and click **Save**.

   If you don't specify a **Category** your dashboard will be listed under **UNCATEGORIZED**. If you are editing an existing dashboard, changes will be saved when exiting the dashboard without having to click **Save**.
   {: note}

## Create a widget in a screen
{: #LA_create_widget}
{: step}

Using the screen option you can create a screen of widgets that you can use to monitor your app using metrics (counters), operational KPIs (gauges), tables, and graphs that can be used to analyze patterns and trends.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Screens** icon ![Screens icon](../images/screens.png "Screens icon").

3. Click **NEW SCREEN**.

4. To save the screen, click **Save Screen**. Enter the following and then click **Save**.

   **Name**: The name you want to give to your screen.

   **Category**: Select an existing category or enter a new category name. If adding a new category, click **Add this as a new screen category** to add the category to the list.

5. Click **Add Widget** and select **Count**. A widget is added to your screen.

6. Click the widget. The configuration for the widget is displayed.

7. Change the **Field** and **Field Value** to change what is counted. For example, you might change **Field** to *host* and **Field Value** to a host in your account.  The widget will now count the log messages in the past day. You can also change the **Duration** of time counted.

8. Change the **Label** of the widget to something meaningful to you.

9. Click **Save Screen** > **Save** to save your changes.

10. Add a table widget by clicking **Add Widget** > **Table**.

11. Click the table widget. The configuration for the widget is displayed.

12. Change the **Field** and **Field Value** to change what is displayed in the table. In **Group By**, specify the field used to group the data . For example, you might change **Field** to *host* and **Field Value** to a host in your account. You then might want to group that data by *app*. The widget will display a table of the counts for the host grouped by app during the past day. You can also change the **Duration** of time counted and specify a **Label** for your widget.

    If you need a table with more rows, change the **Data Format** **Number of Rows** to your preferred value.

13. You can resize any of the widgets by clicking the widget and clicking and dragging one of the anchors. Widgets can be moved by clicking the widget and dragging it to your desired location on the screen.

14. Click **Save Screen** > **Save** to save your changes.

   If you do not save your screen, you will lose all your changes.
   {: important}

## Add alert to custom view
{: #LA-add-alert}
{: step}

You can configure an alert to be sent by email, Slack, PagerDuty or as a Webhook when specific criteria is met.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. [Make sure you have a custom view defined.](#LA-create-custom-view).

3. Select the view to change in the navigation. Your view will be listed under the category where it was created, or under **UNCATEGORIZED** if you didn't specify a category when the view was created. For example, the following shows a view named "My View" that was created without an assigned category.

   ![Navigation example](../images/uncategorized_myview.png "An uncategorized view named My View in the navigation")

4. Click the selected view name.  The following example shows the view named "My View".

   ![My View view](../images/myview.png "Heading showing the My View view")

5. Click the view name.  The menu is displayed.  Click **Attach an alert**

   ![Edit view properties](../images/editviewproperties.png "Edit view properties")

6. Click **View-specific alert**.

7. Click **Email**.

8. Configure the alert.

   ![Configure alert](../images/configalert.png "Dialog showing alert configuration")

   1. Specify when the alert will be triggered, and an email sent. For this example specify *When 5 or more matches appear within 30 seconds*.

   2. Select the email addresses of the **Recipients** who should receive the alert.

   3. Click **Save Alert**.

9. Check the configured email for an alert.

10. When you are ready to disable the alert, click the view name and in the menu click **Detach alerts**.

   ![Detach alerts](../images/detachalerts.png "Dialog showing the option to detach associated alerts")

## Next steps
{: #LA-use-step-next}

Want to start fresh? Remove the following resources that you created as a part of this tutorial:

* Delete any views you will not need.
* Delete any dashboards and screens you will not need.
* Delete any parsing rules you will not need.
* Detach any alerts you will not need.
