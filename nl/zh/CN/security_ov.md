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

# 安全性
{: #security_ov}

要控制允许用户执行的 {{site.data.keyword.loganalysisshort}} 操作，您必须向用户分配一个或多个角色。
{:shortdesc}

要使用 {{site.data.keyword.loganalysisshort}} 服务 API，您需要使用 UAA 令牌或 IAM 令牌。要向 {{site.data.keyword.loganalysisshort}} 服务发送日志，您需要日志记录令牌。


## 认证模型
{: #auth1}

要通过 CLI 或 API 使用 {{site.data.keyword.loganalysisshort}} 服务，您需要认证令牌。

{{site.data.keyword.loganalysisshort}} 服务支持以下认证模型：

* [UAA 认证](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)

    您仅可以使用 CLI 来管理 UAA 令牌。
	
* [IAM 认证](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)

    IAM 认证模型提供 UI、CLI 或 API 管理能力。 

**注**：UAA 令牌和 IAM 令牌会在一段时间后到期。 

## 角色
{: #roles3}

在 {{site.data.keyword.Bluemix_notm}} 中有两种类型的角色，控制在用户使用 {{site.data.keyword.loganalysisshort}} 服务时可以执行的操作：

* Cloud Foundry (CF) 角色：您通过分配一个或多个 CF 角色来控制用户可以执行的 {{site.data.keyword.loganalysisshort}} 操作。使用这些角色，您可以控制用户查看和管理空间或组织中日志的许可权。
* IAM 角色：您通过分配一个或多个 IAM 角色来控制用户可以执行的 {{site.data.keyword.loganalysisshort}} 操作。使用这些角色，您可以控制用户查看和管理帐户日志的许可权。 


下表列出角色的类型以及他们在 {{site.data.keyword.Bluemix_notm}} 中所控制的域：

<table>
  <caption>表 1. 每个域控制操作的角色类型</caption>
  <tr>
    <th></th>
	<th align="right">帐户</th>
    <th align="right">组织</th>
    <th align="right">空间</th>	
  </tr>
  <tr>
    <td align="left">CF 角色</td>
	<td align="center">否</td>
	<td align="center">是</td>
	<td align="center">是</td>
  </tr>
  <tr>
    <td align="left">IAM 角色</td>
	<td align="center">是</td>
	<td align="center">否</td>
	<td align="center">否</td>
  </tr>
</table>


## CF 角色
{: #bmx_roles}

下表列出每个 CF 角色使用 {{site.data.keyword.loganalysisshort}} 服务的特权：

<table>
  <caption>表 2. 使用 {{site.data.keyword.loganalysisshort}} 服务的 Cloud Foundry 角色和特权。</caption>
  <tr>
    <th>角色</th>
	<th>域</th>
	<th>访问特权</th>
  </tr>
  <tr>
    <td>管理者</td>
	<td>组织<br>空间</td>
	<td>所有 RESTful API</td>
  </tr>
  <tr>
    <td>开发者</td>
	<td>空间</td>
	<td>所有 RESTful API</td>
  </tr>
  <tr>
    <td>审计员</td>
	<td>组织<br>空间</td>
	<td>仅执行只读操作的 RESTful API，如查询日志。</td>
  </tr>
</table>


## IAM 角色
{: #iam_roles}

下表列出每个 IAM 角色使用 {{site.data.keyword.loganalysisshort}} 服务的特权：

<table>
  <caption>表 3. 使用 {{site.data.keyword.loganalysisshort}} 服务的 IAM 角色和特权。</caption>
  <tr>
    <th>角色</th>
	<th>特权</th>
  </tr>
  <tr>
    <td>管理员</td>
	  <td>查看空间中或帐户级别的日志的相关信息。<br>将日志下载到本地文件，或者通过管道将日志传递到其他程序，例如 Elastic 堆栈。<br>显示空间或帐户中可用的日志的保留期。<br>更新空间或帐户中可用的日志的保留期。<br>列出活动会话及其标识。<br>创建可用于下载日志的会话。<br>删除由会话标识指定的会话。<br>显示单个会话的状态。<br>删除日志。</td>
  </tr>
  <tr>
    <td>编辑者</td>
	  <td>查看空间中或帐户级别的日志的相关信息。<br>将日志下载到本地文件，或者通过管道将日志传递到其他程序，例如 Elastic 堆栈。<br>显示空间或帐户中可用的日志的保留期。<br>更新空间或帐户中可用的日志的保留期。<br>列出活动会话及其标识。<br>创建可用于下载日志的会话。<br>删除由会话标识指定的会话。<br>显示单个会话的状态。<br>删除日志。</td>
  </tr>
  <tr>
    <td>操作员</td>
	  <td>查看空间中或帐户级别的日志的相关信息。<br>显示空间或帐户中可用的日志的保留期。<br>列出活动会话及其标识。<br>显示单个会话的状态。<br>将日志下载到本地文件，或者通过管道将日志传递到其他程序，例如 Elastic 堆栈。<br>创建可用于下载日志的会话。<br>删除由会话标识指定的会话。</td>
  </tr>
  <tr>
    <td>查看者</td>
	  <td>查看空间中或帐户级别的日志的相关信息。<br>显示空间或帐户中可用的日志的保留期。<br>列出活动会话及其标识。<br>显示单个会话的状态。</td>
  </tr>
</table>

下表显示 API、服务操作和 {{site.data.keyword.loganalysisshort}} 服务所使用的 IAM 角色之间的关系。

<table>
  <caption>表 4. API、服务操作和 IAM 角色之间的关系。</caption>
  <tr>
    <th>API</th>
	<th>操作</th>
	<th>IAM 角色</th>
	<th>描述</th>
  </tr>
  <tr>
    <td>DELETE /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_delete</td>
	<td>管理员、编辑者</td>
	<td>删除日志。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs</td>
    <td>ibmcloud-log-analysis.domain.log_read</td>
	<td>管理员、编辑者、查看者</td>
	<td>查看 {{site.data.keyword.Bluemix_notm}} 空间中或帐户级别的日志的相关信息。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/download</td>
    <td>ibmcloud-log-analysis.domain.log_download</td>
	<td>管理员、编辑者</td>
	<td>将日志下载到本地文件，或者通过管道将日志传递到其他程序，例如 Elastic 堆栈。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_read</td>
    <td>管理员、编辑者、查看者</td>
    <td>显示 {{site.data.keyword.Bluemix_notm}} 空间或帐户中可用的日志的保留期。</td>
  </tr>
  <tr>
    <td>PUT /v1/logging/logs/retention</td>
    <td>ibmcloud-log-analysis.domain.policy_write</td>
    <td>管理员、编辑者</td>
    <td>更新 {{site.data.keyword.Bluemix_notm}} 空间或帐户中可用的日志的保留期。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>管理员、编辑者、查看者</td>
    <td>列出活动会话及其标识。</td>
  </tr>
  <tr>
    <td>POST /v1/logging/sessions</td>
    <td>ibmcloud-log-analysis.domain.session_write</td>
    <td>管理员、编辑者</td>
    <td>创建可用于下载日志的会话。</td>
  </tr>
  <tr>
    <td>DELETE /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_delete</td>
    <td>管理员、编辑者</td>
    <td>删除由会话标识指定的会话。</td>
  </tr>
  <tr>
    <td>GET /v1/logging/sessions/{id}</td>
    <td>ibmcloud-log-analysis.domain.session_read</td>
    <td>管理员、编辑者、查看者</td>
    <td>显示单个会话的状态。</td>
  </tr>
</table>

## 使用 API 获取认证令牌以管理日志
{: #get_token}

要使用 {{site.data.keyword.loganalysisshort}} API 来管理日志，您必须使用认证令牌。 

**使用空间域中可用的日志**

* 使用 {{site.data.keyword.loganalysisshort}} CLI 以获取 UAA 令牌。 
* 令牌具有到期时间。 

有关更多信息，请参阅[获取 UAA 令牌](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)。

**使用帐户域中可用的日志**

* 使用 {{{site.data.keyword.Bluemix_notm}} CLI 以获取 IAM 令牌。 
* 令牌具有到期时间。 

有关更多信息，请参阅[获取 IAM 令牌](/docs/services/CloudLogAnalysis/security/auth_iam.html#auth_iam1)。


## 获取日志记录令牌以将日志发送到 Log Analysis
{: #get_logging_token}

要向 {{site.data.keyword.loganalysisshort}} 服务发送日志，您需要日志记录令牌。 

要向空间域发送日志，请选择以下任何一种方法：

* [使用 {{site.data.keyword.Bluemix_notm}} 命令 ibmcloud 服务，获取日志记录令牌以向空间发送日志](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_cloud_cli)
* [使用 Log Analysis CLI 获取日志记录令牌以向空间发送日志](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_la_cloud_cli)
* [使用 Log Analysis API 获取日志记录令牌以向空间发送日志](/docs/services/CloudLogAnalysis/security/logging_token.html#logging_token_api)


## 授予用户使用日志的许可权
{: #grant_permissions1}

要使用户能够管理日志或查看日志，必须在 {{site.data.keyword.Bluemix_notm}} 中授予用户使用 {{site.data.keyword.loganalysisshort}} 服务的许可权。

* 有关管理日志所需的许可权的信息，请参阅[用户管理日志所需的角色](/docs/services/CloudLogAnalysis/manage_logs.html#roles1)。
* 有关查看日志所需的许可权的信息，请参阅[用户查看日志所需的角色](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#roles)。

有关如何授予许可权的更多信息，请参阅：

* [通过 {{site.data.keyword.Bluemix_notm}} UI 向用户分配 IAM 策略](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions)。
* [使用命令行向用户分配 IAM 策略](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_commandline)。
* [使用 {{site.data.keyword.Bluemix_notm}} UI 向用户授予查看空间日志的许可权](/docs/services/CloudLogAnalysis/security/grant_permissions.html#grant_permissions_ui_space)。


