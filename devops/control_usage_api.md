---

copyright:
  years:  2018, 2023
lastupdated: "2021-11-18"

keywords: IBM, Log Analysis, logging, control usage

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Analyzing event data trends by using the API
{: #control_usage_api}

In {{site.data.keyword.la_full}}, you can query your logging instance and identify usage trends over a period of time by using the *Usage API*. You can get aggregated usage data information for applications, hosts and tags during a specific period of time and within the last 6 months.
{: shortdesc}


## API method
{: #control_usage_method}

To query usage data, you can use the following methods:

- For all apps during a time period, you can list the aggregated usage.

    ```text
    curl "<ENDPOINT>/v1/usage/apps/<SERVICE_NAME>?from=<FROM_DATE>&to=<TO_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>:
    ```
    {: codeblock}

- For all tags during a time period, you can list the aggregated usage.

    ```text
    curl "<ENDPOINT>/v1/usage/tags/<SERVICE_NAME>?from=<FROM_DATE>&to=<TO_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>:
    ```
    {: codeblock}

- For all hosts during a time period, you can list the aggregated usage.

    ```text
    curl "<ENDPOINT>/v1/usage/hosts/<SERVICE_NAME>?from=<FROM_DATE>&to=<TO_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>:
    ```
    {: codeblock}

- For 1 app during a time period, you can get the aggregated usage.

    ```text
    curl "<ENDPOINT>/v1/usage/apps/<SERVICE_NAME>/<APP_NAME>?from=<FROM_DATE>&to=<TO_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>:
    ```
    {: codeblock}

- For 1 tag during a time period, you can get the aggregated usage.

    ```text
    curl "<ENDPOINT>/v1/usage/tags/<SERVICE_NAME>/<TAG_NAME>?from=<FROM_DATE>&to=<TO_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>:
    ```
    {: codeblock}

- For 1 host during a time period, you can get the aggregated usage.

    ```text
    curl "<ENDPOINT>/v1/usage/hosts/<SERVICE_NAME>/<HOST_NAME>?from=<FROM_DATE>&to=<TO_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>:
    ```
    {: codeblock}

- Replace `<ENDPOINT>` with the {{site.data.keyword.at_full_notm}} API endpoint. To see the list of endpoints, see either [Public API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api_public) or [Private API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api_private) as appropriate for your environment.
- Replace `<SERVICE_NAME>` with the [CRN service name](/docs/log-analysis?topic=log-analysis-cloud_services) for the service you are interested in.  If not specified, data for all services meeting the other criteria will be returned.
- Replace `<APP_NAME>` with the name of the app.
- Replace `<TAG_NAME>` with the name of the tag.
- Replace `<HOST_NAME>` with the name of the host.

    For platform logs, the `<HOST_NAME>` is the [CRN service name](/docs/log-analysis?topic=log-analysis-cloud_services) for the service.

- Replace the `<SERVICE_KEY>` with a valid service key for the {{site.data.keyword.la_full_notm}} instance. For more information, see [Service keys by using the API](/log-analysis?topic=log-analysis-service_keys#service_keys_api).
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
        "name": "host or app or tag name 1",
        "current_total": 1418178,
        "percentage_of_total": 59.35177415676025
    },
    {
        "name": "host or app or tag name 1",
        "current_total": 287299,
        "percentage_of_total": 12.023670768735
    }
]
```
{: codeblock}

In this case, usage for 2 services has been returned.  The `current_total` value reports the number of ingested lines during the queried time period.  The `percentage_of_total` is the percentage of total lines ingested during the time period by all services.

## Additional examples
{: #control_usage_examples}

The following provide additional, specific usage examples.

### List usage data for all hosts for the past 6 months
{: #control_usage_examples1}

This command list the aggregated usage information for all hosts for the past 6 months.

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts" -u <SERVICE_KEY>:
```
{: codeblock}


### List usage data for the top N hosts for the past 6 months
{: #control_usage_examples2}

This command lists the aggregated usage information for the highest-usage `N` hosts for the past 6 months where `N` is an integer number.

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts?limit=N" -u <SERVICE_KEY>:
```
{: codeblock}

Specifying `5` for `N` will return the information for the top 5 highest-usage hosts as shown in this example:

```json
[
    {
        "name": "cloudcerts",
        "current_total": 1418178,
        "percentage_of_total": 59.35177415676025
    },
    {
        "name": "containers-kubernetes",
        "current_total": 287299,
        "percentage_of_total": 12.023670768735
    },
    {
        "name": "container-registry",
        "current_total": 218164,
        "percentage_of_total": 9.130321057818866
    },
    {
        "name": "ibm-cloud-databases-prod",
        "current_total": 205699,
        "percentage_of_total": 8.608651799894956
    },
    {
        "name": "schematics",
        "current_total": 107925,
        "percentage_of_total": 4.516739242794874
    }
]
```
{: codeblock}


### List usage data for a specific host for the past 6 months
{: #control_usage_examples3}

By specifying the `<HOST_NAME>`, the usage data for only that service is returned.  For platform logs, the `<HOST_NAME>` is the [CRN service name](/docs/log-analysis?topic=log-analysis-cloud_services) for the service.


```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/<HOST_NAME>" -u <SERVICE_KEY>:
```
{: codeblock}

For example, if you want to query usage data for the {{site.data.keyword.containerlong}} service you would run the following:

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/containers-kubernetes" -u <SERVICE_KEY>:
```
{: codeblock}

And the output would be similar to the following:

```json
[
    {
        "name": "containers-kubernetes",
        "current_total": 205699,
        "percentage_of_total": 8.608651799894956
    }
]
```
{: codeblock}

### List usage data for a specific host over the past 10 days
{: #control_usage_examples4}

The following will list the aggregated usage information for the host `<HOST_NAME>` over the past 10 days.

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/<HOST_NAME>?from=$(($(date +%s)-864000))&to=$(date +%s)" -u <SERVICE_KEY>:
```
{: codeblock}


### List usage data for highest usage host for a 1 month period
{: #control_usage_examples5}

The following will list the usage information for the highest usage host over a specific month.  The time period is specified by including a `<START_DATE>` and `END_DATE`.

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts/?from=<START-DATE>&to=<END_DATE>&limit=<LIMIT_NUMBER>" -u <SERVICE_KEY>:
```
{: codeblock}

For example, to return the host with the highest data usage in October 2021, that is from October 1, 2021 through November 1 2021, you would run:

```text
curl "https://api.us-south.logging.cloud.ibm.com/v1/usage/hosts?from=1633046400&to=1635724800&limit=1" -u <SERVICE_KEY>:
```
{: codeblock}
