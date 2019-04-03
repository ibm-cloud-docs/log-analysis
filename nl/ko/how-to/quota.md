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


# 검색 할당량 및 일별 사용량 계산
{: #quota}

{{site.data.keyword.loganalysisshort}} 서비스의 로그 도메인에 대한 할당량과 현재 일별 사용량을 가져오려면 cURL 명령을 실행할 수 있습니다. 
{:shortdesc}

## CLI를 사용하여 검색 할당량 및 일별 사용량 계산
{: #quota_cli}

다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}에 로그인하십시오.

    예를 들어 미국 남부에 로그인하려면 다음 명령을 실행하십시오.

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

2. `ibmcloud logging quota-usage-show` cli 명령을 실행하십시오. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    여기서 

    * 올바른 RESOURCE_TYPE 값은 영역, 계정입니다.
    * RESOURCE_ID는 할당량 사용량을 가져오려는 계정 또는 영역의 GUID입니다.


예를 들어 계정의 할당량 사용량을 표시하려면 다음 명령을 실행하십시오.

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage   
524288000         0   
```
{: screen}

영역의 할당량 사용량을 표시하려면 다음 명령을 실행하십시오.

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage   
524288000         6774014   
```
{: screen}


## CLI를 사용하여 검색 할당량 히스토리 얻기
{: #quota_history_cli}


다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}에 로그인하십시오.

    예를 들어 미국 남부에 로그인하려면 다음 명령을 실행하십시오.

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

2. 매개변수 `-s`가 포함된 `ibmcloud logging quota-usage-show` cli 명령을 실행하십시오. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    여기서 

    * 올바른 RESOURCE_TYPE 값은 영역, 계정입니다.
    * RESOURCE_ID는 할당량 사용량을 가져오려는 계정 또는 영역의 GUID입니다.

예:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage   
2018.02.28   524288000   80405926   
2018.03.06   524288000   18955540   
2018.03.05   524288000   47262944   
2018.03.08   524288000   18311338   
2018.03.01   524288000   82416831   
2018.03.03   524288000   75045462   
2018.03.07   524288000   17386278   
2018.03.02   524288000   104316444   
2018.03.04   524288000   73125223   
```
{: screen}



## API를 사용하여 계정의 검색 할당량 및 일별 사용량 계산
{: #account}

다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

2. 계정 ID를 가져오십시오. 다음 명령을 실행하십시오.

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	계정 및 해당 GUID의 목록이 표시됩니다.
	
	계정 ID를 쉘 변수로 내보내십시오. 예:
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. UAA 토큰을 가져오십시오. 

    자세한 정보는 [UAA 토큰 가져오기](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)를 참조하십시오.

    UAA 토큰을 쉘 변수로 내보내십시오. `Bearer`를 포함시키지 마십시오. 예:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. 도메인의 할당량 및 현재 사용량을 가져오십시오. 다음 명령을 실행하십시오.

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	여기서 *ENDPOINT*는 지역에 따라 다릅니다. 지역별 엔드포인트의 목록은 [로깅 엔드포인트](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints)를 참조하십시오.
	
	예를 들어 미국 남부 지역에서 계정에 대한 할당량을 가져오려면 cURL 명령을 실행하십시오.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	이 결과에 일별 할당량과 사용량에 대한 정보가 포함됩니다.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}

	
## API를 사용하여 영역의 검색 할당량 및 일별 사용량 계산
{: #space1}

다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

2. 영역 ID를 가져오십시오.

    자세한 정보는 [영역의 GUID를 가져오는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid)을 참조하십시오.
	
	영역 ID를 쉘 변수로 내보내십시오. 예:
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. UAA 토큰을 가져오십시오. 

    자세한 정보는 [UAA 토큰 가져오기](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa)를 참조하십시오.

    UAA 토큰을 쉘 변수로 내보내십시오. `Bearer`를 포함시키지 마십시오. 예:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. 도메인의 할당량 및 현재 사용량을 가져오십시오. 다음 명령을 실행하십시오.

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	여기서 *ENDPOINT*는 지역에 따라 다릅니다. 지역별 엔드포인트의 목록은 [로깅 엔드포인트](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints)를 참조하십시오.

    예를 들어 미국 남부 지역의 영역 도메인에 대한 할당량과 사용량을 가져오려면 다음 cURL 명령을 실행하십시오.
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	이 결과에 일별 할당량과 사용량에 대한 정보가 포함됩니다.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}



