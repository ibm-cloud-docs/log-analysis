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


# 오류 메시지
{: #error_msgs}

{{site.data.keyword.Bluemix}}에서 {{site.data.keyword.loganalysisshort}} 서비스를 사용 중일 때 오류 메시지가 표시될 수 있습니다.
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**메시지 설명**

{{site.data.keyword.loganalysisfull}} 인스턴스 {Instance GUID}에 대한 Bluemix 영역 {Space GUID}에 할당된 일별 할당량에 도달했습니다. 현재 일별 할당량은 로그 검색 스토리지당 500MB이며, Kibana에서 검색될 수 있는 3일의 기간 동안 로그 검색 스토리지에 보존됩니다. 매일 로그 검색 스토리지에 추가 데이터를 저장하고 로그 콜렉션 스토리지에 모든 로그도 보존하도록 플랜을 업그레이드하려면 이 영역에 대한 {{site.data.keyword.loganalysisshort}} 서비스 플랜을 업그레이드하십시오. 서비스 플랜 및 플랜 업그레이드 방법에 대한 자세한 정보는 [플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.


**메시지 설명** 

Lite 서비스 플랜에 할당된 로그 검색 스토리지 할당량에 도달하면 ID *BXNLG020001W*가 포함된 메시지가 표시될 수 있습니다. Lite 플랜은 영역에서 {{site.data.keyword.loganalysisshort}} 서비스를 프로비저닝할 때 기본적으로 설정되는 무료 서비스 플랜입니다. 현재 일별 할당량은 로그 검색 스토리지당 500MB이며, Kibana에서 검색될 수 있는 3일의 기간 동안 로그 검색 스토리지에 보존됩니다.

**복구**

매일 로그 검색 스토리지에 추가 데이터를 저장하고 로그 콜렉션 스토리지에 모든 로그도 보존하도록 플랜을 업그레이드하려면 이 영역에 대한 {{site.data.keyword.loganalysisshort}} 서비스 플랜을 업그레이드하십시오. 서비스 플랜 및 플랜 업그레이드 방법에 대한 자세한 정보는 [플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.


## BXNLG020002W 
{: #BXNLG020002W}


**메시지 설명**

{{site.data.keyword.loganalysisfull}} 인스턴스 {Instance GUID}에 대한 Bluemix 영역 {Space GUID}에 할당된 일별 할당량에 도달했습니다.  현재 일별 할당량은 로그 검색 스토리지당 XXX이며, Kibana에서 검색될 수 있는 3일의 기간 동안 보존됩니다. 이는 로그 콜렉션 스토리지의 로그 보관 정책에 영향을 주지 않습니다. 매일 로그 검색 스토리지에 추가 데이터를 저장하도록 플랜을 업그레이드하려면 이 영역에 대한 {{site.data.keyword.loganalysisshort}} 서비스 플랜을 업그레이드하십시오. 서비스 플랜 및 플랜 업그레이드 방법에 대한 자세한 정보는 [플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.

XXX는 현재 플랜에 대해 검색 가능한 데이터의 크기를 표시합니다.

**메시지 설명** 

{{site.data.keyword.loganalysisfull}} 인스턴스 {Instance GUID}에 대한 영역 {Space GUID}에 할당된 일별 할당량에 도달했습니다.  현재 일별 할당량은 로그 검색 스토리지당 500MB, 2GB, 5GB 또는 10GB이며, Kibana에서 검색될 수 있는 3일의 기간 동안 보존됩니다. 이는 로그 콜렉션 스토리지의 로그 보관 정책에 영향을 주지 않습니다.

**복구**

매일 로그 검색 스토리지에 추가 데이터를 저장하도록 플랜을 업그레이드하려면 이 영역에 대한 {{site.data.keyword.loganalysisshort}} 서비스 플랜을 업그레이드하십시오. 서비스 플랜 및 플랜 업그레이드 방법에 대한 자세한 정보는 [플랜](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans)을 참조하십시오.




