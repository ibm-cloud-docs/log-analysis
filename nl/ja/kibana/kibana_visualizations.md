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

# 視覚化を使用した Kibana でのログの分析 
{:#kibana_visualizations}

ログ・データの分析および結果の比較に使用できるグラフや表などの視覚化を作成するには、Kibana の「*Visualize*」ページを使用します。 
{:shortdesc}

ログを分析するために個別に視覚化を使用できます。 

* 「*Discover*」ページで定義して保存した検索から、または「*Visualize*」ページで定義した新規照会から視覚化を作成できます。 検索により、視覚化で表示されるデータのサブセットを定義します。

* 選択した視覚化のタイプにより、分析用にどのようにデータが表示されるのかが決定します。

以下の表では、各種視覚化タイプをリストします。

| 視覚化タイプ | 説明 |
|-----------------------|-------------|
| Area chart (面グラフ) | グラフィカルに数量データが表示されます。 2 つ以上の集約データ・セットを比較する場合に使用します。 |
| Data table (データ表) | 構成された集約の生データが表形式で表示されます。 |
| Line chart (折れ線グラフ) | 時間ベースのデータが表示されます。 2 つ以上の時間ベースの集約データ・セットを比較する場合に使用します。 |
| Markdown widget (マークダウン・ウィジェット) | テキスト情報を表示する場合に使用します。 |
| Metric (メトリック) | ヒット数、または数値フィールドの平均を表示する場合に使用します。 |
| Pie chart (円グラフ) | 1 つのフィールドの各値を表示する場合に使用します。 | 
| Vertical bar chart (垂直棒グラフ) | 時間ベースのデータおよび時間ベースでないデータが表示されます。 データをグループ化する場合に使用します。 |
{: caption="表 1. 視覚化タイプ" caption-side="top"}

「Visualize」ページで、以下の任意のタスクを実行できます。

| タスク | 詳細情報 |
|------|------------------|
| [新規視覚化の作成](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#create) | 「*Discover*」ページで定義して保存した検索から、または「*Visualize*」ページで定義した新規照会から視覚化を作成できます。 |
| [視覚化の削除](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#delete) | 必要ではない視覚化を削除します。 |
| [視覚化のエクスポート](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#export) | 視覚化を JSON ファイルとしてエクスポートできます。  |
| [視覚化のインポート](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#import1) | 視覚化を JSON ファイルとしてインポートできます。  |
| [視覚化のロード](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#reload2) | 視覚化をアップロードして、そのデータを更新するか、視覚化を変更するか、データを分析できます。 |
| [視覚化の保存](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#save2) | 視覚化を将来再使用するために保存できます。 |
{: caption="表 2. 視覚化を操作するタスク" caption-side="top"}


## Kibana での照会からの視覚化の作成
{: #create}

「Visualize」ページから視覚化を作成するには、以下のステップを実行します。

1. Kibana を起動してから、**「Visualize」**ページを選択します。

2. 視覚化のタイプ (例えば *table*) を選択します。

3. 以前に保存した視覚化を**「Or, From a Saved Search」**から選択するか、または、**「From a New Search, Select Index」**セクションから索引を選択します。

4. 照会を構成します。

    * **「Or, From a Saved Search」**を選択した場合、検索照会を選択します。 照会は、視覚化に使用されるデータを取得するために使用されます。 
	
	    検索を選択すると、視覚化ビルダーが開き、選択した照会のデータがロードされます。 
		
		**注**: 保存済み検索に行った変更はすべて、視覚化で自動的に反映されます。 この視覚化にリンクされた照会に行われる自動更新を無効にするには、「*This visualization is linked to a saved search: your_search_name*」というメッセージをダブルクリックします。 

    * **「From a New Search, Select Index」**を選択した場合、新規照会を定義します。 照会は、視覚化で取得および使用されるデータのサブセットを定義するために使用されます。

        詳しくは、『[カスタム検索照会の定義によるログのフィルタリング](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search)』を参照してください。

Kibana について詳しくは、「[Kibana User Guide ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}」を参照してください。


## 視覚化の削除
{: #delete}

視覚化を削除するには、**「Management」**ページで以下のステップを実行します。

1. **「Management」**ページで、**「Saved Objects」**を選択します。

2. **「Visualizations」**タブで、削除する視覚化を選択します。

3. **「削除」**をクリックします。


## 視覚化のエクスポート
{: #export1}

視覚化を JSON ファイルとしてエクスポートするには、**「Management」**ページで以下のステップを実行します。

1. **「Management」**ページで、**「Saved Objects」**を選択します。

2. **「Visualizations」**タブで、エクスポートする視覚化を選択します。

3. **「エクスポート」**をクリックします。

4. ファイルを保存します。

## 視覚化のインポート
{: #import1}

視覚化を JSON ファイルとしてインポートするには、**「Management」**ページで以下のステップを実行します。

1. **「Management」**ページで、**「Saved Objects」**を選択します。

2. **「Visualizations」**タブで**「Import」**を選択します。

3. ファイルを選択し、**「Open」**をクリックします。

視覚化が視覚化のリストに追加されます。


 
## 視覚化のロード
{: #reload2}

保存済み視覚化をロードするには、以下のステップを実行します。

1. 「Visualize」ページのツールバーで、**「Open」**をクリックします。

2. ロードする視覚化を選択します。 


## 視覚化の保存
{: #save2}

「Visualize」ページで視覚化を保存するには、以下のステップを実行します。

1. 「Visualize」ページのツールバーで、**「Save」**をクリックします。

2. 視覚化の名前を入力します。

3. 「保存」をクリックします。 


