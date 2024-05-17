---

copyright:
  years: 2022, 2024
lastupdated: "2024-05-17"

keywords:

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are you getting an error message when starting the Windows 3.6 agent?
{: #troubleshoot-09}
{: troubleshoot}
{: support}

You are are trying to start the {{site.data.keyword.la_full}} 3.6 agent for Windows and it fails to start with a 1067 error.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

You receive a message: `Windows could not start the Mezmo Agent service on Local Computer.  Error 1067: The process terminated unexpectedly.`

Additional error details can be found in the agent service log.

```text
C:\ProgramData\logs\logdna-agent-svc_???.log
```
{: codeblock}
{: tsSymptoms}

The `logdna.conf` file has an incorrect configuration.
{: tsCauses}

[Edit your `logdna.conf` file](/docs/log-analysis?topic=log-analysis-config_agent_windows_v3) and correct any configuration errors. For example, this error occurs if you specify a file name in the `dirs:` section of the `logdna.conf` file.  The `dirs:` section must only include directories, not individual files.
{: tsResolve}
