---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, ingestion key

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Working with ingestion keys
{: #ingestion_key}

The ingestion key is a security key that you must use to configure logging agents and successfully forward logs to your {{site.data.keyword.la_full_notm}} instance in {{site.data.keyword.cloud_notm}}. You automatically get the ingestion key when you provision an instance. Alternatively, you can also obtain the ingestion key by creating a service ID for the instance. 
{: shortdesc}

* To work with ingestion keys through the {{site.data.keyword.la_full_notm}} Web UI, you must have an IAM policy with platform role **Viewer** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service. 
* To work with ingestion keys through the {{site.data.keyword.cloud_notm}} UI, you must have an IAM policy with platform role **Editor** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service. 


## Getting the ingestion key through the {{site.data.keyword.cloud_notm}} UI
{: #ibm_cloud_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

2. Go to the Menu icon ![Menu icon](../../icons/icon_hamburger.svg) &gt; **Observability**. 

3. Click **Logging**. The {{site.data.keyword.la_full_notm}} dashboard opens. You can see the list of logging instances that are available on {{site.data.keyword.cloud_notm}}.

4. Identify the instance that you want to use to collect your cluster logs. 

5. Click the **Actions** icon ![Actions icon](../../icons/action-menu-icon.svg) >  **View key**.

    A window opens where you can click **Show** to view the ingestion key.


## Getting the ingestion key through the {{site.data.keyword.la_full_notm}} web UI
{: #log_analysis_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Settings icon](../images/admin.png) &gt; **Organization** &gt; **API keys**. 

    You can see the ingestion keys that are enabled. 

3. Copy the ingestion key that shows in the **API keys** section. 





## Getting the ingestion key through the CLI
{: #ingestion_key_cli}

To get the ingestion key for a logging instance through the command line, complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the logging instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the logging instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```text
    ibmcloud resource service-instances
    ```
    {: pre}

5. Get the name of the key that is associated with the logging instance. Run the [ibmcloud resource service-keys](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) command:

    ```text
    ibmcloud resource service-keys --instance-name INSTANCE_NAME
    ```
    {: pre}

    where INSTANCE_NAME is the name of the instance that you obtained in the previous step.

6. Get the ingestion key. Run the [ibmcloud resource service-key](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) command:

    ```text
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: pre}

    where APIKEY_NAME is the name of the API key.
 
    The output from this command includes the field **ingestion key** that contains the ingestion key for the instance.





## Resetting the ingestion key 
{: #reset}

If the ingestion key is compromised or you have a policy to renew it after a number of days, you can generate a new key and delete the old one.

To renew the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Settings icon](../images/admin.png) &gt; **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that are enabled. 

4. Select **Generate Ingestion Key**.

    A new key is added to the list.

5. Delete the old ingestion key. Click **X** next to the ingestion key to be deleted.

After you reset the ingestion key, you must update the ingestion key for any log sources that you have configured to forward logs to this {{site.data.keyword.la_full_notm}} instance.
{: important}

For example, see [Resetting the ingestion key that is used by a Kubernetes cluster](/docs/log-analysis?topic=log-analysis-kube_reset).



