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

# 在 Kibana 中透過儀表板來分析日誌
{:#analize_logs_dashboard}

使用 Kibana 中的*儀表板* 頁面，來顯示分組成各儀表板的視覺效果集合。使用儀表板來分析您的日誌資料並比較結果。
{:shortdesc}

在 {{site.data.keyword.Bluemix}} 中有不同類型的儀表板，您可以定義與自訂以視覺化及分析資料。例如，下表列出一些常見的儀表板類型：

|儀表板類型 |說明 |
|-------------------|-------------|
|單一 CF 應用程式儀表板|此儀表板會顯示單一 Cloud Foundry 應用程式的資訊。|
|單一容器儀表板 |此儀表板會顯示單一容器的資訊。|
|容器群組儀表板 |此儀表板會顯示特定容器群組的資訊。|
|多 CF 應用程式儀表板|此儀表板會顯示部署在相同空間中的所有 Cloud Foundry 應用程式的資訊。| 
|多容器儀表板|此儀表板會顯示部署在相同空間中的所有容器的資訊。|
|空間儀表板 |此儀表板會顯示空間中可用的記載資料。| 
{: caption="表 1. 儀表板類型範例" caption-side="top"}

若要將儀表板中的資料視覺化，您可以配置畫面。Kibana 包括可用來分析資訊的各種視覺效果，例如表格、趨勢及直方圖。視覺效果會以畫面形式新增至儀表板。您可以新增、移除及重新排列儀表板中的畫面。每一個畫面的目標都不同。部分畫面會組織成數列，以提供一個以上查詢的結果。其他畫面則會顯示文件或自訂資訊。每一個畫面都以搜尋為基礎。搜尋會定義畫面顯示的部分資料。例如，您可以配置長條圖、圓餅圖或表格，以將資料視覺化，並進行分析。  

下表列出您可以在「儀表板」頁面中執行的各種作業：

|作業 |相關資訊 |
|------|------------------|
|[新增視覺效果](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization) |您可以將現有視覺效果或搜尋新增至儀表板。|
|[建立新的儀表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#new) |您可以建立多個儀表板。每一個儀表板都可以設計為包括不同的搜尋、視覺效果，以及不同部分的日誌資料。|
|[刪除儀表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#delete) |刪除不需要的儀表板。|
|[匯出儀表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#export) |您可以將儀表板匯出成 JSON 檔案。|
|[匯入儀表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#import) |您可以將儀表板匯入成 JSON 檔案。|
|[載入儀表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#reload3) |您可以上傳儀表板，以更新其資料、予以修改或分析資料。|
|[儲存儀表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save) |您可以儲存儀表板，以供之後重複使用。|
{: caption="表 2. 使用儀表板的作業" caption-side="top"}

如需 Kibana 的相關資訊，請參閱 [Kibana User Guide ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}。


## 新增搜尋或視覺效果
{: #add_visualization}

請完成下列步驟，以新增現有視覺效果或搜尋：

1. 在「儀表板」頁面的工具列中，按一下**新增**。 

    **附註**：您可以新增視覺效果及搜尋。 

2. 選取**視覺效果**標籤，以新增視覺效果，或選取**搜尋**標籤，以新增搜尋。

3. 按一下您要新增的搜尋或視覺效果。

    該搜尋或視覺效果的畫面即會新增至儀表板。

	
## 建立新的 Kibana 儀表板
{: #new}

請完成下列步驟，以建立新的儀表板：

1. 在「儀表板」頁面的工具列中，按一下**新增**。 

2. 新增一個以上的搜尋及視覺效果。如需相關資訊，請參閱[新增搜尋或視覺效果](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization)。

    當您新增搜尋或視覺效果時，會在儀表板中新增畫面。

3. 將畫面拖放在您要放置的儀表板部分。
 
4. 儲存儀表板，以供日後重複使用。如需相關資訊，請參閱[儲存 Kibana 儀表板](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save)。


## 刪除 Kibana 儀表板
{: #delete1}

若要刪除儀表板，請在**管理**頁面中完成下列步驟：

1. 在**管理**頁面中，選取**已儲存的物件**。

2. 在**儀表板**標籤中，選取您要刪除的儀表板。

3. 按一下**刪除**。

## 匯出 Kibana 儀表板
{: #export}

若要將儀表板匯出成 JSON 檔案，請在**管理**頁面中完成下列步驟：

1. 在**管理**頁面中，選取**已儲存的物件**。

2. 在**儀表板**標籤中，選取您要匯出的儀表板。

3. 按一下**匯出**。

4. 儲存檔案。

## 匯入 Kibana 儀表板
{: #import}

若要將儀表板匯入成 JSON 檔案，請在**管理**頁面中完成下列步驟：

1. 在**管理**頁面中，選取**已儲存的物件**。

2. 在**儀表板**標籤中，選取**匯入**。

3. 選取檔案，然後按一下**開啟**。

該儀表板即會新增至儀表板清單中。

## 載入 Kibana 儀表板
{: #reload3}

請完成下列步驟，以載入已儲存的儀表板：

1. 在「儀表板」頁面的工具列中，按一下**開啟**。

2. 從*名稱* 欄位下所顯示的可用儀表板清單中，選取儀表板。

您也可以從「搜尋」列中搜尋儀表板。

## 儲存 Kibana 儀表板
{: #save}

請完成下列步驟，以在自訂 Kibana 儀表板之後予以儲存：

1. 在工具列中，按一下**儲存**。

2. 輸入儀表板的名稱。

    **附註：**名稱不得包含空格。

3. 按一下**儲存**。




