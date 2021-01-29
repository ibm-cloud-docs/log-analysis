---

copyright:
  years:  2021
lastupdated: "2021-01-28"

keywords: LogDNA, groups, access

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

# Using LogDNA groups to control LogDNA data access
{: #group_data_access}

You can configure, control, and manage the LogDNA data that is available to users in your {{site.data.keyword.cloud}} account by configuring **groups** in the LogDNA instance. 
{:shortdesc}

A **group** is comprised of **users** with authorization to specific data.

Configuration of groups is only available in the *Paris* data center.
{: important}

## Before you begin
{: #groups_data_access_before_beginning}

Before configuring and using groups you need to understand the following requirements and limitations.

Users require specific {{site.data.keyword.iamlong}} permissions to work with groups and group members.

Role                                                               | Permissions
-------------------------------------------------------------------|------------------------------------------------
Administrator platform role                                        | Required to define group members and their roles
Manager service role                                               | Required to manage LogDNA instance groups
Platform role viewer, service role reader, or standard member      | Required to launch the LogDNA instance
{: caption="Table 1. Roles required for groups" caption-side="top"} 

User roles defining permissions and access to manage LogDNA instance data are defined in {{site.data.keyword.iamlong}}.  However, there is no mapping of {{site.data.keyword.iamshort}} access groups to LogDNA groups. Each must be managed separately.  To ease management of the groups, consider defining similar access groups in LogDNA as you have defined in {{site.data.keyword.iamshort}}.

Users are assigned to a group by their email address.  If a user changes their email address, you must remove the old email address from the LogDNA group and add the new one.  

All users must have logged in to the LogDNA instance at least once before the user can be assigned to a LogDNA group.  If a user changes their email address, the new email must be logged in to the LogDNA instance before it can be added to the LogDNA group.

Users defined in the LogDNA group can see all resources defined in the LogDNA instance.  For example: views, boards, and screens.  Using the data access feature a user can open multiple LogDNA instances in different browser tabs.

## Configuring default LogDNA instance settings
{: #groups_data_access_settings}

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](../../icons/icon_hamburger.svg) &gt; **Observability**. 

4. Select **Logging**.

5. For your instance, click **View LogDNA**. The LogDNA web UI will be displayed.

6. Click ![**Settings**](/images/config.png "Settings icon") &gt; **Organization** &gt; **TEAM** &gt; **Settings**.

7. Set **Access Control** to your desired default setting:

   * **ON** allows all users to see the LogDNA instance data even if they are not part of a group.
   * **OFF** requires users to be a member of a LogDNA group associated with the LogDNA instance to see data.

   Setting **Access Control** to **OFF** prevents users who are not defined to a LogDNA group from seeing the LogDNA instance data.
   {: tip}

## Defining LogDNA groups
{: #groups_data_access_groups}

In LogDNA you can define 1 or more groups, also known as teams, limiting the set of data the users in that group can view and analyze.  You configure the scope of data visible to users in the LogDNA group using an access scope.  Remember, user permissions to access LogDNA and LogDNA features are defined in {{site.data.keyword.iamlong}}.

You can edit a group to add users or change the access scope as needed.

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](../../icons/icon_hamburger.svg) &gt; **Observability**. 

4. Select **Logging**.

5. For your instance, click **View LogDNA**. The LogDNA web UI will be displayed.

6. Click ![**Settings**](/images/config.png "Settings icon") &gt; **Organization** &gt; **TEAM** &gt; **Groups**.

7. Click **Add Group**.

8. Enter a **Group Name** for your group.

   ![Add Group](/images/addgroup.png)

   Consider a naming convention similar to your {{site.data.keyword.iamshort}} for ease of management.
   {: tip}

9. Select the **Members** to be included in the group.

9. Specify the **Access Scope**.

   The access scope is defined as a search query.  The query uses the following format.

   Example Query              | Behavior                          | Example Matches
---------------------------|-----------------------------------|-------------------------------------------------
   `level:error`              | Case-insensitive prefix match     | Error, error, errors
   `level:=error`             | Case-sensitive prefix match       | error, errors
   `level:==error`            | Case-insensitive exact term match | error, Error
   `level:===error`           | Case-sensitive exact term match   | error
   `level:[warning,error]`    | Case-insensitive list of prefixes | warning, Warning, Warnings, error, ERROR, errors
   `level:===[warning,error]` | Case-sensitive list of prefixes   | warning, error
   `level:*`                  | Matches if the field exists       | All lines containing the field `level`
   {: caption="Table 2. Example access scope search queries" caption-side="top"} 

   For example, if you have two apps (`myapp` and `myapp1`), then a LogDNA group with an access scope of  `app:myapp` will allow access to data from both apps. If the access scope is `app:===myapp`, then users in the group will only be able to access data from the `myapp` app. 

   If you want to create a group of administrators with access to all data, specify `host:*` for the 
   **Access Scope**.
   {: note}

## Editing or deleting LogDNA groups
{: #groups_data_access_editing}

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](../../icons/icon_hamburger.svg) &gt; **Observability**. 

4. Select **Logging**.

5. For your instance, click **View LogDNA**. The LogDNA web UI will be displayed.

6. Click ![**Settings**](/images/config.png "Settings icon") &gt; **Organization** &gt; **TEAM** &gt; **Groups**.

7. Click **Edit** or **Delete** to change or remove the group.