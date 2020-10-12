---

copyright:
  years:  2018, 2020
lastupdated: "2020-10-12"

keywords: LogDNA, IBM, Log Analysis, logging, services

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
{:external: target="_blank" .external}


# Cloud services message ID prefixes
{: #cloud_services_msg_prefix}

List of prefixes that [{{site.data.keyword.cloud}} services](/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-cloud_services) use when they send logs to {{site.data.keyword.la_full_notm}}:
{:shortdesc}


## Message format
{: #cloud_services_msg_format}

A message ID is made up of the following parts:

```
<crn-service-name>.####<severity> 
```
{: codeblock}

* The CRN service-name value.
* 4 digit numeric code.
* Severity code I, E, W for the type of message: informational, error, or warning.



## VPC infrastructure
{: #vpc_infrastructure_msg_prefix}

There are 2 types of VPC infrastructure that you can provision in your account:
* [Virtual Private Cloud classic Gen 1](/docs/vpc-on-classic?topic=vpc-on-classic-getting-started)
* [{{site.data.keyword.vpc_full}} Gen 2](/docs/vpc?topic=vpc-getting-started)

The following tables lists message ID prefixes for the different VPC infrastructure services that send logs to {{site.data.keyword.la_full_notm}}:

## VPC infrastructure Gen 2
{: #vpc_infrastructure_gen2}

| Service     | CRN service name </br>`crn-service-name`  | Message ID format      | Sample |
|-------------|-------------------------------------------|---------------------------|------------------|
| [Dedicated host]()  | `is.dedicated-host`            | `<crn-service-name>.####<severity>` | `flow-log-collector.0001` |
| [Flow Logs for VPC](/docs/vpc?topic=vpc-flow-logs)  | `is.flow-log-collector`       | `<crn-service-name>.####<severity>` | `is.dedicated-host.0001` |
{: caption="Table 9. List of VPC infrastructure services (generation 1)" caption-side="top"} 




