---

copyright:
  years:  2018, 2021
lastupdated: "2021-05-28"

keywords: IBM, Log Analysis, logging, endpoints

subcollection: log-analysis

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

# Service IP changes
{: #service-ip-changes}

Due to maintenance, {{site.data.keyword.la_full}} is making changes to service IPs in some regions. You may need to take action to continue using the service.
{:shortdesc}

If you are using private endpoints, there are no user-required tasks. Private endpoints are not changing.
{: important}

## IP changes by region
{: #service-ip-changes-ips}

IPs in the following regions remain the same: Chennai, US-East, Osaka, Seoul, Sydney, and Tokyo.
{: note}


The following tables show changes per region:

### London (eu-gb)
{: #service-ip-changes-london}

| London endpoint                                    | Current IP addresses                                      | New IP addresses |
|----------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.eu-gb.logging.cloud.ibm.com`                 | 158.175.125.165 </br>158.176.135.133 </br>141.125.78.186  | 158.176.163.117 </br>158.175.113.18 </br>141.125.102.149 |
| `logs.private.eu-gb.logging.cloud.ibm.com`         | 166.9.36.3 </br>166.9.34.4 </br>166.9.38.5                | No change |
| `syslog-a.eu-gb.logging.cloud.ibm.com`             | 158.175.113.22 </br>158.176.163.115 </br>141.125.102.148  | No change |
| `api.eu-gb.logging.cloud.ibm.com`                  | 158.176.135.132 </br>158.175.82.238 </br>141.125.78.213   | 158.175.113.20 </br>158.176.163.154 </br>141.125.140.100 |
| `api.private.eu-gb.logging.cloud.ibm.com`          | 166.9.36.2 </br>166.9.38.4 </br>166.9.34.2                | No change |
{: caption="Table 1. Lists of IPs in EU-GB" caption-side="top"}

### Dallas (us-south)
{: #service-ip-changes-dallas}

| US South endpoint                                     | Current IP addresses                                      | New IP addresses  |
|-------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.us-south.logging.cloud.ibm.com`                 | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77      | 169.61.197.84 </br>50.22.153.155 </br>67.228.211.6 |
| `logs.private.us-south.logging.cloud.ibm.com`         | 166.9.14.3 </br>166.9.12.13 </br>166.9.16.12              | No change |
| `syslog-a.us-south.logging.cloud.ibm.com`             | 169.47.102.26 </br>169.62.255.114 </br>169.47.227.242     | 169.60.203.92 </br>50.22.153.157 </br>67.228.211.2 |
| `api.us-south.logging.cloud.ibm.com`                  | 169.47.224.74 </br>169.60.166.44 </br>169.48.237.109      | 169.61.197.85 </br>50.22.153.156 </br>67.228.211.4 |
| `api.private.us-south.logging.cloud.ibm.com`          | 166.9.16.11 </br>166.9.12.12 </br>166.9.14.2              | No change |
{: caption="Table 2. Lists of IPs in US South" caption-side="top"}




### Frankfurt (eu-de)
{: #service-ip-changes-frankfurt}

| Frankfurt endpoint                                 | Current IP addresses                                      | New IP addresses  |
|----------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.eu-de.logging.cloud.ibm.com`                 | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36       | 158.177.157.66 </br>161.156.78.142 </br>149.81.108.173 |
| `logs.private.eu-de.logging.cloud.ibm.com`         | 166.9.28.3 </br>166.9.32.21                               | No change |
| `syslog-a.eu-de.logging.cloud.ibm.com`             | 158.177.136.58 </br>149.81.96.229 </br>161.156.75.98      | 158.177.157.70 </br>161.156.78.138 </br>149.81.108.28 |
| `api.eu-de.logging.cloud.ibm.com`                  | 149.81.86.66 </br>161.156.89.12 </br>158.177.129.34       | 158.177.157.69 </br>161.156.6.180 </br>149.81.108.27 |
| `api.private.eu-de.logging.cloud.ibm.com`          | 166.9.32.7 </br>166.9.28.2                                | No change |
{: caption="Table 3. Lists of IPs in EU-DE" caption-side="top"}



## User-required tasks
{: #service-ip-changes-tasks}

If you are using public endpoints, you must complete the following tasks:

### Reconfigure your firewalls to the new IPs
{: #service-ip-changes-tasks-1}

If you have firewalls set up on the public or private network in your {{site.data.keyword.cloud_notm}} infrastructure account, you need to allow traffic to and from the {{site.data.keyword.la_full_notm}} service. You must allow traffic on TCP port 443 and TCP port 80 in your firewall for the API endpoints and the ingestion endpoints. Check that valid IPs are configured per region where you operate. For a list of valid IPs, see [IP changes by region](/docs/log-analysis?topic=log-analysis-service-ip-changes#service-ip-changes-ips).

### Reconfigure applications and services
{: #service-ip-changes-tasks-2}

If you have applications and services that restrict connectivity to specific IPs and communicate with the {{site.data.keyword.la_short}} service, make sure the new IPs are configured to avoid interruption of the logging service.




