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


# コンプライアンス
{: #compliance}

[{{site.data.keyword.Bluemix}} は、IBM の厳しいセキュリティー規格に準拠したクラウド・プラットフォームおよびサービスを提供します](/docs/security/compliance.html#compliance)。 {{site.data.keyword.loganalysislong}} サービスは、{{site.data.keyword.Bluemix_notm}} 向けに作成された DevOps サービスです。 
{:shortdesc}


## 一般データ保護規則

一般データ保護規則 (GDPR) は、EU 全域における統一されたデータ保護の法的枠組みを作成しようとするものであり、個人データの管理権限を市民の手に取り戻すことを目的とし、世界のどこであろうと個人データをホスティングおよび「処理」するものに対して厳格な規則を課します。 また、この規則では、EU 域内と域外における個人データの自由な移動に関するルールが導入されます。 

**特記事項:** {{site.data.keyword.loganalysisshort}} サービスは、{{site.data.keyword.Bluemix_notm}} 内のお客様のアカウントで実行されている Cloud リソースから、および {{site.data.keyword.Bluemix_notm}} の外部からお客様が送信するログから、ログ・レコードを保管および表示します。 {{site.data.keyword.loganalysisshort}} に保管されるログ項目のどれにも個人情報 (PI) が含まれていてはなりません。なぜなら、このデータは、お客様の社内の他のユーザーからアクセス可能であり、この Cloud サービスをサポートできるように {{site.data.keyword.IBM_notm}} からもアクセス可能であるためです。

### 地域
{: #regions}

{{site.data.keyword.loganalysisshort}} サービスは、このサービスが使用可能な {{site.data.keyword.Bluemix_notm}} Public 地域では GDPR に準拠しています。


### データ保存
{: #data_retention}

{{site.data.keyword.loganalysisshort}} サービスには、お客様のデータが保管される以下の 2 つのデータ・リポジトリーが組み込まれています。 

* Log Search は、Kibana を介して分析に使用可能なログ・データをホスティングします。
* Log Collection は、長期保管のログ・データをホスティングします。

{{site.data.keyword.loganalysisshort}} サービス・プランに応じて、データは Log Search に保管されるか、または、Log Search と Log Collection に保管されます。 標準プランまたはライト・プランの場合、データは Log Search にのみ保管されます。 他のプランの場合、データは Log Search と Log Collection に保管されます。

* Log Search に保管されたログは、3 日間保持されます。
* Log Collection に保管されたログは、保存ポリシーを構成するか手動で削除するまで保持されます。 デフォルトでは、Log Collection 内のログは無期限に保持されます。



### データ削除
{: #data_deletion}

以下の情報を考慮してください。

* Log Search に保管されたログは、3 日後に削除されます。

* Log Collection に保管されたログは、手動で削除したときに削除されるか、または、保存ポリシーが構成されている場合は一定の日数後に削除されます。 

    ログ保存ポリシーを構成して、Log Collection 内でログを保持する日数を定義できます。 詳しくは、『[{{site.data.keyword.Bluemix_notm}} プラグインを使用したログ保存ポリシーの表示および構成](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy)』を参照してください。

    [Log Collection API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} または [Log Collection CLI](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window} を使用して、Log Collection からログを手動で削除できます。 

    CLI を使用して、Log Collection からログを手動で削除できます。 詳しくは、『[{{site.data.keyword.Bluemix_notm}} プラグインを使用した ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs)』を参照してください。


有料プランから標準プランまたはライト・プランに変更すると、Log Collection 内のログは約 1 日後に削除されます。

いつでも、サポート・チケットをオープンし、Log Search および Log Collection からすべてのデータを削除するよう依頼できます。 IBM サポート・チケットのオープンについては、『[サポートへのお問い合わせ](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support)』を参照してください。



### 詳細情報
{: #info}

詳しくは、以下を参照してください。

[{{site.data.keyword.Bluemix_notm}} セキュリティー・コンプライアンス](/docs/security/compliance.html#compliance)

[GDPR - {{site.data.keyword.IBM_notm}} 公式ページ](https://www.ibm.com/data-responsibility/gdpr/)



