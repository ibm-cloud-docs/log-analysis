---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Logging with infrastructure overview
{: #infra_logging}

In {{site.data.keyword.la_short}}, you can send infrastructure logs to an {{site.data.keyword.la_full_notm}} instance from a broad range of sources:
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

## Logging with Kubernetes clusters
{: #infra_logging_cluster}

You can configure a logging agent to collect logs from a Kubernetes cluster and forward them to an instance of the {{site.data.keyword.la_full_notm}} service.

You can collect and monitor logs from a Kubernetes cluster that is located in the same {{site.data.keyword.cloud_notm}} region as your {{site.data.keyword.la_full_notm}} instance or in a different one. You can also collect and monitor logs from clusters that are located outside the {{site.data.keyword.cloud_notm}}.

To configure cluster-level logging for a Kubernetes cluster, you must complete the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service. With this step, you configure a centralized log management system where log data is hosted on {{site.data.keyword.cloud_notm}}.
2. Provision a cluster, for example, a standard cluster on the {{site.data.keyword.containerlong_notm}}.
3. Deploy and configure the logging agent in the cluster.

![Log Analysis component overview on the {{site.data.keyword.cloud_notm}}](../images/kube.png "Log Analysis component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for Kubernetes" caption-side="bottom"}

For more information, see [Logging with Kubernetes clusters](/docs/log-analysis?topic=log-analysis-kube).


## Logging with Bare metal
{: #infra_logging_bm}

You can use the {{site.data.keyword.la_full}} service to monitor and manage logs from a bare metal in a centralized logging system on the {{site.data.keyword.cloud_notm}}. You can collect and monitor system and application logs.

By default, the logging agent on Linux servers monitors log files in the `/var/log` directory. For example, the Ubuntu system log (`/var/log/syslog`) is monitored by default.

On the {{site.data.keyword.cloud_notm}}, you can configure an bare metal to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision a bare metal running Ubuntu Linux.
2. Provision an instance of the {{site.data.keyword.la_full_notm}} service.
3. Configure the logging agent in the bare metal.
4. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for bare metal" caption-side="bottom"}

For more information, see [Logging with Bare metals](/docs/log-analysis?topic=log-analysis-ubuntu_baremetal).


## Logging with Linux VPC instances
{: #infra_logging_vpc}

You can use the {{site.data.keyword.la_full}} service to monitor and manage logs from a Linux VPC server instance in a centralized logging system on the {{site.data.keyword.cloud_notm}}. You can collect and monitor system and application logs.

By default, the logging agent for Linux VPC instances monitors log files in the `/var/log` directory. For example, the Ubuntu system log (`/var/log/syslog`) is monitored by default.

On the {{site.data.keyword.cloud_notm}}, you can configure a Linux VPC server to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision a VPC running Ubuntu Linux for example.
2. Provision an instance of the {{site.data.keyword.la_full_notm}} service.
3. Configure the logging agent in the Ubuntu server.
4. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/ubuntu.png "Component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for Ubuntu Linux" caption-side="bottom"}

For more information, see [Logging with Linux VPC server instances](/docs/log-analysis?topic=log-analysis-ubuntu).

## Logging with Syslog
{: #infra_logging_syslog}

You can send logs to an {{site.data.keyword.la_full_notm}} instance via Syslog. TCP and TCP+TLS are both supported.

To configure syslog, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in syslog-ng, or (c) a custom port in rsyslog, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance.  Depending on your environment, this may present a significant security risk. Use these configurations at your organization’s own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
{: important}

To use a custom port to send logs via UDP and to disable a custom port, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Getting support](/docs/get-support).

For more information on using Syslog, see [Logging with Syslog](/docs/log-analysis?topic=log-analysis-syslog).

## Logging with rsyslog
{: #infra_logging_rsyslog}

You can send logs to an {{site.data.keyword.la_full_notm}} instance via Rsyslog.
- TCP, UDP, and TCP+TLS are supported.

    - Use port 6514 when using TCP+TLS.

    - Use port 514 when using TCP or UDP.

    - Use a custom port if you cannot modify the message template for rsyslog with the logging instance information.

        To use a custom port, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in syslog-ng, or (c) a custom port in rsyslog, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance.  Depending on your environment, this may present a significant security risk. Use these configurations at your organization’s own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
        {: important}

        To disable a custom port, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Getting support](/docs/get-support).

- The rsyslog default format, RFC 5424 and RFC 3164 are automatically parsed.

### TCP+TLS
{: #infra_logging_rsyslog_1}

Complete the following steps to configure Rsyslog to send logs to {{site.data.keyword.la_short}} via TCP secured with TLS:

1. Download the [Root CA Certificate](https://assets.logdna.com/rootca/ld-root-ca.crt) and put it into `/etc/ld-root-ca.crt`.

2. Add the following entries to `/etc/rsyslog.d/22-logdna.conf`.

    ```text
    $DefaultNetstreamDriverCAFile /etc/ld-root-ca.crt # trust these CAs
    $ActionSendStreamDriver gtls # use gtls netstream driver
    $ActionSendStreamDriverMode 1 # require TLS
    $ActionSendStreamDriverAuthMode x509/name # authenticate by hostname
    $ActionSendStreamDriverPermittedPeer *.logdna.com

    $template LogDNAFormat,"<%PRI%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [logdna@48950 key=\"INGESTION-KEY\" tags=\"tag1,tag2\"] %msg%"

    *.* @@syslog-a.<REGION>.logging.cloud.ibm.com:6514;LogDNAFormat
    ```
    {: codeblock}

    Where

    **INGESTION-KEY** is the logging instance ingestion key. For more information, see [Working with ingestion keys](/docs/log-analysis?topic=log-analysis-ingestion_key).

    **REGION** must be set to the location where the logging instance is available. For more information about syslog endpoints, see [Syslog endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog).

3. Install `rsyslog-gnutls`.

4. Restart rsyslog.

    ```sh
    sudo /etc/init.d/rsyslog restart
    ```
    {: pre}



### TCP
{: #infra_logging_rsyslog_2}

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
    sudo /etc/init.d/rsyslog restart
    ```
    {: pre}

### UDP
{: #infra_logging_rsyslog_3}

Complete the following steps to configure Rsyslog to send logs to {{site.data.keyword.la_short}} via TCP:

1. Add the following entries to `/etc/rsyslog.d/22-logdna.conf`.

    ```text
    $template LogDNAFormat,"<%PRI%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [logdna@48950 key=\"INGESTION-KEY\" tags=\"tag1,tag2\"] %msg%"

    *.* @@syslog-u.<REGION>.logging.cloud.ibm.com:514;LogDNAFormat
    ```
    {: codeblock}

    Where

    **INGESTION-KEY** is the logging instance ingestion key. For more information, see [Working with ingestion keys](/docs/log-analysis?topic=log-analysis-ingestion_key).

    **REGION** must be set to the location where the logging instance is available. For more information about syslog endpoints, see [Syslog endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog).

2. Restart rsyslog.

    ```sh
    sudo /etc/init.d/rsyslog restart
    ```
    {: pre}

## Logging with ng-syslog
{: #infra_logging_ngsyslog}

You can send logs to an {{site.data.keyword.la_full_notm}} instance via ng-syslog.
- TCP, UDP, and TCP+TLS are supported.

    - Use port 6514 when using TCP+TLS.

    - Use port 514 when using TCP or UDP.

    - Use a custom port if you cannot modify the message template for rsyslog with the logging instance information.

        To use a custom port, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in `syslog-ng`, or (c) a custom port in `rsyslog`, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
        {: important}

        To disable a custom port, you can open an IBM support ticket. For information about opening an IBM support ticket, or about support levels and ticket severities, see [Getting support](/docs/get-support).

- The Syslog-ng default format, RFC 5424 and RFC 3164 are automatically parsed.





### TCP+TLS
{: #infra_logging_ngsyslog_1}

Complete the following steps to configure Rsyslog to send logs to {{site.data.keyword.la_short}} via TCP secured with TLS:

1. Download the [Root CA Certificate](https://assets.logdna.com/rootca/ld-root-ca.crt) and put it into `/etc/ld-root-ca.crt`.

2. Add the following entries to `/etc/syslog-ng/syslog-ng.conf`.

    ```text
    source s_logdna {
    system();    # Check which OS & collect system logs
    internal();    # Collect syslog-ng logs
    };

    template LogDNAFormat { template("<${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} ${MSGID} [logdna@48950 key=\"INGESTION-KEY\"] tags=\"prod,dev\"] $MSG\n");
        template_escape(no);
    };

    destination d_logdna {
        tcp("syslog-a.<REGION>.logging.cloud.ibm.com" port(6514)
        tls(cert-file("/etc/ld-root-ca.crt"))
        template(LogDNAFormat));
    };

    log {
        source(s_logdna);
        destination(d_logdna);
    };
    ```
    {: codeblock}

    Where

    **INGESTION-KEY** is the logging instance ingestion key. For more information, see [Working with ingestion keys](/docs/log-analysis?topic=log-analysis-ingestion_key).

    **REGION** must be set to the location where the logging instance is available. For more information about syslog endpoints, see [Syslog endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog).

3. Restart ng-syslog.

    ```sh
    sudo /etc/init.d/syslog-ng
    ```
    {: pre}



### TCP
{: #infra_logging_ngsyslog_2}

Complete the following steps to configure Rsyslog to send logs to {{site.data.keyword.la_short}} via TCP:

1. Add the following entries to `/etc/syslog-ng/syslog-ng.conf`.

    ```text
    source s_logdna {
    system();    # Check which OS & collect system logs
    internal();    # Collect syslog-ng logs
    };

    template LogDNAFormat { template("<${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} ${MSGID} [logdna@48950 key=\"INGESTION-KEY\"] tags=\"prod,dev\"] $MSG\n");
        template_escape(no);
    };

    destination d_logdna {
        tcp("syslog-a.<REGION>.logging.cloud.ibm.com" port(514)
        tls(cert-file("/etc/ld-root-ca.crt"))
        template(LogDNAFormat));
    };

    log {
        source(s_logdna);
        destination(d_logdna);
    };
    ```
    {: codeblock}

    Where

    **INGESTION-KEY** is the logging instance ingestion key. For more information, see [Working with ingestion keys](/docs/log-analysis?topic=log-analysis-ingestion_key).

    **REGION** must be set to the location where the logging instance is available. For more information about syslog endpoints, see [Syslog endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog).

2. Restart ng-syslog.

    ```sh
    sudo /etc/init.d/syslog-ng
    ```
    {: pre}

### UDP
{: #infra_logging_ngsyslog_3}

Complete the following steps to configure Rsyslog to send logs to {{site.data.keyword.la_short}} via TCP:

1. Add the following entries to `/etc/syslog-ng/syslog-ng.conf`.

    ```text
    source s_logdna {
    system();    # Check which OS & collect system logs
    internal();    # Collect syslog-ng logs
    };

    template LogDNAFormat { template("<${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} ${MSGID} [logdna@48950 key=\"INGESTION-KEY\"] tags=\"prod,dev\"] $MSG\n");
        template_escape(no);
    };

    destination d_logdna {
        tcp("syslog-u.<REGION>.logging.cloud.ibm.com" port(6514)
        tls(cert-file("/etc/ld-root-ca.crt"))
        template(LogDNAFormat));
    };

    log {
        source(s_logdna);
        destination(d_logdna);
    };
    ```
    {: codeblock}

    Where

    **INGESTION-KEY** is the logging instance ingestion key. For more information, see [Working with ingestion keys](/docs/log-analysis?topic=log-analysis-ingestion_key).

    **REGION** must be set to the location where the logging instance is available. For more information about syslog endpoints, see [Syslog endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_syslog).

2. Restart ng-syslog.

    ```sh
    sudo /etc/init.d/syslog-ng
    ```
    {: pre}


## Logging with Windows systems
{: #infra_logging_windows}

You can use the {{site.data.keyword.la_full}} service to monitor and manage logs from Windows systems.

NXLog is used to provide log files to {{site.data.keyword.la_full}}.

To configure NXLog, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in `syslog-ng`, or (c) a custom port in `rsyslog`, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
{: important}

By default, NXLog monitors log files in the `C:\\ProgramData\\logs` directory.

On the {{site.data.keyword.cloud_notm}}, configure an Windows server to forward logs to an {{site.data.keyword.la_full_notm}} instance by completing the following steps:

1. Provision an instance of the {{site.data.keyword.la_full_notm}} service.
2. Configure NXLog on the Windows server.
3. Optionally, add additional directories to be monitored by the agent.

![Component overview on the {{site.data.keyword.cloud_notm}}](../images/windows.svg "Component overview on the {{site.data.keyword.cloud_notm}}"){: caption="Log Analysis component overview on the {{site.data.keyword.cloud_notm}} for Windows" caption-side="bottom"}

For more information on logging from Windows systems, see the following:

* [Logging from a Windows client](/docs/log-analysis?topic=log-analysis-windows)
* [Logging from Windows Server systems](/docs/log-analysis?topic=log-analysis-windows_serv)
* [Logging with Windows VPC server instances](/docs/log-analysis?topic=log-analysis-windows_vpc_tutorial)



## Logging with AIX systems (WIP)
{: #infra_logging_aix}

You can use the {{site.data.keyword.la_full}} service to monitor and manage logs from AIX systems.

Logging from AIX systems is done using `rsyslog`.

For more information on logging from AIX system, see [Logging with AIX](/docs/log-analysis?topic=log-analysis-aix).


## Logging for VMware vCenter Server deployments
{: #infra_logging_vmware}

You can add logging capabilities to VMware vCenter Server deployments by configuring a centralized syslog server that collects logs from your vSphere environment and sends them to {{site.data.keyword.la_full_notm}} by using rsyslog for analysis, troubleshooting, and alerting.

[VMware templates](/docs/log-analysis?topic=log-analysis-templates-vmware) are available to gain insight on your VMware environments.
{: tip}

VMware vCenter Server® is a hosted private cloud that delivers the VMware vSphere® stack as a service. The VMware® environment is built in addition to a minimum of three {{site.data.keyword.cloud}} bare metal servers and it offers shared network-attached storage and dedicated software-defined storage options. It also includes the automatic deployment and configuration of an easy-to-manage logical edge firewall, which VMware NSX® powers. For more information, see [vCenter Server overview](/docs/vmwaresolutions?topic=vmwaresolutions-vc_vcenterserveroverview).

The following graphic depicts the high-level architecture and components of a three node vCenter Server with NSX-T deployment.

![Architecture of a vCenter Server NSX-T deployment](../images/Log-Analysis-05-VMware-vCenter-Architecture.svg "Architecture of a vCenter Server NSX-T deployment"){: caption="Figure 1. Architecture of a vCenter Server NSX-T deployment" caption-side="bottom"}

For more information on logging from VMware vCenter Server deployments, see [Logging for VMware vCenter Server deployments](/docs/log-analysis?topic=log-analysis-vmware-vcenter).

