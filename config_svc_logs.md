---

copyright:
  years:  2018, 2019
lastupdated: "2019-08-12"

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

To view logs from platform services in your account, you must configure {{site.data.keyword.la_full_notm}}.
{:shortdesc}

You can have multiple {{site.data.keyword.la_full_notm}} instances in a location. However, only 1 instance in a location (region) can be configured to receive logs from [enabled services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services) in that {{site.data.keyword.cloud_notm}} location.
{: important}


## Configuring platform services logs through the Observability dashboard
{: #config_svc_logs_ui}

To configure an instance from the Observability dashboard in the {{site.data.keyword.cloud_notm}}, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Go to the menu icon ![menu icon](../../icons/icon_hamburger.svg) &gt; **Observability** to access the *Observability* dashboard.

3. Select **Logging**, then click **Configure platform services logs**. 

4. Select a [region](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-regions). 

5. Choose which LogDNA instance will recieve logs from enabled services on that location. [Learn more about the services that are enabled to send logs to {{site.data.keyword.la_full_notm}}.](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services)

6. Click **Save**. 

The main *Observability* page opens.

The instance that you choose to receive service logs shows the flag **Platform services logs**.


