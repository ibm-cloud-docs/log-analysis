---

copyright:
  years:  2021, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, AIX, tutorial

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Logging with PowerVS running AIX (WIP)
{: #powervs-aix}

Use the {{site.data.keyword.la_full}} service to monitor and manage logs from a PowerVS instance running AIX in a centralized logging system on the {{site.data.keyword.cloud_notm}}.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

To monitor and manage logs from a PowerVS instance running AIX on the IBM Cloud, you can use IBM Log Analysis. You must configure Rsyslog in your AIX system to send logs to a Log Analysis instance.


You can collect and monitor system and application logs.

You can send logs to an {{site.data.keyword.la_full_notm}} instance via Rsyslog.
- TCP, UDP, and TCP+TLS are supported.

    - Use port 6514 when using TCP+TLS.

    - Use port 514 when using TCP or UDP.

    - Use a custom port if you cannot modify the rsyslog settings.

        To configure syslog, you may need to enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in `syslog-ng`, or (c) a custom port in `rsyslog`, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
        {: important}

        To disable a custom port, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Getting support](/docs/get-support).

- The rsyslog default format, RFC 5424 and RFC 3164 are automatically parsed.


The rsyslog service must be installed on the PowerVS instance that you want to monitor. Rsyslog defaults to using TCP on port 514.
{: note}

On the {{site.data.keyword.cloud_notm}}, configure a PowerVS instance to forward logs to an {{site.data.keyword.la_short}} instance by completing the following steps:


## Prerequisites
{: #powervs-aix-prereqs}

- Use a user ID that is a member or an owner of an {{site.data.keyword.cloud_notm}} account. To get an {{site.data.keyword.cloud_notm}} user ID, go to: [Registration](https://cloud.ibm.com/login){: external}.

ssh-keygen -t rsa

rsyslog

```
 "mail messages, at debug or higher, go to Log file. File must exist."
# "all facilities, at debug and higher, go to console"
# "all facilities, at crit or higher, go to all users"
#  mail.debug           /usr/spool/mqueue/syslog
#  *.debug              /dev/console
#  *.crit                       *
*.debug              /var/log/syslog.debug100k.out  rotate size 100k files 4
*.crit               /var/log/syslog.dailycrit.out  rotate time 1d

```



- Check if syslog is active. If it is not active start it.
# lssrc -s syslogd
Subsystem Group PID Status
syslogd ras active

If syslog is active, then refresh the daemon to read the new configuration.
# refresh -s syslogd

If syslog is not active then start it using SRC.
# startsrc -s syslogd

change /etc/ssh/sshd_config


### {{site.data.keyword.la_short}}
{: #powervs-aix-prereqs-la}

- [Your {{site.data.keyword.IBM_notm}}ID must have assigned IAM policies for each of the following resources](/docs/log-analysis?topic=log-analysis-work_iam). For example, to work in the US-south region and in the default resource group, you need the following permissions:

| Resource                             | Scope of the access policy | Role    | Region    | Information                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Resource group **Default**           |  Resource group            | Viewer  | us-south  | This policy is required to allow the user to see service instances in the Default resource group.    |
| {{site.data.keyword.la_full_notm}} service |  Resource group      | Editor  | us-south  | This policy is required to allow the user to provision and administer the {{site.data.keyword.la_full_notm}} service in the Default resource group.   |
{: caption="Table 1. List of IAM policies" caption-side="top"}

Provision a service instance of {{site.data.keyword.la_short}} through the {{site.data.keyword.cloud_notm}} console. For more information, see [Provisioning an instance](/docs/log-analysis?topic=log-analysis-provision).


### Power VS
{: #powervs-aix-prereqs-power}


- Learn more about [Creating an AIX virtual machine (VM)](/docs/power-iaas?topic=power-iaas-create-vm).

- Provision a PowerVS instance that is connected to the public network


- Enable syslog for your RHEL instance:

    ```
    subscription-manager repos --enable rhel-8-for-ppc64le-supplementary-rpms
    ```
    {: codeblock}
















1. [Configure a Syslog server and client on your AIX system.](https://www.ibm.com/support/pages/how-setup-basic-syslog-server-and-client-remote-logging){: external}

2. [Download and install `rsyslog` in place of the native Syslog logging service.](https://www.ibm.com/support/pages/ibm-aix-how-download-install-and-use-rsyslog-place-native-syslog-logging-service){: external}

3. Edit the `/etc/rsyslog.conf` file and add the following to the file.

   ```text
   ### START LogDNA rsyslog logging directives ###

   $template LogDNAFormat,"<%PRI%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [logdna@48950 key=\"INGESTIONKEY

   # Send messages to LogDNA over TCP using the template.
   *.* @@syslog-a.eu-gb.logging.cloud.ibm.com:514;LogDNAFormat

   ### END LogDNA rsyslog logging directives ###
   ```
   {: codeblock}

4. [Configure the log files to be monitored by adding the following to the `/etc/rsyslog.conf` file.](https://www.ibm.com/support/pages/use-rsyslog-monitor-log-file-and-generate-syslog-items){: external}

   ```text
   ### Adding log files ####
   $ModLoad imfile
   $InputFileName <PATH/FILENAME>
   $InputFileTag <APP-NAME-THAT GENERATES LOG FILE>:
   $InputFileStateFile /tmp/processlog_state
   $InputFileSeverity info
   $InputFileFacility local3
   $InputRunFileMonitor
   ```
   {: codeblock}

   For example:

   ```text
   ### Adding log files ####
   $ModLoad imfile
   $InputFileName /opt/prometheus/telegraf/telegraf.log
   $InputFileTag log-telegraf:
   $InputFileStateFile /tmp/processlog_state
   $InputFileSeverity info
   $InputFileFacility local3
   $InputRunFileMonitor
   ```
   {: codeblock}

5. Restart the [`rsyslogd`](https://www.ibm.com/docs/en/aix/7.2?topic=r-rsyslogd-daemon){: external} daemon to pick up the changes.

   1. Stop the daemon by running one of the following commands.

      ```text
      ps -ef | grep rsyslog
      ```
      {: pre}

      or

      ```text
      stopsrc -s rsyslogd
      ```
      {: pre}

   2. Start the daemon by running the following command

      ```text
      startsrc -s rsyslogd
      ```
      {: pre}
