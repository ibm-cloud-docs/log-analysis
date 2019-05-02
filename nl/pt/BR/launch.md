---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, web UI, browser

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

# Navegando para a UI da web
{: #launch}

Depois de fornecer uma instância do serviço {{site.data.keyword.la_full_notm}} no {{site.data.keyword.cloud_notm}} e configurar um agente LogDNA para uma origem de dados de log, é possível visualizar, monitorar e gerenciar logs por meio da IU da web do {{site.data.keyword.la_full_notm}}.
{:shortdesc}


## Concedendo políticas do IAM a um usuário para visualizar dados 
{: #step1}

**Nota:** deve-se ser um administrador do serviço do {{site.data.keyword.la_full_notm}}, um administrador de uma instância do {{site.data.keyword.la_full_notm}} ou ter permissões de IAM da conta para conceder outras políticas de usuários.

A tabela a seguir lista as políticas mínimas que um usuário deve ter para ser capaz de ativar a IU da web e visualizar os dados:

| Serviço                              | Função                      | Permissão concedida       |
|--------------------------------------|---------------------------|---------------------|
| `{{site.data.keyword.la_full_notm}}` | Função de plataforma: visualizador     | Permite que o usuário visualize a lista de instâncias de serviço no painel Criação de log de Observabilidade. |
| `{{site.data.keyword.la_full_notm}}` | Função de serviço: gravador      | Permite que o usuário ative a IU da web e visualize logs na IU da web.    |
{: caption="Tabela 1. Políticas do IAM" caption-side="top"} 

Para obter mais informações sobre como configurar essas políticas para um usuário, consulte [Concedendo permissões a um usuário para visualizar logs](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Ativando a IU da web por meio da IU do {{site.data.keyword.cloud_notm}}
{: #launch_step2}

Você ativa a IU da web dentro do contexto de uma instância do {{site.data.keyword.la_full_notm}} por meio da IU do {{site.data.keyword.cloud_notm}}. 

Conclua as etapas a seguir para ativar a IU da web:

1. Efetue login em sua conta do  {{site.data.keyword.cloud_notm}} .

    Clique em [ Painel do {{site.data.keyword.cloud_notm}}![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window} para ativar o painel do {{site.data.keyword.cloud_notm}}.

	Após você efetuar login com o seu ID do usuário e senha, o Painel do {{site.data.keyword.cloud_notm}} será aberto.

2. No menu de navegação, selecione  ** Observabilidade **. 

3. Selecione  ** Criação de log **. 

    A lista de instâncias que estão disponíveis no {{site.data.keyword.cloud_notm}} é exibida.

4. Selecione uma instância. Em seguida, clique em  ** Visualizar LogDNA **.

A UI da Web é aberta.


## Obtendo a URL da IU da web por meio do {{site.data.keyword.cloud_notm}}
{: #launch_get}

Para obter a URL da IU da web, conclua as etapas a seguir por meio de um terminal:

1. Configure o grupo de recursos no qual a instância do {{site.data.keyword.la_full_notm}} é fornecida.

    ```
    export logdna_rg_name=<Resource_Group_Name_Where_LogDNA_Instance_Is_Created>
    ```
    {: codeblock}

2. Configure o nome da instância do  {{site.data.keyword.la_full_notm}} .

    ```
    export logdna_instance_name=<Your_LogDNA_Instance_Name>
    ```
    {: codeblock}

3. Configure o terminal.

    ```
    export rc_endpoint=resource-controller.cloud.ibm.com
    ```
    {: codeblock}

4. Configure o token do IAM.

    ```
    export iam_token=$(ibmcloud iam oauth-tokens | grep IAM | grep -oP  "eyJ.*")
    ```
    {: codeblock}

    **Nota:** se você estiver trabalhando em um terminal MacOS, o comando será como a seguir: `export iam_token=$(ic iam oauth-tokens | grep IAM | grep -o  "eyJ.*")`

5. Configure o ID do grupo de recursos.

    ```
    export resource_group_id=$(ibmcloud resource groups | grep "^$logdna_rg_name" | awk '{print $2}')
    ```
    {: codeblock}

6. Configure a URL da IU da web em uma variável.

    ```
    export dashboard_url=$(curl -H "Accept: application/json" -H "Authorization: Bearer $iam_token" "https://$rc_endpoint/v1/resource_instances?resource_group_id=$resource_group_id&type=service_instance" | jq ".resources[] | select(.name==\"$logdna_instance_name\") | .dashboard_url")
    ```
    {: codeblock}

7. Obtenha a URL da IU da web.

    ```
    echo $dashboard_url
    ```
    {: codeblock}

    

