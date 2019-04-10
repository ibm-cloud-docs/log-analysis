---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, getting started

subcollection: LogDNA

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

# Tutorial de introdução
{: #getting-started}

Use o {{site.data.keyword.la_full}} para incluir recursos de gerenciamento de log na arquitetura do {{site.data.keyword.cloud_notm}}. O {{site.data.keyword.la_full_notm}} é operado por LogDNA em parceria com o {{site.data.keyword.IBM_notm}}.
{:shortdesc}


## Etapa 1. Antes de Iniciar
{: #getting-started_prereqs}

* Leia sobre o {{site.data.keyword.la_full_notm}}. Para obter mais informações, consulte [Sobre o {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).
* Verifique as regiões em que o serviço está disponível. Para obter mais informações, consulte [Regiões](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_regions).
* Obtenha um ID do usuário que seja um membro ou um proprietário de uma conta do {{site.data.keyword.cloud_notm}}. 

    Para obter um ID do usuário do {{site.data.keyword.cloud_notm}}, clique em [Registro ![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window}.



## Etapa 2. Get iniciado
{: #getting-started_step2}

Escolha um recurso de nuvem para o qual você deseja gerenciar os logs. Em seguida, configure essa origem de log para que seja possível monitorar seus logs por meio do serviço {{site.data.keyword.la_full_notm}}. A origem de log pode ser localizada na mesma região em que você fornece uma instância do {{site.data.keyword.la_full_notm}} ou em uma região diferente.

A tabela a seguir lista exemplos de recursos em nuvem que podem ser configurados para armazenar e gerenciar logs usando o serviço {{site.data.keyword.la_full_notm}}. Conclua o tutorial para que um recurso seja iniciado com o serviço {{site.data.keyword.loganalysisshort}}:

<table>
  <caption>Tutoriais para começar a trabalhar com o serviço do {{site.data.keyword.la_full_notm}} </caption>
  <tr>
    <th>Recurso</th>
    <th>Tutorial</th>
    <th>Ambiente</th>
    <th>Cenário</th>
  </tr>
  <tr>
    <td>Contêineres em execução no  {{site.data.keyword.containershort}}</td>
    <td>[ Gerenciando logs de cluster do Kubernetes com o  {{site.data.keyword.la_full_notm}} ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-kube#kube)</td>
    <td>{{site.data.keyword.cloud_notm}} Public </td>
    <td>![{{site.data.keyword.containershort}} e o {{site.data.keyword.la_full_notm}}](images/kube.png "{{site.data.keyword.containershort}} e o {{site.data.keyword.la_full_notm}}")</td>
  </tr>
  <tr>
    <td>Linux Ubuntu, Linux Debian</td>
    <td>[ Gerenciando logs do Linux Ubuntu com o  {{site.data.keyword.la_full_notm}} ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-ubuntu#ubuntu)</td>
    <td>Em premissas</td>
    <td>![Servidor Ubuntu e o {{site.data.keyword.la_full_notm}}](images/ubuntu.png "Servidor Ubuntu e o {{site.data.keyword.la_full_notm}}")</td>
  </tr>
</table>



## Etapa 3. Fazer upgrade do plano
{: #getting-started_step3}

Ativar mais recursos de criação de log.

Faça upgrade do plano de serviço do {{site.data.keyword.la_full_notm}} para um plano pago para poder [filtrar logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step5), [procurar logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step6), [definir visualizações](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7) e [configurar alertas](https://docs.logdna.com/docs/alerts). Para obter mais informações sobre os planos de serviço do {{site.data.keyword.la_full_notm}}, consulte [Planos de precificação](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#overview_pricing_plans).

## Etapa 4. Etapas seguintes 
{: #getting-started_iam}

Em seguida, gerencie o acesso de usuário com o IAM.

Identifique as políticas do IAM que um usuário precisa para trabalhar com o serviço {{site.data.keyword.la_full_notm}}.

Para saber mais sobre a integração do IAM com o serviço {{site.data.keyword.la_full_notm}}, consulte [Gerenciando o acesso de usuário com o IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).

Por exemplo, escolha uma função de usuário para saber como conceder permissões a esse usuário para trabalhar com o serviço {{site.data.keyword.la_full_notm}}. 

| Função de usuário no {{site.data.keyword.cloud_notm}} | Para obter mais informações                     |
|-----------------------------------------------------|------------------------------------------|
| Proprietário da conta                                       | [Concedendo permissões a um usuário para que se torne um administrador do serviço na conta do {{site.data.keyword.cloud_notm}} ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Administrador do serviço de plataforma na conta       | [Concedendo permissões a um usuário para que se torne um administrador do serviço na conta do {{site.data.keyword.cloud_notm}} ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_account) |
| Administrador do serviço de plataforma em um grupo de recursos  | [Concedendo permissões a um usuário para se tornar um administrador do serviço dentro de um grupo de recursos](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_rg) |
| Operador do Platform DevOps na conta           | [Concedendo permissões a um usuário do DevOps para gerenciar o serviço na conta do {{site.data.keyword.cloud_notm}} ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_account) |
| Operador da plataforma DevOps em um grupo de recursos        | [Concedendo permissões a um usuário do DevOps para gerenciar o serviço dentro de um grupo de recursos](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#devops_rg) |
| Administrador de serviço no LogDNA                     | [Concedendo permissões para gerenciar logs e configurar alertas no LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#admin_user_logdna)              |
| Usuário / Desenvolvedor                                    | [Concedendo permissões a um usuário para visualizar e gerenciar logs no LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna)               |
{: caption="Tabela 2. Funções de nuvem no  {{site.data.keyword.cloud_notm}}" caption-side="top"}


