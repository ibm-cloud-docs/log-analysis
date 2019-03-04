---

copyright:
  years:  2018, 2019
lastupdated: "2019-02-28"

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

# Working with ingestion keys
{: #ingestion_key}

The ingestion key is a security key that you must use to configure LogDNA agents and successfully forward logs to your {{site.data.keyword.la_full_notm}} instance in {{site.data.keyword.cloud_notm}}. You automatically get the ingestion key when you provision an instance. Alternatively, you can also obtain the ingestion key by creating a service ID for the instance. 
{:shortdesc}

**Note:** 

* To work with ingestion keys through the {{site.data.keyword.la_full_notm}} Web UI, you must have an IAM policy with platform role **Viewer** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service. 
* To work with ingestion keys through the {{site.data.keyword.cloud_notm}} UI, you must have an IAM policy with platform role **Editor** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service. 


## Get the ingestion key through the {{site.data.keyword.cloud_notm}} UI
{: #ibm_cloud_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    Click [{{site.data.keyword.cloud_notm}} dashboard ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window} to launch the {{site.data.keyword.cloud_notm}} dashboard.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} UI opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. The {{site.data.keyword.la_full_notm}} dashboard opens. You can see the list of logging instances that are available on {{site.data.keyword.cloud_notm}}.

3. Identify the instance for which you want to get the ingestion key, and click **View ingestion key**.

4. A window opens where you can click **Show** to view the ingestion key.


## Get the ingestion key through the {{site.data.keyword.la_full_notm}} web UI
{: #logdna_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. Launch the {{site.data.keyword.la_full_notm}} web UI. For more information, see [Launching the {{site.data.keyword.la_full_notm}} Web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Select the **Configuration** icon. Then select **Organization**. 

3. Select **API keys**.

You can see the ingestion keys that have been created. 

**Note:** Only one ingestion key is active at once. 


## Get the ingestion key through the {{site.data.keyword.cloud_notm}} CLI
{: #ibm_cloud_cli}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance through the command line, complete the following steps:

1. [Pre-requisite] Install the {{site.data.keyword.cloud_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the instance is running. Run the following command: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the {{site.data.keyword.la_full_notm}} instance is running. Run the following command: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target) with the option `-g`.

    By default, the `default` resource group is set.

4. Get the name of the API key that is associated with the {{site.data.keyword.la_full_notm}} instance. Run the [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) command:

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    Identify the service key that is associated to your instance.

5. Get the ingestion key. Run the [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) command:

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    Where APIKEY_NAME is the name of the API key
 
    The output from this command includes the field **ingestion_key** that contains the ingestion key for the instance.


## Reset the ingestion key 
{: #reset}

If the ingestion key is compromised or you have a policy to renew it after a number of days, you can generate a new key and delete the old one.

To renew the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. Launch the {{site.data.keyword.la_full_notm}} web UI. For more information, see [Launching the {{site.data.keyword.la_full_notm}} web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Select the **Configuration** icon. Then select **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that have been created. 

4. Select **Generate Ingestion Key**.

    A new key is added to the list.

5. Delete the old ingestion key. Click **delete**.

**Note:** After you reset the ingestion key, you must update the ingestion key for any log sources that you have configured to forward logs to this {{site.data.keyword.la_full_notm}} instance.



