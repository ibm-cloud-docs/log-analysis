---

copyright:
  years: 2018
lastupdated: "2018-10-22"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

# Working with the LogDNA instance ingestion key
{: #ingestion_key}

The ingestion key is a security key that you must use to configure LogDNA agents and successfully forward logs to your IBM Log Analysis with LogDNA instance in {{site.data.keyword.Bluemix}}. You automatically get the ingestion key when you provision an instance. Alternatively, you can also obtain the ingestion key by creating a service ID for the instance. 
{:shortdesc}

**Note:** 

* To work with ingestion keys through the IBM Log Analysis with LogDNA Web UI, you must have an IAM policy with platform role **Viewer** and service role **Manager** for the IBM Log Analysis with LogDNA service. 
* To work with ingestion keys through the {{site.data.keyword.Bluemix_notm}} UI, you must have an IAM policy with platform role **Editor** and service role **Manager** for the IBM Log Analysis with LogDNA service. 


## Getting the ingestion key through the {{site.data.keyword.Bluemix_notm}} UI
{: #ibm_cloud_ui}

To get the ingestion key for an IBM Log Analysis with LogDNA instance by using the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} UI opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. The IBM Log Analysis with LogDNA dashboard opens. You can see the list of logging instances that are available on {{site.data.keyword.Bluemix_notm}}.

3. Identify the instance for which you want to get the ingestion key, and click **View ingestion key**.

4. A pop up window opens where you can click **Show** to view the ingestion key.


## Getting the ingestion key through the IBM Log Analysis with LogDNA Web UI
{: #logdna_ui}

To get the ingestion key for an IBM Log Analysis with LogDNA instance by using the IBM Log Analysis with LogDNA Web UI, complete the following steps:

1. Launch the IBM Log Analysis with LogDNA web UI. For more information, see [Launching the IBM Log Analysis with LogDNA Web UI](/docs/services/Log-Analysis-with-LogDNA/launch_webui.html#launch_webui).

2. Select the **Configuration** icon. Then select **Organization**. 

3. Select **API keys**.

You can see the ingestion keys that have been created. 

**Note:** Only one ingestion key is active at once. 


## Getting the ingestion key through the {{site.data.keyword.Bluemix_notm}} CLI
{: #ibm_cloud_cli}

To get the ingestion key for an IBM Log Analysis with LogDNA instance through the command line, complete the following steps:

1. [Pre-requisite] Install the {{site.data.keyword.Bluemix_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.Bluemix_notm}} where the instance is running. Run the following command: [`ibmcloud login`](/docs/cli/reference/ibmcloud/bx_cli.html#ibmcloud_login)

3. Set the resource group where the IBM Log Analysis with LogDNA instance is running. Run the following command: [`ibmcloud target`](/docs/cli/reference/ibmcloud/bx_cli.html#ibmcloud_target) with the option `-g`.

    By default, the `default` resource group is set.

4. Get the name of the API key that is associated with the IBM Log Analysis with LogDNA instance. Run the [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud/cli_resource_group.html#ibmcloud_resource_service_instances) command:

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    Identify the service key that is associated to your instance.

5. Get the ingestion key. Run the [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud/cli_resource_group.html#ibmcloud_resource_service_key) command:

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    where

    * APIKEY_NAME is the name of the API key
 
    The output from this command includes the field **ingestion_key** that contains the ingestion key for the LogDA instance.


## Renew the ingestion key 
{: #renew}

If the ingestion key is compromissed or you have a policy to renew it after a number of days, you can generate a new key and delete the old one.

To renew the ingestion key for an IBM Log Analysis with LogDNA instance by using the IBM Log Analysis with LogDNA Web UI, complete the following steps:

1. Launch the IBM Log Analysis with LogDNA web UI. For more information, see [Launching the IBM Log Analysis with LogDNA Web UI](/docs/services/Log-Analysis-with-LogDNA/launch_webui.html#launch_webui).

2. Select the **Configuration** icon. Then select **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that have been created. 

4. Select **Generate Ingestion Key**.

    A new key is added to the list.

5. Delete the old ingestion key. Click **delete**.

**Note:** After you reset the ingestion key, you must update the ingestion key for any log sources that you have configured to forward logs to this IBM Log Analysis with logDNA instance.
