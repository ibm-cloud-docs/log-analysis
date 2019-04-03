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


# エラー・メッセージ
{: #error_msgs}

{{site.data.keyword.Bluemix}} で {{site.data.keyword.loganalysisshort}} サービスを使用するときに、以下のエラー・メッセージが表示されることがあります。
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**メッセージの説明**

{{site.data.keyword.loganalysisfull}} インスタンス {インスタンス GUID} について Bluemix スペース {スペース GUID} に割り振られた毎日の割り当て量に達しました。 Log Searchストレージについての現在の毎日の割り当ては 500MB です。これは 3 日間Log Searchストレージに保存され、この間 Kibana での検索が可能です。 1 日により多くのデータをLog Searchストレージに保管して、すべてのログをLog Collection ストレージに保存できるようにプランをアップグレードするには、このスペースの {{site.data.keyword.loganalysisshort}} サービス・プランをアップグレードしてください。 サービス・プランとプランのアップグレード方法について詳しくは、『[プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。


**メッセージの説明** 

ライト・サービス・プランで割り振られたLog Searchストレージの割り当て量に達すると、ID *BXNLG020001W* のメッセージが表示されることがあります。 ライト・プランは、スペースで {{site.data.keyword.loganalysisshort}} サービスをプロビジョンするとデフォルトで設定される補完的なサービス・プランです。 Log Searchストレージについての現在の毎日の割り当ては 500MB です。これは 3 日間Log Searchストレージに保存され、この間 Kibana での検索が可能です。

**リカバリー**

1 日により多くのデータをLog Searchストレージに保管して、すべてのログをLog Collection ストレージに保存できるようにプランをアップグレードするには、このスペースの {{site.data.keyword.loganalysisshort}} サービス・プランをアップグレードしてください。 サービス・プランとプランのアップグレード方法について詳しくは、『[プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。


## BXNLG020002W 
{: #BXNLG020002W}


**メッセージの説明**

{{site.data.keyword.loganalysisfull}} インスタンス {インスタンス GUID} について Bluemix スペース {スペース GUID} に割り振られた毎日の割り当て量に達しました。  Log Searchストレージについての現在の毎日の割り当ては XXX です。これは 3 日間保存され、この間 Kibana での検索が可能です。 これは、Log Collection ストレージでのログ保存ポリシーには影響を与えません。 1 日により多くのデータをLog Searchストレージに保管できるようにプランをアップグレードするには、このスペースの {{site.data.keyword.loganalysisshort}} サービス・プランをアップグレードしてください。 サービス・プランとプランのアップグレード方法について詳しくは、『[プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。

XXX は、現在のプランで検索可能なデータのサイズを表します。

**メッセージの説明** 

{{site.data.keyword.loganalysisfull}} インスタンス {インスタンス GUID} についてスペース {スペース GUID} に割り振られた毎日の割り当て量に達しました。  Log Searchストレージについての現在の毎日の割り当ては 500MB、2 GB、5 GB、または 10 GB です。これは 3 日間保存され、この間 Kibana での検索が可能です。 これは、Log Collection ストレージでのログ保存ポリシーには影響を与えません。

**リカバリー**

1 日により多くのデータをLog Searchストレージに保管できるようにプランをアップグレードするには、このスペースの {{site.data.keyword.loganalysisshort}} サービス・プランをアップグレードしてください。 サービス・プランとプランのアップグレード方法について詳しくは、『[プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。




