---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging instance, provision

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Provisioning an instance
{: #provision}

Before you can monitor and manage log data with {{site.data.keyword.la_full_notm}}, you must first provision an instance of the service in {{site.data.keyword.cloud_notm}}.
{: shortdesc}

To provision an {{site.data.keyword.la_full_notm}} instance in a Public Cloud region, you must select the service plan that is associated with the instance, the location where  logs are collected, and the plan that determines the retention period for your logs. You can choose from 7, 14, or 30-day retention periods.

Alternatively, {{site.data.keyword.la_full_notm}} offers a `Lite` plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.


## Provisioning an instance through the Observability dashboard
{: #provision_ui}

To provision an instance from the Observability dashboard in the {{site.data.keyword.cloud_notm}}, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability** to access the *Observability* dashboard.

3. Click **Logging**, then click **Options** > **Create**. 

4. Enter a name for the service instance.

5. Select the [location](/docs/log-analysis?topic=log-analysis-regions) where you plan to provision the instance. 

6. Select a resource group. 

    By default, the **default** resource group is set.

    **Note:** If you are not able to select a resource group, check that you have editing permissions on the resource group where you want to provision the instance.

7. Select the `Lite` service plan. 

    By default, the lite plan is set.

    For more information about other service plans, see [Pricing plans](/docs/log-analysis?topic=log-analysis-service_plans).

8. Click **Create**.

After you provision an instance, the *Logging* dashboard opens. 

Next, configure a log source by adding a logging agent. This agent is responsible for collecting and forwarding logs to your instance. 



## Provisioning an instance through the catalog
{: #provision_catalog}

To provision an instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} catalog, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. To filter the list of services that is displayed, select the **Logging and Monitoring** category.

4. Click the **{{site.data.keyword.la_full_notm}}** tile. 

5. Select the [location](/docs/log-analysis?topic=log-analysis-regions) where you plan to provision the instance. 

6. Enter a name for the service instance.

7. Select a resource group. 

    By default, the **Default** resource group is set.

    **Note:** If you are not able to select a resource group, check that you have editing permissions on the resource group where you want to provision the instance.

8. Select the `Lite` service plan. 

    By default, the lite plan is set.

    For more information about other service plans, see [Pricing plans](/docs/log-analysis?topic=log-analysis-service_plans).

9. Click **Create**.

After you provision an instance, the *Logging* dashboard opens. 

Next, configure a log source by adding a logging agent. This agent is responsible for collecting and forwarding logs to your instance. 



## Provisioning an instance through the CLI
{: #provision_cli}

To provision an instance of {{site.data.keyword.at_full_notm}} through the command line, you must provision an instance, and create the credentials for that instance.

### Step 1. Provision an instance
{: #provision_cli_1}

1. [Pre-requisite] Installation of the {{site.data.keyword.cloud_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where you want to provision the instance. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where you want to provision the instance. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Create the instance. Run the [ibmcloud resource service-instance-create](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) command:

    ```
    ibmcloud resource service-instance-create NAME la_service SERVICE_PLAN_NAME LOCATION
    ```
    {: codeblock}

    Where

    `NAME` is the name of the instance

    The value *la_service* is the name of the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}}.

    `SERVICE_PLAN_NAME` is the type of plan. Valid values are *lite*, *7-days*, *14-days*, *30-days*.
    
    `LOCATION` is the region where the logging instance is created. To get the latest list of locations that are available for the {{site.data.keyword.la_full_notm}} service, see [Locations](/docs/log-analysis?topic=log-analysis-regions).

    For example, to provision an instance with the 7 days retention plan, run the following command:

    ```
    ibmcloud resource service-instance-create logging-instance-01 la_service 7-day us-south
    ```
    {: pre}


### Step 2. Create the credentials for your instance
{: #provision_cli_2}

Run the following command to create a service ID:

```
ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
```
{: pre}

Where 

* `SERVICE_INSTANCE_NAME` is the name of the instance that you provisioned in the previous step.
* `NAME` is the name of the service ID. Use the following format to name the key **<SERVICE_INSTANCE_NAME>-key-admin**
* `ROLE_NAME` is the permission that you grant this service ID. Set it to **Manager**.

 
For example, you can run the following command:

```
ibmcloud resource service-key-create logging-via-cli-key-admin Manager --instance-name logging-via-cli
```
{: pre}



