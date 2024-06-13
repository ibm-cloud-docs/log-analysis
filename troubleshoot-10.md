---

copyright:
  years: 2023, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are you unable to access the {{site.data.keyword.la_full_notm}} dashboard? (WIP)
{: #troubleshoot-10}
{: troubleshoot}
{: support}

When using a VPN, you are unable to access the {{site.data.keyword.la_full}} dashboard.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

SYMPTOM
{: tsSymptoms}

There is a known issue that causes issues with the {{site.data.keyword.la_short}} dashboard being displayed when a VPN is running before the dashboard is started.
{: tsCauses}

To resolve this issue, access your {{site.data.keyword.la_short}} dashboard and start you VPN in the following order:

1. [Log in to the {{site.data.keyword.cloud_notm}}.](https://cloud.ibm.com/login){: external}

2. [Launch the {{site.data.keyword.la_full_notm}} dashboard.](/docs/log-analysis?topic=log-analysis-observe#observe_ui)

3. Start your desired VPN.

If this start order does not resolve your issue, [contact {{site.data.keyword.IBM_notm}} support.](/docs/log-analysis?topic=log-analysis-gettinghelp)
{: tsResolve}
