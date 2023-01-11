---

copyright:
  years:  2018, 2023
lastupdated: "2022-12-13"

keywords: IBM, Log Analysis, logging, endpoints

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Endpoints
{: #endpoints}

Review the connectivity options for interacting with {{site.data.keyword.la_full}}.
{: shortdesc}

Due to maintenance, {{site.data.keyword.la_full}} makes changes periodically to IPs in some regions. You might need to take action to continue using the service. This topic lists the currently supported, or planned to be supported, endpoints. For a history and current status of endpoint changes, see [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes).
{: important}

## Connectivity options
{: #connectivity-options}

{{site.data.keyword.la_full_notm}} offers two connectivity options:

Public endpoints
:   By default, you can connect to resources in your account over the {{site.data.keyword.cloud_notm}} public network.

Private endpoints
:   For added benefits, you can also enable [virtual routing and forwarding (VRF)](/docs/account?topic=account-vrf-service-endpoint#vrf") and [service endpoints](/docs/account?topic=account-vrf-service-endpoint) for your infrastructure account. When you enable VRF for your account, you can connect to {{site.data.keyword.la_full_notm}} by using a private IP that is accessible only through the {{site.data.keyword.cloud_notm}} private network. To learn more about VRF, see [Virtual routing and forwarding on {{site.data.keyword.cloud_notm}}](/docs/dl?topic=dl-overview-of-virtual-routing-and-forwarding-vrf-on-ibm-cloud). To learn how to connect to {{site.data.keyword.la_full_notm}} by using a private endpoint, [Securing your connection](/docs/log-analysis?topic=log-analysis-service-connection).


## Opening required ports and IP addresses in your firewall
{: #firewall}

If you have firewalls set up on the public or private network in your {{site.data.keyword.cloud_notm}} infrastructure account, you need to allow traffic to and from the {{site.data.keyword.la_full_notm}} service. You must allow traffic on TCP port 443 and TCP port 80 in your firewall for the API endpoints and the ingestion endpoints.

The ingestion endpoints are required to send logs into a logging instance. To see the list of endpoints, see [Ingestion endpoints](/docs/log-analysis?topic=log-analysis-endpoints#endpoints_ingestion).

The `API` endpoint is required for:
- The authentication of the logging agent.
- Exporting logs.
- Configuring resources by using the Config API.


## API endpoints
{: #endpoints_api}

### Public API endpoints
{: #endpoints_api_public}

The following table shows the public API endpoints:

| Region                 | Public API endpoint                  | Public IP addresses                            | Ports            |
|------------------------|--------------------------------------|------------------------------------------------|------------------|
| `Chennai (in-che)`     | `api.in-che.logging.cloud.ibm.com`   | 169.38.94.141                                  | TCP 443   TCP 80 |
| `Dallas (us-south)`    | `api.us-south.logging.cloud.ibm.com` | 50.22.151.6     52.117.134.204  67.228.208.253 | TCP 443   TCP 80 |
| `Frankfurt (eu-de)`    | `api.eu-de.logging.cloud.ibm.com`    | 149.81.169.206  158.177.133.235 161.156.28.220 | TCP 443   TCP 80 |
| `London (eu-gb)`       | `api.eu-gb.logging.cloud.ibm.com`    | 141.125.86.131  158.175.91.91   158.176.142.2  | TCP 443   TCP 80 |
| `Osaka (jp-osa)`       | `api.jp-osa.logging.cloud.ibm.com`   | 163.68.75.68    163.69.70.155   163.73.70.118  | TCP 443   TCP 80 |
| `Sao Paulo (br-sao)`   | `api.br-sao.logging.cloud.ibm.com`   | 163.107.67.3    163.107.68.196  163.109.68.98  | TCP 443   TCP 80 |
| `Sydney (au-syd)`      | `api.au-syd.logging.cloud.ibm.com`   | 130.198.1.212   135.90.89.221   135.90.92.246  | TCP 443   TCP 80 |
| `Tokyo (jp-tok)`       | `api.jp-tok.logging.cloud.ibm.com`   | 128.168.96.179  161.202.231.186 165.192.111.36 | TCP 443   TCP 80 |
| `Toronto (ca-tor)`     | `api.ca-tor.logging.cloud.ibm.com`   | 163.74.65.133   163.75.73.42    169.53.161.75  | TCP 443   TCP 80 |
| `Washington (us-east)` | `api.us-east.logging.cloud.ibm.com`  | 169.47.134.86   169.60.72.62    169.61.107.10  | TCP 443   TCP 80 |

{: caption="Table 1. Lists of public API endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}


### Private API endpoints
{: #endpoints_api_private}

The following table shows the private API endpoints:

| Region                 | Private API endpoint                         | Private IP addresses                         | Ports            |
|------------------------|----------------------------------------------|----------------------------------------------|------------------|
| `Chennai (in-che)`     | `api.private.in-che.logging.cloud.ibm.com`   | 166.9.60.6                                   | TCP 443   TCP 80 |
| `Dallas (us-south)`    | `api.private.us-south.logging.cloud.ibm.com` | 166.9.12.12     166.9.14.2      166.9.16.11  | TCP 443   TCP 80 |
| `Frankfurt (eu-de)`    | `api.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.2      166.9.30.231    166.9.32.7   | TCP 443   TCP 80 |
| `London (eu-gb)`       | `api.private.eu-gb.logging.cloud.ibm.com`    | 166.9.34.2      166.9.36.2      166.9.38.4   | TCP 443   TCP 80 |
| `Osaka (jp-osa)`       | `api.private.jp-osa.logging.cloud.ibm.com`   | 166.9.70.19     166.9.71.21     166.9.72.19  | TCP 443   TCP 80 |
| `Sao Paulo (br-sao)`   | `api.private.br-sao.logging.cloud.ibm.com`   | 166.9.82.23     166.9.83.24     166.9.84.25  | TCP 443   TCP 80 |
| `Sydney (au-syd)`      | `api.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.2      166.9.54.128    166.9.56.3   | TCP 443   TCP 80 |
| `Tokyo (jp-tok)`       | `api.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.2      166.9.42.3      166.9.44.13  | TCP 443   TCP 80 |
| `Toronto (ca-tor)`     | `api.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.26     166.9.77.23     166.9.78.24  | TCP 443   TCP 80 |
| `Washington (us-east)` | `api.private.us-east.logging.cloud.ibm.com`  | 166.9.20.72     166.9.22.35     166.9.24.247 | TCP 443   TCP 80 |

{: caption="Table 2. Lists of private API endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

## Ingestion endpoints
{: #endpoints_ingestion}

### Public ingestion endpoints
{: #endpoints_ingestion_public}

The following table shows the ingestion endpoints:

| Region                 | Public Ingestion endpoint             | Public IP addresses                             | Ports            |
|------------------------|---------------------------------------|-------------------------------------------------|------------------|
| `Chennai (in-che)`     | `logs.in-che.logging.cloud.ibm.com`   | 169.38.75.46                                    | TCP 443   TCP 80 |
| `Dallas (us-south)`    | `logs.us-south.logging.cloud.ibm.com` | 169.61.197.84   50.22.153.155   67.228.211.6    | TCP 443   TCP 80 |
| `Frankfurt (eu-de)`    | `logs.eu-de.logging.cloud.ibm.com`    | 149.81.108.173  158.177.157.66  161.156.78.142  | TCP 443   TCP 80 |
| `London (eu-gb)`       | `logs.eu-gb.logging.cloud.ibm.com`    | 141.125.102.149 158.175.113.18  158.176.163.117 | TCP 443   TCP 80 |
| `Osaka (jp-osa)`       | `logs.jp-osa.logging.cloud.ibm.com`   | 163.68.73.62    163.69.67.212   163.73.68.44    | TCP 443   TCP 80 |
| `Sao Paulo (br-sao)`   | `logs.br-sao.logging.cloud.ibm.com`   | 163.107.69.13   163.109.68.108  169.57.152.195  | TCP 443   TCP 80 |
| `Sydney (au-syd)`      | `logs.au-syd.logging.cloud.ibm.com`   | 130.198.1.213   135.90.67.172   168.1.27.60     | TCP 443   TCP 80 |
| `Tokyo (jp-tok)`       | `logs.jp-tok.logging.cloud.ibm.com`   | 128.168.107.243 165.192.100.74  169.56.11.253   | TCP 443   TCP 80 |
| `Toronto (ca-tor)`     | `logs.ca-tor.logging.cloud.ibm.com`   | 163.74.65.131   163.75.66.243   169.55.135.27   | TCP 443   TCP 80 |
| `Washington (us-east)` | `logs.us-east.logging.cloud.ibm.com`  | 169.47.134.84   169.60.98.94    169.61.98.204   | TCP 443   TCP 80 |

{: caption="Table 3. Lists of public ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

### Private ingestion endpoints
{: #endpoints_ingestion_private}

The following table shows the private ingestion endpoints:

| Region                 | Private Ingestion endpoint                    | Private IP addresses                         | Ports            |
|------------------------|-----------------------------------------------|----------------------------------------------|------------------|
| `Chennai (in-che)`     | `logs.private.in-che.logging.cloud.ibm.com`   | 166.9.60.7                                   | TCP 443   TCP 80 |
| `Dallas (us-south)`    | `logs.private.us-south.logging.cloud.ibm.com` | 166.9.61.86     166.9.86.91     166.9.90.101 | TCP 443   TCP 80 |
| `Frankfurt (eu-de)`    | `logs.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.3      166.9.30.238    166.9.32.21  | TCP 443   TCP 80 |
| `London (eu-gb)`       | `logs.private.eu-gb.logging.cloud.ibm.com`    | 166.9.34.4      166.9.36.3      166.9.38.5   | TCP 443   TCP 80 |
| `Osaka (jp-osa)`       | `logs.private.jp-osa.logging.cloud.ibm.com`   | 166.9.70.21     166.9.71.20     166.9.72.21  | TCP 443   TCP 80 |
| `Sao Paulo (br-sao)`   | `logs.private.br-sao.logging.cloud.ibm.com`   | 166.9.82.25     166.9.83.25     166.9.84.27  | TCP 443   TCP 80 |
| `Sydney (au-syd)`      | `logs.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.5      166.9.54.127    166.9.56.20  | TCP 443   TCP 80 |
| `Tokyo (jp-tok)`       | `logs.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.3      166.9.42.4      166.9.44.71  | TCP 443   TCP 80 |
| `Toronto (ca-tor)`     | `logs.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.29     166.9.77.26     166.9.78.27  | TCP 443   TCP 80 |
| `Washington (us-east)` | `logs.private.us-east.logging.cloud.ibm.com`  | 166.9.20.73     166.9.22.36     166.9.24.245 | TCP 443   TCP 80 |

{: caption="Table 4. Lists of private ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}


## Web UI endpoints
{: #endpoints_loganalysis_ui}

The following table shows the logging web UI endpoints:

| Location        | Region                 | Public Endpoint                              |
|-----------------|------------------------|----------------------------------------------|
| `Asia Pacific`  | `Chennai (in-che)`     | `https://app.in-che.logging.cloud.ibm.com`   |
| `Asia Pacific`  | `Osaka (jp-osa)`       | `https://app.jp-osa.logging.cloud.ibm.com`   |
| `Asia Pacific`  | `Sydney (au-syd)`      | `https://app.au-syd.logging.cloud.ibm.com`   |
| `Asia Pacific`  | `Tokyo (jp-tok)`       | `https://app.jp-tok.logging.cloud.ibm.com`   |
| `Europe`        | `Frankfurt (eu-de)`    | `https://app.eu-de.logging.cloud.ibm.com`    |
| `Europe`        | `London (eu-gb)`       | `https://app.eu-gb.logging.cloud.ibm.com`    |
| `North America` | `Dallas (us-south)`    | `https://app.us-south.logging.cloud.ibm.com` |
| `North America` | `Toronto (ca-tor)`     | `https://app.ca-tor.logging.cloud.ibm.com`   |
| `North America` | `Washington (us-east)` | `https://app.us-east.logging.cloud.ibm.com`  |
| `South America` | `Sao Paulo (br-sao)`   | `https://app.br-sao.logging.cloud.ibm.com`   |

{: caption="Table 5. Lists of UI endpoints" caption-side="top"}


## Syslog endpoints
{: #endpoints_syslog}

### Syslog public endpoints
{: #endpoints_syslog_endpoints}

The following tables show the syslog public endpoints:

| Region                 | Public Syslog TCP Endpoint                         | Public IP addresses                             |
|------------------------|----------------------------------------------------|-------------------------------------------------|
| `Chennai (in-che)`     | `syslog://syslog-a.in-che.logging.cloud.ibm.com`   | 169.38.75.43                                    |
| `Dallas (us-south)`    | `syslog://syslog-a.us-south.logging.cloud.ibm.com` | 52.116.247.170  52.117.134.206  67.228.102.117  |
| `Frankfurt (eu-de)`    | `syslog://syslog-a.eu-de.logging.cloud.ibm.com`    | 149.81.108.28   158.177.157.70  161.156.78.138  |
| `London (eu-gb)`       | `syslog://syslog-a.eu-gb.logging.cloud.ibm.com`    | 141.125.102.148 158.175.113.22  158.176.163.115 |
| `Osaka (jp-osa)`       | `syslog://syslog-a.jp-osa.logging.cloud.ibm.com`   | 163.68.72.220   163.69.67.210   163.73.68.45    |
| `Sao Paulo (br-sao)`   | `syslog://syslog-a.br-sao.logging.cloud.ibm.com`   | 163.107.68.195  163.109.68.109  169.57.254.118  |
| `Sydney (au-syd)`      | `syslog://syslog-a.au-syd.logging.cloud.ibm.com`   | 130.198.1.210   135.90.92.254   168.1.202.76    |
| `Tokyo (jp-tok)`       | `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`   | 128.168.95.2    161.202.248.162 165.192.100.77  |
| `Toronto (ca-tor)`     | `syslog://syslog-a.ca-tor.logging.cloud.ibm.com`   | 163.74.69.234   163.75.66.13    169.53.186.154  |
| `Washington (us-east)` | `syslog://syslog-a.us-east.logging.cloud.ibm.com`  | 169.47.34.203   169.60.121.243  169.61.98.203   |

{: caption="Table 6. List of syslog-a public endpoints" caption-side="top"}

| Region                 | Public Syslog UDP Endpoint                         | Public IP addresses                             |
|------------------------|----------------------------------------------------|-------------------------------------------------|
| `Chennai (in-che)`     | `syslog://syslog-u.in-che.logging.cloud.ibm.com`   | 169.38.126.5                                    |
| `Dallas (us-south)`    | `syslog://syslog-u.us-south.logging.cloud.ibm.com` | 169.60.203.92   52.116.247.173  67.228.102.116  |
| `Frankfurt (eu-de)`    | `syslog://syslog-u.eu-de.logging.cloud.ibm.com`    | 149.81.108.30   158.177.143.26  161.156.78.139  |
| `London (eu-gb)`       | `syslog://syslog-u.eu-gb.logging.cloud.ibm.com`    | 141.125.140.98  158.175.66.210  158.176.163.156 |
| `Osaka (jp-osa)`       | `syslog://syslog-u.jp-osa.logging.cloud.ibm.com`   | 163.68.72.219   163.69.68.70    163.73.68.46    |
| `Sao Paulo (br-sao)`   | `syslog://syslog-u.br-sao.logging.cloud.ibm.com`   | 163.107.69.14   163.109.68.100  169.57.152.196  |
| `Sydney (au-syd)`      | `syslog://syslog-u.au-syd.logging.cloud.ibm.com`   | 130.198.71.30   135.90.92.253   168.1.27.59     |
| `Tokyo (jp-tok)`       | `syslog://syslog-u.jp-tok.logging.cloud.ibm.com`   | 128.168.107.244 165.192.100.76  169.56.11.252   |
| `Toronto (ca-tor)`     | `syslog://syslog-u.ca-tor.logging.cloud.ibm.com`   | 163.74.69.236   163.75.66.11    169.55.135.29   |
| `Washington (us-east)` | `syslog://syslog-u.us-east.logging.cloud.ibm.com`  | 169.47.34.204   169.60.98.91    169.61.98.202   |


{: caption="Table 7. List of syslog-u public endpoints" caption-side="top"}

### Syslog private endpoints
{: #endpoints_syslog_private_endpoints}

The following table shows the syslog private endpoints:

| Region                 | Private Syslog TCP Endpoint                                | Private IP addresses                         |
|------------------------|------------------------------------------------------------|----------------------------------------------|
| `Chennai (in-che)`     | `syslog://syslog-a.private.in-che.logging.cloud.ibm.com`   | 166.9.60.9                                   |
| `Dallas (us-south)`    | `syslog://syslog-a.private.us-south.logging.cloud.ibm.com` | 166.9.12.15     166.9.14.5      166.9.16.14  |
| `Frankfurt (eu-de)`    | `syslog://syslog-a.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.5      166.9.30.236    166.9.32.23  |
| `London (eu-gb)`       | `syslog://syslog-a.private.eu-gb.logging.cloud.ibm.com`    | 166.9.34.18     166.9.36.5      166.9.38.20  |
| `Osaka (jp-osa)`       | `syslog://syslog-a.private.jp-osa.logging.cloud.ibm.com`   | 166.9.70.22     166.9.71.22     166.9.72.22  |
| `Sao Paulo (br-sao)`   | `syslog://syslog-a.private.br-sao.logging.cloud.ibm.com`   | 166.9.82.26     166.9.83.22     166.9.84.23  |
| `Sydney (au-syd)`      | `syslog://syslog-a.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.8      166.9.54.124    166.9.56.22  |
| `Tokyo (jp-tok)`       | `syslog://syslog-a.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.23     166.9.42.26     166.9.44.67  |
| `Toronto (ca-tor)`     | `syslog://syslog-a.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.31     166.9.77.28     166.9.78.29  |
| `Washington (us-east)` | `syslog://syslog-a.private.us-east.logging.cloud.ibm.com`  | 166.9.20.76     166.9.22.38     166.9.24.243 |

{: caption="Table 8. Lists of syslog-a private endpoints" caption-side="top"}

| Region                 | Private Syslog UDP Endpoint                                | Private IP addresses                         |
|------------------------|------------------------------------------------------------|----------------------------------------------|
| `Chennai (in-che)`     | `syslog://syslog-u.private.in-che.logging.cloud.ibm.com`   | 166.9.60.10                                  |
| `Dallas (us-south)`    | `syslog://syslog-u.private.us-south.logging.cloud.ibm.com` | 166.9.12.16     166.9.14.6      166.9.16.15  |
| `Frankfurt (eu-de)`    | `syslog://syslog-u.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.7      166.9.30.239    166.9.32.24  |
| `London (eu-gb)`       | `syslog://syslog-u.private.eu-gb.logging.cloud.ibm.com`    | 166.9.34.19     166.9.36.6      166.9.38.21  |
| `Osaka (jp-osa)`       | `syslog://syslog-u.private.jp-osa.logging.cloud.ibm.com`   | 166.9.70.23     166.9.71.23     166.9.72.23  |
| `Sao Paulo (br-sao)`   | `syslog://syslog-u.private.br-sao.logging.cloud.ibm.com`   | 166.9.82.27     166.9.83.26     166.9.84.26  |
| `Sydney (au-syd)`      | `syslog://syslog-u.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.9      166.9.54.115    166.9.56.23  |
| `Tokyo (jp-tok)`       | `syslog://syslog-u.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.24     166.9.42.27     166.9.44.73  |
| `Toronto (ca-tor)`     | `syslog://syslog-u.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.32     166.9.77.29     166.9.78.30  |
| `Washington (us-east)` | `syslog://syslog-u.private.us-east.logging.cloud.ibm.com`  | 166.9.20.77     166.9.22.39     166.9.24.244 |

{: caption="Table 9. List of syslog-u private endpoints" caption-side="top"}


### Syslog TLS endpoints
{: #endpoints_syslog_tls}

The following table shows the syslog TLS endpoints:

| Region                 | Public Syslog TLS Endpoint                             | Public IP addresses                             |
|------------------------|--------------------------------------------------------|-------------------------------------------------|
| `Chennai (in-che)`     | `syslog-tls://syslog-a.in-che.logging.cloud.ibm.com`   | 169.38.75.43                                    |
| `Dallas (us-south)`    | `syslog-tls://syslog-a.us-south.logging.cloud.ibm.com` | 52.116.247.170  52.117.134.206  67.228.102.117  |
| `Frankfurt (eu-de)`    | `syslog-tls://syslog-a.eu-de.logging.cloud.ibm.com`    | 149.81.108.28   158.177.157.70  161.156.78.138  |
| `London (eu-gb)`       | `syslog-tls://syslog-a.eu-gb.logging.cloud.ibm.com`    | 141.125.102.148 158.175.113.22  158.176.163.115 |
| `Osaka (jp-osa)`       | `syslog-tls://syslog-a.jp-osa.logging.cloud.ibm.com`   | 163.68.72.220   163.69.67.210   163.73.68.45    |
| `Sao Paulo (br-sao)`   | `syslog-tls://syslog-a.br-sao.logging.cloud.ibm.com`   | 163.107.68.195  163.109.68.109  169.57.254.118  |
| `Sydney (au-syd)`      | `syslog-tls://syslog-a.au-syd.logging.cloud.ibm.com`   | 130.198.1.210   135.90.92.254   168.1.202.76    |
| `Tokyo (jp-tok)`       | `syslog-tls://syslog-a.jp-tok.logging.cloud.ibm.com`   | 128.168.95.2    161.202.248.162 165.192.100.77  |
| `Toronto (ca-tor)`     | `syslog-tls://syslog-a.ca-tor.logging.cloud.ibm.com`   | 163.74.69.234   163.75.66.13    169.53.186.154  |
| `Washington (us-east)` | `syslog-tls://syslog-a.us-east.logging.cloud.ibm.com`  | 169.47.34.203   169.60.121.243  169.61.98.203   |


{: caption="Table 10. Lists of Syslog-TLS public endpoints" caption-side="top"}


### Private syslog TLS endpoints
{: #endpoints_syslog_tls_private}

The following table shows the syslog TLS endpoints:

| Region                 | Private Syslog TLS Endpoint                                    | Private IP addresses                         |
|------------------------|----------------------------------------------------------------|----------------------------------------------|
| `Chennai (in-che)`     | `syslog-tls://syslog-a.private.in-che.logging.cloud.ibm.com`   | 166.9.60.9                                   |
| `Dallas (us-south)`    | `syslog-tls://syslog-a.private.us-south.logging.cloud.ibm.com` | 166.9.12.15     166.9.14.5      166.9.16.14  |
| `Frankfurt (eu-de)`    | `syslog-tls://syslog-a.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.5      166.9.30.236    166.9.32.23  |
| `London (eu-gb)`       | `syslog-tls://syslog-a.private.eu-gb.logging.cloud.ibm.com`    | 166.9.34.18     166.9.36.5      166.9.38.20  |
| `Osaka (jp-osa)`       | `syslog-tls://syslog-a.private.jp-osa.logging.cloud.ibm.com`   | 166.9.70.22     166.9.71.22     166.9.72.22  |
| `Sao Paulo (br-sao)`   | `syslog-tls://syslog-a.private.br-sao.logging.cloud.ibm.com`   | 166.9.82.26     166.9.83.22     166.9.84.23  |
| `Sydney (au-syd)`      | `syslog-tls://syslog-a.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.8      166.9.54.124    166.9.56.22  |
| `Tokyo (jp-tok)`       | `syslog-tls://syslog-a.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.23     166.9.42.26     166.9.44.67  |
| `Toronto (ca-tor)`     | `syslog-tls://syslog-a.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.31     166.9.77.28     166.9.78.29  |
| `Washington (us-east)` | `syslog-tls://syslog-a.private.us-east.logging.cloud.ibm.com`  | 166.9.20.76     166.9.22.38     166.9.24.243 |


{: caption="Table 11. Lists of Syslog-TLS private endpoints" caption-side="top"}
