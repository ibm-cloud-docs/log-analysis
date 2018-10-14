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

 
# Managing user access with Identity and Access Management
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

To manage access or assign new access for users by using IAM policies, you must be the account owner, administrator on all services in the account, or an administrator for the particular service or service instance. 

Choose any of the following actions to manage IAM policies in the {{site.data.keyword.Bluemix_notm}}:

* To modify the permissions of a user, see [Editing existing access](/docs/iam/mngiam.html#editing-existing-access).
* To grant permissions to a user, see [Assign new access](/docs/iam/mngiam.html#assignaccess).
* To revoke permissions, see [Removing access](/docs/iam/mngiam.html#removing-access).
* To review a user's permissions, see [Reviewing your assigned access](/docs/iam/mngiam.html#reviewing-your-assigned-access).


## {{site.data.keyword.Bluemix_notm}} platform roles
{: #platform}

Use the following to table to identify the role that you can grant a user in the {{site.data.keyword.Bluemix_notm}} to run any of the following platform actions:

| Actions                                                                 | {{site.data.keyword.Bluemix_notm}} Platform Roles    | 
|:------------------------------------------------------------------------|:-----------------------------------------------------|
| `Grant other account members access to work with the service`           | Administrator                                        | 
| `Provision a service instance`                                          | Administrator </br>Editor                            | 
| `Delete a service instance`                                             | Administrator </br>Editor                            | 
| `Create a service ID`                                                   | Administrator </br>Editor                            |
| `View details of a service instance`                                    | Operator </br>Viewer                                 | 
{: caption="Table 1. IAM user roles and actions" caption-side="top"}


The following table maps the LogDNA roles to Platform {{site.data.keyword.Bluemix_notm}} roles:

| LogDNA role                              |  {{site.data.keyword.Bluemix_notm}} role  |
|:-----------------------------------------|:------------------------------------------|
| Admin role                               | Administrator                             |
| NO role                                  | Operator </br>Viewer                      |
{: caption="Table 2. Mapping of LogDNA roles to Platform {{site.data.keyword.Bluemix_notm}} roles" caption-side="top"}


## {{site.data.keyword.Bluemix_notm}} service roles
{: #service}

Use the following to table to identify the roles that you can grant a user to run any of the following service actions:

| Actions                                                                 | {{site.data.keyword.Bluemix_notm}} Platform Roles    | 
|:------------------------------------------------------------------------|:-----------------------------------------------------|
| `Access all log data`                                                   | Manager
| `View logs                                                  `           | Manager </br>Writer                                  | 
{: caption="Table 3. IAM user roles and actions" caption-side="top"}

The following table maps LogDNA roles to service {{site.data.keyword.Bluemix_notm}} roles:

| LogDNA role                              |  {{site.data.keyword.Bluemix_notm}} role  |
|:-----------------------------------------|:------------------------------------------|
| Admin role                               | Manager                                   |
| User  role                               | Writer                                    |
| NO role                                  | Reader                                    |
{: caption="Table 4. Mapping of LogDNA roles to service {{site.data.keyword.Bluemix_notm}} roles" caption-side="top"}








