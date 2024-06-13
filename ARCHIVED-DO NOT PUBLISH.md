


FROM service_keys.md

## Managing a service key by using the API
{: #service_keys_api}

You can create and view service keys using the {{site.data.keyword.cloud_notm}} API.




### Creating a service key by using the API
{: #service_keys_api_create}


This section needs to be archived and replaced withthe create key instructions using create key method
{: note}

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




Archive thios section and replace with : 1 using the List keys method (this method allows the user to get all keys of type service), 1 section on the Get key method (this method requres the user to know the id)
{: note}

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

