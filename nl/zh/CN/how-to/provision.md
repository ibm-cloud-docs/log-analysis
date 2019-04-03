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


# 供应 Log Analysis 服务
{: #provision}

可以通过 {{site.data.keyword.Bluemix}} UI 或命令行供应 {{site.data.keyword.loganalysisshort}} 服务。
{:shortdesc}


## 通过 UI 供应
{: #ui}

要在 {{site.data.keyword.Bluemix_notm}} 中供应 {{site.data.keyword.loganalysisshort}} 服务的实例，请完成以下步骤：

1. 登录到 {{site.data.keyword.Bluemix_notm}} 帐户。

    {{site.data.keyword.Bluemix_notm}}“仪表板”位于：[http://bluemix.net![外部链接图标](../../../icons/launch-glyph.svg "外部链接图标")](http://bluemix.net){:new_window}。
    
	使用用户标识和密码登录后，{{site.data.keyword.Bluemix_notm}} UI 将打开。

2. 单击**目录**。这将打开 {{site.data.keyword.Bluemix_notm}} 上可用的服务的列表。

3. 选择 **Developer Tools** 类别以过滤显示的服务列表。

4. 单击 **Log Analysis** 磁贴。

5. 选择服务套餐。缺省情况下，已设置 **Lite** 套餐。


    有关服务套餐的更多信息，请参阅[服务套餐](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。
	
6. 单击**创建**以在您登录到的 {{site.data.keyword.Bluemix_notm}} 空间中供应 {{site.data.keyword.loganalysisshort}} 服务。
  
 

## 通过 CLI 供应
{: #cli}

要通过命令行在 {{site.data.keyword.Bluemix_notm}} 中供应 {{site.data.keyword.loganalysisshort}} 服务的实例，请完成以下步骤：

1. [先决条件] 安装 {{site.data.keyword.Bluemix_notm}} CLI。

   有关更多信息，请参阅[安装 {{site.data.keyword.Bluemix_notm}} CLI](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)。
   
   如果 CLI 已安装，请继续执行下一步。
    
2. 登录到 {{site.data.keyword.Bluemix_notm}} 中要供应服务的区域、组织和空间。 

    有关更多信息，请参阅[如何登录到 {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)。
	
3. 运行 `ibmcloud service create` 命令来供应实例。

    ```
	ibmcloud service create service_name service_plan service_instance_name
	```
	{: codeblock}
	
	其中
	
	* service_name 是服务的名称，即 **ibmLogAnalysis**。
	* service_plan 是服务套餐名称。有关套餐的列表，请参阅[服务套餐](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans)。
	* service_instance_name 是要用于所创建的新服务实例的名称。

	例如，要使用轻量套餐创建 {{site.data.keyword.loganalysisshort}} 服务实例，请运行以下命令：
	
	```
	ibmcloud service create ibmLogAnalysis standard my_logging_svc
	```
	{: codeblock}
	
4. 验证服务是否创建成功。运行以下命令：

    ```	
	ibmcloud service list
	```
	{: codeblock}
	
	运行此命令的输出如下所示：
	
	
	
	```
    Getting services in org MyOrg / space MySpace as xxx@yyy.com...
    OK

    
    name                           service                  plan                   bound apps              last operation
    my_logging_svc                ibmLogAnalysis           standard                                        create succeeded
	```
	{: screen}

	



