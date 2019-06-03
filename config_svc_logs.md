---

copyright:
  years:  2018, 2019
lastupdated: "2019-06-03"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# Configuring {{site.data.keyword.cloud_notm}} service logs
{: #config_svc_logs}

You can have multiple {{site.data.keyword.la_full_notm}} instances in a region. However, only 1 instance in a region can be configured to receive logs from enabled services in the {{site.data.keyword.cloud_notm}}.
{:shortdesc}



## Configuring platform services logs through the Observability dashboard
{: #config_svc_logs_ui}

To configure an instance from the Observability dashboard in the {{site.data.keyword.cloud_notm}}, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} UI opens.

2. Go to the menu icon ![menu icon](../../icons/icon_hamburger.svg) &gt; **Observability** to access the *Observability* dashboard.

3. Select **Logging**, then click **Configure platform services logs**. 

4. Choose which LogDNA instance will recieve logs from enabled services on the cloud platform.

5. Select a [location](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-regions). 

6. Select an instance.

7. Click **Save**. 

The main *Observability* page opens.

The instance that you choose to receive service logs shows the flag **Platform services logs**.

For more information about the services that are enabled to send logs to {{site.data.keyword.la_full_notm}}, see [Cloud services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services).

