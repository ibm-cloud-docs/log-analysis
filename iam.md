---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, iam, manage user access

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

 
# Managing user access with IAM
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

* [Creating an access group](/docs/iam?topic=iam-groups#create_ag).
* [Assigning access to a group](/docs/iam?topic=iam-groups#access_ag).


## Managing access by assigning policies directly to users
{: #users}

To manage access or assign new access for users by using IAM policies, you must be the account owner, administrator on all services in the account, or an administrator for the particular service or service instance. 

Choose any of the following actions to manage IAM policies in the {{site.data.keyword.cloud_notm}}:

* To modify the permissions of a user, see [Editing existing access](/docs/iam?topic=iam-iammanidaccser#edit_existing).
* To grant permissions to a user, see [Assign new access](/docs/iam?topic=iam-iammanidaccser#assign_new_access).
* To revoke permissions, see [Removing access](/docs/iam?topic=iam-iammanidaccser#removing_access).
* To review a user's permissions, see [Reviewing your assigned access](/docs/iam?topic=iam-iammanidaccser#review_your_access).




## {{site.data.keyword.cloud_notm}} platform roles
{: #platform}

Use the following table to identify the platform role that you can grant a user in the {{site.data.keyword.cloud_notm}} to run any of the following platform actions:

| Platform actions                                                         | {{site.data.keyword.cloud_notm}} Platform Roles    | 
|--------------------------------------------------------------------------|------------------------------------------------------|
| `Grant other account members access to work with the service`            | Administrator                                        | 
| `Provision a service instance`                                           | Editor                            | 
| `Delete a service instance`                                              | Administrator </br>Editor                            | 
| `Create a service ID`                                                    | Administrator </br>Editor                            |
| `View details of a service instance`                                     | Administrator </br>Editor </br>Operator </br>Viewer  | 
| `View service instances in the Observability Logging dashboard`          | Administrator </br>Editor </br>Operator </br>Viewer  | 
| `View the ingestion key in the {{site.data.keyword.cloud_notm}} console` | Administrator                                        | 
{: caption="Table 1. IAM user roles and actions" caption-side="top"}



## {{site.data.keyword.cloud_notm}} service roles
{: #service}

Use the following table to identify the service roles that you can grant a user to run any of the following service actions:

| Actions                                                                 | {{site.data.keyword.cloud_notm}} Service Roles     | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `Add LogDNA log sources`                                                | Manager                                              |
| `Manage ingestion keys through the logDNA web UI`                       | Manager </br>Writer </br>Reader                       |
| `Manage service keys`                                                   | Manager                                              |
| `Archive logs`                                                          | Manager                                              |
| `Manage parsing`                                                        | Manager                                              |
| `Configure alerts`                                                      | Manager </br>Writer </br>Reader                      | 
| `Filter and search log data`                                            | Manager </br>Writer </br>Reader                      |
| `Create views`                                                          | Manager </br>Writer </br>Reader                      |
| `Manage views`                                                          | Manager </br>Writer </br>Reader                      |
| `Export log data`                                                       | Manager </br>Writer </br>Reader                      |
| `Configure user preferences in the LogDNA web UI`                       | Manager </br>Writer </br>Reader                      |
| `View logs through the LogDNA web UI`                                   | Manager </br>Writer </br>Reader                      | 
{: caption="Table 3. IAM user roles and actions" caption-side="top"}


**Note:** The **manager** service role maps directly to the LogDNA admin role.





