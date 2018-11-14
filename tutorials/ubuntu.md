---

copyright:
  years: 2018
lastupdated: "2018-11-15"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}


# Managing Ubuntu logs with IBM Log Analysis with LogDNA
{: #ubuntu}

Use the IBM Log Analysis with LogDNA service to monitor and manage Ubuntu logs in a centralized logging system on the {{site.data.keyword.Bluemix}}. 
{:shortdesc}

You can collect and monitor system and application logs. 

By default, the LogDNA agent for Ubuntu monitors log files in the **/var/log** directory. For example, the Ubuntu system log (*/var/log/syslog*) is monitored by default.

On the {{site.data.keyword.Bluemix_notm}}, to configure an Ubuntu server to forward logs to an IBM Log Analysis with LogDNA instance, you must complete the following steps:

1. Provision an instance of the IBM Log Analysis with LogDNA service. 
2. Configure the LogDNA agent in the Ubuntu server.
3. Optionally, add more directories to monitor by the agent.

![Component overview on the {{site.data.keyword.Bluemix_notm}}](../images/ubuntu.png "Component overview on the {{site.data.keyword.Bluemix_notm}}")

In this tutorial, you will learn how to configure an Ubuntu server to forward logs to an IBM Log Analysis with LogDNA instance.

## Before you begin
{: #prereqs}

Work in the US-South region. 

Read about IBM Log Analysis with LogDNA. For more information, see [About LogDNA](/docs/services/Log-Analysis-with-LogDNA/overview.html#about).

Use a user ID that is a member or an owner of an {{site.data.keyword.Bluemix_notm}} account. To get an {{site.data.keyword.Bluemix_notm}} user ID, go to: [Registration ![External link icon](../../../icons/launch-glyph.svg "External link icon")](https://console.bluemix.net/registration/){:new_window}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources: 

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| IBM Log Analysis with LogDNA service |  Resource group            | Editor  | us-south  | This policy is required to allow the user to provision and administer the IBM Log Analysis with LogDNA service in the Default resource group.   |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"} 

Install the {{site.data.keyword.Bluemix_notm}} CLI. For more information, see [Installing the {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli/index.html#overview).



## Step1: Provision an IBM Log Analysis with LogDNA instance
{: #step1}

To provision an instance of IBM Log Analysis with LogDNA through the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} UI opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.Bluemix_notm}} opens.

3. To filter the list of services that is displayed, select the **Developer Tools** category.

4. Click the **IBM Log Analysis with LogDNA** tile.

5. Enter a name for the service instance.

6. Select the **Default** resource group. 

    By default, the **Default** resource group is set.

7. Select the **Lite** service plan. 

    By default, the **Lite** plan is set.

    For more information about other service plans, see [Pricing plans](/docs/services/Log-Analysis-with-LogDNA/overview.html#pricing_plans).

8. To provision the IBM Log Analysis with LogDNA service in the {{site.data.keyword.Bluemix_notm}} resource group where you are logged in, click **Create**.

After you provision an instance, the IBM Log Analysis with LogDNA dashboard opens. 


**Note:** To provision an instance of LogDNA through the CLI, see [Provisioning LogDNA through the {{site.data.keyword.Bluemix_notm}} CLI](/docs/services/Log-Analysis-with-LogDNA/provision.html#provision_cli).


## Step2: Configure your Ubuntu server to send logs to your instance
{: #step2}

To configure your Ubuntu server to send logs to your IBM Log Analysis with LogDNA instance, you must install a `logdna-agent`. The LogDNA agent reads log files from */var/log*, and forwards the log data to your LogDNA instance.

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

2. Set the ingestion key that the LogDNA agent must use to forward logs to the IBM Log Analysis with LogDNA instance.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    where INGESTION_KEY contains the ingestion key active for the IBM Log Analysis with LogDNA instance where you are configuring to forward logs.

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


## Step 3: Launch the LogDNA Web UI
{: #step3}

To launch IBM the Log Analysis with LogDNA dashboard through the {{site.data.keyword.Bluemix_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.Bluemix_notm}} account.

    The {{site.data.keyword.Bluemix_notm}} dashboard can be found at: [http://bluemix.net ![External link icon](../../../icons/launch-glyph.svg "External link icon")](http://bluemix.net){:new_window}.

	After you log in with your user ID and password, the {{site.data.keyword.Bluemix_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**. 

3. Select **Logging**. 

    The list of IBM Log Analysis with LogDNA instances that are available on {{site.data.keyword.Bluemix_notm}} is displayed.

3. Select one instance. Then, click **View LogDNA**.

    The LogDNA Web UI opens and displays your cluster logs.


## Step 4: View your logs
{: step4}

From the LogDNA Web UI, you can view your logs as they pass through the system. You view logs by using log tailing. 

**Note:** With the **Free** service plan, you can only tail your latest logs.

For more information, see [Viewing logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#view_logs).


## Next steps
{: #next_steps}

[Filter logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step5), [search logs](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step6), [define views](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#step7), and [configure alerts](https://docs.logdna.com/docs/alerts). 

**Note:** To use any of these features, you must upgrade the IBM Log Analysis with LogDNA plan to a paid plan.

