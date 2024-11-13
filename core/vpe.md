---

copyright:
  years: 2022, 2024
lastupdated: "2024-11-13"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Using virtual private endpoints for VPC to privately connect to {{site.data.keyword.la_full_notm}}
{: #vpe-connection}

{{site.data.keyword.cloud}} Virtual Private Endpoints (VPE) for VPC enables you to connect to {{site.data.keyword.la_full_notm}} from your VPC network by using the IP addresses of your choosing, allocated from a subnet within your VPC.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

VPEs are virtual IP interfaces that are bound to an endpoint gateway created on a per service, or service instance, basis (depending on the service operation model). The endpoint gateway is a virtualized function that scales horizontally, is redundant and highly available, and spans all availability zones of your VPC. Endpoint gateways enable communications from virtual server instances within your VPC and {{site.data.keyword.cloud}} service on the private backbone. VPE for VPC gives you the experience of controlling all the private addressing within your cloud. For more information, see [About virtual private endpoint gateways](/docs/vpc?topic=vpc-about-vpe).


## Before you begin
{: #prereq-service-endpoint}

Before you target a virtual private endpoint for {{site.data.keyword.la_full_notm}} you must complete the following tasks.

* Ensure that a [Virtual Private Cloud is created](/docs/vpc?topic=vpc-getting-started).
* Make a plan for your [virtual private endpoints](/docs/vpc?topic=vpc-planning-considerations).
* Ensure that [correct access controls](/docs/vpc?topic=vpc-configure-acls-sgs-endpoint-gateways) are set for your virtual private endpoint.
* Understand the [limitations](/docs/vpc?topic=vpc-limitations-vpe) of having a virtual private endpoint.
* Understand how to [view details](/docs/vpc?topic=vpc-vpe-viewing-details-of-an-endpoint-gateway) about a virtual private endpoint.

Virtual private endpoint settings, specifically the Internet Protocol (IP) address, might need to be manually updated during [Disaster recovery and business continuity actions](/docs/log-analysis?topic=log-analysis-ha-dr). 
{: important}

## Virtual Private Service Endpoints
{: #vpe-endpoints}

The following table lists regions where {{site.data.keyword.la_full_notm}} service supports VPE. 
It also lists {{site.data.keyword.la_full_notm}} endpoints supported from each region. You can 
connect to {{site.data.keyword.la_full_notm}} service in another region using supported endpoints. 
For example, from the Sydney region, you can use {{site.data.keyword.la_full_notm}} service in 
`us-south` region using the us-south endpoint.

When connecting to a VPE via [CLI](/docs/vpc?topic=vpc-ordering-endpoint-gateway#vpe-ordering-cli) 
or [API](/docs/vpc?topic=vpc-ordering-endpoint-gateway#vpe-ordering-api), you will 
need to specify the CRN of the region that you will use to connect to the 
{{site.data.keyword.la_full_notm}} service. Use the table below to locate the CRN 
of the target region.
{: note}

| Region     | Endpoints Supported in Region        | CRN                                                                                |  |
|------------|--------------------------------------|------------------------------------------------------------------------------------|--|
| Dallas (us-south) | api.private.us-south.logging.cloud.ibm.com  \n  \n logs.private.us-south.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:us-south:::endpoint:api.private.us-south.logging.cloud.ibm.com |
| Frankfurt (eu-de) | api.private.eu-de.logging.cloud.ibm.com  \n  \n logs.private.eu-de.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:eu-de:::endpoint:api.private.eu-de.logging.cloud.ibm.com |
| London (eu-gb) | api.private.eu-gb.logging.cloud.ibm.com  \n  \n logs.private.eu-gb.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:eu-gb:::endpoint:api.private.eu-gb.logging.cloud.ibm.com |
| Madrid (eu-es) | api.private.eu-es.logging.cloud.ibm.com  \n  \n logs.private.eu-es.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:eu-es:::endpoint:api.private.eu-es.logging.cloud.ibm.com |
| Osaka (jp-osa) | api.private.jp-osa.logging.cloud.ibm.com  \n  \n logs.private.jp-osa.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:jp-osa:::endpoint:api.private.jp-osa.logging.cloud.ibm.com |
| Sao Paulo (br-sao) | api.private.br-sao.logging.cloud.ibm.com  \n  \n logs.private.br-sao.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:br-sao:::endpoint:api.private.br-sao.logging.cloud.ibm.com |
| Sydney (au-syd) | api.private.au-syd.logging.cloud.ibm.com  \n  \n logs.private.au-syd.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:au-syd:::endpoint:api.private.au-syd.logging.cloud.ibm.com |
| Tokyo (jp-tok) | api.private.jp-tok.logging.cloud.ibm.com  \n  \n logs.private.jp-tok.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:jp-tok:::endpoint:api.private.jp-tok.logging.cloud.ibm.com |
| Toronto (ca-tor) | api.private.ca-tor.logging.cloud.ibm.com  \n  \n logs.private.ca-tor.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:ca-tor:::endpoint:api.private.ca-tor.logging.cloud.ibm.com |
| Washington (us-east) | api.private.us-east.logging.cloud.ibm.com  \n  \n logs.private.us-east.logging.cloud.ibm.com | crn:v1:bluemix:public:logdna:us-east:::endpoint:api.private.us-east.logging.cloud.ibm.com |
{: caption="Lists private endpoints for interacting with {{site.data.keyword.la_full_notm}} APIs over IBM Cloud's private network" caption-side="top"}

## Using Virtual Private Endpoints
{: #using-vpes}

### Before you begin
{: #vpes-before-begin}

- You need to have an [{{site.data.keyword.cloud_notm}} account](https://cloud.ibm.com/registration){: external}
- And a {{site.data.keyword.la_full_notm}} instance. You can [provision](/docs/log-analysis?topic=log-analysis-provision) one from the [{{site.data.keyword.cloud_notm}} catalog](https://cloud.ibm.com/catalog/services/). Give your instance a memorable name that appears in your account's Resource List.

### Setting up your VPE
{: #vpes-setup}

1. Create an {{site.data.keyword.vpc_full}}. Follow the `Getting started` [instructions here](/docs/vpc?topic=vpc-getting-started). 

2. Make sure that your VPC has at least one VSI (virtual server instance), and can connect to the VSI. You can use the UI, CLI, and API to quickly provision {{site.data.keyword.vpc_full}} from the Virtual server instances page in {{site.data.keyword.cloud_notm}} console. For more information, see [Creating virtual server instances](/docs/vpc?topic=vpc-creating-virtual-servers).

3. Make sure your {{site.data.keyword.la_full_notm}} deployment's [private endpoint is enabled](/docs/log-analysis?topic=log-analysis-endpoints).

4. In the {{site.data.keyword.cloud_notm}} console, click the menu icon and select **Infrastructure > VPC Layout > Network > Virtual private endpoint gateways**. Create a VPE for your {{site.data.keyword.la_full_notm}} instances with the [following instruction](/docs/vpc?topic=vpc-about-vpe). 

5. After you create your VPE, it might take a few minutes for the new VPE and pDNS to complete the process and begin working for your VPC. Completion is confirmed when you see an IP address set in the [details view](/docs/vpc?topic=vpc-vpe-viewing-details-of-an-endpoint-gateway) of the VPE. 

6. To make sure pDNS is functioning for your VPE, `ssh` into your VSI and run `nslookup <instance_hostname>`. The following example shows the output from running `nslookup` on instance hostnames of `api.private.us-east.logging.cloud.ibm.com` and `logs.private.us-east.logging.cloud.ibm.com`:

   ```text
   root@test-vpc-vsi:~# nslookup api.private.us-east.logging.cloud.ibm.com
   Server:      161.26.0.7
   Address:     161.26.0.7#53

   Non-authoritative answer:
   Name:   api.private.us-east.logging.cloud.ibm.com
   Address: 10.241.65.4
   ```
   {: codeblock}

   ```text
   root@test-vpc-vsi:~# nslookup logs.private.us-east.logging.cloud.ibm.com
   Server:      161.26.0.7
   Address:     161.26.0.7#53

   Non-authoritative answer:
   Name:   logs.private.us-east.logging.cloud.ibm.com
   Address: 10.241.65.4
   ```
   {: codeblock}

   In these examples `10.241.65.4` is your VPE IP address.

7. You can now use your instance in the VSI. 

### VPE Discoverability
{: #vpes-discoverability}

Following the previous steps results in a {{site.data.keyword.la_full_notm}} instance with private endpoints that is reachable with the Virtual Private Endpoints from your VPC network.

For more information, see [Setting up private service endpoints for {{site.data.keyword.la_full_notm}}](/docs/log-analysis?topic=log-analysis-service-connection#endpoint-setup).
{: .tip}

### More resources
{: #vpes-resources}

- [Planning for virtual private endpoint gateways](/docs/vpc?topic=vpc-planning-considerations)
- [Creating an endpoint gateway](/docs/vpc?topic=vpc-ordering-endpoint-gateway)
- For further assistance, see the [FAQs for virtual private endpoints here](/docs/vpc?topic=vpc-faqs-vpe), and the `Troubleshooting VPE gateways` documentation that includes [how to fix communications issues here](/docs/vpc?topic=vpc-troubleshoot-cannot-communicate). 
