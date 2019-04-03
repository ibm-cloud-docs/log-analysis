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


# UAA 토큰 가져오기
{: #auth_uaa}

{{site.data.keyword.loganalysisshort}} API를 사용하여 영역 도메인에서 사용 가능한 로그를 관리하려면 인증 토큰을 사용해야 합니다.
{:shortdesc}

		
## UAA 토큰 가져오기
{: #uaa_cli}


인증 토큰을 가져오려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}} CLI를 설치하십시오.

   자세한 정보는 [{{site.data.keyword.Bluemix}} CLI 다운로드 및 설치](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview)를 참조하십시오.
   
   CLI가 설치되면 다음 단계로 계속 진행하십시오.
    
2. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
	
3. `ibmcloud iam oauth-token` 명령을 실행하여 {{site.data.keyword.Bluemix_notm}} UAA 토큰을 가져오십시오.

    ```
	ibmcloud iam oauth-token
	```
	{: codeblock}
	
	이 출력은 해당 영역과 조직에서 사용자 ID를 인증하는 데 사용해야 하는 UAA 토큰을 리턴합니다.
	

**참고:** 이 토큰을 사용하는 경우 API 호출에서 전달하는 토큰 값에서 *Bearer*를 제거하십시오.
