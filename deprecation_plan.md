---

copyright:
  years:  2018, 2024
lastupdated: "2024-03-13"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Planning the migration to {{site.data.keyword.logs_full_notm}}
{: #deprecation_plan}

Plan your migration from {{site.data.keyword.la_full}} or {{site.data.keyword.at_full_notm}} to {{site.data.keyword.logs_full_notm}}. 
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

This planning information applies to migrating from either {{site.data.keyword.la_full}} or {{site.data.keyword.at_full_notm}}. The dates provided are a suggestion to help you ensure a smooth migration to {{site.data.keyword.logs_full_notm}}.

{{site.data.keyword.logs_full_notm}} will not be supported in Chenai (IN-CHE). If you have {{site.data.keyword.la_full}} or {{site.data.keyword.at_full_notm}} instances in that region, you will need to migrate your observability work to a region supported by {{site.data.keyword.logs_full_notm}}.
{: important}

## March 2024
{: #dep-0324}

* Review the deprecation announcement and additional deprecation documentation.

## April 2024
{: #dep-0424}

* Review your {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} usage and make note of this information for migration steps.

   * What regions are running the instances?

   * What sources are sending data to those instances?

   * Is archiving enabled? Enable archiving if not enabled if you need to retain data from the deprecated services after end of support. For information on archiving, see:
   {: #plan-archive}

      * [{{site.data.keyword.la_full}} archiving](/docs/log-analysis?topic=log-analysis-archiving-ov)
      * [{{site.data.keyword.at_full_notm}} archiving](/docs/activity-tracker?topic=activity-tracker-archiving-ov)

* Make plans in your production schedule to begin using {{site.data.keyword.logs_full_notm}} and prepare for migration by the required deadlines.

## June 2024
{: #dep-0624}

* Review additional deprecation details when published.

* Determine the regions you want to use to test {{site.data.keyword.logs_full_notm}} when {{site.data.keyword.logs_full_notm}} is available in July 2024.

## July 2024
{: #dep-0724}

Test migration to {{site.data.keyword.logs_full_notm}}.

* Review the migration videos and other documentation to understand the migration process and tool.

* Understand how to run {{site.data.keyword.la_full_notm}} or {{site.data.keyword.at_full_notm}} in parallel with {{site.data.keyword.logs_full_notm}}.

* Test {{site.data.keyword.logs_full_notm}} in the first available region and test migrating to this region.

## August 2024
{: #dep-0824}

* Plan your migrations. Schedule the time needed based on your July 2024 testing.

## September 2024 - October 2024
{: #dep-0924}

* Migrate from {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} to each required region.

* Review and compare results from your {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances to your migrated {{site.data.keyword.logs_full_notm}} instances.

## November 2024 - December 2024
{: #dep-1124}

* Finalize testing and prepare to stop sending data to {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}}.

* Ensure you have [archiving](#plan-archive) enabled if you need to retain data from your {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances.

## January 2025
{: #dep-0125}

* Stop sending data to your {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances and continue with {{site.data.keyword.logs_full_notm}} as your observability solution.

* Verify that your [archived](#plan-archive) data has been captured.

* Delete your {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances.

## March 2025
{: #dep0-0325}

The following steps will be taken by IBM on March 30, 2025 00:00:01 UTC when {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} reaches end of support.

* All remaining {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances will be deleted.

* All {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} data not archived will be deleted.
