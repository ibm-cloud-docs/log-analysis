---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Logging agent
{: #log_analysis_agent}

The logging agent collects and forwards logs to your {{site.data.keyword.la_full_notm}} instance. After you provision an {{site.data.keyword.la_full}} instance, you must configure a logging agent for each log source that you want to monitor.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

You can configure a logging agent to connect to an {{site.data.keyword.la_full_notm}} instance through the public network or through the private network. By default, the agent connects through the public network. To connect to {{site.data.keyword.cloud}} services over a private network, you must have access to the classic infrastructure and [enable virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint) and connectivity to service endpoints for your account.

The logging agent authenticates by using the logging ingestion key and opens a secure web socket to the {{site.data.keyword.la_full_notm}} ingestion servers.

By default, the logging agent monitors all files with extension *.log*, and extensionless files under */var/log/*. The logging agent for Kubernetes automatically collects STDOUT and STDERR logs.

The logging agent tails for new log data, and looks for new files that are added to the logging directories that the agent monitors.

To configure a logging agent you will need to:

1. Understand your [storage requirements](/docs/log-analysis?topic=log-analysis-agent_storage).

2. Install the appropriate agent for your environment: [Kubernetes](/docs/log-analysis?topic=log-analysis-agent_kube) or [Linux](/docs/log-analysis?topic=log-analysis-agent_linux).

3. [Configure your agent.](/docs/log-analysis?topic=log-analysis-log_analysis_agent_configure)
