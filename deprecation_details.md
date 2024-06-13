---

copyright:
  years:  2018, 2024
lastupdated: "2024-03-21"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Deprecation details
{: #deprecation_details}

These are the details about the deprecation of {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}}.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

* {{site.data.keyword.at_full_notm}} is being deprecated, but activity tracker events will be supported in both the new {{site.data.keyword.logs_full_notm}} service and with the existing [{{site.data.keyword.atracker_full_notm}}](/docs/atracker) service.

* The end of support date is also the end of life date. End of support and end of life are not separate events.

* The end of support and end of life is 30 March 2025 00:00:01 UTC. At that time all {{site.data.keyword.la_short}} and {{site.data.keyword.at_short}} instances deployed by all {{site.data.keyword.cloud_notm}} users will immediately be de-provisioned and deleted. As long as you have archiving configured, there will be no loss of data. If archiving is not configured, you could lose access to data that you might want to keep. 

   For information on archiving, see:

   * [{{site.data.keyword.la_full}} archiving](/docs/log-analysis?topic=log-analysis-archiving-ov)
   * [{{site.data.keyword.at_full_notm}} archiving](/docs/activity-tracker?topic=activity-tracker-archiving-ov)

* Any user that has archiving enabled will continue to have access to archived data in their {{site.data.keyword.cos_full_notm}} instances. Those {{site.data.keyword.cos_full_notm}} instances will remain as long as you want to keep them. {{site.data.keyword.IBM_notm}} they will not touch or remove your {{site.data.keyword.cos_full_notm}} instances as part of the deprecation process.

* {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} can be run in parallel with {{site.data.keyword.logs_full_notm}} during the transition so you can compare and test the operation between the services. Charges will acrue for all running instances during your testing period.

* A migration tool is planned to be released with {{site.data.keyword.logs_full_notm}} that will let a user do almost the entire migration automatically: from {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}}. The migration tool will also cover migration of related {{site.data.keyword.cloud_notm}} resources such as tags and {{site.data.keyword.iamshort}} permissions. With the migration tool you can automate as much of the migration as desired. You can control and review each step. The tool will migrate {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} configurations, but will not migrate data processed by those services.

If you plan to migrate using the migration tool, you must do so before {{site.data.keyword.la_full}} and {{site.data.keyword.at_full_notm}} are de-provisioned and deleted on 30 March 2025.
{: important}

* When {{site.data.keyword.logs_full_notm}} is released to the first {{site.data.keyword.cloud_notm}} region, you can, and should, begin your investigation and plan your migration. By starting early you can review the migration process and see how it works. You can deploy and begin using {{site.data.keyword.logs_full_notm}} in the initially available regions, even if you eventually want to migrate from those regions to a different region for your production use. The migration process begins for all users when {{site.data.keyword.logs_full_notm}} is available in the first region.

* {{site.data.keyword.logs_full_notm}} will not be supported in one {{site.data.keyword.cloud_notm}} region that is currently supported by {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}: Chennai (in-che). Anyone running {{site.data.keyword.la_short}} and {{site.data.keyword.at_short}} instances in Chennai (in-che) will need to move to another region when migrating to {{site.data.keyword.logs_full_notm}}.


