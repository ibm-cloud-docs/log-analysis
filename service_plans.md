---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-02"

keywords: LogDNA, IBM, Log Analysis, logging, service plan

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

# Service plans
{: #service_plans}

Different pricing plans are available that you can choose for an {{site.data.keyword.la_full_notm}} instance. Each plan defines the number of days that data is retained for search, the number of users allowed to manage the data, and the LogDNA features that are enabled.
{:shortdesc}



| Plan                            | Number of days that data is available for seach | Number of users per plan | Plan ID |
|---------------------------------|-------------------------------------------------|--------------------------|---------|
| `HIPAA 30 day log search` [1]   | 30                                              | 25                       | a9b3eb07-5096-448b-ba34-53711d74742b |
| `30 days log search`            | 30                                              | Unlimited                | deda35aa-662b-4b06-9f6e-05e0b55cc577 |
| `14 days log search`            | 14                                              | Unlimited                | 0b3a45e0-def0-4935-8c74-26976f281751 |
| `7-day log search`              | 7                                               | Unlimited                | 209cbd52-f3e2-47cb-94ce-6b84fafcf22b|
| `Lite`                          | Data is not available for search                | 1                        | abcf7f02-de22-4c7f-98a1-e8a592093d83 |
{: caption="Table 1. List of service plans" caption-side="top"} 

`[1]` To enable the HIPAA plan in your account, you must [open a support ticket](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support). 

{{site.data.keyword.la_full_notm}} offers a `Lite` plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. This plan has a 0-day retention period.


## Features by plan
{: #svcplan_features}

The following tables outline the different features that are included in each service plan:

| Feature                                              | `HIPAA 30 day log search` plan | `30 day log search` plan | `14 days log search` plan    | `7 days log search` plan     | `Lite` plan | 
|------------------------------------------------------|-------------------------|-------------------------------|-----------------------------|--------------|
| `Live streaming tail`                                | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg)|
| `Customizing the LogDNA agent`                      | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg)|
| `Logs are stored and searchable`                    | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Archiving of logs`                                 | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Multi-channel Alerting`                            | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Exporting logs`                                    | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Definig custom parsing templates`                  | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Configuring exclusion rules from the LogDNA web UI` | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Creating views`                      | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Creating dashboards`                      | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Creating screens`                      | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
| `Analyzing logs in different contexts`              | ![Checkmark icon](images/checkmark.svg)  | ![Checkmark icon](images/checkmark.svg) | ![Checkmark icon](images/checkmark.svg) |![Checkmark icon](images/checkmark.svg) | |
{: caption="Table 2. List of features available for each service plan" caption-side="top"} 



## LogDNA features that are not available with {{site.data.keyword.la_full_notm}} service plans
{: #svcplan_exc_features}

The following LogDNA features are not available:
* Embedding views and registering domains
* Sharing a line 
* Role Based Access Control (RBAC)
* LogDNA Command Line Interface (CLI)




