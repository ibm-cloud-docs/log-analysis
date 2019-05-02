---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging instance, delete

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

# Removendo uma Instância
{: #remove}

É possível remover uma instância do serviço do {{site.data.keyword.la_full_notm}} por meio da IU do {{site.data.keyword.Bluemix}} ou da linha de comandos.
{:shortdesc}

Ao remover uma instância do {{site.data.keyword.cloud_notm}}, limpe concluindo as tarefas a seguir:

1. Anote a lista de origens que encaminham métricas para a instância do {{site.data.keyword.la_full_notm}} que você deseja remover. Deve-se remover o agente LogDNA de cada origem.
2. Remover permissões que são concedidas aos usuários para que trabalhem com a instância. 

    Se você gerenciar o acesso usando grupos de acesso dedicados para trabalhar com uma instância específica, deverá remover esses grupos de acesso.

    Se você gerenciar o acesso a múltiplas instâncias de criação de log usando grupos de acesso, deverá remover as políticas que concedem permissões para a instância que você deseja remover.
    
    Se você conceder políticas individuais para os usuários, deverá reunir a lista de usuários que têm permissões para trabalhar com essa instância. Então, para cada usuário que você identificar, deverá remover as políticas relacionadas à instância que deseja excluir.


Então, exclua a instância por meio do painel do {{site.data.keyword.cloud_notm}}.


## Removendo uma instância por meio da UI do  {{site.data.keyword.cloud_notm}}
{: #remove_ui}

Para remover uma instância do {{site.data.keyword.la_full_notm}} usando a IU do {{site.data.keyword.cloud_notm}}, conclua as etapas a seguir:

1. Efetue login em sua conta do  {{site.data.keyword.cloud_notm}} .

    Clique em [ Painel do {{site.data.keyword.cloud_notm}}![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window} para ativar o painel do {{site.data.keyword.cloud_notm}}.

	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.cloud_notm}} é aberta.

2. Acesse o ícone de menu ![ícone de menu](../../icons/icon_hamburger.svg) &gt; **Observabilidade** para acessar o painel *Observabilidade*.

3. Selecione  ** Criação de log **. A lista de instâncias de criação de log é exibida.

4. Selecione a instância que você deseja excluir.

5. A partir do menu  * Ação * , selecione  ** Remover **.


## Removendo uma instância por meio da CLI
{: #remove_cli}

Para remover uma instância do {{site.data.keyword.la_full_notm}} por meio da linha de comandos, conclua as etapas a seguir:

1. [ Pré-requisito ] Instalado da CLI do  {{site.data.keyword.cloud_notm}} .

   Para obter mais informações, consulte [Instalando a CLI do {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).

   Se a CLI estiver instalada, continue com a próxima etapa.

2. Efetue login na região no {{site.data.keyword.cloud_notm}} na qual você deseja provisionar a instância. Execute o comando a seguir: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Configure o grupo de recursos no qual a instância é fornecida. Execute o comando a seguir:  [ ` ibmcloud target ` ](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target)

    Por padrão, o grupo de recursos *default* é configurado.

4. Remova a instância. Execute o comando  [ ` ibmcloud resource service-instance-delete ` ](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_instance_delete) :

    ```
    ibmcloud resource service-instance-delete NAME 
    ```
    {: codeblock}

    Em que NAME é o nome da instância.

    Por exemplo, para remover uma instância, execute o comando a seguir:

    ```
    ibmcloud resource service-instance-delete logdna-instance-01
    ```
    {: codeblock}



