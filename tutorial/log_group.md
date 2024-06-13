---

copyright:
  years:  2022, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

content-type: tutorial
services: log-analysis
account-plan: lite
completion-time: 1h

---

{{site.data.keyword.attribute-definition-list}}


# Creating a group (WIP)
{: #log_group_tutorial}
{: toc-content-type="tutorial"}
{: toc-services="log-analysis"}
{: toc-completion-time="1h"}

You can use a search query to limit the access to specific logs to specific users. For example, you can create a log group showing only logs from specific applications and assign that group to the developers supporting those applications. When those users access the {{site.data.keyword.la_full_notm}} dashboard, they see the logs matching the group definition. Alerts, events, and graphics are also limited by the group definition.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

## Before you begin
{: #kube_reset_prereqs}

Work in a [supported region](/docs/log-analysis?topic=log-analysis-regions). This tutorial assumes you are working in `us-south`.

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About](/docs/log-analysis?topic=log-analysis-getting-started#getting-started-ov).

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration](https://cloud.ibm.com/login){: external}.

[Provision an {{site.data.keyword.la_full_notm}} instance](/docs/log-analysis?topic=log-analysis-provision) in the **default** resource group.

To complete the steps in this tutorial, your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources:

| Resource                             | Scope of the access policy | Roles    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Administrator  | us-south  | This policy is required to grant permissions to log groups.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Viewer  \n Standard-Member  | us-south  | This policy is required to allow the user define a log group.   |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"}

## Create an IAM access group
{: #log_group_step0}

Create an [IAM access group](/docs/log-analysis?topic=log-analysis-iam_grant_group) that will have limited access to log entries in {{site.data.keyword.la_full_notm}}.

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and select **Access Groups**.
2. Click **Create**.
3. Enter a name (for example, `GroupA`) and optional description for your group, and click **Create**.
4. From the menu bar, click **Manage** &gt; **Access (IAM)**, and select **Access Groups**.
5. Select the name of the group that you want to assign access to.
6. Click **Add users** on the **Users** tab.
7. Select the users that you want to add from the list, and click **Add to group**.

## Access the Manage Team settings
{: #log_group_step1}
{: step}

1. Launch the [{{site.data.keyword.la_short}} dashboard.](/docs/log-analysis?topic=log-analysis-launch#launch_cloud_ui)

2. Click the **Settings** icon ![Settingsicon](../images/config.png "Settings") &gt; **Organization** &gt; **Groups**.

**Manage Teams** displays.

## Create a group
{: #log_group_step2}
{: step}

1. Click **Add Group**.

2. for **Group Name** specify the name for your group. For example, `MyLogGroup`.

3. Click **Add query** and specify a [query](/docs/log-analysis?topic=log-analysis-views) that restricts the log lines returned.

4. Click **Preview** to see the results of your query.

5. If the query returns the log lines that you want, click **Add Group** to save your group.

## Define IAM permissions for your instance and group
{: #log_group_step3}
{: step}

These steps associate your IAM access group with the defined {{site.data.keyword.la_short}} group.

1. Click **Manage** &gt; **Access(IAM)**.

2. Click **Access groups**.

3. Click an access group associated with your {{site.data.keyword.la_short}} instance. For example, the access group you created in the [first step.](#log_group_step0)
{: #access_group}

4. Click **Access**.

5. Click **Assign access**.

6. For **Service** select "IBM Log Analysis". Click **Next**.

7. For **Resources** select "Specific resource". For **Attribute type** select "Service instance". For **Value** select your {{site.data.keyword.la_short}} instance. Click **Next**.

8. For **Roles and action** select "Viewer"

9. Click **Manage** &gt; **Access(IAM)**.

10. Click **Access groups**.

11. Click the access group associated with your {{site.data.keyword.la_short}} instance configured in the [previous step.](#access_group)

12. Click **Access**.

13. Click **Assign access**.

14. For **Service** select "IBM Log Analysis". Click **Next**.

15. For **Resources** select "Specific resource". For **Attribute type** select "Service instance". For **Value** select your {{site.data.keyword.la_short}} instance. Click **Add condition**.

16. For **Attribute type** select "logGroup". For **Value** select the [group name you defined in {{site.data.keyword.la_short}}](#log_group_step2). Click **Next**.

17. For **Roles and action** select "Standard Member" and "Viewer".

The members of the IAM access group will now only be able to work with log entries configured in the {{site.data.keyword.la_short}} group definition.
