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


# Managing Ubuntu logs with {{site.data.keyword.la_full_notm}}
{: #ubuntu}

Use the {{site.data.keyword.la_full}} service to monitor and manage Ubuntu logs in a centralized logging system on the {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

You can collect and monitor system and application logs. 

By default, the LogDNA agent for Ubuntu monitors log files in the **/var/log** directory. For example, the Ubuntu system log (*/var/log/syslog*) is monitored by default.

On the {{site.data.keyword.cloud_notm}}, to configure an Ubuntu server to forward logs to an {{site.data.keyword.la_full_notm}} instance, you must complete the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service. 
2. Configure the LogDNA agent in the Ubuntu server.
3. Optionally, add more directories to monitor by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Component overview on the {{site.data.keyword.cloud_notm}}")

In this tutorial, you will learn how to configure an Ubuntu server to forward logs to an {{site.data.keyword.la_full_notm}} instance.

## Before you begin
{: #ubuntu_prereqs}

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Work in the US-South region. The {{site.data.keyword.la_full_notm}} is currently available in the US South region. **Note:** You can send data from an Ubuntu server that is located in the same region or in a different region. 

Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

Install the {{site.data.keyword.cloud_notm}} CLI. For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli/index.html#overview).



## Step 1. Provision an {{site.data.keyword.la_full_notm}} instance
{: #ubuntu_step1}

To provision an instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    Click [{{site.data.keyword.cloud_notm}} dashboard ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window} to launch the {{site.data.keyword.cloud_notm}} dashboard.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click the **{{site.data.keyword.la_full_notm}}** tile.

5. Enter a name for the service instance.

6. Select the **Default** resource group. 

    By default, the **Default** resource group is set.

7. Select the **Lite** service plan. 

    By default, the **Lite** plan is set.

    For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

8. To provision the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}} resource group where you are logged in, click **Create**.

After you provision an instance, the {{site.data.keyword.la_full_notm}} dashboard opens. 


**Note:** To provision an instance of LogDNA through the CLI, see [Provisioning LogDNA through the {{site.data.keyword.cloud_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-provision#provision_cli).


## Step 2. Configure your Ubuntu server to send logs to your instance
{: #ubuntu_step2}

To configure your Ubuntu server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logdna-agent`. The LogDNA agent reads log files from */var/log*, and forwards the log data to your LogDNA instance.

To configure your Ubuntu server to forward logs to your LogDNA instance, complete the following steps from an Ubuntu terminal:

1. Install the LogDNA agent. Run the following commands:

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. Set the ingestion key that the LogDNA agent must use to forward logs to the {{site.data.keyword.la_full_notm}} instance.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    where INGESTION_KEY contains the ingestion key active for the {{site.data.keyword.la_full_notm}} instance where you are configuring to forward logs.

3. Set the authentication endpoint. The LogDNA agent uses this host to authenticate and get the token to forward logs.

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. Set the ingestion endpoint.

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. Define more log paths to be monitored. Run the following command: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    By default, **/var/log** is monitored.

6. Optionally, configure the LogDNA agent to tag your hosts. Run the following commands:

    ```
    sudo logdna-agent -t TAG1,TAG2 
    ```
    {: codeblock}

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}


## Step 3. Launch the LogDNA Web UI
{: #ubuntu_step3}

To launch IBM the Log Analysis with LogDNA dashboard through the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

    Click [{{site.data.keyword.cloud_notm}} dashboard ![External link icon](../../icons/launch-glyph.svg "External link icon")](https://cloud.ibm.com/login){:new_window} to launch the {{site.data.keyword.cloud_notm}} dashboard.

	After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. 

    The list of {{site.data.keyword.la_full_notm}} instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

3. Select one instance. Then, click **View LogDNA**.

    The LogDNA Web UI opens and displays your cluster logs.


## Step 4. View your logs
{: #ubuntu_step4}

From the LogDNA Web UI, you can view your logs as they pass through the system. You view logs by using log tailing. 

**Note:** With the **Free** service plan, you can only tail your latest logs.

For more information, see [Viewing logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs).


## Next steps
{: #ubuntu_next_steps}

[Filter logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [search logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [define views](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7), and [configure alerts](https://docs.logdna.com/docs/alerts). 

**Note:** To use any of these features, you must upgrade the {{site.data.keyword.la_full_notm}} plan to a paid plan.

