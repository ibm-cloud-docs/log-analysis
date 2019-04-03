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


# Provisionando o serviço de análise do log
{: #provision}

É possível provisionar o serviço {{site.data.keyword.loganalysisshort}} por meio da UI do {{site.data.keyword.Bluemix}} ou por meio da linha de comandos.
{:shortdesc}


## Provisionando por meio da UI
{: #ui}

Conclua as etapas a seguir para provisionar uma instância do serviço {{site.data.keyword.loganalysisshort}} no {{site.data.keyword.Bluemix_notm}}:

1. Efetue login em sua conta do {{site.data.keyword.Bluemix_notm}}.

    O painel do {{site.data.keyword.Bluemix_notm}} pode ser localizado em: [http://bluemix.net ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](http://bluemix.net){:new_window}.
    
	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.Bluemix_notm}} é aberta.

2. Clique em **Catálogo**. A lista dos serviços que estão disponíveis no {{site.data.keyword.Bluemix_notm}} é aberta.

3. Selecione a categoria **Ferramentas do desenvolvedor** para filtrar a lista de serviços que é exibida.

4. Clique no quadro **Análise do log**.

5. Selecione um plano de serviço. Por padrão, o plano **Lite** é configurado.

    Para obter mais informações sobre os planos de serviços, veja [Planos de serviços](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).
	
6. Clique em **Criar** para provisionar o serviço {{site.data.keyword.loganalysisshort}} no espaço do {{site.data.keyword.Bluemix_notm}} ao qual você está conectado.
  
 

## Provisionando por meio da CLI
{: #cli}

Conclua as etapas a seguir para provisionar uma instância do serviço {{site.data.keyword.loganalysisshort}} no {{site.data.keyword.Bluemix_notm}} por meio da linha de comandos:

1. [Pré-requisito] Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Instalando a CLI do {{site.data.keyword.Bluemix_notm}}](/docs/cli/index.html#overview).
   
   Se a CLI estiver instalada, continue com a próxima etapa.
    
2. Efetue login na região, organização e espaço no {{site.data.keyword.Bluemix_notm}} em que você deseja provisionar o serviço. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
	
3. Execute o comando `ibmcloud service create` para provisionar uma instância.

    ```
	ibmcloud create service_name service_plan service_instance_name
	```
	{: codeblock}
	
	Em que
	
	* service_name é o nome do serviço, isto é, **ibmLogAnalysis**.
	* service_plan é o nome do plano de serviço. Para obter uma lista de planos, veja [Planos de serviço](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).
	* service_instance_name é o nome que você deseja usar para a nova instância de serviço criada.

	Por exemplo, para criar uma instância do serviço {{site.data.keyword.loganalysisshort}} com o plano Lite, execute o comando a seguir:
	
	```
	serviço ibmcloud create ibmLogAnalysis padrão my_logging_svc
	```
	{: codeblock}
	
4. Verifique se o serviço foi criado com sucesso. Execute o comando a seguir:

    ```	
	Lista de serviços ibmcloud
	```
	{: codeblock}
	
	A saída da execução do comando é semelhante ao seguinte:
	
	```
    Getting services in org MyOrg / space MySpace as xxx@yyy.com...
    OK
    
    name                           service                  plan                   bound apps              last operation
    my_logging_svc                ibmLogAnalysis           standard                                        create succeeded
	```
	{: screen}

	



