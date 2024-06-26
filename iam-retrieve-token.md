---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}



# Retrieving IAM access tokens
{: #iam-retrieve-token}

To use the {{site.data.keyword.la_short}} target API, you must use an {{site.data.keyword.iamlong}} (IAM) access token. Each token is valid only for one hour, and after a token expires, you must request a new one if you want to continue using the API.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}


## Retrieving an access token for the current session by using the {{site.data.keyword.cloud_notm}} CLI
{: #iam-retrieve-token-cli}
{: cli}

You can use the [{{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-getting-started) to generate your IAM access token.

Complete the following steps to generate an access token for the current session:

1. Log in to {{site.data.keyword.cloud_notm}} with the [{{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-getting-started).

    ```sh
    ibmcloud login
    ```
    {: pre}

    If the login fails, run the `ibmcloud login --sso` command to try again. The `--sso` parameter is required when you log in with a federated ID. If this option is used, go to the link listed in the CLI output to generate a one-time passcode.
    {: note}

2. Run the following command to retrieve your Cloud IAM access token.

    ```sh
    ibmcloud iam oauth-tokens | grep IAM | cut -d \: -f 2 | sed 's/^ *//'
    ```
    {: codeblock}

    The following truncated example shows a retrieved IAM token.

    ```sh
    IAM token:  Bearer eyJraWQiOiIyM...
    ```
    {: screen}

## Retrieving an access token by using an API key and the {{site.data.keyword.cloud_notm}} CLI
{: #iam-retrieve-token-cli-apikey}
{: cli}

You can also retrieve your access token programmatically by creating a [service ID API key](/docs/iam?topic=iam-serviceidapikeys) for your application, and then exchanging your API key for an {{site.data.keyword.cloud_notm}} IAM token.

1. Log in to {{site.data.keyword.cloud_notm}} with the [{{site.data.keyword.cloud_notm}} CLI](/docs/cli?topic=cli-getting-started).

    ```sh
    ibmcloud login -a cloud.ibm.com [--apikey KEY | @KEY_FILE]
    ```
    {: pre}

    Where `KEY | @KEY_FILE` is the API key that you want to use to get the access token.

2. Run the following command to get an IAM access token.

    ```sh
    ibmcloud iam oauth-tokens | grep IAM | cut -d \: -f 2 | sed 's/^ *//'
    ```
    {: codeblock}

    The following truncated example shows a retrieved IAM token.

    ```sh
    IAM token:  Bearer eyJraWQiOiIyM...
    ```
    {: screen}


## Retrieving an access token by using an API key in a cURL request
{: #iam-retrieve-token-api-curl}
{: api}

Run the following cURL command to call the [IAM Identity Services API](/apidocs/iam-identity-token-api) to retrieve your access token:

```text
curl -X POST \
    'https://iam.cloud.ibm.com/identity/token' \
    -H 'content-type: application/x-www-form-urlencoded' \
    -H 'accept: application/json' \
    -d 'grant_type=urn%3Aibm%3Aparams%3Aoauth%3Agrant-type%3Aapikey&apikey=<API_KEY>' > token.json
```
{: codeblock}

Replace `<API_KEY>` with your API key.

The following truncated example shows the contents of the `token.json` file:

```json
{
    "access_token": "b3VyIGZhdGhlc...",
    "expiration": 1512161390,
    "expires_in": 3600,
    "refresh_token": "dGhpcyBjb250a...",
    "token_type": "Bearer"
}
```
{: screen}


Use the full `access_token` value, prefixed by the _Bearer_ token type.
{: note}
