---

copyright:
  years:  2018, 2020
lastupdated: "2020-12-04"

keywords: IBM, Log Analysis, logging, terraform

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

# Using Terraform
{: #using-terraform}

You can manage {{site.data.keyword.la_full} views and alerts and automate their deployment programmatically using Terrform commands. {{site.data.keyword.la_full} has a [Terraform provider](https://registry.terraform.io/providers/logdna/logdna/latest){: external} that uses the [Configuration API](https://docs.logdna.com/reference#getting-started-with-the-configuration-api){: external}.
{: shortdesc}

In addition to [managing {{site.data.keyword.cloud_notm}} resources(/docs/terraform?topic=terraform-manage_resources), you can use the Terraform provider to manage {{site.data.keyword.la_full} related items.  For example:

* You can deploy multiple identically defined alerts and views in several {{site.data.keyword.cloud_notm}} regions.

* You can create a set of views or alerts based on a template to a single or different accounts.

* You can create a workflow where changes to views or alerts must be reviewed so alerting isn't disrupted and changes can be rolled-back if necessary. 

Terraform scripts are written in [HCL (Hashicorp Configuration Language)](https://www.terraform.io/docs/configuration/syntax.html){: external}.

## Example

====== ADD AN IBM SPECIFIC EXAMPLE OF USING TERRAFORM HERE ======

## Considerations when using Terraform

If you manage your {{site.data.keyword.la_full} environment using both Terraform and the web UI, you need to consider the following:

* If you create a new view using Terraform and then delete the view using the web UI, Terraform will not know that the view is deleted and an `Error: Resource Not Found` message will be returned when Terraform tries to manage the view.

* Running the `terraform plan` and `terraform apply` commands will not display all possible changes if Terraform is not aware of all existing {{site.data.keyword.la_full} resources.


