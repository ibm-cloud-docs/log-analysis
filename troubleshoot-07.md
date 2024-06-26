---

copyright:
  years: 2022, 2024
lastupdated: "2024-05-24"

keywords: IBM Cloud, Log Analysis, keys, troubleshooting

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are you getting a message about an invalid or deactivated service key when configuring resources?
{: #troubleshoot-07}
{: troubleshoot}
{: support}

You are trying to configure a resource by using the logging API and you are using a service key that is no longer available.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

You are trying to configure a resource and you receive a message including: `Invalid or deactivated servicekey`.
{: tsSymptoms}

The service key you used on your request has been deleted or is no longer availble.
{: tsCauses}

Resubmit your request with a valid service key.
{: tsResolve}
