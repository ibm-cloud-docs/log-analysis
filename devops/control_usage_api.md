---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, control usage

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Analyzing event data trends by using the API (WIP)
{: #control_usage_api}

In {{site.data.keyword.la_full}}, you can query your logging instance and identify usage trends over a period of time by using the *Usage API*. 
{: shortdesc}



## API method
{: #control_usage_method}

The method for querying usage data is:

```text
curl "<ENDPOINT>/v1/usage/hosts/<SERVICE_NAME>?from=<FROM_DATE>&to=<TO_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>: 
```

- Replace `<ENDPOINT>` with the {{site.data.keyword.at_full_notm}} API endpoint. To see the list of endpoints, see either [Public API endpoints](/docs/activity-tracker?topic=activity-tracker-endpoints#endpoints_api-at-public) or [Private API endpoints](/docs/activity-tracker?topic=activity-tracker-endpoints#endpoints_api-at-private) as appropriate for your environment.
- Replace `<SERVICE_NAME>` with the [CRN service name](/docs/activity-tracker?topic=activity-tracker-cloud_services) for the service you are interested in.  If not specified, data for all services meeting the other criteria will be returned.
- Replace the `<SERVICE_KEY>` with a valid service key for the {{site.data.keyword.at_full_notm}} instance. For more information, see [Service keys by using the API](/docs/activity-tracker?topic=activity-tracker-service_keys#service_keys_api).
- Replace `<LIMIT_NUMBER>` with the number of services to be returned from the highest usage to the lowest.  If not specified, only the highest-usage service will be returned.  `<LIMIT_NUMBER>` is an integer number.
- Replace `<FROM_DATE>` with your desired starting date in Unix epoch format.  For example, `$(($(date +%s)-864000))` would be 10 days ago and `$(($(date +%s)-86400))` is 1 day ago. `$(date +%s)` is today.  Dates can be specified as relative values as shown, or a specific integer such as `1633046400`.
- Replace `<TO_DATE>` with your desired ending date in Unix epoch format.

[This website](https://www.epochconverter.com/){: external} can help you calculate the epoch date.
{: tip}

## Output
{: #control_usage_output}

The method returns the requested data in JSON format.

```json
[
    {
        "name": "service name 1",
        "current_total": 1418178,
        "percentage_of_total": 59.35177415676025
    },
    {
        "name": "service name 1",
        "current_total": 287299,
        "percentage_of_total": 12.023670768735
    }
]
```
{: codeblock}

In this case usage for 2 services has been returned.  The `current_total` value reports the number of ingested lines during the queried time period.  The `percentage_of_total` is the percentage of total lines ingested during the time period by all services.

## Additional examples
{: control_usage_examples}

The following provide additional, specific usage examples.

### List usage data for all sources for the past 6 months
{: #control_usage_examples1}

This command list the aggregated usage information for all services for the past 6 months.

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts" -u <SERVICE_KEY>:
```
{: codeblock}


### List usage data for the top N sources for the past 6 months
{: #control_usage_examples2}

This command lists the aggregated usage information for the highest-usage `N` services for the past 6 months where `N` is an integer number. 

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts?limit=N" -u <SERVICE_KEY>:
```
{: codeblock}

Specifying `5` for `N` will return the information for the top 5 highest-usage services as shown in this example:

```json
[
    {
        "name": "cloud-object-storage",
        "current_total": 1418178,
        "percentage_of_total": 59.35177415676025
    },
    {
        "name": "containers-kubernetes",
        "current_total": 287299,
        "percentage_of_total": 12.023670768735
    },
    {
        "name": "sysdig-monitor",
        "current_total": 218164,
        "percentage_of_total": 9.130321057818866
    },
    {
        "name": "kms",
        "current_total": 205699,
        "percentage_of_total": 8.608651799894956
    },
    {
        "name": "is-load-balancer",
        "current_total": 107925,
        "percentage_of_total": 4.516739242794874
    }
]
```
{: codeblock}


### List usage data for a specific spurce for the past 6 months
{: #control_usage_examples3}

By specifying the `<SERVICE_NAME>`, the usage data for only that service is returned.  The `<SERVICE_NAME>` is the [CRN service name](/docs/activity-tracker?topic=activity-tracker-cloud_services) for the service.


```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/<SERVICE_NAME>" -u <SERVICE_KEY>:
```
{: codeblock}

For example, if you want to query usage data for the {{site.data.keyword.keymanagementservicelong_notm}} service you would run the following:

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/kms" -u <SERVICE_KEY>:
```
{: codeblock}

And the output would be similar to the following:

```json
[
    {
        "name": "kms",
        "current_total": 205699,
        "percentage_of_total": 8.608651799894956
    }
]
```
{: codeblock}

### List usage data for a specific source over the past 10 days
{: #control_usage_examples4}

The following will list the aggregated usage information for the `<SERVICE_NAME>` service over the past 10 days.

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/<SERVICE_NAME>?from=$(($(date +%s)-864000))&to=$(date +%s)" -u <SERVICE_KEY>:
```
{: codeblock}


### List usage data for highest usage source for a 1 month period
{: #control_usage_examples5}

The following will list the usage information for the highest usage service over a specific month.  The time period is specified by including a `<START_DATE>` and `END_DATE`.

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/?from=<START-DATE>&to=<END_DATE>" -u <SERVICE_KEY>:
```
{: codeblock}

For example, to return the service with the highest data usage in October 2021, that is from October 1, 2021 through November 1 2021, you would run:

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts?from=1633046400&to=1635724800" -u <SERVICE_KEY>:
```
{: codeblock}





