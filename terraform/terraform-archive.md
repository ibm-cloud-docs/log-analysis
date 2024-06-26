---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, terraform

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}



# Configuring archiving by using Terraform
{: #terraform-archive}

You can use the **LogDNA Terraform provider** to manage the archiving configuration of a {{site.data.keyword.la_full_notm}} instance by using HashiCorp Configuration Language (HCL).
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

## Prereqs
{: #terraform-archive-prereqs}

- You must have a paid service plan for the {{site.data.keyword.la_full_notm}} service. [Learn more](/docs/log-analysis?topic=log-analysis-service_plans).
- Ensure that you have the [required access](/docs/log-analysis?topic=log-analysis-iam) to create and work with {{site.data.keyword.la_short}} resources.
- [Install the Terraform CLI](/docs/log-analysis?topic=log-analysis-terraform-setup#terraform-install-cli).
- [Check the {{site.data.keyword.cloud_notm}} Provider plug-in for Terraform supported versions](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-setup_cli).

    - [Create or delete an IBM Cloud Object Storage bucket](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cos_bucket){: external} by using Terraform.

    - [Provision a {{site.data.keyword.la_short}} instance](/docs/log-analysis?topic=log-analysis-terraform-setup) by using Terraform.

- Get the service key that you must use to validate your credentials with the logging instance.

    - For more information on how to get a service key by using the API, see [Service keys by using the API](/docs/log-analysis?topic=log-analysis-service_keys#service_keys_api).

    - For more information on how to use terraform to manage resource keys and get a service key, see [ibm_resource_key](https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/resource_key){: external}.



## Step 1. Set up the LogDNA Provider plug-in
{: #terraform-archive-step1}

Complete the following steps to set up the LogDNA Provider plug-in for Terraform so that you can start managing resources:

1. Create a `versions.tf` file and specify the LogDNA Provider plug-in version that you want to use with the `version` parameter.

    ```terraform
    terraform {
        required_providers {
            logdna = {
                source = "logdna/logdna"
                version = "1.7.0"
              }
        }
    }
    ```
    {: codeblock}

    To see the latest LogDNA provider version, see [LogDNA provider versions](https://registry.terraform.io/providers/logdna/logdna/latest){: external}.
    {: note}

2. Store the `versions.tf` file in your Git repository or the folder where Terraform is set up.




## Step 2. Configure the LogDNA Provider plug-in
{: #terraform-archive-step2}

Before you can start working with Terraform, you must retrieve the credentials and parameters that are required for a Terraform resource or data source, and specify them in the `provider` configuration. This configuration is used by the LogDNA Provider plug-in to authenticate with the service that runs in the {{site.data.keyword.cloud_notm}} platform and to view, create, update, or delete resources.

The following table lists input parameters that you can set in the `provider` block of your Terraform on your Terraform configuration file:

|Input parameter | Required / optional  | Description           |
|----------------|----------------------|-----------------------|
| `servicekey`   | Required             | API key that you must use to validate your credentials with the logging instance. |
| `url`          | Required            | API endpoint. For more information, see [API Endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_api). |
{: caption="Table 1. List of input parameters that you can set in the provider block of your Terraform" caption-side="top"}

For more information on how to use environment variables, see [Using environment variables](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-provider-reference#env-vars).

You can [add multiple provider configurations within the same Terraform on the {{site.data.keyword.cloud_notm}} configuration file](/docs/ibm-cloud-provider-for-terraform?topic=ibm-cloud-provider-for-terraform-provider-reference#multiple-providers) to create your {{site.data.keyword.cloud_notm}} resources with different provider parameters. For example, you can multiple providers so that you can use different input parameters, such as different regions, zones, infrastructure generations, or accounts to create the {{site.data.keyword.cloud_notm}} resources in your Terraform on {{site.data.keyword.cloud_notm}} configuration file. For more information, see [Multiple Provider Instances](https://www.terraform.io/docs/language/providers/configuration.html){: external}.


### Option 1. Creating a static `provider.tf` file
{: #terraform-archive-step2-1}

You can declare the input parameters in the `provider` block directly.

Because the `provider` block includes sensitive information, do not commit this file into a public source repository. To add version control to your provider configuration, use a local [`terraform.tfvars` file](#tf-variables).
{: important}

Create a `provider.tf` file and specify the input parameters that are required for your resource or data source.

```terraform
provider "logdna" {
    servicekey = "<service_key>"
    url = "<API_ENDPOINT>"
}
```
{: codeblock}

Where


### Option 2. Referencing credentials from a Terraform tfvars file
{: #terraform-archive-step2-2}

You can store sensitive information, such as credentials, in a local `terraform.tfvars` file and reference these credentials in your `provider` block.

Do not commit the `terraform.tfvars` into a public source repository. This file is meant to be stored in your local machine only.
{: important}


1. Create a `terraform.tfvars` file on your local machine and add the input parameters that are required for your resource or data source.

    ```terraform
    servicekey = "<Service Key>"
    url = "<API_ENDPOINT>"
    ```
    {: codeblock}

2. Create a `provider.tf` file and use Terraform interpolation syntax to reference the variables from the `terraform.tfvars`.

    ```terraform
    variable "servicekey" {}
    variable "url" {}

    provider "logdna" {
      servicekey = var.servicekey
      url = var.url
    }
    ```
    {: codeblock}


## Step 3. Initialize the Terraform CLI.
{: #terraform-archive-step3}

Next, initialize the Terraform CLI. Run the following command:

```terraform
./terraform init
```
{: pre}

You should see the following message: `Terraform has been successfully initialized!`.



## Step 4. Create a Terraform configuration file
{: #terraform-archive-step4}

Next, create a Terraform configuration file that is named `main.tf`. In this file, you add the configuration to create an archiving configuration by using HashiCorp Configuration Language (HCL). For more information, see the [Terraform documentation](https://www.terraform.io/docs/language/index.html){: external}.

The following code shows a sample configuration file to archive data to a {{site.data.keyword.cos_full_notm}} (COS).

```terraform
resource "logdna_archive" "config" {
  integration = "ibm"
  ibm_config {
    bucket = "<BUCKET_NAME>"
    endpoint = "<COS_BUCKET_PRIVATE_ENDPOINT>"
    apikey = "<API_KEY>"
    resourceinstanceid = "<COS_BUCKET_CRN>"
  }
}
```
{: codeblock}

Where

| Field       | Value                                                |
|-------------|------------------------------------------------------|
| Bucket      | Set to the COS bucket name.                          |
| Endpoint    | Set to the COS bucket private endpoint.              |
| API Key     | Set to the API key associated to the COS service ID. |
| Instance ID | Set to the COS instance ID.                          |
{: caption="Table 1. COS fields" caption-side="top"}


## Step 5. Configure archiving
{: #terraform-archive-step5}

Complete the following steps:

1. Initialize the Terraform CLI.

    ```terraform
    ./terraform init
    ```
    {: pre}

2. Create a Terraform execution plan. The Terraform execution plan summarizes all the actions that need to be run to create the {{site.data.keyword.la_short}} instance, the resource Key, and IAM access policy in your account.

    ```terraform
    ./terraform plan
    ```
    {: pre}

3. Create the resources.

    ```terraform
    ./terraform apply
    ```
    {: pre}

Next, you can:
- [Monitor archiving with {{site.data.keyword.at_short}}](/docs/log-analysis?topic=log-analysis-archiving-la-monitor).
- [Monitoring archiving by using {{site.data.keyword.mon_full_notm}}](/docs/log-analysis?topic=log-analysis-archiving-monitor).



## Removing the archiving configuration
{: #terraform-archive-remove}

To remove the archiving configuratoon, complete the following steps from the directory where you have the terraform script that you use to configure archiving:

1. Initialize the Terraform CLI.

    ```terraform
    ./terraform init
    ```
    {: pre}

2. Create a Terraform execution plan. The Terraform execution plan summarizes all the actions that need to be run to create the {{site.data.keyword.la_short}} instance, the resource Key, and IAM access policy in your account.

    ```terraform
    ./terraform plan
    ```
    {: pre}

3. Delete the configuration.

    ```terraform
    ./terraform destroy
    ```
    {: pre}
