---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords: IBM, Log Analysis, logging, control usage

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring the usage alert
{: #control_usage_alert}


In {{site.data.keyword.la_full}}, you can define an alert to notify when the data usage in the instance reaches the data usage threshold that you set for the instance.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

## Prereqs
{: #control_usage_alert_prereqs}

You must have the service role **manager** to configure data threshold alerts.


## Configure an alert
{: #control_usage_alert_config}

Complete the following steps to configure an alert that informs you when you reach a specific data volume in the instance:

1. [Launch the {{site.data.keyword.la_full_notm}} web UI](/docs/services/log-analysis?topic=log-analysis-launch).

2. Select the **Settings** icon ![Configuration icon](images/admin.png "Admin icon"). Then select **Usage**.

    In the **Dashboard** section, you can see your data usage.

3. Define a **Usage Alert** to set the **Usage Limit** threshold for data usage in the instance. When the usage reaches the percentage of the threshold you selected, the email recipient will be notified.

    ![Panel to define usage alert](images/control-usage-instance-1.png "Panel to define usage alert")

4. In the **Add recipient** section, enter one or more emails where the notification will be sent.

    ![Panel to define usage alert recipients](images/control-usage-instance-2.png "Panel to define usage alert recipients")
