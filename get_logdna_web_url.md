---

copyright:
  years: 2019, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, web ui, browser

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

# Getting the logging web UI URL
{: #get_logdna_web_url}

After you provision an instance of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}}, you can view, monitor, and manage events through the {{site.data.keyword.la_full_notm}} web UI. You can launch the logging web UI from the {{site.data.keyword.cloud_notm}} UI or directly from a browser.
{:shortdesc}

To get the logging web UI URL, complete the following steps from a terminal:

1. [Pre-requisite] Installation of the {{site.data.keyword.cloud_notm}} CLI. [Learn more](/docs/cli?topic=cli-getting-started).

2. Log in to the location in the {{site.data.keyword.cloud_notm}} where the instance is provisioned. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the instance is available. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the dashboard URL. Run the following command:

    ```
    ic resource service-instance INSTANCE_NAME --output JSON | grep dashboard_url
    ```
    {: codeblock}
    
Where *INSTANCE_NAME* is the name of the instance.

To get the name of the instances that are available in a resource group, you can run `ibmcloud resource service-instances`.
{: tip}

