---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Limits when sending logs
{: #ingest_limits}

There are limits when you send send logs to an {{site.data.keyword.la_full}} instance.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

Body size
:   Maximum size of 10 MB at ingestion.

Message size
:   Maximum size of 16 KB at ingestion. After 16K, the ingested data is truncated.

Metadata size
:   Maximum size of 32 KB.

Hostname length
:   Maximum size of 256 characters.

App name length
:   Maximum size of 512 characters.

Log Level
:   Maximum size of 80 characters.

Tags
:   Maximum size of 80 characters.

Depth of nested fields
:   The maximum number of nested fields that are parsed at ingestion is 3.

Number of unique fields
:   A maximum of 500 fields are indexed per day.
