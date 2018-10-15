---

copyright:
  years:  2018
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

 
# Managing user access with Identity and Access Management (IAM)
{: #iam}

{{site.data.keyword.iamlong}} (IAM) enables you to securely authenticate users and control access to all cloud resources consistently in the {{site.data.keyword.Bluemix_notm}}. 
{:shortdesc}

Every user that accesses the IBM Log Analysis with LogDNA service in your account must be assigned an access policy with an IAM user role defined. That policy determines what actions the user can perform within the context of the service or instance you select. The allowable actions are customized and defined as operations that are allowed to be performed on the service. The actions are then mapped to IAM user roles.

Policies enable access to be granted at different levels. Some of the options include the following: 

* Access to all IAM-enabled services in your account
* Access across all instances of the service in a single region in your account
* Access to an individual service instance in your account
* Access to all instances of the service within the context of a resource group
* Access to all instances of the service in a single region within the context of a resource group
* Access to all IAM-enabled services within the context of a resource group

After you define the scope of the access policy, you assign a role:

* Platform management roles enable users to perform tasks on service resources at the platform level, for example assign user access for the service, create or delete service IDs, create instances, assign policies for your service to other users, and bind instances to applications.
* Service access roles enable users to be assigned varying levels of permission for calling the service's API.

Choose any of the following actions to manage IAM policies in the {{site.data.keyword.Bluemix_notm}}:

* To modify the permissions of a user, see [Editing existing access](/docs/iam/mngiam.html#editing-existing-access).
* To grant permissions to a user, see [Assign new access](/docs/iam/mngiam.html#assignaccess).
* To revoke permissions, see [Removing access](/docs/iam/mngiam.html#removing-access).
* To review a user's permissions, see [Reviewing your assigned access](/docs/iam/mngiam.html#reviewing-your-assigned-access).

**Note:** To manage access or assign new access for users by using IAM policies, you must be the account owner, administrator on all services in the account, or an administrator for the particular service or service instance.{: tip}

## Granting permissions to a user to become an administrator of the service in the {{site.data.keyword.Bluemix_notm}} account
{: #admin_account}

As the **account owner** or as an **IBM Log Analysis with LogDNA service administrator**, you must have permissions to run the following actions: 

* Grant other account members access to work with the service
* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, to grant a user administrator role to manage the service in the account, the user must have an IAM policy for the IBM Log Analysis with LogDNA service with the platform role **Administrator**. You must assign this user access to an individual resource in the account. 

Complete the following steps to assign a user administrator role to the IBM Log Analysis with LogDNA service in the account: 

1. From the menu bar, click **Manage** &gt; **Security** &gt; **Identity and Access**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access to resources**.
4. Select **IBM Log Analysis with LogDNA**.
5. Select **All current regions**.
6. Select **All current service instances**.
7. Select the platform role **Administrator**.
8. Click Assign.


## Granting permissions to a user to become an administrator of the service within a resource group
{: #admin_rg}

As an **IBM Log Analysis with LogDNA service administrator**, you must have permissions to run the following actions: 

* Grant other account members access to work with the service
* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, to grant a user administrator role to manage instances within a resource group in the account, the user must have an IAM policy for the IBM Log Analysis with LogDNA service with the platform role **Administrator** within the context of the resource group. 

Complete the following steps to assign a user administrator role to the IBM Log Analysis with LogDNA service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Security** &gt; **Identity and Access**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the IBM Log Analysis with LogDNA service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Administrator**.
8. Click **Assign**.


## Granting permissions to a Devops user to manage the service in the {{site.data.keyword.Bluemix_notm}} account
{: #devops_account}

As a **Devops user**, you must have permissions to run the following actions: 

* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, you need to have an IAM policy for the IBM Log Analysis with LogDNA service with the platform role **Editor**.

Complete the following steps to assign a user editor role to the IBM Log Analysis with LogDNA service in the account: 

1. From the menu bar, click **Manage** &gt; **Security** &gt; **Identity and Access**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access to resources**.
4. Select **IBM Log Analysis with LogDNA**.
5. Select **All current regions**.
6. Select **All current service instances**.
7. Select the platform role **Editor**.
8. Click Assign.

## Granting permissions to a Devops user to manage the service within a resource group
{: #devops_rg}

As a **Devops user**, you must have permissions to run the following actions: 

* Provision a service instance
* Delete a service instance
* View details of a service instance
* Create a service ID

Therefore, you need an IAM policy for the IBM Log Analysis with LogDNA service with the platform role **Editor**.

Complete the following steps to assign a user editor role to the IBM Log Analysis with LogDNA service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Security** &gt; **Identity and Access**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the IBM Log Analysis with LogDNA service in the resource group.

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

* An IAM policy for the IBM Log Analysis with LogDNA service with the platform role **Viewer**. This policy allows you to view the service instance details through the command line and in the {{site.data.keyword.Bluemix_notm}} dashboard.
* An IAM policy for the IBM Log Analysis with LogDNA service with the service role **Manager**. This policy allows you to monitor, filter and search log, and define alerts through the LogDNA web UI.

**Note:** As an administrator of the service, when you grant a user these policies, consider doing it within the context of a resource group. An IBM Log Analysis with LogDNA instance is provisioned within the context of a resource group. Therefore, you should grant access permissions within the context of the resource group.


Complete the following steps to assign a user both policies for the IBM Log Analysis with LogDNA service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Security** &gt; **Identity and Access**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the IBM Log Analysis with LogDNA service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Editor**.
8. Select the service role **Manager**.
8. Click **Assign**.

## Granting permissions to a user to view and manage logs in LogDNA
{: #user_logdna}

As a **developer**, you must have permissions to run the following actions: 

* View logs
* Search logs
* Filter logs

Therefore, you need the following policies:

* An IAM policy for the IBM Log Analysis with LogDNA service with the platform role **Viewer**. This policy allows you to view the service instance details through the command line and in the {{site.data.keyword.Bluemix_notm}} dashboard.
* An IAM policy for the IBM Log Analysis with LogDNA service with the service role **Writer**. This policy allows you to monitor, filter and search logs through the LogDNA web UI.

**Note:** As an administrator of the service, when you grant a developer these policies, consider doing it within the context of a resource group. An IBM Log Analysis with LogDNA instance is provisioned within the context of a resource group. Therefore, you should grant access permissions within the context of the resource group.

Complete the following steps to assign a user both policies for the IBM Log Analysis with LogDNA service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Security** &gt; **Identity and Access**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the IBM Log Analysis with LogDNA service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Editor**.
8. Select the service role **Writer**.
8. Click **Assign**.



## {{site.data.keyword.Bluemix_notm}} platform roles
{: #platform}

Use the following table to identify the role that you can grant a user in the {{site.data.keyword.Bluemix_notm}} to run any of the following platform actions:

| Actions                                                                 | {{site.data.keyword.Bluemix_notm}} Platform Roles    | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `Grant other account members access to work with the service`           | Administrator                                        | 
| `Provision a service instance`                                          | Administrator </br>Editor                            | 
| `Delete a service instance`                                             | Administrator </br>Editor                            | 
| `Create a service ID`                                                   | Administrator </br>Editor                            |
| `View details of a service instance`                                    | Administrator </br>Editor </br>Operator </br>Viewer  | 
{: caption="Table 1. IAM user roles and actions" caption-side="top"}




## {{site.data.keyword.Bluemix_notm}} service roles
{: #service}

Use the following table to identify the roles that you can grant a user to run any of the following service actions:

| Actions                                                                 | {{site.data.keyword.Bluemix_notm}} Service Roles     | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `Add LogDNA log sources`                                                | Manager                                              |
| `Configure alerts`                                                      | Manager                                              | 
| `Manage log data`                                                       | Manager                                              |
| `Manage the LogDNA Web UI`                                              | Manager                                              |
| `View logs through the LogDNA Web UI`                                   | Manager </br>Writer </br>Reader                      | 
{: caption="Table 2. IAM user roles and actions" caption-side="top"}








