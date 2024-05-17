---

copyright:
  years: 2018, 2024
lastupdated: "2024-05-17"

keywords: IBM, Log Analysis, logging, security, connection

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}


# Securing your connection
{: #service-connection}

To ensure that you have enhanced control and security over your data when you use {{site.data.keyword.la_full}}, you have the option that use private routes to {{site.data.keyword.cloud_notm}} service endpoints. Private routes are not accessible or reachable over the internet. By using the {{site.data.keyword.cloud_notm}} Private service endpoints feature, you can protect your data from threats from the public network and logically extend your private network.
{: shortdesc}

<!-- common deprecation notice -->
{{../_include-segments/deprecation_notice.md}}

## Before you begin
{: #prereq-service-endpoint}

Consider the following factors when you must decide which network to choose:
* Corporate requirements on how services and applications can access cloud-based services in your account.
* Security on production workloads.
* Industry compliance regulations.

For example, you might have the following requirements when you are working in the {{site.data.keyword.cloud_notm}}:
* No access to Internet to connect to {{site.data.keyword.cloud_notm}} services.
* Isolated connectivity for workloads in your account.

When you have these requirements, consider moving from the public network to the private network.

You can configure a logging agent to connect to an {{site.data.keyword.la_full_notm}} instance through the public network or through the private network. By default, the agent connects through the public network.
{: note}

The type of network defines the level of isolation and security that is configured to move workloads between cloud-based resources in your account. Consider connecting the logging agent over the private network.
{: tip}


## Setting up private service endpoints for {{site.data.keyword.la_full_notm}}
{: #endpoint-setup}

Private network endpoints support routing services over the {{site.data.keyword.cloud_notm}} Private network instead of the public network.

* A private network endpoint provides a unique IP address that is accessible to you without a VPN connection.
* Private endpoints work between regions offering a global network. You can run your applications and services in Dallas, and connect to a logging instance in Sydney with a private endpoint.



### Step 1. Enabling your account
{: #endpoint-setup-step1}

To use private network endpoints, the following account features must be enabled for your account:
* Virtual routing and forwarding (VRF)
* Service endpoints

    Enabling service endpoints means that all users in the account can connect to private network endpoints.
    {: note}

You must first enable virtual routing and forwarding in your account, and then you can enable the use of IBM Cloud private service endpoints.
* To enable VRF, you create a support case.
* To enable service endpoints, you use the {{site.data.keyword.cloud_notm}} CLI. For more information about how to enable your account, see [Enabling VRF and service endpoints](/docs/account?topic=account-vrf-service-endpoint).


### Step 2. Setting a private endpoint
{: #endpoint-setup-step2}

After your account is enabled for VRF and service endpoints, you can configure a logging agent to connect to an {{site.data.keyword.la_full_notm}} instance through the private network.

A service instance can have a private network endpoint, a public network endpoint, or both.
* A public network endpoint is a service endpoint on the {{site.data.keyword.cloud_notm}} public network.
* A private network endpoint is a service endpoint that is accessible only on the {{site.data.keyword.cloud_notm}} Private network.

The {{site.data.keyword.la_full_notm}} service offers [private API endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api_private).


### Step 3. Configure your logging agent
{: #endpoint-setup-step3}

You can [configure the logging agent](/docs/log-analysis?topic=log-analysis-logdna_agent) to use the private network by using a private endpoint as the ingestion URL.

What happens when you configure the logging agent to use a private endpoint?
* Private endpoints are not accessible from the public internet.
* All traffic is routed to the {{site.data.keyword.cloud_notm}} Private network.
* Services like {{site.data.keyword.la_full_notm}} are no longer served on an internet routable IP address.



## Limitations that use private endpoints
{: #network_endpoints_limitations}

The logging web UI is not supported on the private network.
