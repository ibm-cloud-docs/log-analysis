---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-24"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion, python

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

 
# Sending logs by using Python
{: #ingest-python}

You can send log data to an {{site.data.keyword.la_full_notm}} instance by using Python. 
{:shortdesc}

Complete the following steps to send logs:

## Prereqs
{: #ingest-python_prereqs}

Run the following command to install the LogDNA handler:

```
python3 -m pip install logdna
```
{: pre}


## Step 1. Get the ingestion API key 
{: #ingest-python_step1}

**Note:** You must have **manager** role for the {{site.data.keyword.la_full_notm}} instance or service to complete this step. For more information, see [Granting permissions to manage logs and configure alerts in LogDNA](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-work_iam#admin_user_logdna).

Complete the following steps to get the ingestion key:
    
1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-view_logs#view_logs_step2).

2. Click the **Configuration** icon ![Configuration icon](images/admin.png) &gt; **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that have been created. 

4. Copy a key. You can use an existing ingestion key or click **Generate Ingestion Key** to create a new one. When you generate a key, the key is added to the list. 




## Step 2. Send logs
{: #ingest-python_step2}

To send logs, creaate a file with the following content:

```
#!/usr/bin/env python3 
import os 
import logging
  
from logdna import LogDNAHandler 
  
apiKey = '<INGESTION-KEY>' 

log = logging.getLogger('logdna')
log.setLevel(logging.INFO)

options = {
  'hostname': '<HOSTNAME>',
  'ip': '10.0.1.1',
  'mac': 'C0:FF:EE:C0:FF:EE',
  'env': 'Dallas',
  'level': 'Info',
  'index_meta': True,
  'url': 'https://logs.us-south.logging.cloud.ibm.com/logs/ingest'
}

test = LogDNAHandler(apiKey, options)

log.addHandler(test)

log.warning("Sample message 1", {'app': 'sample-app'})
log.info("Sample message 2", {'app': 'sample-app'})
```
{: codeblock}

Where 

* INGESTION_KEY is the key that you created in the previous step.

* The following table lists the `options` parameters:

| Query parameter | Type       | Status     | Description |
|-----------------|------------|------------|-------------|
| `hostname`      | `string`     | required   | Host name of the source. |
| `mac`           | `string`     | optional   | The network mac address of the host computer.    |
| `ip`            | `string`     | optional   | The local IP address of the host computer.  | 
| `now`           | `date-time`  | optional   | The source UNIX timestamp in milliseconds at the time of the request. Used to calculate time drift.|
| `tags`          | `string`     | optional   | Tags that are used to dynamically group hosts. |
| `url`           | `string`     | required   | URL represents the entry point to the service. Each region has a different URL. To get the endpoint for a location, see [Ingestion endpoints](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-endpoints#endpoints_ingestion). For example, `https://logs.us-south.logging.cloud.ibm.com/logs/ingest`.
{: caption="Query parameters" caption-side="top"} 




## Example
{: #ingest-python_example}

The following sample sends 2 log lines with different priorities (level) to an instance of the {{site.data.keyword.la_full_notm}} service: 

1. Save the following content to a file named `python3 send-logs.py`.

```
#!/usr/bin/env python3 
import os 
import logging
  
from logdna import LogDNAHandler 
  
apiKey = '<INGESTION-KEY>' 

log = logging.getLogger('logdna')
log.setLevel(logging.INFO)

options = {
  'hostname': 'MyHostName',
  'ip': '10.0.1.1',
  'mac': 'C0:FF:EE:C0:FF:EE',
  'env': 'Dallas',
  'level': 'Info',
  'index_meta': True,
  'url': 'https://logs.us-south.logging.cloud.ibm.com/logs/ingest'
}

test = LogDNAHandler(apiKey, options)

log.addHandler(test)

log.warning("Sample message 1", {'app': 'sample-app'})
log.info("Sample message 2", {'app': 'sample-app'})
```
{: screen}


2. From the command line, run the following command:

```
python3 send-logs.py 
```
{: codeblock}


## Limits when you send logs
{: #ingest_limits-python}

Consider the following limits when you send logs to an {{site.data.keyword.la_full_notm}} instance:

- `Body size`: Maximum size of 10 MB at ingestion.
- `Message size`: Maximum size of 16 KB at ingestion. After 16K, the data is truncated at ingestion.
- `Metadata size`: Maximum size of 32 KB.
- `Hostname length`: Maximum size of 256 characters.
- `App name length`: Maximum size of 512 characters.
- `Log Level`: Maximum size of 80 characters.
- `Tags`: Maximum size of 80 characters.
- `Depth of nested fields`: 3 is the maximum number of nested fields that are parsed at ingestion.
- `Number of unique fields`: A maximum of 500 fields are indexed per day. 

