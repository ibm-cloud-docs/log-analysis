---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-01"

keywords: LogDNA, IBM, Log Analysis, logging, export logs

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
{:external: target="_blank" .external}

 
# Controlling who can export logs
{: #export_config}

For each {{site.data.keyword.la_full_notm}} instance, you can configure whether users can export data.
{:shortdesc}

When the export configuration setting is enabled, you can export data in JSONL format from an {{site.data.keyword.la_full_notm}} instance.


## Allowing users to export logs
{: #export_config_allow}

Complete the following steps to allow users to export logs from an {{site.data.keyword.la_full_notm}} instance:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch).

2. Select the **Configuration** icon ![Configuration icon](../images/admin.png). 

3. Select **Organization** &gt; **General**.

4. Set-on the **Export Log Lines** setting to allow users to export logs. 



## Disable the export feature 
{: #export_config_disable}

Complete the following steps to disable the export feature in an {{site.data.keyword.la_full_notm}} instance:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch).

2. Select the **Configuration** icon ![Configuration icon](../images/admin.png). 

3. Select **Organization** &gt; **General**.

4. Set-off the **Export Log Lines** setting to prevent users from exporting logs. 

