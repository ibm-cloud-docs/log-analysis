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


# Obtendo o token de criação de log
{: #logging_token}

Obtenha um token de criação de log para enviar logs para o serviço {{site.data.keyword.loganalysisshort}}. 
{:shortdesc}


## Obtendo o token de criação de log para enviar logs para um espaço usando a CLI do {{site.data.keyword.loganalysisshort}} 
{: #logging_token_la_cloud_cli}

Para obter o token de criação de log que pode ser usado para enviar logs para o serviço {{site.data.keyword.loganalysisshort}}, conclua as etapas a seguir:

1. Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Fazer download e instalar a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
   Se a CLI estiver instalada, continue com a próxima etapa.
    
2. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
3. Execute o comando a seguir:

    ```
	ibmcloud logging token-get
	```
	{: codeblock}

A saída retorna o token de criação de log.


## Obtendo o token de criação de log para enviar logs para um espaço usando a CLI do {{site.data.keyword.Bluemix_notm}} 
{: #logging_token_cloud_cli}

Para obter o token de criação de log que pode ser usado para enviar logs para o serviço {{site.data.keyword.loganalysisshort}}, conclua as etapas a seguir:

1. Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Fazer download e instalar a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
   Se a CLI estiver instalada, continue com a próxima etapa.
    
2. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
3. Crie uma chave de serviço no espaço em que o serviço {{site.data.keyword.loganalysisshort}} é provisionado. Execute os seguintes comandos:

    Liste os serviços para obter o nome da instância do {{site.data.keyword.loganalysisshort}} no espaço:
	
    ```
	Lista de serviços ibmcloud
	```
	{: codeblock}
	
	Por exemplo:
	
	```
	ibmcloud service list
    Invoking 'cf services'...

    Getting services in org lopezdsr_org / space dev as xxx@yyyy...
    OK

    name              service          plan       bound apps   last operation
    Log Analysis-vg   ibmloganalysis   standard                create succeeded
    ```
	{: screen}
	
	Crie uma chave. Use o valor de **name** para o nome do serviço e insira o nome de sua chave.
	
	```
	ibmcloud service key-create servicename KeyName 
	```
	{: codeblock}
	
	Por exemplo,
	
	```
	ibmcloud service key-create "Log Analysis-vg" mykey2
    Invoking 'cf create-service-key Log Analysis-vg mykey2'...

    Creating service key mykey2 for service instance Log Analysis-vg as xxx@yyyy...
    OK
    ```
	{: screen}
	
4. Obtenha o token de criação de log. Execute o comando a seguir:
	
	```
	ibmcloud service key-show name Keyname
	```
	{: codeblock}
	
	Por exemplo, 
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" 
    Invoking 'cf service-key Log Analysis-vg mykey2'...

    Obtendo a chave mykey2 para a instância de serviço Log Analysis-vg como xxx@yyyy...

    {
     "LOG_INGESTION_MTLJ_URL": "https://ingest-eu-fra.logging.bluemix.net:9091",
     "logging_token": "sdtghyrtfde4",
     "space_id": "12345678-avfg-erft-b1f2-2efrtgcb1744"
    }
    ```
	{: screen}
	
	Para obter o token de criação de log, é possível executar o comando a seguir:
	
	```
	ibmcloud service key-show "Log Analysis-vg" "mykey2" | tail -n +4 | jq -r .logging_token
    sdtghyrtfde4
	```
	{: screen}


	
## Obtendo o token de criação de log para enviar logs para um espaço usando a API do Log Analysis
{: #logging_token_api}


Para obter o token de criação de log que pode ser usado para enviar logs para o serviço {{site.data.keyword.loganalysisshort}}, conclua as etapas a seguir:

1. Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Fazer download e instalar a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
   Se a CLI estiver instalada, continue com a próxima etapa.
    
2. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
3. Obtenha o [token do UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#uaa_cli).

    Por exemplo, execute o comando `ibmcloud cf oauth-token` para obter o token UAA.

    ```
	ibmcloud cf oauth-token
	```
	{: codeblock}
	
	A saída retorna o token UAA que se deve usar para autenticar seu ID do usuário nesse espaço e nessa organização.

4. Obtenha o GUID do espaço.

   Para obter mais informações, veja [Como obter o GUID de um espaço](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid2).  
	
5. Exporte as variáveis a seguir: TOKEN e SPACEID.

    * *TOKEN* é o token oauth obtido na etapa anterior, excluindo Bearer.
	
	* *SPACEID* é o GUID do espaço obtido na etapa anterior. 
		
	Por exemplo,
	
	```
	export TOKEN="eyJhbGciOiJI....cGFzc3dvcmQiLCJjZiIsInVhYSIsIm9wZW5pZCJdfQ.JaoaVudG4jqjeXz6q3JQL_SJJfoIFvY8m-rGlxryWS8"
	export SPACEID="667fb895-abcd-defg-aaaa-cf4587341095"
	```
	{: screen}
	
6. Obtenha o token de criação de log. Execute o comando a seguir:
 
    ```
	curl -k -X GET  --header "X-Auth-Token: ${TOKEN}"  --header "X-Auth-Project-Id: s-${SPACEID}"  LOGGING_ENDPOINT/token
    ```
    {: codeblock}	
	
	Em que
	* SPACEID é o GUID do espaço no qual o serviço está em execução.
	* TOKEN é o token do UAA obtido em uma etapa anterior sem o prefixo bearer.
	* LOGGING_ENDPOINT é o terminal do {{site.data.keyword.loganalysisshort}} para a região do {{site.data.keyword.Bluemix_notm}} na qual a organização e o espaço estão disponíveis. O LOGGING_ENDPOINT é diferente por região. Para ver as URLs para os diferentes terminais, veja [Terminais](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).
	
    O comando retorna o token de criação de log que se deve usar para enviar logs para esse espaço.
	
