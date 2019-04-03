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

# 在 Kibana 中使用視覺效果來分析日誌 
{:#kibana_visualizations}

請利用 Kibana 中的*視覺化* 頁面來建立圖形及表格等視覺效果，讓您可以用來分析日誌資料及比較結果。
{:shortdesc}

您可以個別使用視覺效果來分析日誌。 

* 您可以從您定義並儲存在*探索* 頁面中的搜尋來建立視覺效果，也可以從您在*視覺化* 頁面中定義的新查詢來建立視覺效果。搜尋會定義視覺效果顯示的部分資料。

* 您選擇的視覺效果類型，會決定顯示資料以進行分析的方式。

下表列出不同的視覺效果類型：

|視覺效果類型|說明 |
|-----------------------|-------------|
|區域圖 |以圖形方式顯示定量資料。可用來比較兩組以上的聚集資料。|
|資料表 |針對組合的聚集，以表格方式顯示原始資料。|
|折線圖 |顯示時間型資料。可用來比較兩組以上的時間型聚集資料。|
|Markdown 小組件 |可用來顯示文字資訊。|
|度量值 |可用來顯示相符數，或是數值欄位的確切平均值。|
|圓餅圖 |可用來顯示欄位的不同值。| 
|垂直長條圖 |顯示時間型資料，以及非時間型資料。可用來將資料分組。|
{: caption="表 1. 視覺效果類型" caption-side="top"}

在「視覺化」頁面中，您可以執行下列任何作業：

|作業 |相關資訊 |
|------|------------------|
|[建立新的視覺效果](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#create) |您可以從您定義並儲存在*探索* 頁面中的搜尋來建立視覺效果，也可以從您在*視覺化* 頁面中定義的新查詢來建立視覺效果。|
|[刪除視覺效果](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#delete) |刪除不需要的視覺效果。|
|[匯出視覺效果](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#export) |您可以將視覺效果匯出成 JSON 檔案。|
|[匯入視覺效果](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#import1) |您可以將視覺效果匯入成 JSON 檔案。|
|[載入視覺效果](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#reload2) |您可以上傳視覺效果，以更新其資料、予以修改或分析資料。|
|[儲存視覺效果](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#save2) |您可以儲存視覺效果，以供之後重複使用。|
{: caption="表 2. 使用視覺效果的作業" caption-side="top"}


## 在 Kibana 中從查詢建立視覺效果
{: #create}

請完成下列步驟，以從「視覺化」頁面中建立視覺效果：

1. 啟動 Kibana，然後選取**視覺化**頁面。

2. 選擇視覺效果類型，例如，*表格*。

3. 在**或者，從已儲存的搜尋**中選取您先前儲存的視覺效果，或在**從新的搜尋，選取索引**區段中選取索引。

4. 配置查詢。

    * 如果您選取**或者，從已儲存的搜尋**，請選取搜尋查詢。此查詢用來擷取用於視覺效果的資料。 
	
	    選取搜尋之後，視覺效果建置器即會開啟，並針對選取的查詢載入資料。 
		
		**附註**：您對已儲存的搜尋所做的任何變更，會自動反映在視覺效果中。若要停用您對鏈結至此視覺效果的查詢所進行的自動更新，請按兩下此訊息：*此視覺效果鏈結至已儲存的搜尋：your_search_name*。 

    * 如果您選取**從新的搜尋，選取索引**，請定義新的查詢。此查詢用來定義視覺效果所擷取及使用的部分資料。

        如需相關資訊，請參閱[透過定義自訂查詢過濾日誌](/docs/services/CloudLogAnalysis/kibana/define_search.html#define_search)。

如需 Kibana 的相關資訊，請參閱 [Kibana User Guide ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}。


## 刪除視覺效果
{: #delete}

若要刪除視覺效果，請在**管理**頁面中完成下列步驟：

1. 在**管理**頁面中，選取**已儲存的物件**。

2. 在**視覺效果**標籤中，選取您要刪除的視覺效果。

3. 按一下**刪除**。


## 匯出視覺效果
{: #export1}

若要將視覺效果匯出成 JSON 檔案，請在**管理**頁面中完成下列步驟：

1. 在**管理**頁面中，選取**已儲存的物件**。

2. 在**視覺效果**標籤中，選取您要匯出的視覺效果。

3. 按一下**匯出**。

4. 儲存檔案。

## 匯入視覺效果
{: #import1}

若要將視覺效果匯入成 JSON 檔案，請在**管理**頁面中完成下列步驟：

1. 在**管理**頁面中，選取**已儲存的物件**。

2. 在**視覺效果**標籤中，選取**匯入**。

3. 選取檔案，然後按一下**開啟**。

該視覺效果即會新增至視覺效果清單中。


 
## 載入視覺效果
{: #reload2}

請完成下列步驟，以載入已儲存的視覺效果：

1. 在「視覺化」頁面的工具列中，按一下**開啟**。

2. 選取您要載入的視覺效果。 


## 儲存視覺效果
{: #save2}

請完成下列步驟，以在「視覺化」頁面中儲存視覺效果：

1. 在「視覺化」頁面的工具列中，按一下**儲存**。

2. 輸入視覺效果的名稱。

3. 按一下「儲存」。 


