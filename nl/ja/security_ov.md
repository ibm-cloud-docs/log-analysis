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

# セキュリティー
{: #security_ov}

ユーザーが実行を許可される {{site.data.keyword.loganalysisshort}} アクションを制御するために、1 人のユーザーに 1 つ以上の役割を割り当てることができます。 
{:shortdesc}

{{site.data.keyword.loganalysisshort}} サービス API を使用して作業するためには、UAA トークンまたは IAM トークンを使用する必要があります。 ログを {{site.data.keyword.loganalysisshort}} サービスに送信するためには、ロギング・トークンが必要です。


## 認証モデル
{: #auth1}

{{site.data.keyword.loganalysisshort}} サービスでの作業を CLI または API を介して行うには、認証トークンが必要です。

{{site.data.keyword.loganalysisshort}} サービスでは、以下の認証モデルがサポートされます。

* [UAA 認証](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#auth_uaa)

    UAA トークンを管理するには、CLI のみを使用できます。
	
* [IAM 認証](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_iam1#auth_iam1)

    IAM 認証モデルは、UI、CLI、または API の管理機能を提供します。 

**注:** UAA トークンおよび IAM トークンは、一定期間を過ぎると有効期限が切れます。 

## 役割
{: #roles3}

{{site.data.keyword.cloud_notm}} には 2 つのタイプの役割があり、それらの役割によって、ユーザーが {{site.data.keyword.loganalysisshort}} サービスを使用した処理を行うときに実行できるアクションが制御されます。

* Cloud Foundry (CF) 役割: 1 つ以上の CF 役割を割り当てることによって、ユーザーが実行できる {{site.data.keyword.loganalysisshort}} アクションを制御します。 スペースまたは組織内のログを表示および管理するためのユーザーの許可を、これらの役割によって制御します。
* IAM 役割: 1 つ以上の IAM 役割を割り当てることによって、ユーザーが実行できる {{site.data.keyword.loganalysisshort}} アクションを制御します。 アカウント・ログを表示および管理するためのユーザーの許可を、これらの役割によって制御します。 


以下の表は、役割のタイプと、役割が制御する {{site.data.keyword.cloud_notm}} のドメインを示します。

<table>
  <caption>表 1. アクションを制御するドメイン別の役割のタイプ</caption>
  <tr>
    <th></th>
	<th align="right">アカウント</th>
    <th align="right">組織</th>
    <th align="right">スペース</th>	
  </tr>
  <tr>
    <td align="left">CF 役割</td>
	<td align="center">いいえ</td>
	<td align="center">はい</td>
	<td align="center">はい</td>
  </tr>
  <tr>
    <td align="left">IAM 役割</td>
	<td align="center">はい</td>
	<td align="center">いいえ</td>
	<td align="center">いいえ</td>
  </tr>
</table>


## CF 役割
{: #bmx_roles}

以下の表に、{{site.data.keyword.loganalysisshort}} サービスを使用して作業するための各 CF 役割の特権をリストします。

<table>
  <caption>表 2. {{site.data.keyword.loganalysisshort}} サービスでの作業のための Cloud Foundry 役割と特権</caption>
  <tr>
    <th>役割</th>
	<th>ドメイン</th>
	<th>アクセス特権</th>
  </tr>
  <tr>
    <td>管理者</td>
	<td>組織 <br>スペース</td>
	<td>すべての RESTful API</td>
  </tr>
  <tr>
    <td>開発者</td>
	<td>スペース</td>
	<td>すべての RESTful API</td>
  </tr>
  <tr>
    <td>監査員</td>
	<td>組織 <br>スペース</td>
	<td>ログの照会などの読み取り専用操作を実行する RESTful API のみ。</td>
  </tr>
</table>


## IAM 役割
{: #iam_roles}

以下の表に、{{site.data.keyword.loganalysisshort}} サービスを使用して作業するための各 IAM 役割の特権をリストします。

<table>
  <caption>表 3. {{site.data.keyword.loganalysisshort}} サービスでの作業のための IAM 役割と特権</caption>
  <tr>
    <th>役割</th>
	<th>特権</th>
  </tr>
  <tr>
    <td>管理者</td>
	  <td>スペース内のログまたはアカウント・レベルのログに関する情報を表示します。 <br>ローカル・ファイルにログをダウンロードしたり、ログを別のプログラム (Elastic スタックなど) にパイプしたりします。 <br>スペースまたはアカウントで使用可能なログの保存期間を表示します。 <br>スペースまたはアカウントで使用可能なログの保存期間を更新します。 <br>アクティブ・セッションおよびその ID をリストします。 <br>ログのダウンロードに使用できるセッションを作成します。 <br>セッション ID で指定されたセッションを削除します。 <br>単一セッションの状況を表示します。 <br>ログを削除します。 </td>
  </tr>
  <tr>
    <td>エディター</td>
	  <td>スペース内のログまたはアカウント・レベルのログに関する情報を表示します。 <br>ローカル・ファイルにログをダウンロードしたり、ログを別のプログラム (Elastic スタックなど) にパイプしたりします。 <br>スペースまたはアカウントで使用可能なログの保存期間を表示します。 <br>スペースまたはアカウントで使用可能なログの保存期間を更新します。 <br>アクティブ・セッションおよびその ID をリストします。 <br>ログのダウンロードに使用できるセッションを作成します。 <br>セッション ID で指定されたセッションを削除します。 <br>単一セッションの状況を表示します。 <br>ログを削除します。  </td>
  </tr>
  <tr>
    <td>オペレーター</td>
	  <td>スペース内のログまたはアカウント・レベルのログに関する情報を表示します。 <br>スペースまたはアカウントで使用可能なログの保存期間を表示します。 <br>アクティブ・セッションおよびその ID をリストします。 <br>単一セッションの状況を表示します。 <br>ローカル・ファイルにログをダウンロードしたり、ログを別のプログラム (Elastic スタックなど) にパイプしたりします。  <br>ログのダウンロードに使用できるセッションを作成します。 <br>セッション ID で指定されたセッションを削除します。 </td>
  </tr>
  <tr>
    <td>ビューアー</td>
	  <td>スペース内のログまたはアカウント・レベルのログに関する情報を表示します。 <br>スペースまたはアカウントで使用可能なログの保存期間を表示します。 <br>アクティブ・セッションおよびその ID をリストします。 <br>単一セッションの状況を表示します。 </td>
  </tr>
</table>

以下の表は、API、サービス・アクション、および、{{site.data.keyword.loganalysisshort}} サービスによって使用される IAM 役割の間の関係を示します。

<table>
  <caption>表 4. API、サービス・アクション、および IAM 役割の間の関係 </caption>
  <tr>
    <th>API</th>
	<th>アクション</th>
	<th>IAM 役割</th>
	<th>説明</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>管理者、エディター</td>
	<td>ログを削除します。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>管理者、エディター、ビューアー</td>
	<td>{{site.data.keyword.cloud_notm}} スペース内のログまたはアカウント・レベルのログに関する情報を表示します。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>管理者、エディター</td>
	<td>ローカル・ファイルにログをダウンロードしたり、ログを別のプログラム (Elastic スタックなど) にパイプしたりします。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>管理者、エディター、ビューアー</td>
    <td>{{site.data.keyword.cloud_notm}} スペースまたはアカウントで使用可能なログの保存期間を表示または変更します。</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>管理者、エディター</td>
    <td>{{site.data.keyword.cloud_notm}} スペースまたはアカウントで使用可能なログの保存期間を表示または更新します。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>管理者、エディター、ビューアー</td>
    <td>アクティブ・セッションおよびその ID をリストします。</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>管理者、エディター</td>
    <td>ログのダウンロードに使用できるセッションを作成します。</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>管理者、エディター</td>
    <td>セッション ID で指定されたセッションを削除します。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>管理者、エディター、ビューアー</td>
    <td>単一セッションの状況を表示します。</td>
  </tr>
</table>

## API を使用したログ管理のための認証トークンの取得
{: #get_token}

{{site.data.keyword.loganalysisshort}} API を使用してログを管理するには、認証トークンを使用する必要があります。 

**スペース・ドメイン内にあるログの処理**

* {{site.data.keyword.loganalysisshort}} CLI を使用して UAA トークンを取得します。 
* トークンには有効期限があります。 

詳しくは、『[UAA トークンの取得](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_uaa#auth_uaa)』を参照してください。

**アカウント・ドメイン内にあるログの処理**

* {{site.data.keyword.cloud_notm}} CLI を使用して IAM トークンを取得します。 
* トークンには有効期限があります。 

詳しくは、『[IAM トークンの取得](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-auth_iam1#auth_iam1)』を参照してください。


## ログを Log Analysis に送信するためのロギング・トークンの取得
{: #get_logging_token}

ログを {{site.data.keyword.loganalysisshort}} サービスに送信するためには、ロギング・トークンが必要です。 

スペース・ドメインにログを送信するには、以下のいずれかの方法を選択してください。

* [{{site.data.keyword.cloud_notm}} コマンド ibmcloud service を使用して、ログをスペースに送信するためのロギング・トークンを取得する](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-logging_token#logging_token_cloud_cli)
* [Log Analysis CLI を使用して、ログをスペースに送信するためのロギング・トークンを取得する](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-logging_token#logging_token_la_cloud_cli)
* [Log Analysis API を使用して、ログをスペースに送信するためのロギング・トークンを取得する](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-logging_token#logging_token_api)


## ログを処理するためのユーザーへの許可の付与
{: #grant_permissions1}

ユーザーがログの管理または表示を実行できるためには、{{site.data.keyword.loganalysisshort}} サービスを使用して作業することの許可を {{site.data.keyword.cloud_notm}} においてユーザーに付与されている必要があります。

* ログを管理するために必要な許可について詳しくは、『[ログを管理するユーザーに必要な役割](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-manage_logs#roles1)』を参照してください。
* ログを表示するために必要な許可について詳しくは、『[ログを表示するユーザーに必要な役割](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#roles)』を参照してください。

許可を付与する方法について詳しくは、以下を参照してください。

* [{{site.data.keyword.cloud_notm}} UI を使用してユーザーに IAM ポリシーを割り当てる](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions)
* [コマンド・ラインを使用してユーザーに IAM ポリシーを割り当てる](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_commandline)
* [{{site.data.keyword.cloud_notm}} UI を使用して、スペース・ログを表示する許可をユーザーに付与する](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_space)


