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


# Calculando a cota de procura e o uso diário
{: #quota}

Para obter a cota e uso diário atual de um domínio de logs do serviço {{site.data.keyword.loganalysisshort}}, é possível executar um comando cURL. 
{:shortdesc}

## Calculando a cota de procura e o uso diário usando a CLI
{: #quota_cli}

Conclua as etapas a seguir:

1. Efetue login na {{site.data.keyword.Bluemix_notm}}.

    Por exemplo, para efetuar login no Sul dos EUA, execute o comando:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Execute o comando da CLI `ibmcloud logging quota-usage-show`. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    Em que 

    * Os valores RESOURCE_TYPE válidos são os seguintes: space, account
    * RESOURCE_ID é o GUID da conta ou do espaço para o qual você deseja obter o uso de cotas.


Por exemplo, para mostrar o uso de cota de uma conta, execute o comando a seguir:

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage   
524288000         0   
```
{: screen}

Para mostrar o uso de cota de um espaço, execute o comando a seguir:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage   
524288000         6774014   
```
{: screen}


## Obtendo o histórico de cota de procura usando a CLI
{: #quota_history_cli}


Conclua as etapas a seguir:

1. Efetue login na {{site.data.keyword.Bluemix_notm}}.

    Por exemplo, para efetuar login no Sul dos EUA, execute o comando:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Execute o comando da CLI `ibmcloud logging quota-usage-show` com o parâmetro `-s`. 

    ```
    ibmcloud logging quota-usage-show  [ -r, -- resource-type RESOURCE_TYPE ][-i,--resource-id RESOURCE_ID]  [ -s, -- history ]
    ```
    {: codeblock}

    Em que 

    * Os valores RESOURCE_TYPE válidos são os seguintes: space, account
    * RESOURCE_ID é o GUID da conta ou do espaço para o qual você deseja obter o uso de cotas.

Por exemplo,

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744...
OK

Date Allotmant Usage 2018.02.28 524288000 80405926 2018.03.06 524288000 18955540 2018.03.05 524288000 47262944 2018.03.08 524288000 18311338 2018.03.01 524288000 82416831 2018.03.03 524288000 75045462 2018.03.07 524288000 17386278 2018.03.02 524288000 104316444 2018.03.04 524288000 73125223   
```
{: screen}



## Calculando a cota de procura e o uso diário de uma conta usando a API
{: #account}

Conclua as etapas a seguir:

1. Efetue login na {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Obtenha o ID da conta. Execute o comando a seguir:

    ```
	Contas ibmcloud iam
	```
    {: codeblock}	

	Uma lista de contas com seus GUIDs é exibida.
	
	Exporte o ID da conta para uma variável shell. Por exemplo:
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. Obtenha o token UAA. 

    Para obter mais informações, veja [Obtendo o token do UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exporte o token do UAA para uma variável shell. Não inclua `Bearer`. Por exemplo:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Obtenha a cota do domínio e o uso atual. Execute o comando a seguir:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	em que *ENDPOINT* é diferente por região. Para obter uma lista de terminais por região, veja [Terminais de criação de log](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).
	
	Por exemplo, execute o comando cURL para obter a cota para a conta na região Sul dos EUA:
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	O resultado inclui as informações sobre a cota e o uso diários.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "uso": {
        "dailyallotment": 524288000, "current": 2115811531 }
    }
    ```
    {: screen}

	
## Calculando a cota de procura e o uso diário de um espaço usando a API
{: #space1}

Conclua as etapas a seguir:

1. Efetue login na {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Obtenha o ID do espaço.

    Para obter mais informações, veja [Como obter o GUID de um espaço](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid).
	
	Exporte o ID do espaço para uma variável shell. Por exemplo:
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. Obtenha o token UAA. 

    Para obter mais informações, veja [Obtendo o token do UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exporte o token do UAA para uma variável shell. Não inclua `Bearer`. Por exemplo:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Obtenha a cota do domínio e o uso atual. Execute o comando a seguir:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	em que *ENDPOINT* é diferente por região. Para obter uma lista de terminais por região, veja [Terminais de criação de log](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).

    Por exemplo, execute o comando cURL a seguir para obter a cota e uso de um domínio de espaço na região Sul dos EUA:
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	O resultado inclui as informações sobre a cota e o uso diários.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "uso": {
        "dailyallotment": 524288000, "current": 2115811531 }
    }
    ```
    {: screen}



