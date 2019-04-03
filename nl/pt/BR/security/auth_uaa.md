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


# Obtendo o token do UAA
{: #auth_uaa}

Para gerenciar os logs que estão disponíveis em um domínio de espaço usando a API do {{site.data.keyword.loganalysisshort}}, deve-se usar um token de autenticação.
{:shortdesc}

		
## Obtendo o token do UAA
{: #uaa_cli}


Para obter o token de autorização, conclua as etapas a seguir:

1. Instale a CLI do {{site.data.keyword.Bluemix_notm}}.

   Para obter mais informações, veja [Fazer download e instalar a CLI do {{site.data.keyword.Bluemix}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Se a CLI estiver instalada, continue com a próxima etapa.
    
2. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Execute o comando `ibmcloud iam oauth-token` para obter o token do UAA do {{site.data.keyword.Bluemix_notm}}.

    ```
	ibmcloud iam oauth-token
	```
	{: codeblock}
	
	A saída retorna o token UAA que se deve usar para autenticar seu ID do usuário nesse espaço e nessa organização.
	

**Nota:** ao usar o token, remova *Bearer* do valor do token que for passado em uma chamada API.
