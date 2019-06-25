---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, logs

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

# Exibindo logs
{: #view_logs}

Depois de fornecer uma instância do serviço {{site.data.keyword.la_full_notm}} no {{site.data.keyword.cloud_notm}} e configurar um agente LogDNA para uma origem de log, é possível visualizar, monitorar e gerenciar dados do log por meio da IU da web do {{site.data.keyword.la_full_notm}}.
{:shortdesc}

Ao ativar a IU da web do {{site.data.keyword.la_full_notm}}, as entradas de log são exibidas com um formato predefinido. Na seção **Preferências do usuário**, é possível modificar como as informações são exibidas em cada linha de log. Também é possível filtrar os logs e modificar as configurações de procura e, em seguida, marcar o resultado como uma *visualização*. É possível anexar e remover um ou mais alertas para uma visualização. É possível definir um formato customizado para a exibição das linhas na visualização. É possível expandir uma linha de log e ver os dados analisados.


Conclua as etapas a seguir para visualizar logs:


## Etapa 1. Conceder políticas do IAM para um usuário visualizar os logs
{: #view_logs_step1}

**Nota:** deve-se ser um administrador do serviço {{site.data.keyword.la_full_notm}}, um administrador da instância do {{site.data.keyword.la_full_notm}} ou ter permissões do IAM da conta para conceder outras políticas de usuários.

A tabela a seguir lista as políticas mínimas que um usuário deve ter para ser capaz de ativar a IU da web do {{site.data.keyword.la_full_notm}} e visualizar os logs:

| Serviço                        | Função                      | Permissão concedida            |
|--------------------------------|---------------------------|-------------------------------|  
| `{{site.data.keyword.la_full_notm}} ` | Função de plataforma: visualizador     | Permite que o usuário visualize a lista de instâncias de serviço no painel Criação de log de Observabilidade. |
| `{{site.data.keyword.la_full_notm}} ` | Função de serviço: Reader      | Permite que o usuário ative a IU da web e visualize logs na IU da web.  |
{: caption="Tabela 1. Políticas do IAM" caption-side="top"} 

Para obter mais informações sobre como configurar essas políticas para um usuário, consulte [Concedendo permissões para um usuário visualizar os logs no LogDNA](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-work_iam#user_logdna).


## Etapa 2. Navegue para a IU da web por meio da IU do {{site.data.keyword.cloud_notm}}
{: #view_logs_step2}

Para ativar a IU do {{site.data.keyword.la_full_notm}} por meio da IU do {{site.data.keyword.cloud_notm}}, conclua as etapas a seguir:

1. Efetue login em sua conta do  {{site.data.keyword.cloud_notm}} .

    Clique em [ Painel do {{site.data.keyword.cloud_notm}}![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window} para ativar o painel do {{site.data.keyword.cloud_notm}}.

	Depois de efetuar login com seu ID do usuário e senha, o *Painel* do {{site.data.keyword.cloud_notm}} se abre.

2. No menu de navegação, selecione  ** Observabilidade **. 

3. Selecione  ** Criação de log **. 

    A lista de instâncias do {{site.data.keyword.la_full_notm}} que estão disponíveis no {{site.data.keyword.cloud_notm}} é exibida.

4. Selecione uma instância. Em seguida, clique em  ** Visualizar LogDNA **.

A IU da web do {{site.data.keyword.la_full_notm}} se abre e exibe os logs encaminhados para essa instância.


## Etapa 3. Customizar a sua visualização padrão
{: #view_logs_step3}

Na seção **PREFERÊNCIAS DO USUÁRIO**, é possível modificar a ordem dos campos de dados que são exibidos por linha.

Conclua as etapas a seguir para modificar o formato de uma linha de log:

1. Selecione o ícone de **Configuração** ![Ícone de Configuração](images/admin.png "Ícone de Administrador").
2. Selecione  ** PREFERÊNCIAS DO USUÁRIO **. Uma nova janela é aberta.
3. Selecione  ** Formato de log **.
4. Modifique a seção *Formato de linha* para corresponder aos seus requisitos. Caixas de arrasto.


## Etapa 4. Procurar em uma linha de log
{: #view_logs_step4}

A qualquer momento, é possível visualizar cada linha de log no contexto.

Conclua as etapas a seguir: 

1. Clique no ícone de **Visualizações** ![Ícone de Configuração](images/views.png "Ícone de Configuração").
2. Selecione  ** Tudo **  ou uma visualização.
3. Identifique uma linha no log que você deseja explorar.
4. Expandir a linha de log. 

    Informações sobre identificadores de linha, tags e rótulos são exibidas.

5. Clique em **Visualizar no contexto** para ver a linha de log no contexto de outras linhas de log desse host, app ou ambos.

6. Clique em **Copiar para a área de transferência** para copiar o campo de mensagem para a área de transferência.

Quando tiver concluído, feche a linha.


## Etapa 5. Filtrar logs
{: #view_logs_step5}

É possível filtrar logs por origem de log, aplicativo e nível de log. 

* Uma origem pode ser um host, um computador, uma máquina virtual ou um app Heroku.
* Um aplicativo representa um arquivo de log, um programa ou um contêiner.
* Exemplos de níveis de log são: INFO, DEBUG e ERROR

Conclua as etapas a seguir para filtrar os logs:

1. Clique no ícone de **Visualizações** ![Ícone de Configuração](images/views.png "Ícone de Configuração").
2. Selecione  ** Tudo **  ou uma visualização.
3. Expanda **Todas as tags** para ver a lista de tags que são identificadas nos logs. Em seguida, escolha os que você deseja.
4. Expanda **Todas as origens** para ver a lista de origens de log que são identificadas nos logs. Em seguida, escolha os que você deseja.
5. Expanda **Todos os apps** para ver a lista de apps que são identificados nos logs. Em seguida, escolha os que você deseja.
6. Expanda **Todos os níveis** para ver a lista de níveis de log que são identificados nos logs. Em seguida, escolha os que você deseja.


**Nota:** em cada seção, é possível múltiplas opções em um grupo. Agrupe tags, origens de log, apps e níveis de log para reutilizar esses agrupamentos quando você filtrar dados do log em outras visualizações customizadas.

Para criar um grupo, selecione múltiplos valores. Em seguida, clique em **Salvar como grupo**. Insira um nome para o grupo e salve-o.


## Etapa 6. Procurar logs
{: #view_logs_step6}

Ao procurar dados do log, a procura aplica quaisquer filtros de log e consultas de tempo configuradas nessa visualização.

É possível fazer procuras simples (procura de sequência de termo único), procura composta (múltiplos termos de procura e operadores), procuras de campo se a linha de log puder ser analisada e outras. Para obter mais informações, consulte [Como pesquisar logs em docs do LogDNA ![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://docs.logdna.com/docs/search){:new_window}.

**Nota:** os operadores AND e OR fazem distinção entre maiúsculas e minúsculas e devem estar em letras maiúsculas.



## Etapa 7. Criar visualizações
{: #view_logs_step7}


Conclua as etapas a seguir para criar uma visualização:

1. Clique no ícone de **Visualizações** ![Ícone de Configuração](images/views.png "Ícone de Configuração").
2. Selecione  ** Tudo **  ou uma visualização.
3. Filtre os dados do log e, em seguida, clique em **Salvar como nova visualização/alerta**.

    A página  * Criar nova visualização *  é aberta.

4. Insira um nome para a visualização no campo *Nome*.

5. Opcionalmente, inclua uma categoria. Insira um nome e, em seguida, clique em **Incluí-lo isso como uma nova categoria de visualização**.

6. Opcionalmente, anexe um alerta. Uma nova seção é exibida para que você configure o alerta.

7. Clique em  ** Salvar visualização **
