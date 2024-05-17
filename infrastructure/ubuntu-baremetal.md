---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords: IBM, Log Analysis, logging, ubuntu, tutorial, bare metal

subcollection: log-analysis

content-type: tutorial
account-plan: lite
completion-time: 1h

---

{{site.data.keyword.attribute-definition-list}}


# Logging with bare metal servers
{: #ubuntu_baremetal}
{: toc-content-type="tutorial"}
{: toc-completion-time="1h"}

Use the {{site.data.keyword.la_full}} service to monitor and manage logs from a bare metal server in a centralized logging system on the {{site.data.keyword.cloud_notm}}.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

These instructions are for Ubuntu Linux systems but can be used for other Linux systems.
{: note}

You can collect and monitor system and application logs.

By default, the logging agent for Ubuntu monitors log files in the `/var/log` directory. For example, the Ubuntu system log (`/var/log/syslog`) is monitored by default.

On the {{site.data.keyword.cloud_notm}}, configure a bare metal server to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision a bare metal server running Ubuntu Linux.
2. Provision an instance of the {{site.data.keyword.la_full_notm}} service.
3. Configure the logging agent in the bare metal server.
4. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/Log-Analysis-03-Ubuntu.svg "Component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Figure 1. Component overview on the {{site.data.keyword.cloud_notm}}" caption-side="bottom"}

In this tutorial, you will learn how to configure a bare metal server to forward logs to an {{site.data.keyword.la_full_notm}} instance.

## Before you begin
{: #ubuntu_baremetal_prereqs}

Read about {{site.data.keyword.la_full_notm}}. For more information, see [About](/docs/log-analysis?topic=log-analysis-getting-started#getting-started-ov).

Work in a [supported region](/docs/log-analysis?topic=log-analysis-regions).

You can send data from an Ubuntu instance that is located in the same region as your logging instance, in a different region, or not in the {{site.data.keyword.cloud_notm}}.
{: note}

Use a user ID that is a member, or an owner of, an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} {{site.data.keyword.IBM_notm}}ID, go to: [Create an account](https://cloud.ibm.com/login){: external}.

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources in the region that your {{site.data.keyword.la_full_notm}} instance is in:

Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources:

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group            | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the default resource group.   |
{: caption="Table 1. List of IAM policies required to complete the tutorial" caption-side="top"}

The {{site.data.keyword.cloud_notm}} CLI must be installed. For more information, see [Installing the {{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-install-ibmcloud-cli).

## Provision a bare metal server
{: #ubuntu_baremetal_step1}
{: step}

If you have a bare metal server that you want to monitor, you can skip this step.

If you don't have a bare metal server, complete the following steps

1. [Provision a bare metal server](/docs/bare-metal?topic=bare-metal-getting-started).

    To complete the steps in this topic, ensure you have internet access from the bare metal server. This is needed for configuring the monitoring agent.

2. Configure a VPN connection between your terminal and the bare metal server

    Virtual Private Networking (VPN) access enables users to manage all servers remotely and securely over the {{site.data.keyword.cloud}} private network. A VPN connection from your location to the private network allows out-of-band management and server rescue through an encrypted VPN tunnel. VPN tunnels can be initiated to any {{site.data.keyword.cloud_notm}} data center or PoP allowing you geographic redundancy.

    Complete the following steps to configure a VPN connection between your terminal and the bare metal server:

    1. [Enable VPN access on each account that needs VPN access](/docs/iaas-vpn?topic=iaas-vpn-getting-started#enable-user-vpn-access).

    2. Depending on your operating system, download the latest `MotionPro` 32-bit or 64-bit files from the Array Networks [Clients and Tools](https://support.arraynetworks.net/prx/001/http/supportportal.arraynetworks.net/downloads/downloads.html){: external} download site. [Learn more](/docs/iaas-vpn?topic=iaas-vpn-standalone-vpn-clients){: external}.

    3. Configure a standalone SSL VPN client and open a connection:

    For example, if you use the MotionPro Plus client for MacOS, to add a profile, click **Add**.

    In the `Basic` section, enter a `Title`. Enter a `Gateway`, for example, for a bare metal in Dallas 10, enter `vpn.dal10.softlayer.com`. Enter your VPN user name. Check that the `Port` is set to `443`. Then, click **OK**.

    To open a secure connection, click **Login**.

3. Connect to a bare metal server by using SSH

    You might require a VPN to access your system depending on your security setup and `ssh` configuration on the bare metal host.

    You must `ssh` to the host by using your credentials, or the root credentials that are available from the {{site.data.keyword.cloud_notm}} Console.

    You will require root permissions in order to install the monitoring agent.

    For example, you can complete the following steps to get the bare metal server information that you need to `ssh` into the server:

    1. [Log in to your {{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/login){: external}.

    2. Click the **Menu** icon ![Menu icon](../images/icon_hamburger.svg) &gt; **Classic Infrastructure** &gt; **Device List**.

    3. Identify the bare metal server that you want to monitor. Copy the **Public IP**.

    4. Click the bare metal server device name.

    5. Select **Passwords**. Copy the password for the **root** user.

       Then, from a terminal, run the following command:

       ```text
       ssh <USER_ID>@<IP_ADDRESS>
       ```
       {: pre}

       Where:

       `<USER_ID>` is the user ID that you use to log in to the bare metal server. For example, use `root`.

       `<IP_ADDRESS>` is the public IP address of the bare metal server.

       For example: `ssh root@45.123.122.12`


## Provision an {{site.data.keyword.la_full_notm}} instance
{: #ubuntu_baremetal_step2}
{: step}

To provision an instance of {{site.data.keyword.la_full_notm}} through the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [Log in to {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/login){: external} to sign in to the {{site.data.keyword.cloud_notm}}.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} console opens.

2. Click **Catalog**. The list of the services that are available in {{site.data.keyword.cloud_notm}} opens.

3. To filter the list of services that is displayed, click **Services** and select the **Logging and Monitoring** category.

4. Click the **{{site.data.keyword.la_full_notm}}** tile.

5. Select a region for the service instance.

6. Select the **Lite** service plan.

   By default, the **Lite** plan is set.

   For more information about other service plans, see [Pricing plans](/docs/log-analysis?topic=log-analysis-service_plans).

7. Specify a **Service name** for your {{site.data.keyword.la_full_notm}} service instance.

8. Select the **Default** resource group.

   By default, the **Default** resource group is set.

9. To provision the {{site.data.keyword.la_full_notm}} service in the {{site.data.keyword.cloud_notm}} selected resource group, click **Create**.

After you provision an instance, the {{site.data.keyword.la_full_notm}} dashboard opens.

To provision an instance of logging through the CLI, see [Provisioning logging through the {{site.data.keyword.cloud_notm}} CLI](/docs/log-analysis?topic=log-analysis-provision#provision_cli).
{: note}


## Configure a bare metal server to send logs to your logging instance
{: #ubuntu_baremetal_step3}
{: step}

To configure your bare metal server to send logs to your {{site.data.keyword.la_full_notm}} instance, you must install a `logging-agent`. The logging agent reads log files from `/var/log` or other directories you specify, and forwards the log data to your logging instance.

To configure your bare metal server to forward logs to your logging instance, complete the following steps from an Ubuntu terminal:

1. Install the logging agent. Run the following commands:

   ```text
   echo "deb https://assets.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list
   ```
   {: pre}

   ```text
   wget -O- https://assets.logdna.com/logdna.gpg | sudo apt-key add -
   ```
   {: pre}

   ```text
   sudo apt-get update
   ```
   {: pre}

   ```text
   sudo apt-get install logdna-agent < "/dev/null"
   ```
   {: pre}

2. Set the ingestion key that the logging agent will use to forward logs to the {{site.data.keyword.la_full_notm}} instance.

   ```text
   sudo logdna-agent -k <INGESTION_KEY>
   ```
   {: pre}

   where <INGESTION_KEY> contains the ingestion key for the {{site.data.keyword.la_full_notm}} instance where the logs will be forwarded.

   You can retrieve the ingestion key using the [{{site.data.keyword.cloud_notm}} console](/docs/log-analysis?topic=log-analysis-ingestion_key#ibm_cloud_ui), or by the [{{site.data.keyword.cloud_notm}} CLI](/docs/log-analysis?topic=log-analysis-ingestion_key#ingestion_key_cli).

3. Set the authentication endpoint. The logging agent uses this host to authenticate and get the token to forward logs.

   ```text
   sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
   ```
   {: pre}

4. Set the ingestion endpoint.

   ```text
   sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
   ```
   {: pre}

5. (Optional) Define any additional log paths to be monitored. Run the following command:

   ```text
   sudo logdna-agent -d <PATH_TO_LOG_FOLDERS>
   ```
   {: pre}

   Where <PATH_TO_LOG_FOLDERS> is the path where logs are saved on your system.  By default, `/var/log` is monitored.

6. (Optional) Configure the logging agent to tag your hosts. Run the following command:

   ```text
   sudo logdna-agent -t TAG1,TAG2
   ```
   {: pre}

   Tags must be separated by commas and without any spaces between the comma and tag name.
   {: note}

7. Update the logging agent with your changes.  Run the following command:

   ```text
   sudo update-rc.d logdna-agent defaults
   ```
   {: pre}

8. Start the logging agent.  Run the following command:

   ``` text
   sudo /etc/init.d/logdna-agent start
   ```
   {: pre}


### Troubleshooting
{: #ubuntu_baremetal_troubleshooting}

You can use the `/var/log/logdna-agent.log` log to determine if there are any issues with your `logdna-agent` installation.

## Launch the logging Web UI
{: #ubuntu_baremetal_step4}
{: step}

To launch the {{site.data.keyword.la_full_notm}} dashboard from the {{site.data.keyword.cloud_notm}} UI, complete the following steps:

1. Log in to your {{site.data.keyword.cloud_notm}} account.

   Click [{{site.data.keyword.cloud_notm}} dashboard](https://cloud.ibm.com/login){: external} to launch the {{site.data.keyword.cloud_notm}} dashboard.

   After you log in with your user ID and password, the {{site.data.keyword.cloud_notm}} Dashboard opens.

2. In the navigation menu, select **Observability**.

3. Click **Logging**.

   The list of {{site.data.keyword.la_full_notm}} instances that are available on {{site.data.keyword.cloud_notm}} is displayed.

4. Select one instance. Then, click **Open dashboard**.

   The logging Web UI opens and displays your cluster logs.


## View your logs
{: #ubuntu_baremetal_step5}
{: step}

From the logging Web UI, you can view your logs as they pass through the system. You view logs by using log tailing.

With the **Free** service plan, you can only tail your latest logs.
{: note}

For more information, see [Viewing logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs).


## Next steps
{: #ubuntu_baremetal_next_steps}

The following additional features are available:

* [Filtering logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step5)
* [Searching logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step6)
* [Defining views](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step7)
* [Configuring alerts](/docs/log-analysis?topic=log-analysis-alerts).

To use any of these features, you must upgrade the {{site.data.keyword.la_full_notm}} plan to a paid plan.
{: note}
