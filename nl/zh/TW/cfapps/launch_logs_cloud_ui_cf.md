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

# 導覽至 Cloud Foundry 應用程式的日誌
{: #launch_logs_cloud_ui_cf}

在 {{site.data.keyword.Bluemix}} 使用者介面中，您可以透過每一個 Cloud Foundry 應用程式都有的日誌標籤或透過 {{site.data.keyword.loganalysisshort}} 服務使用者介面，來檢視、過濾及分析日誌。
{:shortdesc}

若要檢視 CF 應用程式日誌，請考量下列資訊： 

<table>
  <caption>{{site.data.keyword.Bluemix_notm}} 中 CF 應用程式日誌的相關資訊  </caption>
  <tr>
    <th>使用者介面選項</th>
    <th>資訊</th>
  </tr>
  <tr>
    <td>透過 CF 應用程式使用者介面提供的日誌標籤</td>
    <td>可供分析使用的日誌包括過去 24 小時的資料。</td>
  </tr>
  <tr>
    <td>{{site.data.keyword.loganalysisshort}} 儀表板 (Kibana)</td>
    <td>可供分析使用的日誌包括過去 3 天的資料。您也可以指定自訂時段。</td>
  </tr>
</table>


## 透過 CF 應用程式儀表板導覽至 CF 應用程式日誌 
{: #cfapp_ui}

若要查看 Cloud Foundry 應用程式的部署或運行環境日誌，請完成下列步驟：

1. 從「應用程式」儀表板，按一下 Cloud Foundry 應用程式的名稱。 
    
2. 從應用程式詳細資料頁面，按一下**日誌**。
    
    從**日誌**標籤，您可以檢視應用程式的最新日誌，或即時讀取日誌尾端的內容。此外，您還可以依元件（日誌類型）、依應用程式實例 ID 以及依錯誤來過濾日誌。
    
依預設，來自 {{site.data.keyword.Bluemix_notm}} 主控台可供分析的日誌包含過去 24 小時的資料。


## 透過 {{site.data.keyword.loganalysisshort}} 使用者介面導覽至 CF 應用程式日誌 
{: #cfapp_la}

若要查看 Cloud Foundry 應用程式的部署或運行環境日誌，請完成下列步驟：

1. 從「應用程式」儀表板，按一下 Cloud Foundry 應用程式的名稱。 
    
2. 從應用程式詳細資料頁面，按一下**日誌**。
    
3. 按一下**在 Kibana 中檢視**。

依預設，可供分析使用的日誌包括過去 15 分鐘的資料。

**提示：**若要分析自訂時段的資料，請參閱[使用 Kibana 執行進階日誌分析](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#analyzing_logs_Kibana)。 


