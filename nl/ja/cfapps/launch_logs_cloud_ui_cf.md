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

# Cloud Foundry アプリのログへのナビゲート
{: #launch_logs_cloud_ui_cf}

{{site.data.keyword.Bluemix}} UI で、Cloud Foundry アプリごとにある「ログ」タブを介して、または、{{site.data.keyword.loganalysisshort}} サービス UI を介して、ログの表示、フィルター操作、および分析を行うことができます。
{:shortdesc}

CF アプリ・ログを表示するには、以下の情報を考慮してください。 

<table>
  <caption>{{site.data.keyword.Bluemix_notm}} での CF アプリ・ログについての情報</caption>
  <tr>
    <th>UI オプション</th>
    <th>情報</th>
  </tr>
  <tr>
    <td>CF アプリ UI を介して使用可能な「ログ」タブ </td>
    <td>過去 24 時間のデータが含まれている、分析に使用できるログ。</td>
  </tr>
  <tr>
    <td>{{site.data.keyword.loganalysisshort}} ダッシュボード (Kibana)</td>
    <td>過去 3 日間のデータが含まれている、分析に使用できるログ。 カスタム期間を指定することもできます。</td>
  </tr>
</table>


## CF アプリ・ダッシュボードを介した CF アプリ・ログへのナビゲート 
{: #cfapp_ui}

Cloud Foundry アプリのデプロイメントまたはランタイムのログを表示するには、以下のステップを実行します。

1. 「アプリ」ダッシュボードで Cloud Foundry アプリの名前をクリックします。 
    
2. アプリ詳細ページで**「ログ」**をクリックします。
    
    **「ログ」**タブでは、アプリの最近のログを表示したり、最新のログ (ログ・ファイルの末尾) をリアルタイムで確認することができます。 また、コンポーネント (ログ・タイプ)、アプリ・インスタンス ID、およびエラーで、ログをフィルター操作できます。
    
デフォルトでは、{{site.data.keyword.Bluemix_notm}} コンソールから分析用に使用可能なログには、過去 24 時間のデータが含まれます。


## {{site.data.keyword.loganalysisshort}} UI を介した CF アプリ・ログへのナビゲート 
{: #cfapp_la}

Cloud Foundry アプリのデプロイメントまたはランタイムのログを表示するには、以下のステップを実行します。

1. 「アプリ」ダッシュボードで Cloud Foundry アプリの名前をクリックします。 
    
2. アプリ詳細ページで**「ログ」**をクリックします。
    
3. **「Kibana で表示」**をクリックします。

デフォルトでは、分析に使用できるログには、過去 15 分間のデータが含まれます。

**ヒント:** カスタム期間のデータを分析するには、『[Kibana での高度なログ分析](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#analyzing_logs_Kibana)』を参照してください。 


