---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, web UI, observability

subcollection: log-analysis

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

# Managing logging instances in the Observability UI
{: #observe}

You can manage your logging instances through the `Observability` dashboard in {{site.data.keyword.cloud_notm}}.
{:shortdesc}



## Launch the logging UI
{: #observe_ui}

Complete the following steps to launch the logging web UI:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**. 

3. Select **Logging** to go to the *Logging UI*. 

    The list of instances that are available on {{site.data.keyword.cloud_notm}} is displayed.


## Managing logging instance
{: #observe_manage}

In the *Logging UI*, you can manage your logging instances. 
* You can view all instances across all locations. You can also specify 1 location and view the instances that are available in that location. 
* You can view all instances across all the resource groups in your account. You can also select 1 resource group and view the instances that are available in that resource group.
* You can configure the instances in your account to collect platform logs. [Learn more](/docs/log-analysis?topic=log-analysis-config_svc_logs).
* You can create instances. [Learn more](/docs/log-analysis?topic=log-analysis-provision).

For each instance, you can view the following information:
* The status of an instance
* The resource group that is associated with an instance
* The region where the instance is provisioned
* The instances that are configured to collect automatically platform logs
* The service plan of an instance

You can also view sources. If you select **Edit log sources** for an instance, a new page opens where you can find instructions on how to configure logging agents tp forward logs to this instance. 

You might see the **Edit log sources** disabled. When this happens, the information icon displays a message that suggests that you need a new ingestion key. Notice that the ingestion key has not been lost. If you created the instance through the CLI, but did not create a service key for that instance, then the ingestion key is not available through the *Logging UI* for the instance. To fix the problem and enable the **Edit log sources**, complete 1 of the following steps: 
* [Create a service key](/docs/log-analysis?topic=log-analysis-provision#provision_cli_2).
* Follow the instructions given through the information icon. Click **i** &gt; **Got it** &gt; **Generate your key**.






    

