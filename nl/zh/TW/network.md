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

 
# 管理網路資料流量
{: #network}

當您已設定其他防火牆時，或您已自訂 {{site.data.keyword.cloud_notm}} 基礎架構中的防火牆設定時，您需要容許網路資料流量送出至 {{site.data.keyword.la_full_notm}} 服務。
{:shortdesc}


## 美國南部地區中自訂防火牆配置的網路資料流量
{: #ips_us-south}

您必須容許在防火牆的 TCP 埠 443 和 TCP 埠 80 上送出資料流量。例如，您必須從每個工作者節點開啟 TCP 埠 443 和 TCP 埠 80，以容許送出資料流量到 {{site.data.keyword.la_full_notm}} 服務。

**附註：**LogDNA 代理程式鑑別需要 API 端點。LogDNA 代理程式會取得一個記號，可用來將日誌傳送至「汲取」端點。

下表列出每個地區中，您必須配置在防火牆中以容許送出資料流量的 IP 位址：

| 地區      | 汲取端點                          | 公用 IP 位址               | 埠   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="表 1. 傳送日誌的 IP 位址" caption-side="top"}


| 地區      | 鑑別端點                     | 公用 IP 位址               | 埠   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="表 2. LogDNA 代理程式使用的 IP 位址" caption-side="top"}



## EU DE 地區中自訂防火牆配置的網路資料流量
{: #ips_eu-de}

您必須容許在防火牆的 TCP 埠 443 和 TCP 埠 80 上送出資料流量。例如，您必須從每個工作者節點開啟 TCP 埠 443 和 TCP 埠 80，以容許送出資料流量到 {{site.data.keyword.la_full_notm}} 服務。

**附註：**LogDNA 代理程式鑑別需要 API 端點。LogDNA 代理程式會取得一個記號，可用來將日誌傳送至「汲取」端點。

下表列出每個地區中，您必須配置在防火牆中以容許送出資料流量的 IP 位址：

| 地區      | 汲取端點                          | 公用 IP 位址               | 埠   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="表 3. 傳送日誌的 IP 位址" caption-side="top"}


| 地區      | 鑑別端點                     | 公用 IP 位址               | 埠   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="表 4. LogDNA 代理程式使用的 IP 位址" caption-side="top"}


