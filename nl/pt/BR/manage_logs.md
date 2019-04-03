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


# Gerenciando logs
{: #manage_logs}

É possível usar a CLI do {{site.data.keyword.loganalysisshort}} e a API do {{site.data.keyword.loganalysisshort}} para gerenciar os logs que são armazenados na Coleção de logs.
{:shortdesc}

Para gerenciar logs, considere as informações a seguir:

1. O ID do usuário deve ter uma política designada no {{site.data.keyword.cloud_notm}} para o {{site.data.keyword.loganalysisshort}} com permissões para gerenciar os logs. 

    Para obter uma lista das funções e tarefas do IAM por função, veja [Funções do IAM](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#iam_roles). 
	
	Para obter mais informações sobre como designar uma política, veja [Designar uma política do IAM a um usuário por meio da IU do {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/security?topic=cloudloganalysis-grant_permissions#grant_permissions_ui_account).
	
2. Esse recurso está disponível somente para os planos de serviço que permitem retenção de log. 

    Para obter mais informações sobre os planos de serviços, veja [Planos de serviços](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

O serviço {{site.data.keyword.loganalysisshort}} oferece duas CLIs que podem ser usadas para gerenciar os logs:

* Um plug-in do {{site.data.keyword.loganalysisshort}} {{site.data.keyword.cloud_notm}}. Para obter mais informações sobre a CLI, veja [CLI do {{site.data.keyword.loganalysisshort}}(plug-in do {{site.data.keyword.cloud_notm}})](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli).
* Um plug-in CF do {{site.data.keyword.loganalysisshort}} (Descontinuado). Para obter mais informações sobre a CLI, veja [Configurando a CLI do Log Analysis (plug-in do CF)](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#logging_cli).


## Configurando uma política de retenção de log
{: #log_retention_policy}

É possível usar a CLI do {{site.data.keyword.loganalysisshort}} para visualizar e configurar uma política de retenção de log. A política especifica o número de dias que os logs são mantidos na Coleção de logs. 

* Por padrão, quando você seleciona um plano pago, os logs são coletados e mantidos na Coleção de logs. 
* Quando você configura um período de retenção, após a expiração do período de retenção, os logs são excluídos automaticamente da Coleção de logs e não podem ser recuperados.
* É possível especificar um período de retenção para uma conta. O período de retenção é configurado automaticamente para todos os espaços nessa conta. 
* É possível especificar um período de retenção para um espaço.
* É possível mudar a qualquer momento a política de retenção.
* É possível desativar a política configurando seu valor como *-1*. 

**Nota:** quando você desativar a política de retenção de log, deverá manter os logs da Coleção de logs. É possível usar o comando da CLI [cf logging delete](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-logging_cli#delete4) para excluir logs antigos.

Para obter mais informações, veja:

* [Visualizando e configurando a política de retenção de log usando o plug-in do {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy).
* [Visualizando e configurando a política de retenção de log usando o plug-in do CF](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy1#configuring_retention_policy).


## Excluindo logs
{: #log_deletion}

Os logs armazenados em Procura de log são excluídos após 3 dias.

Os logs armazenados em Coleção de logs são mantidos até você configurar uma política de retenção ou excluí-los manualmente. 

* É possível configurar uma política de retenção de log para definir o número de dias que você deseja manter os logs na Coleção de logs. Para obter mais informações, veja [Visualizando e configurando a política de retenção de log usando o plug-in do {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-configuring_retention_policy#configuring_retention_policy).

* É possível usar a [API de Coleção de logs](https://console.bluemix.net/apidocs/948-ibm-cloud-log-collection-api?&language=node&env_id=ibm%3Ayp%3Aus-south#introduction){: new_window} ou a [CLI de Coleção de logs](/docs/services/CloudLogAnalysis/reference?topic=cloudloganalysis-log_analysis_cli#log_analysis_cli){: new_window} para excluir logs manualmente da Coleção de logs. 

* É possível usar a CLI. Para obter mais informações sobre a exclusão manual de logs por meio da CLI veja [ibmcloud logging log-delete usando o plug-in do {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-deleting_logs#deleting_logs).
    


## Fazendo download de logs
{: #download_logs2}

É possível procurar logs dos últimos 3 dias no Kibana. Para poder analisar dados de log mais antigos, é possível fazer download de logs em um arquivo local ou canalizar esses logs para outros programas, como um Elastic Stack local. 

Para obter mais informações, veja:

* [Fazendo download de logs usando o plug-in do {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs#downloading_logs).
* [Fazendo download de logs usando o plug-in do CF](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-downloading_logs1#downloading_logs1).



## Obtendo informações sobre seus logs
{: #info_about_logs}

Para obter informações gerais sobre seus logs, use o comando `ibmcloud logging log-show` ou o comando `cf logging status`. Para obter mais informações, veja:

* [Visualizando informações de log usando o plug-in do {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status1#viewing_log_status1)
* [Visualizando informações de log usando o plug-in do CF](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-viewing_log_status#viewing_log_status1).

Por exemplo, para manter o custo sob controle, você pode desejar monitorar o tamanho dos logs de seus apps durante um período de tempo. Por exemplo, talvez você queira saber o tamanho de cada tipo de log durante uma semana para um espaço do {{site.data.keyword.cloud_notm}} para identificar se algum app ou serviço está gerando mais logs do que o esperado. Para verificar o tamanho de seus logs, use o comando `ibmcloud logging log-show` ou o comando `cf logging status`.

É possível visualizar informações sobre os logs que são armazenados em um domínio de espaço, um domínio de organização ou um domínio de contas.



## Instalando a CLI do {{site.data.keyword.loganalysisshort_notm}} (plug-in do {{site.data.keyword.cloud_notm}})
{: #install_cli2}

Para saber como instalar a CLI, veja [Instalando a CLI de criação de log](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#config_log_collection_cli).

Para verificar a versão da CLI, execute o comando `ibmcloud plugin list`.

Para obter ajuda sobre como executar comandos, veja [Obtendo ajuda da linha de comandos para executar comandos](/docs/services/CloudLogAnalysis/how-to/manage-logs?topic=cloudloganalysis-config_log_collection_cli#command_cli_help).


## Terminais de criação de log
{: #endpoints}

A tabela a seguir lista as URLs de criação de log por região:

<table>
    <caption>Terminais por região</caption>
    <tr>
      <th>Region</th>
      <th>URL</th>
    </tr>
	<tr>
      <td>Frankfurt</td>
	  <td>[https://logging.eu-fra.bluemix.net](https://logging.eu-fra.bluemix.net)</td>
    </tr>
	<tr>
      <td>Sydney</td>
	  <td>[https://logging.au-syd.bluemix.net](https://logging.au-syd.bluemix.net)</td>
    </tr>
	<tr>
      <td></td>
	  <td>[https://logging.eu-gb.bluemix.net](https://logging.eu-gb.bluemix.net)</td>
    </tr>
    <tr>
      <td>Sul dos Estados Unidos</td>
      <td>[Https://logging.ng.bluemix.net](https://logging.ng.bluemix.net)</td>
    </tr>
</table>

## Funções que são requeridas por um usuário para gerenciar os logs
{: #roles1}

No {{site.data.keyword.cloud_notm}}, é possível designar uma ou mais funções para os usuários. Essas funções definem quais tarefas estão ativadas para esse usuário para trabalhar com o serviço {{site.data.keyword.loganalysisshort}}. 

As tabelas a seguir listam as funções que um usuário deve ter para gerenciar os logs:

<table>
  <caption>Permissões requeridas por um **proprietário da conta** para gerenciar os logs</caption>
  <tr>
	<th>Função IAM</th>
	<th>Ações</th>
  </tr>
  <tr>
    <td>*Administrador*</td>
    <td>Verificar os status de logs </br>Fazer download de logs </br>Excluir logs </br>Mudar a política de retenção de log </br>Gerenciar sessões </td>
</table>

<table>
  <caption>Permissões requeridas por um **auditor** para gerenciar os logs</caption>
  <tr>
	<th>Função IAM</th>
	<th>Ações</th>
  </tr>
  <tr>
    <td>*Visualizador*</td>
    <td>Obtenha informações sobre os logs hospedados na Coleção de logs. </br>Obtenha informações sobre a política de retenção de log que está configurada. </td>
</table>

<table>
  <caption>Permissões requeridas por um **administrador** para gerenciar os logs</caption>
  <tr>
	<th>Função IAM</th>
	<th>Ações</th>
  </tr>
  <tr>
    <td>*Administrador*</td>
    <td>Verificar os status de logs </br>Fazer download de logs </br>Excluir logs </br>Mudar a política de retenção de log </br>Gerenciar sessões </td>
</table>

<table>
  <caption>Permissões requeridas por um **desenvolvedor** para gerenciar os logs.</caption>
  <tr>
	<th>Função IAM</th>
	<th>Ações</th>
  </tr>
  <tr>
    <td>*Aplicativos *</td>
    <td>Verificar os status de logs </br>Fazer download de logs </br>Excluir logs </br>Mudar a política de retenção de log </br>Gerenciar sessões</td>
</table>

