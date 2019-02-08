---

copyright:
  years: 2018, 2019
lastupdated: "2010-01-08"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

# Configuring a CF app to forward logs to a LogDNA instance
{: #cf}

You can configure a Cloud Foundry (CF) application to stream application logs to an instance of the the {{site.data.keyword.la_full_notm}} service. You can configure a secure connection or a TLS connection.
{:shortdesc}

To send CF logs to a {{site.data.keyword.la_short}} instance, consider the following information:
* In the {{site.data.keyword.la_short}} instance, you must provision a syslog port. 
* In CF, you must define a user-provided service (cups) instance to deliver the logging instance credentials to the CF app, and to trigger streaming of application logs to the syslog port that you enabled in your {{site.data.keyword.la_short}} instance. 



# Before you begin
{: #cf-prereqs}

The steps that are provided through this tutorial assume that you will be working in the US-South region. 

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).

Use a user ID that is a member or an owner of an {{site.data.keyword.Cloud_notm}} account. To get an {{site.data.keyword.Cloud_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://cloud.ibm.com /registration/){:new_window}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group      | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
| CF app                               |  Resource                  | Editor  | us-south  | This policy is required to configure the CF app to forward logs to the logging instance. |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

* Install the {{site.data.keyword.Cloud_notm}} CLI. For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).


## Objectives
{: #cf-objectives}

In this tutorial, you can learn how to configure a CF application to send logs to a logging instance. In particular, you will:

- Provision an {{site.data.keyword.la_full_notm}} instance. 
- Configure the CF app to forward logs to the logging instance. 
- Open the LogDNA dashboard to find your logs. 


## Step1: Provision an {{site.data.keyword.la_full_notm}} instance
{: #cf-step1}

To provision a service instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.Bluemix_notm}} console, complete the following steps:

1. Log in to the [{{site.data.keyword.Cloud_notm}} account ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://cloud.ibm.com ) where you created your Kubernetes cluster.

2. Click **Catalog**. A list of {{site.data.keyword.Bluemix_notm}} services opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click **{{site.data.keyword.la_full_notm}}**. The **Observability** dashboard opens.

5. Select **Create instance**. 

6. Enter a name for the service instance.

7. Select the resource group that your cluster is in. By default, the **Default** resource group is set for you. 

8. Choose a service plan for your service instance. By default, the **Lite** plan is selected for you. For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

9. Click **Create**. The **Observability** dashboard opens and shows the details for your service. 

To provision an instance through the CLI, see [Provisioning an instance through the {{site.data.keyword.Bluemix_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA/provision.html#provision_cli).
{: tip}



## Step 2: Provision a syslog port in the logging instance
{: #cf-step2}

### 1. Launch the LogDNA web UI
{: #cf-step2-1}

You launch the web UI within the context of an {{site.data.keyword.la_full_notm}} instance, from the {{site.data.keyword.Cloud_notm}} UI. 

Complete the following steps to launch the web UI:

1. Log in to your {{site.data.keyword.Cloud_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [https://cloud.ibm.com ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. 

    The list of instances that are available on {{site.data.keyword.Bluemix_notm}} is displayed.

4. Select the logging instance where you want to send CF application logs. Then, click **View LogDNA**.

The Web UI opens.


### 2. Provision a port
{: #cf-step2-2}

From the LogDNA web UI, complete the following steps:

1. Open the log sources panel on the LogDNA web UI. Select the *Install instructions icon*: ![Install instructions icon](../../images/logdna_install.png "Install instructions icon")
2. Select **View platform** &gt; **Cloud Foundry**.
3. Click **Provision a Syslog port**.  

A port is displayed. Copy the port. 


## Step 3: Configure a user-provided service instance for your CF app
{: #cf-step3}

Complete the following steps:

1. Create a user-provided service instance (cups). Specify the URL of the logging service with the option `-l`.

    To create a cups instance without security enabled, run the following command:

    ```
    ibmcloud cf cups SVC_INSTANCE_NAME -l syslog://SYSLOG_ENDPOINT_URL:PORT_NUMBER`
    ```
    {: codeblock}

    To create a cups instance with TLS enabled, run the following command:

    ```
    ibmcloud cf cups SVC_INSTANCE_NAME -l syslog-tls://SYSLOG_ENDPOINT_URL:PORT_NUMBER`
    ```
    {: codeblock}

    where

    * *SVC_INSTANCE_NAME* is the name of the CF service instance.

    * *SYSLOG_ENDPOINT_URL* is the endpoint URL in the region where the instance is running. For example, for us-south, the URL is: `syslog-a.us-south.logging.cloud.ibm.com`

    * *PORT_NUMBER* is the port number that you provisioned in your logging instance.

    A sample command looks as follows:

    ```
    ibmcloud cf cups MyCFsvcInstance -l syslog://syslog-a.us-south.logging.cloud.ibm.com:49235
    ```
    {: screen}

2. Bind the service. Run the following command:

    ```
    ibmcloud cf bind-service CF_APP_NAME SVC_INSTANCE_NAME
    ```
    {: codeblock}

    where

    * *CF_APP_NAME* is the name of the Cloud Foundry application.

    * *SVC_INSTANCE_NAME* is the name of the CF service instance.

    A sample command looks as follows:

    ```
    ibmcloud cf bind-service MyCFapp MyCFsvcInstance
    ```
    {: screen}

3. Restage the CF application. Run the following command:

    ```
    ibmcloud cf restage CF_APP_NAME
    ```
    {: codeblock}

    where *CF_APP_NAME* is the name of the Cloud Foundry application.

     A sample command looks as follows:

    ```
    ibmcloud cf restage MyCFapp
    ```
    {: screen}


## Step 3: Verify that CF app logs are displayed through the LogDNA web UI
{: #cf-step3}

Launch the LogDNA web UI. Then, search for your CF application logs. For more information, see [Filtering logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step5).

Try also some of these tasks:
- [Search logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step6)
- [Define views](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step7)
- [Configure alerts](https://docs.logdna.com/docs/alerts). 

**Note:** Some of these features require a plan upgrade.

