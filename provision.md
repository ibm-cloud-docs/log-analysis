---

copyright:
  years: 2018
lastupdated: "2018-10-22"

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

Before you can monitor and manage log data with IBM Log Analysis with LogDNA, you must first provision an instance of the service in {{site.data.keyword.Bluemix}}.
{:shortdesc}

To provision an IBM Log Analysis with LogDNA instance in a Public Cloud region, you must select the service plan that is associated with the instance, the region where your logs are collected, and the plan that determines the retention period for your logs. You can choose from 7, 14, or 30-day retention periods.

Alternatively, IBM Log Analysis with LogDNA offers a **Free** plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.


## Provisioning an instance through the {{site.data.keyword.Bluemix_notm}} UI
{: #provision_ui}

To provision an instance of IBM Log Analysis with LogDNA by using the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available on {{site.data.keyword.Bluemix_notm}} opens.

3. Filter the list of services that is displayed. Select the **Developer Tools** category.

4. Click the **LogDNA** tile.

5. Select a service plan. By default, the **Free** plan is set.

    For more information about the service plans, see [Service plans](/docs/services/.....).

6. Select a resource group. By default, the **default** one is set.

7. Click **Create** to provision an instance of the service in the {{site.data.keyword.Bluemix_notm}} resource group where you are logged in.

After you provision an instance, the *Edit sources* page opens. A service ID is automatically created. You can use this service ID to get the ingestion key for your instance.

Next, configure a log source by adding a LogDNA agent. This agent is responsible for collecting and forwarding logs to LogDNA.


## Provisioning an instance through the CLI
{: #logdna_provision_cli}

To provision an instance of IBM Log Analysis with LogDNA through the command line, complete the following steps:

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

    * NAME is the name of the instance
    * *logdna** is the name of the IBM Log Analysis with LogDNA service in the {{site.data.keyword.Bluemix_notm}}
    * SERVICE_PLAN_NAME is the type of plan. Valid values are: *lite*, *ibm-7day*, *ibm-14day*, *ibm-30day*
    * LOCATION is the region where the LogDNA instance is created. Valid values are: *us-south*

    For example, to provision an instance with the 7 day retention plan, run the following command:

    ```
    ibmcloud resource service-instance-create logdna-instance-01 logdna ibm-7day us-south
    ```
    {: codeblock}

5. Create a service key with permissions to operate the instance. Run the [`ibmcloud resource service-key-create`](/docs/cli/reference/ibmcloud/cli_resource_group.html#ibmcloud_resource_service_key_create) command:

    ```
    ibmcloud resource service-key-create NAME ROLE_NAME --instance-name SERVICE_INSTANCE_NAME
    ```
    {: codeblock}

    where

    * NAME is the name of the API key. Suggestion: Name the API key like the IBM Log Analysis with LogDNA instance. This will help you  identify the API key later on.
    * ROLE_NAME is the role that defines the permissions that are enabled. Valid values are: *editor*, *operator*, *administrator*
    * SERVICE_INSTANCE_NAME is the name of the instance in the {{site.data.keyword.Bluemix_notm}}

    For example, to create an API key for the instance *logdna-instance-01* with *editor* permissions on the service instance, run the following command:

    ```
    ibmcloud resource service-key-create logdna-instance-01 Editor --instance-name logdna-instance-01
    ```
    {: pre}

    The output from this command includes different values like the `crn` value of the instance and the LogDNA ingestion key.
