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

# ダッシュボードを使用した Kibana でのログの分析
{:#analize_logs_dashboard}

Kibana の「*Dashboard*」ページを使用して、ダッシュボードでグループ化された視覚化のコレクションを表示します。 ダッシュボードを使用して、ログ・データの分析および結果の比較を行います。
{:shortdesc}

{{site.data.keyword.Bluemix}} では、さまざまなタイプのダッシュボードがあり、それらを定義およびカスタマイズしてデータを視覚化および分析できます。 例えば、以下の表では、一般的なダッシュボード・タイプをいくつかリストします。

| ダッシュボードのタイプ | 説明 |
|-------------------|-------------|
| single-cf-app ダッシュボード | これは、単一の Cloud Foundry アプリケーションの情報を表示するダッシュボードです。 |
| 単一コンテナー・ダッシュボード  | これは、単一のコンテナーの情報を表示するダッシュボードです。  |
| コンテナー・グループ・ダッシュボード  | これは、特定のコンテナー・グループの情報を表示するダッシュボードです。  |
| multi-cf-app ダッシュボード | これは、同じスペースにデプロイされているすべての Cloud Foundry アプリケーションの情報を表示するダッシュボードです。  | 
| 複数コンテナー・ダッシュボード | 同じスペースにデプロイされているすべてのコンテナーの情報を表示するダッシュボードです。  |
| スペース・ダッシュボード | これは、スペースで使用可能なロギング・データを表示するダッシュボードです。  | 
{: caption="表 1. ダッシュボード・タイプのサンプル" caption-side="top"}

ダッシュボードでデータを視覚化するには、パネルを構成します。 Kibana には、さまざまな視覚化 (表、トレンド、ヒストグラムなど) が組み込まれているので、情報を分析するためにそれらを利用できます。 視覚化は、ダッシュボードにパネルとして追加されます。 ダッシュボード内のパネルの追加、削除、並べ替えを行うことができます。 各パネルの目標は異なります。 一部のパネルは、1 つ以上の照会の結果を表す行に編成されています。 その他のパネルは、文書またはカスタム情報を表示します。 各パネルは、検索に基づきます。 検索により、パネルに表示されるデータのサブセットを定義します。 データを視覚化し、分析するために、例えば、棒グラフ、円グラフ、または表を構成することができます。  

以下の表では、「Dashboard」ページで実行できる各種タスクをリストします。

| タスク | 詳細情報 |
|------|------------------|
| [視覚化の追加](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization) | 既存の視覚化または検索をダッシュボードに追加できます。|
| [新規ダッシュボードの作成](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#new) | 複数のダッシュボードを作成できます。 各ダッシュボードは、異なる検索、視覚化、およびログ・データの異なるサブセットを含めるように設計できます。  |
| [ダッシュボードの削除](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#delete) | 必要ではないダッシュボードを削除します。 |
| [ダッシュボードのエクスポート](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#export) | ダッシュボードを JSON ファイルとしてエクスポートできます。 |
| [ダッシュボードのインポート](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#import) | ダッシュボードを JSON ファイルとしてインポートできます。 |
| [ダッシュボードのロード](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#reload3) | ダッシュボードをアップロードして、そのデータを更新するか、ダッシュボードを変更するか、データを分析できます。 |
| [ダッシュボードの保存](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save) | ダッシュボードを将来再使用するために保存できます。 |
{: caption="表 2. ダッシュボードを操作するタスク" caption-side="top"}

Kibana について詳しくは、「[Kibana User Guide ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}」を参照してください。


## 新規検索または視覚化の追加
{: #add_visualization}

既存の視覚化または検索を追加するには、以下のステップを実行します。

1. 「Dashboard」ページのツールバーで、**「追加」** をクリックします。 

    **注**: 視覚化および検索を追加できます。 

2. **「Visualizations」**タブを選択して視覚化を追加するか、**「Searches」**タブを選択して検索を追加します。

3. 追加する検索または視覚化をクリックします。

    その検索または視覚化のパネルがダッシュボードに追加されます。

	
## 新規 Kibana ダッシュボードの作成
{: #new}

新規ダッシュボードを作成するには、以下のステップを実行します。

1. 「Dashboard」ページのツールバーで、**「追加」** をクリックします。 

2. 1 つ以上の検索および視覚化を追加します。 詳しくは、『[新規検索または視覚化の追加](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#add_visualization)』を参照してください。

    検索または視覚化を追加すると、パネルがダッシュボードに追加されます。

3. パネルをドラッグし、ダッシュボード上の配置する部分にドロップします。
 
4. 将来再使用するためにダッシュボードを保存します。 詳しくは、『[Kibana ダッシュボードの保存](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analize_logs_dashboard#save)』を参照してください。


## Kibana ダッシュボードの削除
{: #delete1}

ダッシュボードを削除するには、**「Management」**ページで以下のステップを実行します。

1. **「Management」**ページで、**「Saved Objects」**を選択します。

2. **「Dashboards」**タブで、削除するダッシュボードを選択します。

3. **「削除」**をクリックします。

## Kibana ダッシュボードのエクスポート
{: #export}

ダッシュボードを JSON ファイルとしてエクスポートするには、**「Management」**ページで以下のステップを実行します。

1. **「Management」**ページで、**「Saved Objects」**を選択します。

2. **「Dashboard」**タブで、エクスポートするダッシュボードを選択します。

3. **「エクスポート」**をクリックします。

4. ファイルを保存します。

## Kibana ダッシュボードのインポート
{: #import}

ダッシュボードを JSON ファイルとしてインポートするには、**「Management」**ページで以下のステップを実行します。

1. **「Management」**ページで、**「Saved Objects」**を選択します。

2. **「Dashboard」**タブで**「Import」**を選択します。

3. ファイルを選択し、**「Open」**をクリックします。

ダッシュボードがダッシュボードのリストに追加されます。

## Kibana ダッシュボードのロード
{: #reload3}

保存済みダッシュボードをロードするには、以下のステップを実行します。

1. 「Dashboard」ページのツールバーで、**「Open」** をクリックします。

2. *「Name」*フィールドの下に表示される使用可能なダッシュボードのリストから、いずれかのダッシュボードを選択します。

検索バーでダッシュボードを検索することもできます。

## Kibana ダッシュボードの保存
{: #save}

カスタマイズした Kibana ダッシュボードを保存するには、以下のステップを実行します。

1. ツールバーで、**「Save」**をクリックします。

2. ダッシュボードの名前を入力します。

    **注:** 名前にスペースを使用することはできません。

3. **「保存」**をクリックします。




