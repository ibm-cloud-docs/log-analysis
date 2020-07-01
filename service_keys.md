---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-01"

keywords: LogDNA, IBM, Log Analysis, logging, service keys

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
 
# Managing service keys
{: #service_keys}

In an {{site.data.keyword.la_full_notm}} instance, you can create, delete, and view service keys through the LogDNA web UI. A service key is an API key that you must use to validate your credentials with the auditing instance when you export data programmatically.
{:shortdesc}


## Creating a service key
{: #service_keys_create}

You must have **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

You can only generate a service Key through the LogDNA web UI.
{: important}
    
Complete the following steps to create a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch).

2. Select the **Configuration** icon ![Configuration icon](images/admin.png). Then, select **Organization**. 

3. Select **API keys**.

    You can see the service keys that are created.   

4. Click **Generate Service Key**. A new key is added to the list. 



## Deleting a service key
{: #service_keys_delete}

You must have **manager** role for the {{site.data.keyword.la_full_notm}} service to complete this step.
{: important} 

You can only delete a service Key through the LogDNA web UI.
{: important}

Complete the following steps to delete a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch).

2. Select the **Configuration** icon ![Configuration icon](images/admin.png). Then, select **Organization**. 

3. Select **API keys**.

    You can see the service keys that are created.   

4. Delete the key.


## Viewing a service key
{: #service_keys_view}

Only users that have the **manager** service role or the **standard-member** service role can view service keys.
{: important} 

For more information, see [service roles](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-iam#service).

Complete the following steps to view a service key:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-launch).

2. Select the **Configuration** icon ![Configuration icon](images/admin.png). Then, select **Organization**. 

3. Select **API keys**.

    If you have permissions, you can see the service keys that are available.   


