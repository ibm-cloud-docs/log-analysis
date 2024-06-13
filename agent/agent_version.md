---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, config agent

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# About agent versions
{: #agent_version}


{{../_include-segments/deprecation_notice.md}}

The  {{site.data.keyword.la_full_notm}} agent version consists of multiple parts:

```text
X.Y.Z-<date>.[hash]
```
{: codeblock}

Where

- `X` represents the major version of an image.
- `Y` represents the minor version of an image.
- `Z` represents an incremental ID that determines the latest patched minor version.
- `<date>` represents the date that the image is built and available. The format is `YYYYMMDD`.
- `[hash]` represents the digest (manifest) of the container image. It is a unique `SHA-256` hash.


The tag that is associated to a logging image indicates whether the logging agent is automatically updated.
{: important}

For more information about the agent new features and new versions, see [Agent Release Notes](https://docs.mezmo.com/changelog){: external}.




## End of support
{: #agent_version_eos}

The  {{site.data.keyword.la_full_notm}} service supports `n-3` versions back based on the minor number.
{: note}

## Deprecation
{: #agent_version_deprecation}

When an agent version becomes unsupported, the agent version is maintained for vulnerabilities for 3 years. After 3 years, the image is deprecated and unavailable.

Unsupported versions of the  {{site.data.keyword.la_full_notm}} agent have a 3-year deprecation policy.
{: note}


## Determining installed {{site.data.keyword.la_short}} agent versions
{: #agent_version_ui}


For {{site.data.keyword.la_short}} agent v2 or greater, you can find the version of the agent in the `_ingester` field that you can find in the header of each log record, as part of the line context.
