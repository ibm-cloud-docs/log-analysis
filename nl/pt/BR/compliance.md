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


# Conformidade
{: #compliance}

[O {{site.data.keyword.Bluemix}} fornece uma plataforma de nuvem e serviços que são construídos para padrões de segurança rigorosos da IBM.](/docs/security/compliance.html#compliance). O serviço {{site.data.keyword.loganalysislong}} é um serviço DevOps construído para o {{site.data.keyword.Bluemix_notm}}. 
{:shortdesc}


## Regulamento Geral de Proteção de Dados

O General Data Protection Regulation (GDPR) procura criar uma estrutura harmonizada de lei de proteção de dados em toda a UE e visa devolver aos cidadãos o controle de seus dados pessoais, impondo regras rígidas aos que hospedam e 'processam' esses dados, em qualquer lugar do mundo. O regulamento também introduz regras relativas à livre circulação de dados pessoais dentro e fora da UE. 

**Renúncia de responsabilidade:** o serviço {{site.data.keyword.loganalysisshort}} armazena e exibe registros de log de recursos em nuvem que são executados em sua conta no {{site.data.keyword.Bluemix_notm}} e de logs que você pode enviar de fora do {{site.data.keyword.Bluemix_notm}}. As informações pessoais (PI) não devem ser incluídas em nenhuma das entradas de log armazenadas no {{site.data.keyword.loganalysisshort}}, pois esses dados são acessíveis a outros usuários da empresa, assim como para a {{site.data.keyword.IBM_notm}} poder suportar o Serviço de nuvem.

### Regiões
{: #regions}

O serviço {{site.data.keyword.loganalysisshort}} é compatível com o GDPR nas regiões do {{site.data.keyword.Bluemix_notm}} Public em que o serviço está disponível.


### Retenção de Dados
{: #data_retention}

O serviço {{site.data.keyword.loganalysisshort}} inclui 2 repositórios de dados nos quais os dados podem ser armazenados: 

* Procura de log, que hospeda os dados de log disponíveis para análise por meio do Kibana.
* Coleção de logs, que hospeda os dados do log para armazenamento de longo prazo.

Dependendo do plano de serviço do {{site.data.keyword.loganalysisshort}}, os dados são armazenados em Procura de log ou em Procura de log e Coleção de logs. O plano padrão ou Lite só armazena dados em Procura de log. O restante dos planos armazena dados em Procura de log e em Coleção de logs.

* Os logs armazenados em Procura de log são mantidos por 3 dias.
* Os logs armazenados em Coleção de logs são mantidos até você configurar uma política de retenção ou excluí-los manualmente. Por padrão, os logs são mantidos indefinidamente na Coleção de logs.



### Exclusão de dados
{: #data_deletion}

Considere as seguintes informações:

* Os logs armazenados em Procura de log são excluídos após 3 dias.

* Os logs armazenados em Coleção de logs são excluídos após um número de dias em que você configurar uma política de retenção ou quando excluí-los manualmente. 

    É possível configurar uma política de retenção de log para definir o número de dias que você deseja manter os logs na Coleção de logs. Para obter mais informações, veja [Visualizando e configurando a política de retenção de log usando o plug-in do {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/configuring_retention_policy_cloud.html#configuring_retention_policy).

    É possível usar a [API de Coleção de logs](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} ou a [CLI de Coleção de logs](/docs/services/CloudLogAnalysis/reference/log_analysis_cli_cloud.html#log_analysis_cli){: new_window} para excluir logs manualmente da Coleção de logs. 

    É possível usar a CLI para excluir os logs manualmente da Coleção de logs. Para obter mais informações, veja [ibmcloud logging log-delete usando o plug-in do {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs/deleting_logs_cloud.html#deleting_logs).


Se você mudar de um plano pago para o plano padrão ou lite, os logs na Coleção de logs serão excluídos em aproximadamente um dia.

A qualquer momento, será possível abrir um chamado de suporte e solicitar que todos os dados sejam excluídos da Procura de log e da Coleção de logs. Para obter informações sobre como abrir um chamado de suporte IBM, veja [Entrando em contato com o suporte](/docs/get-support/howtogetsupport.html#getting-customer-support).



### Informações Adicionais
{: #info}

Para obter mais informações, veja:

[{{site.data.keyword.Bluemix_notm}} conformidade de segurança](/docs/security/compliance.html#compliance)

[PIBR- {{site.data.keyword.IBM_notm}} oficial página](https://www.ibm.com/data-responsibility/gdpr/)



