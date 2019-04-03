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


# 규제 준수
{: #compliance}

[{{site.data.keyword.Bluemix}}는 빌드된 클라우드 플랫폼 및 서비스를 IBM의 엄격한 보안 표준에 제공합니다.](/docs/security/compliance.html#compliance) {{site.data.keyword.loganalysislong}} 서비스는 {{site.data.keyword.Bluemix_notm}}를 위해 빌드된 DevOps 서비스입니다. 
{:shortdesc}


## 일반 개인정보 보호법률(General Data Protection Regulation)

GDPR(General Data Protection Regulation)은 전세계 모든 곳에서 이 데이터를 호스팅하고 ‘처리’하는데 엄격한 규칙을 부과하면서 EU의 조화된 데이터 보호 법 프레임워크 작성을 추구하고 개인용 데이터의 제어를 다시 시민에게 돌려 주는 것을 목표로 합니다. 또한 규제는 EU 내부 및 외부에서 개인용 데이터의 자유로운 이동과 관련된 규칙을 도입합니다. 

**면책사항:** {{site.data.keyword.loganalysisshort}} 서비스는 {{site.data.keyword.Bluemix_notm}}의 사용자 계정에서 실행되는 클라우드 리소스 및 {{site.data.keyword.Bluemix_notm}} 외부에서 전송할 수 있는 로그의 로그 레코드를 저장하고 표시합니다. Cloud Service를 지원할 수 있는 {{site.data.keyword.IBM_notm}}을 비롯한 엔터프라이즈 내의 기타 사용자가 이 데이터에 액세스할 수 있으므로 개인정보(PI)는 {{site.data.keyword.loganalysisshort}}에 저장된 로그 항목에 포함되지 않아야 합니다.

### 지역
{: #regions}

{{site.data.keyword.loganalysisshort}} 서비스는 이 서비스를 사용할 수 있는 {{site.data.keyword.Bluemix_notm}} 퍼블릭 지역의 GDPR을 준수합니다.


### 데이터 보존
{: #data_retention}

{{site.data.keyword.loganalysisshort}} 서비스에는 데이터를 저장할 수 있는 두 개의 데이터 저장소가 포함됩니다. 

* 로그 검색 - Kibana를 통해 분석에 사용할 수 있는 로그 데이터를 호스팅합니다.
* 로그 콜렉션 - 장기 스토리지를 위해 로그 데이터를 호스팅합니다.

{{site.data.keyword.loganalysisshort}} 서비스 플랜에 따라 데이터는 로그 검색 또는 로그 검색 및 로그 콜렉션에 저장됩니다. 표준 또는 Lite 플랜은 로그 검색의 데이터만 저장합니다. 나머지 플랜은 로그 검색 및 로그 콜렉션의 데이터를 저장합니다.

* 로그 검색에 저장된 로그는 3일 동안 보관됩니다.
* 로그 콜렉션에 저장된 로그는 보존 정책을 구성하거나 해당 로그를 수동으로 삭제할 때까지 보관됩니다. 기본적으로, 로그는 로그 콜렉션에 무기한 보관됩니다.



### 데이터 삭제
{: #data_deletion}

다음 정보를 고려하십시오.

* 로그 검색에 저장된 로그는 3일 이후에 삭제됩니다.

* 로그 콜렉션에 저장된 로그는 보존 정책을 구성하거나 해당 로그를 수동으로 삭제할 때 며칠 후에 삭제됩니다. 

    로그 콜렉션에 로그를 보존하기 원하는 일 수를 정의하기 위한 로그 보존 정책을 구성할 수 있습니다. 자세한 정보는 [{{site.data.keyword.Bluemix_notm}} 플러그인을 사용하여 로그 보존 정책 보기 및 구성](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy)을 참조하십시오.

    [로그 콜렉션 API](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} 또는 [로그 콜렉션 CLI](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window}를 사용하여 로그 콜렉션에서 로그를 수동으로 삭제할 수 있습니다. 

    CLI를 사용하여 로그 콜렉션에서 로그를 수동으로 삭제할 수 있습니다. 자세한 정보는 [{{site.data.keyword.Bluemix_notm}} 플러그인을 사용한 ibmcloud logging log-delete](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs)를 참조하십시오.


유료 플랜에서 표준 또는 Lite 플랜으로 변경하는 경우 로그 콜렉션의 로그가 약 1일 후에 삭제됩니다.

언제라도 지원 티켓을 열고 로그 검색 및 로그 콜렉션에서 모든 데이터가 삭제되도록 요청할 수 있습니다. IBM 지원 티켓 열기에 대한 정보는 [지원 문의](/docs/get-support?topic=get-support-getting-customer-support#getting-customer-support)를 참조하십시오.



### 자세한 정보
{: #info}

자세한 정보는 다음을 참조하십시오.

[{{site.data.keyword.Bluemix_notm}} 보안 규제 준수](/docs/security/compliance.html#compliance)

[GDPR - {{site.data.keyword.IBM_notm}} 공식 페이지](https://www.ibm.com/data-responsibility/gdpr/)



