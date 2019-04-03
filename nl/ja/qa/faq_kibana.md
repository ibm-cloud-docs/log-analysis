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


# Kibana FAQ
{: #faq_kibana}

ここでは、{{site.data.keyword.Bluemix}} ロギング機能の使用に関するよくある質問に対する回答を示します。 {:shortdesc}

* [Kibana の「Discover」ページでデータを表示できない場合、どうすればよいですか?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_discover_kibana)
* [認証例外を受け取った場合、どうすればよいですか?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_no_data_dashboard_kibana)
* [Kibana の「Discover」ページでフィールドの横に ? 記号が表示されるのはなぜですか?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#logging_qa_kibana_question)
* [デフォルトの索引パターンを変更しようとすると 403 エラーが表示されます](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#error_403)
* [短縮 URL が機能しません](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#short_url)
* [Bluemix でアカウント・ログを検索できますか?](/docs/services/CloudLogAnalysis/qa/faq_kibana.html#acc_logs_1)


## Kibana の「Discover」ページでデータを表示できない場合、どうすればよいですか?
{: #logging_qa_no_data_discover_kibana}

Kibana でデータを表示できない場合、以下の異なるシナリオが考えられます。

1. Kibana を起動したときに、「Discover」ページでデータが表示されない場合があります。 **「No results found.」**というメッセージを受け取ります。 
2. Kibana の「Discover」ページで作業している場合があります。 ただし、短時間後に Kibana でタスクを実行しようとすると、**「No results found.」**というメッセージが表示されます。

この問題を解決するには、以下のステップを実行します。

1. 「Discover」ページで設定されている*時間ピッカー* を確認し、期間を長くします。 

    **注**: デフォルトでは、{{site.data.keyword.Bluemix_notm}} において*時間ピッカー* は、過去 15 分間のデータを表示するように設定されています。

    *時間ピッカー* の設定方法について詳しくは、『[時間フィルターの設定](/docs/services/CloudLogAnalysis/kibana/filter_logs.html#set_time_filter1)』を参照してください。
       
2. 「*Discover*」ページの検索バーにある拡大鏡をクリックします。 ページ・データが、デフォルトの検索照会に基づいて最新表示されます。

    あるいは、*自動最新表示* の期間を設定できます。

    **注**: デフォルトでは、{{site.data.keyword.Bluemix_notm}} において*自動最新表示* の期間は、**OFF** に設定されています。
    
    これを有効にする方法について詳しくは、『[データの自動最新表示](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_refresh_interval)』を参照してください。



## 認証例外を受け取った場合、どうすればよいですか?
{: #logging_qa_no_data_dashboard_kibana}

「Dashboard」ページの視覚化にデータが表示されず、**「Error: Authorization Exception.」**というエラー・メッセージを受け取った場合、各視覚化のデータを表示する権限を確認します。

以下の情報を考慮してください。
「Dashboard」ページで 1 つ以上の視覚化を構成できます。 「Dashboard」ページが視覚化で表示されるデータを収集する要求を行う際には、すべての視覚化に対して 1 つの要求のみが発行されます。 いずれかの視覚化のデータを表示する権限がない場合、要求全体が失敗します。

この問題を解決するには、以下のステップを実行します。

1. 権限がない視覚化を識別します。

    1. 「*Dashboard*」ページ内の視覚化の*鉛筆* アイコンをクリックします。 「*Visualize*」ページで視覚化が開きます。 あるいは、「*Visualize*」ページで 1 つの視覚化をロードします。 
    2. データを表示できるかを確認します。
    
    視覚化ごとに上記ステップを繰り返します。

2. クラウド管理者に対して、視覚化のデータを表示する権限を要求します。

3. 問題の原因となっている視覚化のデータを表示する権限を付与してもらっている間、権限のない視覚化を除外した新規「Dashboard」ページを作成します。 

    そのダッシュボードを共有している場合、同じダッシュボードを使用している他のチーム・メンバーが影響を受けるため、視覚化を削除しないでください。



## Kibana の「Discover」ページでフィールドの横に ? 記号が表示されるのはなぜですか?
{: #logging_qa_kibana_question}

Kibana で「Discover」ページを開くと、「available fields」セクションにリストされるフィールドの横に文字 `t` ではなく疑問符 `?` が表示されることがあります。フィールドのリストを再ロードすると、フィールドのタイプが分析され、疑問符 `?` は文字 `t` に置き換えられます。詳しくは、『[フィールド・リストの再ロード](/docs/services/CloudLogAnalysis/kibana/analize_logs_interactively.html#discover_view_reload_fields)』を参照してください。


## デフォルトの索引パターンを変更しようとすると 403 エラーが表示されます
{: #error_403}

デフォルトの索引パターンは変更できません。 

異なる索引パターンを新規のデフォルトの索引パターンとして設定しようとすると、エラー「`Config: Error 403 Forbidden`」が表示されます。

## 短縮 URL が機能しません
{: #short_url}

検索、視覚化、またはダッシュボードの共有はサポートされません。 したがって、共有したい Kibana オブジェクトの短縮 URL も機能しません。 

## Bluemix でアカウント・ログを検索できますか?
{: #acc_logs_1}

アカウント所有者は、自身のアカウント・ログを検索および分析することができます。

アカウント・ログを表示するには、以下のステップを実行します。

1. [Kibana を起動します](/docs/services/CloudLogAnalysis/kibana/launch.html#launch_Kibana_from_browser)。 例えば、米国南部地域の場合は URL `https://logging.ng.bluemix.net` を使用します。

2. アカウント・ログを表示するため、オプション**「View AccountName account Logs」**を選択します。 *AccountName* はアカウントの名前です。

