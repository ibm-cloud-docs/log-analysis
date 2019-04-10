---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, iam, manage user access

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

 
# Gerenciando o acesso de usuário com o IAM
{: #iam}

O {{site.data.keyword.iamlong}} (IAM) permite que você autentique com segurança os usuários e controle o acesso a todos os recursos em nuvem de forma consistente no {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

**Cada usuário que acessa o serviço {{site.data.keyword.la_full_notm}} em sua conta deve ter uma política de acesso designada com uma função de usuário do IAM definida.** A política determina quais ações o usuário pode executar dentro do contexto do serviço ou instância que você selecionar. As ações permitidas são customizadas e definidas como operações que têm permissão para serem executadas no serviço. As ações são, então, mapeadas para funções de usuário do IAM.

*Políticas* permitem que o acesso seja concedido em níveis diferentes. Algumas das opções incluem o seguinte: 

* Acesso a todos os serviços ativados pelo IAM em sua conta
* Acesso a todas as instâncias do serviço em uma única região em sua conta
* Acesso a uma instância de serviço individual em sua conta
* Acesso a todas as instâncias do serviço dentro do contexto de um grupo de recursos
* Acesso a todas as instâncias do serviço em uma única região dentro do contexto de um grupo de recursos
* Acesso a todos os serviços ativados pelo IAM dentro do contexto de um grupo de recursos

*Funções* definem as ações que um usuário ou ID de serviço pode executar. Há diferentes tipos de funções no {{site.data.keyword.cloud_notm}}:

* As *funções de gerenciamento de plataforma* permitem que os usuários executem tarefas em recursos de serviço no nível de plataforma, por exemplo, designar acesso de usuário para o serviço, criar ou excluir IDs de serviço, criar instâncias, designar políticas do seu serviço a outros usuários e ligar instâncias a aplicativos.
* *Funções de acesso de serviço* permitem que níveis variados de permissão sejam designados aos usuários para que eles chamem a API do serviço.

**Para organizar um conjunto usuários e IDs serviço em uma única entidade que facilite o gerenciamento das permissões do IAM, use *access groups*.** É possível designar uma política única ao grupo em vez
de designar o mesmo acesso múltiplas vezes por usuário ou ID de serviço individual.
{: tip}


## Gerenciando o acesso designando as políticas diretamente para os usuários
{: #users}

Para gerenciar o acesso ou designar um novo acesso para os usuários usando políticas do IAM, deve-se ser o proprietário da conta, o administrador em todos os serviços na conta ou um administrador para o serviço ou instância de serviço específica. 

Escolha qualquer uma das ações a seguir para gerenciar as políticas do IAM no {{site.data.keyword.cloud_notm}}:

* Para modificar as permissões de um usuário, consulte [Editando o acesso existente](/docs/iam?topic=iam-iammanidaccser#edit_existing).
* Para conceder permissões a um usuário, consulte [Designar novo acesso](/docs/iam?topic=iam-iammanidaccser#assign_new_access).
* Para revogar permissões, consulte  [ Removendo o Acesso ](/docs/iam?topic=iam-iammanidaccser#removing_access).
* Para revisar as permissões de um usuário, consulte [Revisando seu acesso designado](/docs/iam?topic=iam-iammanidaccser#review_your_access).


## Gerenciando acesso usando grupos de acesso
{: #groups}

Para gerenciar o acesso ou designar um novo acesso para usuários usando grupos de acesso, deve-se ser o proprietário da conta, o administrador ou o editor em todos os serviços ativados do Identity and Access na conta ou o administrador ou o editor designado para o serviço de grupos de acesso do IAM. 

Escolha qualquer uma das ações a seguir para gerenciar os grupos de acesso no {{site.data.keyword.cloud_notm}}:

* [ Criando um grupo de acesso ](/docs/iam?topic=iam-groups#create_ag).
* [ Designando acesso a um grupo ](/docs/iam?topic=iam-groups#access_ag).



## {{site.data.keyword.cloud_notm}}  funções da plataforma
{: #platform}

Use a tabela a seguir para identificar a função de plataforma que você pode conceder a um usuário no {{site.data.keyword.cloud_notm}} para executar qualquer uma das ações de plataforma a seguir:

| Ações da plataforma                                                        | Funções do {{site.data.keyword.cloud_notm}} Platform    | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `Conceder acesso aos outros membros da conta para que trabalhem com o serviço`           | Administrador                                        | 
| `Fornecer uma instância de serviço`                                          | Aplicativos                            | 
| `Excluir uma instância de serviço`                                             | Administrador </br>Aplicativos                            | 
| `Criar um ID de serviço`                                                   | Administrador </br>Aplicativos                            |
| `Visualizar detalhes de uma instância de serviço`                                    | Administrador </br>Aplicativos </br>Operador </br>Visualizador  | 
| `Visualizar instâncias de serviço no painel Criação de log de observabilidade`         | Administrador </br>Aplicativos </br>Operador </br>Visualizador  | 
{: caption="Tabela 1. Funções e ações do usuário do IAM" caption-side="top"}



## Funções de serviço do {{site.data.keyword.cloud_notm}}
{: #service}

Use a tabela a seguir para identificar as funções de serviço que você pode conceder a um usuário para executar qualquer uma das ações de serviço a seguir:

| Ações                                                                 | Funções de serviço do {{site.data.keyword.cloud_notm}}     | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `Add LogDNA log sources`                                                | Gerenciador                                              |
| `Manage ingestion keys`                                                 | Gerenciador                                              |
| `Manage service keys`                                                   | Gerenciador                                              |
| `Archive logs`                                                          | Gerenciador                                              |
| `Configure alerts`                                                      | Gerenciador </br>Gravador </br>Reader                      | 
| `Filter and search log data`                                            | Gerenciador </br>Gravador </br>Reader                      |
| `Create views`                                                          | Gerenciador </br>Gravador </br>Reader                      |
| `Export log data`                                                       | Gerenciador </br>Gravador </br>Reader                      |
| `Configure user preferences in the LogDNA web UI`                       | Gerenciador </br>Gravador </br>Reader                      |
| `View logs through the LogDNA web UI`                                   | Gerenciador </br>Gravador </br>Reader                      | 
{: caption="Tabela 3. Funções e ações do usuário do IAM" caption-side="top"}


**Nota:** a função de serviço **gerenciador** é mapeada diretamente para a função de administrador de LogDNA.






