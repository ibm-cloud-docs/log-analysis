---

copyright:
  years:  2018, 2020
lastupdated: "2020-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

2. Go to the Menu icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**. 

3. Select **Logging**. The {{site.data.keyword.la_full_notm}} dashboard opens. You can see the list of logging instances that are available on {{site.data.keyword.cloud_notm}}.

3. Identify the instance for which you want to get the ingestion key, and click **View ingestion key**.

4. A window opens where you can click **Show** to view the ingestion key.


## Get the ingestion key through the {{site.data.keyword.la_full_notm}} web UI
{: #logdna_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Click the **Configuration** icon ![Configuration icon](images/admin.png) &gt; **Organization**. 

3. Select **API keys**. 

You can see the ingestion keys that are enabled. 



## Get the ingestion key through the CLI
{: #ingestion_key_cli}

To get the ingestion key for a LogDNA instance through the command line, complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-getting-started).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the LogDNA instance is running. Run the following command: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)
/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login
3. Set the resource group where the LogDNA instance is running. Run the following command: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name. Run the following command: [`ibmcloud resource service-instances`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```
    ibmcloud resource service-instances
    ```
    {: pre}

5. Get the name of the key that is associated with the LogDNA instance. Run the [`ibmcloud resource service-keys`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances) command:

    ```
    ibmcloud resource service-keys --instance-name INSTANCE_NAME
    ```
    {: pre}

    where INSTANCE_NAME is the name of the instance that you obtained in the previous step.

6. Get the ingestion key. Run the [`ibmcloud resource service-key`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) command:

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: pre}

    where APIKEY_NAME is the name of the API key.
 
    The output from this command includes the field **ingestion key** that contains the ingestion key for the instance.





## Reset the ingestion key 
{: #reset}

If the ingestion key is compromised or you have a policy to renew it after a number of days, you can generate a new key and delete the old one.

To renew the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Click the **Configuration** icon ![Configuration icon](images/admin.png) &gt; **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that are enabled. 

4. Select **Generate Ingestion Key**.

    A new key is added to the list.

5. Delete the old ingestion key. Click **delete**.

After you reset the ingestion key, you must update the ingestion key for any log sources that you have configured to forward logs to this {{site.data.keyword.la_full_notm}} instance.
{: important}

For example, see [Resetting the ingestion key that is used by a Kubernetes cluster](/docs/Log-Analysis-with-LogDNA?topic=LogDNA-kube_reset).



