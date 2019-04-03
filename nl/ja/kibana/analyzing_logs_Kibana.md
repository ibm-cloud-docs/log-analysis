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

# ログの表示と分析 (Kibana)
{:#analyzing_logs_Kibana}

分析および視覚化のためのオープン・ソース・プラットフォームである Kibana 5.1 を使用して、さまざまなグラフ (図表や表など) でデータのモニター、検索、分析、および視覚化を行うことができます。 高機能な分析タスクを実行するには、Kibana を使用してください。
{:shortdesc}

Kibana はブラウザー・ベースのインターフェースであり、データを対話式に分析したり、ダッシュボードをカスタマイズしてから使用することで、ログ・データを分析し、高機能な管理タスクを実行したりすることができます。 詳しくは、「[Kibana User Guide ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}」を参照してください。

Kibana ページで表示されるデータは、検索によって制限されます。 デフォルトのデータ・セットは、事前構成された索引パターンによって定義されています。 情報をフィルタリングするために、新しい検索照会を追加し、フィルターをデフォルトのデータ・セットに適用できます。 その後、その検索を将来の再使用のために保存できます。 

Kibana には、ログの分析に使用できる、以下のような各種ページが含まれています。

| Kibana ページ | 説明 |
|-------------|-------------|
| Discover | このページは、検索を定義し、表およびヒストグラムでログを対話式に分析する場合に使用します。 |
| Visualize | このページは、ログ・データの分析および結果の比較に使用できるグラフや表などの視覚化を作成する場合に使用します。  |
| ダッシュボード | このページは、保存済みの視覚化および検索のコレクションを介してログを分析する場合に使用します。  |
{: caption="表 1. Kibana ページ" caption-side="top"}

**注:** 「Visualize」ページまたは「Dashboard」ページで一度に分析できる期間は丸 1 日だけです。ただし、3 日遡ることができます。 ログ・データはデフォルトで 3 日間保管されます。 

| Kibana ページ | 期間の情報 |
|-------------|-------------------------|
| Discover | 最大 3 日分のデータを分析します。 |
| Visualize | 24 時間の期間のデータを分析します。 <br> 24 時間のカスタム期間のログ・データをフィルタリングできます。  |
| ダッシュボード | 24 時間の期間のデータを分析します。 <br> 24 時間のカスタム期間のログ・データをフィルタリングできます。 <br> 設定した時間ピッカーは、ダッシュボードに含まれているすべての視覚化に適用されます。 |
{: caption="表 2. 期間の情報" caption-side="top"}

例えば、以下のように、Kibana を使用して、各ページでスペース内の CF アプリまたはコンテナーに関する情報を表示できます。

## Kibana ダッシュボードへのナビゲート
{: #launch_Kibana}

Kibana は以下のどの方法でも起動できます。

* {{site.data.keyword.loganalysisshort}} サービス・ダッシュボードから

    Kibana を起動して、用意されているスペース内のサービスのログを、表示データで集約することができます。
	
	詳しくは、『[Log Analysis サービスのダッシュボードから Kibana へのナビゲート](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_log_analysis)』を参照してください。

* {{site.data.keyword.Bluemix_notm}} から

    特定の CF アプリのコンテキストにおいて、そのログが Kibana に表示されるようにすることで Kibana を起動できます。 詳しくは、『[CF アプリのダッシュボードから Kibana へのナビゲート](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_cf_app)』を参照してください。
    
    特定の Docker コンテナーのコンテキストにおいて、そのログが Kibana に表示されるようにすることで Kibana を起動できます。 この機能は、{{site.data.keyword.Bluemix_notm}} が管理するインフラストラクチャーにデプロイされたコンテナーにのみ適用されます。 詳しくは、『[コンテナーのダッシュボードから Kibana へのナビゲート](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_for_containers)』を参照してください。
    
    CF アプリでは、Kibana で分析に使用できるデータをフィルタリングするために使用される照会により、Cloud Foundry アプリケーションのログ項目を取得します。 Kibana にデフォルトで表示されるログ情報は、単一の Cloud Foundry アプリケーションとそのすべてのインスタンスに関連するすべてです。 
    
    コンテナーでは、Kibana で分析に使用できるデータをフィルタリングするために使用される照会により、コンテナーのすべてのインスタンスのログ項目を取得します。 Kibana にデフォルトで表示されるログ情報は、単一コンテナーまたはコンテナー・グループおよびそのすべてのインスタンスに関連するすべてです。 
    
    

* ブラウザーの直接リンクから

    Kibana を起動し、表示されるデータで、提供されているスペース内のサービスからのログを集約するようにすることができます。
    
    ダッシュボードに表示されるデータをフィルター操作するために使用される照会によって、{{site.data.keyword.Bluemix_notm}} 組織内のスペースのログ項目が取り出されます。 Kibana に表示されるログ情報には、ログインしている {{site.data.keyword.Bluemix_notm}} 組織のスペース内にデプロイされているすべてのリソースに関するレコードが含まれます。 
    
    詳しくは、『[Web ブラウザーから Kibana ダッシュボードへのナビゲート](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)』を参照してください。
    
    

## データの対話式分析
{: #analyze_discover}

「Discover」ページで、新規検索照会を定義し、照会ごとにフィルターを適用します。 ログ・データは、表およびヒストグラムで表示されます。 これらの視覚化を使用して、データを対話式に分析できます。 詳しくは、『[Kibana でのログの対話式分析](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#analize_logs_interactively)』を参照してください。

ログ・フィールド (例: message_type や instance_ID) からフィルターを構成したり、期間を設定したりすることができます。 これらのフィルターを動的に有効または無効にすることができます。 有効にした照会およびフィルターの基準に一致するログ項目が表やヒストグラムに表示されます。 詳しくは、『[Kibana でのログのフィルタリング](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#filter_logs)』を参照してください。

## 視覚化を通じたデータの分析
{: #analyze_visualize}
    
「Visualize」ページで、新規検索照会および視覚化を定義します。 保存された視覚化を開いたり、視覚化を保存したりもできます。

データを分析するために、既存の検索または新規検索に基づいて、視覚化を作成できます。 Kibana には、さまざまなタイプの視覚化 (表、トレンド、ヒストグラムなど) が組み込まれているので、情報を分析するためにそれらを利用できます。 各視覚化の目標は異なります。 一部の視覚化は、1 つ以上の照会の結果を表す行に編成されています。 文書またはカスタム情報を表示する視覚化もあります。 視覚化のデータは、検索照会を更新して、修正または変更できます。 視覚化を Web ページに埋め込んだり、共有したりすることができます。 

詳しくは、『[視覚化を使用したログの分析](/docs/services/CloudLogAnalysis/kibana/kibana_visualizations.html#kibana_visualizations)』を参照してください。

## ダッシュボードでのデータの分析
{: #analyze_dashboard}

「Dashboard」ページでは、複数の視覚化および検索を同時にカスタマイズ、保存、および共有できます。 

ダッシュボード内の視覚化の追加、削除、並べ替えを行うことができます。 詳しくは、『[ダッシュボードを使用した Kibana でのログの分析](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#analize_logs_dashboard)』を参照してください。
    
Kibana ダッシュボードをカスタマイズした後、その視覚化を使用してデータを分析し、将来再使用するために保存できます。 詳しくは、『[Kibana ダッシュボードの保存](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save)』を参照してください。

## Kibana のカスタマイズ
{: #analyze_management}

**「Management」**ページから、Kibana リソースを構成および管理することもできます。 

以下の任意のタスクを実行できます。

* 検索の保存、削除、エクスポート、およびインポート。 
* 視覚化の保存、削除、エクスポート、およびインポート。
* ダッシュボードの保存、削除、エクスポート、およびインポート。
* [フィールド・リストの最新表示](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)。

## 制限
{: #limitations}

Kibana で視覚化またはダッシュボードを共有できるのは、同じ組織またはアカウントのメンバーのみです。

以下の Kibana 機能はサポートされません。

* 検索の共有。
* 新しい索引パターンの作成。 


## ログを表示するユーザーに必要な役割
{: #roles}

{{site.data.keyword.Bluemix_notm}} では、ユーザーに 1 つ以上の役割を割り当てることができます。 これらの役割は、{{site.data.keyword.loganalysisshort}} サービスを使用して作業するためにユーザーが使用できるタスクを定義します。 

以下の表は、ログを表示するために必要なユーザーの役割を示します。

<table>
  <caption>ログを表示するために**アカウント所有者**に必要な許可</caption>
  <tr>
    <th>アクション</th>
	<th>CF スペースの役割</th>
	<th>CF 組織の役割</th>
	<th>IAM 役割</th>
  </tr>
  <tr>
    <td>スペース・ドメイン内のログを表示する</td>
	<td>*管理者* </br>*開発者* </br>*監査員*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>アカウント・ドメイン内のログを表示する</td>
	<td></td>
	<td></td>
	<td>*管理者*</td>
  </tr>
  <tr>
    <td>組織ドメイン内のログを表示する</td>
	<td></td>
	<td>*管理者* </br>*請求管理者*  </br>*監査員*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>ログを表示するために**監査員**に必要な許可</caption>
  <tr>
    <th>アクション</th>
	<th>CF スペースの役割</th>
	<th>CF 組織の役割</th>
	<th>IAM 役割</th>
  </tr>
  <tr>
    <td>スペース・ドメイン内のログを表示する</td>
	<td>*監査員*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>アカウント・ドメイン内のログを表示する</td>
	<td></td>
	<td></td>
	<td>*ビューアー*</td>
  </tr>
  <tr>
    <td>組織ドメイン内のログを表示する</td>
	<td></td>
	<td>*監査員*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>ログを表示するために**管理者**に必要な許可</caption>
  <tr>
    <th>アクション</th>
	<th>CF スペースの役割</th>
	<th>CF 組織の役割</th>
	<th>IAM 役割</th>
  </tr>
  <tr>
    <td>スペース・ドメイン内のログを表示する</td>
	<td>*開発者*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>アカウント・ドメイン内のログを表示する</td>
	<td></td>
	<td></td>
	<td>*ビューアー*</td>
  </tr>
  <tr>
    <td>組織ドメイン内のログを表示する</td>
	<td></td>
	<td>*管理者*</td>
	<td></td>
  </tr>
</table>

<table>
  <caption>ログを表示するために**開発者**に必要な許可</caption>
  <tr>
    <th>アクション</th>
	<th>CF スペースの役割</th>
	<th>CF 組織の役割</th>
	<th>IAM 役割</th>
  </tr>
  <tr>
    <td>スペース・ドメイン内のログを表示する</td>
	<td>*開発者*</td>
	<td></td>
	<td></td>
  </tr>
  <tr>
    <td>アカウント・ドメイン内のログを表示する</td>
	<td></td>
	<td></td>
	<td>*ビューアー*</td>
  </tr>
  <tr>
    <td>組織ドメイン内のログを表示する</td>
	<td></td>
	<td>*監査員*</td>
	<td></td>
  </tr>
</table>



## Kibana を起動するための URL
{: #urls_kibana}

以下の表に、Kibana を起動するための URL と Kibana のバージョンを地域別にリストします。

<table>
    <caption>Kibana を起動するための URL</caption>
    <tr>
      <th>地域</th>
      <th>URL</th>
      <th>Kibana バージョン</th>
    </tr>
	<tr>
      <td>フランクフルト</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>シドニー</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
	<tr>
      <td>英国</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
    <tr>
      <td>米国南部</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
	  <td>Kibana 5.1</td>
    </tr>
</table>




