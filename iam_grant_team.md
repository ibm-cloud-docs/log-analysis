---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: groups, access

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
{:external: target="_blank" .external}

# RBAC, groups and IAM integration
{: #iam_grant_group}

{{site.data.keyword.iamlong}} (IAM) enables you to securely authenticate users and consistently control access to all cloud resources in the {{site.data.keyword.cloud_notm}}. Groups provide an isolated workspace in an {{site.data.keyword.la_full_notm}} instance for a user or group of users to have access to auditing events in a defined scope. 
{:shortdesc}

IAM can map a combination of groups and roles so that a user only has access to a specific set of auditing events and can take a defined set of actions within the product.
{: note}

Groups provide additional security by only allowing users to see a subset of auditing events, as opposed to all auditing events that are generated in the account. For example, you could grant a group of users access to only see auditing events that are related to development services in the account.

In an {{site.data.keyword.la_short}} instance, you can define 1 or more groups. 
- A group provides an isolated workspace for a user or group of users to have access to auditing events with a defined scope. 
- An administrator of the service can configure multiple groups.

By default, when you grant a user access to work with the {{site.data.keyword.la_short}} service, the user can see all auditing events. 
- A user can be a member of 1 or more groups. 
- Users in a group have access to the data that is in scope of the group.


For a user to monitor data within the context of a group, you must grant the user a policy for the {{site.data.keyword.la_full_notm}} service. The policy specifies the group and the service permissions for the user so the user can work with the data in scope for that group. 


You can grant any of the following IAM service roles:
- Standard-member: A standard-member role allows a user to monitor data through views, dashboards, screens, and alerts, and to manage resources such as dashboards, and alerts that are in scope for the group.
- Reader: A reader role allows a user to monitor data through views, dashboards, screens, and alerts that are in scope for the group.
- Manager: The manager role is an instance level role that grants administrative permissions. If you grant this role in a policy for a group, you are granting admin permissions over the instance to the users that belong to that group.


The following table shows the user roles that you can grant a user to work with the {{site.data.keyword.la_short}} service:

| User role            | IAM service role |
|----------------------|------------------|
| `ROLE_USER`          | `reader`         |
| `ROLE_ADVANCED_USER` | `standard-member` |
| `ROLE_ADMIN`         | `manager`        | 
{: caption="Table 1. List of user roles" caption-side="top"} 


The following table shows the group roles that you can grant users to work within the context of a group in an {{site.data.keyword.la_short}} instance:

| Team role            | IAM service role | logGroup   |
|----------------------|------------------|--------|
| `ROLE_GROUP_READ`     | `reader`         | Custom group |
| `ROLE_GROUP_EDIT`     | `standard-member` | Custom group |
| `ROLE_GROUP_ADMIN`    | `manager`        | Custom group |
{: caption="Table 2. List of group roles" caption-side="top"} 

You can define in the {{site.data.keyword.la_short}} UI more groups to define different levels of access to data per group and set of users.

To grant a user access to 1 or more groups, an administrator must grant the user a policy for each group that the user needs access to. By using individual policies for each group, administrators can define different service access and permissions levels to work with data in the auditing instance.

For example, a user that needs to work in a group requires the following policies:
* A policy with a platform role **viewer** to allow the user to see auditing instances in the {{site.data.keyword.cloud_notm}}. 
* A policy to grant the user access to 1 group. The service role determines the permissions of the user to work with data that is in scope for the group.


Complete the following steps to grant a user or service ID permissions to work with the {{site.data.keyword.la_full_notm}} service within the context of a group.


## Prerequisites
{: #iam_grant_group_prereq}

Your user ID needs **administrator platform permissions** to manage the {{site.data.keyword.la_full_notm}} service. The account owner can grant user access to the account for the purposes of managing user access and managing account resources. [Learn more](/docs/account?topic=account-userroles).


## Step 1. Create an IAM access group
{: #iam_grant_group_step1}

Do the following to create an access group:

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and select **Access Groups**.
2. Click **Create**.
3. Enter a name and optional description for your group, and click **Create**.

You can delete a group by selecting the **Remove group** option. When you remove a group from the account, you are removing all users and service IDs from the group and all access that is assigned to the group.
{: note}

To create an access group by using the CLI, you can use the [ibmcloud iam access-group-create](/docs/cli?topic=cli-ibmcloud_commands_iam#ibmcloud_iam_access_group_create) command.

```
ibmcloud iam access-group-create GROUP_NAME [-d, --description DESCRIPTION]
```
{: codeblock}




## Step 2. Add permissions to view {{site.data.keyword.la_short}} instances in the Observability UI
{: #iam_grant_group_step2}

After you set up your access group, you can assign a common access policy to the group. You must add permissions to view {{site.data.keyword.la_short}} instances in the Observability UI. 

Any policy that you set for an access group applies to all entities, users, and service IDs within the group. 
{: note}

You can assign the policy by using the UI or through the command line. 

When you define the policy, you need to select a platform role. Platform management roles cover a range of actions, including the ability to create and delete instances, manage aliases, bindings, and credentials, and manage access. Valid platform roles are administrator, editor, operator, viewer. 


### Add permissions through the CLI
{: #iam_grant_group_step2_1}

To create an access group policy by using the CLI, you can use the [ibmcloud iam access-group-policy-create](/docs/cli?topic=cli-ibmcloud_commands_iam#ibmcloud_iam_access_group_policy_create) command with the **viewer** role.

```
ibmcloud iam access-group-policy-create GROUP_NAME {-f, --file @JSON_FILE | --roles ROLE_NAME1,ROLE_NAME2... [--service-name SERVICE_NAME] [--service-instance SERVICE_INSTANCE] [--region REGION] [--resource-type RESOURCE_TYPE] [--resource RESOURCE] [--resource-group-name RESOURCE_GROUP_NAME] [--resource-group-id RESOURCE_GROUP_ID]}
```
{: codeblock}

For example, you can run the following command to grant a user viewer permissions:

```
ibmcloud iam access-group-policy-create my-access-group --roles Viewer --service-name my-auditing-instance --service-instance 99999999-9999-9999-999999
```
{: pre}


### Add permissions through the UI
{: #iam_grant_group_step2_2}

Complete the following steps to assign a policy to an access group through the UI:

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and select **Access Groups**.
2. Select the name of the group that you want to assign access to. 
3. Click **Access policies**  &gt; **Assign access**  &gt; **Assign access to resources**.
4. Select **IAM services**.
5. In the section *What type of access do you want to assign?*, select **{{site.data.keyword.la_full_notm}}**.
6. In the section *Which services do you want to assign access to?*, choose one of the following options:

    Select **All services** to define the scope of the policy to include all instances.

    Select **Services based on attributes** to refine the scope of the policy. Choose 1 of the following options:
    
    Option 1: The scope is set to a resource group. Select **Resource group** to choose 1 resource group and define the scope of the policy to include all instances that are associated with that resource group. 

    Option 2: The scope is set to 1 instance in a resource group. Select **Resource group** to choose the resource group. Then select **Service Instance** to choose the instance within the resource group.
    
    Option 3: The scope is set to 1 instance. Select **Service Instance** to choose the instance.

    Do not specify a value in the **logGroup** section.
    {: important}

7. Select the **viewer** platform role.

8. Click **Add**.

9. Click **Assign**.



## Step 3. Add permissions to work in an IAM access group
{: #iam_grant_group_step3}

Next, you must add a policy that grants the user permissions to work with data in the {{site.data.keyword.la_short}} service within the context of a group.

When you define the policy, you need to select a service role. Service access roles define a user's or service’s ability to perform actions on a service instance. The service access roles are manager, standard-member, and reader.


### Add permissions through the CLI
{: #iam_grant_group_step3_1}

To create an access group policy by using the CLI, you can use the [ibmcloud iam access-group-policy-create](/docs/cli?topic=cli-ibmcloud_commands_iam#ibmcloud_iam_access_group_policy_create) command.

```
ibmcloud iam access-group-policy-create GROUP_NAME {-f, --file @JSON_FILE | --roles ROLE_NAME1,ROLE_NAME2... [--service-name SERVICE_NAME] [--service-instance SERVICE_INSTANCE] [--region REGION] [--resource-type RESOURCE_TYPE] [--resource RESOURCE] [--resource-group-name RESOURCE_GROUP_NAME] [--resource-group-id RESOURCE_GROUP_ID]}
```
{: codeblock}

Where valid roles are `Reader`, `Standard-member`, and `Manager`.

You must use a JSON file to create the group policy.
{: important}

For example, you can run the following command:

```
ibmcloud iam access-group-policy-create accessGroupName accessGroupGUID --file policy.json
```
{: codeblock}

Where 

* `accessGroupName` is the access group name.
* `accessGroupGUID` is the GUID of the access group.

You can run the command `ibmcloud iam access-groups` to get the list of names and corresponding GUIDs in the account.
{: tip}

And use the following JSON file. 

```json
{
    "type": "access",
    "subjects": [
        {
            "attributes": [
                {
                    "name": "access_group_id",
                    "value": "AccessGroupGuid"
                }
            ]
        }
    ],
    "roles" : [
    {
            "role_id" : "crn:v1:bluemix:public:iam::::serviceRole:Reader"
    }
    ],
    "resources": [
        {
            "attributes": [
                {
                    "name": "accountId",
                    "value": "accountGuid"
                },
                {
                    "name": "serviceName",
                    "value": "logdnaat"
                },
                {
                    "name": "serviceInstance",
                    "value": "instanceGuid"
                },
                {
                    "name": "logGroup",
                    "value": "group1"
                }
            ]
        }
    ]
}
```
{: codeblock}


### Add permissions through the UI
{: #iam_grant_group_step3_2}

Complete the following steps to assign a policy to an access group through the UI:

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and select **Access Groups**.
2. Select the name of the group that you want to assign access to. 
3. Click **Access policies**  &gt; **Assign access**  &gt; **Assign access to resources**.
4. Select **IAM services**.
5. In the section *What type of access do you want to assign?*, select **{{site.data.keyword.la_full_notm}}**.
6. In the section *Which services do you want to assign access to?*, complete the following steps:

    1. Select **Services based on attributes** to refine the scope of the policy. Choose 1 of the following options:

        Option 1: Set the scope to 1 instance in a resource group. Select **Resource group** to choose the resource group. Then select **Service Instance** to choose the instance within the resource group.
    
        Option 2: Set the scope to 1 instance. Select **Service Instance** to choose the instance.

    2. Select a **logGroup**.

7. Select a service role. The service role defines the permissions a user has to view and manage resources in that group.

    * Select **manager** to grant admin permissions for the service.

    * Select **reader** to grant permissions to view data only.

    [Learn more about the roles that you need](/docs/log-analysis?topic=log-analysis-iam).

8. Click **Add**.

9. Click **Assign**.




## Step 4. Add a user or service ID to the access group
{: #iam_grant_group_step4}

You can add users or service IDs to an existing access group.

### Add a user to the access group
{: #iam_grant_group_step4_user}

Complete the following steps to add a user:

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and select **Access Groups**.
2. Select the name of the group that you want to assign access to. 
3. Click **Add users** on the **Users** tab.
4. Select the users that you want to add from the list, and click **Add to group**.


### Add a service ID to the access group
{: #iam_grant_group_step4_svcid}

Complete the following steps to add a service ID:

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and select **Access Groups**.
2. Select the name of the group that you want to assign access to. 
3. Click the **Service IDs** tab, and click **Add service ID**.
4. Select the IDs that you want to add from the list, and click **Add to group**.




