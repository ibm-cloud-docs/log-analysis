---

copyright:
  years: 2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are your events not being archived?
{: #troubleshoot-12}
{: troubleshoot}
{: support}

Archiving is configured for your account and your events are not being archived.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

Events are not being archived. You [access the archiving configuration UI](/docs/log-analysis?topic=log-analysis-archiving#archiving_step8) and see the following message:

```text
If an invalid configuration which prevents uploads (ex. insufficient permissions) is detected and persists for over 24 hours, automatic archiving will be disabled for this account.
```
{: screen}
{: tsSymptoms}

Permissions are incorrectly configured or the API key is incorrect or was changed. Archving will retry for 24 hours, but, if not corrected, archiving will stop after that point.
{: tsCauses}

Ensure that [permissions are correctly configured](/docs/log-analysis?topic=log-analysis-archiving#archiving_step7) for archiving for the account. You can also use {{site.data.keyword.at_full}} templates to [monitor your archiving for potential errors.](/docs/activity-tracker?topic=activity-tracker-templates-archiving#archive_template_views)
{: tsResolve}
