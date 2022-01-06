---

copyright:
  years:  2018, 2022
lastupdated: "2021-03-28"

keywords: groups, access

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Using groups to control data access
{: #group_data_access}

You can configure, control, and manage data that is available to users in your {{site.data.keyword.cloud}} account by configuring **groups** in the logging instance. 
{: shortdesc}

A **group** is comprised of **users** with authorization to specific data.


## Before you begin
{: #groups_data_access_before_beginning}

Before configuring and using groups, you need to understand the following requirements and limitations.

Users require specific {{site.data.keyword.iamlong}} permissions to work with groups and group members.

Role                                                               | Permissions
-------------------------------------------------------------------|------------------------------------------------
Account management role                                            | Required to invite users, access groups, and define policies
Administrator platform role                                        | Required to manage the service
Manager service role                                               | Required to manage groups
Platform role viewer, service role reader, or standard member      | Required to launch the logging instance
{: caption="Table 1. Roles required for groups" caption-side="top"} 

User roles defining permissions and access to manage auditing events are defined in {{site.data.keyword.iamlong}}.  

You can map {{site.data.keyword.iamshort}} access groups to service groups. Consider the following information:
- You must name your service groups with the same name as your access groups. Users that belong to an access group are granted access to manage data in the service group.
- You must define a policy per service group, where the group that you specify matches the access group name. 
- You must define the scope of the data that each service group can manage when you define the service group through the web UI.



## Configuring default access settings
{: #groups_data_access_settings}

Complete the following steps to define the default settings for viewing data:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](/images/icon_hamburger.svg) &gt; **Observability**. 

4. Click **Logging**.

5. For your instance, click **Open dashboard**. The UI will be displayed.

6. Click the Settings icon ![**Settings icon**](/images/config.png "Settings icon") &gt;  **TEAM** &gt; **Settings**.

7. Set **Access Control** to your desired default setting:

   * **ON** allows all users to see the auditing data even if they are not part of a group.
   * **OFF** requires users to be a member of a service group that is associated with the logging instance to see events.

   Setting **Access Control** to **OFF** prevents users who are not defined to a service group from seeing auditing events.
   {: tip}

## Defining service groups
{: #groups_data_access_groups}

You can define 1 or more groups, also known as teams, limiting the set of data the users in that group can view and analyze. You configure the scope of data visible to users in a service group by using an access scope.  Remember, user permissions to manage data are defined in {{site.data.keyword.iamlong}}.

You can edit a group to change the access scope as needed.

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](/images/icon_hamburger.svg) &gt; **Observability**. 

4. Select **Logging**.

5. For your instance, click **Open dashboard**. The UI will be displayed.

6. Click ![**Settings**](/images/config.png "Settings icon") &gt; **TEAM** &gt; **Groups**.

7. Click **Add Group**.

8. Enter a **Group Name** for your group.

   ![Add Group](/images/addgroup.png)

   Consider a naming convention similar to your {{site.data.keyword.iamshort}} access groups for ease of management.
   {: tip}

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

For example, if you have two apps (`myapp` and `myapp1`), then a service group with an access scope of  `app:myapp` will allow access to data from both apps. If the access scope is `app:===myapp`, then users in the group will only be able to access data from the `myapp` app. 

If you want to create a group of administrators with access to all data, specify `host:*` for the  **Access Scope**.
{: note}

## Editing or deleting service groups
{: #groups_data_access_editing}

Complete the following steps to edit or delete a service group:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Select your account.

3. Click the **Menu** icon ![Menu icon](/images/icon_hamburger.svg) &gt; **Observability**. 

4. Click **Logging**.

5. For your instance, click **Open dashboard**. The UI will be displayed.

6. Click ![**Settings**](/images/config.png "Settings icon") &gt; **TEAM** &gt; **Groups**.

7. Click **Edit** or **Delete** to change or remove the group.


