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

# 가상 머신
{: #logging_vm_ov}

가상 머신(VM) 에 대한 로깅 기능은 자동으로 사용 가능하게 설정할 수 없습니다. 그러나 사용자의 VM이 로그 콜렉션에 로그를 전송하도록 구성할 수 있습니다. VM에서 {{site.data.keyword.loganalysisshort}} 서비스로 로그 데이터를 수집해서 전송하려면 다중 테넌트 Logstash 포워더(mt-logstash-forwarder)를 구성해야 합니다. 그러면 Kibana에서 로그를 보고, 필터링하며 분석할 수 있습니다.
{:shortdesc}


## 로그 수집
{: #log_ingestion2}

{{site.data.keyword.loganalysisshort}} 서비스는 여러 가지 플랜을 제공합니다. *Lite* 플랜을 제외한 모든 플랜에는 로그 콜렉션으로 로그를 전송할 수 있는 기능이 포함되어 있습니다. 플랜에 대한 자세한 정보는 [서비스 플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.

mt-logstash-forwarder를 사용하여 {{site.data.keyword.loganalysisshort}}에 로그를 전송할 수 있습니다. 자세한 정보는 [다중 테넌트 Logstash 포워더(mt-logstash-forwarder)를 사용하여 로그 데이터 전송](/docs/services/CloudLogAnalysis/how-to/send-data/send_data_mt.html#send_data_mt)을 참조하십시오.


## 로그 콜렉션
{: #log_collection2}

기본적으로 {{site.data.keyword.Bluemix_notm}}는 최대 3일 동안의 로그 데이터를 저장합니다.   

* 하루에 영역당 최대 500MB의 데이터가 저장됩니다. 500MB 상한을 넘는 로그는 버려집니다. 상한 분배는 매일 오전 12:30 UTC에
재설정됩니다.
* 최대 1.5GB의 데이터를 최대 3일 동안 검색할 수 있습니다. 로그 데이터는 1.5GB의 데이터에 도달하거나 3일 이후에 롤오버(FIFO)됩니다.

{{site.data.keyword.loganalysisshort}} 서비스는 필요한 기간 만큼 로그 콜렉션에 로그를 저장하도록 허용하는 추가 플랜을 제공합니다. 각 플랜의 가격에 대한 자세한 정보는 [서비스 플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.

* 로그 콜렉션에 로그를 보존하기 원하는 일 수를 정의하는 데 사용할 수 있는 로그 보존 정책을 구성할 수 있습니다. 자세한 정보는 [로그 보존 정책](/docs/services/CloudLogAnalysis/manage_logs.html#log_retention_policy)을 참조하십시오.
* 로그 콜렉션 CLI 또는 API를 사용하여 로그를 수동으로 삭제할 수 있습니다.


## 로그 검색
{: #log_search2}

기본적으로 Kibana를 사용하여 {{site.data.keyword.Bluemix_notm}}에서 하루에 최대 500MB의 로그를 검색할 수 있습니다. 

{{site.data.keyword.loganalysisshort}} 서비스는 여러 가지 플랜을 제공합니다. 각 플랜에는 각기 다른 로그 검색 기능이 있으며, 예를 들어 *로그 콜렉션* 플랜은 하루에 최대 1GB의 데이터를 검색하도록 허용합니다. 플랜에 대한 자세한 정보는 [서비스 플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.


## 로그 분석
{: #log_analysis}

로그 데이터를 분석하려면 Kibana를 사용하여 고급 분석 태스크를 수행하십시오. 오픈 소스 분석 및 시각화 플랫폼인 Kibana를 사용하여 다양한 그래프(예: 차트, 표)로 된 데이터를 모니터, 검색, 분석 및 시각화할 수 있습니다. 자세한 정보는 [Kibana에서 로그 분석](/docs/services/CloudLogAnalysis/kibana/analyzing_logs_Kibana.html#analyzing_logs_Kibana)을 참조하십시오.
