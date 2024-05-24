---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging instance, provision

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Provisioning an instance
{: #provision}

Before you can monitor and manage log data with {{site.data.keyword.la_full_notm}}, you must first provision an instance of the service in {{site.data.keyword.cloud_notm}}.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

To provision an {{site.data.keyword.la_full_notm}} instance in a Public Cloud region, you must select the service plan that is associated with the instance, the location where  logs are collected, and the plan that determines the retention period for your logs. You can choose from 7, 14, or 30-day retention periods.

Alternatively, {{site.data.keyword.la_full_notm}} offers a `Lite` plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.

You must also decide if you want your instance to be accessible through both public and private endpoints, or only private endpoints.

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

## Configuring your instance to be accessible to private endpoints only
{: #config_private_endpoints}

After provisioning your instance through the Observability dashboard or catalog, you can configure the instance to be accessibile by private endpoints only.

If you configure your instance to use private endpoints only, this will block the public endpoints. All ingestion and API usage that may be in progress on the public endpoints will be blocked when the configuration change is made.
{: important}

Unless otherwise specified when provisioning an instance, the default is for the instance to be accessible by both public and private endpoints.
{: note}

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} dashboard opens.

2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**.

3. Select **Logging**.

    The list of {{site.data.keyword.la_full_notm}} instances is displayed.

4. Select the instance in the region where you want to view events. Then, click **Open Dashboard**.

5. Select the **settings** icon.

6. Click **Organization** &gt; **General**.

7. For **Private endpoints only** select *on* to limit access to the instance to only [private endpoints](/docs/log-analysis?topic=log-analysis-endpoints).  Select *off* to allow the instance to be accessed by both [public and private endpoints](/docs/log-analysis?topic=log-analysis-endpoints).

## Provisioning an instance through the CLI
{: #provision_cli}

To provision an instance of {{site.data.keyword.la_full_notm}} through the command line, you must provision an instance, and create the credentials for that instance.

### Step 1. Provision an instance
{: #provision_cli_1}

1. [Pre-requisite] Installation of the {{site.data.keyword.cloud_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where you want to provision the instance. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where you want to provision the instance. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

    By default, the `default` resource group is set.

4. Create the instance. Run the [ibmcloud resource service-instance-create](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_create) command:

    ```text
    ibmcloud resource service-instance-create NAME logdna SERVICE_PLAN_NAME LOCATION -p '{"private_endpoints_only": PRIVATE_ENDPOINT}'
    ```
    {: codeblock}

    Where

    `NAME` is the name of the instance

    `SERVICE_PLAN_NAME` is the type of plan. Valid values are *lite*, *7-day*, *14-day*, *30-day*.

    `LOCATION` is the region where the logging instance is created. To get the latest list of locations that are available for the {{site.data.keyword.la_full_notm}} service, see [Locations](/docs/log-analysis?topic=log-analysis-regions).

    * `PRIVATE_ENDPOINT` is either `true` or `false`.  If `true` only [private endpoints](/docs/log-analysis?topic=log-analysis-endpoints) can be used to access the instance.

       Unless otherwise specified when provisioning an instance, the default is for the instance to be accessible by both public and private endpoints.
       {: note}

    For example, to provision an instance with the 7 days retention plan that can be accessed only by private endpoints, run the following command:

    ```text
    ibmcloud resource service-instance-create my-instance logdna 7-day us-south -p '{"private_endpoints_only": true}'
    ```
    {: codeblock}

    To provision an instance with the 14 days retention plan that can be accessed only by both public and private endpoints, run one of the following commands:

    ```text
    ibmcloud resource service-instance-create my-instance logdna 14-day us-south -p '{"private_endpoints_only": false}'
    ```
    {: codeblock}

    or

    ```text
    ibmcloud resource service-instance-create my-instance logdna 14-day us-south
    ```
    {: codeblock}


### Step 2. Create the credentials for your instance
{: #provision_cli_2}

Run the following command to create a service ID:

```text
ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
```
{: pre}

Where

* `SERVICE_INSTANCE_NAME` is the name of the instance that you provisioned in the previous step.
* `NAME` is the name of the service ID. Use the following format to name the key **<SERVICE_INSTANCE_NAME>-key-admin**
* `ROLE_NAME` is the permission that you grant this service ID. Set it to **Manager**.


For example, you can run the following command:

```text
ibmcloud resource service-key-create my-instance-key-admin Manager --instance-name my-instance
```
{: pre}
