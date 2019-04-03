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


# Kibana ダッシュボードへのナビゲート
{: #launch}

Kibana は、{{site.data.keyword.loganalysisshort}} サービスから起動するか、{{site.data.keyword.Bluemix}} UI から起動するか、または Web ブラウザーから直接起動することができます。
{:shortdesc}

CF アプリおよび Docker コンテナー用に、{{site.data.keyword.Bluemix_notm}} UI から Kibana を起動して、Kibana を起動したリソースに応じてデータを表示および分析することができます。 例えば、特定の CF アプリのログがその特定のアプリに応じて表示されるように Kibana を起動できます。
    
Kubernetes インフラストラクチャーにデプロイされた Docker コンテナーなど、任意のクラウド・リソース用に、直接ブラウザー・リンクから、または、{{site.data.keyword.loganalysisshort}} サービス・ダッシュボードから Kibana を起動して、提供されたスペース内のサービスから集約されたログ・データを表示できます。 ダッシュボードに表示されるデータをフィルター操作するために使用される照会によって、組織内のスペースのログ項目が取り出されます。 Kibana に表示されるログ情報には、ログインしている組織のスペース内にデプロイされているすべてのリソースに関するレコードが含まれます。 

次の表に、いくつかのクラウド・リソースと、Kibana を起動するためのサポートされているナビゲーション方法をリストします。

<table>
<caption>表 1. リソースおよびサポートされているナビゲーション方法のリスト </caption>
  <tr>
    <th>リソース</th>
	<th>{{site.data.keyword.loganalysisshort}} サービス・ダッシュボードから Kibana ダッシュボードへのナビゲート</th>
    <th>Bluemix ダッシュボードから Kibana ダッシュボードへのナビゲート</th>
    <th>Web ブラウザーから Kibana ダッシュボードへのナビゲート</th>
  </tr>
  <tr>
    <td>CF アプリ</td>
	<td>はい</td>
    <td>はい</td>
    <td>はい</td>
  </tr>  
  <tr>
    <td>Kubernetes クラスターにデプロイされたコンテナー</td>
	<td>はい</td>
    <td>はい</td>
    <td>はい</td>
  </tr>  
  <tr>
    <td>{{site.data.keyword.Bluemix_notm}} 管理のインフラストラクチャーにデプロイされたコンテナー (非推奨)</td>
	<td>はい</td>
    <td>はい</td>
    <td>はい</td>
  </tr>  
</table>

Kibana について詳しくは、「[Kibana User Guide ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}」を参照してください。
    

##  Log Analysis サービスのダッシュボードから Kibana へのナビゲート
{: #launch_Kibana_from_log_analysis}

Kibana に表示されるデータをフィルター操作するために使用される照会によって、組織内のスペースのログ項目が取り出されます。 
	
Kibana に表示されるログ情報には、ログインしている組織のスペース内にデプロイされているすべてのリソースに関するレコードが含まれます。

{{site.data.keyword.loganalysisshort}} サービスのダッシュボードから Kibana を起動するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} にログインし、{{site.data.keyword.Bluemix_notm}} ダッシュボードから {{site.data.keyword.loganalysisshort}} サービスをクリックします。 
    
2. {{site.data.keyword.Bluemix_notm}} UI で**「Managed」**タブを選択します。

3. **「起動」**をクリックします。 Kibana ダッシュボードが開きます。

デフォルトでは、**「Discover」**ページは、デフォルトの索引パターンが選択され、時間フィルターが過去 15 分に設定された状態でロードされます。 

「Discover」ページでログ項目が表示されない場合は、時間ピッカーを調整します。 詳しくは、『[時間フィルターの設定](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)』を参照してください。

	
	
##  Web ブラウザーから Kibana へのナビゲート
{: #launch_Kibana_from_browser}

Kibana に表示されるデータをフィルター操作するために使用される照会によって、組織内のスペースのログ項目が取り出されます。 
	
Kibana に表示されるログ情報には、ログインしている組織のスペース内にデプロイされているすべてのリソースに関するレコードが含まれます。

以下のステップを実行して、ブラウザーから Kibana を起動します。

1. Web ブラウザーを開き、Kibana を起動します。 その後、Kibana ユーザー・インターフェースにログインします。

    地域別の URL のリストを表示するには、『[Kibana を起動するための URL](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#urls_kibana)』を参照してください。
    
    Kibana の「Discover」ページが開きます。
	
2. ログ・データの表示および分析を行いたいスペースの索引パターンを選択します。

    1. **「default-index」**をクリックします。
	
	2. スペースの索引パターンを選択します。 索引パターンのフォーマットは次のとおりです。
	
	    ```
	    [logstash-Space_ID-]YYYY.MM.DD 
	    ```
        {: screen}
	
	    ここで、*Space_ID* は、ログ・データの表示および分析を行いたいスペースの GUID です。 
	
「Discover」ページでログ項目が表示されない場合は、時間ピッカーを調整します。 詳しくは、『[時間フィルターの設定](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)』を参照してください。


	
##  CF アプリのダッシュボードから Kibana へのナビゲート
{: #launch_Kibana_from_cf_app}

Kibana で表示されるデータをフィルタリングするために使用される照会によって、Kibana を起動した {{site.data.keyword.Bluemix_notm}} CF アプリのログ項目を取得します。

Cloud Foundry アプリケーションのログを Kibana で表示するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} アカウントにログインします。

    {{site.data.keyword.Bluemix_notm}} ダッシュボードは、[http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window} にあります。
    
	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

2. {{site.data.keyword.Bluemix_notm}} ダッシュボードでアプリ名またはコンテナーをクリックします。 
    
3. {{site.data.keyword.Bluemix_notm}} UI でログ・タブを開きます。

    CF アプリの場合、ナビゲーション・バーの**「ログ」**をクリックします。 
    「ログ」タブが開きます。  

4. **「Kibana で表示」**をクリックします。 Kibana ダッシュボードが開きます。

    デフォルトでは、**「Discover」**ページは、デフォルトの索引パターンが選択され、時間フィルターが過去 15 分に設定された状態でロードされます。 検索照会は、CF アプリのすべての項目に突き合わせるように設定されます。

    「Discover」ページでログ項目が表示されない場合は、時間ピッカーを調整します。 詳しくは、『[時間フィルターの設定](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)』を参照してください。

	
	
##  Kubernetes クラスターにデプロイされたコンテナーのダッシュボードから Kibana へのナビゲート
{: #launch_Kibana_for_containers_kube}

Kibana で表示されるデータをフィルタリングするために使用される照会によって、Kibana を起動したクラスターのログ項目が取り出されます。

コンテナーのログを Kibana で表示するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} アカウントにログインします。

    {{site.data.keyword.Bluemix_notm}} ダッシュボードは、[http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window} にあります。
    
	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

2. メニューから**「ダッシュボード」**を選択します。

3. *「クラスター」*セクションで、クラスターを選択します。

4. *「概要」*セクションで、**「ログの表示」**を選択します。

    Kibana が開きます。




##  {{site.data.keyword.Bluemix_notm}} 管理のインフラストラクチャーにデプロイされたコンテナーのダッシュボードから Kibana へのナビゲート (非推奨)
{: #launch_Kibana_for_containers}

この方法は、{{site.data.keyword.Bluemix_notm}} が管理するインフラストラクチャーにデプロイされたコンテナーにのみ適用されます。

Kibana で表示されるデータをフィルタリングするために使用される照会によって、Kibana を起動したコンテナーのログ項目が取り出されます。

Docker コンテナーのログを Kibana で表示するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} にログインし、{{site.data.keyword.Bluemix_notm}} ダッシュボードでコンテナーをクリックします。 
    
2. {{site.data.keyword.Bluemix_notm}} UI でログ・タブを開きます。

    {{site.data.keyword.IBM_notm}} が管理するインフラストラクチャーにデプロイされたコンテナーの場合、ナビゲーション・バーで**「モニターおよびログ」**を選択してから、**「ロギング」**タブをクリックします。 
    
    「ログ」タブが開きます。  

3. **「拡張ビュー」**をクリックします。 Kibana ダッシュボードが開きます。

    デフォルトでは、**「Discover」**ページは、デフォルトの索引パターンが選択され、時間フィルターが過去 30 秒に設定された状態でロードされます。 検索照会は、Docker コンテナーのすべての項目に突き合わせるように設定されます。

    「Discover」ページでログ項目が表示されない場合は、時間ピッカーを調整します。 詳しくは、『[時間フィルターの設定](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-filter_logs#set_time_filter)』を参照してください。

	



