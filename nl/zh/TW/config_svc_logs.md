---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# 配置 {{site.data.keyword.cloud_notm}} 服務日誌
{: #config_svc_logs}

您可以在一個地區中具有多個 {{site.data.keyword.la_full_notm}} 實例。不過，一個地區中僅有 1 個實例可以配置為從 {{site.data.keyword.cloud_notm}} 中的已啟用服務接收日誌。
{:shortdesc}



## 透過觀察儀表板配置平台服務日誌
{: #config_svc_logs_ui}

若要從 {{site.data.keyword.cloud_notm}} 中的「觀察」儀表板配置實例，請完成下列步驟：

1. [登入 {{site.data.keyword.cloud_notm}} 帳戶 ![外部鏈結圖示](../../icons/launch-glyph.svg "外部鏈結圖示")](https://cloud.ibm.com/login){:new_window}。

	使用您的使用者 ID 和密碼登入之後，即會開啟 {{site.data.keyword.cloud_notm}} 使用者介面。

2. 移至功能表圖示 ![功能表圖示](../../icons/icon_hamburger.svg)。然後，選取**觀察**，以存取*觀察* 儀表板。

3. 選取**記載**，然後按一下**配置平台服務日誌**。 

4. 選擇哪個 LogDNA 實例將從雲端平台上的已啟用服務接收日誌。

5. 選取地區。 

6. 選取實例。

7. 按一下**儲存**。 

即會開啟主要*觀察* 頁面。

您選擇來接收服務日誌的實例會顯示旗標**平台服務日誌**。

如需啟用以傳送日誌至 {{site.data.keyword.la_full_notm}} 之服務的相關資訊，請參閱[雲端服務](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services)。

