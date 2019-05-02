---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, kubernetes, tutorial, reset ingestion key

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


# Reconfigurando a chave de ingestão usada por um cluster Kubernetes para encaminhar logs para uma instância do {{site.data.keyword.la_full_notm}}
{: #kube_reset}

Se a chave de ingestão que você usa para encaminhar logs de um cluster para uma instância do {{site.data.keyword.la_full_notm}} no {{site.data.keyword.cloud_notm}} estiver comprometida, você deverá reconfigurar a chave e atualizar a configuração do cluster Kubernetes para usar a nova chave de ingestão. 
{:shortdesc}

## Antes de iniciar
{: #kube_reset_prereqs}

Trabalhe na região Sul dos EUA. Os dois recursos, a instância do {{site.data.keyword.la_full_notm}} e o cluster do Kubernetes, devem ser executados na mesma conta.

A instância do {{site.data.keyword.la_full_notm}} é fornecida no grupo de recursos **Padrão**.

Leia sobre o {{site.data.keyword.la_full_notm}}. Para obter mais informações, consulte  [ Sobre o LogDNA ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

Para concluir as etapas neste tutorial, seu ID do {{site.data.keyword.IBM_notm}} deve ter designado políticas do IAM para cada um dos recursos a seguir: 

| Recurso                             | Escopo da política de acesso | Atribuições    | Região    | Informações                  |
|--------------------------------------|----------------------------|---------|-----------|------------------------------|
| Grupo de recursos **Padrão**           |  Grupo de recursos            | Visualizador  | us-south  | Essa política é necessária para permitir que o usuário veja instâncias de serviço no Grupo de recursos padrão.    |
| Serviço {{site.data.keyword.la_full_notm}} |  Grupo de recursos            | Aplicativos </br>Gerenciador  | us-south  | Essa política é necessária para permitir que o usuário reconfigure a chave de ingestão.   |
| Instância de cluster do Kubernetes          |  Recurso                  | Aplicativos  | us-south  | Essa política é necessária para excluir e configurar o segredo e o agente LogDNA no cluster Kubernetes. |
{: caption="Tabela 1. Lista de políticas do IAM necessárias para concluir o tutorial" caption-side="top"} 

Para obter mais informações sobre as funções do IAM do {{site.data.keyword.containerlong}}, consulte [Permissões de acesso de usuário](/docs/containers?topic=containers-access_reference#access_reference).

Instale a CLI do {{site.data.keyword.cloud_notm}} e o plug-in da CLI do Kubernetes. Para obter mais informações, consulte [Instalando a CLI do {{site.data.keyword.cloud_notm}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#ibmcloud-cli).


## Etapa 1: reconfigurar a chave de ingestão
{: #kube_reset_step1}

Para renovar a chave de ingestão para uma instância do {{site.data.keyword.la_full_notm}} usando a IU da web do {{site.data.keyword.la_full_notm}}, conclua as etapas a seguir:

1. Ative a IU da web do {{site.data.keyword.la_full_notm}}. Para obter mais informações, consulte [Ativando a IU da web do {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Selecione o ícone  ** Configuração ** . Em seguida, selecione  ** Organização **. 

3. Selecione  ** Chaves API **.

    É possível ver as chaves de ingestão que foram criadas. 

4. Selecione  ** Generate Ingestion Key **.

    Uma nova chave é incluída na lista.

5. Exclua a chave de ingestão antiga. Clique em  ** excluir **.


## Etapa 2: Remover qualquer configuração no cluster que use a antiga chave de ingestão
{: #kube_reset_step2}

Conclua as etapas a seguir:

1. Abra um terminal. Em seguida, efetue login no  {{site.data.keyword.cloud_notm}}. Execute o comando a seguir e siga os prompts:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Selecione a conta na qual você provisionou a instância do {{site.data.keyword.la_full_notm}}.

2. Configure o ambiente em cluster. Execute os comandos a seguir:

    Primeiro, obtenha o comando para configurar a variável de ambiente e faça download dos arquivos de configuração do Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Quando o download dos arquivos de configuração estiver concluído, será exibido um comando que poderá ser usado para configurar o caminho para o seu arquivo de configuração local do Kubernetes como uma variável de ambiente.

    Em seguida, copie e cole o comando que é exibido em seu terminal para configurar a variável de ambiente KUBECONFIG.

    **Nota:** toda vez que você efetuar login na CLI do {{site.data.keyword.containerlong}} para trabalhar com clusters, deverá executar esses comandos para configurar o caminho para o arquivo de configuração do cluster como uma variável de sessão. O Kubernetes CLI usa essa variável para localizar um arquivo de configuração local e certificados que são necessárias para se conectar ao cluster no {{site.data.keyword.cloud_notm}}.

3. Remova o segredo do cluster Kubernetes. O segredo do Kubernetes contém a chave de ingestão do LogDNA. Execute o comando a seguir:

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Remova o agente LogDNA em cada trabalhador (nó) de seu cluster Kubernetes. O agente do LogDNA é responsável por coletar e encaminhar os seus logs. Execute o comando a seguir:

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. Verifique se o agente LogDNA foi excluído com sucesso. Execute o comando a seguir:

    ```
    kubectl get pods
    ```
    {: codeblock}

    Nenhum pod do LogDNA deve ser exibido.


## Etapa 3: Configurar o cluster Kubernetes com a nova chave de ingestão
{: #kube_reset_step3}

Para configurar o seu cluster Kubernetes para encaminhar logs para a sua instância do LogDNA, conclua as etapas a seguir por meio da linha de comandos:

1. Abra um terminal. Em seguida, efetue login no  {{site.data.keyword.cloud_notm}}. Execute o comando a seguir e siga os prompts:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Selecione a conta na qual você provisionou a instância do {{site.data.keyword.la_full_notm}}.

2. Configure o ambiente em cluster. Execute os comandos a seguir:

    Primeiro, obtenha o comando para configurar a variável de ambiente e faça download dos arquivos de configuração do Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Quando o download dos arquivos de configuração estiver concluído, será exibido um comando que poderá ser usado para configurar o caminho para o seu arquivo de configuração local do Kubernetes como uma variável de ambiente.

    Em seguida, copie e cole o comando que é exibido em seu terminal para configurar a variável de ambiente KUBECONFIG.

    **Nota:** toda vez que você efetuar login na CLI do {{site.data.keyword.containerlong}} para trabalhar com clusters, deverá executar esses comandos para configurar o caminho para o arquivo de configuração do cluster como uma variável de sessão. O Kubernetes CLI usa essa variável para localizar um arquivo de configuração local e certificados que são necessárias para se conectar ao cluster no {{site.data.keyword.cloud_notm}}.

3. Inclua um segredo em seu cluster Kubernetes. Execute o comando a seguir:

    ```
    kubectl create secret generic logdna-agent-key--from-literal=logdna-agent-key = LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE
    ```
    {: codeblock}

    O LOGDNA_INGESTION_KEY_FOR_YOUR_INSTANCE mostra a chave de ingestão de LogDNA para a sua instância.

    O segredo do Kubernetes contém a chave de ingestão do LogDNA. A chave de ingestão de LogDNA é usada para autenticar o agente de criação de log com o serviço {{site.data.keyword.la_full_notm}}. Ela é usada para abrir um soquete seguro da web para o servidor de ingestão no sistema back-end de criação de log.

4. Configure o agente LogDNA em cada trabalhador (nó) de seu cluster Kubernetes. Execute o comando a seguir:

    ```
    kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
    ```
    {: codeblock}

    O agente do LogDNA é responsável por coletar e encaminhar os seus logs.

    O agente coleta automaticamente os logs com extensão *.log e arquivos sem extensão localizados em /var/log. Por padrão, os logs são coletados de todos os namespaces, incluindo o kube-system.

5. Verifique o status do agente LogDNA e se ele foi criado com sucesso. Execute o comando a seguir:

    ```
    kubectl get pods
    ```
    {: codeblock}


## Etapa 4: Ativar a IU da web do LogDNA
{: #kube_reset_step4}

Para ativar o painel do IBM Log Analysis com LogDNA por meio da IU do {{site.data.keyword.cloud_notm}}, conclua as etapas a seguir:

1. Efetue login em sua conta do  {{site.data.keyword.cloud_notm}} .

    Clique em [ Painel do {{site.data.keyword.cloud_notm}}![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window} para ativar o painel do {{site.data.keyword.cloud_notm}}.

	Depois de efetuar login com seu ID do usuário e senha, o painel do {{site.data.keyword.cloud_notm}} se abre.

2. No menu de navegação, selecione  ** Observabilidade **. 

3. Selecione  ** Criação de log **. 

    A lista de instâncias do {{site.data.keyword.la_full_notm}} que estão disponíveis no {{site.data.keyword.cloud_notm}} é exibida.

3. Selecione uma instância. Em seguida, clique em  ** Visualizar logs **.

    A IU da web do LogDNA é aberta e exibe os logs do cluster.


## Etapa 5: Visualizar seus logs
{: #kube_reset_step5}

Na IU da web do LogDNA, é possível visualizar os seus logs à medida que eles passam pelo sistema. Você visualiza logs usando o registro de log mais recente. 

**Nota:**com o plano de serviço **Grátis**, é possível seguir somente os seus logs mais recentes.



## Próximos passos
{: #kube_reset_next_steps}

  Se você desejar [filtrar logs de cluster](https://docs.logdna.com/docs/filters), [procurar logs de cluster](https://docs.logdna.com/docs/search), [definir visualizações](https://docs.logdna.com/docs/views) e [configurar alertas](https://docs.logdna.com/docs/alerts), será necessário fazer upgrade do plano {{site.data.keyword.la_full_notm}} para um plano pago.



