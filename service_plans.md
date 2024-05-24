---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, service plan

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Service plans
{: #service_plans}

Different pricing plans are available that you can choose for an {{site.data.keyword.la_full_notm}} instance. Each plan defines the number of days that data is retained for search, the number of users allowed to manage the data, and the logging features that are enabled.
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

| Plan                            | Number of days that data is available for search | Number of users per plan | Plan Name | Plan ID |
|---------------------------------|-------------------------------------------------|--------------------------|---------|--------|
| `HIPAA 30 day log search`       | 30                                              | 25     | `hipaa-30-day` | a9b3eb07-5096-448b-ba34-53711d74742b |
| `30 days log search`            | 30                                              | Unlimited  | `30-day`   | deda35aa-662b-4b06-9f6e-05e0b55cc577 |
| `14 days log search`            | 14                                              | Unlimited   | `14-day`  | 0b3a45e0-def0-4935-8c74-26976f281751 |
| `7-day log search`              | 7                                               | Unlimited   | `7-day`   | 209cbd52-f3e2-47cb-94ce-6b84fafcf22b|
| `Lite`                          | Data is not available for search                | 1           | `lite`  | abcf7f02-de22-4c7f-98a1-e8a592093d83 |
{: caption="Table 1. List of service plans" caption-side="top"}

{{site.data.keyword.la_full_notm}} offers a `Lite` plan that you can use to view your logs as they pass through the system. You can view logs by using log tailing. You can also design filters to prepare for upgrading to a longer retention period plan. You cannot use an instance on the `Lite` plan to receive streamed data. This plan has a 0-day retention period.


## Features by plan
{: #svcplan_features}

The following tables outline the different features that are included in each service plan:

| Feature                                              | `HIPAA 30 day log search` plan | `30 day log search` plan | `14 days log search` plan    | `7 days log search` plan     | `Lite` plan |
|------------------------------------------------------|-------------------------|-------------------------------|-----------------------------|--------------|--------|
| `Live streaming tail`                                | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg)|
| `Customizing the logging agent`                      | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg)|
| `Logs are stored and searchable`                    | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Archiving of logs`                                 | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Multi-channel Alerting`                            | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Exporting logs`                                    | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Definig custom parsing templates`                  | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Configuring exclusion rules from the logging web UI` | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Creating views`                      | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Creating dashboards`                      | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Creating screens`                      | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
| `Analyzing logs in different contexts`              | ![Checkmark icon](images/checkmark-icon.svg)| ![Checkmark icon](images/checkmark-icon.svg) | ![Checkmark icon](images/checkmark-icon.svg) |![Checkmark icon](images/checkmark-icon.svg) | |
{: caption="Table 2. List of features available for each service plan" caption-side="top"}



## Logging features that are not available with {{site.data.keyword.la_full_notm}} service plans
{: #svcplan_exc_features}

The following logging features are not available:
* Sharing a line
