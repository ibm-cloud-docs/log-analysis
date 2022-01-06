---

copyright:
  years:  2018, 2022
lastupdated: "2021-04-12"

keywords: IBM, Log Analysis, logging, ingestion, python

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

 
# Sending logs by using Python
{: #ingest_python}

You can send logs to an {{site.data.keyword.la_full_notm}} instance by using Python. 
{: shortdesc}

Complete the following steps to send logs:

## Prereqs
{: #ingest_python_prereqs}

Run the following command to install the handler:

```text
python3 -m pip install logdna
```
{: pre}


## Step 1. Get the ingestion API key 
{: #ingest_python_step1}

**Note:** You must have **manager** role for the {{site.data.keyword.la_full_notm}} instance or service to complete this step. For more information, see [Granting permissions to manage logs and configure alerts](/docs/log-analysis?topic=log-analysis-work_iam#admin_user_logdna).

Complete the following steps to get the ingestion key:
    
1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Settings icon](../images/admin.png) &gt; **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that have been created. 

4. Copy a key. You can use an existing ingestion key or click **Generate Ingestion Key** to create a new one. When you generate a key, the key is added to the list. 




## Step 2. Send logs
{: #ingest_python_step2}

To send logs, creaate a file with the following content:

```python
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
| `url`           | `string`     | required   | URL represents the entry point to the service. Each region has a different URL. To get the endpoint for a location, see [Ingestion endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_ingestion). For example, `https://logs.us-south.logging.cloud.ibm.com/logs/ingest`.
{: caption="Query parameters" caption-side="top"} 




## Example
{: #ingest_python_example}

The following sample sends 2 log lines with different priorities (level) to an instance of the {{site.data.keyword.la_full_notm}} service: 

1. Save the following content to a file named `send-logs.py`.

    ```python
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
    {: codeblock}

2. From the command line, run the following command:

    ```text
    python3 send-logs.py 
    ```
    {: pre}


## Limits when you send logs
{: #ingest_limits_python}

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

