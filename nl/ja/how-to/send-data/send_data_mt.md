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

# IBM Cloud のスペースへのオンプレミス・データの送信
{: #send_data_mt}

{{site.data.keyword.loganalysisshort}} サービスにログ・データを送信するために、マルチテナント Logstash Forwarder (mt-logstash-forwarder) を構成することができます。 
{: shortdesc}

{{site.data.keyword.Bluemix_notm}} 内のスペースにログ・データを送信するには、以下のステップを実行します。

## 前提条件
{: #prereqs1}

* {{site.data.keyword.Bluemix_notm}} にログインするための {{site.data.keyword.Bluemix_notm}} ID。
* スペース内で {{site.data.keyword.loganalysisshort}} サービスと連携するための許可のあるユーザー ID。 詳しくは、『[セキュリティー](/docs/services/CloudLogAnalysis/security_ov.html#security_ov)』を参照してください。
* ローカル環境にインストールされた {{site.data.keyword.loganalysisshort}} CLI。
* ログ取り込みを許可するプランを持つアカウント内のスペースにプロビジョンされた {{site.data.keyword.loganalysisshort}} サービス。


## ステップ 1: ロギング・トークンを取得する
{: #get_logging_auth_token}

{{site.data.keyword.loganalysisshort}} CLI がインストールされた端末セッションから以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} で、地域、組織、およびスペースにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。
    
2. `ibmcloud logging token-get` コマンドを実行します。 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    このコマンドはロギング・トークンを返します。
    
    以下に例を示します。

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    ここで、*Tenant Id* は、ログの送信を予定しているスペースの GUID です。


## ステップ 2: mt-logstash-forwarder を構成する
{: #configure_mt_logstash_forwarder}

{{site.data.keyword.loganalysisshort}} サービスにログを送信することを計画している環境で mt-logstash-forwarder を構成するには、以下のステップを実行します。

1.	root ユーザーとしてログインします。 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	ログの時刻を同期するため、Network Time Protocol (NTP) パッケージをインストールします。 

    例えば、Ubuntu システムの場合、`timedatectl status` で *Network time on: yes* と表示されるかどうかをチェックします。 表示される場合、ご使用の Ubuntu システムは ntp を使用するように既に構成済みであり、このステップはスキップしてもかまいません。
    
    ```
    # timedatectl status
    Local time: Mon 2017-06-12 03:01:22 PDT
    Universal time: Mon 2017-06-12 10:01:22 UTC
    RTC time: Mon 2017-06-12 10:01:22
    Time zone: America/Los_Angeles (PDT, -0700)
    Network time on: yes
    NTP synchronized: yes
    RTC in local TZ: no
    ```
    {: screen}
    
    Ubuntu システムに ntp をインストールするには、以下のステップを実行します。

    1.	以下のコマンドを実行して、パッケージを更新します。 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	以下のコマンドを実行して、ntp パッケージをインストールします。 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	以下のコマンドを実行して、ntpdate パッケージをインストールします。 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	以下のコマンドを実行して、サービスを停止します。 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	以下のコマンドを実行して、システム・クロックを同期化します。 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        以下の例のように、時刻が調整されたことが結果で示されます。
        
        ```
        4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	以下のコマンドを実行して、ntpd を再度開始します。 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        サービスが開始していることを結果で確認できます。

    7.	以下のコマンドを実行して、ntpd サービスがクラッシュやリブートの後に自動的に開始できるようにします。 
    
        ```
        service ntp enable
        ```
        {: codeblock}
        
        表示される結果は、ntpd サービスを管理するために使用できるコマンドのリストです。以下に例を示します。
        
        ```
        Usage: /etc/init.d/ntpd {start|stop|status|restart|try-restart|force-reload}
        ```
        {: screen}

3. システムのパッケージ・マネージャー内に {{site.data.keyword.loganalysisshort}} サービス用のリポジトリーを追加します。 次のコマンドを実行します。

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. ご使用の環境から Log Collection にログを送信するように、mt-logstash-forwarder をインストールし、構成します。 

    1. 以下のコマンドを実行して、mt-logstash-forwarder をインストールします。
    
        ```
        apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. ご使用の環境に応じて mt-logstash-forwarder 構成ファイルを作成します。 このファイルに含まれる変数が、{{site.data.keyword.loganalysisshort}} サービスをポイントするように mt logstash forwarder を構成するために使用されます。
    
       ファイル `/etc/mt-logstash-forwarder/mt-lsf-config.sh` を編集します。 例えば、次のように vi エディターを使用できます。
               
       ```
       vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       forwarder が {{site.data.keyword.loganalysisshort}} サービスをポイントするようにするため、**mt-lsf-config.sh** ファイルに以下の変数を追加します。 
         
       <table>
          <caption>表 1. VM 内の forwarder が {{site.data.keyword.loganalysisshort}} サービスをポイントするために必要な変数のリスト </caption>
          <tr>
            <th>変数名</th>
            <th>説明</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>VM の ID (例: *MyTestVM*)。 </td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>ターゲット URL。 取り込み URL のリストを取得するには、『[取り込み URL](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls)』を参照してください。 例えば、米国南部地域のログを送信するには、値を **ingest.logging.ng.bluemix.net:9091** に設定します。 </td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>{{site.data.keyword.Bluemix_notm}} に送信するログを {{site.data.keyword.loganalysisshort}} サービスが収集する準備ができている場所のスペース ID。 <br>ステップ 1 で取得した値を使用してください。</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>ロギング・トークン。 <br>ステップ 1 で取得した値を使用してください。</td>
          </tr>
          <tr>
            <td>LSF_GROUP_ID</td>
            <td>この値を、関連するログをグループ化するために定義できるカスタム・タグに設定してください。</td>
          </tr>
       </table>
        
       例えば、以下のサンプル・ファイルは、英国地域の ID *7d576e3b-170b-4fc2-a6c6-b7166fd57912* のスペース用のファイルです。
        
       ```
       # more mt-lsf-config.sh 
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. mt-logstash-forwarder を開始します。 
    
       ```
       service mt-logstash-forwarder start
       ```
       {: codeblock}
                
デフォルトでは、forwarder は syslog のみを監視します。 ログは Kibana での分析に使用可能です。
        

## ステップ 3: さらにログ・ファイルを指定する
{: #add_logs}

デフォルトでは、/var/log/syslog ファイルのみが forwarder によってモニターされます。 別の構成ファイルも forwarder によってモニターされるように、それらをディレクトリー `/etc/mt-logstash-forwarder/conf.d/syslog.conf/` に追加できます。 

ご使用の環境で実行されるアプリの構成ファイルを追加するには、以下のステップを実行します。

1.	`/etc/mt-logstash-forwarder/conf.d/syslog.conf` ファイルをコピーします。 

    **ヒント:** ログ・ファイルを追加するために syslog.conf ファイルを編集しないでください。
    
    例えば、Ubuntu システムで、次のコマンドを実行します。
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	テキスト・エディターを使用して *myapp.conf* ファイルを編集し、モニターしたいアプリケーション・ログを含むように更新します。 各アプリ・ログのログ・タイプを含めてください。 使用されない例は削除してください。

3.	mt-logstash-forwarder を再始動します。 

     mt-logstash-forwarder サービスを再始動します。 次のコマンドを実行します。
    
    ```
    service mt-logstash-forwarder restart
    ```
    {: codeblock}

**例**

hello アプリからの stdout または stderr を含めるため、stdout または stderr をログ・ファイルにリダイレクトします。 このアプリの forwarder 構成ファイルを作成します。 その後、mt-logstash-forwarder を再始動します。

1.	`/etc/mt-logstash-forwarder/conf.d/syslog.conf` ファイルをコピーします。 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. 構成ファイル *myapp.conf* を編集します。

    ログを取り込む際、Kibana で JSON フィールドによって検索できるようにするには、JSON 構文解析を有効にします。 特定のファイル・パスについて、構成ファイルで `is_json` を true に設定します。 このように構成されたログ・ファイルの場合、ログ行は、復帰改行文字によって分離された、JSON ブロックとしてフォーマットされます。 それにより、mt-logstash-forwarder は、それらのすべての JSON フィールドを個別の Kibana 検索可能フィールドとして取り込みます。 JSON フィールド名には、タイプに基づいた接尾部が含まれます。
    
    ```
    {
    "files": [
         # other file configurations omitted...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
