---

copyright:
  years:  2018, 2023
lastupdated: "2023-09-26"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Protecting {{site.data.keyword.la_full_notm}} resources with context-based restrictions
{: #cbr}

Context-based restrictions give account owners and administrators the ability to define and enforce access restrictions for {{site.data.keyword.cloud}} resources based on the context of access requests. Access to {{site.data.keyword.la_full_notm}} resources can be controlled with context-based restrictions and identity and access management (IAM) policies.
{: shortdesc}

These restrictions work with traditional IAM policies, which are based on identity, to provide an extra layer of protection. Unlike IAM policies, context-based restrictions don't assign access. Context-based restrictions check that an access request comes from an allowed context that you configure. Since both IAM access and context-based restrictions enforce access, context-based restrictions offer protection even in the face of compromised or mismanaged credentials. For more information, see [What are context-based restrictions](/docs/account?topic=account-context-restrictions-whatis).

A user must have the Administrator role on the {{site.data.keyword.la_full_notm}} service to create, update, or delete rules. A user must also have either the Editor or Administrator role on the Context-based restrictions service to create, update, or delete network zones. A user with the Viewer role on the Context-based restrictions service can only add network zones to a rule.
{: note}

Any {{site.data.keyword.cloudaccesstraillong_notm}} or audit log events generated come from the context-based restrictions service, not {{site.data.keyword.la_full_notm}}. For more information, see [Monitoring context-based restrictions](/docs/account?topic=account-cbr-monitor).

To get started protecting your {{site.data.keyword.la_full_notm}} resources with context-based restrictions, see the tutorial for [Leveraging context-based restrictions to secure your resources](/docs/account?topic=account-context-restrictions-tutorial).

<!-- Most services can include only the content above this comment. If your service has limitations, stipulations as to how rules and network zones are enforced, or other use cases specific to your service, then review the following section to include additional information. -->

## How {{site.data.keyword.la_full_notm}} integrates with context-based restrictions
{: #cbr-overview}

You can use context-based restrictions when [configuring archving to {{site.data.keyword.cos_full_notm}}](/docs/log-analysis?topic=log-analysis-archiving) and [streaming to {{site.data.keyword.messagehub}}.](/docs/log-analysis?topic=log-analysis-streaming-configure)

By using context-based restrictions you restrict {{site.data.keyword.cos_full_notm}} or {{site.data.keyword.messagehub}} to receive data only from {{site.data.keyword.la_full_notm}} without specifically configuring a service ID to access the service.

Additional services and IP addresses can be configured in rules to send data to {{site.data.keyword.cos_full_notm}} or {{site.data.keyword.messagehub}} in addition to {{site.data.keyword.la_full_notm}}.
{: note}

## Restrictions
{: #cbr-restrictions}

Consider the following when configuring context-based restrictions:

* Any zones and rules configured for {{site.data.keyword.at_full_notm}} will also apply to {{site.data.keyword.la_full_notm}}. Any zones and rules configured for {{site.data.keyword.la_full_notm}} will also apply to {{site.data.keyword.at_full_notm}}.

* {{site.data.keyword.messagehub}} credentials created for {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} can be shared by {{site.data.keyword.la_full_notm}} and {{site.data.keyword.at_full_notm}} instances, but can not be shared with any other services.

## Creating network zones
{: #network-zone}

A network zone represents an allowlist of IP addresses where an access request is created. It defines a set of one or more network locations that are specified by the following attributes:

* IP addresses, which include individual addresses, ranges, or subnets.
* VPCs
* Service references, which allow access from other {{site.data.keyword.cloud_notm}} services.

Make sure to add {{site.data.keyword.la_full_notm}} to network zones for rules that target other {{site.data.keyword.cloud_notm}} resources, or some operations in your workflow might fail.
{: important}

### Service references
{: #service-references}

The `IBM Log Analysis` IAM service needs to be added to network zones as a service reference.


### Creating network zones in the console
{: #network-zone-ui}
{: ui}

1. In the {{site.data.keyword.cloud_notm}} console click **Manage** >  **Context-based restrictions**.

2. Click **Network zones**.

3. Click **Create**.

4. Enter a name for your network zone and an optional description.

5. Enter the allowed and denied IP addresses associated with the network zone.

6. Select the VPCs allowed by the network zone.

7. For **Service type** select `IAM services`.

8. For **Service** select `IBM Log Analysis`.

9. Click **Add**.


### Creating network zones by using the API
{: #network-zone-api}
{: api}

You can create network zones by using the `POST` method. For more information, see the [API docs](/apidocs/context-based-restrictions#create-zone). You can add {{site.data.keyword.la_full_notm}} to network zones as a service reference to allow {{site.data.keyword.la_full_notm}} to access resources and services in your account that are the subject of a rule.

The `serviceRef` attribute for {{site.data.keyword.la_full_notm}} is `logdna`.
{: tip}

For example, create a zone for {{site.data.keyword.la_full_notm}}:

```text
curl -X POST --location --header "Authorization: Bearer {iam_token}" --header "Accept: application/json" --header "Content-Type: application/json" --data '{ "name": "MY_LOG_ANALYSIS_ZONE", "description": "This is my Log Analysis zone", "account_id": "{account_id}", "addresses": [  { "type": "serviceRef", "ref": { "account_id": "{account_id}", "service_name": "logdna" } } ] }' "https://cbr.cloud.ibm.com/v1/zones"
```
{: codeblock}

You can use `PUT` and `DELETE` to update and delete zones. You can use `GET` to list all defined zones or get additional information for a single zone. For more information about these methods, see the [API docs](/apidocs/context-based-restrictions).

### Creating network zones by using the CLI
{: #network-zone-cli}
{: cli}

You can use the `cbr-zone-create` command to add network locations, VPCs, and service references to network zones. For more information, see the CBR [CLI reference](/docs/account?topic=account-cbr-plugin#cbr-zones-cli). Add {{site.data.keyword.la_full_notm}} to network zones as a service reference to allow {{site.data.keyword.la_full_notm}} to access resources and services in your account that are the subject of a rule.

To find a list of available service refs, run the `ibmcloud cbr service-ref-targets` [command](/docs/account?topic=account-cbr-plugin#cbr-cli-service-ref-targets-command). The `service-ref service_name` for {{site.data.keyword.la_full_notm}} is `logdna`.
{: tip}

For example, create a zone for {{site.data.keyword.la_full_notm}}:

```text
ibmcloud cbr zone-create --name MY_LOG_ANALYSIS_ZONE --description "This is my Log Analysis zone" --service-ref service_name=logdna
```
{: codeblock}

You can use `zone-update` and `zone-delete` to update and delete zones. You can use `ibmcloud cbr zones` to list all defined zones. For more information about these commands, see the CBR [CLI reference](/docs/account?topic=account-cbr-plugin#cbr-zones-cli).


## Creating rules
{: #create-rules}

Define restrictions to {{site.data.keyword.la_full_notm}} resources by creating rules.

### Creating rules in the console
{: #rules-ui}
{: ui}

1. In the {{site.data.keyword.cloud_notm}} console click **Manage** >  **Context-based restrictions**.

2. Click **Rules**.

3. Click **Create**.

4. For **Service** select one of the following:

   `Cloud Object Storage` if you are configuring a context-based restriction for archiving to a bucket.

   `Event Streams` if you are configuring a context-based restriction for streaming to {{site.data.keyword.messagehub}}.

5. Click **Next**.

6. Select **All resources** or **Specific resources** as appropriate. If you are limiting resources, add the conditions defining the limit.

7. Click **Review**.

8. Click **Continue**.

9. Select if you want to limit access by **endpoint type**.

10. Select the **Network zone** you want associated to the rule. If you don't have a zone created, you can create one by clicking **Create**.

11. Click **Continue**.

12. Add an optional description for the rule.

13. Select how you want the rule enforced:

    **Enabled**: The rule is enforced and denied access attempts are reported in {{site.data.keyword.at_full_notm}}.

    **Disabled**: The rule is not enforced. Restrictions are not applied.

    **Report-only**: Monitors how the rule affects users without enforcing it. All access attempts are reported in {{site.data.keyword.at_full_notm}}. Monitoring for 30 days before enforcing a rule will help you determine if there are any errors in your configuration.

14. Click **Create**.

### Creating rules by using the API
{: #rules-api}
{: api}

Review the following examples to learn how to create rules for {{site.data.keyword.la_full_notm}}. For more information, see the [API docs](/apidocs/context-based-restrictions#create-rule).

Create a rule allowing access between {{site.data.keyword.cos_full_notm}} and the zone defined for {{site.data.keyword.la_full_notm}}:

```text
curl -X POST --location --header "Authorization: Bearer {iam_token}" --header "Accept: application/json" --header "Content-Type: application/json" --data '{ "description": "My rule between Log Analysis and Cloud Object Storage", "resources": [ { "attributes": [ { "name": "accountId", "value": "{account_id}" }, { "name": "serviceName", "value": "cloud-object-storage" } ] } ], "contexts": [ { "attributes": [ { "name": "networkZoneId", "value": "{zone_id}" } ] } ] }' "https://cbr.cloud.ibm.com/v1/rules"

```
{: codeblock}

Where the `zone_id` is the zone configured for {{site.data.keyword.la_full_notm}}.

You can find a list of configured zones by running the `GET /v1/zones` method. To retrieve the zone ID, use the `GET /v1/zones/{zone_id}` method.
{: tip}

The following service names can be used when configuring rules to connect with {{site.data.keyword.la_full_notm}}:

`cloud-object-storage`
:   {{site.data.keyword.cos_full_notm}}

`messagehub`
:    {{site.data.keyword.messagehub}}

Use `enforcement_mode` to determine how the rule is processed. For example, this rule between {{site.data.keyword.messagehub}} and {{site.data.keyword.la_full_notm}} is defined, but is disabled and will not be enforced.

```text
curl -X POST --location --header "Authorization: Bearer {iam_token}" --header "Accept: application/json" --header "Content-Type: application/json" --data '{ "description": "My rule between Log Analysis and Event Streams", "resources": [ { "attributes": [ { "name": "accountId", "value": "{account_id}" }, { "name": "serviceName", "value": "messagehub" } ] } ], "contexts": [ { "attributes": [ { "name": "networkZoneId", "value": "{zone_id}" } ] } ], "enforcement_mode": "disabled" }' "https://cbr.cloud.ibm.com/v1/rules"

```
{: codeblock}

Enforcement modes that can be configured for a rule are:

`Enabled`
:   The rule is enforced and denied access attempts are reported in {{site.data.keyword.at_full_notm}}.

`Disabled`
:   The rule is not enforced. Restrictions are not applied.

`Report`
:    Monitors how the rule affects users without enforcing it. All access attempts are reported in {{site.data.keyword.at_full_notm}}. Monitoring for 30 days before enforcing a rule will help you determine if there are any errors in your configuration.

You can use `PUT` and `DELETE` to update and delete rules. You can use `GET` to list all defined rules or list detailed information about a single rule. For more information about these methods, see the CBR [API docs](/apidocs/context-based-restrictions).



### Creating rules by using the CLI
{: #rules-cli}
{: cli}

Review the following examples to learn how to create rules for {{site.data.keyword.la_full_notm}}. For more information, see the CBR [CLI reference](/docs/account?topic=account-cbr-plugin).

For example, create a rule allowing access between {{site.data.keyword.cos_full_notm}} and the zone defined for {{site.data.keyword.la_full_notm}}:

```text
ibmcloud cbr rule-create --description "My rule between the Log Analysis zone and Cloud Object Storage" --service-name cloud-object-storage --zone-id 445bdf061e5eb36f53188d26760401aa
```
{: codeblock}

Where the `zone-id` is the zone configured for {{site.data.keyword.la_full_notm}}. 

You can find a list of configured zones by running the `ibmcloud cbr zones` command.
{: tip}


The following service names can be used when configuring rules to connect with {{site.data.keyword.la_full_notm}}:

`cloud-object-storage`
:   {{site.data.keyword.cos_full_notm}}

`messagehub`
:    {{site.data.keyword.messagehub}}

You can also limit access between services. For example, limiting access to private endpoints only:

```text
ibmcloud cbr rule-create --description "My rule between Log Analysis and Cloud Object Storage" --service-name cloud-object-storage --zone-id 445bdf061e5eb36f53188d26760401aa --context-attributes endpointType=private
```
{: codeblock}

Using `enforcement-mode` determines how the rule is processed. For example, this rule between {{site.data.keyword.messagehub}} and {{site.data.keyword.la_full_notm}} is defined, but is disabled and will not be enforced.

```text
ibmcloud cbr rule-create --description "My rule between Log Analysis and Event Streams" --service-name messagehub --zone-id 445bdf061e5eb36f53188d26760401aa --enforcement-mode disabled
```
{: codeblock}

Enforcement modes that can be configured for a rule are:

`Enabled`
:   The rule is enforced and denied access attempts are reported in {{site.data.keyword.at_full_notm}}.

`Disabled`
:   The rule is not enforced. Restrictions are not applied.

`Report`
:    Monitors how the rule affects users without enforcing it. All access attempts are reported in {{site.data.keyword.at_full_notm}}. Monitoring for 30 days before enforcing a rule will help you determine if there are any errors in your configuration.

You can use `rule-update` and `rule-delete` to update and delete rules. You can use `ibmcloud cbr rules` to list all defined rules. For more information about these commands, see the CBR [CLI reference](/docs/account?topic=account-cbr-plugin#cbr-zones-cli).
