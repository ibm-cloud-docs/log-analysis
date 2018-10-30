---

copyright:
  years:  2018
lastupdated: "2018-11-02"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

 
# Exporting logs to local file
{: #export}

You can export log data in JSONL format from an IBM Log Analysis with LogDNA instance into a local file.
{:shortdesc}


## Exporting logs from the Web UI
{: #ui}

Complete the following steps to export log data:

1. Perform your search query for the desired log lines.
2. Click on the view menu to the left of the All Sources filter and select Export Lines.
3. Select a time range to apply to the search results.
4. Select an option to prefer newer or older lines in case the export exceeds our line limit.
5. You will receive an email with a link download to your exported lines.

## Exporting logs programmatically by using the API
{: #api}


Complete the following steps:

1. Generate a Service Key.

2. Run the cURL command:

```curl "https://api.logdna.com/v1/export?to=$(date +%s)000&from=$(($(date +%s)-86400))000&levels=warn" \
-u INSERT_SERVICE_KEY:
```
{: codeblock}

For more information, see [/v1/export](https://docs.logdna.com/v1.0/reference#v1export).