---

copyright:
  years:  2018, 2019
lastupdated: "2019-11-15"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

subcollection: LogDNA

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


# Adoption guidelines for regulated and highly available workloads
{: #adoption}

In {{site.data.keyword.la_full_notm}}, you can define custom data parsing templates 
{:shortdesc}




| `Guidelines`                                |  `HIPAA`           | `PCI`        |  `Business Continuity`  | `Disaster Recovery`              |
|---------------------------------------------|----------------------------------------------------|
| Configure IAM permissions                   | 
| Archive data                                | 
| Setup absence alerts                        |
| 
{: caption="Table 1. Regulated and highly available workloads adoption guidelines summary" caption-side="top"}



![Checkmark icon](../../icons/checkmark-icon.svg)

HIPAA (Health Insurance Portability and Accountability Act of 1996) is United States legislation that provides data privacy and security provisions for safeguarding medical information.

Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organizations that handle branded credit cards from the major card schemes. The PCI Standard is mandated by the card brands and administered by the Payment Card Industry Security Standards Council.  controls surrounding the storing, transmission and processing of card holder’s details, so that their data is protected.


## Control access 
{: #adoption_iam}

Configure IAM to control access to the data and administritation of the data


## Control where data goes


## Control what you log



## Notify in the event of an exception  
{: #adoption_alerts}

HIPAA
PCI

Setup absence alerting

Follow these steps:
Setup alert
Configure it for absence alerting

bsence alerting tests for the absence of data flowing into your service instance.  If data is not flowing into the system it may indicate an issue in the application or environment.  Absence duration is unique to workload and can be customized within the UI.


## Prepare a proper Object Storage location

HIPAA
PCI
Business Continuity
Disaster Recovery

Review and identify the right COS configuration for your business needs.  Set this up to prepare for service archive.


LogDNA can archive to a client configured COS bucket.  There are many COS configurations helping clients meet a variety of needs.  Data may need to be replicated across Regions to meet business and regulated requirements.  Alternatively data may need to be restricted to certain locations to meet data locality requirements.  Learn more about COS configurations here.



## Setup archive

HIPAA
PCI
Business Continuity
Disaster Recovy

Follow these steps.

Archive, when sent to the properly configured COS account may provide your application or environment the necessary backup of data.  


LogDNA as a service does not store an independent backup copy of your data. 


When LogDNA is setup to archive to IBM COS, setup archive to a COS bucket which does not have preconfigured retention policies.

