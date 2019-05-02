---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, IAM, security, logging, access groups

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

 
# Gerenciando políticas e grupos de acesso do IAM
{: #work_iam}

É possível usar o {{site.data.keyword.iamlong}} (IAM) para autenticar com segurança os usuários e controlar o acesso a todos os recursos em nuvem de forma consistente no {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

Para obter mais informações, consulte [Gerenciando o acesso do usuário com o IAM](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).


## Concedendo permissões a um usuário para que se torne um administrador do serviço na conta do {{site.data.keyword.cloud_notm}}
{: #admin_account}

Como o **proprietário da conta** ou como um administrador de serviço do **{{site.data.keyword.la_full_notm}} **, deve-se ter permissões para executar as ações a seguir: 

* Conceda acesso a outros membros de conta para trabalharem com o serviço
* Provisão de uma instância de serviço
* Excluir uma instância de serviço
* Visualizar detalhes de uma instância de serviço
* Criar um ID de serviço

Portanto, para conceder a um usuário a função de administrador para que ele gerencie o serviço na conta, o usuário deve ter uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de plataforma **Administrador**. Deve-se designar esse acesso de usuário a um recurso individual na conta. 

Conclua as etapas a seguir para designar a um usuário a função de administrador para o serviço {{site.data.keyword.la_full_notm}} na conta: 

1. Na barra de menus, clique em **Gerenciar** &gt; **Acesso (IAM)** e, em seguida, selecione **Usuários**.
2. Na linha para o usuário que você deseja designar acesso, selecione o menu **Ações** e, em seguida, clique em **Designar acesso**.
3. Selecione **Designar acesso a recursos**.
4. Selecione  ** IBM Log Analysis com LogDNA **.
5. Selecione  ** Todas as regiões atuais **.
6. Selecione  ** Todas as instâncias de serviço atuais **.
7. Selecione a função de plataforma  ** Administrador **.
8. Clique em Atribuir.


## Concedendo permissões a um usuário para se tornar um administrador do serviço dentro de um grupo de recursos
{: #admin_rg}

Como um **administrador de serviço do {{site.data.keyword.la_full_notm}} **, deve-se ter permissões para executar as ações a seguir: 

* Conceda acesso a outros membros de conta para trabalharem com o serviço
* Provisão de uma instância de serviço
* Excluir uma instância de serviço
* Visualizar detalhes de uma instância de serviço
* Criar um ID de serviço

Portanto, para conceder a um usuário a função de administrador para que ele gerencie as instâncias dentro de um grupo de recursos na conta, o usuário deve ter uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de plataforma **Administrador** dentro do contexto do grupo de recursos. 

Conclua as etapas a seguir para designar a um usuário a função de administrador para o serviço {{site.data.keyword.la_full_notm}} dentro do contexto de um grupo de recursos: 

1. Na barra de menus, clique em **Gerenciar** &gt; **Acesso (IAM)** e, em seguida, selecione **Usuários**.
2. Na linha para o usuário que você deseja designar acesso, selecione o menu **Ações** e, em seguida, clique em **Designar acesso**.
3. Selecione **Designar acesso em um grupo de recursos**.
4. Selecione um grupo de recursos.
5. Se o usuário não tiver uma função que já tenha sido concedida para o grupo de recursos selecionado, escolha uma função para o campo **Designar acesso a um grupo de recursos**. 

    Dependendo da função que você selecionar, o usuário poderá visualizar o grupo de recursos em seu painel, editar o nome do grupo de recursos ou gerenciar o acesso de usuário ao grupo. 
    
    Será possível selecionar **Sem acesso**, se você desejar que o usuário tenha acesso somente ao serviço do {{site.data.keyword.la_full_notm}} no grupo de recursos.

6. Selecione  ** IBM Log Analysis com LogDNA **.
7. Selecione a função de plataforma  ** Administrador **.
8. Clique em **Designar**.


## Concedendo permissões a um usuário do DevOps para gerenciar o serviço na conta do {{site.data.keyword.cloud_notm}}
{: #devops_account}

Como um **usuário do DevOps**, deve-se ter permissões para executar as ações a seguir: 

* Provisão de uma instância de serviço
* Excluir uma instância de serviço
* Visualizar detalhes de uma instância de serviço
* Criar um ID de serviço

Portanto, é necessário ter uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de plataforma **Editor**.

Conclua as etapas a seguir para designar a um usuário a função de editor para o serviço {{site.data.keyword.la_full_notm}} na conta: 

1. Na barra de menus, clique em **Gerenciar** &gt; **Acesso (IAM)** e, em seguida, selecione **Usuários**.
2. Na linha para o usuário que você deseja designar acesso, selecione o menu **Ações** e, em seguida, clique em **Designar acesso**.
3. Selecione **Designar acesso a recursos**.
4. Selecione  ** IBM Log Analysis com LogDNA **.
5. Selecione  ** Todas as instâncias de serviço **.
6. Selecione a função de plataforma  ** Editor **.
7. Clique em Atribuir.

## Concedendo permissões a um usuário do DevOps para gerenciar uma instância na conta do {{site.data.keyword.cloud_notm}}
{: #devops_account_instance}

Conclua as etapas a seguir para designar a um usuário a função de editor em uma instância do serviço {{site.data.keyword.la_full_notm}} na conta: 

1. Na barra de menus, clique em **Gerenciar** &gt; **Acesso (IAM)** e, em seguida, selecione **Usuários**.
2. Na linha para o usuário que você deseja designar acesso, selecione o menu **Ações** e, em seguida, clique em **Designar acesso**.
3. Selecione **Designar acesso a recursos**.
4. Selecione  ** IBM Log Analysis com LogDNA **.
5. Selecione a instância.
6. Selecione a função de plataforma  ** Editor **.
7. Clique em Atribuir.



## Concedendo permissões a um usuário do DevOps para gerenciar o serviço dentro de um grupo de recursos
{: #devops_rg}

Como um **usuário do DevOps**, deve-se ter permissões para executar as ações a seguir: 

* Provisão de uma instância de serviço
* Excluir uma instância de serviço
* Visualizar detalhes de uma instância de serviço
* Criar um ID de serviço

Portanto, é necessária uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de plataforma **Editor**.

Conclua as etapas a seguir para designar a um usuário a função de editor para o serviço {{site.data.keyword.la_full_notm}} dentro do contexto de um grupo de recursos: 

1. Na barra de menus, clique em **Gerenciar** &gt; **Acesso (IAM)** e, em seguida, selecione **Usuários**.
2. Na linha para o usuário que você deseja designar acesso, selecione o menu **Ações** e, em seguida, clique em **Designar acesso**.
3. Selecione **Designar acesso em um grupo de recursos**.
4. Selecione um grupo de recursos.
5. Se o usuário não tiver uma função que já tenha sido concedida para o grupo de recursos selecionado, escolha uma função para o campo **Designar acesso a um grupo de recursos**. 

    Dependendo da função que você selecionar, o usuário poderá visualizar o grupo de recursos em seu painel, editar o nome do grupo de recursos ou gerenciar o acesso de usuário ao grupo. 
    
    Será possível selecionar **Sem acesso**, se você desejar que o usuário tenha acesso somente ao serviço do {{site.data.keyword.la_full_notm}} no grupo de recursos.

6. Selecione  ** IBM Log Analysis com LogDNA **.
7. Selecione a função de plataforma  ** Editor **.
8. Clique em **Designar**.

## Concedendo permissões para gerenciar logs e configurar alertas no LogDNA
{: #admin_user_logdna}

Como um **usuário administrador** no LogDNA, deve-se ter as permissões para executar as ações a seguir: 

* Incluir origens de log do LogDNA
* Visualizar logs
* Procurar logs
* Filtrar logs
* Configurar alertas

Portanto, são necessárias as políticas a seguir:

* Uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de plataforma **Editor**. Essa política concede permissões para visualizar os detalhes da instância de serviço por meio da linha de comandos e no painel do {{site.data.keyword.cloud_notm}}.
* Uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de serviço **Gerenciador**. Essa política concede permissões para monitorar, filtrar e procurar o log e definir alertas por meio da IU da web do LogDNA.

**Nota:** como um administrador do serviço, quando você concede a um usuário essas políticas, considere fazer isso dentro do contexto de um grupo de recursos. Uma instância do {{site.data.keyword.la_full_notm}} é provisionada dentro do contexto de um grupo de recursos. Portanto, conceda permissões de acesso dentro do contexto do grupo de recursos.


Conclua as etapas a seguir para designar a um usuário ambas as políticas para o serviço do {{site.data.keyword.la_full_notm}} dentro do contexto de um grupo de recursos: 

1. Na barra de menus, clique em **Gerenciar** &gt; **Acesso (IAM)** e, em seguida, selecione **Usuários**.
2. Na linha para o usuário que você deseja designar acesso, selecione o menu **Ações** e, em seguida, clique em **Designar acesso**.
3. Selecione **Designar acesso em um grupo de recursos**.
4. Selecione um grupo de recursos.
5. Se o usuário não tiver uma função já concedida para o grupo de recursos selecionado, escolha uma função para o campo **Designar acesso a um grupo de recursos**. 

    Dependendo da função que você selecionar, o usuário poderá visualizar o grupo de recursos em seu painel, editar o nome do grupo de recursos ou gerenciar o acesso de usuário ao grupo. 
    
    Será possível selecionar **Sem acesso**, se você desejar que o usuário tenha acesso somente ao serviço do {{site.data.keyword.la_full_notm}} no grupo de recursos.

6. Selecione  ** IBM Log Analysis com LogDNA **.
7. Selecione a função de plataforma  ** Editor **.
8. Selecione a função de serviço  ** Gerenciador **.
8. Clique em **Designar**.

## Concedendo permissões a um usuário para visualizar logs no LogDNA
{: #user_logdna}

Como um **usuário**, **auditor** ou **desenvolvedor**, você pode precisar de permissões para executar as ações a seguir: 

* Visualizar logs
* Procurar logs
* Filtrar logs

Portanto, são necessárias as políticas a seguir:

* Uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de plataforma **Visualizador**. Essa política concede permissões para visualizar os detalhes da instância de serviço por meio da linha de comandos e no painel do {{site.data.keyword.cloud_notm}}.
* Uma política do IAM para o serviço {{site.data.keyword.la_full_notm}} com a função de serviço **Leitor**. Essa política concede permissões para visualizar, filtrar e procurar logs por meio da IU da web do LogDNA.

**Nota:** como um administrador do serviço, quando você concede a um usuário essas políticas, considere fazer isso dentro do contexto de um grupo de recursos. Uma instância do {{site.data.keyword.la_full_notm}} é provisionada dentro do contexto de um grupo de recursos. Portanto, conceda permissões de acesso para usuários dentro do contexto do grupo de recursos.

Conclua as etapas a seguir para designar a um usuário ambas as políticas para o serviço do {{site.data.keyword.la_full_notm}} dentro do contexto de um grupo de recursos: 

1. Na barra de menus, clique em **Gerenciar** &gt; **Acesso (IAM)** e, em seguida, selecione **Usuários**.
2. Na linha para o usuário que você deseja designar acesso, selecione o menu **Ações** e, em seguida, clique em **Designar acesso**.
3. Selecione **Designar acesso em um grupo de recursos**.
4. Selecione um grupo de recursos.
5. Se o usuário não tiver uma função já concedida para o grupo de recursos selecionado, escolha uma função para o campo **Designar acesso a um grupo de recursos**. 

    Dependendo da função que você selecionar, o usuário poderá visualizar o grupo de recursos em seu painel, editar o nome do grupo de recursos ou gerenciar o acesso de usuário ao grupo. 
    
    Será possível selecionar **Sem acesso**, se você desejar que o usuário tenha acesso somente ao serviço do {{site.data.keyword.la_full_notm}} no grupo de recursos.

6. Selecione  ** IBM Log Analysis com LogDNA **.
7. Selecione a função de plataforma  ** Visualizador **.
8. Selecione a função de serviço  ** Reader **.
8. Clique em **Designar**.

