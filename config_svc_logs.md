---

copyright:
  years:  2018, 2020
lastupdated: "2020-06-01"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# Configuring {{site.data.keyword.cloud_notm}} platform logs
{: #config_svc_logs}

To monitor logs from {{site.data.keyword.cloud_notm}} platform services in your account, you must configure {{site.data.keyword.la_full_notm}}.
{:shortdesc}

You can have multiple {{site.data.keyword.la_full_notm}} instances in a location. However, only 1 instance in a location (region) can be configured to receive logs from [enabled services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services) in that {{site.data.keyword.cloud_notm}} location.
{: important}


## Configuring platform services logs through the Observability dashboard
{: #config_svc_logs_ui}

To configure an instance from the Observability dashboard in the {{site.data.keyword.cloud_notm}}, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Go to the menu icon ![menu icon](../../icons/icon_hamburger.svg) &gt; **Observability** to access the *Observability* dashboard.

3. Select **Logging**, then click **Configure platform services logs**. 

4. Select a [region](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-regions). 

5. Choose which LogDNA instance will recieve logs from enabled services on that location. [Learn more about the services that are enabled to send logs to {{site.data.keyword.la_full_notm}}.](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services)

6. Click **Save**. 

The main *Observability* page opens.

The instance that you choose to receive service logs shows the flag **Platform services logs**.



## Enabling a LogDNA instance from the command line
{: #platform_metrics_enabling_cli}

To enable platform logs in a region, the instance that you want to configure to receive platform logs must have set on the **default_receiver** property.
{: note}

Complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-getting-started).

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the LogDNA instance is running. Run the following command: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the LogDNA instance is running. Run the following command: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name. Run the following command: [`ibmcloud resource service-instances`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```
    ibmcloud resource service-instances
    ```
    {: pre}

5. Get the plan ID of the instance. 

    Run the following command and copy the value of the field `resource_plan_id`. This value is needed to update the instance.

    ```
    ibmcloud resource service-instance InstanceName --output JSON
    ```
    {: pre}

    Where `InstanceName` is the name of your LogDNA instance.

5. Set on the **default_receiver** property. Run the following command:

    ```
    ibmcloud resource service-instance-update InstanceName --service-plan-id PlanID -p '{"default_receiver": true}'
    ```
    {: codeblock}

    Where `PlanID` is the resource plan ID of your LogDNA instance.
    


