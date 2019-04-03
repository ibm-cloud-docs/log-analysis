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

# Analisando logs no Kibana por meio de um painel
{:#analize_logs_dashboard}

Use a página *Painel* no Kibana para exibir coleções de visualizações que são agrupadas em painéis. Use os painéis para analisar seus dados do log e comparar resultados.
{:shortdesc}

No {{site.data.keyword.Bluemix}}, há diferentes tipos de painéis que podem ser definidos e customizados para visualizar e analisar os dados. Por exemplo, a tabela a seguir lista alguns tipos comuns de painéis:

| Tipo de painel | Descrição |
|-------------------|-------------|
| Painel Single-cf-app | Esse é um painel que mostra informações para um único aplicativo Cloud Foundry. |
| Painel de contêiner único  | Esse é um painel que mostra informações para um único contêiner.  |
| Painel de grupo de contêiner  | Esse é um painel que mostra informações para um grupo de contêiner específico.  |
| Painel Multi-cf-app | Esse é um painel que mostra informações para todos os aplicativos Cloud Foundry que são implementados no mesmo espaço.  | 
| Painel de múltiplos contêineres | Esse é um painel que mostra informações para todos os contêineres que são implementados no mesmo espaço.  |
| Painel de espaço | Esse é um painel que mostra os dados de criação de log que estão disponíveis em um espaço.  | 
{: caption="Tabela 1. Amostras de tipos de painel" caption-side="top"}

Para visualizar os dados em um painel, configure telas. O Kibana inclui diferentes visualizações, como tabela, tendências e histograma, que podem ser usadas para analisar as informações. Uma visualização é incluída como uma tela para um painel. É possível incluir, remover e reorganizar os painéis no painel. O objetivo de cada painel varia. Alguns painéis são organizados em linhas que fornecem os resultados de uma ou mais consultas. Outros painéis exibem documentos ou informações customizadas. Cada tela é baseada em uma procura. A procura define o subconjunto de dados que a tela exibe. Por exemplo, é possível configurar um gráfico de barras, gráfico de pizza ou tabela para visualizar os dados e analisá-los.  

A tabela a seguir lista as diferentes tarefas que podem ser executadas na página Painel:

| Tarefa | Informações Adicionais |
|------|------------------|
| [Incluir uma visualização](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#add_visualization) | É possível incluir uma visualização ou procura existente em um painel.|
| [Criar um novo painel](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#new) | É possível criar múltiplos painéis. Cada painel pode ser projetado para incluir diversas procuras e visualizações e um subconjunto diferente de dados do log.  |
| [Excluir um painel](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#delete) | Exclua painéis que não forem necessários. |
| [Exportar um painel](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#export) | É possível exportar um painel como um arquivo JSON. |
| [Importar um painel](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#import) | É possível importar um painel como um arquivo JSON. |
| [Carregar um painel](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#reload3) | É possível fazer upload de um painel para atualizar, modificar ou analisar seus dados. |
| [Salvar um painel](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save) | É possível salvar um painel para reutilização posterior. |
{: caption="Tabela 2. Tarefas para trabalhar com painéis" caption-side="top"}

Para obter mais informações sobre Kibana, veja o [Guia do Usuário do Kibana ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Incluindo uma nova procura ou visualização
{: #add_visualization}

Conclua as etapas a seguir para incluir uma visualização ou procura existente:

1. Na barra de ferramentas da página Painel, clique em **Incluir**. 

    **Nota**: é possível incluir visualizações e procuras. 

2. Selecione a guia **Visualizações** para incluir uma visualização ou selecione a guia **Procura** para incluir uma procura.

3. Clique na procura ou na visualização que deseja incluir.

    Uma tela para essa procura ou visualização é incluída no painel.

	
## Criando um novo painel do Kibana
{: #new}

Conclua as etapas a seguir para criar um novo painel:

1. Na barra de ferramentas da página Painel, clique em **Incluir**. 

2. Inclua uma ou mais procuras e visualizações. Para obter mais informações, consulte [Incluindo uma nova procura ou visualização](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#add_visualization).

    Ao incluir uma procura ou visualização, uma tela é incluída no painel.

3. Arraste a tela e solte-a na parte do painel em que deseja posicioná-la.
 
4. Salve o painel para reutilização futura. Para obter mais informações, veja [Salvando um painel do Kibana](/docs/services/CloudLogAnalysis/kibana/analize_logs_dashboard.html#save).


## Excluindo um painel do Kibana
{: #delete1}

Para excluir um painel, conclua as etapas a seguir na página **Gerenciamento**:

1. Na página **Gerenciamento**, selecione **Objetos salvos**.

2. Na guia **Painéis**, selecione o painel que você deseja excluir.

3. Clique em **Excluir**.

## Exportando um painel do Kibana
{: #export}

Para exportar um painel como um arquivo JSON, conclua as etapas a seguir na página **Gerenciamento**:

1. Na página **Gerenciamento**, selecione **Objetos salvos**.

2. Na guia **Painel**, selecione o painel que deseja exportar.

3. Clique em **Exportar**.

4. Salve o arquivo.

## Importando um painel do Kibana
{: #import}

Para importar um painel como um arquivo JSON, conclua as etapas a seguir na página **Gerenciamento**:

1. Na página **Gerenciamento**, selecione **Objetos salvos**.

2. Na guia **Painel**, selecione **Importar**.

3. Selecione um arquivo e clique em **Abrir**.

O painel é incluído na lista de painéis.

## Carregando um painel do Kibana
{: #reload3}

Conclua as etapas a seguir para carregar um painel salvo:

1. Na barra de ferramentas da página Painel, clique em **Abrir**.

2. Selecione um painel na lista de painéis disponíveis que é mostrada no campo *Nome*.

Também é possível procurar um painel na barra de Procura.

## Salvando um painel do Kibana
{: #save}

Conclua as etapas a seguir para salvar um painel do Kibana após sua customização:

1. Na barra de ferramentas, clique em **Salvar**.

2. Insira um nome para o painel.

    **Nota:** o nome não deve conter espaços.

3. Clique em **Salvar**.




