---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, archive logs, COS, cloud object storage

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

 
# IBM Cloud Object Storage へのログのアーカイブ
{: #archiving}

{{site.data.keyword.la_full_notm}} インスタンスから {{site.data.keyword.cos_full_notm}} (COS) インスタンス内のバケットにログをアーカイブできます。 
{:shortdesc}

アーカイブを構成するためには、**ビューアー**のプラットフォーム役割と {{site.data.keyword.la_full_notm}} サービスに対する**管理者**のサービス役割を持つ IAM ポリシーが必要です。

{{site.data.keyword.la_full_notm}} インスタンスから {{site.data.keyword.cos_full_notm}} (COS) インスタンス内のバケットにログをアーカイブします。 各 {{site.data.keyword.la_full_notm}} インスタンスには、独自のアーカイブ構成があります。 

ログは、1 日 1 回、圧縮フォーマット **(.json.gz)** で自動的にアーカイブされます。 行ごとにそのメタデータが保持されます。

ログは、構成の保存後 24 時間から 48 時間以内にアーカイブされます。 

{{site.data.keyword.cos_full_notm}} インスタンスは、リソース・グループのコンテキスト内でプロビジョンされます。 {{site.data.keyword.la_full_notm}} インスタンスも、リソース・グループのコンテキスト内でプロビジョンされます。 両方のインスタンスを同じリソース・グループの下にグループ化することも、別々のリソース・グループに入れることもできます。 

{{site.data.keyword.la_full_notm}} はサービス ID を使用して {{site.data.keyword.cos_full_notm}} サービスと通信します。

* {{site.data.keyword.cos_full_notm}} インスタンス用に作成するサービス ID は、{{site.data.keyword.la_full_notm}} により、{{site.data.keyword.cos_full_notm}} インスタンスの認証とアクセスのために使用されます。 
* このサービス ID には、{{site.data.keyword.cos_full_notm}} インスタンスに対する許可を制限する特定のアクセス・ポリシーを割り当てることができます。 サービス ID を、ログのアーカイブ場所として計画しているバケットに対する書き込み許可だけを持つように制限します。

以下の図に、ログのアーカイブ時に統合されるさまざまなコンポーネントの概略を示します。

![ログのアーカイブに関する概略](images/archive.png "ログのアーカイブに関する概略")


{{site.data.keyword.la_full_notm}} インスタンスを {{site.data.keyword.cos_full_notm}} インスタンス内のバケットにアーカイブするには、以下のステップを実行します。


## ステップ 1. {{site.data.keyword.cos_full_notm}} を操作するための IAM ポリシーをユーザーに付与する
{: #archiving_step1}

**注:** このステップは、{{site.data.keyword.cloud_notm}} 上のアカウント所有者か {{site.data.keyword.cos_full_notm}} サービスの管理者が完了しなければなりません。

{{site.data.keyword.cos_full_notm}} サービスの管理者は、サービスのインスタンスをプロビジョンしたり、これらのインスタンスを使って作業するための許可をその他のユーザーに付与したり、サービス ID を作成したりできなければなりません。 

{{site.data.keyword.cos_full_notm}} サービスのエディターになるための許可をユーザーに付与できる方法は複数あります。

* アカウント内のサービスの管理者であるユーザーには、*管理者*のプラットフォーム役割を持つ、{{site.data.keyword.cos_full_notm}} サービスに対する IAM ポリシーがなければなりません。 アカウント内の個別リソースへのアクセス権限をこのユーザーに割り当てる必要があります。 

* リソース・グループのコンテキスト内のサービスの管理者であるユーザーには、リソース・グループのコンテキスト内の*管理者*のプラットフォーム役割を持つ、{{site.data.keyword.cos_full_notm}} サービスに対する IAM ポリシーがなければなりません。 


以下の表に、{{site.data.keyword.cos_full_notm}} サービスに対するアクションを完了するためにユーザーに付与できる役割をリストします。

| サービス                    | プラットフォーム役割    | アクション                                                                                        | 
|----------------------------|-------------------|-----------------------------------------------------------------------------------------------|       
| `Cloud Object Storage`     | 管理者     | ユーザーが {{site.data.keyword.cos_full_notm}} サービスを使って作業するためのポリシーをアカウント内のユーザーに割り当てられるようにします。 |
| `Cloud Object Storage`     | 管理者 </br>エディター | ユーザーが {{site.data.keyword.cos_full_notm}} サービスのインスタンスをプロビジョンできるようにします。    |
| `Cloud Object Storage`     | 管理者 </br>エディター </br>オペレーター | ユーザーがサービス ID を作成できるようにします。    | 
{: caption="表 1. 役割とアクション" caption-side="top"} 


リソース・グループのコンテキスト内の {{site.data.keyword.cos_full_notm}} サービスに対する管理者役割をユーザーに割り当てるには、以下のステップを実行します。 

1. メニュー・バーで**「管理」** &gt; **「アクセス (IAM)」**をクリックして、**「ユーザー」**を選択します。
2. アクセス権限を割り当てる対象のユーザーの行で、**「アクション」**メニューを選択し、**「アクセス権限の割り当て」**をクリックします。
3. **「リソース・グループ内のアクセス権限の割り当て」**を選択します。
4. リソース・グループを選択します。
5. 選択したリソース・グループに対する役割がまだユーザーに付与されていない場合は、**「リソース・グループへのアクセス権限の割り当て」**フィールドで役割を選択します。 

    選択する役割に応じて、ユーザーはダッシュボードでのリソース・グループの表示、リソース・グループ名の編集、またはグループへのユーザー・アクセスの管理を行うことができます。 
    
    リソース・グループ内の {{site.data.keyword.la_full_notm}} サービスへのアクセス権限のみをユーザーに付与する場合は、**「アクセス権限なし」**を選択します。

6. **「Cloud Object Storage」**を選択します。
7. **「管理者」**プラットフォーム役割を選択します。
8. **「割り当て」**をクリックします。



## ステップ 2. {{site.data.keyword.cos_full_notm}} のインスタンスをプロビジョンする
{: #archiving_step2}

**注:** このステップは、エディターか、{{site.data.keyword.cloud_notm}} 上の {{site.data.keyword.cos_full_notm}} サービスの管理者が完了しなければなりません。 

{{site.data.keyword.cos_full_notm}} インスタンスをプロビジョンするには、以下のステップを実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} UI が開きます。

2. **「カタログ」**をクリックします。 {{site.data.keyword.cloud_notm}} で使用可能なサービスのリストが開きます。

3. 表示されるサービスのリストをフィルタリングするには、**「ストレージ」**カテゴリーを選択します。

4. **「Object Storage」**タイルをクリックします。

5. サービス・インスタンスの名前を入力します。

6. リソース・グループを選択します。 

    デフォルトでは、**Default** リソース・グループが設定されます。

7. サービス・プランを選択します。 

    デフォルトでは、**「ライト」**プランが設定されます。

9. **「作成」**をクリックします。



## ステップ 3. バケットを作成する
{: #archiving_step3}

バケットにより、{{site.data.keyword.cos_full_notm}} インスタンス内のデータを編成できます。 

バケットを管理するには、{{site.data.keyword.cos_full_notm}} インスタンス上のバケットで作業するための許可をユーザーに付与しなければなりません。 以下の表に、ユーザーがバケットで作業するために保持できるさまざまなアクションと役割をリストします。

| サービス                    | 役割                   | アクション                             | 
|----------------------------|-------------------------|------------------------------------|       
| `Cloud Object Storage`     | プラットフォーム役割: ビューアー   | ユーザーが {site.data.keyword.Bluemix_notm}} UI によりバケットをすべて表示したり、バケット内のオブジェクトをすべてリストできるようにします。 |
| `Cloud Object Storage`     | サービス役割: 管理者   | ユーザーがオブジェクトを公開できるようにします。                                                       |
| `Cloud Object Storage`     | サービス役割: 管理者 </br>ライター | ユーザーがバケットやオブジェクトを作成したり破棄したりできるようにします。                         | 
| `Cloud Object Storage`     | サービス役割: リーダー    | ユーザーがオブジェクトをリストしたりダウンロードしたりできるようにします。                                                 |
{: caption="表 1. バケットで作業するための役割とアクション" caption-side="top"} 

**注:** バケットを作成するには、{{site.data.keyword.cos_full_notm}} インスタンスに対する管理者またはライター許可がユーザーになければなりません。

バケットを作成するには、以下のステップを実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} ダッシュボードが開きます。

2. ダッシュボードから、バケットの作成場所として計画している {{site.data.keyword.cos_full_notm}} インスタンスを選択します。

3. **「バケット」**を選択します。 次に、**「バケットの作成」**をクリックします。

4. *「固有のバケット名」*フィールドでバケット名を入力します。

    **注:** 全世界のすべての地域のすべてのバケットが、単一の名前空間を共有します。 

    バケット名の一部として {{site.data.keyword.la_full_notm}} インスタンス名を使用できます。 例えば、名前が *logdna-1* のインスタンスの場合、バケット名として *accountN-logdna-1* を使用できます。

    この名前は、{{site.data.keyword.la_full_notm}} Web UI でアーカイブを構成するのに必要です。

5. 回復力のタイプと、データを物理的に保管しようとしている場所を選択します。

    回復力 (レジリエンシー) とは、データが分散する地理的な領域の範囲や規模を指します。 
    
    クロス地域の回復力では、データが複数の都市圏の間に分散します。
    
    地域の回復力では、データが単一の都市圏全体に分散します。 
    
    単一データ・センターでは、データは単一の設置場所のデバイス間のみに分散します。

    詳しくは、[地域とエンドポイントの選択](/docs/services/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints)を参照してください。

6. *ストレージ・クラス*のタイプを選択します。

    さまざまなストレージ・クラスのバケットを作成できます。 データを取得するための要件に基づいて、バケットのストレージ・クラスを選択します。 詳しくは、[ストレージ・クラスの使用](/docs/services/cloud-object-storage?topic=cloud-object-storage-use-storage-classes#use-storage-classes)を参照してください。

    **注:** バケットがいったん作成されると、そのバケットのストレージ・クラスは変更できません。 オブジェクトを再分類する必要がある場合は、ご希望のストレージ・クラスの別のバケットにデータを移動する必要があります。

7. オプションで、Key Protect キーを追加して、保存されたデータを暗号化します。

    デフォルトでは、すべてのオブジェクトは、ランダムに生成される鍵と AONT (all-or-nothing-transform) を使用して暗号化されます。 保存されたデータのセキュリティーはこのデフォルトの暗号化モデルにより備えられますが、使用する暗号鍵を保有する必要のあるワークロードもあります。 詳しくは、[暗号化の管理](/docs/services/cloud-object-storage?topic=cloud-object-storage-manage-encryption#manage-encryption)を参照してください。



## ステップ 4. {{site.data.keyword.cos_full_notm}} インスタンスのサービス ID を作成する
{: #archiving_step4}

ユーザー ID がユーザーを識別するのと同様の方法で、サービス ID はサービスを識別します。 サービス ID は特定のユーザーに結び付けられません。 サービス ID を作成したユーザーが組織を辞めてアカウントから削除されるようなことがあっても、そのサービス ID はそのまま残ります。

{{site.data.keyword.cos_full_notm}} インスタンスのサービス ID を作成しなければなりません。 このサービス ID は、{{site.data.keyword.la_full_notm}} インスタンスで {{site.data.keyword.cos_full_notm}} インスタンスを認証するのに使用されます。 

このサービス ID には、特定のサービスを使用するための許可を制限したり、さまざまなサービスにアクセスするための許可を結合したりする特定のアクセス・ポリシーを割り当てなければなりません。 例えば、アクセスを単一のバケットに制限するには、コンソールまたは CLI を使用して、サービス ID がインスタンス・レベルのポリシーを持たないようにしてください。


{{site.data.keyword.cos_full_notm}} インスタンスに対する書き込み許可があるサービス ID を作成するには、以下のステップを実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} ダッシュボードが開きます。

2. ダッシュボードから、バケットの作成場所として計画している {{site.data.keyword.cos_full_notm}} インスタンスを選択します。

3. **「サービス資格情報」**を選択します。 次に、**「新規資格情報」**を選択します。

4. 名前を入力します。 

5. **「ライター」**役割を選択します。

6. **「追加」**をクリックします。

    新しいサービス ID がリストに追加されます。 


作成したばかりのサービス ID について、**「資格情報の表示」**をクリックします。 そのサービス ID に関連した情報を表示できます。 

* API 鍵をコピーします。 **「apikey」**フィールドの値セットが該当します。
* リソース・インスタンス ID をコピーします。 **「resource_instance_id」**フィールドの値セットが該当します。


## ステップ 5. バケットに対する書き込み許可だけを持つようにサービス ID を制限する
{: #archiving_step5}

サービス ID がバケットに対する書き込み許可だけを持つように制限しようとしている場合は、以下のステップを実行します。

1. サービス ID に関する情報を読み、**「iam_apikey_name」**フィールドの値と**「iam_apikey_name」**フィールドを書き留めます。 

2. ダッシュボードから、**「管理」** &gt; **「アクセス (IAM)」**を選択してから、**「ユーザー」**を選択します。

3. **「サービス ID」**を選択します。

4. iam_apikey_name 値の一部である **auto-generated-serviceId-<ID という名前のサービス ID を見つけます。

5. サービス ID を選択します。 次に、**「アクセス・ポリシー」**で、**「ライター」**をクリックします。

6. 「*リソース・タイプ*」フィールドで、**「バケット」**を入力します。

7. 「*リソース ID*」フィールドで、バケットの名前を入力します。

8. **「保存」**をクリックします。

**注:**「リソース・タイプ」フィールドか「リソース」フィールドをブランクのままにすると、作成されるポリシーはインスタンス・レベルのポリシーになります。


## ステップ 6. エンドポイントを選択する
{: #archiving_step6}

エンドポイントは、バケットの検索場所を定義します。 地域や回復力のタイプに応じて、さまざまなエンドポイントがあります。 詳しくは、[地域とエンドポイントの選択](/docs/services/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints)を参照してください。

バケットのエンドポイントを入手するには、以下のステップを実行します。

1. {{site.data.keyword.cloud_notm}} アカウントにログインします。

    [{{site.data.keyword.cloud_notm}} ダッシュボード ![外部リンク・アイコン](../../icons/launch-glyph.svg "外部リンク・アイコン")](https://cloud.ibm.com/login){:new_window} をクリックして、{{site.data.keyword.cloud_notm}} ダッシュボードを起動します。

	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.cloud_notm}} ダッシュボードが開きます。

2. ダッシュボードから、バケットの作成場所として計画している {{site.data.keyword.cos_full_notm}} インスタンスを選択します。

3. **「バケット」**を選択します。 次に、ログのアーカイブ場所にする作成済みのバケットを選択します。

4. **「構成」**を選択します。

5. プライベート・エンドポイントの 1 つをコピーします。 



## ステップ 7. ログをアーカイブするための IAM ポリシーをユーザーに付与する
{: #archiving_step7}

以下の表に、{{site.data.keyword.la_full_notm}} Web UI から {{site.data.keyword.cos_full_notm}} インスタンス内のバケットへのログのアーカイブを構成するために、ユーザーが保持する必要のあるポリシーをリストします。

| サービス                        | 役割                      | 付与される許可                  | 
|--------------------------------|---------------------------|-------------------------------------|  
| `{{site.data.keyword.la_full_notm}}` | プラットフォーム役割: ビューアー     | ユーザーが「プログラム識別情報ロギング (Observability Logging)」ダッシュボードでサービス・インスタンスのリストを表示できるようにします。 |
| `{{site.data.keyword.la_full_notm}}` | サービス役割: 管理者      | ユーザーが Web UI を起動して Web UI にログを表示できるようにします。                             |
{: caption="表 2. IAM ポリシー" caption-side="top"} 

ユーザーに対してこれらのポリシーを構成する方法について詳しくは、[LogDNA でのログの表示許可をユーザーに付与する](/docs/services/Log-Analysis-with-LogDNA/work_iam.html#user_logdna)を参照してください。

ログをアーカイブするための許可をユーザーに割り当てるには、以下のステップを実行します。 

1. メニュー・バーで**「管理」** &gt; **「アクセス (IAM)」**をクリックして、**「ユーザー」**を選択します。
2. アクセス権限を割り当てる対象のユーザーの行で、**「アクション」**メニューを選択し、**「アクセス権限の割り当て」**をクリックします。
3. **「リソース・グループ内のアクセス権限の割り当て」**を選択します。
4. リソース・グループを選択します。
5. 選択したリソース・グループに対する役割がまだユーザーに付与されていない場合は、**「リソース・グループへのアクセス権限の割り当て」**フィールドで役割を選択します。 

    選択する役割に応じて、ユーザーはダッシュボードでのリソース・グループの表示、リソース・グループ名の編集、またはグループへのユーザー・アクセスの管理を行うことができます。 
    
    リソース・グループ内の {{site.data.keyword.la_full_notm}} サービスへのアクセス権限のみをユーザーに付与する場合は、**「アクセス権限なし」**を選択します。

6. **「IBM Log Analysis with LogDNA」**を選択します。
7. **「ビューアー」**プラットフォーム役割を選択します。
8. **「管理者」**サービス役割を選択します。
9. **「割り当て」**をクリックします。



## ステップ 8. {{site.data.keyword.la_full_notm}} インスタンス用にアーカイブを構成する
{: #archiving_step8}


{{site.data.keyword.la_full_notm}} インスタンスの COS バケットへのアーカイブを構成するには、以下のステップを実行します。

1. {{site.data.keyword.la_full_notm}} Web UI ブラウザーを起動します。 [詳細はこちら](/docs/services/Log-Analysis-with-LogDNA/view_logs.html#view_logs_step2)。

2. **「構成」**アイコンを選択します。 次に、**「アーカイブ (Archiving)」**を選択します。 

3. **「IBM Cloud Object Storage」**を選択します。

4. ログのアーカイブ場所にしようとしているバケット、エンドポイント、API 鍵、インスタンス ID を設定します。

    <table>
      <caption>表 3. COS フィールド</caption>
      <tr>
         <th>フィールド</th>
         <th>値</th>
      </tr>
      <tr>
         <td>バケット</td>
         <td>COS バケット名を設定します。 </td>
      </tr>
      <tr>
         <td>エンドポイント</td>
         <td>COS バケットのプライベート・エンドポイントに設定します。</td>
      </tr>
      <tr>
         <td>API キー</td>
         <td>COS サービス ID に関連付けられる API 鍵に設定します。</td>
      </tr>
      <tr>
         <td>インスタンス ID</td>
         <td>COS インスタンス ID を設定します。 </td>
      </tr>
    </table>

5. **「保存」**をクリックします。


構成の保存後に、1 日に 1 回ログがアーカイブされます。



