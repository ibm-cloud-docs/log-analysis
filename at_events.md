---

copyright:
  years:  2018, 2020
lastupdated: "2020-06-19"

keywords: LogDNA, IBM, Log Analysis, logging, audit, activity tracker, events, audit logs

subcollection: Log-Analysis-with-LogDNA

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}
{:important: .important}
{:note: .note}

---

# Auditing events for {{site.data.keyword.la_full_notm}}
{: #at_events}

As a security officer, auditor, or manager, you can use the Activity Tracker service to track how users and applications interact with the {{site.data.keyword.la_full_notm}} service in {{site.data.keyword.cloud}}.
{: shortdesc}

{{site.data.keyword.at_full_notm}} records user-initiated activities that change the state of a service in {{site.data.keyword.cloud_notm}}. You can use this service to investigate abnormal activity and critical actions and to comply with regulatory audit requirements. In addition, you can be alerted about actions as they happen. The events that are collected comply with the Cloud Auditing Data Federation (CADF) standard. For more information, see the [getting started tutorial for {{site.data.keyword.at_full_notm}}](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-getting-started).

{{site.data.keyword.la_full_notm}} automatically generates events so that you can track activity on your service instance.

## Management events
{: #at_events_mgt}

### Login actions
{: #at_events_admin}

| Action               | Description                |
|----------------------|----------------------------|
| `logdna.user.login`  | This event is generated when a user logs in to the LogDNA web UI. |
| `logdna.user.logout` | This event is generated when a user logs out to the LogDNA web UI. |
{: caption="Table 1. Events for log in actions" caption-side="top"} 


### Archiving
{: #at_events_archive}

| Action                                            | Description                |
|---------------------------------------------------|----------------------------|
| `logdna.instance-archiving.turn-on`               | This event is generated when an administrator enables archiving for a LogDNA instance.    |
| `logdna.instance-archiving.turn-off`              | This event is generated when an administrator disabled archiving for a LogDNA instance.   |
| `logdna.instance-archiving-configuration.create`  | This event is generated when an administrator configures archiving for a LogDNA instance. |
| `logdna.instance-archiving.backup`   `(MISSING)`  | This event is generated when archiving is triggered for a LogDNA instance.                |          
{: caption="Table 1. Events for archiving actions" caption-side="top"} 


### Ingestion keys
{: #at_events_ingestion_keys}

| Action                               | Description                |
|--------------------------------------|----------------------------|
| `logdna.ingestion-key.create`        | This event is generated when an administrator creates an ingestion key through the LogDNA web UI. |
| `logdna.ingestion-key.delete`        | This event is generated when an administrator deletes an ingestion key through the LogDNA web UI. |
{: caption="Table 1. Events for ingestion keys actions" caption-side="top"} 


### Service keys
{: #at_events_service_keys}

| Action                               | Description                |
|--------------------------------------|----------------------------|
| `logdna.service-key.create`          | This event is generated when an administrator creates a service key through the LogDNA web UI. |
| `logdna.service-key.delete`          | This event is generated when an administrator deletes a service key through the LogDNA web UI. |
{: caption="Table 1. Events for service keys actions" caption-side="top"} 


### Exclusion rules
{: #at_events_exclusion_rules}

| Action                              | Description                |
|-------------------------------------|----------------------------|
| `logdna.exclusion-rule.create`      | This event is generated when an administrator creates an exclusion rule through the LogDNA web UI. |
| `logdna.exclusion-rule.update`      | This event is generated when an administrator updates an exclusion rule through the LogDNA web UI. |
| `logdna.exclusion-rule.delete`      | This event is generated when an administrator deletes an exclusion rule through the LogDNA web UI. |
{: caption="Table 1. Events for exclusion rules actions" caption-side="top"} 


### Parsing templates
{: #at_events_parsing}

| Action                                | Description                |
|---------------------------------------|----------------------------|
| `logdna.parsing-template.turn-on`     | This event is generated when an administrator enables parsing templates for a LogDNA instance. |
| `logdna.parsing-template.turn-off`    | This event is generated when an administrator disables parsing templates for a LogDNA instance. |
| `logdna.parsing-template.create`      | This event is generated when an administrator creates a parsing template through the LogDNA web UI. |
| `logdna.parsing-template.update`      | This event is generated when an administrator updates a parsing template through the LogDNA web UI. |
| `logdna.parsing-template.delete`      | This event is generated when an administrator deletes a parsing template through the LogDNA web UI. |
{: caption="Table 1. Events for parsing templates actions" caption-side="top"} 


### User metadata 
{: #at_events_user_metadata}

| Action                              | Description                |
|-------------------------------------|----------------------------|
| `logdna.user-metadata.import`      | This event is generated when an administrator imports user-metadata through the LogDNA web UI. |
| `logdna.user-metadata.export`      | This event is generated when an administrator exports user-metadata through the LogDNA web UI. |
{: caption="Table 1. Events for user-metadata related actions" caption-side="top"} 


### Export
{: #at_events_mgt_export}

MISSING
{: important}

| Action                        | Description                |
|-------------------------------|----------------------------|
| `logdna.export.turn-on`       | This event is generated when an administrator enables exporting data for a LogDNA instance. |
| `logdna.export.turn-off`      | This event is generated when an administrator disables exporting data for a LogDNA instance. |
{: caption="Table 1. Events for export actions" caption-side="top"} 


### Extract fields
{: #at_events_mgt_extract}

MISSING
{: important}

| Action                              | Description                |
|-------------------------------------|----------------------------|
| `logdna.extract-data.turn-on`       | This event is generated when an administrator enables extracting of data by using the extract fields feature for a LogDNA instance. |
| `logdna.extract-data.turn-off`      | This event is generated when an administrator disables extracting of data by using the extract fields feature for a LogDNA instance. |
{: caption="Table 1. Events for extracting of data actions" caption-side="top"} 


### Data usage and control
{: #at_events_mgt_usage}

MISSING
{: important}

| Action                         | Description                |
|--------------------------------|----------------------------|
| `logdna.data.turn-on`          | This event is generated when an administrator enables incoming data for a LogDNA instance. |
| `logdna.data.turn-off`         | This event is generated when an administrator disables incoming data for a LogDNA instance. |
| `logdna.usage-alert.configure` | This event is generated when an administrator configures or updates the usage-alert for a LogDNA instance. |
| `logdna.usage-alert-recipient.add` | This event is generated when an administrator adds a recipient to the usage-alert for a LogDNA instance. |
| `logdna.usage-alert-recipient.remove` | This event is generated when an administrator removes a recipient from the usage-alert for a LogDNA instance. |
| `logdna.usage-alert-notification.send` | This event is generated when an alert is sent to the recipients. |
{: caption="Table 1. Events for data related actions" caption-side="top"} 

Suspend all incoming data


## Data events
{: #at_events_data}


### Search
{: #at_events_data_search}

MISSING
{: important}

| Action                              | Description                |
|-------------------------------------|----------------------------|
| `logdna.data.search`                | This event is generated when a search query is run. |
{: caption="Table 1. Events for exporting data" caption-side="top"} 


### Views
{: #at_events_data_views}

| Action                    | Description                |
|---------------------------|----------------------------|
| `logdna.view.create`      | This event is generated when a view is created. |
| `logdna.view.update`      | This event is generated when a view is updated. |
| `logdna.view.delete`      | This event is generated when a view is deleted. |
{: caption="Table 1. Events for views" caption-side="top"} 

### Alerts
{: #at_events_data_alerts}

| Action                     | Description                |
|----------------------------|----------------------------|
| `logdna.alert.create`      | This event is generated when an alert is created. |
| `logdna.alert.update`      | This event is generated when an alert is updated. |
| `logdna.alert.delete`      | This event is generated when an alert is deleted. |
{: caption="Table 1. Events for alerts" caption-side="top"} 

INCLUDES PRESETS -> BUT NEED TO VERIFY ONCE EVENTS ARE AVAILABLE
{: important}

### Dashboards
{: #at_events_data_boards}

| Action                        | Description                |
|-------------------------------|----------------------------|
| `logdna.board.create`         | This event is generated when a dashboard is created. |
| `logdna.board.delete`         | This event is generated when a dashboard is deleted. |
| `logdna.board-graph.create`   | This event is generated when a graph is added to a dashboard. |
| `logdna.board-graph.delete`   | This event is generated when a graph is deleted from a dashboard. |
{: caption="Table 1. Events for dashboards" caption-side="top"} 


### Screens
{: #at_events_data_screens}

| Action                     | Description                |
|----------------------------|----------------------------|
| `logdna.screen.create`      | This event is generated when a screen is created. |
| `logdna.screen.update`      | This event is generated when a screen is updated. |
| `logdna.screen.delete`      | This event is generated when a screen is deleted. |
{: caption="Table 1. Events for alerts" caption-side="top"} 



### Export
{: #at_events_data_export}

| Action                              | Description                |
|-------------------------------------|----------------------------|
| `logdna.data.export`                | This event is generated when an administrator imports user-metadata through the LogDNA web UI. |
{: caption="Table 1. Events for exporting data" caption-side="top"} 




## Viewing events
{: #at_events_ui}

Events that are generated by an instance of the {{site.data.keyword.la_full_notm}} service are automatically forwarded to the {{site.data.keyword.at_full_notm}} service instance that is available in the same location. For more information, see [Cloud services locations](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-cloud_services_locations).

{{site.data.keyword.at_full_notm}} can have only one instance per location. To view events, you must access the web UI of the {{site.data.keyword.at_full_notm}} service in the same location where your service instance is available. For more information, see [Launching the web UI through the IBM Cloud UI](/docs/Activity-Tracker-with-LogDNA?topic=Activity-Tracker-with-LogDNA-launch).




## Analyzing events
{: #at_events_analyze}



