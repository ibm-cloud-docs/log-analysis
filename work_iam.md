---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: iam, security, logging, access groups

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

 
# Working with IAM policies and access groups
{: #work_iam}

{{site.data.keyword.iamlong}} (IAM) enables you to securely authenticate users and control access to all cloud resources consistently in the {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

For more information, see [Managing user access with IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).


## Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.cloud_notm}} account
{: #admin_account}

As the **account owner** or as an **{{site.data.keyword.la_full_notm}} service administrator**, you must have permissions to run the following actions: 

* Grant other account members access to work with the service
* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, to grant a user administrator role to manage the service in the account, the user must have an IAM policy for the {{site.data.keyword.la_full_notm}} service with the platform role **Administrator**. You must assign this user access to an individual resource in the account. 

Complete the following steps to assign a user administrator role to the {{site.data.keyword.la_full_notm}} service in the account: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access to resources**.
4. Select **IBM Log Analysis with LogDNA**.
5. Select **All current regions**.
6. Select **All current service instances**.
7. Select the platform role **Administrator**.
8. Click Assign.


## Granting permissions to a user to become an administrator of the service within a resource group
{: #admin_rg}

As an **{{site.data.keyword.la_full_notm}} service administrator**, you must have permissions to run the following actions: 

* Grant other account members access to work with the service
* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, to grant a user administrator role to manage instances within a resource group in the account, the user must have an IAM policy for the {{site.data.keyword.la_full_notm}} service with the platform role **Administrator** within the context of the resource group. 

Complete the following steps to assign a user administrator role to the {{site.data.keyword.la_full_notm}} service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the {{site.data.keyword.la_full_notm}} service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Administrator**.
8. Click **Assign**.


## Granting permissions to a Devops user to manage the service in the {{site.data.keyword.cloud_notm}} account
{: #devops_account}

As a **Devops user**, you must have permissions to run the following actions: 

* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, you need to have an IAM policy for the {{site.data.keyword.la_full_notm}} service with the platform role **Editor**.

Complete the following steps to assign a user editor role to the {{site.data.keyword.la_full_notm}} service in the account: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access to resources**.
4. Select **IBM Log Analysis with LogDNA**.
5. Select **All service instances**.
6. Select the platform role **Editor**.
7. Click Assign.

## Granting permissions to a Devops user to manage an instance in the {{site.data.keyword.cloud_notm}} account
{: #devops_account_instance}

Complete the following steps to assign a user editor role on one instance of the {{site.data.keyword.la_full_notm}} service in the account: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access to resources**.
4. Select **IBM Log Analysis with LogDNA**.
5. Select the instance.
6. Select the platform role **Editor**.
7. Click Assign.



## Granting permissions to a Devops user to manage the service within a resource group
{: #devops_rg}

As a **Devops user**, you must have permissions to run the following actions: 

* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, you need an IAM policy for the {{site.data.keyword.la_full_notm}} service with the platform role **Editor**.

Complete the following steps to assign a user editor role to the {{site.data.keyword.la_full_notm}} service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the {{site.data.keyword.la_full_notm}} service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Editor**.
8. Click **Assign**.

## Granting permissions to manage logs and configure alerts in LogDNA
{: #admin_user_logdna}

As an **admin user** in LogDNA, you must have permissions to run the following actions: 

* Add LogDNA log sources
* View logs
* Search logs
* Filter logs
* Configure alerts

Therefore, you need the following policies:

* An IAM policy for the {{site.data.keyword.la_full_notm}} service with the platform role **Editor**. This policy allows you to view the service instance details through the command line and in the {{site.data.keyword.cloud_notm}} dashboard.
* An IAM policy for the {{site.data.keyword.la_full_notm}} service with the service role **Manager**. This policy allows you to monitor, filter and search log, and define alerts through the LogDNA web UI.

**Note:** As an administrator of the service, when you grant a user these policies, consider doing it within the context of a resource group. An {{site.data.keyword.la_full_notm}} instance is provisioned within the context of a resource group. Therefore, you should grant access permissions within the context of the resource group.


Complete the following steps to assign a user both policies for the {{site.data.keyword.la_full_notm}} service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the {{site.data.keyword.la_full_notm}} service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Editor**.
8. Select the service role **Manager**.
8. Click **Assign**.

## Granting permissions to a user to view logs in LogDNA
{: #user_logdna}

As a **user**, **auditor**, or **developer**, you might need permissions to run the following actions: 

* View logs
* Search logs
* Filter logs

Therefore, you need the following policies:

* An IAM policy for the {{site.data.keyword.la_full_notm}} service with the platform role **Viewer**. This policy allows you to view the service instance details through the command line and in the {{site.data.keyword.cloud_notm}} dashboard.
* An IAM policy for the {{site.data.keyword.la_full_notm}} service with the service role **Reader**. This policy allows you to view, filter and search logs through the LogDNA web UI.

**Note:** As an administrator of the service, when you grant a user these policies, consider doing it within the context of a resource group. An {{site.data.keyword.la_full_notm}} instance is provisioned within the context of a resource group. Therefore, you should grant access permissions within the context of the resource group.

Complete the following steps to assign a user both policies for the {{site.data.keyword.la_full_notm}} service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the {{site.data.keyword.la_full_notm}} service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Viewer**.
8. Select the service role **Reader**.
8. Click **Assign**.

