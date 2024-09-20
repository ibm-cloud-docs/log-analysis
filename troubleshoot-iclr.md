---

copyright:
  years: 2018, 2024
lastupdated: "2024-09-20"

keywords:

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Why can't I find my logs using the queries I've always used?
{: #troubleshoot-iclr}
{: troubleshoot}
{: support}

After logs are routed to {{site.data.keyword.la_full_notm}} using {{site.data.keyword.logs_routing_full_notm}}, queries to search for the logs are no longer finding them.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

The searches you used to use to find your logs are no longer returning the desired results.
{: tsSymptoms}

{{site.data.keyword.logs_routing_full_notm}} configures the host value to a differet value than the service name.
{: tsCauses}

See [Why can't I find logs routed to {{site.data.keyword.la_full_notm}}](/docs/logs-router?topic=logs-router-ts-hostvalue) for required changes to your queries.
{: tsResolve}
