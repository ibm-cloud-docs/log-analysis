---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Agent storage requirements
{: #agent_storage}

If the agent is unable to send logs to the {{site.data.keyword.la_full_notm}} service, the logs are buffered.  For example, buffered in local storage on the Kubernetes node. When the agent is able to send logs again, the buffered logs are sent. The most recent logs are sent first.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

To avoid losing logs when logs are buffered, make sure you have enough local storage to buffer logs for the desired length of time. 24 hours is recommended for critical logs.

To determine how much local storage you might need, use the {{site.data.keyword.la_full_notm}} dashboard to determine your usage or use the [Usage API](/apidocs/log-analysis#get-usage-host). To see your usage per day using the {{site.data.keyword.la_full_notm}} dashboard, access  your {{site.data.keyword.la_full_notm}} instance and click **Usage** > **Dashboard**.

Local storage should be the amount of storage required for logging per day plus an additional 20% contingency.
