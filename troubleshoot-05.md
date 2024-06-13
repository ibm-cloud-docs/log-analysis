---

copyright:
  years: 2019, 2024
lastupdated: "2024-05-24"

keywords: IBM Cloud, Log Analysis, API, troubleshooting

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are you getting an error when you initialize terraform?
{: #troubleshoot-05}
{: troubleshoot}
{: support}

When you initialize terraform and you get a message that indicates that you cannot retrieve the list of available versions for a provider, you must rerun  `terraform init` with `-upgrade` to search for upgrades to the providers that you have configured and upgrade the plugins associated with those providers.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}


Failed to query available provider packages.
{: tsSymptoms}

Could not retrieve the list of available versions for your providers.
{: tsCauses}

Run `terraform init -upgrade` to get the new versions of the providers in your configuration.
{: tsResolve}
