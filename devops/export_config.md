---

copyright:
  years:  2018, 2024
lastupdated: "2024-03-27"

keywords: IBM, Log Analysis, logging, export logs

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Controlling who can export logs
{: #export_config}

For each {{site.data.keyword.la_full_notm}} instance, you can configure whether users can export data.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

When the export configuration setting is enabled, you can export data in JSONL format from an {{site.data.keyword.la_full_notm}} instance.


## Allowing users to export logs
{: #export_config_allow}

Complete the following steps to allow users to export logs from an {{site.data.keyword.la_full_notm}} instance:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Settings icon](../images/admin.png).

3. Select **Organization** &gt; **General**.

4. Set-on the **Export Log Lines** setting to allow users to export logs.



## Disable the export feature
{: #export_config_disable}

Complete the following steps to disable the export feature in an {{site.data.keyword.la_full_notm}} instance:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/log-analysis?topic=log-analysis-launch).

2. Click the **Settings** icon ![Settings icon](../images/admin.png).

3. Select **Organization** &gt; **General**.

4. Set-off the **Export Log Lines** setting to prevent users from exporting logs.
