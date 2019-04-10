---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# Removendo um agente LogDNA de uma instância
{: #detach_agent}

Remova um agente LogDNA de uma instância de criação de log para parar a coleta de logs.
{:shortdesc}

## Removendo um agente LogDNA de um cluster Kubernetes
{: #detach_agent_kube}

Para fazer com que o cluster Kubernetes pare de enviar logs para a instância do {{site.data.keyword.la_full_notm}}, deve-se remover o agente LogDNA do cluster. 

Para fazer com que o cluster Kubernetes pare de encaminhar logs para a sua instância do LogDNA, conclua as etapas a seguir por meio da linha de comandos:

1. Abra um terminal. Em seguida, [efetue login no {{site.data.keyword.cloud_notm}} ![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window} e siga os prompts.

    Selecione a conta na qual você forneceu a instância do {{site.data.keyword.la_full_notm}}.

2. Configure o ambiente em cluster. Execute os comandos a seguir:

    Primeiro, obtenha o comando para configurar a variável de ambiente e faça download dos arquivos de configuração do Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Quando o download dos arquivos de configuração estiver concluído, será exibido um comando que poderá ser usado para configurar o caminho para o seu arquivo de configuração local do Kubernetes como uma variável de ambiente.

    Em seguida, copie e cole o comando que é exibido em seu terminal para configurar a variável de ambiente `KUBECONFIG`.

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




