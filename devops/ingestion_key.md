---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords: IBM, Log Analysis, logging, ingestion key

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Working with ingestion keys
{: #ingestion_key}

The ingestion key is a security key that you must use to configure logging agents and successfully forward logs to your {{site.data.keyword.la_full_notm}} instance in {{site.data.keyword.cloud_notm}}. You automatically get the ingestion key when you provision an instance.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

To work with ingestion keys through the {{site.data.keyword.la_full_notm}} Web UI, you must have an IAM policy with platform role **Viewer** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service.


## Getting ingestion keys
{: #get_ingestion_key}
{: ui}

### Getting the ingestion key through the {{site.data.keyword.cloud_notm}} UI
{: #ingestion_key_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

2. Go to the Menu icon ![Menu icon](../../icons/icon_hamburger.svg) &gt; **Observability**.

3. Click **Logging**. The {{site.data.keyword.la_full_notm}} dashboard opens. You can see the list of logging instances that are available on {{site.data.keyword.cloud_notm}}.

4. Identify the instance that you want to use to collect your cluster logs.

5. Click the **Actions** icon ![Actions icon](../../icons/action-menu-icon.svg) >  **View key**.

    A window opens where you can click **Show** to view the ingestion key.


### Getting the key through the {{site.data.keyword.la_short}} web UI
{: #ingestion_key_la_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Settings icon](../images/admin.png) &gt; **Organization** &gt; **API keys**.

    You can see the ingestion keys that are enabled.

3. Copy the ingestion key that shows in the **API keys** section.

### Creating a service key by using the logging UI
{: #ingestion_key_create_ui}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important}

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

Complete the following steps to create a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Settings icon](../images/admin.png).

3. Select **Organization**.

4. Select **API keys**.

   If you have the correct permissions, the available service keys are displayed in the **Ingestion keys** section.

5. Click **Generate Ingestion Key**. A new key is added to the list.

### Deleting a service key by using the UI
{: #ingestion_key_delete_ui}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important}

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

Complete the following steps to delete an ingestion key:

1. [Launch the {{site.data.keyword.la_short}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Settings icon](../images/admin.png).

3. Select **Organization**.

4. Select **API keys**.

   If you have the correct permissions, the available service keys are displayed in the **Ingestion Keys** section.

5. Delete the key by clicking the **X** next to the key to be deleted.


### Rotating an ingestion key through the UI
{: #ingestion_key_rotate_ui}

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

For example, see [Resetting the ingestion key that is used by a Kubernetes cluster](/docs/log-analysis?topic=log-analysis-kube_reset_ingestion).

## Getting the ingestion key through the CLI
{: #ingestion_key_cli}
{: cli}

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

## Managing ingestion keys through the API
{: #ingestion_key_api}
{: api}

You can use the configuration API to manage keys.

### List all keys
{: #ingestion_key_api_list}

To list all ingestion keys that ae available in an instance, you can run the following request:

```sh
curl  https://API_ENDPOINT/v1/config/keys?type="ingestion"
  -H 'content-type: application/json' \
  -H 'servicekey: SERVICE_KEY'
```
{: pre}

Where:

`API_ENDPOINT`
:   Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage categories programmatically. For information about endpoints per region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).

For example, to list all the ingestion keys that are available in an instance in US South, you can run the following request:

```sh
curl  https://api.us-south.logging.cloud.ibm.com/v1/config/keys?type="ingestion"  -H "content-type: application/json"  -H "servicekey: xxxxxxxxx"
```
{: pre}

### Get details on a key
{: #ingestion_key_api_get}

To get information on an ingestion key, you can run:

```sh
curl -X GET  https://API_ENDPOINT/v1/config/keys/KEY_ID
  -H 'content-type: application/json' \
  -H 'servicekey: SERVICE_KEY'
```
{: pre}

Where:

`API_ENDPOINT`
:   Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage categories programmatically. For information about endpoints per region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).

`KEY_ID`
:   ID value of the ingestion key for which you want to get details.

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).

For example, to get information on an ingestion key that is available in an instance in US South, you can run the following request:

```sh
curl  https://api.us-south.logging.cloud.ibm.com/v1/config/keys/123456789"  -H "content-type: application/json"  -H "servicekey: xxxxxxxxx"
```
{: pre}

### Create a key
{: #ingestion_key_api_create}

```sh
curl -X POST  https://API_ENDPOINT/v1/config/keys?type="ingestion"
  -H 'content-type: application/json' \
  -H 'servicekey: SERVICE_KEY' \
  -d '{"name": "KEY_NAME"}'
```
{: pre}

Where:

`API_ENDPOINT`
:   Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage categories programmatically. For information about endpoints per region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).

`KEY_NAME`
:   Name that you want to give the key. The maximum size of a name is 30 characters.

### Change the name of a key
{: #ingestion_key_api_update}

```sh
curl -X PUT  https://API_ENDPOINT/v1/config/keys/KEY_ID
  -H 'content-type: application/json' \
  -H 'servicekey: SERVICE_KEY' \
  -d '{"name": "KEY_NAME"}'
```
{: pre}

Where:

`API_ENDPOINT`
:   Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage categories programmatically. For information about endpoints per region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).

`KEY_ID`
:   ID value of the ingestion key for which you want to get details.

`KEY_NAME`
:   Name that you want to give the key. The maximum size of a name is 30 characters.

### Delete a key
{: #ingestion_key_api_delete}

To delete an ingestion key, run the following command.

```sh
curl -X DELETE "https://API_ENDPOINT/v1/config/keys/KEY_ID"
  -H 'content-type: application/json' \
  -H 'servicekey: SERVICE_KEY'
```
{: pre}

Where:

`API_ENDPOINT`
:   Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage categories programmatically. For information about endpoints per region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).

`KEY_ID`
:   ID value of the ingestion key to be deleted.

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).


## Rotating the ingestion key by using the API
{: #ingestion_key_replace_api}
{: api}

If the ingestion key is compromised or you have a policy that requies renewal of a key after a number of days, you can generate a new key and delete the old one.


To rotate a key, complete the following steps:

1. Get the details of the key that you want to rotate.

    You can list all ingestion keys to obtain the ID of the key that you want to rotate. For more information, see [Listing all ingestion keys](#ingestion_key_api_list).

    If you know the Key ID, skip to the next step.

2. Create a new key. For more information, see [Creating an ingestion key](#ingestion_key_api_create).

3. Delete the old key. Make sure you use the ID of the key that you identified previously. For more information, see [Deleting a key](#ingestion_key_api_delete).

4. After you rotate the ingestion key, you must update the ingestion key for any log sources that you have configured to forward logs to this {{site.data.keyword.la_short}} instance. For example, see [Resetting the ingestion key that is used by a Kubernetes cluster](/docs/log-analysis?topic=log-analysis-kube_reset_ingestion).
{: important}
