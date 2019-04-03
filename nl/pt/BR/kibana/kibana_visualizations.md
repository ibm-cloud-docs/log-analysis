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

# Analisando logs no Kibana usando visualizações 
{:#kibana_visualizations}

Use a página *Visualizar* no Kibana para criar visualizações, como gráficos e tabelas, que podem ser usadas para analisar seus dados do log e comparar resultados. 
{:shortdesc}

É possível usar uma visualização individualmente para analisar seus logs. 

* É possível criar visualizações em uma procura que você define e salvar na página *Descobrir* ou em uma nova consulta que você define na página *Visualizar*. A procura define o subconjunto de dados que uma visualização exibe.

* O tipo de visualização que for escolhido determina como os dados são exibidos para análise.

A tabela a seguir lista os diferentes tipos de visualizações:

| Tipo de visualização | Descrição |
|-----------------------|-------------|
| gráfico de Áreas | Exibe dados quantitativos graficamente. Use para comparar dois ou mais conjuntos de dados agregados. |
| Tabela de Dados | Exibe dados brutos em formato tabular para uma agregação composta. |
| Gráfico de Linhas | Exibe dados baseados em tempo. Use para comparar dois ou mais conjuntos de dados agregados baseados em tempo. |
| Widget de redução de preço | Use para exibir informações de texto. |
| Métrica | Use para mostrar uma contagem de ocorrências ou a média exata de um campo numérico. |
| Gráfico de pizza | Use para exibir diferentes valores de um campo. | 
| Gráfico de barras verticais | Exibe dados que são baseados em tempo e dados que não são baseados em tempo. Use para agrupar dados. |
{: caption="Tabela 1. Tipos de visualização" caption-side="top"}

Na página Visualizar, é possível executar qualquer uma das tarefas a seguir:

| Tarefa | Informações Adicionais |
|------|------------------|
| [Criar uma nova visualização](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#create) | É possível criar visualizações em uma procura que você define e salvar na página *Descobrir* ou em uma nova consulta que você define na página *Visualizar*. |
| [Excluir uma visualização](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#delete) | Exclua visualizações que não forem necessárias. |
| [Exportar uma visualização](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#export) | É possível exportar uma visualização como um arquivo JSON.  |
| [Importar uma visualização](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#import1) | É possível importar uma visualização como um arquivo JSON.  |
| [Carregar uma visualização](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#reload2) | É possível fazer upload de uma visualização para atualizar, modificar ou analisar seus dados. |
| [Salvar uma visualização](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-kibana_visualizations#save2) | É possível salvar visualizações para reutilização posterior. |
{: caption="Tabela 2. Tarefas para trabalhar com visualizações" caption-side="top"}


## Criando visualizações por meio das consultas no Kibana
{: #create}

Conclua as etapas a seguir para criar uma visualização na página Visualizar:

1. Ative o Kibana e, em seguida, selecione a página **Visualizar**.

2. Escolha um tipo de visualização, por exemplo, *tabela*.

3. Selecione uma visualização salva anteriormente do **Ou em uma procura salva** ou selecione um índice na seção **Em uma nova procura, selecione índice**.

4. Configure a consulta.

    * Se você selecionar **Ou em uma procura salva**, selecione uma consulta de procura. A consulta é usada para recuperar os dados que são usados para a visualização. 
	
	    Depois de selecionar uma procura, o construtor de visualização se abre e carrega os dados para a consulta selecionada. 
		
		**Nota**: quaisquer mudanças feitas em uma procura salva são refletidas automaticamente na visualização. Para desativar atualizações automáticas que você faz na consulta que é vinculada a essa visualização, dê um clique duplo na mensagem: *Esta visualização é vinculada a uma procura salva: your_search_name*. 

    * Se você selecionar **Em uma nova procura, selecione índice**, defina uma nova consulta. A consulta é usada para definir o subconjunto de dados que é recuperado e usado pela visualização.

        Para obter mais informações, consulte
[Filtrando logs definindo consultas customizadas](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-define_search#define_search).

Para obter mais informações sobre Kibana, veja o [Guia do Usuário do Kibana ![Ícone de link externo](../../../icons/launch-glyph.svg "Ícone de link externo")](https://www.elastic.co/guide/en/kibana/5.1/index.html){: new_window}.


## Excluindo uma visualização
{: #delete}

Para excluir uma visualização, conclua as etapas a seguir na página **Gerenciamento**:

1. Na página **Gerenciamento**, selecione **Objetos salvos**.

2. Na guia **Visualizações**, selecione as visualizações que deseja excluir.

3. Clique em **Excluir**.


## Exportando uma visualização
{: #export1}

Para exportar uma visualização como um arquivo JSON, conclua as etapas a seguir na página **Gerenciamento**:

1. Na página **Gerenciamento**, selecione **Objetos salvos**.

2. Na guia **Visualizações**, selecione a visualização que deseja exportar.

3. Clique em **Exportar**.

4. Salve o arquivo.

## Importando uma visualização
{: #import1}

Para importar uma visualização como um arquivo JSON, conclua as etapas a seguir na página **Gerenciamento**:

1. Na página **Gerenciamento**, selecione **Objetos salvos**.

2. Na guia **Visualizações**, selecione **Importar**.

3. Selecione um arquivo e clique em **Abrir**.

A visualização é incluída na lista de visualizações.


 
## Carregando uma visualização
{: #reload2}

Conclua as etapas a seguir para carregar uma visualização salva:

1. Na barra de ferramentas da página Visualizar, clique em **Abrir**.

2. Selecione a visualização que deseja carregar. 


## Salvando uma visualização
{: #save2}

Conclua as etapas a seguir para salvar uma visualização na página Visualizar:

1. Na barra de ferramentas da página Visualizar, clique em **Salvar**.

2. Insira um nome para a visualização.

3. Clique em salvar. 


