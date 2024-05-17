---

copyright:
  years: 2022, 2024
lastupdated: "2024-05-17"

keywords: IBM Cloud, Log Analysis, endpoint

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Limiting instance access to only private endpoints
{: #private_endpoints_only}

You can limit access to an {{site.data.keyword.la_full}} instance to private endpoints only.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

You can configure your {{site.data.keyword.la_full_notm}} instance so it is accessible through [private endpoints](/docs/log-analysis?topic=log-analysis-endpoints) only.

If you configure your instance to use private endpoints only, this will block the public endpoints. All ingestion and API usage that may be in progress on the public endpoints will be blocked when the configuration change is made.
{: important}

Unless otherwise specified when provisioning an instance, the default is for the instance to be accessible by both public and private endpoints.
{: note}

## Limiting instances while provisioning
{: #private_endpoints_provisioning}

You can configure your instance to only use private endpoints when you [provision your instance.](/docs/log-analysis?topic=log-analysis-provision)

## Limiting an existing instance
{: #private_endpoint_running}

If you have an exising instance you can change it to use private endpoints only.

### Limiting the instance using the Observability dashboard
{: #pe_dashboard}

If you have an existing {{site.data.keyword.la_full_notm}} instance and need to change it to be accessible by private endpoints only, do the following using the Observability dashboard:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} dashboard opens.

2. Click the **Menu** icon ![Menu icon](../icons/icon_hamburger.svg) &gt; **Observability**.

3. Select **Logging**.

    The list of {{site.data.keyword.la_full_notm}} instances is displayed.

4. Select the instance in the region where you want to view events. Then, click **Open Dashboard**.

5. Select the **settings** icon.

6. Click **Organization** &gt; **General**.

7. For **Private endpoints only** select *on* to limit access to the instance to only [private endpoints](/docs/log-analysis?topic=log-analysis-endpoints).  Select *off* to allow the instance to be accessed by both [public and private endpoints](/docs/log-analysis?topic=log-analysis-endpoints).

### Limiting the instance using the CLI
{: #pe_cli}

If you have an existing {{site.data.keyword.la_full_notm}} instance and need to change it to be accessible by private endpoints only, do the following using the CLI:

1. Install the {{site.data.keyword.cloud_notm}} CLI. [Learn more](/docs/cli?topic=cli-getting-started).

2. Log in to the location in the {{site.data.keyword.cloud_notm}} where the instance is provisioned. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

   To get the latest list of locations that are available for the {{site.data.keyword.la_full_notm}} service, see [Locations](/docs/services/log-analysis?topic=log-analysis-regions).

3. Set the resource group where the instance is available. Run the following command: [ibmcloud target](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target)

   By default, the `default` resource group is set.

4. Change your instance to accept access from private endpoints only. Run the [ibmcloud resource service-instance-update](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_update) command:

   ```text
   ibmcloud resource service-instance-update NAME -p '{"private_endpoints_only": PRIVATE_ENDPOINT}'
   ```
   {: codeblock}

   Where:

   * `NAME` is the name of the instance.

   * `PRIVATE_ENDPOINT` is either `true` or `false`.  If `true` only [private endpoints](/docs/log-analysis?topic=log-analysis-endpoints) can be used to access the instance.


    For example, to change the instance named `my-instance` to be accessible by both public and private endpoints, run the following command:

    ```text
    ibmcloud resource service-instance-update my-instance -p '{"private_endpoints_only": false}'
    ```
    {: codeblock}
