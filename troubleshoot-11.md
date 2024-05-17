---

copyright:
  years: 2023, 2024
lastupdated: "2024-05-17"

keywords:

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are you unable to install the {{site.data.keyword.la_full_notm}} agent on Red Hat Linux?
{: #troubleshoot-11}
{: troubleshoot}
{: support}

Installation of the {{site.data.keyword.la_full}} agent fails on Red Hat Linux.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

When you install the {{site.data.keyword.la_full_notm}} agent with the [agent installation instructions](/docs/log-analysis?topic=log-analysis-config_agent_rhel3), the installation fails when the `sudo yum install logdna-agent` command is run.
{: tsSymptoms}

You need to update the crypto policies default to `SHA1` for the `logdna-agent` before you install the agent.
{: tsCauses}

To resolve this issue, run the following commands before you run the `sudo yum install logdna-agent` command.

```sh
update-crypto-policies --set DEFAULT:SHA1
dnf install logdna-agent
update-crypto-policies --set DEFAULT:NO-SHA1
```
{: codeblock}
