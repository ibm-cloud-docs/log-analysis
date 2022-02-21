---

copyright:
  years:  2018, 2022
lastupdated: "2022-02-21"

keywords: IBM, Log Analysis, logging, Windows, tutorial

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Logging from a Windows client 
{: #windows}

Use the {{site.data.keyword.la_full}} service to monitor and manage logs from Windows client systems. 
{: shortdesc}

You will use NXLog to add your Windows logs into {{site.data.keyword.la_full_notm}}.

To configure NXLog, you must enable a port to send logs via syslog to your logging instance. If you are using (a) the classic syslog protocol, (b) a custom port in `syslog-ng`, or (c) a custom port in `rsyslog`, there is no authentication available and anyone with knowledge of the endpoint can submit logs to your instance. As a result, depending on your environment, your use of the classic syslog protocol or custom port configurations with `syslog-ng` or `rsyslog` may present a significant security risk.  Use these configurations at your organization's own risk.  Validate with your compliance and security teams whether this security risk is acceptable to your organization.
{: important}

{{site.data.content.windows_prereqs}}

{{site.data.content.nxlog_install}}

{{site.data.content.nxlog_config}}

{{site.data.content.nxlog_run}}



