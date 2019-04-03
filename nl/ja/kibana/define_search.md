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

# カスタム検索照会の定義
{:#define_search}

「Discover」ページの検索バーで、Lucene 照会言語を使用して検索照会を定義および保存できます。 検索ごとに、フィルターを適用して、分析で使用可能な項目を詳細化できます。
{:shortdesc}

カスタム検索を定義するには、以下のタスクを実行します。

1. Kibana を起動します。

    Cloud Foundry (CF) アプリの場合、『[CF アプリのダッシュボードからの Kibana の起動](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app)』を参照してください。

	{{site.data.keyword.Bluemix_notm}} が管理するインフラストラクチャーで実行しているコンテナーの場合、『[コンテナーのダッシュボードからの Kibana の起動](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers)』を参照してください。
    
    すべてのクラウド・リソース (例えば、Kubernetes クラスターで実行しているコンテナーなど) の場合、『[ブラウザーからの Kibana の起動](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)』を参照してください。 
	
	Kibana にアクセスすると、デフォルト検索が適用されます。 照会しているリソースのインスタンスのリストに関するログを確認できます。 そのスペース内の {{site.data.keyword.Bluemix_notm}} リソースのすべてまたは任意のものについて、ログをフィルタリングできます。

2. 「Discover」ページを見て、表示されているデータのサブセットを確認します。 詳しくは、『[「Discover」ページで表示されているデータの識別](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#identify_data)』を参照してください。 次に、項目をフィルタリングするためのデフォルト照会を変更します。

    **注:** カスタム照会の定義には、Lucene 照会言語を使用します。 詳しくは、『[Apache Lucene - Query Parser Syntax  ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html){: new_window}』を参照してください。
    
    Kibana が {{site.data.keyword.Bluemix_notm}} UI から起動された場合、照会の変更および複数の検索基準の定義のために、論理項 **AND** および **OR** を使用できます。 これらの演算子は、大文字でなければなりません。    
    
    * キーワードまたはその一部を検索するには、語の後にアスタリスク (*) (ワイルドカード) を付けて入力します。例えば、`Java*` などです。 
    * 特定の句を検索するには、その句を二重引用符 (" ") で囲んで入力します。例えば、`"Java/1.8.0"` などです。
    * さらに複雑な検索を作成するには、論理条件の AND および OR を使用できます。例えば、`"Java/1.8.0" OR "Java/1.7.0"` などです。
    * 特定フィールド内の値を検索するには、*log_field_name:search_term* の形式 (例えば、`instance_id:"1"` など) で検索を入力します。
    * 特定ログ・フィールドで一定範囲の値を検索するには、*log_field_name:[start_of_range TO end_of_range]* の形式 (例えば、`instance_id:["1" TO "2"]` など) で検索を入力します。

     例えば、CF アプリの場合、インスタンス *0* および *1* の項目のみがリストされる照会 `application_id:9d222152-8834-4bab-8685-3036cd25931a AND instance_id:["0" TO "1"]` を作成できます。 

3. 照会を保存して、後から再使用できるようにします。 詳しくは、『[検索の保存](/docs/services/CloudLogAnalysis/kibana/define_search.html#save_search1)』を参照してください。 

**注:** 照会を削除する必要がある場合は、『[検索の削除](/docs/services/CloudLogAnalysis/kibana/define_search.html#delete_search)』を参照してください。



## 検索の削除
{: #delete_search}

検索を削除するには、「Settings」ページで以下のステップを実行します。

1. 「Settings」ページで**「Objects」**タブを選択します。

2. **「Searches」**タブで、削除する検索を選択します。

3. **「削除」**をクリックします。


## 検索のエクスポート
{: #export_search}

検索をエクスポートするには、「Settings」ページで以下のステップを実行します。

1. 「Settings」ページで**「Objects」**タブを選択します。

2. **「Searches」**タブで、エクスポートする検索を選択します。

3. **「エクスポート」**をクリックします。

4. ファイルを保存します。

 
## 検索のインポート
{: #import_search}

検索をインポートするには、「Settings」ページで以下のステップを実行します。

1. 「Settings」ページで**「Objects」**タブを選択します。

2. **「Searches」**タブで**「Import」**を選択します。

3. ファイルを選択し、**「Open」**をクリックします。

検索が検索リストに追加されます。

## 検索のコンテンツの最新表示
{: #refresh_search}

検索のコンテンツを手動で最新表示するために、検索バーで使用可能な拡大鏡をクリックできます。 

「Discover」ページで表示されるデータを自動的に最新表示する場合は、最新表示間隔を構成できます。 最新表示間隔の現行値は、「Discover」ページのメニュー・バーに表示されます。 デフォルトでは、自動最新表示は **OFF** に設定されます。

最新表示間隔を設定するには、以下のステップを実行します。

1. 「Discover」ページのメニュー・バーで使用可能な**「Time Filter」**をクリックします。

2. **「Auto Refresh」** ![自動最新表示](images/auto_refresh_icon.jpg "自動最新表示") をクリックします。

3. リストから最新表示間隔を選択します。 

**注**: 自動最新表示間隔を有効にした後には、一時停止ボタン ![一時停止](images/auto_refresh_pause_icon.jpg "一時停止") をクリックすることで、自動最新表示を一時停止できます。


## 検索の再ロード
{: #reload_search1}

保存済み検索をロードするには、以下のステップを実行します。

1. 「Discover」ページのツールバーにある**「Load Search」**ボタン ![検索のロード](images/load_icon.jpg "検索のロード") をクリックします。

2. ロードする検索を選択します。 

## 新規検索の開始
{: #k4_new_search}

新規検索を開始するには、「Discover」ページのツールバーにある**「New Search」**ボタン ![新規検索](images/new_search_icon.jpg "新規検索")をクリックします。

## 検索の保存 
{: #save_search1}

Kibana でのカスタム検索の保存に関する以下の情報を考慮してください。

* 検索を保存すると、検索照会ストリングおよび現在選択されている索引パターンが保存されます。
* *「Discover」*ページで検索を開いて変更する際、同じ名前で保存することを選択するか、または、変更後のカスタム検索を別の名前で保存することができます。 デフォルトでは、提供される検索名は、最初に開いたカスタム検索に対応する名前です。

    * 変更後のカスタム検索を同じ名前で保存するには、**「Save」**をクリックします。 元のカスタム検索が上書きされることに注意してください。 
	
	* 変更後のカスタム検索を別の名前で保存するには、**「Save Search」**フィールドに新しい名前を入力し、**「Save」**をクリックします。 


「Discovery」ページで現在の検索を保存するには、以下のステップを実行します。

1. 「Discover」ページのツールバーにある**「Save Search」**ボタン ![検索の保存](images/save_search_icon.jpg "検索の保存") をクリックします。

2. 検索の名前を入力します。

    **注:** **「Save」**をクリックするときに、上書きについての警告は表示されません。したがって、既存の名前を指定して保存すると、何も示されずにそのバージョンが置換されます。

3. **「保存」**をクリックします。 
