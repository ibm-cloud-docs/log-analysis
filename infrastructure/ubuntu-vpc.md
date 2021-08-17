---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, ubuntu, tutorial

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


# Logging with Linux VPC server instances
{: #ubuntu}

Use the {{site.data.keyword.la_full}} service to monitor and manage logs from a Linux VPC server instance in a centralized logging system on the {{site.data.keyword.cloud_notm}}. 
{: shortdesc}

You can collect and monitor system and application logs. 

By default, the logging agent for Ubuntu monitors log files in the `/var/log` directory. For example, the Ubuntu system log (`/var/log/syslog`) is monitored by default.

On the {{site.data.keyword.cloud_notm}}, configure an Ubuntu server to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision a VPC running Ubuntu Linux.
2. Provision an instance of the {{site.data.keyword.la_full_notm}} service. 
2. Configure the logging agent in the Ubuntu server.
3. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Component overview on the {{site.data.keyword.cloud_notm}}")

In this tutorial, you will learn how to configure an Ubuntu server to forward logs to an {{site.data.keyword.la_full_notm}} instance.

## Before you begin
{: #ubuntu_prereqs}

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About](/docs/log-analysis?topic=log-analysis-getting-started#getting-started_ov).

Work in a [supported region](/docs/log-analysis?topic=log-analysis-regions). 

You can send data from an Ubuntu instance that is located in the same region as your logging instance, in a different region, or not in the {{site.data.keyword.cloud_notm}}.
{: note}

Use a user ID that is a member, or an owner of, an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} {{site.data.keyword.IBM_notm}}ID, go to: [Create an account](https://cloud.ibm.com/login){: external}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources in the region that your {{site.data.keyword.la_full_notm}} instance is in:  

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **default**           |  Resource group            | Viewer  | `us-south`  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the default resource group.   |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

The {{site.data.keyword.cloud_notm}} CLI must be installed. For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

## Step 1. Provision an Ubuntu Linux VPC server instance
{: #ubuntu_step1}

If you have an existing Ubuntu Linux virtual server instance you want to monitor, you can skip this step.

1. If you don't have a virtual private cloud, [use the {{site.data.keyword.cloud_notm}} console to create VPC resources](/docs/vpc?topic=vpc-creating-a-vpc-using-the-ibm-cloud-console).

2. If you don't have an Ubuntu Linux virtual server instance, [create an Ubuntu Linux virtual server instance by using the UI and selecting **Ubuntu Linux** as the **Operating System**](https://cloud.ibm.com/docs/vpc?topic=vpc-creating-virtual-servers).

## Step 2. Provision an {{site.data.keyword.la_full_notm}} instance
{: #ubuntu_step2}

To provision an instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. Select the **Logging and Monitoring** category.

4. Click the **{{site.data.keyword.la_full_notm}}** tile.

5. Select a region for the service instance.

6. Select the **Lite** service plan. 

   By default, the **Lite** plan is set.

   For more information about other service plans, see [Pricing plans](/docs/log-analysis?topic=log-analysis-service_plans).

7. Specify a **Service name** for your {{site.data.keyword.la_full_notm}} service instance.

8. Select the **Default** resource group. 

   By default, the **Default** resource group is set.

8. To provision the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}} selected resource group, click **Create**.

After you provision an instance, the {{site.data.keyword.la_full_notm}} dashboard opens. 

To provision an instance of logging through the CLI, see [Provisioning logging through the {{site.data.keyword.cloud_notm}} CLI](/docs/log-analysis?topic=log-analysis-provision#provision_cli).
{: note}


## Step 3. Configure your Ubuntu server to send logs to your instance
{: #ubuntu_step3}

To configure your Ubuntu server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logging-agent`. The logging agent reads log files from `/var/log` or other directories you specify, and forwards the log data to your logging instance.

To configure your Ubuntu server to forward logs to your logging instance, complete the following steps from an Ubuntu terminal:

1. Install the logging agent. Run the following commands:

   ```
   echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
   ```
   {: pre}

   ```
   wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
   ```
   {: pre}

   ```
   sudo apt-get update
   ```
   {: pre}

   ```
   sudo apt-get install logging-agent < "/dev/null"
   ```
   {: pre}

2. Set the ingestion key that the logging agent will use to forward logs to the {{site.data.keyword.la_full_notm}} instance.  

   ```
   sudo logging-agent -k <INGESTION_KEY>
   ```
   {: pre}

   where <INGESTION_KEY> contains the ingestion key for the {{site.data.keyword.la_full_notm}} instance where the logs will be forwarded.

   You can retrieve the ingestion key using the [{{site.data.keyword.cloud_notm}} console](/docs/log-analysis?topic=log-analysis-ingestion_key#ibm_cloud_ui), or by the [{{site.data.keyword.cloud_notm}} CLI](/docs/log-analysis?topic=log-analysis-ingestion_key#ingestion_key_cli).

3. Set the authentication endpoint. The logging agent uses this host to authenticate and get the token to forward logs.

   ```
   sudo logging-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
   ```
   {: pre}

4. Set the ingestion endpoint.

   ```
   sudo logging-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
   ```
   {: pre}

5. (Optional) Define any additional log paths to be monitored. Run the following command: 

   ```
   sudo logging-agent -d <PATH_TO_LOG_FOLDERS>
   ```
   {: pre}

   Where <PATH_TO_LOG_FOLDERS> is the path where logs are saved on your system.  By default, `/var/log` is monitored.

6. (Optional) Configure the logging agent to tag your hosts. Run the following command:

   ```
   sudo logging-agent -t TAG1,TAG2 
   ```
   {: pre}

   Tags must be separated by commas and without any spaces between the comma and tag name.
   {: note}

7. Update the logging agent with your changes.  Run the following command:

   ```
   sudo update-rc.d logging-agent defaults
   ```
   {: pre}

8. Start the logging agent.  Run the following command:

   ``` 
   sudo /etc/init.d/logging-agent start
   ```
   {: pre}


## Step 4. Launch the logging Web UI
{: #ubuntu_step4}

To launch the {{site.data.keyword.la_full_notm}} dashboard from the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [{{site.data.keyword.cloud_notm}} dashboard](https://cloud.ibm.com/login){: external} to launch the {{site.data.keyword.cloud_notm}} dashboard.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Click **Logging**. 

   The list of {{site.data.keyword.la_full_notm}} instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select one instance. Then, click **Open dashboard**.

   The logging Web UI opens and displays your cluster logs.


## Step 5. View your logs
{: #ubuntu_step5}

From the logging Web UI, you can view your logs as they pass through the system. You view logs by using log tailing. 

With the **Free** service plan, you can only tail your latest logs.
{: note}

For more information, see [Viewing logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs).


## Next steps
{: #ubuntu_next_steps}

The following additional features are available:

* [Filtering logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step5)
* [Searching logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step6)
* [Defining views](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step7)
* [Configuring alerts](/docs/log-analysis?topic=log-analysis-alerts). 

To use any of these features, you must upgrade the {{site.data.keyword.la_full_notm}} plan to a paid plan.
{: note}

