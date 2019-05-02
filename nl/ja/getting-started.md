---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

subcollection: LogDNA

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

# 入門チュートリアル
{: #getting-started}

{{site.data.keyword.cloud_notm}} アーキテクチャーにログ管理機能を追加するには、{{site.data.keyword.la_full}} を使用します。 {{site.data.keyword.la_full_notm}} は、{{site.data.keyword.IBM_notm}} とのパートナーシップにより LogDNA で運用されます。
{:shortdesc}


## ステップ 1. 始める前に
{: #getting-started_prereqs}

* {{site.data.keyword.la_full_notm}} についてお読みください。 詳しくは、[{{site.data.keyword.la_full_notm}} の概要](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about)を参照してください。
* サービスが使用可能な地域を確認します。 詳しくは、[地域](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions)を参照してください。
* {{site.data.keyword.cloud_notm}} アカウントのメンバーまたは所有者であるユーザー ID を取得します。 

    {{site.data.keyword.cloud_notm}} ユーザー ID を取得するには、[「登録」![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックしてください。



## ステップ 2. はじめに
{: #getting-started_step2}

ログを管理する対象のクラウド・リソースを選択します。 次に、{{site.data.keyword.la_full_notm}} サービスを使用してログをモニターできるように、このログ・ソースを構成します。 ログ・ソースの場所は、{{site.data.keyword.la_full_notm}} インスタンスをプロビジョンする地域でも、別の地域でもかまいません。

以下の表に、{{site.data.keyword.la_full_notm}} サービスを使用してログの保管や管理を行うように構成できるクラウド・リソースの例をリストします。 {{site.data.keyword.loganalysisshort}} サービスへの入門として、まず 1 つのリソースに関してこのチュートリアルを実行してください。

<table>
  <caption>{{site.data.keyword.la_full_notm}} サービス入門チュートリアル </caption>
  <tr>
    <th>リソース</th>
    <th>チュートリアル</th>
    <th>環境</th>
    <th>シナリオ</th>
  </tr>
  <tr>
    <td>{{site.data.keyword.containershort}} で実行されているコンテナー</td>
    <td>[{{site.data.keyword.la_full_notm}} による Kubernetes クラスター・ログの管理](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} Public </td>
    <td>![{{site.data.keyword.containershort}} と {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} と {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu、Linux Debian</td>
    <td>[{{site.data.keyword.la_full_notm}} による Linux Ubuntu の管理](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>オンプレミス</td>
    <td>![Ubuntu サーバーと {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Ubuntu サーバーと {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## ステップ 3. 計画のアップグレード
{: #getting-started_step3}

より多くのロギング機能を使用できるようにします。

{{site.data.keyword.la_full_notm}} サービス・プランを、[ログのフィルター処理](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5)、[ログの検索](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6)、[ビューの定義](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7)、[アラートの構成](https://docs.logdna.com/docs/alerts)を行える有料プランにアップグレードします。 {{site.data.keyword.la_full_notm}} サービス・プランについて詳しくは、[価格プラン](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans)を参照してください。

## ステップ 4. 次のステップ 
{: #getting-started_iam}

次に、IAM でのユーザー・アクセスを管理します。

ユーザーが {{site.data.keyword.la_full_notm}} サービスを使って作業するのに必要な IAM ポリシーを識別します。

{{site.data.keyword.la_full_notm}} サービスとの IAM の統合について詳しくは、[IAM でのユーザー・アクセスの管理](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam)を参照してください。

例えば、1 つのユーザー役割を選択して、{{site.data.keyword.la_full_notm}} サービスを使って作業するための許可をそのユーザーに付与する方法を学びます。 

| {{site.data.keyword.cloud_notm}} でのユーザー役割 | 詳細情報                     |
|-----------------------------------------------------|------------------------------------------|
| アカウント所有者                                       | [{{site.data.keyword.cloud_notm}} アカウント内のサービスの管理者になるための許可をユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| アカウント内のプラットフォーム・サービス管理者       | [{{site.data.keyword.cloud_notm}} アカウント内のサービスの管理者になるための許可をユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| リソース・グループ内のプラットフォーム・サービス管理者  | [リソース・グループ内のサービスの管理者になるための許可をユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg) |
| アカウント内のプラットフォーム DevOps オペレーター           | [{{site.data.keyword.cloud_notm}} アカウント内のサービスを管理するための許可を DevOps ユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account) |
| リソース・グループ内のプラットフォーム DevOps オペレーター        | [リソース・グループ内のサービスを管理するための許可を DevOps ユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg) |
| LogDNA 内のサービス管理者                     | [LogDNA でログを管理しアラートを構成するための許可を付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)              |
| ユーザー / 開発者                                    | [LogDNA でログを表示および管理するための許可をユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)               |
{: caption="表 2. {{site.data.keyword.cloud_notm}} での Cloud 役割" caption-side="top"}


