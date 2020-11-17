---

copyright:
   years: 2020
lastupdated: "2020-11-16"

keywords: IBM Cloud, LogDNA, Activity Tracker, Kubernetes logs

subcollection: Activity-Tracker-with-LogDNA

content-type: tutorial
account-plan: lite <!-- Set `lite` if tutorial can be completed by using only Lite plan services; Set `paid` if the tutorial requires a pay-go or subscription versions of plans for the service --> 
completion-time: 10m <!-- Estimated time to complete the steps in this tutorial. Minute values are supported up to 90 minutes. Whole hours are also supported; for example: 2h -->

---

{:shortdesc: .shortdesc}
{:screen: .screen}  
{:codeblock: .codeblock}  
{:pre: .pre}
{:tip: .tip}
{:note: .note}
{:external: target="_blank" .external}
{:step: data-tutorial-type='step'} <!-- Apply to steps for automatic numbering -->

<!-- The title of your tutorial should be in active voice and and start with a verb. If you include product names, makes sure to use the non-trademarked short version conref. -->
<!-- Make sure each H1/H2/H3/etc. heading is _unique_ to your tutorial by adding a short but human-readable identifier. For example, instead of just "#overview", use "#cd-kube-overview" -->

# Use the LogDNA web UI
{: #tutorial-use-logdna}
{: toc-content-type="tutorial"} <!-- Always use this value -->
{: toc-services="containers, Registry"} <!-- Only if multi-service - use same values from services metadata above-->
{: toc-completion-time="10m"} <!-- Use same value from completion-time metadata above-->

<!-- The short description should be a single, concise paragraph that contains one or two sentences and no more than 50 words. Briefly mention what the user's learning goal is and include the following SEO keywords in the title short description: IBM Cloud, ServiceName, tutorial.--> 

In this tutorial, you learn how to use the {{site.data.keyword.la_full}} web UI to create rules and views for Kubernetes log data.  
{: shortdesc}

You can use {{site.data.keyword.la_full_notm}} to add log management capabilities to your {{site.data.keyword.cloud_notm}} architecture. {{site.data.keyword.la_full_notm}} offers administrators, DevOps teams, and developers advanced features to filter, search, and tail log data, define alerts, and design custom views to monitor
application and system logs.








<!-- It's recommended to include an architectural diagram that shows how the services that are used in this tutorial interact. SVG is the recommended format. If you include a diagram, include a brief text-based description of the workflow shown in the diagram, using active voice to describe the workflow. This makes the content more searchable and improves accessibility. -->

<!-- ![Architectural diagram](images/image.svg)
{: figure caption="Figure 1. A diagram that shows the architecture for my tutorial."}-->


## Before you begin
{: #LA-use-logdna-prereqs}

<!-- List any access, setup, or knowledge that the user must have before they start the tutorial. Be sure to link to any related documentation or resources to help the user complete these prerequisites.-->

<!-- Note: Currently no format for checkboxes. Let's check with design if required for first pass -->

* Make sure you have a Kubernetes instance with data you want to analyze.  For example, you can [create a VPC instance](https://cloud.ibm.com/docs/vpc?topic=vpc-getting-started).
* [Configure {{site.data.keyword.la_full_notm}} for your instance.](https://cloud.ibm.com/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-kube#kube)


<!-- For each step in your tutorial, add an H2 section. The title should be task-oriented and descriptive. If you find your tutorial going over 9 steps, consider whether your substeps can be grouped differently or whether your tutorial should be a multi-part series. -->

## Launch the {{site.data.keyword.la_full_notm}} web UI
{: #LA-launch-ui}
{: step}

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**. 

4. Select **Logging**.

5. For your instance, click **View LogDNA**.  The LogDNA web UI will be displayed.


## Create a custom view
{: #LA-create-custom-view}
{: step}

In {{site.data.keyword.la_full_notm}}, you can configure custom views to monitor a subset of data. For example, you configure your cluster to forward API audit logs to the logging instance, you can filter out
those logs for analysis.

This tutorial will show you how to create a view that shows only a specific log.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Select the **EVERYTHING** view.

   ![EVERYTHING view](/images/everything.png "EVERYTHING view")

3. Click **Apps** and select the log you want to view.

4. Click **Apply**.

   The view changes to only show your selected logs and the tab changes to **Unsaved View**.

   ![Unsaved view](/images/unsaved.png "Heading showing the dropdown changed to Unsaved View")

5. Click **Unsaved View** > **Save as new view / alert**.

6. Enter a **Name** for your view.  Optionally, you can select a **Category** and **Alert** value.  Click **Save View**.

   Your view is listed under your selected category.  If you didn't select a category, it will be listed under **UNCATEGORIZED**.

## Customize the log format
{: #LA-customize-log-format}
{: step}

When you launch the {{site.data.keyword.la_full_notm}} web UI, log entries are displayed in a predefined format. You can modify how the log entries are displayed.

Configuration changes will affect all defined views.
{: note}

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Settings** icon ![Settings icon](/images/config.png "Settings icon").

3. Click **USER PREFERENCES**.

4. Click **Log Format**.

5. Modify the log format as desired.  

   Change the log viewer text size by using the slider.

   To add items to log view, drag the available items from the bottom line to the top line.  To rearrange the order of the items, drag and drop the items in the top line until you have your desired view.

6. Click **Done** to save your changes.  To cancel without making changes, press **Esc**.


## Customize the data displayed for a view
{: #LA-customize-data-display}
{: step}

You can customize the fields that are displayed in a custom view.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. [Make sure you have a custom view defined.](#LA-create-custom-view).

3. Select the view to change in the navigation.  Your view will be listed under the category where it was created, or under **UNCATEGORIZED** if you didn't specify a category when the view was created. For example, the following shows a view named "My View" that was created without an assigned category.

   ![Navigation example](/images/uncategorized_myview.png "An uncategorized view named My View in the navigation") 

4. Click the selected view name at the top of the page.  The following example shows the view named "My View".

   ![My View view](/images/myview.png "Heading showing the dropdown showing the My View view") 

5. Click the view name at the top of the page.  The dropdown is displayed.  Click **Edit view properties**.

   ![Edit view properties](/images/editviewproperties.png "Edit view properties") 

6. In the **Custom Template** you can change how you want the log line formatted for the view by including static text and fields from the log.

   1. To determine the possible fields, click the down arrow on a log line in the view.

      ![Open log entry](/images/loglinedropdown.png "Open log entry twistie")

   2. Click **Extract Fields** ![Extract Fields](/images/extractfields.png "Extract Fields")

      The log fields that can be used are displayed in the **Reference line** along with the specific values from the selected log entry.  For example:

      ```
      {"logSourceCRN":"crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy::","saveServiceCopy":true,"message":"Cluster yyyyy health status set to All Workers Normal"}
      ```
      {: codeblock}

      In this case the following fields can be used in the **Custom Template**: `logSourceCRN` and `message`.

      The `saveServiceCopy` field value cannot be used because it is a boolean value.  Boolean field values will not display in a **Custom Template**.
      {: important}

   3. In **Custom Template** specify the fields and static text in the way you want them displayed.  Fields need to be enclosed in double braces `{{field}}` or in BASH format `${field}`.  All other specified characters will be rendered as plain text.

      For example, if you have log entries similar to the following:

      ```
      Nov 16 13:59:02 containers-kubernetes crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy:: Cluster yyyyy health status set to All Workers Normal
      ```
      {: codeblock}

      And you want them formatted like this:

      ```
      SOURCE: Nov 16 13:59:02 containers-kubernetes crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy:: 
      MESSAGE: Cluster yyyyy health status set to All Workers Normal
      ```
      {: codeblock}

      And the extracted reference line is:

      ```
      {"logSourceCRN":"crn:v1:bluemix:public:containers-kubernetes:us-south:a/xxxxx:yyyyy::","saveServiceCopy":true,"message":"Cluster yyyy health status set to All Workers Normal"}
      ```
      {: codeblock}

      Then your **Custom Template** would be:

      ```
      SOURCE: {{logSourceCRN}} 
      MESSAGE: {{message}}
      ```
      {: codeblock}

      The original log line will be displayed followed by the custom formatting.


## Create a parsing rule
{: #LA-create-parsing rule}
{: step}

There are occasions when you might want to search for information that is available in log records. Parsing rules maps information from a log line to a searchable field.

1. [Make sure you are logged in to the {{site.data.keyword.cloud_notm}} and have accessed the {{site.data.keyword.la_full_notm}} web UI](#LA-launch-ui).

2. Click the **Settings** icon ![Settings icon](/images/config.png "Settings icon").

3. Click **PARSING**.

4. Click **Create Template**.  The template wizard opens.

5. Click the ![Pencil icon](/images/pencil.png "Pencil icon") and enter a name for your parsing rule.

6. For this tutorial, for **Choose a sample log line to begin building your template** select *Find an existing log line*.   Enter a search term that will match a field in your log.  See [Customize the data displayed for a view](#LA-customize-log-format) for information on extracting log fields.

7. Scroll to the bottom of the page and click **Build Parsing Template**.  A **Reference Line** for your log records is displayed.

8. Choose the **Extract values by delimiter** extractor.

9. For **Delimiter** specify a `,` (comma). A preview of the output delimited by a comma is presented for your review.

10. Choose one of the entries.  For example, if your log contains a field called `message` you might select that line.

11.  For **Choose an Operator** select **Extract Values by Delimiter**.

12. For **Delimiter** specify a delimiter that makes sense for your selected entry.  For example, a reasonable delimiter might be a `:` (colon).  A preview of the delimited output is presented for your review.

13. Select an entry containing a date value.

14. For **Choose an Operator** select **Trim Value**.  Using the index range specify a starting and ending character position so only the date is retained in the displayed output.

15. For **Choose an Operator** select **Capture in Field** to set the name of the field that will capture this information.

16. For **Field Name** specify a name that you will use to search for this type of information.

17. At the bottom of the page click **Proceed to Validation**.

18. For **Set a query and verify parsed output with different sample lines** enter a search that will return multiple records.  For example, `message`.

19. If all log lines returned match the rule you specified, click **Mark as Valid** for each and then click **Activate** at the bottom of the page.

    Until you validate all results, the **Activate** option will be disabled.
    {: note}

The rule will take affect in approximately 15 minutes.


## Analyze the log line
{: #LA-analyze-log}
{: step}


## Apply a timeframe
{: #LA-timeframe}
{: step}


## Create dashboard
{: #LA-dashboard}
{: step}


## Monitor cluster API logs
{: #LA-monitor-cluster-logs}
{: step}


## Add alert to custom view
{: #LA-add-alert}
{: step}


<!-- Introduce each major step with a description of what it will accomplish. If there are sequential substeps, use an ordered list for each substep. Don't include the step number. -->

First, you need to set up a Kubernetes cluster on the {{site.data.keyword.containershort_notm}} service. {{site.data.keyword.containershort_notm}} delivers powerful tools by combining Docker and Kubernetes technologies, an intuitive user experience, and built-in security and isolation to automate the deployment, operation, scaling, and monitoring of containerized apps in a cluster of compute hosts.

1. In the IBM Cloud catalog, go to the [Kubernetes Service](/kubernetes/catalog/cluster/create).
1. Select **Standard** as the cluster type, and select **2 MB / 1 Worker** as the machine type. All other options can be left as default.  
1. Click **Create** to create your cluster. Check the status of your cluster and worker nodes until they're in the Ready state. 

You'll need to wait until your workers are ready to move to the next step. 
{: note}

## Build your app locally
{: #cd-kube-build-app}
{: step}

<!-- For commands, introduce the command in a sentence first. Then surround what the user must enter in the command prompt with three backticks, and set the programming language if it applies. After the code block, add a {: pre} attribute to add a $ before the command and a copy link. --> 

You can build and run the application as you normally would using `mvn` for Java&trade; local development or `npm` for Node.js development.  You can also build a Docker image and run the application in a container to ensure consistent execution locally and on the cloud. Use the following steps to build your docker image.

1. Ensure your local Docker engine is started.
   ```
   docker ps
   ```
   {: pre}
1. Navigate to the generated project directory.
   ```
   cd <project name>
   ```
   {: pre}
1. Build the application locally.
   ```
   ibmcloud dev build
   ```
   {: pre}

   This might take a few minutes to run because all of the application dependencies are downloaded and a Docker image, which contains your application and all the required environment, is built.

## Add a task-oriented title
{: #cd-kube-step-desc}
{: step}

## Add a task-oriented title
{: #cd-kube-step-desc}
{: step}

## Add a task-oriented title
{: #cd-kube-step-desc}
{: step}

## Next steps
{: #cd-kube-step-next}

Want to start fresh? Remove the following resources that you created as a part of this tutorial:

* Delete the Git repository.
* Delete the toolchain.
* Delete the cluster.
* Delete the Slack channel.
