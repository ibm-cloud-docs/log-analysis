---

copyright:
  years: 2018
lastupdated: "2018-12-14"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

# Provisioning an instance
{: #provision}

Before you can monitor and manage log data with {{site.data.keyword.la_full_notm}}, you must first provision an instance of the service in {{site.data.keyword.Bluemix}}.
{:shortdesc}

To provision an {{site.data.keyword.la_full_notm}} instance in a Public Cloud region, you must select the service plan that is associated with the instance, the region where your logs are collected, and the plan that determines the retention period for your logs. You can choose from 7, 15, or 30-day retention periods.

Alternatively, {{site.data.keyword.la_full_notm}} offers a **Free** plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.


## Provisioning an instance through the {{site.data.keyword.Bluemix_notm}} UI
{: #provision_ui}

To provision an instance of {{site.data.keyword.la_full_notm}} by using the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://cloud.ibm.com ![External link icon](../../icons/launch-glyph.svg "External link icon")](http://cloud.ibm.com){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.Bluemix_notm}} opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click the **{{site.data.keyword.la_full_notm}}** tile. The *Observability* Dashboard opens.

5. Select **Create instance**. 

6. Enter a name for the service instance.

7. Select a resource group. 

    By default, the **Default** resource group is set.

    **Note:** If you are not able to select a resource group, check that you have editing permissions on the resource group where you want to provision the instance.

8. Select the **Lite** service plan. 

    By default, the **Lite** plan is set.

    For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

9. To provision the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.Bluemix_notm}} resource group where you are logged in, click **Create**.

After you provision an instance, 

* The *Observability* dashboard opens. 
* A service ID is automatically created. You can use this service ID to get the ingestion key for your instance.

Next, configure a log source by adding a LogDNA agent. This agent is responsible for collecting and forwarding logs to LogDNA. 


## Provisioning an instance through the CLI
{: #provision_cli}

To provision an instance of {{site.data.keyword.la_full_notm}} through the command line, complete the following steps:

1. [Pre-requisite] Install the {{site.data.keyword.Bluemix_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.Bluemix_notm}} where you want to provision the instance. Run the following command: [`ibmcloud login`](/docs/cli/reference/ibmcloud/bx_cli.html#ibmcloud_login)

3. Set the resource group where you want to provision the instance. Run the following command: [`ibmcloud target`](/docs/cli/reference/ibmcloud/bx_cli.html#ibmcloud_target)

    By default, the `default` resource group is set.

4. Create the instance. Run the [`ibmcloud resource service-instance-create`](/docs/cli/reference/ibmcloud/cli_resource_group.html#ibmcloud_resource_service_instance_create) command:

    ```
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    where

    NAME is the name of the instance

    *logdna* is the name of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.Bluemix_notm}}

    SERVICE_PLAN_NAME is the type of plan. Valid values are: *lite*, *7-days*, *14-days*, *30-days*
    
    LOCATION is the region where the LogDNA instance is created. Valid values are: *us-south*

    For example, to provision an instance with the 7 days retention plan, run the following command:

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna 7-day us-south
    ```
    {: codeblock}

5. Create a service key with **administrator** permissions to operate the instance. Run the [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud/cli_resource_group.html#ibmcloud_resource_service_key_create) command:

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    where

    NAME is the name of the API key. Suggestion: Name the API key like the {{site.data.keyword.la_full_notm}} instance. This will help you  identify the API key later on.

    ROLE_NAME is the role that defines the permissions that are enabled. Valid values are: *editor*, *operator*, *administrator*

    SERVICE_INSTANCE_NAME is the name of the instance in the {{site.data.keyword.Bluemix_notm}}

    For example, to create an API key for the instance *logdna-instance-01* with *administrator* permissions on the service instance, run the following command:

    ```
    ibmcloud resource service-key-create logdna-instance-01 Administrator --instance-name logdna-instance-01
    ```
    {: pre}

    The output from this command includes different values like the `crn` value of the instance and the LogDNA ingestion key.
