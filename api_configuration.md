---

copyright:
  years: 2019, 2020
lastupdated: "2020-12-09"

keywords: IBM Cloud, LogDNA, Log Analysis

subcollection: Log-Analysis-with-LogDNA

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

# Managing views programmatically
{: #api_configuration}

You can use the *Configuration REST API* to programmatically manage views and alerts. For details on the LogDNA Configuration API and its parameters, see the [LogDNA documentation](https://docs.logdna.com/reference#getting-started-with-the-configuration-api).
{:shortdesc}

- You can use the **POST** method to create a view, or create a view and attach an alert to it.
- You can use the **PUT** method to modify an existing view, and alerts that are attached to views.
- You can use the **DELETE** method to delete a view and associated alerts.

When using the **POST** method, the `name` parameter is always required.  The `name` parameter defines the name of the new view.

When using the **PUT** method, you must specify the `name` and `viewid`.  In these examples, replace `<VIEWID>` with the ID returned when you created your view.

For the **DELETE** method, you must specify the `viewid` of the view to be deleted.

## Authentication
{: #api_configuration-authentication}

The LogDNA Configuration API uses a service key in the header to provide authentication. HTTP headers are the part of the API request and response that contain the meta-data associated with the API request and response.

You can pass the service key in the header parameter (`-H`) of your requests. Alternatively, you can pass service key in the username element (`-u`) of the request and leave the password value blank or empty.
{: note}

In these examples `<SERVICE_KEY>` is the [service key](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-service_keys) for your {{site.data.keyword.la_full_notm}} instance. 

## Configuration API endpoints
{: #api_configuration-endpoints}

There are two types of LogDNA Configuration API endpoints: public and private.

### Public API endpoints
{: #api_configuration-endpoints-public}

The following table shows the LogDNA public API endpoints:

| Region                   |  Public Endpoint                                   |
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `https://api.in-che.logging.cloud.ibm.com/v1/config/view`       |
| `Dallas (us-south)`      | `https://api.us-south.logging.cloud.ibm.com/v1/config/view`       |
| `Frankfurt (eu-de)`      | `https://api.eu-de.logging.cloud.ibm.com/v1/config/view`          |
| `London (eu-gb)`         | `https://api.eu-gb.logging.cloud.ibm.com/v1/config/view`          |
| `Tokyo (jp-tok)`         | `https://api.jp-tok.logging.cloud.ibm.com/v1/config/view`         |
| `Seoul (kr-seo)`         | `https://api.kr-seo.logging.cloud.ibm.com/v1/config/view`         |
| `Sydney (au-syd)`        | `https://api.au-syd.logging.cloud.ibm.com/v1/config/view`         |
| `Washington (us-east)`   | `https://api.us-east.logging.cloud.ibm.com/v1/config/view`         |
{: caption="Table 1. LogDNA public API endpoints" caption-side="top"}

### Private API endpoints
{: #api_configuration-endpoints-private}

The following table shows the LogDNA private API endpoints:

| Region                   |  Private Endpoint                                   |
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `https://api.private.in-che.logging.cloud.ibm.com/v1/config/view`       |
| `Dallas (us-south)`      | `https://api.private.us-south.logging.cloud.ibm.com/v1/config/view`       |
| `Frankfurt (eu-de)`      | `https://api.private.eu-de.logging.cloud.ibm.com/v1/config/view`          |
| `London (eu-gb)`         | `https://api.private.eu-gb.logging.cloud.ibm.com/v1/config/view`          |
| `Tokyo (jp-tok)`         | `https://api.private.jp-tok.logging.cloud.ibm.com/v1/config/view`         |
| `Seoul (kr-seo)`         | `https://api.private.kr-seo.logging.cloud.ibm.com/v1/config/view`         |
| `Sydney (au-syd)`        | `https://api.private.au-syd.logging.cloud.ibm.com/v1/config/view`         |
| `Washington (us-east)`   | `https://api.private.us-east.logging.cloud.ibm.com/v1/config/view`         |
{: caption="Table 2. LogDNA private API endpoints" caption-side="top"}

## Examples of using the LogDNA Configuration API
{: #api_configuration-samples}

The following are examples of how to use the LogDNA Configuration API.

A category must exist before you create a view.  In these examples replace `<MY_CATEGORY>` with your category. 
{: note}

### Creating a view
{: #api_configuration-create-view}

The following creates a view.

```
curl https://api.us-south.logging.cloud.ibm.com/v1/config/view \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
  -d '{
  "name": "My RC 200",
  "query": "reason.reasonCode:200",
  "hosts": ["ibm-cloud-databases-prod"],
  "apps": ["N/A"],
  "levels": ["normal"],
  "tags": ["N/A"],
  "category": ["<MY_CATEGORY>"]
}'
```
{: pre}

A response similar to the following will be returned:

```
{"name":"My RC 200","query":"reason.reasonCode:200","hosts":["ibm-cloud-databases-prod"],"apps":["N/A"],"levels":["normal"],"tags":["N/A"],"category":["89610d13a7"],"viewid":"3c3de90460"}
```
{: screen}

### Creating a view and attaching an alert
{: #api_configuration-create-view-alert}

The following creates a view and associates an alert with the view.

```
curl https://api.logdna.com/v1/config/view \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
  -d '{
  "name": "My RC 200",
  "query": "reason.reasonCode:200",
  "hosts": ["host1", "host2"],
  "apps": ["apps1", "apps2"],
  "levels": ["error"],
  "tags": ["prod"],
  "category": ["<MY_CATEGORY>"],
  "channels": [
    {
      "integration": "email",
      "emails": ["user@mycompany.com"],
      "triggerlimit": 15,
      "triggerinterval": "5m",
      "immediate": true,
      "terminal": true,
      "operator": "presence",
      "timezone": "America/Los_Angeles"
    {
      "integration": "webhook",
      "url": "<YOUR_WEBHOOK_URL>",
      "triggerlimit": 25,
      "triggerinterval": "30",
      "operator": "presence",
      "immediate": true,
      "terminal": true,
      "method": "post",
      "headers": {
        "X-MY-HEADER": "My Header Value"
      },
      "bodyTemplate": {
        "my_log_lines": "{{ lines }}"
      }
    },
    {
      "integration": "pagerduty",
      "key": "<YOUR_PD_KEY>",
      "triggerlimit": 150,
      "triggerinterval": "15m",
      "operator": "absence",
      "immediate": false,
      "terminal": true
    }
  ]
}'
```
{: pre}

A response similar to the following will be returned:

```
{"name":"My RC 200","query":"reason.reasonCode:200","hosts":["ibm-cloud-databases-prod"],"apps":["N/A"],"levels":["normal"],"tags":["N/A"],"category":["89610d13a7"],"viewid":"3c3de90460"}
```
{: screen}

### Modifying a view

The following modifies a view.

```
curl --request PUT \
  --url https://api.us-south.logging.cloud.ibm.com/v1/config/view/<VIEWID> \
  --header 'Content-Type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' 
```
{: pre}

If the `viewid` you are trying to modify does not exist, a response similar to the following will be returned: 

```
{"error":"Nothing to configure","code":"BadRequest","status":"error"}
```
{: screen}

### Modifying a view by adding an alert
{: #api_configuration-mod-view-alert}

The following modifies a view by adding an alert.

```
curl --request PUT \
  --url https://api.us-south.logging.cloud.ibm.com/v1/config/view/<VIEWID> \
  --header 'Content-Type: application/json' \
  -H 'servicekey: <SERVICE_KEY>'  \
-d '{
  "name": "My RC 200",
  "query": "reason.reasonCode:200",
  "hosts": ["ibm-cloud-databases-prod"],
  "apps": ["N/A"],
  "levels": ["normal"],
  "tags": ["N/A"],
  "category": ["<CATEGORY"],
  "channels": [
    {
      "integration": "email",
      "emails": ["user@mycompany.com"],
      "triggerlimit": 15,
      "triggerinterval": "5m",
      "immediate": true,
      "terminal": true,
      "operator": "presence",
      "timezone": "Europe/London"
 }
  ]
}'
```
{: pre}

A response similar to the following is returned:

```
{"name":"My RC 200","query":"reason.reasonCode:200","hosts":["ibm-cloud-databases-prod"],"apps":["N/A"],"levels":["normal"],"tags":["N/A"],"category":["89610d13a7"],"channels":[{"integration":"email","emails":"user@mycompany.com","triggerlimit":15,"triggerinterval":300,"immediate":true,"terminal":true,"operator":"presence","timezone":"Europe/London","alertid":"<ALERTID>"}],"viewid":"<VIEWID>"}
```
{: screen}

If you modify a view so that the app is empty, a response similar to the following will be returned:

```
{"details":[{"message":"\"apps[0]\" is not allowed to be empty","key":"apps[0]"}],"error":"\"apps[0]\" is not allowed to be empty","code":"BadRequest","status":"error"}
```
{: screen}

### Modifying a view by changing the search query
{: #api_configuration-mod-view-query}

The following changes a view's search query.

```
curl https://api.us-south.logging.cloud.ibm.com/v1/config/view/<VIEWID> \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
  -d '{
  "name": "My View from API",
  "query": "logType:stderr",
  "hosts": ["ibm-cloud-databases-prod"],
  "apps": ["crn:v1:bluemix:public:databases-for-redis:us-south:a/<xxxxxxxxxxxx>:<xxxxxxx>::"],
  "levels": ["info"],
  "tags": ["script"],
  "category": ["<CATEGORY>"]
}'
```
{: pre}

A response similar to the following will be returned:

```
{"name":"My View from API","query":"logType:stderr","hosts":["ibm-cloud-databases-prod"],"apps":["crn:v1:bluemix:public:databases-for-redis:us-south:a/<xxxxxxxxxxxx>:<xxxxxxx>::"],"levels":["info"],"tags":["script"],"category":[],"viewid":"f7b46891df"}
```
{: screen}

### Deleting a view
{: #api_configuration-del-view}

The following deletes a view.

```
curl --request DELETE \
  --url https://api.us-south.logging.cloud.ibm.com/v1/config/view/<VIEWID> \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>'  \
```  
{: pre}

The following response will be returned when the view is successfully deleted:

```
{"deleted":true}
```
{: screen}
