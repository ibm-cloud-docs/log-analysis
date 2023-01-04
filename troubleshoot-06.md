---

copyright:
  years: 2022, 2023
lastupdated: "2021-02-08"

keywords: IBM Cloud, Log Analysis, streaming, troubleshooting

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are you getting a failed to connect message when configuring streaming?
{: #troubleshoot-06}
{: troubleshoot}
{: support}

You are trying to configure streaming and receive a "failure to connect" error.
{: shortdesc}

You are trying to configure streaming and receive a message similar to the following: `Failed to connect: Port should be >= 0 and < 65536. Received NaN.`
{: tsSymptoms}

You are attempting to configure multiple **Bootstrap Server URLs** at the same time.
{: tsCauses}

Configure **Bootstrap Server URLs** one at a time clicking **Add another URL** to add each new URL.  Multiple URLs cannot be specified in a single **Bootstrap Server URLs** field and the **Bootstrap Server URLs** cannot include quotes or commas.
{: tsResolve}
