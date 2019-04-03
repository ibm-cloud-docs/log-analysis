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

# 定義自訂搜尋查詢
{:#define_search}

您可以在「探索」頁面的搜尋列中，使用 Lucene 查詢語言來定義及儲存搜尋查詢。您可以為每一個搜尋套用過濾器，以精簡可用於分析的項目。
{:shortdesc}

請完成下列作業，以定義自訂搜尋：

1. 啟動 Kibana。

    針對 Cloud Foundry (CF) 應用程式，請參閱[從 CF 應用程式的儀表板啟動 Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_cf_app)。

	針對在 {{site.data.keyword.Bluemix_notm}} 所管理基礎架構中執行的容器，請參閱[從容器的儀表板啟動 Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_for_containers)。
    
    針對所有雲端資源（例如，在 Kubernetes 叢集中執行的容器），請參閱[從瀏覽器啟動 Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-launch#launch_Kibana_from_browser)。 
	
	當您存取 Kibana 時，會套用預設搜尋。您可以在日誌裡查看正在查詢的資源實例清單。您可以針對該空間中的任何或所有 {{site.data.keyword.Bluemix_notm}} 資源過濾日誌。

2. 在「探索」頁面中，查看它顯示哪部分的資料。如需相關資訊，請參閱[識別 Kibana 探索頁面中顯示的資料](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_interactively#identify_data)。然後，修改預設查詢來過濾項目。

    **附註：**請使用 Lucene 查詢語言來定義自訂查詢。如需相關資訊，請參閱 [Apache Lucene - 查詢剖析器語法 ![外部鏈結圖示](../../../icons/launch-glyph.svg "外部鏈結圖示")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}
    
    從 {{site.data.keyword.Bluemix_notm}} 使用者介面啟動 Kibana 時，若要修改查詢以及定義多個搜尋準則，您可以使用邏輯術語 **AND** 及 **OR**。這些運算子必須大寫。    
    
    * 若要搜尋關鍵字或部分關鍵字，請輸入一個單字，後面接著萬用字元星號 (*)，例如 `Java*`。 
    * 若要搜尋特定詞組，請用雙引號 (" ") 輸入該詞組，例如 `"Java/1.8.0"`。
    * 若要建立較複雜的搜尋，您可以使用邏輯術語 AND 和 OR，例如 `"Java/1.8.0" OR "Java/1.7.0"`。
    * 若要搜尋特定欄位中的值，請以下列格式輸入您的搜尋內容：*log_field_name:search_term*，例如 `instance_id:"1"`。
    * 若要搜尋特定日誌欄位中某範圍的值，請以下列格式輸入您的搜尋內容：*log_field_name:[start_of_range TO end_of_range]*，例如 `instance_id:["1" TO "2"]`。

     例如，若為 CF 應用程式，您可以建立查詢 `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]`，此查詢只列出實例 *0* 及 *1* 的項目。 

3. 儲存查詢，以供之後重複使用。如需相關資訊，請參閱[儲存搜尋](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#save_search1)。 

**附註：**如果您需要刪除查詢，請參閱[刪除搜尋](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#delete_search)。



## 刪除搜尋
{: #delete_search}

若要刪除搜尋，請在「設定」頁面中完成下列步驟：

1. 在「設定」頁面中，選取**物件**標籤。

2. 在**搜尋**標籤中，選取您要刪除的搜尋。

3. 按一下**刪除**。


## 匯出搜尋
{: #export_search}

若要匯出搜尋，請在「設定」頁面中完成下列步驟：

1. 在「設定」頁面中，選取**物件**標籤。

2. 在**搜尋**標籤中，選取您要匯出的搜尋。

3. 按一下**匯出**。

4. 儲存檔案。

 
## 匯入搜尋
{: #import_search}

若要匯入搜尋，請在「設定」頁面中完成下列步驟：

1. 在「設定」頁面中，選取**物件**標籤。

2. 在**搜尋**標籤中，選取**匯入**。

3. 選取檔案，然後按一下**開啟**。

該搜尋即會新增至搜尋清單中。

## 重新整理搜尋的內容
{: #refresh_search}

若要手動重新整理搜尋的內容，您可以按一下搜尋列中可用的放大鏡。 

若要自動重新整理「探索」頁面中顯示的資料，您可以配置重新整理間隔。重新整理間隔的現行值會顯示在「探索」頁面的功能表列中。依預設，自動重新整理設定為**關閉**。

請完成下列步驟，以設定重新整理間隔：

1. 在「探索」頁面中，按一下功能表列中可用的**時間過濾器**。

2. 按一下**自動重新整理** ![自動重新整理](images/auto_refresh_icon.jpg "自動重新整理")。

3. 從清單中選擇重新整理間隔。 

**附註**：啟用自動重新整理間隔之後，您可以按一下「暫停」按鈕 ![暫停](images/auto_refresh_pause_icon.jpg "暫停") 來將它暫停。


## 重新載入搜尋
{: #reload_search1}

請完成下列步驟，以載入已儲存的搜尋：

1. 在「探索」頁面的工具列中，按一下**載入搜尋**按鈕 ![載入搜尋](images/load_icon.jpg "載入搜尋")。

2. 選取您要載入的搜尋。 

## 開始新搜尋
{: #k4_new_search}

若要開始新搜尋，請按一下「探索」頁面工具列中的**新搜尋**按鈕 ![新搜尋](images/new_search_icon.jpg "新搜尋")。

## 儲存搜尋 
{: #save_search1}

請考量下列有關在 Kibana 中儲存自訂搜尋的資訊：

* 當您儲存搜尋時，會儲存搜尋查詢字串及目前選取的索引型樣。
* 當您在*探索* 頁面中開啟並修改搜尋時，可以選擇使用相同的名稱來儲存它，也可以使用不同的名稱來儲存修改過的自訂搜尋。依預設，所提供的搜尋名稱就是對應於您一開始所開啟之自訂搜尋的名稱。

    * 若要使用相同的名稱來儲存修改過的自訂搜尋，請按一下**儲存**。請注意，會改寫原始自訂搜尋。 
	
	* 若要使用不同的名稱來儲存修改過的自訂搜尋，請在**儲存搜尋**欄位中輸入新名稱，然後按一下**儲存**。 


請完成下列步驟，以在「探索」頁面中儲存目前的搜尋：

1. 在「探索」頁面的工具列中，按一下**儲存搜尋**按鈕 ![儲存搜尋](images/save_search_icon.jpg "儲存搜尋")。

2. 輸入搜尋的名稱。

    **附註：**當您按一下**儲存**時，不會有改寫的警告，因此，如果您指定現有名稱，則儲存會取代該版本，而沒有任何指示。

3. 按一下**儲存**。 
