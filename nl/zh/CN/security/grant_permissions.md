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

# 授予许可权以管理日志和查看帐户日志
{: #grant_permissions}

在 {{site.data.keyword.Bluemix}} 中，您可以为用户分配一个或多个 IAM 角色。这些角色可定义要启用什么任务以便该用户能够使用 {{site.data.keyword.loganalysisshort}} 服务。
  
{:shortdesc}

例如，您可以授予用户**操作员**角色以允许该用户管理日志。如果只希望某个用户查看帐户日志，那么可授予该用户**查看者**角色。有关更多信息，请参阅 [IAM 角色](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles)。

**注：** 

* 要授予用户管理日志或查看帐户日志的许可权，您必须有权将策略分配给帐户中的其他用户，或者您必须是帐户所有者。如果您不是帐户所有者，那么必须具有 IAM 策略以及编辑者、操作员或管理员角色。
* 要授予用户查看空间中日志的许可权，您必须在组织和空间中有权为该用户分配 Cloud Foundry 角色，该角色描述了此用户可以在该空间中使用 {{site.data.keyword.loganalysisshort}} 服务执行的操作。 

## 通过 {{site.data.keyword.Bluemix_notm}} UI 向用户分配 IAM 政策
{: #grant_permissions_ui_account}

要授予用户使用 {{site.data.keyword.loganalysisshort}} 服务的许可权，请完成以下步骤：



1. 登录到 {{site.data.keyword.Bluemix_notm}} 控制台。

    打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}
	
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 从菜单栏，单击**管理 > 帐户 > 用户**。 

    *用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
3. 如果用户是帐户的成员，请从列表中选择用户名，或者从*操作*菜单中单击**管理用户**。

    如果用户不是帐户的成员，请参阅[邀请用户](/docs/iam?topic=iam-iamuserinv#iamuserinv)。

4. 在**访问策略**部分，单击**分配访问权**，然后选择**分配对资源的访问权**。

    这将打开*向用户分配资源访问权** 窗口。

5. 输入策略的信息。下表列出定义策略所需的字段列表： 

    <table>
	  <caption>用于配置 IAM 策略的字段列表。</caption>
	  <tr>
	    <th>字段</th>
		<th>值</th>
	  </tr>
	  <tr>
	    <td>服务</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>区域</td>
		<td>您可以指定要授予用户使用日志的访问权的区域。分别选择一个或多个区域，或者选择**所有当前区域**以授予对所有区域的访问权。</td>
	  </tr>
	  <tr>
	    <td>服务实例</td>
		<td>选择*所有服务实例*。</td>
	  </tr>
	  <tr>
	    <td>角色</td>
		<td>选择一个或多个 IAM 角色。<br>有效角色为：*管理员*、*操作员*、*编辑者*和*查看者*。<br>有关每种角色所允许的操作的更多信息，请参阅 [IAM 角色](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles)。</td>
	  </tr>
     </table>
	
6. 单击**分配**。
	
您所配置的策略适用于所选区域。 


## 使用命令行向用户分配 IAM 策略
{: #grant_permissions_commandline}

完成以下步骤，使用命令行，授予用户查看帐户日志的访问权：

1. 在终端上，登录到 {{site.data.keyword.Bluemix_notm}} 帐户。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。

2. 检查用户是否是帐户成员。运行以下命令来获取帐户中用户的列表：

    ```
	ibmcloud account users
	```
    {: codeblock}	

	这将显示用户及其 GUID 的列表。

3. 如果用户不是帐户成员，请联系帐户所有者并请求邀请该用户加入帐户。有关更多信息，请参阅[邀请用户](/docs/iam?topic=iam-iamuserinv#iamuserinv)。

    **提示**：用于邀请用户加入帐户的命令如下：`ibmcloud iam account-user-invite USER_EMAIL`
		
4. 为用户分配策略。运行以下命令：

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	其中
    * USER_NAME 是用户的 {{site.data.keyword.Bluemix_notm}} 标识。
	* ROLE 是 IAM 角色。有效值为：*administrator*、*operator*、*editor* 和 *viewer*

5. 验证是否为用户分配了策略。运行以下命令来列出分配给用户的所有策略：

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## 使用 {{site.data.keyword.Bluemix_notm}} UI 向用户授予查看空间日志的许可权
{: #grant_permissions_ui_space}

要授予用户查看空间中日志的许可权，您必须为该用户分配 Cloud Foundry 角色，该角色描述了此用户可以在空间中使用 {{site.data.keyword.loganalysisshort}} 服务执行的操作。 

要授予用户使用 {{site.data.keyword.loganalysisshort}} 服务的许可权，请完成以下步骤：



1. 登录到 {{site.data.keyword.Bluemix_notm}} 控制台。

    打开 Web 浏览器并启动 {{site.data.keyword.Bluemix_notm}}“仪表板”：[http://bluemix.net ![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}
	
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 从菜单栏，单击**管理 > 帐户 > 用户**。 

    *用户*窗口显示用户列表，其中包含目前所选帐户的电子邮件地址。
	
3. 如果用户是帐户的成员，请从列表中选择用户名，或者从*操作*菜单中单击**管理用户**。

    如果用户不是帐户的成员，请参阅[邀请用户](/docs/iam?topic=iam-iamuserinv#iamuserinv)。

4. 选择 **Cloud Foundry 访问权**，然后选择组织。

    这将列出该组织中可用空间的列表。

5. 选择一个空间。然后，从菜单操作中，选择**编辑空间角色**。

6. 选择一个或多个空间角色。有效角色为：*管理者*、*开发者*和*审计员*
	
7. 单击**保存角色**。




