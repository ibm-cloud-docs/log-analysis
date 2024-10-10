---

copyright:
  years:  2022, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, api, category, categories

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Managing categories programmatically
{: #config_categories}

You can use the *Configuration REST API* to programmatically manage categories. Categories are used to group views, boards, or screens.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

- You can use the **POST** method to create new categories.
- You can use the **GET** method to list defined categories.

Before you run any automated tasks, consider doing a back up of your account configuration resources. You can use the back up to restore the resources, to the state before any change is applied, if you encounter problems. See [Export the configuration of resources in a logging instance](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions#export_config_res).
{: tip}


## API methods
{: #config_categories_methods}

The following table outlines the actions that you can run to manage categories programmatically:

| Action                                         | Request  | URL                                  |
| -----------------------------------------------|----------|--------------------------------------|
| List all categories for a given type           | `GET`    | `<ENDPOINT>/v1/config/categories/<TYPE>` |
| Create a new category for a given type         | `POST`   | `<ENDPOINT>/v1/config/categories/<TYPE>`          |
| Get information about a category               | `GET`    | `<ENDPOINT>/v1/config/categories/<TYPE>/<ID>` |
| Modify a catagory                              | `PUT`    | `<ENDPOINT>/v1/config/categories/<TYPE>/<ID>` |
| Delete a category                              | `DELETE` | `<ENDPOINT>/v1/config/categories/<TYPE>/<ID>` |
{: caption="Actions to manage categories" caption-side="top"}

Where `<TYPE>` defines the type of category. Valid values are `views`, `boards`, or `screens`.

## Endpoint URL
{: #config_categories_endpoint}

Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage categories  programmatically. For information about endpoints per region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).


## Authentication
{: #config_categories_authentication}

When you manage categories programmatically, you must use a service key. Authorization to the logging configuration API is enforced by using a service key.
{: note}

A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).

Use of the logging configuration REST API is done by adding a valid service key to the HTTP Authorization request header. You must pass the service key as a header parameter (`-H`) of your requests.

For example, in a cURL request, you must set the `content-type` header as follows:

```text
-H 'servicekey: <SERVICE_KEY>'
```
{: codeblock}


## Additional headers
{: #config_api_headers}

Some additional headers might be required to make successful requests to the API. Those additional headers are:

### content-type
{: #config-categories-headers-content-type}

Define the `Content-Type` header to make successful requests to the API. The `content-type` header specifies that the request body is in JSON format.
{: note}

You must pass the `content-type` in the header parameter (`-H`) of your requests.

For example, in a cURL request, you must set the `content-type` header as follows:

```text
-H 'content-type: application/json'
```
{: codeblock}



## Body parameters
{: #config_categories_parm}

The following field is body parameter that you can set in the API request:

### name (string)
{: #config-categories-parm-name}

Specifies the name of the category to be created.

The following table indicates when the `name` parameter is required:

| Action                                                                | Request  | Field required                       |
| ----------------------------------------------------------------------|----------|--------------------------------------|
| Create a new category for a given type.                          | `POST`   | ![Check mark icon](../images/checkmark-icon.svg "Check mark icon indicating required")|
| Modify a category | `UPDATE`    | ![Check mark icon](../images/checkmark-icon.svg "Check mark icon indicating required")|
{: caption="Required status per method" caption-side="top"}


## Examples of using the categories configuration API
{: #config-categories-samples}

The following are examples of how to use the categories configuration API.

In these examples, `<SERVICE_KEY>` is the [service key](/docs/log-analysis?topic=log-analysis-service_keys) for your {{site.data.keyword.la_short}} instance.

### Creating a category for boards
{: #config-categories-create-category-boards}

The following sample creates a new category for boards named `My new category`.

```text
curl POST https://api.us-south.logging.cloud.ibm.com/v1/config/categories/boards \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
  -d '{"name": "My new category"}'
```
{: pre}

### Listing all defined categories for views
{: #config-categories-list-category-views}

The following sample lists all defined categories for views.

```text
curl GET https://api.us-south.logging.cloud.ibm.com/v1/config/categories/views \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
```
{: pre}

### Deleting a category
{: #config-categories-delete-category-boards}

The following sample deletes a category.

```text
curl DELETE https://api.us-south.logging.cloud.ibm.com/v1/config/categories/views/xxxxxxxxxx \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
```
{: pre}



### Changing the name of a category
{: #config-categories-update-category-boards}

The following sample gets information about a category.

```text
curl GET https://api.us-south.logging.cloud.ibm.com/v1/config/categories/views/xxxxxxxxxx \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
  -d '{"name": "My new category name"}
```
{: pre}



### Getting details about a category
{: #config-categories-get-category-boards}


The following sample gets information about a category.

```text
curl GET https://api.us-south.logging.cloud.ibm.com/v1/config/categories/views/xxxxxxxxxx \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
```
{: pre}
