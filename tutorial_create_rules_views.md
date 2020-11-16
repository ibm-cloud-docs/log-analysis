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


## View logs
{: #LA-view-logs}
{: step}


## Customize data display
{: #LA-customize-data-display}
{: step}


## Create a parsing rule
{: #LA-create-parsing rule}
{: step}


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
