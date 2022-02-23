---

copyright:
  years:  2018, 2022
lastupdated: "2022-02-22"

keywords: IBM, Log Analysis, logging, endpoints

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Service IP changes
{: #service-ip-changes}

Due to maintenance, {{site.data.keyword.la_full}} makes changes periodically to service IPs in some regions. You might need to take action to continue using the service.
{: shortdesc}

Endpoints and regions that are not listed are unchanged.
{: note}

If you are using private endpoints, there are no user-required tasks. Private endpoints have not changed.
{: important}

## 3 February 2022 changes
{: #service-ip-changes-03feb2022}

The following changes were made:

### Tokyo (jp-tok)
{: #syslog-ip-changes-tokyo}

| Tokyo IP address                                 | Original IP addresses                                      | New IP addresses  | 
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`                  | 169.56.11.251  \n 165.192.100.77  \n 128.168.107.245       | 128.168.95.2  \n 161.202.248.162  \n 165.192.100.77 | 
{: caption="Table 1. IP changes in JP-TOK" caption-side="top"}

## 28 May 2021 changes
{: #service-ip-changes-28May2021}

The following changes were made:

### London (eu-gb)
{: #service-ip-changes-london}

| London IP address                                     | Original IP addresses                                      | New IP addresses |
|----------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.eu-gb.logging.cloud.ibm.com`                 | 158.175.125.165  \n 158.176.135.133  \n 141.125.78.186  | 158.176.163.117  \n 158.175.113.18  \n 141.125.102.149 |
| `logs.private.eu-gb.logging.cloud.ibm.com`         | 166.9.36.3  \n 166.9.34.4  \n 166.9.38.5                | No change |
| `syslog-a.eu-gb.logging.cloud.ibm.com`             | 158.175.113.22  \n 158.176.163.115  \n 141.125.102.148  | No change |
| `api.eu-gb.logging.cloud.ibm.com`                  | 158.176.135.132  \n 158.175.82.238  \n 141.125.78.213   | 158.175.113.20  \n 158.176.163.154  \n 141.125.140.100 |
| `api.private.eu-gb.logging.cloud.ibm.com`          | 166.9.36.2  \n 166.9.38.4  \n 166.9.34.2                | No change |
{: caption="Table 2. IP changes in EU-GB" caption-side="top"}

### Dallas (us-south)
{: #service-ip-changes-dallas}

| Dallas IP addresses                                     | Original IP addresses                                      | New IP addresses  |
|-------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.us-south.logging.cloud.ibm.com`                 | 169.48.237.107  \n 169.60.166.45  \n 169.47.224.77      | 169.61.197.84  \n 50.22.153.155  \n 67.228.211.6 |
| `logs.private.us-south.logging.cloud.ibm.com`         | 166.9.14.3  \n 166.9.12.13  \n 166.9.16.12              | No change |
| `syslog-a.us-south.logging.cloud.ibm.com`             | 169.47.102.26  \n 169.62.255.114  \n 169.47.227.242     | 169.60.203.92  \n 50.22.153.157  \n 67.228.211.2 |
| `api.us-south.logging.cloud.ibm.com`                  | 169.47.224.74  \n 169.60.166.44  \n 169.48.237.109      | 169.61.197.85  \n 50.22.153.156  \n 67.228.211.4 |
| `api.private.us-south.logging.cloud.ibm.com`          | 166.9.16.11  \n 166.9.12.12  \n 166.9.14.2              | No change |
{: caption="Table 3. IP changes in US-South" caption-side="top"}

### Frankfurt (eu-de)
{: #service-ip-changes-frankfurt}

| Frankfurt IP addresses                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.eu-de.logging.cloud.ibm.com`                 | 161.156.89.11  \n 149.81.86.68  \n 158.177.129.36       | 158.177.157.66  \n 161.156.78.142  \n 149.81.108.173 |
| `logs.private.eu-de.logging.cloud.ibm.com`         | 166.9.28.3  \n 166.9.32.21                               | No change |
| `syslog-a.eu-de.logging.cloud.ibm.com`             | 158.177.136.58  \n 149.81.96.229  \n 161.156.75.98      | 158.177.157.70  \n 161.156.78.138  \n 149.81.108.28 |
| `api.eu-de.logging.cloud.ibm.com`                  | 149.81.86.66  \n 161.156.89.12  \n 158.177.129.34       | 158.177.157.69  \n 161.156.6.180  \n 149.81.108.27 |
| `api.private.eu-de.logging.cloud.ibm.com`          | 166.9.32.7  \n 166.9.28.2                                | No change |
{: caption="Table 4. IP changes in EU-DE" caption-side="top"}

## User-required tasks
{: #service-ip-changes-tasks}

If you are using public endpoints, you must complete the following tasks:

### Reconfigure your firewalls to the new IPs
{: #service-ip-changes-tasks-1}

If you have firewalls set up on the public or private network in your {{site.data.keyword.cloud_notm}} infrastructure account, you need to allow traffic to and from the {{site.data.keyword.la_full_notm}} service. You must allow traffic on TCP port 443 and TCP port 80 in your firewall for the API endpoints and the ingestion endpoints. Check that valid IPs are configured per region where you operate. For a list of valid IPs, see [IP changes by region](/docs/log-analysis?topic=log-analysis-service-ip-changes#service-ip-changes-ips).

### Reconfigure applications and services
{: #service-ip-changes-tasks-2}

If you have applications and services that restrict connectivity to specific IPs and communicate with the {{site.data.keyword.la_short}} service, make sure the new IPs are configured to avoid interruption of the logging service.




