---

copyright:
  years: 2019, 2024
lastupdated: "2024-05-24"

keywords: IBM Cloud, Log Analysis, streaming

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Monitoring streaming to a {{site.data.keyword.la_short}} instance (WIP)
{: #streaming-monitor-l2l}

missimng samples
{: important}

You can use {{site.data.keyword.at_full_notm}} to monitor streaming of data from your {{site.data.keyword.la_short}} instance to a destination {{site.data.keyword.la_short}} instance.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}


## Monitoring streaming by using {{site.data.keyword.at_full_notm}}
{: #streaming-monitor-2}

Streaming generates {{site.data.keyword.at_short}} events with the action **logdna.streaming-logs.send** to notify about data streaming failures.

The `reasonType` and `notificationType` will indicate they type of failure.  For example, `request_failed_with_status_code_403` can indicate an invalid ingestion key.

The following are possible error codes:

| Code | Possible failure |
| -------------- | ----------- |
| 400 | Access error.  For example, the regular ingestion URL might have been specified instead of the self-stream ingestion URL. |
| 403 | Authentication error.  For example, an incorrect ingestion key was specified. |
| 404 | A valid ingestion server was specified, but an invalid ingestion URL was specified. |
| 500 | An internal server error was detected from the receiving instance |
{: caption="Table 1. Possible streaming errors" caption-side="bottom"}

These errors assume that a valid, reachable hostname was specified on the ingestion URL.  Issues with connectivity, or an invalid hostname, can result in an error `getaddrinfo_enotfound_<URL>` where `<URL>` is the URL that was provided on the request.  Connectivity issues with the destination ingestion service, or if the service is offline, will result in `connect_econnrefused_<IP_ADDR>` where `<IP_ADDR>` is the service IP address.

The following sections include samples of some fields in the notification event that you can use to monitor and be alerted when a failure happens:

```json
"requestData": {
        "notificationType": "unknown_topic_or_partition",
        "start": "2021-06-29T21:33:52.333Z",
        "end": "2021-06-29T21:35:13.772Z",
        "topic": "kafka-java-console-sample-topic",
        "error": "Error: Broker: Unknown topic or partition"
    },
```
{: codeblock}

```json
"reason": {
        "reasonCode": 500,
        "reasonType": "unknown_topic_or_partition",
        "reasonForFailure": "Error: Broker: Unknown topic or partition"
    },
```
{: codeblock}

```json
"target": {
        "id": "crn:v1:staging:public:logdna:us-south:a/9bb3ea01633c4d828080de16ce34ea70:d8ba830f-b0e0-4c42-9345-8981d4a94b31:streaming-logs:",
        "typeURI": "logdna/account/streaming-notification"
```
{: codeblock}


### Query to monitor failures
{: #streaming-monitor-2-1}

In {{site.data.keyword.la_short}}, you can create a view with the following query to filter for event stream failure notifications:

```text
action:logdnaat.streaming-logs.send reason.reasonCode:500 severity:critical target.typeURI:"logdna/account/streaming-notification"
```
{: codeblock}

You can define a presence alert on this view to notify you as soon as 1 event reporting failure comes in.

In addition, you can create views for each type of notification. For example, to monitor for a failure to authenticate with {{site.data.keyword.messagehub}}, you can use the following query:

```text
action:logdnaat.streaming-logs.send reason.reasonCode:500 severity:critical target.typeURI:"logdna/account/streaming-notification" requestData.notificationType:"authentication_failure"
```
{: codeblock}
