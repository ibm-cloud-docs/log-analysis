---

copyright:
  years: 2019, 2022
lastupdated: "2021-11-24"

keywords: IBM Cloud, Log Analysis, api

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Managing presets programmatically 
{: #preset-api}

You can use the *Configuration REST API* to manage presets programmatically.  
{: shortdesc}

Presets are templates that can be used to quickly configure alerts.  Presets can also be configured through the [UI](/docs/log-analysis?topic=log-analysis-preset_ui).

- You can use the **POST** method to create preset.
- You can use the **GET** method to get information about presets configured in the instance.
- You can use the **PUT** method to modify a preset.
- You can use the **DELETE** method to delete a preset.

Before you run any automated tasks, consider doing a back up of your account configuration resources. You can use the back up to restore the resources, to the state before any change is applied, if you encounter problems. See [Export the configuration of resources in a logging instance](/docs/log-analysis?topic=log-analysis-reuse_resource_definitions#export_config_res).
{: tip}


## API methods
{: #preset-api-methods}

The following table outlines the actions that you can run to configure presets programmatically:

| Action                                                                  | Request  | URL                                  |
| ------------------------------------------------------------------------|----------|--------------------------------------|
| Create a preset                            | `POST`   | `<ENDPOINT>/v1/config/presetalert`          |
| Get all configured presets                            | `GET`   | `<ENDPOINT>/v1/config/presetalert`          |
| Get information about a specific preset                            | `GET`   | `<ENDPOINT>/v1/config/presetalert/<PRESET_ID>`          |
| Modify an existing preset   | `PUT`    | `<ENDPOINT>/v1/config/presetalert/<PRESET_ID>` |
| Delete a preset                               | `DELETE` | `<ENDPOINT>/v1/config/presetalert/<PRESET_ID>` |
{: caption="Table 1. Preset configuration API endpoints" caption-side="top"}

Where `<PRESET_ID>` is the ID of a preset.

## Endpoint URL
{: #preset-api-endpoint}

Depending on [your account settings](/docs/account?topic=account-service-endpoints-overview), you can use public or private endpoints to manage presets programmatically. For information about endpoints for each region, see [API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api).


## Authentication
{: #preset-api-authentication}

When you manage presets programmatically, you must use a service key. Authorization to the Configuration API is enforced by using a service key.
{: note} 

A service key is a unique code that is passed in an API request to identify the calling application or user. The service key is specific to a logging instance. For more information on how to generate a service key, see [Managing service keys](/docs/log-analysis?topic=log-analysis-service_keys).

Use of the Configuration REST API is done by adding a valid service key to the HTTP Authorization request header. You must pass the service key as a header parameter (`-H`) on your requests.

For example, in a cURL request, you must set the `servicekey` header as follows:

```text
-H "servicekey: <SERVICE_KEY>"
```
{: codeblock}


## Additional headers 
{: #preset-api-headers}

Some additional headers might be required to make successful requests to the API. Those additional headers are:

### content-type
{: #preset-api-headers-content-type}

Define the `Content-Type` header to make successful requests to the API. The `content-type` header specifies that the request body is in JSON format.
{: note}

You must pass the `content-type` in the header parameter (`-H`) of your requests.

For example, in a cURL request, you must set the `content-type` header as follows:

```text
-H "content-type: application/json"
```
{: codeblock}



## Body parameters
{: #preset-api-parm}

The following fields are body parameters that you can set in the API request:

### name (string)
{: #preset-api-parm-name}

Specifies the name of the view.

The following table indicates when the `name` parameter is required:

| Action                                                                | Request  | Field required                       |
| ----------------------------------------------------------------------|----------|--------------------------------------|
| Create a preset                          | `POST`   | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating required")|
| Modify an existing preset | `PUT`    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating required")|
| Get preset information                           | `GET`   | |
| Delete a preset                              | `DELETE` |  |
{: caption="Table 2. Required status per method" caption-side="top"}


### channels (array of objects)
{: #presetalert-api-parm-channels}

Specifies the notification channels configuration associated with the preset.  

The following values can be specifed for all `channels`.

| Value | Description | 
|--------------------------|------|
| `integration` | The integration type.  Valid values are: `slack`, `email`, `webhook`, `pagerduty`, `pagerduty-auto-resolve`, and `sysdig`. |
| `immediate` | Specified if the alert is sent immediately after the line criteria is met (`"immediate": true`) or after the line and time criteria is met (`"immediate": false`). |
| `triggerlimit` | The number of matching log lines to trigger the alert. |
| `triggerinterval` | The amount of time to look for the number of matching log lines.  \n Only following `triggerinterval` values are valid:  \n * `30` - 30 seconds  \n * `1m` - 1 minute  \n * `5m` - 5 minutes  \n * `30m` - 30 minutes  \n * `1h` - 1 hour  \n * `6h` - 6 hours  \n * `12h` - 12 hours  \n * `24h` - 24 hours|
| `operator` | Specifies whether the alert is triggered when the condition exists (`presence`) or when it does not exist (`absence`).|
| `blackout` | (Optional) Specifies the time period when the alert would be active. |
{: caption="Channel configuration values for all preset types" caption-side="top"}

The following is an example `blackout` definition specifying that the alert is active Monday through Friday from 8:00 AM to 5:00 PM in (GMT-05:00) America/New York.

```json
blackout": {
   "enabled": true,    A 
   "times": {
       "enabled": true,
       "periods": [
           [
               "17:00",
               "08:00"
           ]
       ]
   },
   "days": [
       "0",
       "6"
   ],
   "timezone": "America/New_York"
}
```
{: codeblock}

The following values are only valid for the specified preset type:

| Value | Description | 
|--------------------------|------|
| `emails` | The email addresses where the alert will be sent. |
| `timezone` | (Optional) The preferred timezone. |
{: caption="Channel configuration values for email presets" caption-side="top"}
{: #end-api-img-1}
{: tab-title="Email"}
{: tab-group="preset_channels1"}
{: class="simple-tab-table"}

| Value | Description | 
|--------------------------|------|
| `key` | The PagerDuty key associated with the integration.  This is obtained by [configuring PagerDuty through the UI](/docs/activity-tracker?topic=activity-tracker-preset_ui) and then using the [`GET` all configured presets](#preset-api-get-all) method to return the `key` value for the preset. |
{: caption="Channel configuration values for PagerDuty) presets" caption-side="top"}
{: #end-api-img-2}
{: tab-title="PagerDuty"}
{: tab-group="preset_channels1"}
{: class="simple-tab-table"}

| Value | Description | 
|--------------------------|------|
| `url` | The URL of your Slack webhook |
| `color` | The color your alert is displayed in Slack. For example, `#d4b135`. |
{: caption="Channel configuration values for Slack presets" caption-side="top"}
{: #end-api-img-3}
{: tab-title="Slack"}
{: tab-group="preset_channels1"}
{: class="simple-tab-table"}

| Value | Description | 
|--------------------------|------|
| `key` | Your API key. |
| `severity` | The severity level associated with the alert.  For example, `high`. |
| `url` | The URL of your {{site.data.keyword.mon_full_notm}} instance. |
{: caption="Channel configuration values for Sysdig (IBM Cloud Monitoring) presets" caption-side="top"}
{: #end-api-img-4}
{: tab-title="Sysdig (IBM Cloud Monitoring)"}
{: tab-group="preset_channels2"}
{: class="simple-tab-table"}

| Value | Description | 
|--------------------------|------|
| `bodyTemplate`| The JSON body to be passed to the Webhook. |
| `url` | The Webhook URL to receive the alert. |
{: caption="Channel configuration values for Webhook presets" caption-side="top"}
{: #end-api-img-5}
{: tab-title="Webhook"}
{: tab-group="preset_channels2"}
{: class="simple-tab-table"}

Examples of `channels` values can be obtained by [creating presets in the UI](/docs/activity-tracker?topic=activity-tracker-preset_ui) and then using the [`GET` all configured presets](#preset-api-get-all) method to return the `channels` values for the preset.

## Examples of using the preset configuration API
{: #preset-api-samples}

The following are examples of how to use the preset configuration API.

In these examples, `<SERVICE_KEY>` is the [service key](/docs/log-analysis?topic=log-analysis-service_keys) for your {{site.data.keyword.at_full_notm}} instance. 

### Creating a preset
{: #preset-api-create-view}

The following sample creates a preset.

```text
curl --request POST https://api.us-south.logging.cloud.ibm.com/v1/config/presetalert \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -H "servicekey: <SERVICE_KEY>" \
     -d '{ "name": "My preset", "channels": ["<CHANNEL>"] }'
```
{: pre}

A response similar to the following will be returned:

```text
{"name":"Send by email","channels":[{"integration":"email","immediate":false,"terminal":true,"triggerlimit":1,"triggerinterval":30,"operator":"presence","emails":"AnotherUser@mycompany.com","alertid":"719a919782"}],"presetid":"8485dcf363"}
```
{: screen}

### Get all configured presets
{: #preset-api-get-all}

The following sample gets all configured presets for the instance.

```text
curl --request GET https://api.us-south.logging.cloud.ibm.com/v1/config/presetalert \
     -H "Accept: application/json" \
     -H "servicekey: <SERVICE_KEY>"  
```
{: pre}

A response similar to the following will be returned:

```text
[{"channels":[{"integration":"email","immediate":false,"terminal":true,"triggerlimit":1,"triggerinterval":"30","operator":"presence","emails":["MyUser@mycompany.com"],"alertid":"4991f78d6d"}],"presetid":"291a4100b0","account":"090bba4d47","name":"Email preset","_created":"2021-11-18T15:15:53.414Z","_modified":"2021-11-18T15:15:53.414Z"},{"channels":[{"integration":"email","alertid":"be14de8671","immediate":false,"terminal":true,"triggerlimit":1,"triggerinterval":"30","operator":"presence","emails":["MyUser@mycompany.com"]},{"integration":"email","alertid":"398bec1582","immediate":false,"terminal":true,"triggerlimit":1,"triggerinterval":"15m","operator":"absence","emails":["MyUser@mycompany.com"]},{"integration":"webhook","immediate":false,"terminal":true,"triggerlimit":1,"triggerinterval":"30","operator":"presence","bodyTemplate":"{\n\"name\": \"{{ name}}\",\n\"sentFrom\": \"logDNA\"\n}","url":"https://mycompany.domain.com/webhook/endpoint","alertid":"56dbdca8e7"}],"presetid":"e0f24d3ebf","account":"090bba4d47","name":"Email preset with 2 notifications","_created":"2021-11-18T15:16:50.376Z","_modified":"2021-11-18T15:16:50.376Z"}]
```
{: screen}


### Get information about a specific preset
{: #preset-api-get}

The following sample gets information about a specific preset.

```text
curl --request GET https://api.us-south.logging.cloud.ibm.com/v1/config/presetalert/<PRESET_ID> \
     -H "Accept: application/json"
     -H "servicekey: <SERVICE_KEY>"  
```
{: pre}

Where `<PRESET_ID>` is the `presetid` value returned when [running the `GET` method to return all presets.](#preset-api-get-all)

A response similar to the following will be returned:

```text
{"channels":[{"integration":"email","immediate":false,"terminal":true,"triggerlimit":1,"triggerinterval":"30","operator":"presence","emails":["MyUser@mycompany.com"],"alertid":"4991f78d6d"}],"presetid":"291a4100b0","account":"090bba4d47","name":"Email preset","_created":"2021-11-18T15:15:53.414Z","_modified":"2021-11-18T15:15:53.414Z"}
```
{: screen}


### Modifying a preset
{: #preset-api-put}

The following modifies a view by adding an alert.

```text
curl --request PUT https://api.us-south.logging.cloud.ibm.com/v1/config/presetalert/<PRESET_ID> \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -H "servicekey: <SERVICE_KEY>" \
     -d '{ "name": "My preset", "channels": ["<CHANNEL>"] }'
```
{: pre}

Where `<PRESET_ID>` is the `presetid` value returned when [running the `GET` method to return all presets.](#preset-api-get-all)

A response similar to the following is returned:

```text
{"name":"Send by email","channels":[{"integration":"email","immediate":false,"terminal":true,"triggerlimit":1,"triggerinterval":30,"operator":"presence","emails":"AnotherUser@mycompany.com","alertid":"6043b60788"}],"presetid":"291a4100b0"}
```
{: screen}

If the `<PRESET_ID>` does not exist, the following is returned:

```text
{"error":"Resource Not Found","code":"NotFound","status":"error"}
```
{: screen}


### Deleting a preset
{: #preset-api-delete}

The following sample deletes a preset.

```text
curl --request DELETE https://api.us-south.logging.cloud.ibm.com/v1/config/presetalert/<PRESET_ID> \
     -H "Accept: application/json" \
     -H "servicekey: <SERVICE_KEY>"  \
```  
{: pre}

Where `<PRESET_ID>` is the `presetid` value returned when [running the `GET` method to return all presets.](#preset-api-get-all)

The following response will be returned when the preset is successfully deleted:

```text
{"deleted":true}
```
{: screen}

If the `<PRESET_ID>` does not exist, the following is returned:

```text
{"error":"Resource Not Found","code":"NotFound","status":"error"}
```
{: screen}


