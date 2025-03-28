---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, endpoints

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Endpoints
{: #endpoints}

Review the connectivity options for interacting with {{site.data.keyword.la_full}}.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

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

| Region                 | Public API endpoint                  | Public IP addresses                                 | Ports              |
|------------------------|--------------------------------------|-----------------------------------------------------|--------------------|
| `Chennai (in-che)`     | `api.in-che.logging.cloud.ibm.com`   | 169.38.94.141                                       | TCP 443  \n TCP 80 |
| `Dallas (us-south)`    | `api.us-south.logging.cloud.ibm.com` | 52.117.134.204  \n 50.22.151.6    \n 67.228.208.253 | TCP 443  \n TCP 80 |
| `Frankfurt (eu-de)`    | `api.eu-de.logging.cloud.ibm.com`    | 158.177.133.235 \n 161.156.28.220 \n 149.81.169.206 | TCP 443  \n TCP 80 |
| `London (eu-gb)`       | `api.eu-gb.logging.cloud.ibm.com`    | 158.175.91.91   \n 141.125.86.131 \n 158.176.142.2  | TCP 443  \n TCP 80 |
| `Madrid (eu-es)`       | `api.eu-es.logging.cloud.ibm.com`    | 13.120.68.42 `(*)`  \n 13.121.67.53 `(*)`  \n 13.122.67.90 `(*)`  | TCP 443  \n TCP 80 |
| `Osaka (jp-osa)`       | `api.jp-osa.logging.cloud.ibm.com`   | 163.68.75.68    \n 163.69.70.155  \n 163.73.70.118  | TCP 443  \n TCP 80 |
| `Sao Paulo (br-sao)`   | `api.br-sao.logging.cloud.ibm.com`   | 163.107.67.3    \n 163.107.68.196 \n 163.109.68.98  | TCP 443  \n TCP 80 |
| `Sydney (au-syd)`      | `api.au-syd.logging.cloud.ibm.com`   | 135.90.92.246   \n 130.198.1.212  \n 135.90.89.221  | TCP 443  \n TCP 80 |
| `Tokyo (jp-tok)`       | `api.jp-tok.logging.cloud.ibm.com`   | 161.202.231.186 \n 128.168.96.179 \n 165.192.111.36 | TCP 443  \n TCP 80 |
| `Toronto (ca-tor)`     | `api.ca-tor.logging.cloud.ibm.com`   | 169.53.161.75   \n 163.74.65.133  \n 163.75.73.42   | TCP 443  \n TCP 80 |
| `Washington (us-east)` | `api.us-east.logging.cloud.ibm.com`  | 169.47.134.86   \n 169.60.72.62   \n 169.61.107.10  | TCP 443  \n TCP 80 |
{: caption="Lists of public API endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

### Private API endpoints
{: #endpoints_api_private}

The following table shows the private API endpoints:

| Region                 | Private API endpoint                         | Private IP addresses                            | Ports              |
|------------------------|----------------------------------------------|-------------------------------------------------|--------------------|
| `Chennai (in-che)`     | `api.private.in-che.logging.cloud.ibm.com`   | 166.9.60.6  \n  \n 166.9.60.11 `(*)`  \n  \n  166.9.249.113 `(*)`  \n 166.9.249.142 `(*)`  \n 166.9.249.178 `(*)`   | TCP 443  \n TCP 80 |
| `Dallas (us-south)`    | `api.private.us-south.logging.cloud.ibm.com` | 166.9.16.11   \n 166.9.12.12    \n 166.9.14.2  \n  \n 166.9.90.41 `(*)`  \n 166.9.85.89 `(*)`  \n 166.9.61.79 `(*)`   \n  \n  166.9.228.39 `(*)`  \n 166.9.229.39 `(*)`  \n 166.9.230.39 `(*)` | TCP 443  \n TCP 80 |
| `Frankfurt (eu-de)`    | `api.private.eu-de.logging.cloud.ibm.com`    | 166.9.32.7    \n 166.9.28.2     \n 166.9.30.231  \n  \n 166.9.30.45 `(*)`  \n 166.9.28.159 `(*)`  \n 166.9.32.117 `(*)`  \n  \n 166.9.248.116 `(*)`  \n 166.9.248.149 `(*)` \n 166.9.248.85 `(*)` | TCP 443  \n TCP 80 |
| `London (eu-gb)`       | `api.private.eu-gb.logging.cloud.ibm.com`    | 166.9.36.2    \n 166.9.38.4     \n 166.9.34.2  \n  \n 166.9.36.105 `(*)`  \n 166.9.34.79 `(*)`  \n 166.9.38.84 `(*)`  \n  \n 166.9.244.22 `(*)`  \n 166.9.244.53 `(*)`  \n 166.9.244.85 `(*)`   | TCP 443  \n TCP 80 |
| `Madrid (eu-es)`       | `api.private.eu-es.logging.cloud.ibm.com`    | 166.9.94.33  \n 166.9.95.35  \n 166.9.96.34  \n  \n 166.9.225.13 `(*)`  \n 166.9.226.14 `(*)`  \n 166.9.227.13 `(*)` | TCP 443  \n TCP 80 |
| `Osaka (jp-osa)`       | `api.private.jp-osa.logging.cloud.ibm.com`   | 166.9.71.21   \n 166.9.72.19    \n 166.9.70.19  \n  \n 166.9.71.14 `(*)`  \n 166.9.72.13 `(*)`  \n 166.9.70.13 `(*)`  \n  \n 166.9.247.106 `(*)`  \n 166.9.247.37 `(*)`  \n 166.9.247.72 `(*)` | TCP 443  \n TCP 80 |
| `Sao Paulo (br-sao)`   | `api.private.br-sao.logging.cloud.ibm.com`   | 166.9.83.24   \n 166.9.82.23    \n 166.9.84.25  \n  \n 166.9.83.12 `(*)`  \n 166.9.82.12 `(*)`  \n 166.9.84.12 `(*)`  \n  \n 166.9.246.105 `(*)`   \n 166.9.246.156 `(*)` \n 166.9.246.75 `(*)` | TCP 443  \n TCP 80 |
| `Sydney (au-syd)`      | `api.private.au-syd.logging.cloud.ibm.com`   | 166.9.56.3    \n 166.9.52.2     \n 166.9.54.128  \n  \n 166.9.56.79 `(*)`  \n 166.9.52.82 `(*)`  \n 166.9.54.129 `(*)`  \n  \n 166.9.244.111 `(*)`  \n 166.9.244.141 `(*)`  \n 166.9.244.175 `(*)` | TCP 443  \n TCP 80 |
| `Tokyo (jp-tok)`       | `api.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.2    \n 166.9.42.3     \n 166.9.44.13  \n  \n 166.9.40.13 `(*)`  \n 166.9.42.72 `(*)`  \n 166.9.44.76 `(*)`  \n  \n 166.9.249.108 `(*)`  \n 166.9.249.137 `(*)`  \n 166.9.249.173 `(*)` | TCP 443  \n TCP 80 |
| `Toronto (ca-tor)`     | `api.private.ca-tor.logging.cloud.ibm.com`   | 166.9.77.23   \n 166.9.76.26    \n 166.9.78.24  \n  \n 166.9.78.10 `(*)`  \n 166.9.76.10 `(*)`  \n 166.9.77.10 `(*)`  \n  \n 166.9.247.151 `(*)`  \n 166.9.247.182 `(*)`  \n 166.9.247.201 `(*)` | TCP 443  \n TCP 80 |
| `Washington (us-east)` | `api.private.us-east.logging.cloud.ibm.com`  | 166.9.22.35   \n 166.9.20.72    \n 166.9.24.247  \n  \n 166.9.24.171 `(*)`  \n 166.9.22.194 `(*)`  \n 166.9.68.157 `(*)`  \n  \n 166.9.231.235 `(*)`  \n 166.9.232.23 `(*)`  \n 166.9.233.10 `(*)` | TCP 443  \n TCP 80 |
{: caption="Lists of private API endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

## Ingestion endpoints
{: #endpoints_ingestion}

### Public ingestion endpoints
{: #endpoints_ingestion_public}

The following table shows the ingestion endpoints:

| Region                 | Public Ingestion endpoint             | Public IP addresses                                   | Ports              |
|------------------------|---------------------------------------|-------------------------------------------------------|--------------------|
| `Chennai (in-che)`     | `logs.in-che.logging.cloud.ibm.com`   | 169.38.75.46  \n  \n 169.38.94.141 `(*)` | TCP 443  \n TCP 80 |
| `Dallas (us-south)`    | `logs.us-south.logging.cloud.ibm.com` | 169.61.197.84   \n 50.22.153.155  \n 67.228.211.6  \n  \n 52.117.134.204 `(*)`  \n 50.22.151.6 `(*)`  \n 67.228.208.253 `(*)` | TCP 443  \n TCP 80 |
| `Frankfurt (eu-de)`    | `logs.eu-de.logging.cloud.ibm.com`    | 149.81.108.173  \n 158.177.157.66 \n 161.156.78.142  \n  \n 158.177.133.235 `(*)`  \n 161.156.28.220 `(*)`  \n 149.81.169.206 `(*)`   | TCP 443  \n TCP 80 |
| `London (eu-gb)`       | `logs.eu-gb.logging.cloud.ibm.com`    | 158.176.163.117 \n 158.175.113.18 \n 141.125.102.149  \n  \n 158.175.91.91 `(*)`  \n 141.125.86.131 `(*)`  \n 158.176.142.2 `(*)`  | TCP 443  \n TCP 80 |
| `Madrid (eu-es)`       | `logs.eu-es.logging.cloud.ibm.com`    | 13.120.68.42 `(*)`  \n 13.121.67.53 `(*)`  \n 13.122.67.90 `(*)` | TCP 443  \n TCP 80 |
| `Osaka (jp-osa)`       | `logs.jp-osa.logging.cloud.ibm.com`   | 163.73.68.44    \n 163.69.67.212  \n 163.68.73.62  \n  \n 163.68.75.68 `(*)`    \n 163.69.70.155 `(*)`  \n 163.73.70.118 `(*)` | TCP 443  \n TCP 80 |
| `Sao Paulo (br-sao)`   | `logs.br-sao.logging.cloud.ibm.com`   | 163.109.68.108  \n 163.107.69.13  \n 169.57.152.195  \n  \n 163.107.67.3 `(*)`  \n 163.107.68.196 `(*)`  \n 163.109.68.98 `(*)` | TCP 443  \n TCP 80 |
| `Sydney (au-syd)`      | `logs.au-syd.logging.cloud.ibm.com`   | 168.1.27.60     \n 130.198.1.213  \n 135.90.67.172  \n  \n 135.90.92.246 `(*)`  \n 130.198.1.212 `(*)`  \n 135.90.89.221 `(*)` | TCP 443  \n TCP 80 |
| `Tokyo (jp-tok)`       | `logs.jp-tok.logging.cloud.ibm.com`   | 128.168.107.243 \n 165.192.100.74 \n 169.56.11.253  \n  \n 161.202.231.186 `(*)`  \n 128.168.96.179 `(*)`  \n 165.192.111.36 `(*)` | TCP 443  \n TCP 80 |
| `Toronto (ca-tor)`     | `logs.ca-tor.logging.cloud.ibm.com`   | 163.74.65.131   \n 169.55.135.27  \n 163.75.66.243  \n  \n 169.53.161.75 `(*)`  \n 163.74.65.133 `(*)`  \n 163.75.73.42 `(*)` | TCP 443  \n TCP 80 |
| `Washington (us-east)` | `logs.us-east.logging.cloud.ibm.com`  | 169.47.134.84   \n 169.60.98.94   \n 169.61.98.204  \n  \n 169.47.134.86 `(*)`  \n 169.60.72.62 `(*)`  \n 169.61.107.10 `(*)` | TCP 443  \n TCP 80 |
{: caption="Lists of public ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

### Private ingestion endpoints
{: #endpoints_ingestion_private}

The following table shows the private ingestion endpoints:


| Region                   | Private Ingestion endpoint                    | Private IP addresses                        | Ports              |
|--------------------------|-----------------------------------------------|---------------------------------------------|--------------------|
| `Chennai (in-che)`       | `logs.private.in-che.logging.cloud.ibm.com`   | 166.9.60.7  \n  \n 166.9.60.11 `(*)` \n  \n  166.9.249.113 `(*)`  \n 166.9.249.142 `(*)`  \n 166.9.249.178 `(*)` | TCP 443  \n TCP 80 |
| `Dallas (us-south)`      | `logs.private.us-south.logging.cloud.ibm.com` | 166.9.61.86 \n 166.9.90.101 \n 166.9.86.91  \n  \n 166.9.90.41 `(*)`  \n 166.9.85.89 `(*)`  \n 166.9.61.79 `(*)`  \n  \n  166.9.228.39 `(*)`  \n 166.9.229.39 `(*)`  \n 166.9.230.39 `(*)` | TCP 443  \n TCP 80 |
| `Frankfurt (eu-de)`      | `logs.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.3  \n 166.9.32.21  \n 166.9.30.238  \n  \n 166.9.30.45 `(*)`  \n 166.9.28.159 `(*)`  \n 166.9.32.117 `(*)`  \n  \n 166.9.248.116 `(*)`  \n 166.9.248.149 `(*)` \n 166.9.248.85 `(*)` | TCP 443  \n TCP 80 |
| `London (eu-gb)`         | `logs.private.eu-gb.logging.cloud.ibm.com`    | 166.9.36.3  \n 166.9.34.4   \n 166.9.38.5  \n  \n 166.9.36.105 `(*)`  \n 166.9.34.79 `(*)`  \n 166.9.38.84 `(*)`  \n  \n 166.9.244.22 `(*)`  \n 166.9.244.53 `(*)`  \n 166.9.244.85 `(*)` | TCP 443  \n TCP 80 |
| `Madrid (eu-es)`         | `logs.private.eu-es.logging.cloud.ibm.com`    | 166.9.94.33 `(*)`  \n 166.9.95.35 `(*)`  \n 166.9.96.34 `(*)`  \n  \n 166.9.225.13 `(*)` \n 166.9.226.14 `(*)`  \n 166.9.227.13 `(*)` | TCP 443  \n TCP 80 |
| `Osaka (jp-osa)`         | `logs.private.jp-osa.logging.cloud.ibm.com`   | 166.9.71.20 \n 166.9.70.21  \n 166.9.72.21  \n  \n 166.9.71.14 `(*)`  \n 166.9.72.13 `(*)`  \n 166.9.70.13 `(*)`  \n  \n 166.9.247.106 `(*)`  \n 166.9.247.37 `(*)`  \n 166.9.247.72 `(*)` | TCP 443  \n TCP 80 |
| `Sao Paulo (br-sao)`     | `logs.private.br-sao.logging.cloud.ibm.com`   | 166.9.83.25 \n 166.9.84.27  \n 166.9.82.25  \n  \n 166.9.83.12 `(*)`  \n 166.9.82.12 `(*)`  \n 166.9.84.12 `(*)`  \n  \n  166.9.246.105 `(*)`  \n 166.9.246.156 `(*)`  \n 166.9.246.75 `(*)` | TCP 443  \n TCP 80 |
| `Sydney (au-syd)`        | `logs.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.5  \n 166.9.56.20  \n 166.9.54.127  \n  \n 166.9.56.79 `(*)`  \n 166.9.52.82 `(*)`  \n 166.9.54.129 `(*)` \n  \n 166.9.244.111 `(*)`  \n 166.9.244.141 `(*)`  \n 166.9.244.175 `(*)` | TCP 443  \n TCP 80 |
| `Tokyo (jp-tok)`         | `logs.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.3  \n 166.9.42.4   \n 166.9.44.71  \n  \n 166.9.40.13 `(*)`  \n 166.9.42.72 `(*)`  \n 166.9.44.76 `(*)`  \n  \n 166.9.249.108 `(*)`  \n 166.9.249.137 `(*)`  \n 166.9.249.173 `(*)` | TCP 443  \n TCP 80 |
| `Toronto (ca-tor)`       | `logs.private.ca-tor.logging.cloud.ibm.com`   | 166.9.77.26 \n 166.9.76.29  \n 166.9.78.27  \n  \n 166.9.78.10 `(*)`  \n 166.9.76.10 `(*)`  \n 166.9.77.10 `(*)`  \n  \n 166.9.247.151 `(*)`  \n 166.9.247.182 `(*)`  \n 166.9.247.201 `(*)` | TCP 443  \n TCP 80 |
| `Washington (us-east)`   | `logs.private.us-east.logging.cloud.ibm.com`  | 166.9.22.36 \n 166.9.20.73  \n 166.9.24.245  \n  \n 166.9.24.171 `(*)`  \n 166.9.22.194 `(*)`  \n 166.9.68.157 `(*)`  \n  \n 166.9.231.235 `(*)`  \n 166.9.232.23 `(*)`  \n 166.9.233.10 `(*)` | TCP 443  \n TCP 80 |
{: caption="Lists of private ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}


## Web UI endpoints
{: #endpoints_loganalysis_ui}

The following table shows the logging web UI endpoints:

| Location        | Region                    | Public Endpoint                              |
|-----------------|---------------------------|----------------------------------------------|
| `Asia Pacific`  | `Chennai (in-che)`        | `https://app.in-che.logging.cloud.ibm.com`   |
| `Asia Pacific`  | `Osaka (jp-osa)`          | `https://app.jp-osa.logging.cloud.ibm.com`   |
| `Asia Pacific`  | `Sydney (au-syd)`         | `https://app.au-syd.logging.cloud.ibm.com`   |
| `Asia Pacific`  | `Tokyo (jp-tok)`          | `https://app.jp-tok.logging.cloud.ibm.com`   |
| `Europe`        | `Frankfurt (eu-de)`       | `https://app.eu-de.logging.cloud.ibm.com`    |
| `Europe`        | `London (eu-gb)`          | `https://app.eu-gb.logging.cloud.ibm.com`    |
| `Europe`        | `Madrid (eu-es)`          | `https://app.eu-es.logging.cloud.ibm.com`    |
| `North America` | `Dallas (us-south)`       | `https://app.us-south.logging.cloud.ibm.com` |
| `North America` | `Washington DC (us-east)` | `https://app.us-east.logging.cloud.ibm.com`  |
| `North America` | `Toronto (ca-tor)`        | `https://app.ca-tor.logging.cloud.ibm.com`   |
| `South America` | `Sao Paulo (br-sao)`      | `https://app.br-sao.logging.cloud.ibm.com`   |
{: caption="Lists of UI endpoints" caption-side="top"}




## Syslog endpoints
{: #endpoints_syslog}

### Syslog public endpoints
{: #endpoints_syslog_endpoints}

The following tables show the syslog public endpoints:

| Region                   | Public Syslog TCP Endpoint                         | IP addresses                                           |
|--------------------------|----------------------------------------------------|--------------------------------------------------------|
| `Chennai (in-che)`       | `syslog://syslog-a.in-che.logging.cloud.ibm.com`   | 169.38.75.43                                           |
| `Dallas (us-south)`      | `syslog://syslog-a.us-south.logging.cloud.ibm.com` | 52.117.134.206   \n 52.116.247.170  \n 67.228.102.117  |
| `Frankfurt (eu-de)`      | `syslog://syslog-a.eu-de.logging.cloud.ibm.com`    | 149.81.108.28    \n 161.156.78.138  \n 158.177.157.70  |
| `London (eu-gb)`         | `syslog://syslog-a.eu-gb.logging.cloud.ibm.com`    | 141.125.102.148  \n 158.175.113.22  \n 158.176.163.115 |
| `Madrid (eu-es)`         | `syslog://syslog-a.eu-es.logging.cloud.ibm.com`    | 13.120.67.126 `(*)`  \n 13.121.68.83 `(*)`  \n 13.122.68.133 `(*)` |
| `Osaka (jp-osa)`         | `syslog://syslog-a.jp-osa.logging.cloud.ibm.com`   | 163.73.68.45     \n 163.69.67.210   \n 163.68.72.220   |
| `Sao Paulo (br-sao)`     | `syslog://syslog-a.br-sao.logging.cloud.ibm.com`   | 169.57.254.118   \n 163.107.68.195  \n 163.109.68.109  |
| `Sydney (au-syd)`        | `syslog://syslog-a.au-syd.logging.cloud.ibm.com`   | 168.1.202.76     \n 135.90.92.254   \n 130.198.1.210   |
| `Tokyo (jp-tok)`         | `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`   | 128.168.95.2     \n 161.202.248.162 \n 165.192.100.77  |
| `Toronto (ca-tor)`       | `syslog://syslog-a.ca-tor.logging.cloud.ibm.com`   | 163.75.66.13     \n 169.53.186.154  \n 163.74.69.234   |
| `Washington (us-east)`   | `syslog://syslog-a.us-east.logging.cloud.ibm.com`  | 169.61.98.203    \n 169.47.34.203   \n 169.60.121.243  |
{: caption="List of syslog-a public endpoints" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}


| Region                 | Public Syslog UDP Endpoint                         | IP addresses                                           |
|------------------------|----------------------------------------------------|--------------------------------------------------------|
| `Chennai (in-che)`     | `syslog://syslog-u.in-che.logging.cloud.ibm.com`   | 169.38.126.5                                           |
| `Dallas (us-south)`    | `syslog://syslog-u.us-south.logging.cloud.ibm.com` | 52.116.247.173  \n 169.60.203.92    \n 67.228.102.116  |
| `Frankfurt (eu-de)`    | `syslog://syslog-u.eu-de.logging.cloud.ibm.com`    | 161.156.78.139  \n 149.81.108.30    \n 158.177.143.26  |
| `London (eu-gb)`       | `syslog://syslog-u.eu-gb.logging.cloud.ibm.com`    | 158.175.66.210  \n 158.176.163.156  \n 141.125.140.98  |
| `Madrid (eu-es)`       | `syslog://syslog-u.eu-es.logging.cloud.ibm.com`    | 13.120.67.123 `(*)`  \n 13.121.68.85 `(*)`  \n 13.122.68.132 `(*)` |
| `Osaka (jp-osa)`       | `syslog://syslog-u.jp-osa.logging.cloud.ibm.com`   | 163.69.68.70    \n 163.73.68.46     \n 163.68.72.219   |
| `Sao Paulo (br-sao)`   | `syslog://syslog-u.br-sao.logging.cloud.ibm.com`   | 169.57.152.196  \n 163.107.69.14    \n 163.109.68.100  |
| `Sydney (au-syd)`      | `syslog://syslog-u.au-syd.logging.cloud.ibm.com`   | 135.90.92.253   \n 168.1.27.59      \n 130.198.71.30   |
| `Tokyo (jp-tok)`       | `syslog://syslog-u.jp-tok.logging.cloud.ibm.com`   | 165.192.100.76  \n 169.56.11.252    \n 128.168.107.244 |
| `Toronto (ca-tor)`     | `syslog://syslog-u.ca-tor.logging.cloud.ibm.com`   | 163.75.66.11    \n  169.55.135.29   \n 163.74.69.236   |
| `Washington (us-east)` | `syslog://syslog-u.us-east.logging.cloud.ibm.com`  | 169.47.34.204   \n 169.61.98.202    \n 169.60.98.91    |
{: caption="List of syslog-u public endpoints" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

### Syslog private endpoints
{: #endpoints_syslog_private_endpoints}

The following table shows the syslog private endpoints:

| Region                 | Private Endpoint                                  | IP addresses                                 |
|------------------------|---------------------------------------------------|----------------------------------------------|
| `Chennai (in-che)`     | `syslog-a.private.in-che.logging.cloud.ibm.com`   | 166.9.60.9                                   |
| `Dallas (us-south)`    | `syslog-a.private.us-south.logging.cloud.ibm.com` | 166.9.14.5   \n 166.9.12.15  \n 166.9.16.14  |
| `Frankfurt (eu-de)`    | `syslog-a.private.eu-de.logging.cloud.ibm.com`    | 166.9.32.23  \n 166.9.28.5   \n 166.9.30.236 |
| `London (eu-gb)`       | `syslog-a.private.eu-gb.logging.cloud.ibm.com`    | 166.9.38.20  \n 166.9.34.18  \n 166.9.36.5   |
| `Madrid (eu-es)`       | `syslog-a.private.eu-es.logging.cloud.ibm.com`    | 166.9.94.34 `(*)`  \n 166.9.95.32 `(*)`  \n 166.9.96.35 `(*)` |
| `Osaka (jp-osa)`       | `syslog-a.private.jp-osa.logging.cloud.ibm.com`   | 166.9.70.22  \n 166.9.71.22  \n 166.9.72.22  |
| `Sao Paulo (br-sao)`   | `syslog-a.private.br-sao.logging.cloud.ibm.com`   | 166.9.82.26  \n 166.9.83.22  \n 166.9.84.23  |
| `Sydney (au-syd)`      | `syslog-a.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.8   \n 166.9.56.22  \n 166.9.54.124 |
| `Tokyo (jp-tok)`       | `syslog-a.private.jp-tok.logging.cloud.ibm.com`   | 166.9.42.26  \n 166.9.40.23  \n 166.9.44.67  |
| `Toronto (ca-tor)`     | `syslog-a.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.31  \n 166.9.77.28  \n 166.9.78.29  |
| `Washington (us-east)` | `syslog-a.private.us-east.logging.cloud.ibm.com`  | 166.9.22.38  \n 166.9.20.76  \n 166.9.24.243 |
{: caption="Lists of syslog private endpoints" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

| Region                 | Public Endpoint                                            | IP addresses                               |
|------------------------|------------------------------------------------------------|--------------------------------------------|
| `Chennai (in-che)`     | `syslog://syslog-u.private.in-che.logging.cloud.ibm.com`   | 166.9.60.10                                |
| `Dallas (us-south)`    | `syslog://syslog-u.private.us-south.logging.cloud.ibm.com` | 166.9.14.6  \n 166.9.16.15 \n 166.9.12.16  |
| `Frankfurt (eu-de)`    | `syslog://syslog-u.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.7  \n 166.9.32.24 \n 166.9.30.239 |
| `London (eu-gb)`       | `syslog://syslog-u.private.eu-gb.logging.cloud.ibm.com`    | 166.9.36.6  \n 166.9.38.21 \n 166.9.34.19  |
| `Madrid (eu-es)`       | `syslog://syslog-u.private.eu-es.logging.cloud.ibm.com`    |  166.9.94.35 `(*)`  \n 166.9.95.33 `(*)` \n 166.9.96.32 `(*)`|
| `Osaka (jp-osa)`       | `syslog://syslog-u.private.jp-osa.logging.cloud.ibm.com`   | 166.9.70.23 \n 166.9.72.23 \n 166.9.71.23  |
| `Sao Paulo (br-sao)`   | `syslog://syslog-u.private.br-sao.logging.cloud.ibm.com`   | 166.9.83.26 \n 166.9.84.26 \n 166.9.82.27  |
| `Sydney (au-syd)`      | `syslog://syslog-u.private.au-syd.logging.cloud.ibm.com`   | 166.9.56.23 \n 166.9.52.9  \n 166.9.54.115 |
| `Tokyo (jp-tok)`       | `syslog://syslog-u.private.jp-tok.logging.cloud.ibm.com`   | 166.9.42.27 \n 166.9.40.24 \n 166.9.44.73  |
| `Toronto (ca-tor)`     | `syslog://syslog-u.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.32 \n 166.9.78.30 \n 166.9.77.29  |
| `Washington (us-east)` | `syslog://syslog-u.private.us-east.logging.cloud.ibm.com`  | 166.9.22.39 \n 166.9.20.77 \n 166.9.24.244 |
{: caption="List of syslog-u public endpoints" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}


### Syslog TLS endpoints
{: #endpoints_syslog_tls}

The following table shows the syslog TLS endpoints:


| Region                   |  Public Endpoint                                         | IP addresses                                         |
|--------------------------|----------------------------------------------------------|------------------------------------------------------|
| `Chennai (in-che)`       | `syslog-tls://syslog-a.in-che.logging.cloud.ibm.com`     | 169.38.75.43                                         |
| `Dallas (us-south)`      | `syslog-tls://syslog-a.us-south.logging.cloud.ibm.com`   | 52.116.247.170  \n 52.117.134.206  \n 67.228.102.117 |
| `Frankfurt (eu-de)`      | `syslog-tls://syslog-a.eu-de.logging.cloud.ibm.com`      | 161.156.78.138  \n 158.177.157.70  \n 149.81.108.28  |
| `London (eu-gb)`         | `syslog-tls://syslog-a.eu-gb.logging.cloud.ibm.com`      | 158.176.163.115 \n 141.125.102.148 \n 158.175.113.22 |
| `Madrid (eu-es)`         | `syslog-tls://syslog-a.eu-es.logging.cloud.ibm.com`    | 13.120.67.126 `(*)`  \n 13.121.68.83 `(*)`  \n 13.122.68.133 `(*)` |
| `Osaka (jp-osa)`         | `syslog-tls://syslog-a.jp-osa.logging.cloud.ibm.com`     | 163.69.67.210   \n 163.68.72.220   \n 163.73.68.45   |
| `Sao Paulo (br-sao)`     | `syslog-tls://syslog-a.br-sao.logging.cloud.ibm.com`     | 169.57.254.118  \n 163.107.68.195  \n 163.109.68.109 |
| `Sydney (au-syd)`        | `syslog-tls://syslog-a.au-syd.logging.cloud.ibm.com`     | 135.90.92.254   \n 168.1.202.76    \n 130.198.1.210  |
| `Tokyo (jp-tok)`         | `syslog-tls://syslog-a.jp-tok.logging.cloud.ibm.com`     | 128.168.95.2    \n 161.202.248.162 \n 165.192.100.77 |
| `Toronto (ca-tor)`       | `syslog-tls://syslog-a.ca-tor.logging.cloud.ibm.com`     | 163.75.66.13    \n 163.74.69.234   \n 169.53.186.154 |
| `Washington (us-east)`   | `syslog-tls://syslog-a.us-east.logging.cloud.ibm.com`    | 169.60.121.243  \n 169.61.98.203   \n 169.47.34.203  |
{: caption="Lists of Syslog-TLS endpoints" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}

### Private syslog TLS endpoints
{: #endpoints_syslog_tls_private}

The following table shows the syslog TLS endpoints:


| Region                 | Public Endpoint                                                | IP addresses                               |
|------------------------|----------------------------------------------------------------|--------------------------------------------|
| `Chennai (in-che)`     | `syslog-tls://syslog-a.private.in-che.logging.cloud.ibm.com`   | 166.9.60.9                                 |
| `Dallas (us-south)`    | `syslog-tls://syslog-a.private.us-south.logging.cloud.ibm.com` | 166.9.16.14 \n 166.9.12.15 \n 166.9.14.5   |
| `Frankfurt (eu-de)`    | `syslog-tls://syslog-a.private.eu-de.logging.cloud.ibm.com`    | 166.9.28.5  \n 166.9.32.23 \n 166.9.30.236 |
| `London (eu-gb)`       | `syslog-tls://syslog-a.private.eu-gb.logging.cloud.ibm.com`    | 166.9.34.18 \n 166.9.36.5  \n 166.9.38.20  |
| `Madrid (eu-es)`       | `syslog-tls://syslog-a.private.eu-es.logging.cloud.ibm.com`    | 166.9.94.34 `(*)`  \n 166.9.95.32 `(*)`  \n 166.9.96.35 `(*)` |
| `Osaka (jp-osa)`       | `syslog-tls://syslog-a.private.jp-osa.logging.cloud.ibm.com`   | 166.9.72.22 \n 166.9.71.22 \n 166.9.70.22  |
| `Sao Paulo (br-sao)`   | `syslog-tls://syslog-a.private.br-sao.logging.cloud.ibm.com`   | 166.9.82.26 \n 166.9.83.22 \n 166.9.84.23  |
| `Sydney (au-syd)`      | `syslog-tls://syslog-a.private.au-syd.logging.cloud.ibm.com`   | 166.9.52.8  \n 166.9.56.22 \n 166.9.54.124 |
| `Tokyo (jp-tok)`       | `syslog-tls://syslog-a.private.jp-tok.logging.cloud.ibm.com`   | 166.9.40.23 \n 166.9.42.26 \n 166.9.44.67  |
| `Toronto (ca-tor)`     | `syslog-tls://syslog-a.private.ca-tor.logging.cloud.ibm.com`   | 166.9.76.31 \n 166.9.78.29 \n 166.9.77.28  |
| `Washington (us-east)` | `syslog-tls://syslog-a.private.us-east.logging.cloud.ibm.com`  | 166.9.22.38 \n 166.9.20.76 \n 166.9.24.243 |
{: caption="Lists of Syslog-TLS endpoints" caption-side="top"}

`(*)` Indicates endpoints that are in plan to be supported.  See [Service IP changes](/docs/log-analysis?topic=log-analysis-service-ip-changes) for planned changes. These endpoints should be added to an allowlist in advance to avoid service interruptions.
{: note}
