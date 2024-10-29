---

copyright:
  years:  2018, 2024
lastupdated: "2024-10-29"

keywords: IBM, Log Analysis, logging, powerVS, tutorial, ppc64le

subcollection: log-analysis

content-type: tutorial
account-plan: lite
completion-time: 1h

---

{{site.data.keyword.attribute-definition-list}}


# Logging with PowerVS
{: #powervs-rhel}
{: toc-content-type="tutorial"}
{: toc-completion-time="1h"}

Use the {{site.data.keyword.la_full}} service to monitor and manage logs from a PowerVS instance running RHEL in a centralized logging system on the {{site.data.keyword.cloud_notm}}.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}


You can collect and monitor system and application logs.

You can send logs to an {{site.data.keyword.la_full_notm}} instance via Rsyslog.
- TCP, UDP, and TCP+TLS are supported.

    - Use port 6514 when using TCP+TLS.

    - Use port 514 when using TCP or UDP.

    - Use a custom port if you cannot modify the message template for rsyslog with the logging instance information.

        To configure syslog, you may need to enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in `syslog-ng`, or (c) a custom port in `rsyslog`, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
        {: important}

        To disable a custom port, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Creating support cases](/docs/account?topic=account-open-case&interface=ui).

- The rsyslog default format, RFC 5424 and RFC 3164 are automatically parsed.


The rsyslog service must be installed on the PowerVS instance that you want to monitor. Rsyslog defaults to using TCP on port 514.
{: note}



On the {{site.data.keyword.cloud_notm}}, configure a PowerVS instance to forward logs to an {{site.data.keyword.la_short}} instance by completing the following steps:


## Prerequisites
{: #powervs-rhel-prereqs}

- Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration](https://cloud.ibm.com/login){: external}.

### {{site.data.keyword.la_short}}
{: #powervs-rhel-prereqs-la}

- [Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources](/docs/log-analysis?topic=log-analysis-work_iam). For example, to work in the US-south region and in the default resource group, you need the following permissions:

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group      | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
{: caption="List of IAM policies" caption-side="top"}

Provision a service instance of {{site.data.keyword.la_short}} through the {{site.data.keyword.cloud_notm}} console. For more information, see [Provisioning an instance](/docs/log-analysis?topic=log-analysis-provision).


### Power VS
{: #powervs-rhel-prereqs-power}


- Learn more about [Using RHEL within the Power Systems Virtual Server service](/docs/power-iaas?topic=power-iaas-linux-with-powervs).

- Provision a PowerVS instance that is connected to the public network and is registered with subscription manager. [Learn more](/docs/power-iaas?topic=power-iaas-getting-started).


- Enable syslog for your RHEL instance:

    ```
    subscription-manager repos --enable rhel-8-for-ppc64le-supplementary-rpms
    ```
    {: codeblock}



## Get the {{site.data.keyword.la_short}} instance ingestion data
{: #powervs-rhel-step1}
{: step}

To configure rsyslog, you need the following data:

- The **ingestion key** of the {{site.data.keyword.la_short}} instance. See [Working with ingestion keys](/docs/log-analysis?topic=log-analysis-ingestion_key).

- The region where the {{site.data.keyword.la_short}} instance is provisioned.




## Configure rsyslog in your PowerVS instance
{: #powervs-rhel-step2}
{: step}

Complete the following steps to configure rsyslog on Red Hat Enterprise Linux:

1. Log in as `root`.

2. Modify the file `/etc/rsyslog.conf`. For example, you can use the vi editor to modify the file.

    Uncomment the following lines:

    ```
    #module(load="imudp")
    #input(type="imudp" port="514")

    #module(load="imtcp")
    #input(type="imtcp" port="514")
    ```
    {: screen}

    Add the following lines at the end of the file:

    ```
    #Save Deep Security Manager (DSM) logs to DSM.log
    Local4.* /var/log/DSM.log
    ```
    {: screen}

    Replace `Local4` with the value on your Manager settings.

    Save the file and exit.

3. Create the `/var/log/DSM.log` file and set the permissions so that syslog can write data into the file. Run the following command:

    ```
    touch /var/log/DSM.log
    ```
    {: codeblock}

    ```
    chmod 777 /var/log/DSM.log
    ```
    {: codeblock}

4. Restart rsyslog. Run the following command:

    ```
    systemctl restart rsyslog
    ```
    {: codeblock}

5. Verify which ports rsyslog is listening to:

    ```
    netstat -tnlp | grep rsyslog
    ```
    {: codeblock}

6. Enter the following command as root to starts automatically rsyslog:

    ```
    chkconfig rsyslog on
    ```
    {: codeblock}


## Configure Rsyslog to send logs to {{site.data.keyword.la_short}} via TCP
{: #powervs-rhel-step3}
{: step}

Complete the following steps to configure Rsyslog to send logs to {{site.data.keyword.la_short}} via TCP:

1. Add the following entries to `/etc/rsyslog.d/22-logdna.conf`.

    ```text
    $template LogDNAFormat,"<%PRI%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [logdna@48950 key=\"INGESTION-KEY\" tags=\"tag1,tag2\"] %msg%"

    *.* @@syslog-a.<REGION>.logging.cloud.ibm.com:514;LogDNAFormat
    ```
    {: codeblock}

    Where

    **INGESTION-KEY** is the logging instance ingestion key. For more information, see [Working with ingestion keys](/docs/log-analysis?topic=log-analysis-ingestion_key).

    **REGION** must be set to the location where the logging instance is available. For more information about syslog endpoints, see [Syslog endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog).

2. Restart rsyslog.

    ```sh
    systemctl restart rsyslog
    ```
    {: pre}




## Next steps
{: #powervs-rhel-next}

From the logging Web UI, you can view your logs as they pass through the system. You view logs by using log tailing.For more information, see [Viewing logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs).

With the **Free** service plan, you can only tail your latest logs.
{: note}

Try out the following additional features:

* [Filtering logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step5)
* [Searching logs](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step6)
* [Defining views](/docs/log-analysis?topic=log-analysis-view_logs#view_logs_step7)
* [Configuring alerts](/docs/log-analysis?topic=log-analysis-alerts).

To use any of these features, you must upgrade the {{site.data.keyword.la_full_notm}} plan to a paid plan.
{: note}
