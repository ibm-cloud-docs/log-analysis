---

copyright:
  years:  2018, 2021
lastupdated: "2021-03-28"

keywords: IBM, Log Analysis, logging, export logs

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

 
# Exporting logs through the logging UI
{: #export}

You can export log data in JSONL format from an {{site.data.keyword.la_full_notm}} instance graphically through the web UI.
{: shortdesc}

Consider the following information when you export log data:
* You can export a set of log entries. To define the set of data that you want to export, you can apply filter and searches. You can also specify the time range. 
* From the Web UI, when you export logs, you get an email that is sent to your email address, with a link to a compressed file that includes the data. To get the data, you must click the link and download the compressed file.
* The compressed log file that contains the data that you want to export is available for a maximum of 12 hours. 
* When you export logs, you have a limit of lines that you can export in a request. You can specify to export older lines or newer lines in case you reach the limit in the time range that you specify for the export. 


## Prerequisites
{: #export_prereqs}

* **You must have a paid service plan** for the {{site.data.keyword.la_full_notm}} service. [Learn more](/docs/log-analysis?topic=log-analysis-service_plans). 

* Check that your user ID has permissions to launch the web UI, view or manage service keys, and view logs. [Learn more](/docs/log-analysis?topic=log-analysis-view_logs).

* Check that the logging instance has the export feature enabled. [Learn more](/docs/log-analysis?topic=log-analysis-export_config).

## Exporting logs from the Web UI
{: #export_ui_view}

You can create a custom view and then export data for a period of time.

Complete the following steps to export log data through the logging web UI:

1. [Launch the logging web UI](/docs/log-analysis?topic=log-analysis-launch).
2. Click the **Views** icon ![Views icon](../images/views.png "Views icon").
3. Select a view.
4. Select the view name. 
5. Select **Export lines**. A new window opens.

    You can not export lines from the **EVERYTHING** view.  
    {: note}

6. Check the time range. If you need to change it, click the predefined time range in the *Time Range for Export* field.
7. Select **Prefer newer lines** or **Prefer older lines** in case the export request exceeds the line limit.
8. Check your email. You should receive an email with a link to download your exported lines.


## Exporting logs from a search
{: #export_ui_search}

You can export data from a custom search.

Complete the following steps to export data through the logging web UI:

1. [Launch the logging web UI](/docs/log-analysis?topic=log-analysis-launch).
2. Click the **Views** icon ![Views icon](../images/views.png "Views icon").
3. Select **Everything**.
4. Apply filters and search criteria until you see the entries that you want to export.
4. Click **Unsaved View**.
5. Select **Export lines**. A new window opens.
6. Check the time range. If you need to change it, click the predefined time range in the *Time Range for Export* field.
7. Select **Prefer newer lines** or **Prefer older lines** in case the export request exceeds the line limit.
8. Check your email. You receive an email with a link to download your exported lines.


