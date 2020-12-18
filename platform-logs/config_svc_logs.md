---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-02"

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
{:external: target="_blank" .external}

# Configuring {{site.data.keyword.cloud_notm}} platform logs
{: #config_svc_logs}

`Platform logs` are logs that are exposed by enabled-LogDNA services and the platform in {{site.data.keyword.cloud_notm}}. You must configure a LogDNA instance in a region to monitor these logs.
{:shortdesc}

* Platform logs are regional. 

    You can monitor logs from enabled-LogDNA services on the {{site.data.keyword.cloud_notm}} in the region where the service is available. 

* You can configure 1 instance only of the {{site.data.keyword.la_full_notm}} service per region to collect *platform logs* in that location. 

    You can have multiple {{site.data.keyword.la_full_notm}} instances in a location. However, only 1 instance in a location (region) can be configured to receive logs from [enabled services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services) in that {{site.data.keyword.cloud_notm}} location.
    {: important}

* To configure a LogDNA instance, you must set on the *platform logs* configuration setting. Also, you must have the platform role `editor` or higher for the {{site.data.keyword.la_full_notm}} service in your account.

* If a LogDNA instance in a region is already enabled to collect platform logs, logs from enabled-LogDNA services are collected automatically and available for analysis through this instance. For more information about enabled-LogDNA services, see [Cloud services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services).

* To monitor platform logs for a service instance, check that the {{site.data.keyword.la_full_notm}} instance is provisioned in the same region where the service instance that you want to monitor is provisioned.


## Configuring platform logs through the Observability dashboard
{: #config_svc_logs_ui}

To configure a logging instance from the Observability dashboard in the {{site.data.keyword.cloud_notm}}, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Go to the menu icon ![menu icon](../../icons/icon_hamburger.svg) &gt; **Observability** to access the *Observability* dashboard.

3. Select **Logging**, then click **Configure platform logs**. 

4. Select a [region](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-regions). 

5. Choose which LogDNA instance will receive logs from enabled services on that location. [Learn more about the services that are enabled to send logs to {{site.data.keyword.la_full_notm}}.](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services)

6. Click **Save**. 

The main *Observability* page opens.

The instance that you choose to receive service logs shows the flag **Platform logs**.



## Configuring platform logs from the command line
{: #platform_logs_enabling_cli}

To enable platform logs in a region, the instance that you want to configure to receive platform logs must have set on the **default_receiver** property.

Check if you have an instance with the flag **Platform Logs** set in the region that you want to configure platform logs. Your user must have permissions to see all instances in the account. 
{: important}

If you have an instance with the flag **Platform Logs**, stop and contact the account administrator to confirm that you will not impact the account operations. There is only 1 instance per region that can collect platform logs. After you make this change, platform logs are collected through this instance in the region, and permissions to view platform logs are impacted. See [Changing the instance that collects platform logs from the command line](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-config_svc_logs#platform_logs_change_cli).  
{: important}

If you do not have an instance with the flag **Platform Logs** in the region, complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where the LogDNA instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the LogDNA instance is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Get the instance name and plan ID. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```
    ibmcloud resource service-instance InstanceName --output JSON
    ```
    {: pre}

    Copy the value of the field `resource_plan_id`. This value is needed to update the instance.

5. Set on the **default_receiver** property. Run the following command:

    Check that the change will not affect other account members. There is only 1 instance per region that can collect platform logs. After you make this change, platform logs are collected through this instance in the region, and permissions to view platform logs are impacted.  
    {: important}

    ```
    ibmcloud resource service-instance-update InstanceName --service-plan-id PlanID -p '{"default_receiver": true}'
    ```
    {: codeblock}

    Where `PlanID` is the resource plan ID of your LogDNA instance.
    


## Changing the instance that collects platform logs from the command line
{: #platform_logs_change_cli}

You must use a user that has permissions to see all instances in the account.
{: note}

Before you change the instance that collects platform logs, check that the change will not affect other account members. There is only 1 instance per region that can collect platform logs. After you make this change, platform logs are collected through this instance in the region, and permissions to view platform logs are impacted.  
{: important}

Complete the following steps:

1. [Pre-requisite] [Install the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

2. [Pre-requisite]Get the details of the instance with the flag **Platform Logs** set in the region that you want to reconfigure. 

3. Log in to the region in the {{site.data.keyword.cloud_notm}} where the LogDNA instance is running. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

4. Set the resource group where the LogDNA instance that has the **platform logs** flag is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

5. Get the instance name and plan ID. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```
    ibmcloud resource service-instance InstanceName --output JSON
    ```
    {: pre}

    Copy the value of the field `resource_plan_id`. This value is needed to update the instance.

6. Set on the **default_receiver** property. Run the following command:

    ```
    ibmcloud resource service-instance-update InstanceName --service-plan-id PlanID -p '{"default_receiver": true}'
    ```
    {: codeblock}

    Where 
    
    * `PlanID` is the resource plan ID of your LogDNA instance.

    * `InstanceName` is the name of the instance that you want to turn on and start collecting platform logs.

7. Set the resource group where the LogDNA instance that you want to stop collecting platform logs is running. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

8. Get the instance name and plan ID. Run the following command: [ibmcloud resource service-instances](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instances)

    ```
    ibmcloud resource service-instances --output JSON
    ```
    {: pre}

    Copy the value of the field `resource_plan_id`. This value is needed to update the instance.

9. Set off the **default_receiver** property. Run the following command:

    ```
    ibmcloud resource service-instance-update InstanceName --service-plan-id PlanID -p '{"default_receiver": false}'
    ```
    {: codeblock}

    Where 
    
    * `PlanID` is the resource plan ID of your LogDNA instance.

    * `InstanceName` is the name of the instance that you want to turn off from collecting platform logs.
    




