---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, network, IP addresses, port

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

 
# 네트워크 트래픽 관리
{: #network}

추가 방화벽을 설정했거나 {{site.data.keyword.cloud_notm}} 인프라에서 방화벽 설정을 사용자 정의한 경우, {{site.data.keyword.la_full_notm}} 서비스에 대한 발신 네트워크 트래팩을 허용해야 합니다. 
{:shortdesc}


## 미국 남부 지역의 사용자 정의 방화벽 구성에 대한 네트워크 트래픽
{: #ips_us-south}

방화벽에서 TCP 포트 443 및 TCP 포트 80에서 발신 트래픽을 허용해야 합니다. 예를 들어, 각 작업자에서 {{site.data.keyword.la_full_notm}} 서비스로 TCP 포트 443 및 TCP 포트 80을 열어야 합니다.

**참고:** API 엔드포인트는 LogDNA 에이전트 인증에 필요합니다. LogDNA 에이전트는 수집 엔드포인트로 로그를 전송하는 데 사용할 수 있는 토큰을 가져옵니다.

다음 표에는 발신 트래픽을 허용하도록 방화벽에서 구성해야 하는 지역별 IP 주소가 나열되어 있습니다.

| 지역      | 수집 엔드포인트                          | 공인 IP 주소               | 포트   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `미국 남부`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="표 1. 로그를 전송할 IP 주소" caption-side="top"}


| 지역      | 인증 엔드포인트                     | 공인 IP 주소               | 포트   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `미국 남부`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="표 2. LogDNA 에이전트에서 사용하는 IP 주소" caption-side="top"}



## 독일 지역의 사용자 정의 방화벽 구성에 대한 네트워크 트래픽
{: #ips_eu-de}

방화벽에서 TCP 포트 443 및 TCP 포트 80에서 발신 트래픽을 허용해야 합니다. 예를 들어, 각 작업자에서 {{site.data.keyword.la_full_notm}} 서비스로 TCP 포트 443 및 TCP 포트 80을 열어야 합니다.

**참고:** API 엔드포인트는 LogDNA 에이전트 인증에 필요합니다. LogDNA 에이전트는 수집 엔드포인트로 로그를 전송하는 데 사용할 수 있는 토큰을 가져옵니다.

다음 표에는 발신 트래픽을 허용하도록 방화벽에서 구성해야 하는 지역별 IP 주소가 나열되어 있습니다.

| 지역      | 수집 엔드포인트                          | 공인 IP 주소               | 포트   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `독일`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="표 3. 로그를 전송할 IP 주소" caption-side="top"}


| 지역      | 인증 엔드포인트                     | 공인 IP 주소               | 포트   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `독일`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="표 4. LogDNA 에이전트에서 사용하는 IP 주소" caption-side="top"}


