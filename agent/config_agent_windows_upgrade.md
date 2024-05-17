---

copyright:
  years:  2022, 2024
lastupdated: "2024-05-17"

keywords: IBM, Log Analysis, logging, config agent, Windows

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Upgrading the Windows logging agent from V2 to V3
{: #upgrade_agent_windows}

The logging agent is responsible for collecting and forwarding logs to your {{site.data.keyword.la_full_notm}} instance. If you have installed V2 of the Windows agent you will want to upgrade to V3.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

To uninstall the you existing V2 Windows agent, run the following command.

```text
choco uninstall logdna-agent
```
{: pre}

Then install the V3 Windows agent using [these instructions.](/docs/log-analysis?topic=log-analysis-config_agent_windows_v3)
