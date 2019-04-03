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

# ログの管理許可とアカウント・ログの表示許可の付与
{: #grant_permissions}

{{site.data.keyword.Bluemix}} では、1 人のユーザーに 1 つ以上の IAM 役割を割り当てることができます。 これらの役割は、{{site.data.keyword.loganalysisshort}} サービスを使用して作業するためにユーザーが使用できるタスクを定義します。  
{:shortdesc}

例えば、ユーザーに**オペレーター**の役割を付与して、そのユーザーにログの管理を許可することができます。 ユーザーにアカウント・ログを見てもらいたいだけなら、そのユーザーに**ビューアー**の役割を付与することができます。 詳しくは、[IAM 役割](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles)を参照してください。

**注:** 

* ログの管理またはアカウント・ログの表示を行う許可をユーザーに付与するには、アカウント内の他のユーザーにポリシーを割り当てる許可を持っているか、または、アカウント所有者である必要があります。 アカウント所有者でない場合、エディター、オペレーター、または管理者の役割が設定された IAM ポリシーを持っている必要があります。
* スペース内のログを表示する許可をユーザーに付与するには、そのユーザーがそのスペース内で {{site.data.keyword.loganalysisshort}} サービスを使用して実行できるアクションを記述する Cloud Foundry 役割をそのユーザーに割り当てるための、組織およびスペースでの許可を持っている必要があります。 

## {{site.data.keyword.Bluemix_notm}} UI を使用してユーザーに IAM ポリシーを割り当てる
{: #grant_permissions_ui_account}

{{site.data.keyword.loganalysisshort}} サービスを使用して作業する許可をユーザーに付与するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} コンソールにログインします。

    Web ブラウザーを開き、{{site.data.keyword.Bluemix_notm}} ダッシュボード: [http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window} を起動します。
	
	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

2. メニュー・バーから、**「管理」>「アカウント」>「ユーザー」**をクリックします。 

    「*ユーザー*」ウィンドウに、現在選択されているアカウントにおけるユーザーのリストが、E メール・アドレスと共に表示されます。
	
3. ユーザーがアカウントのメンバーである場合、リストからユーザー名を選択するか、または、**「アクション」**メニューから*「ユーザーの管理」*をクリックします。

    ユーザーがアカウントのメンバーでない場合、『[ユーザーの招待](/docs/iam/iamuserinv.html#iamuserinv)』を参照してください。

4. **「アクセス・ポリシー」**セクションで、**「アクセス権限の割り当て」**をクリックし、**「リソースへのアクセス権限の割り当て」**を選択します。

    *「ユーザー * へのリソース・アクセス権限の割り当て (Assign resource access to user*)」* ウィンドウが開きます。

5. ポリシーに関する情報を入力します。 以下の表は、ポリシーを定義する必須のフィールドを示します。 

    <table>
	  <caption>IAM ポリシーを構成するためのフィールドのリスト。</caption>
	  <tr>
	    <th>フィールド</th>
		<th>値</th>
	  </tr>
	  <tr>
	    <td>サービス</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>地域</td>
		<td>ユーザーがログを処理する権限を付与される地域を指定できます。 1 つ以上の地域を個々に選択するか、または、**「すべての現行地域」**を選択してすべての地域の権限を付与します。</td>
	  </tr>
	  <tr>
	    <td>サービス・インスタンス</td>
		<td>*「すべてのサービス・インスタンス」* を選択します。</td>
	  </tr>
	  <tr>
	    <td>役割</td>
		<td>1 つ以上の IAM 役割を選択してください。 <br>有効な役割は、*管理者*、*オペレーター*、*エディター*、*ビューアー*です。 <br>役割ごとの許可されるアクションについて詳しくは、『[IAM 役割](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles)』を参照してください。
		</td>
	  </tr>
     </table>
	
6. **「割り当て」**をクリックします。
	
構成したポリシーは、選択した地域で利用できます。 


## コマンド・ラインを使用してユーザーに IAM ポリシーを割り当てる
{: #grant_permissions_commandline}

コマンド・ラインを使用して、アカウント・ログを表示する権限をユーザーに付与するには、以下のステップを実行します。

1. 端末から、{{site.data.keyword.Bluemix_notm}} アカウントにログインします。 

    詳しくは、『[{{site.data.keyword.Bluemix_notm}} にログインするにはどうすればよいですか](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)』を参照してください。

2. ユーザーがアカウントのメンバーであることを確認します。 次のコマンドを実行して、アカウント内のユーザーのリストを取得します。

    ```
	ibmcloud account users
	```
    {: codeblock}	

	ユーザーとその GUID のリストが表示されます。

3. ユーザーがアカウントのメンバーでない場合、アカウント所有者に連絡して、ユーザーをアカウントに招待するよう依頼します。 詳しくは、『[ユーザーの招待](/docs/iam/iamuserinv.html#iamuserinv)』を参照してください。

    **ヒント:** アカウントにユーザーを招待するコマンドは、`ibmcloud iam account-user-invite USER_EMAIL` です。
		
4. ユーザーにポリシーを割り当てます。 次のコマンドを実行します。

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	各部分の説明:
    * USER_NAME は、ユーザーの {{site.data.keyword.Bluemix_notm}} ID です。
	* ROLE は、IAM 役割です。 有効な値は、*管理者*、*オペレーター*、*エディター*、*ビューアー*です。

5. ポリシーがユーザーに割り当てられたことを検証します。 次のコマンドを実行して、ユーザーに割り当てられたすべてのポリシーをリストします。

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## {{site.data.keyword.Bluemix_notm}} UI を使用して、スペース・ログを表示する許可をユーザーに付与する
{: #grant_permissions_ui_space}

スペース内のログを表示する許可をユーザーに付与するには、そのユーザーがそのスペース内で {{site.data.keyword.loganalysisshort}} サービスを使用して実行できるアクションを記述した Cloud Foundry 役割をそのユーザーに割り当てる必要があります。 

{{site.data.keyword.loganalysisshort}} サービスを使用して作業する許可をユーザーに付与するには、以下のステップを実行します。

1. {{site.data.keyword.Bluemix_notm}} コンソールにログインします。

    Web ブラウザーを開き、{{site.data.keyword.Bluemix_notm}} ダッシュボード: [http://bluemix.net ![外部リンク・アイコン](../../../icons/launch-glyph.svg "外部リンク・アイコン")](http://bluemix.net){:new_window} を起動します。
	
	ユーザー ID とパスワードを使用してログインすると、{{site.data.keyword.Bluemix_notm}} UI が開きます。

2. メニュー・バーから、**「管理」>「アカウント」>「ユーザー」**をクリックします。 

    「*ユーザー*」ウィンドウに、現在選択されているアカウントにおけるユーザーのリストが、E メール・アドレスと共に表示されます。
	
3. ユーザーがアカウントのメンバーである場合、リストからユーザー名を選択するか、または、**「アクション」**メニューから*「ユーザーの管理」*をクリックします。

    ユーザーがアカウントのメンバーでない場合、『[ユーザーの招待](/docs/iam/iamuserinv.html#iamuserinv)』を参照してください。

4. **「Cloud Foundry アクセス権限」**を選択してから、組織を選択します。

    その組織で使用可能なスペースのリストが表示されます。

5. スペースを 1 つ選択します。 次に、メニュー・アクションから**「スペースの役割の編集」**を選択します。

6. スペースの役割を 1 つ以上選択します。 有効な役割は、*管理者*、*開発者*、および*監査員* です。
	
7. **「役割の保存」**をクリックします。




