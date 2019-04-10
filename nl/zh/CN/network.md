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

 
# 管理网络流量
{: #network}

如果设置了其他防火墙，或者在 {{site.data.keyword.cloud_notm}} 基础架构中定制了防火墙设置，那么需要允许流至 {{site.data.keyword.la_full_notm}} 服务的出局网络流量。
{:shortdesc}


## 美国南部区域中定制防火墙配置的网络流量
{: #ips_us-south}

必须允许防火墙中 TCP 端口 443 和 TCP 端口 80 上的出局流量。例如，必须打开 TCP 端口 443 和 TCP 端口 80，使流量能从每个工作程序流至 {{site.data.keyword.la_full_notm}} 服务。

**注：**API 端点对于 LogDNA 代理程序认证是必需的。LogDNA 代理程序会获取可用于将日志发送到摄入端点的令牌。

下表列出了针对每个区域必须在防火墙中配置以允许出局流量的 IP 地址：

|区域|摄入端点|公共 IP 地址|端口|
|-------------|---------------------------------------------|-----------------------------------|---------|
|`US South`|logs.us-south.logging.cloud.ibm.com|169.48.237.107</br>169.60.166.45</br>169.47.224.77|TCP 443</br>TCP 80| 
{: caption="表 1. 用于发送日志的 IP 地址" caption-side="top"}


|区域|认证端点|公共 IP 地址|端口|
|-------------|---------------------------------------------|-----------------------------------|---------|
|`US South`|api.us-south.logging.cloud.ibm.com|169.47.224.74</br>169.60.166.44</br>169.48.237.109|TCP 443</br>TCP 80|
{: caption="表 2. LogDNA 代理程序使用的 IP 地址" caption-side="top"}



## EU DE 区域中定制防火墙配置的网络流量
{: #ips_eu-de}

必须允许防火墙中 TCP 端口 443 和 TCP 端口 80 上的出局流量。例如，必须打开 TCP 端口 443 和 TCP 端口 80，使流量能从每个工作程序流至 {{site.data.keyword.la_full_notm}} 服务。

**注：**API 端点对于 LogDNA 代理程序认证是必需的。LogDNA 代理程序会获取可用于将日志发送到摄入端点的令牌。

下表列出了针对每个区域必须在防火墙中配置以允许出局流量的 IP 地址：

|区域|摄入端点|公共 IP 地址|端口|
|-------------|---------------------------------------------|-----------------------------------|---------|
|`EU DE`|logs.eu-de.logging.cloud.ibm.com|161.156.89.11</br>149.81.86.68</br>158.177.129.36|TCP 443</br>TCP 80| 
{: caption="表 3. 用于发送日志的 IP 地址" caption-side="top"}


|区域|认证端点|公共 IP 地址|端口|
|-------------|---------------------------------------------|-----------------------------------|---------|
|`EU DE`|api.eu-de.logging.cloud.ibm.com|161.156.89.12</br>149.81.86.66</br>158.177.129.34|TCP 443</br>TCP 80|
{: caption="表 4. LogDNA 代理程序使用的 IP 地址" caption-side="top"}


