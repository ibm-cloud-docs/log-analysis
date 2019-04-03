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


# 获取 IAM 令牌
{: #auth_iam1}

要使用 {{site.data.keyword.loganalysisshort}} API 来管理可在帐户域中使用的日志，您必须使用认证令牌。使用 {{{site.data.keyword.Bluemix_notm}} CLI 以获取 IAM 令牌。令牌具有到期时间。
{:shortdesc}


## 获取 IAM 令牌
{: #iam_token_cli}

要使用 {{site.data.keyword.Bluemix_notm}} CLI 获取授权令牌，请在终端上完成以下步骤：

1. 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[下载并安装 {{site.data.keyword.Bluemix}} CLI](/docs/cli/index.html#overview)。
   
   如果 CLI 已安装，请继续执行下一步。
    
2. 登录到 {{site.data.keyword.Bluemix_notm}} 中的区域。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)。
	
3. 运行 `ibmcloud iam oauth-tokens` 命令以获取 IAM 令牌。

    ```
	ibmcloud iam oauth-tokens
	```
	{: codeblock}
	
	输出返回您在该空间和组织中认证用户标识时必须使用的 IAM 令牌。您可以将 IAM 令牌导出到 shell 变量，如 `$iam_token`。



**注**：使用令牌时，请从您在 API 调用中传递的令牌值中除去 *Bearer*。

