---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, service keys

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Managing service keys
{: #service_keys}

In an {{site.data.keyword.la_full}} instance you can create, delete, and view service keys by using the UI.  You can also create and view service keys by using the CLI and API.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

A service key is a unique code that is passed in an API request to identify the calling application or user.

You must use a logging service key to complete any of the following tasks:
- Export data programmatically
- Manage views and alerts programmatically by using the Configuration API or Terraform.
- Configure resources such as groups, archiving, keys by using the Configuration API or Terraform.

You can enable a maximum of 20 service keys for each instance.
{: important}


## Prereqs. Check your IAM permissions to manage service keys
{: #service_keys_prereq}

To generate a new service key or get an existing service key, you need the following roles on the {{site.data.keyword.la_full_notm}}:
- Platform role `operator`, `editor` or `administrator`
- Service role `Manager`

To restrict access to a service key, you need the following role on the `IAM Identity Service service`:
- Platform role `Administrator`



## Managing service keys by using the UI
{: #service_keys_ui}
{: ui}

You can create, delete, and view service keys through the UI.

### Creating a service key by using the logging UI
{: #service_keys_create}

You must have the **manager** role for the {{site.data.keyword.la_short}} service to complete this step.
{: important}

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

Complete the following steps to create a service key:

1. [Launch the {{site.data.keyword.la_short}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Settings icon](../images/admin.png).

3. Select **Organization**.

4. Select **API keys**.

   If you have the correct permissions, the available service keys are displayed in the **Service Keys** section.

5. Click **Generate Service Key**. A new key is added to the list.



### Deleting a service key by using the UI
{: #service_keys_delete}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important}

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).


Complete the following steps to delete a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Settings icon](../images/admin.png).

3. Select **Organization**.

4. Select **API keys**.

   If you have the correct permissions, the available service keys are displayed in the **Service Keys** section.

5. Delete the key by clicking the **X** next to the key to be deleted.


### Viewing a service key by using the UI
{: #service_keys_view}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important}

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

Complete the following steps to view a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Settings icon](../images/admin.png).

3. Select **Organization**.

4. Select **API keys**.

   If you have the correct permissions, the available service keys are displayed in the **Service Keys** section.



### Rotating an service key through the UI
{: #service_keys_rotate_ui}

If the service key is compromised or you have a policy to renew it after a number of days, you can generate a new key and delete the old one.

To renew the service key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Settings icon](../images/admin.png) &gt; **Organization**.

3. Select **API keys**.

    You can see the service keys that are enabled.

4. Select **Generate Service Key**.

    A new key is added to the list.

5. Delete the old service key. Click **X** next to the service key to be deleted.

After you reset the service key, you must update any operation processes where the service key is used with the new value.
{: important}




## Managing a logging service key by using the CLI
{: #service_keys_cli}
{: cli}

You can create and view logging service keys by using the {{site.data.keyword.cloud_notm}} CLI.

### Creating a service key by using the CLI
{: #service_keys_cli_create}

Only a single service key can be created using the CLI.  Using these commands to create a service key where one already exists will not create a new key.  If you need to create more than one service key, use the [UI](#service_keys_ui) or use the [API]](#service_keys_api_create).
{: important}

To create a logging service key for a logging instance through the command line, complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the logging instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the logging instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```text
    ibmcloud resource service-instances
    ```
    {: pre}

5. Create the {{site.data.keyword.cloud_notm}} resource service key. Run the [ibmcloud resource service-key-create](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create) command:

    ```text
    ibmcloud resource service-key-create <NAME> --instance-name <SERVICE_INSTANCE>
    ```
    {: pre}

    Where NAME is the desired name of the service key and SERVICE_INSTANCE is the name of the service instance from the previous step.

    The output from this command includes the field **service_key** that contains the logging service key for the instance.

6. Restrict access to the {{site.data.keyword.cloud_notm}} resource service key so that only users that have the `administrator` and `manager` roles can see information associated with the service key.

    Identify the service ID associated with the service that you created in the previous step. Run the following command to list all the service IDs that are available in the resource group:

    ```text
    ibmcloud iam service-ids
    ```
    {: pre}

    The **ID** column indicates the `SERVICE_ID` that is associated with the service key that you created in the previous step.

    Identify the logging instance ID. Run the following command:

    ```text
    ibmcloud resource service-instance <LOGGING_INSTANCE_NAME>
    ```
    {: pre}

    Then, create a policy to restrict access to the service key:

    ```text
    ibmcloud iam service-policy-create <SERVICE_ID> --roles Administrator,Manager --service-name logdna --service-instance <LOGGING_INSTANCE_ID]
    ```
    {: pre}


Consider deleting the service key. There is a limit on the number of service IDs per account. For more information, see [IBM Cloud IAM limits](/docs/account?topic=account-known-issues&interface=cli#iam_limits).
{: tip}

To delete a service key, run the following command:

```text
ibmcloud resource service-key-delete <NAME>
```
{: pre}



### Getting the service key by using the CLI
{: #service_keys_cli_get}


To get the service key through the command line, complete the following steps:

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
    ibmcloud resource service-keys --instance-name <INSTANCE_NAME>
    ```
    {: pre}

    where INSTANCE_NAME is the name of the instance that you obtained in the previous step.

6. Get the {{site.data.keyword.cloud_notm}} resource service key. Run the [ibmcloud resource service-key](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) command:

    ```text
    ibmcloud resource service-key <KEY_NAME>
    ```
    {: pre}

    where KEY_NAME is the name of the key obtained in the previous step.

    The output from this command includes the field **service_key** that contains a service key for the instance.  If no service key has been created for the instance, or, if you do not have **manager** access, no service key will be returned.



## Managing a service key by using the API
{: #service_keys_api}
{: api}

You can manage service keys by using the Configuration API.


### List all keys
{: #service_keys_api_list}

To list all service keys that are available in an instance, you can run the following request:

```sh
curl  https://API_ENDPOINT/v1/config/keys?type="service"
  -H 'content-type: application/json' \
  -H 'servicekey: SERVICE_KEY'
```
{: pre}

Where:

`API_ENDPOINT`
:   Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage categories programmatically. For information about endpoints per region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).



For example, to list all the service keys that are available in an instance in US South, you can run the following request:

```sh
curl  https://api.us-south.logging.cloud.ibm.com/v1/config/keys?type="service"  -H "content-type: application/json"  -H "servicekey: xxxxxxxxx"
```
{: pre}

### Get details on a key
{: #service_keys_api_get}

To get information on an service key, you can run:

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
:   ID value of the service key for which you want to get details.

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).


For example, to get information on an service key that is available in an instance in US South, you can run the following request:

```sh
curl  https://api.us-south.logging.cloud.ibm.com/v1/config/keys/123456789  -H "content-type: application/json"  -H "servicekey: xxxxxxxxx"
```
{: pre}

### Create a key
{: #service_keys_api_create}

```sh
curl -X POST  https://API_ENDPOINT/v1/config/keys?type="service"
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
{: #service_keys_api_update}

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
:   ID value of the service key for which you want to get details.

`KEY_NAME`
:   Name that you want to give the key. The maximum size of a name is 30 characters.


### Delete a key
{: #service_keys_api_delete}

To delete an service key, run the following command.

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
:   ID value of the service key to be deleted.

`SERVICE_KEY`
:   Service key value. A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).




## Rotating the service key by using the API
{: #service_keys_replace_api}
{: api}

If the service key is compromised or you have a policy that requies renewal of a key after a number of days, you can generate a new key and delete the old one.


To rotate a key, complete the following steps:

1. Get the details of the key that you want to rotate.

    You can list all service keys to obtain the ID of the key that you want to rotate. For more information, see [Listing all service keys](#service_keys_api_list).

    If you know the Key ID, skip to the next step.

2. Create a new key. For more information, see [Creating an service key](#service_keys_api_create).

3. Delete the old key. Make sure you use the ID of the key that you identified previously. For more information, see [Deleting a key](#service_keys_api_delete).

4. After you rotate the service key, you must update any operation processes where the service key is used with the new value.
{: important}
