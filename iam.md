---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, iam, manage user access

subcollection: log-analysis

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

 
# Managing access with IAM
{: #iam}

{{site.data.keyword.iamlong}} (IAM) enables you to securely authenticate users and control access to all cloud resources consistently in the {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

**Every user that accesses the {{site.data.keyword.la_full_notm}} service in your account must be assigned an access policy with an IAM user role defined.** The policy determines what actions the user can perform within the context of the service or instance you select. The allowable actions are customized and defined as operations that are allowed to be performed on the service. The actions are then mapped to IAM user roles.

*Policies* enable access to be granted at different levels. Some of the options include the following: 

* Access to all IAM-enabled services in your account
* Access across all instances of the service in a single region in your account
* Access to an individual service instance in your account
* Access to all instances of the service within the context of a resource group
* Access to all instances of the service in a single region within the context of a resource group
* Access to all IAM-enabled services within the context of a resource group

*Roles* define the actions that a user or serviceID can run. There are different types of roles in the {{site.data.keyword.cloud_notm}}:

* *Platform management roles* enable users to perform tasks on service resources at the platform level, for example assign user access for the service, create or delete service IDs, create instances, assign policies for your service to other users, and bind instances to applications.
* *Service access roles* enable users to be assigned varying levels of permission for calling the service's API.

**To organize a set of users and service IDs into a single entity that makes it easy for you to manage IAM permissions, use *access groups*.** You can assign a single policy to the group instead of assigning the same access multiple times per individual user or service ID.
{: tip}


## Managing access by using access groups
{: #groups}

To manage access or assign new access for users by using access groups, you must be the account owner, administrator or editor on all Identity and Access enabled services in the account, or the assigned administrator or editor for the IAM Access Groups Service. 

Choose any of the following actions to manage access groups in the {{site.data.keyword.cloud_notm}}:

* [Creating an access group](/docs/account?topic=account-groups#create_ag).
* [Assigning access to a group](/docs/account?topic=account-groups#access_ag).


## Managing access by assigning policies directly to users
{: #users}

To manage access or assign new access for users by using IAM policies, you must be the account owner, administrator on all services in the account, or an administrator for the particular service or service instance. 

Choose any of the following actions to manage IAM policies in the {{site.data.keyword.cloud_notm}}:

* To grant permissions to a user, see [Assign access](/docs/account?topic=account-assign-access-resources#assign_new_access).
* To revoke permissions, see [Removing access](/docs/account?topic=account-assign-access-resources#removing_access).
* To review a user's permissions, see [Reviewing your assigned access](/docs/account?topic=account-assign-access-resources#review_your_access).




## {{site.data.keyword.cloud_notm}} platform roles
{: #platform}

Use the following table to identify the platform role that you can grant a user in the {{site.data.keyword.cloud_notm}} to run any of the following platform actions:

| Platform actions                                                          | Administrator                                     | Editor | Operator | Viewer  |
|---------------------------------------------------------------------------|:-------------------------------------------------:|:-------:|:--------:|:------:|
| `Grant other account members access to work with the service`             | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |         |          |        |
| `View the ingestion key in the {{site.data.keyword.cloud_notm}} console`  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")         |          |        |
| `Provision a service instance`                                            | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |      |      |
| `Delete a service instance`                                               | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |        |      |
| `Update a service instance`                                               | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |        |      |
| `Create a service ID`                                                     | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |        |      |
| `View details of a service instance`                                      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |
| `View service instances in the Observability Logging dashboard`           | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |
{: caption="Table 1. IAM user platform roles and actions" caption-side="top"}


## {{site.data.keyword.cloud_notm}} service roles
{: #service}

Use the following table to identify the service roles that you can grant a user to run any of the following service actions:

| Actions            | Manager           | Standard-Member        | Reader |
|-------------|----------------------|----------------------------|----------|
| `Configure global settings` | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |    |   |
| `Manage groups`   | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |  |  |
| `Create and delete ingestion keys through the logging web UI`   | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |     |   |
| `Create and delete service keys through the logging web UI`     | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |  |   |
| `Add logging log sources`  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |              |   |
| `Configure archiving`  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |    |   |
| `Manage parsing`     | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |       |   |
| `Define exclusion rules`   | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |       |   |
| `Create and delete categories`    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |       |   |
| `Manage how views and dashboards are grouped in categories` | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |      |   |
| `Export the configuration of views, alerts, dashboards, and templates`  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |     |   |
| `Export log data`     | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")  | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") | |
| `View service keys through the logging web UI`                           | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage") |     |
| `Configure alerts`                                                      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    |    |
| `View usage`                                                            | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                   |      |
| `Create views`                                                          | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    |      |
| `Create dashboards`                                                     | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    |     |
| `Create screens`                                                        | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    |     |
| `Configure user preferences in the logging web UI`                       | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |
| `Filter and search data`                                                | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |
| `Use views to monitor logs`                                           | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |
| `Use dashboards to monitor logs`                                      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |
| `Use screens to monitor logs`                                      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")      | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")                    | ![Check mark icon](images/checkmark-icon.svg "Check mark icon indicating correct usage")    |
{: caption="Table 2. IAM service roles and actions" caption-side="top"}


The **manager** service role maps directly to the logging admin role.
{: note}



## IAM actions
{: #iam_actions}

The following table identifies the IAM actions that are assigned to the platform and service roles for the {{site.data.keyword.la_full_notm}} service:

| Role type         | Role              | IAM actions |
|-------------------|-------------------|--------------|
| Platform          | `administrator`   | `logdna.dashboard.view` </br>`logdna.dashboard.manage` | 
| Service           | `manager`         | `logdna.dashboard.view` </br>`logdna.dashboard.manage` |
| Service           | `writer`          | `logdna.dashboard.view` </br>`logdna.dashboard.member` |
| Service           | `reader`          | `logdna.dashboard.view` </br>`logdna.dashboard.read` |
{: caption="Table 3. IAM actions assigned to platform and service roles" caption-side="top"}



## How do I know which access policies are set for me?
{: #iam_accesspolicy}

You can see which access policies are set for you in the [{{site.data.keyword.cloud_notm}} UI](https://cloud.ibm.com/){: external} console.

1. Go to [Access IAM users](https://cloud.ibm.com/iam/users){: external}.
2. Click your name in the user table.
3. Click the **Access policies** tab to see your access policies.
4. Click the **Access groups** tab to see the access groups where you are a member. Check the policies for each group.



