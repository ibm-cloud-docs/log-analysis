---

copyright:
  years: 2019
lastupdated: "2019-08-14"

keywords: LogDNA, IBM, Log Analysis, logging, cf

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


# Monitoring Cloud Foundry logs
{: #monitor_cfapp_logs}

In {{site.data.keyword.cloud}} public, you can monitor logs from Cloud Foundry (CF) resources that run in the {{site.data.keyword.cloud_notm}} or outside the {{site.data.keyword.cloud_notm}} by using the {{site.data.keyword.la_full_notm}} service. You can view, filter, search, and analyze these logs through the web UI for a number of days that is determined by the plan of your logging instance. You can also configure archiving, and have access to those logs through the archived files.
{:shortdesc}

You have different options to collect and forward logs to an instance of the {{site.data.keyword.la_full_notm}} service:
* You can configure 1 instance of the {{site.data.keyword.la_full_notm}} service per region with the flag **service platform logs**. This instance collects infrastructure and application logs for any CF apps that run on that same region.
* You can configure a CF user provided service (CUPS) for each CF app to monitor your CF app logs through a {{site.data.keyword.la_full_notm}} instance.


Add graph ( Cloud Foundry (CF) infrastructure, from CF apps that run in the {{site.data.keyword.cloud_notm}} or on-prem, and from requests made to your apps through internal components of CF and stream them to the {{site.data.keyword.la_full_notm}} service. )



## Monitor CF resources that are hosted in {{site.data.keyword.cloud_notm}} public
{: #monitor_cfapp_logs_public}

CF resources are location bound resources in the {{site.data.keyword.cloud_notm}}. For example, you can have a CF app running in the Dallas (us-south) region. 

In the {{site.data.keyword.cloud_notm}}, you can configure 1 logging instance to collect and host platform services logs in a region. After the instance is provisioned and configured in a region, logs that are generated from enabled services in that region such as CF apps or CF infrastructure are automatically collected and forwarded through the ELK-Adatper. You can monitor logs through this logging instance.

To configure an instance from the Observability dashboard in the {{site.data.keyword.cloud_notm}}, see [Configuring IBM Cloud service logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-config_svc_logs).



## Configuring a CF app to forward logs to a custom LogDNA instance by using Syslog drains
{: #monitor_cfapp_logs}

You can configure a Cloud Foundry (CF) application, running in the {{site.data.keyword.cloud_notm}} or outside the {{site.data.keyword.cloud_notm}}, to stream application logs to an instance of the the {{site.data.keyword.la_full_notm}} service. You can configure a secure connection or a TLS connection between the CF app and the logging instance.

To send CF logs to a {{site.data.keyword.la_short}} instance, consider the following information:
* In the {{site.data.keyword.la_short}} instance, you must provision a syslog port. 
* In CF, you must define a user-provided service (cups) instance to deliver the logging instance credentials to the CF app, and to trigger streaming of application logs to the syslog port that you enabled in your {{site.data.keyword.la_short}} instance. 



### Before you begin
{: #monitor_cfapp_logs_prereqs}

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources. For example, to work in the US-south region and in the default resource group, you need the following permissions: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group      | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
{: caption="Table 1. List of IAM policies" caption-side="top"} 

Your {{site.data.keyword.IBM_notm}}ID must have the **developer** role assigned for the Cloud Foundry space where the CF application is running.

You must install the {{site.data.keyword.cloud_notm}} CLI. For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli). This CLI includes the CF CLI.

You must have a CF app deployed and running.


### Step1: Provision an {{site.data.keyword.la_full_notm}} instance
{: #monitor_cfapp_logs_step1}

To provision a service instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} console, complete the following steps:

1. Log in to the [{{site.data.keyword.cloud_notm}} account ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login) where you created your Kubernetes cluster.

2. Click **Catalog**. A list of {{site.data.keyword.cloud_notm}} services opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click **{{site.data.keyword.la_full_notm}}**. The **Observability** dashboard opens.

5. Select **Create instance**. 

6. Enter a name for the service instance.

7. Select the resource group that your cluster is in. By default, the **Default** resource group is set for you. 

8. Choose a service plan for your service instance. By default, the **Lite** plan is selected for you. For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

9. Click **Create**. The **Observability** dashboard opens and shows the details for your service. 

To provision an instance through the CLI, see [Provisioning an instance through the {{site.data.keyword.cloud_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli).
{: tip}



### Step 2: Provision a syslog port in the logging instance
{: #monitor_cfapp_logs_step2}

#### 1. Launch the LogDNA web UI
{: #monitor_cfapp_logs_step2_1}

You launch the web UI within the context of an {{site.data.keyword.la_full_notm}} instance, from the {{site.data.keyword.cloud_notm}} UI. 

Complete the following steps to launch the web UI:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    Click [{{site.data.keyword.cloud_notm}} dashboard ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window} to launch the {{site.data.keyword.cloud_notm}} dashboard.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. 

    The list of instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select the logging instance where you want to send CF application logs. Then, click **View LogDNA**.

The web UI opens.


#### 2. Provision a port
{: #monitor_cfapp_logs_step2_2}

From the LogDNA web UI, complete the following steps:

1. Open the log sources panel on the LogDNA web UI. Select the *Install instructions icon*: ![Install instructions icon](../images/logdna_install.png "Install instructions icon")
2. Select **View platform** &gt; **Cloud Foundry**.
3. Click **Provision a Syslog port**.  

A port is displayed. Copy the port. 


### Step 3: Configure a user-provided service instance for your CF app
{: #monitor_cfapp_logs_step3}

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

    Where

    *SVC_INSTANCE_NAME* is the name of the CF service instance.

    *SYSLOG_ENDPOINT_URL* is the endpoint URL in the region where the instance is running. For example, for us-south, the URL is: `syslog-a.us-south.logging.cloud.ibm.com`

    *PORT_NUMBER* is the port number that you provisioned in your logging instance.

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

    Where

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

    Where *CF_APP_NAME* is the name of the Cloud Foundry application.

     A sample command looks as follows:

    ```
    ibmcloud cf restage MyCFapp
    ```
    {: screen}


### Step 4: Verify that CF app logs are displayed through the LogDNA web UI
{: #monitor_cfapp_logs_step4}

Launch the LogDNA web UI. Then, search for your CF application logs. For more information, see [Filtering logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5).

Try also some of these tasks:
- [Search logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)
- [Define views](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)
- [Configure alerts](https://docs.logdna.com/docs/alerts). 

**Note:** Some of these features require a plan upgrade.








