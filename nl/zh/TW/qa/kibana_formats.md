---

copyright:
  years: 2017, 2019

lastupdated: "2019-03-06"

keywords: IBM Cloud, logging

subcollection: cloudloganalysis

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

# Kibana 日誌格式
{: #kibana_formats}

您可以配置 Kibana，以在*探索* 頁面中顯示每一個日誌項目的不同欄位。
{:shortdesc}



## Cloud Foundry 應用程式的 Kibana 日誌格式
{: #kibana_log_format_cf}

您可以配置 Kibana，以在*探索* 頁面顯示每一個日誌項目的下列欄位：


|欄位 |說明 |
|-------|-------------|
|@timestamp |`yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> 所記載事件的時間。<br> 時間戳記最多定義到毫秒。|
|@version |事件的版本。|
|ALCH_TENANT_ID |{{site.data.keyword.Bluemix_notm}} 空間的 ID。|
|\_id |日誌文件的唯一 ID。|
|\_index |日誌項目的索引。|
|\_type |日誌類型；例如 *syslog*。|
|app_name|應用程式的名稱。|
|application_id |應用程式的唯一 ID。|
|host |產生日誌資料之應用程式的名稱。|
|instance_id |產生日誌資料之應用程式實例的實例 ID。|
|loglevel |所記載事件的嚴重性。|
|message |元件所發出的訊息。<br> 訊息會視環境定義而改變。|
|message_type |將日誌訊息寫入其中的串流。<br> * **OUT** 是指 stdout 串流。<br> * **ERR** 是指 stderr 串流。|
|org_id |{{site.data.keyword.Bluemix_notm}} 組織的唯一 ID。|
|org_name |應用程式編譯打包所在之 {{site.data.keyword.Bluemix_notm}} 組織的名稱。|
|origin |產生事件的元件。|
|source_id |產生日誌的元件。<br> 下列清單說明來自各元件的日誌：<br> * **API**：針對要求變更應用程式狀態之 API 呼叫所記載的回應。<br> * **APP**：已記載的應用程式回應。<br> * **CELL**：已記載的 Diego Cell 回應，指出應用程式啟動、停止或當機的時間。<br> * **LGR**：已記載的日誌聚集器回應，指出記載程序的問題。<br> * **RTR**：當路由器將 HTTP 要求遞送至應用程式時，已記載的路由器回應。<br> * **SSH**：當使用者使用 `cf ssh` 指令來存取應用程式容器時，已記載的 Diego Cell 回應。<br> * **STG**：將應用程式編譯打包或重新編譯打包時，已記載的 Diego Cell 或 Droplet Execution Agent 回應。|
|space_name |應用程式編譯打包所在之 {{site.data.keyword.Bluemix_notm}} 空間的名稱。|
|timestamp |所記載事件的時間。時間戳記最多定義到毫秒。|
{: caption="表 1. CF 應用程式的欄位" caption-side="top"}



## Kubernetes 叢集中所部署 Docker 容器的 Kibana 日誌格式
{: #kibana_log_format_containers_kubernetes}

您可以配置 Kibana，以在*探索* 頁面中顯示每一個日誌項目的下列欄位。這些欄位由 {{site.data.keyword.IBM}} 所設定，並且包括您的訊息資料。 

|欄位 |說明 |其他資訊|
|-------|-------------|---------------------------|
|@timestamp |`yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> 所記載事件的時間。<br> 時間戳記最多定義到毫秒。| |
|@version |事件的版本。| |
|ALCH_TENANT_ID |{{site.data.keyword.Bluemix_notm}} 空間的 ID。| |
|\_id |日誌文件的唯一 ID。| |
|\_index |日誌項目的索引。| |
|\_score |  |  |
|\_type |日誌類型；例如 *logs*。| |
|crn_str |日誌來源的相關資訊。|依預設，此欄位由 {{site.data.keyword.IBM_notm}} 設定。<br> **附註**：如果您以有效的 JSON 格式傳送日誌訊息，而且其中一個欄位命名為 `crn`，則會將欄位的值改寫為訊息中所設定的值。|  
|docker.container_id_str |Pod 中所執行容器的 GUID。| |
|ibm-containers.account_str |{{site.data.keyword.Bluemix_notm}} 帳戶的 GUID。|  |
|ibm-containers.cluster_id_str |Kubernetes 叢集的 GUID。|  |
|ibm-containers.cluster_type_str |  |保留供 {{site.data.keyword.IBM_notm}} 內部使用的值。|
|ibm-containers.region_str |{{site.data.keyword.Bluemix_notm}} 中的地區。|  |
|kubernetes.container_name_str |應用程式部署所在容器的名稱。|  |
|kubernetes.host |容器執行所在工作者節點的公用 IP 位址。|  |
|kubernetes.labels.*example_label_name*\_str |附加至 Kubernetes 物件（例如 Pod）的金鑰值組。|每一個附加至 Kubernetes 物件的標籤都會列為 Kibana 中所顯示日誌項目中的欄位。<br> 您可以有 0 個以上的標籤。|
|kubernetes.namespace_name_str |容器部署所在的 Kubernetes 名稱空間|  |
|kubernetes.pod_id_str |容器部署所在 Pod 的 GUID。|  |
|kubernetes.pod_name_str |Pod 的名稱。|  |
|message |完整訊息。|如果您傳送有效的 JSON 格式化訊息，則會個別剖析每一個欄位，並將其顯示在 Kibana 中。|
|stream_str |  |保留供 {{site.data.keyword.IBM_notm}} 內部使用的值。|
|tag_str |  |保留供 {{site.data.keyword.IBM_notm}} 內部使用的值。|
{: caption="表 3. Docker 容器的欄位" caption-side="top"}


## Message Hub 的 Kibana 日誌格式
{: #kibana_log_format_messagehub}

您可以配置 Kibana，以在*探索* 頁面顯示每一個日誌項目的下列欄位：


|欄位 |說明 |
|-------|-------------|
|@timestamp |`yyyy-MM-ddTHH:mm:ss:SS-0500`  <br> 所記載事件的時間。<br> 時間戳記最多定義到毫秒。|
|@version |事件的版本。|
|ALCH_TENANT_ID |{{site.data.keyword.Bluemix_notm}} 空間的 ID。|
|\_id |日誌文件的唯一 ID。|
|\_index |日誌項目的索引。|
|\_type |日誌類型；例如 *syslog*。|
|loglevel |所記載事件的嚴重性，例如 **Info**。|
|module |此欄位設為 **MessageHub**。|
{: caption="表 4. Message Hub 事件的欄位" caption-side="top"}

日誌項目的範例：

```
March 8th 2017, 17:15:16.454	

message:
    Creating topic ABC
@version:
    1
@timestamp:
    March 8th 2017, 17:15:16.454
loglevel:
    Info
module:
    MessageHub
ALCH_TENANT_ID:
    3d8d2eae-f3f0-44f6-9717-126113a00b51
&#95;id:
    AVqu6vJl1zcfr8KYMI95
&#95;type:
    logs
&#95;index:
    logstash-2017.03.08
```
{: screen}


