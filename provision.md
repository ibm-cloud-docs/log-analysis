---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, provision

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

# Provisioning an instance
{: #provision}

Before you can monitor and manage log data with {{site.data.keyword.la_full_notm}}, you must first provision an instance of the service in {{site.data.keyword.cloud_notm}}.
{:shortdesc}

To provision an {{site.data.keyword.la_full_notm}} instance in a Public Cloud region, you must select the service plan that is associated with the instance, the region where your logs are collected, and the plan that determines the retention period for your logs. You can choose from 7, 14, or 30-day retention periods.

Alternatively, {{site.data.keyword.la_full_notm}} offers a `Lite` plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.


## Provisioning an instance through the Observability dashboard
{: #provision_ui}

To provision an instance from the Observability dashboard in the {{site.data.keyword.cloud_notm}}, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    The {{site.data.keyword.cloud_notm}} dashboard can be found at: [{{site.data.keyword.cloud_notm}} dashboard ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} UI opens.

2. Go to the menu icon ![menu icon](../../icons/icon_hamburger.svg). Then, select **Observability** to access the *Observability* dashboard.

3. Select **Logging**, then click **Create instance**. 

4. Enter a name for the service instance.

5. Select a resource group. 

    By default, the **Default** resource group is set.

    **Note:** If you are not able to select a resource group, check that you have editing permissions on the resource group where you want to provision the instance.

6. Enable **IBM service logs**.

    **Note:** Only one instance of the service can collect IBM service logs.

7. Select the `Lite` service plan. 

    By default, the lite plan is set.

    For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

7. Click **Create**.

After you provision an instance, the *Logging* dashboard opens. 

Next, configure a log source by adding a LogDNA agent. This agent is responsible for collecting and forwarding logs to your instance. 



## Provisioning an instance through the catalog
{: #provision_catalog}

To provision an instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} catalog, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    Click [{{site.data.keyword.cloud_notm}} dashboard ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window} to launch the {{site.data.keyword.cloud_notm}} dashboard.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click the **{{site.data.keyword.la_full_notm}}** tile. 

5. Enter a name for the service instance.

6. Select a resource group. 

    By default, the **Default** resource group is set.

    **Note:** If you are not able to select a resource group, check that you have editing permissions on the resource group where you want to provision the instance.

7. Select the `Lite` service plan. 

    By default, the lite plan is set.

    For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. Click **Create**.

After you provision an instance, the *Logging* dashboard opens. 

Next, configure a log source by adding a LogDNA agent. This agent is responsible for collecting and forwarding logs to your instance. 



## Provisioning an instance through the CLI
{: #provision_cli}

To provision an instance of {{site.data.keyword.la_full_notm}} through the command line, complete the following steps:

1. [Pre-requisite] Installation of the {{site.data.keyword.cloud_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where you want to provision the instance. Run the following command: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where you want to provision the instance. Run the following command: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Create the instance. Run the [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) command:

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    Where

    NAME is the name of the instance

    The value *logdna* is the name of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}}

    SERVICE_PLAN_NAME is the type of plan. Valid values are *lite*, *7-days*, *14-days*, *30-days*
    
    LOCATION is the region where the LogDNA instance is created. Valid value is *us-south*

    For example, to provision an instance with the 7 days retention plan, run the following command:

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}

5. Create a service key with **administrator** permissions to operate the instance. Run the [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key_create) command:

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    Where

    NAME is the name of the API key. You can name the API key like the {{site.data.keyword.la_full_notm}} instance to help you identify the API key later on.

    ROLE_NAME is the role that defines the permissions that are enabled. Valid values are *editor*, *operator*, *administrator*

    SERVICE_INSTANCE_NAME is the name of the instance in the {{site.data.keyword.cloud_notm}}

    For example, to create an API key for the instance *logdna-instance-01* with *administrator* permissions on the service instance, run the following command:

    ```
    ibmcloud resource service-key-create logdna-instance-01 Administrator --instance-name logdna-instance-01
    ```
    {: pre}

    The output from this command includes different values like the `crn` value of the instance and the LogDNA ingestion key.


