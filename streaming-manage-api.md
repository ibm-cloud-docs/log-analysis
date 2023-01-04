---

copyright:
  years: 2019, 2023
lastupdated: "2022-07-21"

keywords: IBM Cloud, Log Analysis, streaming, API

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Managing streaming to {{site.data.keyword.messagehub}} by using the API
{: #streaming-manage-api}


{{site.data.keyword.la_full}} provides an API that you can use to configure streaming for an {{site.data.keyword.la_full_notm}} instance.
{: shortdesc}


## Get details of the streaming configuration
{: #streaming-api-get-conf}

Use [this method](https://{DomainName}/apidocs/log-analysis#get-v1-config-stream){: external} to get the details about an existing streaming configuration.

```text
curl --request GET https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
```
{: pre}

The response will be similar to the following:

```text
{"status":"active","brokers":["kafka-0.mh-svc1-0000.eu-de.containers.appdomain.cloud:9093","kafka-1.mh-sv2.eu-de.containers.appdomain.cloud:9093","kafka-2.mh-sv3.eu-de.containers.appdomain.cloud:9093"],"topic":"la-london-topic","user":"token"}
```
{: codeblock}


## Delete the streaming configuration
{: #streaming-api-delete-conf}

Use [this method](https://{DomainName}/apidocs/log-analysis#delete-v1-config-stream){: external} to delete an existing streaming configuration.

```text
curl --request DELETE https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
```
{: pre}

The response will be similar to the following if the configuration is successfully deleted:

```text
{"deleted":true}
```
{: codeblock}

If an incorrect service key was specified, a response similar to the following will be returned:

```text
{"error":"Service Key Validation Error: Invalid or deactivated servicekey","status":"error","code":"NotAuthorized"}
```
{: codeblock}

## Configure streaming
{: #streaming-api-conf}

Use [this method](https://{DomainName}/apidocs/log-analysis#post-v1-config-stream){: external} to create a streaming configuration.

```text
curl --request POST https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
 -d '{"brokers":["<BROKERS>"],"topic":"topic","user":"token","password":"<COS_SERVICE_CREDENTIAL_API_KEY>"}'
 ```
 {: pre}

The response will be similar to the following if the configuration is successfully configured:

 ```text
 {"status":"active","brokers":["kafka-0.mh-svc1-0000.eu-de.containers.appdomain.cloud:9093","kafka-1.mh-sv2.eu-de.containers.appdomain.cloud:9093","kafka-2.mh-sv3.eu-de.containers.appdomain.cloud:9093"],"topic":"la-london-topic","user":"token"}
 ```
 {: codeblock}

## Update the streaming configuration
{: #streaming-api-update-conf}

Use [this method](https://{DomainName}/apidocs/log-analysis#put-v1-config-stream){: external} to update a streaming configuration.

```text
curl --request PUT https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
 -d '{"brokers":["<BROKERS>"],"topic":"topic","user":"token","password":"<COS_SERVICE_CREDENTIAL_API_KEY>"}'
```
{: pre}

The response will be similar to the following if the configuration is successfully updated:

 ```text
{"status":"active","brokers":["kafka-0.mh-svc1-0000.eu-de.containers.appdomain.cloud:9093","kafka-1.mh-sv2.eu-de.containers.appdomain.cloud:9093","kafka-2.mh-sv3.eu-de.containers.appdomain.cloud:9093"],"topic":"la-london-topic","user":"token"}
 ```
 {: codeblock}

If streaming is not configured, the following will be returned when trying to do an update:

```text
{"error":"Streaming configuration does not exist","code":"NotFound","status":"error"}
```
{: codeblock}

## Check the status of a streaming configuration
{: #streaming-api-conf-status}

To check if streaming is enabled or disabled, you can use either the GET or PUT methods.

When streaming is not enabled, the following is returned when running the [GET method](#streaming-api-get-conf):

```text
{"error":"Not found","code":"NotFound","status":"error"}
```
{: codeblock}

When streaming is not enabled, the following is returned when running the [PUT method](#streaming-api-update-conf):

```text
{"error":"Streaming configuration does not exist","code":"NotFound","status":"error"}
```
{: codeblock}

## List streaming exclusion rules
{: #streaming-api-list-rules}

Use [this method](https://{DomainName}/apidocs/log-analysis#get-v1-config-stream-exclusions){: external} to list existing streaming exclusion rules.

```text
curl --request GET https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream/exclusions
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
 ```
 {: pre}

The response will be similar to the following:

 ```text
 [{"hosts":[],"apps":[],"title":"Exclude Rule 1","query":"host:iam-am (action read)","active":true,"id":"xxxxxxxxxx"}]
 ```
 {: codeblock}

## Get details about a streaming exclusion rule
{: #streaming-api-get-rules}

Use [this method](https://{DomainName}/apidocs/log-analysis#get-v1-config-stream-exclusions-rule-id){: external} to get details of an existing streaming exclusion rule.

```text
curl --request GET https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream/exclusions/{ruleId}
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"

```
{: pre}

The response will be similar to the following:

```text
{"hosts":[],"apps":[],"title":"Exclude Rule 1","query":"host:iam-am (action read)","active":true,"id":"xxxxxxxxxx"}
```
{: codeblock}

## Create a streaming exclusion rule
{: #streaming-api-add-rules}

Use [this method](https://{DomainName}/apidocs/log-analysis#post-v1-config-stream-exclusions){: external} to create a streaming exclusion rule.

```text
curl --request POST https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream/exclusions
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
 -d '{"title": "Exclude Example", "query": "example", "active": true}'

```
{: pre}

The response will be similar to the following:

```text
{"hosts":[],"apps":[],"title":"Exclude Rule 1","query":"host:iam-am (action read)","active":true,"id":"xxxxxxxxxx"}
```
{: codeblock}

## Delete a streaming exclusion rule
{: #streaming-api-delete-rules}

Use [this method](https://{DomainName}/apidocs/log-analysis#delete-v1-config-stream-exclusions-rule-id){: external} to delete an existing streaming exclusion rule.

```text
curl --request DELETE https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream/exclusions/{ruleId}
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
```
{: pre}

The response will be similar to the following:

```text
{"deleted":true}
```
{: codeblock}

## Update a streaming exclusion rule
{: #streaming-api-update-rules}

Use [this method](https://{DomainName}/apidocs/log-analysis#patch-v1-config-stream-exclusions-rule-id){: external} to update an existing streaming exclusion rule.

```text
curl --request PATCH https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream/exclusions/{ruleId}
 -H "content-type: application/json"
 -H "servicekey: <SERVICE_KEY>"
 -d '{"title": "Exclude Example Update", "query": "example", "active": false}'
```
{: pre}

The response will be similar to the following:

```text
{"hosts":[],"apps":[],"title":"Exclude Example Update","query":"example","active":false,"id":"xxxxxxxxxx"}
```
{: codeblock}
