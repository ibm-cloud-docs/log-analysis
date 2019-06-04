---

copyright:
  years:  2018, 2019
lastupdated: "2019-06-03"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

subcollection: LogDNA

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

# Working with ingestion keys
{: #ingestion_key}

The ingestion key is a security key that you must use to configure LogDNA agents and successfully forward logs to your {{site.data.keyword.la_full_notm}} instance in {{site.data.keyword.cloud_notm}}. You automatically get the ingestion key when you provision an instance. Alternatively, you can also obtain the ingestion key by creating a service ID for the instance. 
{:shortdesc}

**Note:** 

* To work with ingestion keys through the {{site.data.keyword.la_full_notm}} Web UI, you must have an IAM policy with platform role **Viewer** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service. 
* To work with ingestion keys through the {{site.data.keyword.cloud_notm}} UI, you must have an IAM policy with platform role **Editor** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service. 


## Get the ingestion key through the {{site.data.keyword.cloud_notm}} UI
{: #ibm_cloud_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

2. Go to the Menu icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**. 

3. Select **Logging**. The {{site.data.keyword.la_full_notm}} dashboard opens. You can see the list of logging instances that are available on {{site.data.keyword.cloud_notm}}.

3. Identify the instance for which you want to get the ingestion key, and click **View ingestion key**.

4. A window opens where you can click **Show** to view the ingestion key.


## Get the ingestion key through the {{site.data.keyword.la_full_notm}} web UI
{: #logdna_ui}

To get the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Click the **Configuration** icon ![Configuration icon](images/admin.png) &gt; **Organization**. 

3. Select **API keys**. 

You can see the ingestion keys that are enabled. 



## Reset the ingestion key 
{: #reset}

If the ingestion key is compromised or you have a policy to renew it after a number of days, you can generate a new key and delete the old one.

To renew the ingestion key for an {{site.data.keyword.la_full_notm}} instance by using the {{site.data.keyword.la_full_notm}} Web UI, complete the following steps:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Click the **Configuration** icon ![Configuration icon](images/admin.png) &gt; **Organization**. 

3. Select **API keys**.

    You can see the ingestion keys that are enabled. 

4. Select **Generate Ingestion Key**.

    A new key is added to the list.

5. Delete the old ingestion key. Click **delete**.

After you reset the ingestion key, you must update the ingestion key for any log sources that you have configured to forward logs to this {{site.data.keyword.la_full_notm}} instance.
{: important}

For example, see [Resetting the ingestion key that is used by a Kubernetes cluster](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube_reset).



