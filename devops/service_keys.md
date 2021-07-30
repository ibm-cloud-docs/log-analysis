---

copyright:
  years:  2018, 2021
lastupdated: "2021-07-30"

keywords: IBM, Log Analysis, logging, service keys

subcollection: log-analysis

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
{:external: target="_blank" .external}
 
# Managing service keys
{: #service_keys}

In an {{site.data.keyword.la_full_notm}} instance you can create, delete, and view service keys using the UI.  You can also create and view service keys using the CLI and API.

A service key is a unique code that is passed in an API request to identify the calling application or user. 

You must use a service key to complete any of the following tasks:
- Export data programmatically 
- Manage views and alerts programmatically by using the Configuration API or Terraform.

Only users that have **manager** role for the {{site.data.keyword.la_full_notm}} service, can manage service keys in an auditing instance.

You can enable a maximum of 20 service keys for each auditing instance.  To create more than one service key, you have to add additional service keys using the UI.  You can only create one service key using the API or CLI.
{: important}

If a service key does not exist, the first API command sent to {{site.data.keyword.la_full}} will automatically generate a service key.
{: note}
 
## Managing service keys by using the UI
{: #service_keys_ui}

You can create, delete, and view service keys using the logging UI.

### Creating a service key by using the UI
{: #service_keys_create}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).
  
Complete the following steps to create a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Select the **Configuration** icon ![Configuration icon](../images/admin.png). 

3. Select **Organization**. 

4. Select **API keys**.

   If you have the correct permissions, the available service keys are displayed in the **Service Keys** section.   

4. Click **Generate Service Key**. A new key is added to the list. 



### Deleting a service key by using the UI
{: #service_keys_delete}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

You can only delete a service Key through the logging web UI.
{: important}

Complete the following steps to delete a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Select the **Configuration** icon ![Configuration icon](../images/admin.png). 

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

2. Select the **Configuration** icon ![Configuration icon](../images/admin.png). 

3. Select **Organization**. 

3. Select **API keys**.

   If you have the correct permissions, the available service keys are displayed in the **Service Keys** section.   


## Managing a service key by using the CLI
{: #service_keys_cli}

You can create and view service keys using the {{site.data.keyword.cloud_notm}} CLI.

### Getting the service key by using the CLI
{: #service_keys_cli_get}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

To get the service key through the command line, complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the logging instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the auditing instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```
    ibmcloud resource service-instances
    ```
    {: pre}

5. Get the name of the key that is associated with the auditing instance. Run the [ibmcloud resource service-keys](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) command:

    ```
    ibmcloud resource service-keys --instance-name <INSTANCE_NAME>
    ```
    {: pre}

    where INSTANCE_NAME is the name of the instance that you obtained in the previous step.

6. Get the service key. Run the [ibmcloud resource service-key](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) command:

    ```
    ibmcloud resource service-key <KEY_NAME>
    ```
    {: pre}

    where KEY_NAME is the name of the key obtained in the previous step.
 
    The output from this command includes the field **service_key** that contains a service key for the instance.  If no service key has been created for the instance, or, if you do not have **manager** access, no service key will be returned.

### Creating a service key by using the CLI
{: #service_keys_cli_create}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

Only a single service key can be created using the CLI.  Using these commands to create a service key where one already exists will not create a new key.  If you need to create more than one service key, use the [UI](#service_keys_ui).
{: important}

To create a service key for a logging instance through the command line, complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the logging instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the logging instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```
    ibmcloud resource service-instances
    ```
    {: pre}

5. Create the service key. Run the [ibmcloud resource service-key-create](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create) command:

    ```
    ibmcloud resource service-key-create <NAME> --instance-name <SERVICE_INSTANCE>

    ```
    {: pre}

    Where NAME is the desired name of the service key and SERVICE_INSTANCE is the name of the service instance from the previous step.
 
    The output from this command includes the field **service_key** that contains the service key for the instance.


## Managing a service key by using the API
{: #service_keys_api}

You can create and view service keys using the {{site.data.keyword.cloud_notm}} API.

### Getting the service key by using the API
{: #service_keys_api_get}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

To get the service key through the API, complete the following steps:

1.  Get the GUID of the service instance if you do not already have it.

    - [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

    - Log in to the region in the {{site.data.keyword.cloud_notm}} where the logging instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

    - Set the resource group where the auditing instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

        By default, the `default` resource group is set.

    - Get the instance name. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

        ```
        ibmcloud resource service-instances
        ```
        {: pre}

    - Get the GUID that is associated with the auditing instance. Run the [ibmcloud resource service-instance](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance) command:

       ```
       ibmcloud resource service-instance <INSTANCE_NAME>
       ```
       {: pre}

       Where INSTANCE_NAME is the name of the instance that you obtained in the previous step.  Make note of the GUID value which will be used in the API.

2. Get an access token. 

    You need an IAM access token to authenticate in {{site.data.keyword.cloud_notm}}.

    To generate an IAM access token, run the following command:

    ```
    export ACCESS_TOKEN=`ibmcloud iam oauth-tokens | grep IAM | cut -d \: -f 2 | sed 's/^ *//'`
    ```
    {: pre}

    The access token is only valid for 1 hour. ACCESS_TOKEN includes the string "Bearer" followed by the IAM token.

3. [Get the service key](https://cloud.ibm.com/apidocs/resource-controller/resource-controller#get-resource-key). Run the following cURL command:

    ```shell
    curl -X GET https://resource-controller.cloud.ibm.com/v2/resource_keys/<GUID> -H "Authorization: $ACCESS_TOKEN" -H "content-type: application/json"
    ```
    {: codeblock}

    Where GUID is the GUID obtained in the first step.


### Creating a service key
{: #service_keys_api_create}

You must have the **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

For more information, see [service roles](/docs/log-analysis?topic=log-analysis-iam#service).

Only a single service key can be created using the API.  Using the API to create a service key where one already exists will not create a new key.  If you need to create more than one service key, use the [UI](#service_keys_ui).
{: important}

To create the service key through the API, complete the following steps:

1.  Get the GUID of the service instance if you do not already have it.

    - [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

    - Log in to the region in the {{site.data.keyword.cloud_notm}} where the logging instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

    - Set the resource group where the auditing instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target) 
        
        By default, the `default` resource group is set.

    - Get the instance name. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

        ```
        ibmcloud resource service-instances
        ```
        {: pre}

    - Get the GUID that is associated with the auditing instance. Run the [ibmcloud resource service-instance](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance) command:

       ```
       ibmcloud resource service-instance <INSTANCE_NAME>
       ```
       {: pre}

       Where INSTANCE_NAME is the name of the instance that you obtained in the previous step.  Make note of the GUID value which will be used in the API.

2. Get an access token. 

    You need an IAM access token to authenticate in {{site.data.keyword.cloud_notm}}.

    To generate an IAM access token, run the following command:

    ```
    export ACCESS_TOKEN=`ibmcloud iam oauth-tokens | grep IAM | cut -d \: -f 2 | sed 's/^ *//'`
    ```
    {: pre}

    The access token is only valid for 1 hour.  ACCESS_TOKEN includes the string "Bearer" followed by the IAM token.

3. [Create the service key](https://cloud.ibm.com/apidocs/resource-controller/resource-controller#post-resource-key). Run the following cURL command:

    ```shell
    curl -X POST https://resource-controller.cloud.ibm.com/v2/resource_keys -H "Authorization: $ACCESS_TOKEN" -H "content-type: application/json" -d '{"name":"<NAME>", "source":"<GUID>"}'
    ```
    {: codeblock}

    Where NAME is the name to be given to the service key and GUID is the GUID obtained in the first step.  

