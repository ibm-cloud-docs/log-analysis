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

# 로그 관리 및 계정 로그 보기를 위한 권한 부여
{: #grant_permissions}

{{site.data.keyword.Bluemix}}에서는 사용자에게 하나 이상의 IAM 역할을 지정할 수 있습니다. 이러한 역할은 사용자가 {{site.data.keyword.loganalysisshort}} 서비스를 사용하여 수행할 수 있는 태스크를 정의합니다.  
{:shortdesc}

예를 들면, 특정 사용자에게 로그를 관리할 수 있도록 **운영자** 역할을 부여할 수 있습니다. 사용자가 계정 로그를 볼 수 있도록 하려는 경우에는 **뷰어** 역할을 부여할 수 있습니다. 자세한 정보는 [IAM 역할](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles)을 참조하십시오.

**참고:** 

* 사용자에게 로그를 관리하고 계정 로그를 볼 수 있는 권한을 부여하려면 사용자는 계정의 다른 사용자에게 정책을 지정할 수 있는 권한이 있어야 하거나 계정 소유자여야 합니다. 계정 소유자가 아닌 경우 편집자, 운영자 또는 관리자 역할이 있는 IAM 정책이 있어야 합니다.
* 사용자에게 영역의 로그를 볼 수 있는 권한을 부여하려면 해당 사용자에게 이 사용자가 영역에서 {{site.data.keyword.loganalysisshort}} 서비스에 대해 수행할 수 있는 조치를 설명하는 Cloud Foundry 역할을 사용자에게 지정하기 위한 조직 및 영역의 권한이 있어야 합니다. 

## {{site.data.keyword.Bluemix_notm}} UI를 통해 사용자에게 IAM 정책 지정
{: #grant_permissions_ui_account}

{{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행할 권한을 사용자에게 부여하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오.

    웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드를 실행하십시오. [http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window}
	
	사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

2. 메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오. 

    *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
3. 사용자가 계정의 구성원인 경우 목록에서 사용자 이름을 선택하거나 *조치* 메뉴에서 **사용자 관리**를 클릭하십시오.

    사용자가 계정의 구성원이 아닌 경우 [사용자 초대](/docs/iam/iamuserinv.html#iamuserinv)를 참조하십시오.

4. **액세스 정책** 섹션에서 **액세스 권한 지정**을 클릭한 후 **리소스에 대한 액세스 권한 지정**을 선택하십시오.

    *사용자에 리소스 액세스 권한 지정** 창이 열립니다.

5. 정책에 대한 정보를 입력하십시오. 다음 표는 정책을 정의하는 데 필요한 필드를 나열합니다. 

    <table>
	  <caption>IAM 정책을 구성하는 필드 목록입니다.</caption>
	  <tr>
	    <th>필드</th>
		<th>값</th>
	  </tr>
	  <tr>
	    <td>서비스</td>
		<td>*IBM Cloud Log Analysis*</td>
	  </tr>	  
	  <tr>
	    <td>지역</td>
		<td>사용자에게 로그 작업을 수행하기 위한 액세스 권한을 부여할 지역을 지정할 수 있습니다. 하나 이상의 지역을 개별적으로 선택하거나 **모든 현재 지역**을 선택하여 모든 지역에 대한 액세스 권한을 부여하십시오.</td>
	  </tr>
	  <tr>
	    <td>서비스 인스턴스</td>
		<td>*모든 서비스 인스턴스*를 선택하십시오.</td>
	  </tr>
	  <tr>
	    <td>역할</td>
		<td>하나 이상의 IAM 역할을 선택하십시오. <br>올바른 역할: *관리자*, *운영자*, *편집자* 및 *뷰어*. <br>각 역할에 허용되는 조치에 대한 자세한 정보는 [IAM 역할](/docs/services/CloudLogAnalysis/security_ov.html#iam_roles)을 참조하십시오.
		</td>
	  </tr>
     </table>
	
6. **지정**을 클릭하십시오.
	
구성하는 정책을 선택한 지역에 적용할 수 있습니다. 


## 명령행을 사용하여 사용자에게 IAM 정책 지정
{: #grant_permissions_commandline}

명령행을 통해 계정 로그를 볼 수 있는 액세스 권한을 사용자에게 부여하려면 다음 단계를 완료하십시오.

1. 터미널에서 {{site.data.keyword.Bluemix_notm}} 계정에 로그인하십시오. 

    자세한 정보는 [{{site.data.keyword.Bluemix_notm}}에 로그인하는 방법](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login)을 참조하십시오.

2. 사용자가 계정의 구성원인지 확인하십시오. 다음 명령을 실행하여 계정의 사용자 목록을 가져오십시오.

    ```
	ibmcloud account users
	```
    {: codeblock}	

	사용자 및 해당 GUID의 목록이 표시됩니다.

3. 사용자가 계정의 구성원이 아닌 경우 계정 소유자에게 문의하여 해당 사용자를 해당 계정에 초대하도록 요청하십시오. 자세한 정보는 [사용자 초대](/docs/iam/iamuserinv.html#iamuserinv)를 참조하십시오.

    **팁:** 사용자를 계정에 초대하는 명령은 `ibmcloud iam account-user-invite USER_EMAIL`입니다.
		
4. 사용자에게 정책을 지정하십시오. 다음 명령을 실행하십시오.

    ```
    ibmcloud iam user-policy-create USER_NAME --roles ROLE --service-name ibmloganalysis
	```
	{: codeblock}

	여기서
    * USER_NAME은 사용자의 {{site.data.keyword.Bluemix_notm}} ID입니다.
	* ROLE은 IAM 역할입니다. 올바른 값은 *관리자*, *운영자*, *편집자* 및 *뷰어*입니다.

5. 사용자에게 정책이 지정되었는지 확인하십시오. 사용자에게 지정된 모든 정책을 나열하려면 다음 명령을 실행하십시오.

    ```
    ibmcloud iam user-policies USER_NAME
	```
	{: codeblock}




## {{site.data.keyword.Bluemix_notm}} UI를 사용하여 사용자에게 영역 로그를 볼 수 있는 권한 부여
{: #grant_permissions_ui_space}

사용자에게 영역의 로그를 볼 수 있는 권한을 부여하려면 해당 사용자에게 이 사용자가 영역에서 {{site.data.keyword.loganalysisshort}} 서비스로 수행할 수 있는 조치를 설명하는 Cloud Foundry 역할을 지정해야 합니다. 

{{site.data.keyword.loganalysisshort}} 서비스에 대한 작업을 수행할 권한을 사용자에게 부여하려면 다음 단계를 완료하십시오.

1. {{site.data.keyword.Bluemix_notm}} 콘솔에 로그인하십시오.

    웹 브라우저를 열고 {{site.data.keyword.Bluemix_notm}} 대시보드를 실행하십시오. [http://bluemix.net ![외부 링크 아이콘](../../../icons/launch-glyph.svg "외부 링크 아이콘")](http://bluemix.net){:new_window}
	
	사용자 ID 및 비밀번호를 사용하여 로그인하면 {{site.data.keyword.Bluemix_notm}} UI가 열립니다.

2. 메뉴 표시줄에서 **관리 > 계정 > 사용자**를 클릭하십시오. 

    *사용자* 창에 현재 선택한 계정의 이메일 주소와 함께 사용자 목록이 표시됩니다.
	
3. 사용자가 계정의 구성원인 경우 목록에서 사용자 이름을 선택하거나 *조치* 메뉴에서 **사용자 관리**를 클릭하십시오.

    사용자가 계정의 구성원이 아닌 경우 [사용자 초대](/docs/iam/iamuserinv.html#iamuserinv)를 참조하십시오.

4. **Cloud Foundry 액세스**를 선택한 후 조직을 선택하십시오.

    해당 조직에서 사용 가능한 영역의 목록이 나열됩니다.

5. 하나의 영역을 선택하십시오. 그런 다음 메뉴 조치에서 **영역 역할 편집**을 선택하십시오.

6. 하나 이상의 영역 역할을 선택하십시오. 올바른 역할은 *관리자*, *개발자* 및 *감사자*입니다.
	
7. **역할 저장**을 클릭하십시오.




