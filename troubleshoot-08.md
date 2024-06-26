---

copyright:
  years: 2022, 2024
lastupdated: "2024-05-24"

keywords: IBM Cloud, Log Analysis, keys, troubleshooting

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are your logs not being routed to another region as configured?
{: #troubleshoot-08}
{: troubleshoot}
{: support}

You are routing logs using private endpoints to a different region and you cannot see the log entries in {{site.data.keyword.la_full}} in the destination region.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

You receive a message: `failed sending http request, retrying: request timed out!`.
{: tsSymptoms}

A network issue is causing an issue communicating between different regions.
{: tsCauses}

Research and resolve the network issue.
{: tsResolve}
