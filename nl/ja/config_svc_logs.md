---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# {{site.data.keyword.cloud_notm}} サービス・ログの構成
{: #config_svc_logs}

1 つの地域に複数の {{site.data.keyword.la_full_notm}} インスタンスを含めることができます。ただし、{{site.data.keyword.cloud_notm}} において有効なサービスのログを受信するよう構成できるのは、1 つの地域において 1 つのインスタンスのみです。
{:shortdesc}



## プログラム識別情報ダッシュボードによるプラットフォーム・サービス・ログの構成
{: #config_svc_logs_ui}

{{site.data.keyword.cloud_notm}} のプログラム識別情報ダッシュボードからインスタンスを構成するには、以下の手順を実行します。

1. [{{site.data.keyword.cloud_notm}} アカウント ![外部リンクのアイコン](../../icons/launch-glyph.svg "外部リンクのアイコン")](https://cloud.ibm.com/login){:new_window} にログインします。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. メニュー・アイコン ![メニュー・アイコン](../../icons/icon_hamburger.svg) に移動します。 その後、**「プログラム識別情報」**を選択して、*「プログラム識別情報」*ダッシュボードにアクセスします。

3. **「ロギング」**を選択してから、**「プラットフォーム・サービス・ログの構成 (Configure platform services logs)」**をクリックします。 

4. クラウド・プラットフォームの有効なサービスからログを受信する LogDNA インスタンスを選択します。

5. 地域を選択します。 

6. インスタンスを選択します。

7. **「保存」**をクリックします。 

*プログラム識別情報*のメイン・ページが開きます。

サービス・ログを受信するよう選択したインスタンスに、**「プラットフォーム・サービス・ログ (Platform services logs)」**というフラグが表示されます。

{{site.data.keyword.la_full_notm}} にログを送信できるサービスについて詳しくは、[クラウド・サービス](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services)を参照してください。

