---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords: IBM, Log Analysis, logging instance, delete

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Removing an instance
{: #remove}

You can remove an instance of the {{site.data.keyword.la_full_notm}} service from the {{site.data.keyword.cloud_notm}} UI or through the command line.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

When you remove an instance from the {{site.data.keyword.cloud_notm}}, clean up by completing the following tasks:

1. Write down the list of sources that forward metrics to the {{site.data.keyword.la_full_notm}} instance that you want to remove. You must remove the logging agent from each source.
2. Remove permissions that are granted to users to work with the instance.

    If you manage access by using dedicated access groups to work with a specific instance, you must remove these access groups.

    If you manage access to multiple logging instances by using access groups, you must remove the policies that grant permissions to the instance that you want to remove.

    If you grant individual policies to users, you must gather the list of users that have permissions to work with that instance. Then, for each user that you identify, you must remove the policies that relate to the instance that you want to delete.


Then, delete the instance from the {{site.data.keyword.cloud_notm}} Dashboard.


## Removing an instance through the {{site.data.keyword.cloud_notm}} UI
{: #remove_ui}

To remove an instance of {{site.data.keyword.la_full_notm}} by using the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Go to the menu icon ![menu icon](../icons/icon_hamburger.svg) &gt; **Observability** to access the *Observability* Dashboard.

3. Click **Logging**. The list of logging instances is displayed.

4. Click the **Actions** icon ![Actions icon](../icons/action-menu-icon.svg) next to the instance that you want to delete.

5. Click **Delete**.


## Removing an instance through the CLI
{: #remove_cli}

To remove an instance of {{site.data.keyword.la_full_notm}} through the command line, complete the following steps:

1. [Pre-requisite] Install the {{site.data.keyword.cloud_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

2. Log in to {{site.data.keyword.cloud_notm}}. Run the following command: [ibmcloud login](/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login)

3. Get information about the instance that you plan to delete.

    ```text
    ibmcloud resource service-instance INSTANCE-NAME --output JSON
    ```
    {: codeblock}

4. Remove any service key associated with the instance.

    Find the service keys that are associated with an instance:

    ```text
    ibmcloud resource service-keys --instance-id INSTANCE-GUID
    ```
    {: codeblock}

    Run the following command to delete 1 service key. You must delete all.

    ```text
    ibmcloud resource service-key-delete SERVICE-KEY-NAME
    ```
    {: codeblock}

5. Remove the instance. Run the [ibmcloud resource service-instance-delete](/docs/cli?topic=cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) command:

    ```text
    ibmcloud resource service-instance-delete NAME
    ```
    {: codeblock}

    Where NAME is the name of the instance.

    For example, to remove an instance, run the following command:

    ```text
    ibmcloud resource service-instance-delete logging-instance-01
    ```
    {: codeblock}
