---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, archive logs, COS, cloud object storage

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

 
# Archiving logs to IBM Cloud Object Storage
{: #archiving}

You can archive logs from an {{site.data.keyword.la_full_notm}} instance into a bucket in an {{site.data.keyword.cos_full_notm}} (COS) instance. 
{: shortdesc}

To configure archiving, you must have an IAM policy with platform role **Viewer** and service role **Manager** for the {{site.data.keyword.la_full_notm}} service.

You archive logs from an {{site.data.keyword.la_full_notm}} instance into a bucket in an {{site.data.keyword.cos_full_notm}} (COS) instance. Each {{site.data.keyword.la_full_notm}} instance has its own archiving configuration. 

* Logs are automatically archived in a compressed format **(.json.gz)**. Each line preserves its metadata.

* Logs are archived 24 - 48 hours after you save the configuration. 

* Logs are archived hourly. 

    Previously, logs have been archived daily. Through this transition, you might observe a small overlap between the older daily format archives and the new archives.
    {: note}

* The hourly archive directory format looks like this:

    ```
    YYYY/MM/DD/<accountID>.<YYYY>-<MM>-<DD>.<HH>00.json.gz
    ```
    {: codeblock}
    
    Where 

    `YYYY` represents the year; `MM` represents the month; and `DD` represents the day.

    `<accountID>` represents the logging account ID, that is, the ID that showd in the [logging web UI URL](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-get_logdna_web_url).
    
    `HH` represents hours in 24 format. 

    The daily archive directory format looks like this:
    
    ```
    <accountID>.<YYYY>-<MM>-<DD>.<clusterId>.json.gz
    ```
    {: codeblock}

* Logs that are included in a file correspond to the period of time that is indicated as part of the name of the file. 

* The timestamp that is used to determine whether the log record is included in an archive is the UTC timestamp.

    Notice that depending on your location, there might be logs that you see in local time in your views on a specific day. However, you cannot find them on the archive file. You are most likely viewing logs in local time and the archive process uses the UTC timestamp.

* After you configure archiving, the first archive file is created when the archiving process runs and there is data.
* The first time the archive process runs, consider the following information:

    * The maximum number of days that data is archived includes logs for the past 30 days when the instance has a `30 day Log search` plan.

    * The maximum number of days that data is archived includes logs for the past 14 days when the instance has a `14 day Log search` plan.

    * The maximum number of days that data is archived includes logs for the past 7 days when the instance has a `7 day Log search` plan.

For example, you have a service plan of 30 days. You configured the instance 10 days ago. You enable archiving on the 10th day. The archiving process generates multiple files. Each file includes logs for the period of time indicated as part of its name. If there is no data, the archive file for that period is empty.

Each {{site.data.keyword.at_full_notm}} instance has its own archiving configuration.
{: important}

The {{site.data.keyword.cos_full_notm}} instance is provisioned in the context of a resource group. The {{site.data.keyword.la_full_notm}} instance is also provisioned in the context of a resource group. Both instances can be grouped under the same resource group or in different ones. 

{{site.data.keyword.la_full_notm}} uses a service ID to communicate with the {{site.data.keyword.cos_full_notm}} service.

* The service ID that you create for an {{site.data.keyword.cos_full_notm}} instance is used by the {{site.data.keyword.la_full_notm}} to authenticate and access the {{site.data.keyword.cos_full_notm}} instance. 
* You can assign specific access policies to the service ID that restrict permissions on the {{site.data.keyword.cos_full_notm}} instance. Restrict the service ID to have only writing permissions on the bucket where you plan to archive the logs.

The following figure shows a high-level view of the different components that are integrated when you archive logs:

![High-level view archiving logs](../images/archive.png "High-level view archiving logs")


Complete the following steps to archive an {{site.data.keyword.la_full_notm}} instance into a bucket in an {{site.data.keyword.cos_full_notm}} instance:


## Step 1. Grant IAM policies to a user to work with {{site.data.keyword.cos_full_notm}}
{: #archiving_step1}

This step must be completed by the account owner or an administrator of the {{site.data.keyword.cos_full_notm}} service on the {{site.data.keyword.cloud_notm}}.
{: note}

As an administrator of the {{site.data.keyword.cos_full_notm}} service, you must be able to provision instances of the service, grant other users permissions to work with these instances, and create service IDs. 

You can grant a user permissions to become an editor of the {{site.data.keyword.cos_full_notm}} service:

* As administrator of the service in the account, the user must have an IAM policy for the {{site.data.keyword.cos_full_notm}} service with the platform role *Administrator*. You must assign this user access to an individual resource in the account. 

* As administrator of the service within the context of a resource group, the user must have an IAM policy for the {{site.data.keyword.cos_full_notm}} service with the platform role *Administrator* within the context of the resource group. 


The following table lists the roles that a user can have to complete the actions listed for the {{site.data.keyword.cos_full_notm}} service:

| Service                    | Platform roles    | Action                                                                                        | 
|----------------------------|-------------------|-----------------------------------------------------------------------------------------------|       
| `Cloud Object Storage`     | Administrator     | Allows the user to assign policies to users in the account to work with the {{site.data.keyword.cos_full_notm}} service. |
| `Cloud Object Storage`     | Administrator  \n Editor | Allows the user to provision an instance of the {{site.data.keyword.cos_full_notm}} service.    |
| `Cloud Object Storage`     | Administrator  \n Editor  \n Operator | Allows the user to create a service ID.    | 
{: caption="Table 1. Roles and actions" caption-side="top"} 


Complete the following steps to assign a user administrator role to the {{site.data.keyword.cos_full_notm}} service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role that is already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to have only access to the {{site.data.keyword.la_full_notm}} service in the resource group.

6. Select **Cloud Object Storage**.
7. Select the platform role **Administrator**.
8. Click **Assign**.



## Step 2. Provision an instance of {{site.data.keyword.cos_full_notm}}
{: #archiving_step2}

This step must be completed by an editor, or administrator of the {{site.data.keyword.cos_full_notm}} service on the {{site.data.keyword.cloud_notm}}. 
{: note}

Complete the following steps to provision an {{site.data.keyword.cos_full_notm}} instance:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log in, the {{site.data.keyword.cloud_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. To filter the list of services that is displayed, select the **Storage** category.

4. Click the **Object Storage** tile.

5. Enter a name for the service instance.

6. Select a resource group. 

    By default, the **Default** resource group is set.

7. Select a service plan. 

    By default, the **Lite** plan is set.

8. Click **Create**.



## Step 3. Create a bucket
{: #archiving_step3}

Buckets are a way to organize your data in an {{site.data.keyword.cos_full_notm}} instance. 

To manage buckets, your user must be granted permissions to work with buckets on the {{site.data.keyword.cos_full_notm}} instance. The following table outlines the different actions and roles that a user can have to work with buckets:

| Service                    | Roles                   | Action                             | 
|----------------------------|-------------------------|------------------------------------|       
| `Cloud Object Storage`     | Platform role: Viewer   | Allows the user to view all buckets and list the objects within them through the {{site.data.keyword.cloud_notm}} UI. |
| `Cloud Object Storage`     | Service role: Manager   | Allows the user to make objects public.                                                       |
| `Cloud Object Storage`     | Service roles: Manager  \n Writer | Allows the user to create and destroy buckets and objects.                         | 
| `Cloud Object Storage`     | Service role: reader    | Allows the user to list and download objects.                                                 |
{: caption="Table 1. Roles and actions to work with buckets" caption-side="top"} 

**Note:** To create a bucket, your user must have manager or writer permissions for the {{site.data.keyword.cos_full_notm}} instance.

Complete the following steps to create a bucket:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    Click [{{site.data.keyword.cloud_notm}} dashboard ](https://cloud.ibm.com/login){: external} to launch the {{site.data.keyword.cloud_notm}} dashboard.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. From the Dashboard, select the {{site.data.keyword.cos_full_notm}} instance where you plan to create the bucket.

3. Select **Buckets**. Then, click **Create Bucket**.

4. Enter a bucket name for the *Unique bucket name* field.

    **Note:** All buckets in all regions across the globe share a single namespace. 

    You can use as part of the bucket name your {{site.data.keyword.la_full_notm}} instance name. For example, for an instance with name *logging-1*, you can use *accountN-logging-1* as your bucket name.

    You need this name to configure archiving through the {{site.data.keyword.la_full_notm}} web UI.

5. Choose the type of resiliency and a location where you would like your data to be physically stored.

    Resiliency refers to the scope and scale of the geographic area across which your data is distributed. 
    
    Cross Region resiliency spreads your data across several metropolitan areas.
    
    Regional resiliency spreads data across a single metropolitan area. 
    
    A Single Data Center will only distribute data across devices within a single site.

    For more information, see [Select regions and endpoints](/docs/cloud-object-storage?topic=cloud-object-storage-endpoints).

6. Choose the type of *Storage class*.

    You can create buckets with different storage classes. Choose the storage class for your bucket based on your requirements to retrieve data. For more information, see [Use storage classes](/docs/cloud-object-storage?topic=cloud-object-storage-classes).

    **Note:** It is not possible to change the storage class of a bucket once the bucket is created. If objects need to be reclassified, it is necessary to move the data to another bucket with the wanted storage class.

7. Optionally, add a Key Protect Key to encrypt data at rest.

    All objects are encrypted by default by using randomly generated keys and an all-or-nothing-transform. While this default encryption model provides at-rest security, some workloads need to be in possession of the encryption keys used. For more information, see [Manage encryption](/docs/cloud-object-storage?topic=cloud-object-storage-encryption).



## Step 4. Create a service ID for the {{site.data.keyword.cos_full_notm}} instance
{: #archiving_step4}

A service ID identifies a service similar to how a user ID identifies a user. Service IDs are not tied to a specific user. If the user that creates the service ID leaves your organization and is deleted from the account, the service ID remains.

You must create a service ID for your {{site.data.keyword.cos_full_notm}} instance. This service ID is used by the {{site.data.keyword.la_full_notm}} instance to authenticate with your {{site.data.keyword.cos_full_notm}} instance. 

You must assign specific access policies to the service ID that restrict permissions for using specific services, or even combine permissions for accessing different services. For example, to restrict access to a single bucket, ensure that the service ID doesn't have any instance level policies by using either the console or CLI.


Complete the following steps to create a service ID with writing permissions for the {{site.data.keyword.cos_full_notm}} instance:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    Click [{{site.data.keyword.cloud_notm}} dashboard](https://cloud.ibm.com/login){: external} to launch the {{site.data.keyword.cloud_notm}} dashboard.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. From the Dashboard, select the {{site.data.keyword.cos_full_notm}} instance where you plan to create the bucket.

3. Select **Service credentials**. Then, select **New credential**.

4. Enter a name. 

5. Select the **Reader** role.

6. Click **Add**.

    A new service ID is added to the list. 


For the service ID that you just created, click **View credentials**. You can see information that is related to the service ID. 

* Copy the API key. This is the value set for the field **apikey**.
* Copy the resource instance ID. This is the value set for the field **resource_instance_id**.


## Step 5. Restrict the service ID to have only writing permissions for the bucket
{: #archiving_step5}

If you want to restrict the service ID to have only writing permissions for a bucket, complete the following steps:

1. Read the information for the service ID and write down the value of the **iam_apikey_name** field and the **iam_apikey_name** field. 

2. From the Dashboard, select **Manage** &gt; **Access (IAM)**, and then select **Users**.

3. Select **Service IDs**.

4. Look for a service ID that has the following name: `auto-generated-serviceId-<ID that is part of the iam_apikey_name value>`.

5. Select the service ID. Then, in **Access policies**, click **Writer**.

6. In the *Resource type* field enter **bucket**.

7. In the *Resource ID* field enter the name of your bucket.

8. Click **Save**.

If you leave the Resource Type or Resource fields blank, the policy that is created is an instance-level policy.
{: note}


## Step 6. Select the endpoint
{: #archiving_step6}

An endpoint defines where to look for a bucket. There are different endpoints depending on the region and type of resiliency. For more information, see [Select regions and endpoints](/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints).

Complete the following steps to obtain the endpoint for your bucket:

1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

	After you log, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. From the Dashboard, select the {{site.data.keyword.cos_full_notm}} instance where you plan to create the bucket.

3. Select **Buckets**. Then, select the bucket that you created where you want to archive logs.

4. Select **Configuration**.

5. Copy one of the private endpoints. 



## Step 7. Grant IAM policies to a user to archive logs
{: #archiving_step7}

The following table lists the policies that a user must have to configure archiving of logs from the {{site.data.keyword.la_full_notm}} web UI into a bucket in an {{site.data.keyword.cos_full_notm}} instance:

| Service                        | Role                      | Permission granted                  | 
|--------------------------------|---------------------------|-------------------------------------|  
| `{{site.data.keyword.la_full_notm}}` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `{{site.data.keyword.la_full_notm}}` | Service role: Manager      | Allows the user to launch the web UI and view logs in the web UI.                             |
{: caption="Table 2. IAM policies" caption-side="top"} 

For more information on how to configure these policies for a user, see [Granting permissions to a user to view logs](/docs/log-analysis?topic=log-analysis-work_iam#user_logdna).

Complete the following steps to assign a user permission to archive logs: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to have only access to the {{site.data.keyword.la_full_notm}} service in the resource group.

6. Select **{{site.data.keyword.la_full_notm}}**.
7. Select the platform role **Viewer**.
8. Select the service role **Manager**.
9. Click **Assign**.



## Step 8. Configure archiving for your {{site.data.keyword.la_full_notm}} instance
{: #archiving_step8}


Complete the following steps to configure archiving of your {{site.data.keyword.la_full_notm}} instance into a COS bucket:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step2).

2. Click the **Settings** icon ![Configuration icon](../images/admin.png "Admin icon"). Then select **Archiving**. 

3. Make sure **Enable Archiving** is on.

4. Select **IBM Cloud Object Storage** as the **Provider**.

5. Set the bucket, endpoint, API key, and instance ID where you want logs to be archived.

    | Field       | Value                                                |
    |-------------|------------------------------------------------------|
    | Bucket      | Set to the COS bucket name.                          |
    | Endpoint    | Set to the COS bucket private endpoint.              |
    | API Key     | Set to the API key associated to the COS service ID. |
    | Instance ID | Set to the COS instance ID.                          |
    {: caption="Table 3. COS fields" caption-side="top"}

6. Click **Save**.


After you save the configuration, logs are archived once a day.


