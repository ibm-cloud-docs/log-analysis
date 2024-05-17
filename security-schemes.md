---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-17"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Security schemes for authentication
{: #security-schemes}

The {{site.data.keyword.la_full_notm}} API supports the following security schemes:
{: shortdesc}

<!-- common deprecation notice -->
{{_include-segments/deprecation_notice.md}}

## Service API key authorization
{: #security-schemes-1}

You can use a service key in the header.

This key is used for all APIs with the exception of ingest.

You can obtain a service key by following [these instructions](https://cloud.ibm.com/docs/log-analysis?topic=log-analysis-service_keys) and placing the key in the header of your call.

For example, see a sample call:

```
curl GET https://api.<region>.logging.cloud.ibm.com/v1/config/categories/views \
  -H 'content-type: application/json' \
  -H 'servicekey: <SERVICE_KEY>' \
```
{: codeblock}

## Ingestion API key authorization
{: #security-scheme-2}

You can use an ingestion key in the header.


You can obtain the ingestion key by following [these instructions](https://cloud.ibm.com/docs/log-analysis?topic=log-analysis-ingestion_key) and placing the key in the header of your call.

For example, see a sample call:

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" \
  -H 'content-type: application/json' \
  -H 'ingestionkey: <INGESTION_KEY>' \
  -d "LOG_LINES"
```
{: codeblock}


## IAM token authorization
{: #security-scheme-3}

This scheme is an alternative to authenticating with a service key in IBM environments.
{: note}

You can use a bearer `access_token` that you obtain from the [IAM Identity Services API](https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey).

The token that you get has an expiration time.
{: important}

This token must also be sent with the `cloud-resource-name` header to identify which account you are accessing. To get the CRN, see [Retrieving your instance ID and cloud resource name (CRN)](https://cloud.ibm.com/docs/key-protect?topic=key-protect-retrieve-instance-ID)

For example, a sample cURL looks like:

```text
curl https://api.<region>.logging.cloud.ibm.com/v1/config/view --header 'Authorization: Bearer [IAM_ACCESS_TOKEN]' --header 'cloud-resource-name: [IBM_INSTANCE_CRN]'
```
{: codeblock}

To get the access token, you can run the following:

```
curl -X POST https://iam.cloud.ibm.com/identity/token -H "content-type: application/x-www-form-urlencoded" -H "accept: application/json" -d "grant_type=urn%3Aibm%3Aparams%3Aoauth%3Agrant-type%3Aapikey&apikey=<APIKEY>"
```
{: codeblock}

## Basic authentication
{: #security-scheme-4}

As an alternative to authenticating with a header value, you can also use basic authentication.

You can use either an `apiKey` or a `servicekey` as basic authentication. Simply pass the key as the username with no password.

For example, see the following sample when using a service key:

```
curl https://api.<region>.logging.cloud.ibm.com/v1/config/view -u SERVICE_KEY:
```
{: codeblock}

For example, see the following sample when using an ingestion key:

```
curl "ENDPOINT/logs/ingest?QUERY_PARAMETERS" -u INGESTION_KEY: --header "Content-Type: application/json; charset=UTF-8" -d "LOG_LINES"
```
{: codeblock}
