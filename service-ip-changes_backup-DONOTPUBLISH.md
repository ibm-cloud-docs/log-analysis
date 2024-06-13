---

copyright:
  years:  2018, 2023
lastupdated: "2022-12-08"

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

## 8 December 2022 changes
{: #endpoint-changes-08Dec2022}

The following changes were made:

### Dallas (us-south)
{: #120822_ussouth}

| Dallas IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `logs.private.us-south.logging.cloud.ibm.com` | 166.9.14.3  \n 166.9.12.13  \n 166.9.16.12  | 166.9.90.101  \n 166.9.61.86  \n 166.9.86.91 |
| `syslog-tls://syslog-a.us-south.logging.cloud.ibm.com` | 52.117.134.203 | 52.117.134.206  \n 52.116.247.170  \n 67.228.102.117 |
{: caption="Table 1. IP changes in US-SOUTH" caption-side="top"}

### Frankfurt (eu-de)
{: #120822_eude}

| Frankfurt IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.private.eu-de.logging.cloud.ibm.com` | 166.9.32.7  \n 166.9.28.2 | 166.9.32.7  \n 166.9.30.231 (NEW)  \n 166.9.28.2 |
| `logs.private.eu-de.logging.cloud.ibm.com` | 166.9.28.3  \n 166.9.32.21 | 166.9.32.21  \n 166.9.28.3  \n 166.9.30.238 (NEW) |
| `syslog-a.private.eu-de.logging.cloud.ibm.com` | 166.9.32.23  \n 166.9.28.5 | 166.9.30.236 (NEW)  \n 166.9.28.5  \n 166.9.32.23 |
| `syslog://syslog-u.private.eu-de.logging.cloud.ibm.com` | 166.9.28.7  \n 166.9.32.24 | 166.9.32.24  \n 166.9.28.7  \n 166.9.30.239 (NEW) |
| `syslog-tls://syslog-a.private.eu-de.logging.cloud.ibm.com` | 166.9.28.5  \n 166.9.32.23 | 166.9.30.236 (NEW)  \n 166.9.32.23  \n 166.9.28.5 |
{: caption="Table 2. IP changes in EU-DE" caption-side="top"}

### Sao Paulo (br-sao)
{: #120822_brsao}

| Sao Paulo IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.private.br-sao.logging.cloud.ibm.com` | 163.107.67.3  \n 163.107.68.196  \n 163.109.68.98 | 166.9.82.23  \n 166.9.83.24  \n 166.9.84.25 |
{: caption="Table 3. IP changes in BR-SAO" caption-side="top"}

### Seoul (kr-seo)
{: #120822_krseo}

| Seoul IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.kr-seo.logging.cloud.ibm.com` | 169.56.165.158 | Deprecated |
| `api.private.kr-seo.logging.cloud.ibm.com` | 166.9.46.5 | Deprecated
| `logs.kr-seo.logging.cloud.ibm.com` | 169.56.98.142 | Deprecated |
| `logs.private.kr-seo.logging.cloud.ibm.com` | 166.9.46.6 | Deprecated |
| `syslog://syslog-a.kr-seo.logging.cloud.ibm.com` | 169.56.98.139 | Deprecated |
| `syslog-a.private.kr-seo.logging.cloud.ibm.com` | 166.9.46.8 | Deprecated |
| `syslog://syslog-u.kr-seo.logging.cloud.ibm.com` | 169.56.98.141 | Deprecated |
| `syslog://syslog-u.private.kr-seo.logging.cloud.ibm.com` | 166.9.44.103  \n 166.9.42.123  \n 166.9.40.114 | Deprecated |
| `syslog-tls://syslog-a.kr-seo.logging.cloud.ibm.com` | 169.56.98.139 | Deprecated |
| `syslog-tls://syslog-a.private.kr-seo.logging.cloud.ibm.com` | 166.9.40.113  \n 166.9.42.122  \n 166.9.44.112 | Deprecated |
{: caption="Table 4. IP changes in KR-SEO" caption-side="top"}

### Sydney (au-syd)
{: #120822_ausyd}

| Sydney IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.private.au-syd.logging.cloud.ibm.com` | 166.9.56.3  \n 166.9.52.2 | 166.9.52.2  \n 166.9.54.128 (NEW)  \n 166.9.56.3 |
| `logs.private.au-syd.logging.cloud.ibm.com` | 166.9.52.5  \n 166.9.56.20  | 166.9.54.127 (NEW)  \n 166.9.52.5  \n 166.9.56.20 |
| `syslog-a.private.au-syd.logging.cloud.ibm.com` | 166.9.52.8  \n 166.9.56.22 | 166.9.54.124 (NEW)  \n 166.9.52.8  \n 166.9.56.22 |
| `syslog://syslog-u.private.au-syd.logging.cloud.ibm.com` | 166.9.56.23  \n 166.9.52.9 | 166.9.52.9  \n 166.9.54.115 (NEW)  \n 166.9.56.23 |
| `syslog-tls://syslog-a.private.au-syd.logging.cloud.ibm.com` | 166.9.38.20  \n 166.9.34.18  \n 166.9.36.5 | 166.9.52.8  \n 166.9.56.22  \n 166.9.54.124 |
{: caption="Table 5. IP changes in AU-SYD" caption-side="top"}

### Tokyo (jp-tok)
{: #120822_jptok}

| Tokyo IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.private.jp-tok.logging.cloud.ibm.com` | 166.9.40.2  \n 166.9.42.3 | 166.9.42.3  \n 166.9.40.2  \n 166.9.44.13 (NEW) |
| `logs.private.jp-tok.logging.cloud.ibm.com` | 166.9.40.3  \n 166.9.42.4  | 166.9.42.4  \n  166.9.44.71 (NEW)  \n 166.9.40.3 |
| `syslog://syslog-a.jp-tok.logging.cloud.ibm.com` | 169.56.11.251  \n 165.192.100.77  \n 128.168.107.245 | 165.192.100.77  \n 128.168.95.2  \n 161.202.248.162 |
| `syslog-a.private.jp-tok.logging.cloud.ibm.com` | 166.9.42.26  \n 166.9.40.23 | 166.9.44.67 (NEW)  \n 166.9.40.23  \n 166.9.42.26 |
| `syslog://syslog-u.private.jp-tok.logging.cloud.ibm.com` | 166.9.42.27  \n 166.9.40.24 | 166.9.40.24  \n 166.9.44.73 (NEW)  \n 166.9.42.27 |
| `syslog-tls://syslog-a.jp-tok.logging.cloud.ibm.com` | 128.168.107.245  \n 165.192.100.77  \n 169.56.11.251 | 128.168.95.2  \n 161.202.248.162  \n 165.192.100.77 |
| `syslog-tls://syslog-a.private.jp-tok.logging.cloud.ibm.com` | 166.9.40.23  \n 166.9.42.26 | 166.9.40.23  \n 166.9.42.26  \n 166.9.44.67 (NEW) |
{: caption="Table 6. IP changes in JP-TOK" caption-side="top"}

### Toronto (ca-tor)
{: #120822_cator}

| Toronto IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.private.ca-tor.logging.cloud.ibm.com` | 169.53.161.75  \n 163.74.65.133  \n 163.75.73.42 | 166.9.76.26  \n 166.9.77.23  \n 166.9.78.24 |
| `logs.private.ca-tor.logging.cloud.ibm.com` | 166.9.77.26  \n 166.9.76.29 | 166.9.77.26  \n  166.9.76.29  \n 166.9.78.27 (NEW) |
{: caption="Table 7. IP changes in CA-TOR" caption-side="top"}

### Washington (us-east)
{: #120822_useast}

| Washington IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.private.us-east.logging.cloud.ibm.com` | 166.9.22.35  \n 166.9.20.72 | 166.9.24.247 (NEW)  \n 166.9.22.35  \n 166.9.20.72 |
| `logs.private.us-east.logging.cloud.ibm.com` | 166.9.22.36  \n 166.9.20.73 | 166.9.20.73  \n 166.9.22.36  \n 166.9.24.245 (NEW) |
| `syslog-a.private.us-east.logging.cloud.ibm.com` | 166.9.22.38  \n 166.9.20.76 | 166.9.22.38  \n 166.9.20.76  \n 166.9.24.243 (NEW) |
| `syslog://syslog-u.private.us-east.logging.cloud.ibm.com` | 166.9.22.39  \n 166.9.20.77 | 166.9.20.77  \n 166.9.22.39  \n 166.9.24.244 (NEW) |
| `syslog-tls://syslog-a.private.us-east.logging.cloud.ibm.com` | 166.9.22.38  \n 166.9.20.76 | 166.9.22.38  \n 166.9.24.243 (NEW)  \n 166.9.20.76 |
{: caption="Table 8. IP changes in US-EAST" caption-side="top"}


## 9 May 2022 changes
{: #endpoint-changes-09May2022}

The following changes were made:

### Chenai (in-che)
{: #042122_inche}

| Chenai IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.in-che.logging.cloud.ibm.com` | 169.38.94.138 | 169.38.94.141 |
| `syslog-a.private.in-che.logging.cloud.ibm.com` | NEW | 166.9.60.9 |
{: caption="Table 9. IP changes in IN-CHE" caption-side="top"}

### Dallas (us-south)
{: #042122_ussouth}

| Dallas IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.us-south.logging.cloud.ibm.com` | 169.61.197.85  \n 67.228.211.4  \n 50.22.153.156 | 52.117.134.204  \n 50.22.151.6  \n 67.228.208.253 |
| `syslog-a.private.us-south.logging.cloud.ibm.com` | NEW | 166.9.14.5  \n 166.9.12.15  \n 166.9.16.14 |
{: caption="Table 10. IP changes in US-SOUTH" caption-side="top"}

### Frankfurt (eu-de)
{: #042122_eude}

| Frankfurt IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.eu-de.logging.cloud.ibm.com` | 149.81.108.27  \n 161.156.6.180  \n 158.177.157.69 | 158.177.133.235  \n 161.156.28.220  \n 149.81.169.206 |
| `syslog-a.private.eu-de.logging.cloud.ibm.com` | NEW | 166.9.32.23  \n 166.9.28.5 |
{: caption="Table 11. IP changes in EU-DE" caption-side="top"}

### London (eu-gb)
{: #042122_eugb}

| London IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.eu-gb.logging.cloud.ibm.com` | 158.175.66.211  \n 158.176.163.114  \n 141.125.102.147 | 158.175.91.91  \n 141.125.86.131  \n 158.176.142.2 |
| `syslog-a.private.eu-gb.logging.cloud.ibm.com` | NEW | 166.9.38.20  \n 166.9.34.18  \n 166.9.36.5 |
{: caption="Table 12. IP changes in EU-GB" caption-side="top"}

### Osaka (jp-osa)
{: #042122_jposa}

| Osaka IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.jp-osa.logging.cloud.ibm.com` | 163.73.65.202  \n 163.68.73.59  \n 163.69.68.68 | 163.68.75.68  \n 163.69.70.155  \n 163.73.70.118 |
| `syslog-a.private.jp-osa.logging.cloud.ibm.com` | NEW | 166.9.70.22  \n 166.9.71.22  \n 166.9.72.22 |
{: caption="Table 13. IP changes in JP-OSA" caption-side="top"}

### Sao Paulo (br-sao)
{: #042122_brsao}

| Sao Paulo IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.br-sao.logging.cloud.ibm.com` | 163.109.68.102  \n 163.107.69.11  \n 169.57.254.115 | 163.107.67.3  \n 163.107.68.196  \n 163.109.68.98 |
| `api.private.br-sao.logging.cloud.ibm.com` | 166.9.82.23  \n 166.9.83.24  \n 166.9.84.25 | 163.107.67.3  \n 163.107.68.196  \n 163.109.68.98 |
| `syslog-a.private.br-sao.logging.cloud.ibm.com` | 169.57.254.118  \n 163.107.68.195  \n 163.109.68.109 | 166.9.82.26  \n 166.9.83.22  \n 166.9.84.23 |
{: caption="Table 14. IP changes in BR-SAO" caption-side="top"}

### Seoul (kr-seo)
{: #042122_krseo}

| Seoul IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.kr-seo.logging.cloud.ibm.com` | 169.56.98.138 | 169.56.165.158 |
| `syslog-a.private.kr-seo.logging.cloud.ibm.com` | NEW | 166.9.46.8	|
{: caption="Table 15. IP changes in KR-SEO" caption-side="top"}

### Sydney (au-syd)
{: #042122_ausyd}

| Sydney IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.au-syd.logging.cloud.ibm.com` | 130.198.71.147  \n 135.90.92.250  \n 168.1.27.61 | 135.90.92.246  \n 130.198.1.212  \n 135.90.89.221 |
| `syslog-a.private.au-syd.logging.cloud.ibm.com` | NEW | 166.9.52.8  \n 166.9.56.22 |
{: caption="Table 16. IP changes in AU-SYD" caption-side="top"}

### Tokyo (jp-tok)
{: #042122_jptok}

| Tokyo IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.jp-tok.logging.cloud.ibm.com` | 128.168.96.180  \n 165.192.111.35  \n 169.56.11.254 | 161.202.231.186  \n 128.168.96.179  \n 165.192.111.36 |
| `api.private.jp-tok.logging.cloud.ibm.com` | 166.9.40.2 | 166.9.40.2  \n 166.9.42.3 |
| `syslog://syslog-a.jp-tok.logging.cloud.ibm.com` | 128.168.95.2  \n 161.202.248.162  \n 165.192.100.77 | 169.56.11.251  \n 165.192.100.77  \n 128.168.107.245 |
| `syslog-a.private.jp-tok.logging.cloud.ibm.com` | NEW | 166.9.42.26  \n 166.9.40.23 |
{: caption="Table 17. IP changes in JP-TOK" caption-side="top"}

### Toronto (ca-tor)
{: #042122_cator}

| Toronto IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.ca-tor.logging.cloud.ibm.com` | 163.75.66.246  \n 163.74.65.134  \n 169.53.186.156 | 169.53.161.75  \n 163.74.65.133  \n 163.75.73.42 |
| `api.private.ca-tor.logging.cloud.ibm.com` | 166.9.77.23  \n 166.9.78.24  \n 166.9.76.26 | 169.53.161.75  \n 163.74.65.133  \n 163.75.73.42 |
| `syslog-a.private.ca-tor.logging.cloud.ibm.com` | NEW | 166.9.76.31  \n 166.9.77.28  \n 166.9.78.29 |
{: caption="Table 18. IP changes in CA-TOR" caption-side="top"}

### Washington (us-east)
{: #042122_useast}

| Washington IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `api.us-east.logging.cloud.ibm.com` | 169.47.134.82  \n 169.60.121.245  \n 52.117.105.38 | 169.47.134.86  \n 169.60.72.62  \n 169.61.107.10 |
| `api.private.us-east.logging.cloud.ibm.com` | 166.9.22.35  \n 166.9.20.72 | 166.9.22.35  \n 166.9.20.72 |
| `syslog-a.private.us-east.logging.cloud.ibm.com` | NEW | 166.9.22.38  \n 166.9.20.76 |
{: caption="Table 19. IP changes in US-EAST" caption-side="top"}


## 3 February 2022 changes
{: #service-ip-changes-03feb2022}

The following changes were made:

### Tokyo (jp-tok)
{: #syslog-ip-changes-tokyo}

| Tokyo IP address                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------| --------------------------------------------------------------|-------------------------------------------|
| `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`                  | 169.56.11.251  \n 165.192.100.77  \n 128.168.107.245       | 128.168.95.2  \n 161.202.248.162  \n 165.192.100.77 |
{: caption="Table 20. IP changes in JP-TOK" caption-side="top"}

## 28 May 2021 changes
{: #service-ip-changes-28May2021}

The following changes were made:

### London (eu-gb)
{: #service-ip-changes-london}

| London IP addresses                                     | Original IP addresses                                      | New IP addresses |
|----------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.eu-gb.logging.cloud.ibm.com`                 | 158.175.125.165  \n 158.176.135.133  \n 141.125.78.186  | 158.176.163.117  \n 158.175.113.18  \n 141.125.102.149 |
| `logs.private.eu-gb.logging.cloud.ibm.com`         | 166.9.36.3  \n 166.9.34.4  \n 166.9.38.5                | No change |
| `syslog-a.eu-gb.logging.cloud.ibm.com`             | 158.175.113.22  \n 158.176.163.115  \n 141.125.102.148  | No change |
| `api.eu-gb.logging.cloud.ibm.com`                  | 158.176.135.132  \n 158.175.82.238  \n 141.125.78.213   | 158.175.113.20  \n 158.176.163.154  \n 141.125.140.100 |
| `api.private.eu-gb.logging.cloud.ibm.com`          | 166.9.36.2  \n 166.9.38.4  \n 166.9.34.2                | No change |
{: caption="Table 21. IP changes in EU-GB" caption-side="top"}

### Dallas (us-south)
{: #service-ip-changes-dallas}

| Dallas IP addresses                                     | Original IP addresses                                      | New IP addresses  |
|-------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.us-south.logging.cloud.ibm.com`                 | 169.48.237.107  \n 169.60.166.45  \n 169.47.224.77      | 169.61.197.84  \n 50.22.153.155  \n 67.228.211.6 |
| `logs.private.us-south.logging.cloud.ibm.com`         | 166.9.14.3  \n 166.9.12.13  \n 166.9.16.12              | No change |
| `syslog-a.us-south.logging.cloud.ibm.com`             | 169.47.102.26  \n 169.62.255.114  \n 169.47.227.242     | 169.60.203.92  \n 50.22.153.157  \n 67.228.211.2 |
| `api.us-south.logging.cloud.ibm.com`                  | 169.47.224.74  \n 169.60.166.44  \n 169.48.237.109      | 169.61.197.85  \n 50.22.153.156  \n 67.228.211.4 |
| `api.private.us-south.logging.cloud.ibm.com`          | 166.9.16.11  \n 166.9.12.12  \n 166.9.14.2              | No change |
{: caption="Table 22. IP changes in US-South" caption-side="top"}

### Frankfurt (eu-de)
{: #service-ip-changes-frankfurt}

| Frankfurt IP addresses                                 | Original IP addresses                                      | New IP addresses  |
|----------------------------------------------------|-----------------------------------------------------------|-------------------------------------------|
| `logs.eu-de.logging.cloud.ibm.com`                 | 161.156.89.11  \n 149.81.86.68  \n 158.177.129.36       | 158.177.157.66  \n 161.156.78.142  \n 149.81.108.173 |
| `logs.private.eu-de.logging.cloud.ibm.com`         | 166.9.28.3  \n 166.9.32.21                               | No change |
| `syslog-a.eu-de.logging.cloud.ibm.com`             | 158.177.136.58  \n 149.81.96.229  \n 161.156.75.98      | 158.177.157.70  \n 161.156.78.138  \n 149.81.108.28 |
| `api.eu-de.logging.cloud.ibm.com`                  | 149.81.86.66  \n 161.156.89.12  \n 158.177.129.34       | 158.177.157.69  \n 161.156.6.180  \n 149.81.108.27 |
| `api.private.eu-de.logging.cloud.ibm.com`          | 166.9.32.7  \n 166.9.28.2                                | No change |
{: caption="Table 23. IP changes in EU-DE" caption-side="top"}

## User-required tasks
{: #service-ip-changes-tasks}

If you are using public endpoints, you must complete the following tasks:

### Reconfigure your firewalls to the new IPs
{: #service-ip-changes-tasks-1}

If you have firewalls set up on the public or private network in your {{site.data.keyword.cloud_notm}} infrastructure account, you need to allow traffic to and from the {{site.data.keyword.la_full_notm}} service. You must allow traffic on TCP port 443 and TCP port 80 in your firewall for the API endpoints and the ingestion endpoints. Check that valid IPs are configured per region where you operate. For a list of valid IPs, see [IP changes by region](/docs/log-analysis?topic=log-analysis-service-ip-changes#service-ip-changes-ips).

### Reconfigure applications and services
{: #service-ip-changes-tasks-2}

If you have applications and services that restrict connectivity to specific IPs and communicate with the {{site.data.keyword.la_short}} service, make sure the new IPs are configured to avoid interruption of the logging service.
