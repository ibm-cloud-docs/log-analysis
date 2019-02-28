---

copyright:
  years:  2018, 2019
lastupdated: "2019-02-28"

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

 
# Archiving logs to IBM Cloud Object Storage
{: #archiving}

You can archive logs from an IBM Log Analysis with LogDNA instance into a bucket in an {{site.data.keyword.cos_full_notm}} (COS) instance. 
{:shortdesc}

To configure archiving, you must have an IAM policy with platform role **Viewer** and service role **Manager** for the IBM Log Analysis with LogDNA service.

You archive logs from an IBM Log Analysis with LogDNA instance into a bucket in an {{site.data.keyword.cos_full_notm}} (COS) instance. Each IBM Log Analysis with LogDNA instance has its own archiving configuration. 

Logs are automatically archived once a day in a compressed format **(.json.gz)**. Each line preserves its metadata.

Logs are archived within 24-48 hours after you save the configuration. 

The {{site.data.keyword.cos_full_notm}} instance is provisioned within the context of a resource group. The IBM Log Analysis with LogDNA instance is also provisioned within the context of a resource group. Both instances can be grouped under the same resource group or in different ones. 

IBM Log Analysis with LogDNA uses a service ID to communicate with the {{site.data.keyword.cos_full_notm}} service.

* The service ID that you create for an {{site.data.keyword.cos_full_notm}} instance is used by the IBM Log Analysis with LogDNA to authenticate and access the {{site.data.keyword.cos_full_notm}} instance. 
* You can assign specific access policies to the service ID that restrict permissions on the {{site.data.keyword.cos_full_notm}} instance. Restrict the service ID to only have writing permissions on the bucket where you plan to archive the logs.

The following figure shows a high level view of the different components that are integrated when archiving logs:

![High level view archiving logs](images/archive.png "High level view archiving logs")


Complete the following steps to archive an IBM Log Analysis with LogDNA instance into a bucket in an {{site.data.keyword.cos_full_notm}} instance:


## Step 1: Grant IAM policies to a user to work with IBM Cloud Object Storage
{: #archiving_step1}

**Note:** This step must be completed by the account owner or an administrator of the {{site.data.keyword.cos_full_notm}} service on the {{site.data.keyword.cloud_notm}}.

As an administrator of the {{site.data.keyword.cos_full_notm}} service, you must be able to provision instances of the service, grant other users permissions to work with these instances, and create service IDs. 

There are different ways in which you can grant a user permissions to become an editor of the {{site.data.keyword.cos_full_notm}} service:

* As administrator of the service in the account, the user must have an IAM policy for the {{site.data.keyword.cos_full_notm}} service with the platform role *Administrator*. You must assign this user access to an individual resource in the account. 

* As administrator of the service within the context of a resource group, the user must have an IAM policy for the {{site.data.keyword.cos_full_notm}} service with the platform role *Administrator* within the context of the resource group. 


The following table lists the roles that a user can have to complete the actions listed for the {{site.data.keyword.cos_full_notm}} service:

| Service                    | Platform roles    | Action                                                                                        | 
|----------------------------|-------------------|-----------------------------------------------------------------------------------------------|       
| `Cloud Object Storage`     | Administrator     | Allows the user to assign policies to users in the account to work with the {{site.data.keyword.cos_full_notm}} service. |
| `Cloud Object Storage`     | Administrator </br>Editor | Allows the user to provision an instance of the {{site.data.keyword.cos_full_notm}} service.    |
| `Cloud Object Storage`     | Administrator </br>Editor </br>Operator | Allows the user to create a service ID.    | 
{: caption="Table 1. Roles and actions" caption-side="top"} 


Complete the following steps to assign a user administrator role to the {{site.data.keyword.cos_full_notm}} service within the context of a resource group: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the IBM Log Analysis with LogDNA service in the resource group.

6. Select **Cloud Object Storage**.
7. Select the platform role **Administrator**.
8. Click **Assign**.



## Step 2: Provision an instance of IBM Cloud Object Storage
{: #archiving_step2}

**Note:** This step must be completed by an editor, or administrator of the {{site.data.keyword.cos_full_notm}} service on the {{site.data.keyword.cloud_notm}}. 

Complete the following steps to provision an {{site.data.keyword.cos_full_notm}} instance:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    The {{site.data.keyword.cloud_notm}} dashboard can be found at: [https://cloud.ibm.com ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. To filter the list of services that is displayed, select the **Storage** category.

4. Click the **Object Storage** tile.

5. Enter a name for the service instance.

6. Select a resource group. 

    By default, the **Default** resource group is set.

7. Select a service plan. 

    By default, the **Lite** plan is set.

9. Click **Create**.



## Step 3: Create a bucket
{: #archiving_step3}

Buckets are a way to organize your data in an {{site.data.keyword.cos_full_notm}} instance. 

To manage buckets, your user must be granted permissions to work with buckets on the {{site.data.keyword.cos_full_notm}} instance. The following table outlines the different actions and roles that a user can have to work with buckets:

| Service                    | Roles                   | Action                             | 
|----------------------------|-------------------------|------------------------------------|       
| `Cloud Object Storage`     | Platform role: Viewer   | Allows the user to view all buckets and list the objects within them through the {site.data.keyword.Bluemix_notm}} UI. |
| `Cloud Object Storage`     | Service role: Manager   | Allows the user to make objects public.                                                       |
| `Cloud Object Storage`     | Service roles: Manager </br>Writer | Allows the user to create and destroy buckets and objects.                         | 
| `Cloud Object Storage`     | Service role: reader    | Allows the user to list and download objects.                                                 |
{: caption="Table 1. Roles and actions to work with buckets" caption-side="top"} 

**Note:** To create a bucket, your user must have manager or writer permissions for the {{site.data.keyword.cos_full_notm}} instance.

Complete the following steps to create a bucket:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    The {{site.data.keyword.cloud_notm}} dashboard can be found at: [https://cloud.ibm.com ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. From the Dashboard, select the {{site.data.keyword.cos_full_notm}} instance where you plan to create the bucket.

3. Select **Buckets**. Then, click **Create Bucket**.

4. Enter a bucket name for the *Unique bucket name* field.

    **Note:** All buckets in all regions across the globe share a single namespace. 

    You can use as part of the bucket name your IBM Log Analysis with LogDNA instance name. For example, for an instance with name *logdna-1*, you can use *accountN-logdna-1* as your bucket name.

    You will need this name to configure archiving through the IBM Log Analysis with LogDNA Web UI.

5. Choose the type of resiliency and a location where you would like your data to be physically stored.

    Resiliency refers to the scope and scale of the geographic area across which your data is distributed. 
    
    Cross Region resiliency will spread your data across several metropolitan areas.
    
    Regional resiliency will spread data across a single metropolitan area. 
    
    A Single Data Center will only distribute data across devices within a single site.

    For more information, see [Select regions and endpoints](/docs/services/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints).

6. Choose the type of *Storage class*.

    You can create buckets with different storage classes. Choose the storage class for your bucket based on your requirements to retrieve data. For more information, see [Use storage classes](/docs/services/cloud-object-storage?topic=cloud-object-storage-use-storage-classes#use-storage-classes).

    **Note:** It is not possible to change the storage class of a bucket once the bucket is created. If objects need to be reclassified, it is necessary to move the data to another bucket with the wanted storage class.

7. Optionally, add a Key Protect Key to encrypt data at rest.

    All objects are encrypted by default using randomly generated keys and an all-or-nothing-transform. While this default encryption model provides at-rest security, some workloads need to be in possession of the encryption keys used. For more information, see [Manage encryption](/docs/services/cloud-object-storage?topic=cloud-object-storage-manage-encryption#manage-encryption).



## Step 4: Create a service ID for the IBM Cloud Object Storage instance
{: #archiving_step4}

A service ID identifies a service similar to how a user ID identifies a user. Service IDs are not tied to a specific user. If the user that creates the service ID leaves your organization and is deleted from the account, the service ID remains.

You must create a service ID for your {{site.data.keyword.cos_full_notm}} instance. This service ID is used by the IBM Log Analysis with LogDNA instance to authenticate with your {{site.data.keyword.cos_full_notm}} instance. 

You must assign specific access policies to the service ID that restrict permissions for using specific services, or even combine permissions for accessing different services. For example, to restrict access to a single bucket, ensure that the service ID doesn't have any instance level policies using either the console or CLI.


Complete the following steps to create a service ID with writing permissions for the {{site.data.keyword.cos_full_notm}} instance:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    The {{site.data.keyword.cloud_notm}} dashboard can be found at: [https://cloud.ibm.com ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. From the Dashboard, select the {{site.data.keyword.cos_full_notm}} instance where you plan to create the bucket.

3. Select **Service credentials**. Then, select **New credential**.

4. Enter a name. 

5. Select the **Writer** role.

6. Click **Add**.

    A new service ID is added to the list. 


For the service ID that you just created, click **View credentials**. You can see information that is related to the service ID. 

* Copy the API key. This is the value set for the field **apikey**.
* Copy the resource instance ID. This is the value set for the field **resource_instance_id**.


## Step 5: Restrict the service ID to only have writing permissions for the bucket
{: #archiving_step5}

If you want to restrict the service ID to only have writing permissions for a bucket, complete the following steps:

1. Read the information for the service ID and write down the value of the **iam_apikey_name** field and the **iam_apikey_name** field. 

2. From the Dashboard, select **Manage** &gt; **Access (IAM)**, and then select **Users**.

3. Select **Service IDs**.

4. Look for a service ID that has the following name: **auto-generated-serviceId-<ID that is part of the iam_apikey_name value>.

5. Select the service ID. Then, in **Access policies**, click **Writer**.

6. In the *Resource type* field enter **bucket**.

7. In the *Resource ID* field enter the name of your bucket.

8. Click **Save**.

**Note:** If you leave the Resource Type or Resource fields blank, the policy that is created is an instance-level policy.


## Step 6: Select the endpoint
{: #archiving_step6}

An endpoint defines where to look for a bucket. There are different endpoints depending on the region and type of resiliency. For more information, see [Select regions and endpoints](/docs/services/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints).

Complete the following steps to obtain the endpoint for your bucket:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    The {{site.data.keyword.cloud_notm}} dashboard can be found at: [https://cloud.ibm.com ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. From the Dashboard, select the {{site.data.keyword.cos_full_notm}} instance where you plan to create the bucket.

3. Select **Buckets**. Then, select the bucket that you created where you want to archive logs.

4. Select **Configuration**.

5. Copy one of the private endpoints. 



## Step 7: Grant IAM policies to a user to archive logs
{: #archiving_step7}

The following table lists the policies that a user must have to be able to configure archiving of logs from IBM Log Analysis with LogDNA Web UI into a bucket in a {{site.data.keyword.cos_full_notm}} instance:

| Service                        | Role                      | Permission granted                  | 
|--------------------------------|---------------------------|-------------------------------------|  
| `IBM Log Analysis with LogDNA` | Platform role: Viewer     | Allows the user to view the list of service instances in the Observability Logging dashboard. |
| `IBM Log Analysis with LogDNA` | Service role: Manager      | Allows the user to launch the Web UI and view logs in the Web UI.                             |
{: caption="Table 2. IAM policies" caption-side="top"} 

For more information on how to configure these policies for a user, see [Granting permissions to a user to view logs in LogDNA](/docs/services/Log-Analysis-with-LogDNA/work_iam.html#user_logdna).

Complete the following steps to assign a user permissions to archive logs: 

1. From the menu bar, click **Manage** &gt; **Access (IAM)**, and then select **Users**.
2. From the row for the user that you want to assign access, select the **Actions** menu, and then click **Assign access**.
3. Select **Assign access within a resource group**.
4. Select a resource group.
5. If the user does not have a role already granted for the selected resource group, choose a role for the **Assign access to a resource group** field. 

    Depending on the role that you select, the user can view the resource group on their dashboard, edit the resource group name, or manage user access to the group. 
    
    You can select **No access**, if you want the user to only have access to the IBM Log Analysis with LogDNA service in the resource group.

6. Select **IBM Log Analysis with LogDNA**.
7. Select the platform role **Viewer**.
8. Select the service role **Manager**.
9. Click **Assign**.



## Step 8: Configure archiving for your IBM Log Analysis with LogDNA instance
{: #archiving_step8}


Complete the following steps to configure archiving of your IBM Log Analysis with LogDNA instance into a COS bucket:

1. Launch the IBM Log Analysis with LogDNA web UI. For more information, see [Launching the IBM Log Analysis with LogDNA Web UI](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#view_logs_step2).

2. Select the **Configuration** icon. Then select **Archiving**. 

3. Select **IBM Cloud Object Storage**.

4. Set the bucket, endpoint, API key, and instance ID where you want logs to be archived.

    <table>
      <caption>Table 3. COS fields</caption>
      <tr>
         <th>Field</th>
         <th>Value</th>
      </tr>
      <tr>
         <td>Bucket</td>
         <td>Set to the COS bucket name. </td>
      </tr>
      <tr>
         <td>Endpoint</td>
         <td>Set to the COS bucket private endpoint.</td>
      </tr>
      <tr>
         <td>API Key</td>
         <td>Set to the API key associated to the COS service ID.</td>
      </tr>
      <tr>
         <td>Instance ID</td>
         <td>Set to the COS instance ID. </td>
      </tr>
    </table>

5. Click **Save**.


After you save the configuration, logs are archived once a day.



