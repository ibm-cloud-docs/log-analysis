---

copyright:
  years:  2018, 2021
lastupdated: "2021-07-30"

keywords: IBM, Log Analysis, logging, service keys

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}
 
# Managing service keys
{: #service_keys}

In an {{site.data.keyword.la_full_notm}} instance you can create, delete, and view logging service keys by using the UI.  You can also create and view logging service keys by using the CLI and API.

A logging service key is a unique code that is passed in an API request to identify the calling application or user. 

You must use a logging service key to complete any of the following tasks:
- Export data programmatically 
- Manage views and alerts programmatically by using the Configuration API or Terraform.

You can enable a maximum of 20 logging service keys for each logging instance.  To create more than one service key, you have to add additional logging service keys by using the UI.  You can only create one service key using the API or CLI.
{: important}

If a logging service key does not exist, the first API command sent to {{site.data.keyword.la_full_notm}} will automatically generate a service key.
{: note}


 
## Prereqs. Check your IAM permissions to manage service keys
{: #service_keys_prereq}

To generate a new service key or get an existing service key, you need the following roles on the {{site.data.keyword.la_full_notm}}:
- Platform role `operator`, `editor` or `administrator`
- Service role `Manager`

To restrict access to a service key, you need the following role on the `IAM Identity Service service`:
- Platform role `Administrator`



## Managing service keys by using the UI
{: #service_keys_ui}

You can create, delete, and view service keys using the logging UI.

### Creating a service key by using the logging UI
{: #service_keys_create}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).
  
Complete the following steps to create a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

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

You can only delete a service Key through the logging web UI.
{: important}

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


## Managing a logging service key by using the CLI
{: #service_keys_cli}

You can create and view logging service keys by using the {{site.data.keyword.cloud_notm}} CLI.

### Creating a service key by using the CLI
{: #service_keys_cli_create}

Only a single service key can be created using the CLI.  Using these commands to create a service key where one already exists will not create a new key.  If you need to create more than one service key, use the [UI](#service_keys_ui).
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

3. Set the resource group where the auditing instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```text
    ibmcloud resource service-instances
    ```
    {: pre}

5. Get the name of the key that is associated with the auditing instance. Run the [ibmcloud resource service-keys](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) command:

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

You can create and view service keys using the {{site.data.keyword.cloud_notm}} API.


### Creating a service key by using the API
{: #service_keys_api_create}

Only a single logging service key can be created using the API.  Using the API to create a service key where one already exists will not create a new key.  If you need to create more than one service key, use the [UI](#service_keys_ui).
{: important}

To create the logging service key through the API, complete the following steps:

1. [Prereq] Generate an [{{site.data.keyword.cloud_notm}} API key](/docs/account?topic=account-userapikey&interface=api#create_user_key).

2. Get an access token. For more information, see [Generating an {{site.data.keyword.cloud_notm}} IAM token by using an API key](/docs/account?topic=account-iamtoken_from_apikey&interface=api).

    You need an IAM access token to authenticate in {{site.data.keyword.cloud_notm}}.

    To generate an IAM access token, run the following command:

    ```text
    curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=MY_APIKEY'
    ```
    {: pre}

    Replace `MY_APIKEY` with your API key from the previous step.

    The access token is only valid for 1 hour. `access_token` includes the string "Bearer" followed by the access token.

3. Get the name and GUID of the service instance if you do not already have it.

    Get the list of resource instances:

    ```text
    curl -X GET   https://resource-controller.cloud.ibm.com/v2/resource_instances   -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```
    {: pre}

    Look for the `guid` field of the instance to get the instance GUID.

4. [Create the {{site.data.keyword.cloud_notm}} resource service key](https://cloud.ibm.com/apidocs/resource-controller/resource-controller#post-resource-key). Run the following cURL command:

    ```text
    curl -X POST https://resource-controller.cloud.ibm.com/v2/resource_keys -H "Authorization: <ACCESS_TOKEN> -H "content-type: application/json" -d '{"name":"<NAME>", "source":"<LOGGING_INSTANCE_GUID>"}'
    ```
    {: codeblock}

    Where `NAME` is the name to be given to the IAM service key and GUID is the logging instance GUID obtained in the previous step.  

5. Add a policy on the service ID that is associated with the service key. For more information, see [Create a policy](/apidocs/iam-policy-management#create-policy).

Consider deleting the service key. There is a limit on the number of service IDs per account. For more information, see [IBM Cloud IAM limits](/docs/account?topic=account-known-issues&interface=cli#iam_limits).
{: tip}

To delete an {{site.data.keyword.cloud_notm}} resource service key, run the following command:

```text
curl -X DELETE https://resource-controller.cloud.ibm.com/v2/resource_keys/<IAM_SERVICE_KEY_GUID> -H "Authorization: $ACCESS_TOKEN" -H "content-type: application/json"
```
{: pre}



### Getting the service key by using the API
{: #service_keys_api_get}

Make sure you use a recent resource service key in this step. Do not use the instance's resource service key that has a suffix of `key-Administrator`.
{: note}

To get the service key through the API, complete the following steps:

1. [Prereq] Generate an [{{site.data.keyword.cloud_notm}} API key](/docs/account?topic=account-userapikey&interface=api#create_user_key). 

2. Get an access token. For more information, see [Generating an {{site.data.keyword.cloud_notm}} IAM token by using an API key](/docs/account?topic=account-iamtoken_from_apikey&interface=api).

    You need an IAM access token to authenticate in {{site.data.keyword.cloud_notm}}.

    To generate an IAM access token, run the following command:

    ```text
    curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=MY_APIKEY'
    ```
    {: pre}

    Replace `MY_APIKEY` with your API key from the previous step.

    The access token is only valid for 1 hour. `access_token` includes the string "Bearer" followed by the IAM token.

3. Get the GUID of an IAM service key.

    Get the list of resource keys:

    ```text
    curl -X GET   https://resource-controller.cloud.ibm.com/v2/resource_keys   -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```
    {: pre}

    Look for the `guid` field.

4. [Get the logging resource service key](https://cloud.ibm.com/apidocs/resource-controller/resource-controller#get-resource-key). Run the following cURL command:

    ```shell
    curl -X GET https://resource-controller.cloud.ibm.com/v2/resource_keys/<GUID> -H "Authorization: <ACCESS_TOKEN>" -H "content-type: application/json"
    ```
    {: codeblock}

    Where `GUID` is the GUID obtained in the previous step.

