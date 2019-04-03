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


# 플랜 변경
{: #change_plan}

{{site.data.keyword.Bluemix_notm}} UI를 통해, 또는 `ibmcloud service update` 명령을 실행하여 {{site.data.keyword.loganalysisshort}} 서비스 플랜을 변경할 수 있습니다. 플랜은 언제든지 업그레이드하거나 줄일 수 있습니다.
{:shortdesc}

## UI를 통해 서비스 플랜 변경
{: #change_plan_ui}

{{site.data.keyword.Bluemix_notm}} UI에서 서비스 플랜을 변경하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}([http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window})에 로그인하십시오. 

2. {{site.data.keyword.loganalysisshort}} 서비스가 사용 가능한 지역, 조직 및 영역을 선택하십시오.  

3. {{site.data.keyword.Bluemix_notm}} *대시보드*에서 {{site.data.keyword.loganalysisshort}} 서비스 인스턴스를 클릭하십시오. 
    
4. {{site.data.keyword.loganalysisshort}} 대시보드에서 **플랜** 탭을 선택하십시오.

    현재 플랜에 대한 정보가 표시됩니다.
	
5. 새 플랜을 선택하여 플랜을 업그레이드하거나 줄이십시오. 

6. **저장**을 클릭하십시오.




## CLI를 통해 서비스 플랜 변경
{: #change_plan_cli}

CLI를 통해 Bluemix의 서비스 플랜을 변경하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}}의 지역, 조직 및 영역에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login)을 참조하십시오.
	
2. `ibmcloud service list` 명령을 실행하여 현재 플랜을 확인하고, 영역에서 사용할 수 있는 서비스 목록에서 {{site.data.keyword.loganalysisshort}} 서비스 이름을 가져오십시오. 

    필드 **name**의 값은 플랜을 변경하는 데 사용해야 하는 값입니다. 

    예:
	
	```
	$ ibmcloud service list
    Invoking 'cf services'...

    Getting services in org MyOrg / space dev as xxx@ibm.com...
    OK

    name                           service                  plan             bound apps            last operation
    Log Analysis-m2                ibmLogAnalysis           premium                                update succeeded
    ```
	{: screen}
    
3. 플랜을 업그레이드하거나 줄이십시오. `ibmcloud service update` 명령을 실행하십시오.
    
	```
	ibmcloud service update service_name [-p new_plan]
	```
	{: codeblock}
	
	여기서 
	
	* *service_name*은 서비스의 이름입니다. `ibmcloud service list` 명령을 실행하여 값을 가져올 수 있습니다.
	* *new_plan*은 플랜의 이름입니다.
	
	여러 가지 플랜과 지원되는 해당 값이 다음 표에 나와 있습니다.
	
	<table>
	  <caption>표 1. 플랜 목록.</caption>
	  <tr>
	    <th>플랜</th>
	    <th>이름</th>
	  </tr>
	  <tr>
	    <td>Lite</td>
	    <td>standard</td>
	  </tr>
	  <tr>
	    <td>로그 콜렉션</td>
	    <td>premium</td>
	  </tr>
	  <tr>
	    <td>2GB/일 검색의 로그 콜렉션</td>
	    <td>premiumsearch2</td>
	  </tr>
	  <tr>
	    <td>5GB/일 검색의 로그 콜렉션</td>
	    <td>premiumsearch5</td>
	  </tr>
	  <tr>
	    <td>10GB/일 검색의 로그 콜렉션</td>
	    <td>premiumsearch10</td>
	  </tr>
	</table>
	
	예를 들어, *Lite* 플랜으로 플랜을 줄이려면 다음 명령을 실행하십시오.
	
	```
	ibmcloud service update "Log Analysis-m2" -p standard
    Updating service instance Log Analysis-m2 as xxx@ibm.com...
    OK
	```
	{: screen}

4. 새 플랜이 변경되었는지 확인하십시오. `ibmcloud service list` 명령을 실행하십시오.

  ```
	ibmcloud service list
	```
	{: codeblock}






