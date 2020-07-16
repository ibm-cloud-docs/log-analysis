---

copyright:
  years:  2018, 2020
lastupdated: "2020-07-02"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# Endpoints
{: #endpoints}

Review the connectivity options for interacting with {{site.data.keyword.la_full}}.
{:shortdesc}



## Connectivity options
{: #connectivity-options}

{{site.data.keyword.la_full_notm}} offers two connectivity options:

<dl>
    <dt>Public endpoints</dt>
        <dd>By default, you can connect to resources in your account over the {{site.data.keyword.cloud_notm}} public network. 
        </dd>
    <dt>Private endpoints</dt>
        <dd>For added benefits, you can also enable <a href="/docs/account?topic=account-vrf-service-endpoint#vrf" target="_blank" class="external"> virtual routing and forwarding (VRF)</a> and <a href="/docs/account?topic=account-vrf-service-endpoint" target="_blank" class="external"> service endpoints</a> for your infrastructure account. When you enable VRF for your account, you can connect to {{site.data.keyword.la_full_notm}} by using a private IP that is accessible only through the {{site.data.keyword.cloud_notm}} private network. To learn more about VRF, see <a href="/docs/dl?topic=dl-overview-of-virtual-routing-and-forwarding-vrf-on-ibm-cloud" target="_blank" class="external">Virtual routing and forwarding on {{site.data.keyword.cloud_notm}}</a>. To learn how to connect to {{site.data.keyword.la_full_notm}} by using a private endpoint, see <a href="/docs/Log-Analysis-with-LogDNA?topic=Log-Analysis-with-LogDNA-service-connection">Securing your connection</a>.
        </dd>
</dl>


## API endpoints
{: #endpoints_api}

### Public API endpoints
{: #endpoints_api_public}

The following table shows the public API endpoints:

| Region                | Public endpoint                             | Public IP addresses                                    | Ports               |
|-----------------------|---------------------------------------------|--------------------------------------------------------|---------------------|
| `Chennai (in-che)`    | `api.in-che.logging.cloud.ibm.com`          | 169.38.82.170                                          | TCP 443 </br>TCP 80 |
| `Dallas (us-south)`   | `api.us-south.logging.cloud.ibm.com`        | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
| `Frankfurt (eu-de)`   | `api.eu-de.logging.cloud.ibm.com`           | 149.81.86.66  </br>161.156.89.12 </br>158.177.129.34   | TCP 443 </br>TCP 80 |
| `London (eu-gb)`      | `api.eu-gb.logging.cloud.ibm.com`           | 158.176.135.132 </br>158.175.82.238 </br>141.125.78.213 | TCP 443 </br>TCP 80 |
| `Seoul (kr-seo)`      | `api.kr-seo.logging.cloud.ibm.com`          | 169.56.70.102                                          | TCP 443 </br>TCP 80 |
| `Sydney (au-syd)`     | `api.au-syd.logging.cloud.ibm.com`          | 130.198.89.43 </br>135.90.70.75 </br>168.1.38.90       | TCP 443 </br>TCP 80 |
| `Tokyo (jp-tok)`      | `api.jp-tok.logging.cloud.ibm.com`          | 165.192.71.226 </br>128.168.70.53 </br>161.202.67.2    | TCP 443 </br>TCP 80 | 
| `Washington (us-east)`| `api.us-east.logging.cloud.ibm.com`         | 169.47.43.67 </br>169.62.55.212 </br>169.60.95.75      | TCP 443 </br>TCP 80 |
{: caption="Table 1. Lists of public API endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}



### Private API endpoints
{: #endpoints_api_private}

The following table shows the private API endpoints:

| Region                   | Private endpoint                                     | Private IP addresses            | Ports               |
|--------------------------|------------------------------------------------------|---------------------------------|---------------------|
| `Chennai (in-che)`       | `https://api.private.in-che.logging.cloud.ibm.com`   | 166.9.60.6                      | TCP 443 </br>TCP 80 |
| `Dallas (us-south)`      | `https://api.private.us-south.logging.cloud.ibm.com` | 166.9.16.11 </br>166.9.12.12 </br>166.9.14.2    | TCP 443 </br>TCP 80 |
| `Frankfurt (eu-de)`      | `https://api.private.eu-de.logging.cloud.ibm.com`    | 166.9.32.7 </br>166.9.28.2      | TCP 443 </br>TCP 80 |
| `London (eu-gb)`         | `https://api.private.eu-gb.logging.cloud.ibm.com`    | 166.9.36.2 </br>166.9.38.4 </br>166.9.34.2     | TCP 443 </br>TCP 80 |
| `Tokyo (jp-tok)`         | `https://api.private.jp-tok.logging.cloud.ibm.com`   | 166.9.42.3 </br>166.9.40.2           | TCP 443 </br>TCP 80 |
| `Seoul (kr-seo)`         | `https://api.private.kr-seo.logging.cloud.ibm.com`   | 166.9.46.5                       | TCP 443 </br>TCP 80 |
| `Sydney (au-syd)`        | `https://api.private.au-syd.logging.cloud.ibm.com`   | 166.9.56.3 </br>166.9.52.2         | TCP 443 </br>TCP 80 | 
| `Washington (us-east)`   | `https://api.private.us-east.logging.cloud.ibm.com`  | 166.9.22.35 </br>166.9.20.72        | TCP 443 </br>TCP 80 |
{: caption="Table 2. Lists of private API endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}





## Ingestion endpoints
{: #endpoints_ingestion}

### Public ingestion endpoints
{: #endpoints_ingestion_public}

The following table shows the ingestion endpoints:

| Region                 | Ingestion endpoint                          | Public IP addresses                                   | Ports               |
|------------------------|---------------------------------------------|-------------------------------------------------------|---------------------|
| `Chennai (in-che)`     | `logs.in-che.logging.cloud.ibm.com`         | 169.38.128.164                                        | TCP 443 </br>TCP 80 |
| `Dallas (us-south)`    | `logs.us-south.logging.cloud.ibm.com`       | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
| `Frankfurt (eu-de)`    | `logs.eu-de.logging.cloud.ibm.com`          | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36   | TCP 443 </br>TCP 80 | 
| `London (eu-gb)`       | `logs.eu-gb.logging.cloud.ibm.com`          | 158.175.125.165 </br>158.176.135.133 </br>141.125.78.186  | TCP 443 </br>TCP 80 | 
| `Seoul (kr-seo)`       | `logs.kr-seo.logging.cloud.ibm.com`         | 169.56.70.98                                          | TCP 443 </br>TCP 80 |
| `Sydney (au-syd)`      | `logs.au-syd.logging.cloud.ibm.com`         | 130.198.89.45 </br>135.90.67.187 </br>168.1.38.92     | TCP 443 </br>TCP 80 |
| `Tokyo (jp-tok)`       | `logs.jp-tok.logging.cloud.ibm.com`         | 165.192.69.122 </br>161.202.93.253 </br>128.168.70.51 | TCP 443 </br>TCP 80 | 
| `Washington (us-east)` | `logs.us-east.logging.cloud.ibm.com`        | 169.61.65.235 </br>169.63.163.51 </br>169.47.52.83    | TCP 443 </br>TCP 80 | 
{: caption="Table 3. Lists of public ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}


### Private ingestion endpoints
{: #endpoints_ingestion_private}

The following table shows the private ingestion endpoints:


| Region                   | Private endpoint                                       | Private IP addresses         | Ports               |
|--------------------------|--------------------------------------------------------|------------------------------|---------------------|
| `Chennai (in-che)`       | `https://logs.private.in-che.logging.cloud.ibm.com`    | 166.9.60.7                    | TCP 443 </br>TCP 80 |
| `Dallas (us-south)`      | `https://logs.private.us-south.logging.cloud.ibm.com`  | 166.9.14.3 </br>166.9.12.13 </br>166.9.16.12    | TCP 443 </br>TCP 80 |
| `Frankfurt (eu-de)`      | `https://logs.private.eu-de.logging.cloud.ibm.com`     | 166.9.28.3 </br>166.9.32.21   | TCP 443 </br>TCP 80 |
| `London (eu-gb)`         | `https://logs.private.eu-gb.logging.cloud.ibm.com`     | 166.9.36.3 </br>166.9.34.4 </br>166.9.38.5       | TCP 443 </br>TCP 80 |
| `Tokyo (jp-tok)`         | `https://logs.private.jp-tok.logging.cloud.ibm.com`    | 166.9.40.3 </br>166.9.42.4      | TCP 443 </br>TCP 80 |
| `Seoul (kr-seo)`         | `https://logs.private.kr-seo.logging.cloud.ibm.com`    | 166.9.46.6                      | TCP 443 </br>TCP 80 |
| `Sydney (au-syd)`        | `https://logs.private.au-syd.logging.cloud.ibm.com`    | 166.9.52.5 </br>166.9.56.20     | TCP 443 </br>TCP 80 |
| `Washington (us-east)`   | `https://logs.private.us-east.logging.cloud.ibm.com`   | 166.9.22.36 </br>166.9.20.73    | TCP 443 </br>TCP 80 |
{: caption="Table 4. Lists of private ingestion endpoints for interacting with {{site.data.keyword.la_full_notm}}" caption-side="top"}




## LogDNA web UI endpoints
{: #endpoints_logdna_ui}

The following table shows the LogDNA web UI endpoints:

| Region                   |  Public Endpoint                                   |
|--------------------------|----------------------------------------------------|
| `Chennai (in-che)`       | `https://app.in-che.logging.cloud.ibm.com`       |
| `Dallas (us-south)`      | `https://app.us-south.logging.cloud.ibm.com`       |
| `Frankfurt (eu-de)`      | `https://app.eu-de.logging.cloud.ibm.com`          |
| `London (eu-gb)`         | `https://app.eu-gb.logging.cloud.ibm.com`          |
| `Tokyo (jp-tok)`         | `https://app.jp-tok.logging.cloud.ibm.com`         |
| `Seoul (kr-seo)`         | `https://app.kr-seo.logging.cloud.ibm.com`         |
| `Sydney (au-syd)`        | `https://app.au-syd.logging.cloud.ibm.com`         |
| `Washington (us-east)`   | `https://app.us-east.logging.cloud.ibm.com`         |
{: caption="Table 5. Lists of LogDNA web UI endpoints" caption-side="top"}



## Syslog public endpoints
{: #endpoints_syslog}

### Syslog endpoints
{: #endpoints_syslog_endpoints}

The following table shows the syslog endpoints:

| Region                   |  Public Endpoint                                   | IP addresses    |
|--------------------------|----------------------------------------------------|-----------------|
| `Chennai (in-che)`       | `syslog://syslog-a.in-che.logging.cloud.ibm.com`   | 169.38.82.173   |
| `Dallas (us-south)`      | `syslog://syslog-a.us-south.logging.cloud.ibm.com` | 169.47.102.26 </br>169.62.255.114 </br>169.47.227.242 |
| `Frankfurt (eu-de)`      | `syslog://syslog-a.eu-de.logging.cloud.ibm.com`    | 158.177.136.58 </br>149.81.96.229 </br>161.156.75.98 |
| `London (eu-gb)`         | `syslog://syslog-a.eu-gb.logging.cloud.ibm.com`    | 158.175.125.163 </br>158.176.135.131 </br>141.125.78.211 |
| `Tokyo (jp-tok)`         | `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`   | 165.192.71.227 </br>161.202.93.250 </br>128.168.91.236 |
| `Seoul (kr-seo)`         | `syslog://syslog-a.kr-seo.logging.cloud.ibm.com`   | 169.56.80.178 |
| `Sydney (au-syd)`        | `syslog://syslog-a.au-syd.logging.cloud.ibm.com`   | 168.1.38.93 </br>130.198.89.46 </br>135.90.70.74 |
| `Washington (us-east)`   | `syslog://syslog-a.us-east.logging.cloud.ibm.com`  | 169.61.109.59 </br>169.47.136.237 </br>169.63.163.50 |
{: caption="Table 6. Lists of Syslog endpoints" caption-side="top"}


### Syslog TLS endpoints
{: #endpoints_syslog_tls}

The following table shows the syslog TLS endpoints:


| Region                   |  Public Endpoint                                         | IP addresses    |
|--------------------------|----------------------------------------------------------|-----------------|
| `Chennai (in-che)`       | `syslog-tls://syslog-a.in-che.logging.cloud.ibm.com`     | 169.38.82.173   |
| `Dallas (us-south)`      | `syslog-tls://syslog-a.us-south.logging.cloud.ibm.com`   | 169.62.255.114  |
| `Frankfurt (eu-de)`      | `syslog-tls://syslog-a.eu-de.logging.cloud.ibm.com`      | 149.81.96.229 </br>158.177.136.58 </br>161.156.75.98 | 
| `London (eu-gb)`         | `syslog-tls://syslog-a.eu-gb.logging.cloud.ibm.com`      | 141.125.78.211 </br>158.176.135.131 </br>158.175.125.163 |
| `Tokyo (jp-tok)`         | `syslog-tls://syslog-a.jp-tok.logging.cloud.ibm.com`     | 128.168.91.236 </br>161.202.93.250 </br>165.192.71.227 |
| `Seoul (kr-seo)`         | `syslog-tls://syslog-a.kr-seo.logging.cloud.ibm.com`     | 169.56.80.178 |
| `Sydney (au-syd)`        | `syslog-tls://syslog-a.au-syd.logging.cloud.ibm.com`     | 168.1.38.93 </br>130.198.89.46 </br>135.90.70.74 |
| `Washington (us-east)`   | `syslog-tls://syslog-a.us-east.logging.cloud.ibm.com`    | 169.47.136.237 </br>169.63.163.50 </br>169.61.109.59 |
{: caption="Table 7. Lists of Syslog-TLS endpoints" caption-side="top"}



