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


# ログの管理
{: #manage_logs}

{{site.data.keyword.loganalysisshort}} CLI および {{site.data.keyword.loganalysisshort}} API を使用して、Log Collection に保管されたログを管理できます。
{:shortdesc}

ログを管理するには、以下の情報を考慮してください。

1. 使用するユーザー ID は、{{site.data.keyword.Bluemix_notm}} において {{site.data.keyword.loganalysisshort}} 用に割り当てられた、ログを管理する許可のあるポリシーを持っている必要があります。 

    IAM 役割のリストと役割ごとのタスクについては、『[IAM 役割](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles)』を参照してください。 
	
	ポリシーの割り当て方法について詳しくは、『[{{site.data.keyword.Bluemix_notm}} UI を使用してユーザーに IAM ポリシーを割り当てる](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_account)』を参照してください。
	
2. このフィーチャーは、ログ保存が許可されるサービス・プランでのみ使用可能です。 

    サービス・プランについて詳しくは、『[サービス・プラン](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)』を参照してください。

{{site.data.keyword.loganalysisshort}} サービスでは次の 2 つの CLI が提供されており、これらを使用してログを管理できます。

* {{site.data.keyword.loganalysisshort}} {{site.data.keyword.Bluemix_notm}} プラグイン。 この CLI について詳しくは、『[{{site.data.keyword.loganalysisshort}} CLI ({{site.data.keyword.Bluemix_notm}} プラグイン)](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli)』を参照してください。
* {{site.data.keyword.loganalysisshort}} CF プラグイン (非推奨)。 詳しくは、『[Log Analysis CLI の構成 (CF プラグイン)](/docs/services/CloudLogAnalysis/reference/logging_cli.html#logging_cli)』を参照してください。


## ログ保存ポリシーの構成
{: #log_retention_policy}

{{site.data.keyword.loganalysisshort}} CLI を使用して、ログ保存ポリシーを表示および構成できます。 ポリシーは、ログが Log Collection 内に保持される日数を指定します。 

* デフォルトでは、有料プランを選択した場合、ログが収集されて Log Collection 内に保持されます。 
* 保存期間を設定した場合、保存期間を過ぎると、ログは Log Collection から自動的に削除され、復旧することはできません。
* アカウントに対して保存期間を指定できます。 その保存期間が、そのアカウントのすべてのスペースに対して自動的に構成されます。 
* スペースに対して保存期間を指定できます。
* 保存ポリシーはいつでも変更できます。
* ポリシーの値を *-1* に設定することによって、ポリシーを無効にすることができます。 

**注:** ログ保存ポリシーを無効にする場合、Log Collection 内のログをユーザー自身が保守する必要があります。 CLI コマンド [cf logging delete](/docs/services/CloudLogAnalysis/reference/logging_cli.html#delete4) を使用して、古いログを削除できます。

詳しくは、以下を参照してください。

* [{{site.data.keyword.Bluemix_notm}} プラグインを使用したログ保存ポリシーの表示および構成](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy)
* [CF プラグインを使用したログ保存ポリシーの表示および構成](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy.html#configuring_retention_policy)


## ログの削除
{: #log_deletion}

Log Search に保管されたログは、3 日後に削除されます。

Log Collection に保管されたログは、保存ポリシーを構成するか手動で削除するまで保持されます。 

* ログ保存ポリシーを構成して、Log Collection 内でログを保持する日数を定義できます。 詳しくは、『[{{site.data.keyword.Bluemix_notm}} プラグインを使用したログ保存ポリシーの表示および構成](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy)』を参照してください。

* [Log Collection API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} または [Log Collection CLI](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window} を使用して、Log Collection からログを手動で削除できます。 

* CLI を使用できます。 CLI を使用してログを手動で削除することについて詳しくは、『[{{site.data.keyword.Bluemix_notm}} プラグインを使用した ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs)』を参照してください。
    


## ログのダウンロード
{: #download_logs2}

過去 3 日間のログを Kibana で検索できます。 より古いログ・データを分析できるように、ログをローカル・ファイルにダウンロードしたり、これらのログを他のプログラム (ローカル Elastic スタックなど) にパイプしたりすることができます。 

詳しくは、以下を参照してください。

* [{{site.data.keyword.Bluemix_notm}} プラグインを使用したログのダウンロード](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs_cloud.html#downloading_logs)
* [CF プラグインを使用したログのダウンロード](/docs/services/CloudLogAnalysis/how-to/manage-logs/downloading_logs.html#downloading_logs1)



## ログに関する情報の取得
{: #info_about_logs}

ログに関する一般情報を取得するには、`ibmcloud logging log-show` コマンドまたは `cf logging status` コマンドを使用します。 詳しくは、以下を参照してください。

* [{{site.data.keyword.Bluemix_notm}} プラグインを使用したログ情報の表示](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information_cloud.html#viewing_log_status1)
* [CF プラグインを使用したログ情報の表示](/docs/services/CloudLogAnalysis/how-to/manage-logs/viewing_log_information.html#viewing_log_status1)

例えば、コストを制御するため、一定の期間にアプリのログのサイズをモニターしたい場合があります。 例えば、予想より多いログを生成しているアプリまたはサービスがあるかどうかを調べるため、ある {{site.data.keyword.Bluemix_notm}} スペースについて、1 週間における各ログ・タイプのサイズを把握したいといった場合が考えられます。 ログのサイズを確認するには、`ibmcloud logging log-show` コマンドまたは `cf logging status` コマンドを使用します。

スペース・ドメイン、組織ドメイン、またはアカウント・ドメインに保管されたログに関する情報を表示できます。



## {{site.data.keyword.loganalysisshort_notm}} CLI のインストール ({{site.data.keyword.Bluemix_notm}} プラグイン)
{: #install_cli2}

CLI のインストール方法について詳しくは、『[ロギング CLI のインストール](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#config_log_collection_cli)』を参照してください。

CLI のバージョンを確認するには、`ibmcloud plugin list` コマンドを実行します。

コマンドの実行方法についてのヘルプを利用するには、『[コマンドの実行に関するコマンド・ライン・ヘルプの利用](/docs/services/CloudLogAnalysis/how-to/manage-logs/config_log_collection_cli_cloud.html#command_cli_help)』を参照してください。


## ロギング・エンドポイント
{: #endpoints}

以下の表は、地域ごとのロギング URL を示します。

<table>
    <caption>地域別のエンドポイント</caption>
    <tr>
      <th>地域</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>フランクフルト</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>シドニー</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td>英国</td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>米国南部</td>
      <td>[https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## ログを管理するユーザーに必要な役割
{: #roles1}

{{site.data.keyword.Bluemix_notm}} では、ユーザーに 1 つ以上の役割を割り当てることができます。 これらの役割は、{{site.data.keyword.loganalysisshort}} サービスを使用して作業するためにユーザーが使用できるタスクを定義します。 

以下の表は、ログを管理するために必要なユーザーの役割を示します。

<table>
  <caption>ログを管理するために**アカウント所有者**に必要な許可</caption>
  <tr>
	<th>IAM 役割</th>
	<th>アクション</th>
  </tr>
  <tr>
    <td>*管理者*</td>
    <td>ログの状況を確認します。 </br>ログをダウンロードします。 </br>ログを削除します。 </br>ログ保存ポリシーを変更します。 </br>セッションを管理します。 </td>
</table>

<table>
  <caption>ログを管理するために**監査員**に必要な許可</caption>
  <tr>
	<th>IAM 役割</th>
	<th>アクション</th>
  </tr>
  <tr>
    <td>*ビューアー*</td>
    <td>Log Collection でホストされているログに関する情報を取得します。 </br>構成されたログ保存ポリシーに関する情報を取得します。 </td>
</table>

<table>
  <caption>ログを管理するために**管理者**に必要な許可</caption>
  <tr>
	<th>IAM 役割</th>
	<th>アクション</th>
  </tr>
  <tr>
    <td>*管理者*</td>
    <td>ログの状況を確認します。 </br>ログをダウンロードします。 </br>ログを削除します。 </br>ログ保存ポリシーを変更します。 </br>セッションを管理します。 </td>
</table>

<table>
  <caption>ログを管理するために**開発者**に必要な許可</caption>
  <tr>
	<th>IAM 役割</th>
	<th>アクション</th>
  </tr>
  <tr>
    <td>*エディター*</td>
    <td>ログの状況を確認します。 </br>ログをダウンロードします。 </br>ログを削除します。 </br>ログ保存ポリシーを変更します。 </br>セッションを管理します。</td>
</table>

