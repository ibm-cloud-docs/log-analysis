---

copyright:
  years:  2018, 2020
lastupdated: "2020-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# Removing an instance
{: #remove}

You can remove an instance of the {{site.data.keyword.la_full_notm}} service from the {{site.data.keyword.Bluemix}} UI or through the command line.
{:shortdesc}

When you remove an instance from the {{site.data.keyword.cloud_notm}}, clean up by completing the following tasks:

1. Write down the list of sources that forward metrics to the {{site.data.keyword.la_full_notm}} instance that you want to remove. You must remove the LogDNA agent from each source.
2. Remove permissions that are granted to users to work with the instance. 

    If you manage access by using dedicated access groups to work with a specific instance, you must remove these access groups.

    If you manage access to multiple logging instances by using access groups, you must remove the policies that grant permissions to the instance that you want to remove.
    
    If you grant individual policies to users, you must gather the list of users that have permissions to work with that instance. Then, for each user that you identify, you must remove the policies that relate to the instance that you want to delete.


Then, delete the instance from the {{site.data.keyword.cloud_notm}} Dashboard.


## Removing an instance through the {{site.data.keyword.cloud_notm}} UI
{: #remove_ui}

To remove an instance of {{site.data.keyword.la_full_notm}} by using the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. [Log in to your {{site.data.keyword.cloud_notm}} account ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Go to the menu icon ![menu icon](../../icons/icon_hamburger.svg) &gt; **Observability** to access the *Observability* Dashboard.

3. Select **Logging**. The list of logging instances is displayed.

4. Select the instance that you want to delete.

5. From the *Action* menu, select **Remove**.


## Removing an instance through the CLI
{: #remove_cli}

To remove an instance of {{site.data.keyword.la_full_notm}} through the command line, complete the following steps:

1. [Pre-requisite] Installion of the {{site.data.keyword.cloud_notm}} CLI.

   For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   If the CLI is installed, continue with the next step.

2. Log in to the region in the {{site.data.keyword.cloud_notm}} where you want to provision the instance. Run the following command: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Set the resource group where the instance is provisioned. Run the following command: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    By default, the *default* resource group is set.

4. Remove the instance. Run the [`ibmcloud resource service-instance-delete`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) command:

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    Where NAME is the name of the instance.

    For example, to remove an instance, run the following command:

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



