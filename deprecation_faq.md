---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-01"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Frequently asked questions (FAQ) about the deprecation
{: #deprecation_faq}

Frequently asked questions about the deprecation of {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}}. 
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

## Deprecation FAQs
{: #dep_faqs}

### Are both {{site.data.keyword.at_full_notm}} and {{site.data.keyword.atracker_full_notm}} deprecated?
{: #dfaq_18}
{: faq}

No, only {{site.data.keyword.at_full_notm}} is being deprecated. Activity tracker events will be supported in both the new {{site.data.keyword.logs_full_notm}} service and with the existing [{{site.data.keyword.atracker_full_notm}}](/docs/atracker) service.

### Can I use {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} after the deprecation announcement date?
{: #dfaq_1}
{: faq}

Yes. Deprecation is a process. Deprecation starts with an announcement and ends with end of support. {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} are announced as deprecated on 28 March 2024 and will reach end of support on 30 March 2025.


### What is the difference between end of support and end of life?
{: #dfaq_2}
{: faq}

For some deprecations the end of support and end of life dates are different. End of support is the last time IBM supports a service. End of life is the date the service can no longer be used. For the deprecation of {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} the end of support and end of life date are the same (30 March 2025).


### How will the {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} pricing plans be managed?
{: #dfaq_3}
{: faq}

{{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} offers different pricing plans. For example: 7 days, 14 days, 30 days, and so on. All plans are deprecated as part of the announcement.

### How are {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} related?
{: #dfaq_4}
{: faq}

{{site.data.keyword.la_full_notm}} handles logging data and {{site.data.keyword.at_full_notm}} handles activity tracker event data.

While the two services manage different data, they are built on the same core technology. Both services are deprecated because the core techology on which they are based is deprecated.

### Will I lose access to data stored in {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}?
{: #dfaq_5}
{: faq}

No. If you need to keep {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} data, configure archiving for the services. Archiving writes the service data to {{site.data.keyword.cos_full_notm}}.

As long as archiving is configured, data will remain in {{site.data.keyword.cos_full_notm}} for as long as you want to keep it.

You will lose access to non-archived data in {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} on the end of support date.

For information on archiving, see:
{: #laat-archive}

* [{{site.data.keyword.la_full}} archiving](/docs/log-analysis?topic=log-analysis-archiving-ov)
* [{{site.data.keyword.at_full_notm}} archiving](/docs/activity-tracker?topic=activity-tracker-archiving-ov)

### How long can I keep my {{site.data.keyword.cos_full_notm}} archive data?
{: #dfaq_6}
{: faq}

You can keep your archived data as long as you want. Data archived to {{site.data.keyword.cos_full_notm}} is not affected by the deprecation of {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}.

## {{site.data.keyword.logs_full_notm}} FAQs
{: #cl_faq}

### Is {{site.data.keyword.logs_full_notm}} available today?
{: #dfaq_17}
{: faq}

No. {{site.data.keyword.logs_full_notm}} is planned to be generally available late second quarter 2024.

### Does {{site.data.keyword.logs_full_notm}} have a free plan?
{: #dfaq_7}
{: faq}

{{site.data.keyword.logs_full_notm}} does not have a free plan. There is a 7-day trial plan. This plan will ingest 7-days of data with fast data access for up to 5 GB of data. This data will be available for 30 days if you configure {{site.data.keyword.cos_full_notm}} buckets for the instance. After 7 days you will no longer be able to access the trial plan {{site.data.keyword.logs_full_notm}} instance, but your data will remain in the {{site.data.keyword.cos_full_notm}} bucket.

### What are the pricing differences between the gigabyte charges that the {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} services used and those used by {{site.data.keyword.logs_full_notm}}
{: #dfaq_price}
{: faq}

The new {{site.data.keyword.logs_full_notm}}, and legacy {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} services all charge by gigabytes processed into the service. The significant difference between {{site.data.keyword.logs_full_notm}} and the legacy {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} services is the ability to define the level of data processing performed on the ingested data.

* {{site.data.keyword.logs_full_notm}} allows clients flexibility to use a mixture of 3 data processing tiers to right-size the value and optimize cost.

* {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} support only 1 type of processing which often led to higher costs because a higher service tier was needed for only a subset of the data.

### Will {{site.data.keyword.logs_full_notm}} support the same regions as {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}?
{: #dfaq_8}
{: faq}

{{site.data.keyword.logs_full_notm}} supports the same regions as {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} with one exception. {{site.data.keyword.logs_full_notm}} will not be available in Chenai (IN-CHE). 

If you are using {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} in Chenai (IN-CHE) you will need to migrate to an {{site.data.keyword.logs_full_notm}} instance in a supported region.

<!--
### How does {{site.data.keyword.logs_full_notm}} compare to {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}?
{: #dfaq_9}
{: faq}

While the foundational features of the three services remain the same, {{site.data.keyword.logs_full_notm}} provides expanded features that offer greater insight, flexibility, and control.

_include-segments/at_la_cl_comparison.md
 -->

### What log retention is available for the {{site.data.keyword.logs_full_notm}} service?
{: #dfaq_clret}
{: faq}

{{site.data.keyword.logs_full_notm}} handles retention differently than the legacy {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} services. The new solution provides greater retention flexibility.

{{site.data.keyword.logs_full_notm}} users connect their provisioned {{site.data.keyword.cos_full_notm}} buckets to their service instance. Data flowing through the service instance is saved to {{site.data.keyword.cos_full_notm}} buckets and this data can be searched using {{site.data.keyword.logs_full_notm}}. Data can also be retained in the service and temporarily held in hot storage to be searched through {{site.data.keyword.logs_full_notm}}. The hot storage feature, called *Priority Insights*, is similar to how {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} retain data today.

All data kept in {{site.data.keyword.cos_full_notm}} is also available for search in {{site.data.keyword.logs_full_notm}}. If a client has 81 days saved to search, they will have 81 days of retention. Data retained in hot storage is retained in hot storage for the configured amount of time. {{site.data.keyword.logs_full_notm}} will offer retention periods for 7, 14, 30, 60, and 90 days in hot storage (*Priority Insights*). If data is sent to hot storage and the client has connected their {{site.data.keyword.cos_full_notm}} buckets, the data will initially be searchable using the hot storage copy of data then by searching the same data direct from {{site.data.keyword.cos_full_notm}} once the hot storage period has expired.

Regarding the {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} HIPAA plans, these special service plans will go away with {{site.data.keyword.logs_full_notm}}. All {{site.data.keyword.logs_full_notm}} premium options will be HIPAA enabled. Clients are still expected to have a Business Associate Contract (BAA) with IBM. Clients are also reminded to use {{site.data.keyword.logs_full_notm}} for operations observability data. {{site.data.keyword.logs_full_notm}} service is enabled in the event HIPAA controlled data leaks through log data sent to the tool. {{site.data.keyword.logs_full_notm}} is not intended to be an active repository for HIPAA data. Applications should be designed to mask sensitive data before sending data to {{site.data.keyword.logs_full_notm}}.

### Do I need an {{site.data.keyword.cos_full_notm}} instance configured to use {{site.data.keyword.logs_full_notm}}?
{: #dfaq_needcos}
{: faq}

{{site.data.keyword.logs_full_notm}} uses {{site.data.keyword.cos_full_notm}} buckets that you own to store processed data as an archive. You can then use {{site.data.keyword.logs_full_notm}} to search all historical data and metadata, as well as any high-speed data that you might be receiving in the tool. You can also access data in the {{site.data.keyword.cos_full_notm}} buckets directly for whatever business purposes may be required.

Using {{site.data.keyword.logs_full_notm}} without {{site.data.keyword.cos_full_notm}} buckets is possible, but not recommended. When {{site.data.keyword.logs_full_notm}} is used without attached {{site.data.keyword.cos_full_notm}} buckets you will lose ability to search data outside of the data being sent to the *Priority insights* pipeline.


## Migration FAQs
{: #mig_faq}

### What capability is available to migrate to {{site.data.keyword.logs_full_notm}}?
{: #dfaq_10}
{: faq}

The tool to let you migrate configurations from {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}} will be available when {{site.data.keyword.logs_full_notm}} is generally available.

### How can we use the log data we have in {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} in the new {{site.data.keyword.logs_full_notm}} that was gathered by the LogDNA agent? Will a log data migration tool be provided? Is log data compatible between {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} and {{site.data.keyword.logs_full_notm}} and we don't need to migrate log data?
{: #dfaq_migdata}
{: faq}

Data aggregated with the {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} services can not be migrated to {{site.data.keyword.logs_full_notm}}. Clients are encouraged to archive logs from {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} then use their existing search solutions for data archived by those services.

### How can we migrate the dashboard settings, authorization settings, and alert triggers to {{site.data.keyword.logs_full_notm}}? Can those be migrated or do we need to create new settings?
{: #dfaq_migset}
{: faq}

Many configuration settings from {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} can be migrated with the migration tool once the tool is available. Dashboards and alerts are both migrated by the migration tool. Examples of other frequently used settings which can be migrated include parsing rules, exclusion rules, views, screens and groups.

### What configurations will the migration tool migrate?
{: #dfaq_11}
{: faq}

The migration tool will migrate {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} configurations to {{site.data.keyword.logs_full_notm}}. These include:

* Views
* Alerts
* Dashboards
* Screens
* Parsing rules
* Exclusion rules
* Index rate alerts
* Groups
* Archiving configurations

### Can I run {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} at the same time as I am testing {{site.data.keyword.logs_full_notm}}? How long can I do so?
{: #dfaq_12}
{: faq}

Yes. The migration process provides steps where you can run {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} at the same time as {{site.data.keyword.logs_full_notm}} so you can test that data is flowing and accessible in both services.

You can run parallel operations for as long as you like for testing. Parallel operations end when you delete your {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances or until the end of support date for those services when they will be automatically deleted.

It is recommended that you delete {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances when they are no longer needed, rather than waiting for the instances to be automatically deleted on the end of support date.

When you run {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} at the same time as {{site.data.keyword.logs_full_notm}}, you will be charged for usage of all service instances.
{: important}

### {{site.data.keyword.logs_full_notm}} is not yet supported in the region I need? How and when do I migrate?
{: #dfaq_13}
{: faq}

{{site.data.keyword.logs_full_notm}} will be deployed at regions starting at {{site.data.keyword.logs_full_notm}} general availability. New regions will be added over time.

While you might not want to use a different region, you should be confident to try {{site.data.keyword.logs_full_notm}} in the first available regions, including trying the migration processes and observing data running in parallel.

### Is there a migration walk-through I can reference?
{: #dfaq_14}
{: faq}

A reference and video walk-through will be available when {{site.data.keyword.logs_full_notm}} is generally available. These will show how to do a migration while running {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} at the same time as {{site.data.keyword.logs_full_notm}}.

### Should I wait to migrate until the region I intend to use is supported by {{site.data.keyword.logs_full_notm}}?
{: #dfaq_15}
{: faq}

You should start your investigation and migration testing well before the {{site.data.keyword.logs_full_notm}} region is available. By investigating and testing early, your migration will be easier.

### If I have multiple {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instances, how does the migration tool handle that?
{: #dfaq_16}
{: faq}

The migration tool can be run multiple times to migrate each instance. Alternatively, the migration tool can generate Terraform that you can modify to consolidate multiple {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} instances into a smaller number of {{site.data.keyword.logs_full_notm}} instances.

Using the migration tool is not a requirement. You can provision new {{site.data.keyword.logs_full_notm}} instances with new configurations.
{: tip}

### Can I use the migration tool after 30 March 2025?
{: #dfaq_19}
{: faq}

If you plan to migrate using the migration tool, you must do so before {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} are de-provisioned and deleted on 30 March 2025.

### Can {{site.data.keyword.logs_full_notm}} access my data that is stored in my {{site.data.keyword.cos_full_notm}} buckets? When using {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} I had to use other tools to access data archived to {{site.data.keyword.cos_full_notm}} buckets.
{: #dfaq_cos_access}
{: faq}

Yes, with {{site.data.keyword.logs_full_notm}} all of the historical data stored in your {{site.data.keyword.cos_full_notm}} buckets is accessible and searchable using {{site.data.keyword.logs_full_notm}}. No other tools are required. However, any tools that can read data from {{site.data.keyword.cos_full_notm}} buckets can also be used, as you might have done with the previous solutions.

