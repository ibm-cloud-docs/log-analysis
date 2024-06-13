---

copyright:
  years:  2022, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Public endpoint changes (WIP)
{: #endpoint_changes}

{{site.data.keyword.la_full}} public endpoints are being changed.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

Due to maintenance, {{site.data.keyword.la_full}} makes changes periodically to IPs in some regions. You might need to take action to continue using the service. This topic lists the currently supported, and planned to be supported, public endpoints. The new endpoints will be effective **XX MONTH 2022** at which time the existing public endpoints will no longer be available.
{: important}

| Region                 | Ingestion endpoint                          | Existing Public IP addresses                                   | New Public IP addresses |Ports               |
|------------------------|---------------------|------------------------|-------------------------------------------------------|---------------------|
| `Chennai (in-che)`     | `logs.in-che.logging.cloud.ibm.com`         | 169.38.75.46                                          | 169.38.94.141  | TCP 443  \n TCP 80 |
| `Dallas (us-south)`    | `logs.us-south.logging.cloud.ibm.com`       | 169.61.197.84   \n 50.22.153.155  \n 67.228.211.6     | 52.117.134.204  \n 50.22.151.6    \n 67.228.208.253 |  TCP 443  \n TCP 80 |
| `Frankfurt (eu-de)`    | `logs.eu-de.logging.cloud.ibm.com`          | 149.81.108.173  \n 158.177.157.66 \n 161.156.78.142   | 158.177.133.235 \n 161.156.28.220 \n 149.81.169.206 | TCP 443  \n TCP 80 |
| `London (eu-gb)`       | `logs.eu-gb.logging.cloud.ibm.com`          | 158.176.163.117 \n 158.175.113.18 \n 141.125.102.149  | 158.175.91.91   \n 141.125.86.131 \n 158.176.142.2 | TCP 443  \n TCP 80 |
| `Osaka (jp-osa)`       | `logs.jp-osa.logging.cloud.ibm.com`         | 163.73.68.44    \n 163.69.67.212  \n 163.68.73.62     | 163.68.75.68    \n 163.69.70.155  \n 163.73.70.118 | TCP 443  \n TCP 80 |
| `Sao Paulo (br-sao)`   | `logs.br-sao.logging.cloud.ibm.com`         | 163.109.68.108  \n 163.107.69.13  \n 169.57.152.195   | unchanged | TCP 443  \n TCP 80 |
| `Seoul (kr-seo)`       | `logs.kr-seo.logging.cloud.ibm.com`         | 169.56.98.142                                         | unchanged | TCP 443  \n TCP 80 |
| `Sydney (au-syd)`      | `logs.au-syd.logging.cloud.ibm.com`         | 168.1.27.60     \n 130.198.1.213  \n 135.90.67.172    | 135.90.92.246   \n 130.198.1.212  \n 135.90.89.221 | TCP 443  \n TCP 80 |
| `Tokyo (jp-tok)`       | `logs.jp-tok.logging.cloud.ibm.com`         | 128.168.107.243 \n 165.192.100.74 \n 169.56.11.253    | 161.202.231.186 \n 128.168.96.179 \n 165.192.111.36 | TCP 443  \n TCP 80 |
| `Toronto (ca-tor)`     | `logs.ca-tor.logging.cloud.ibm.com`         | 163.74.65.131   \n 169.55.135.27  \n 163.75.66.243    | 169.53.161.75   \n 163.74.65.133  \n 163.75.73.42 | TCP 443  \n TCP 80 |
| `Washington (us-east)` | `logs.us-east.logging.cloud.ibm.com`        | 169.47.134.84   \n 169.60.98.94   \n 169.61.98.204    | unchanged | TCP 443  \n TCP 80 |
{: caption="Table 1. Existing and new public endpoints" caption-side="bottom"}
