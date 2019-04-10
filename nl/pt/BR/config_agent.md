---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, config agent

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

# Configurando um Agente LogDNA
{: #config_agent}

O agente LogDNA é responsável por coletar e encaminhar logs para a sua instância do {{site.data.keyword.la_full_notm}}. Depois de fornecer uma instância do {{site.data.keyword.la_full}}, deve-se configurar um agente LogDNA para cada origem de log que você deseja monitorar.
{:shortdesc}

* O agente LogDNA é autenticado usando a chave de ingestão do LogDNA e abre um soquete seguro da web para os servidores de ingestão do {{site.data.keyword.la_full_notm}}. 
* Por padrão, o agente monitora todos os arquivos com a extensão *.log* e os arquivos sem extensão em */var/log/*.
* O agente segue os novos dados do log e procura novos arquivos que são incluídos nos diretórios de criação de log que o agente monitora.

É possível configurar os parâmetros a seguir por meio do agente LogDNA: 

| Parâmetro | Descrição |
|-----------|-------------|
| `tags`    | Defina tags para agrupar hosts automaticamente em grupos dinâmicos. |
| `logdir`  | Defina os caminhos customizados que você deseja que o agente monitore. </br>Separe vários caminhos usando vírgulas. É possível usar padrões de bola. É possível configurar arquivos específicos. Insira padrões glob usando aspas duplas. |
| `exclude` | Defina os arquivos que você não deseja que o agente LogDNA monitore. **Nota:** esses arquivos podem ser localizados em qualquer um dos caminhos definidos por meio do parâmetro logdir. </br>Separe vários arquivos usando vírgulas. É possível usar padrões de bola. É possível configurar arquivos específicos. |
| `exclude_regex` | Defina padrões regex para filtrar quaisquer linhas que correspondam ao padrão. Não inclua `/` à esquerda e à direita. |
| `hostname` | Defina o nome do host. Esse valor substitui o nome do host do sistema operacional. |
| `autoupdate` | Configure como `1` para atualizar o agente automaticamente quando a definição do agente do repositório público for atualizada. Configure como `0` para desativar esse recurso. |  
{: caption="Tabela 1. Parâmetros para customizar um agente LogDNA" caption-side="top"} 



## Configurando um agente LogDNA em um cluster Kubernetes usando um script
{: #config_agent_kube_script}

Para configurar o cluster Kubernetes para enviar logs para a sua instância do {{site.data.keyword.la_full_notm}}, deve-se instalar um pod *logdna-agent* em cada nó do cluster. O agente do LogDNA lê os arquivos de log do pod no qual ele está instalado e encaminha os dados do log para a sua instância do LogDNA.

Para configurar o seu cluster Kubernetes para encaminhar logs para a sua instância do LogDNA, conclua as etapas a seguir por meio da linha de comandos:

1. Abra um terminal para efetuar login no {{site.data.keyword.cloud_notm}}.

   ```
   ibmcloud login -a api.ng.bluemix.net
   ```
   {: pre}

   Selecione a conta na qual você forneceu a instância do {{site.data.keyword.la_full_notm}}.

2. Configure o cluster no qual você deseja configurar a criação de log como o contexto para essa sessão.

   ```
   ibmcloud ks cluster-config <cluster_name_or_ID>
   ```
   {: pre}

   Quando
o download dos arquivos de configuração estiver concluído, será exibido um comando que poderá ser usado
para configurar o caminho para o seu arquivo de configuração local do Kubernetes como uma variável de ambiente. Copie e cole o comando que é exibido em seu terminal para configurar a variável de ambiente `KUBECONFIG`.

3. Crie um segredo do Kubernetes para armazenar a sua chave de ingestão do logDNA para a sua instância de serviço. A chave de ingestão do LogDNA é usada para abrir um soquete da web seguro para o servidor de ingestão do logDNA e para autenticar o agente de criação de log com o serviço do {{site.data.keyword.la_full_notm}}.

   ```
   kubectl create secret generic logdna-agent-key --from-literal=logdna-agent-key=<logDNA_ingestion_key>
   ```
   {: pre}

4. Crie um conjunto de daemon do Kubernetes configurado para implementar o agente do LogDNA em cada nó do trabalhador de seu cluster Kubernetes. O agente do LogDNA coleta logs com a extensão `*.log` e arquivos sem extensão que são armazenados no diretório `/var/log` de seu pod. Por padrão, os logs são coletados de todos os namespaces, incluindo `kube-system` e encaminhados automaticamente para o serviço do {{site.data.keyword.la_full_notm}}.

   ```
   kubectl create -f https://repo.logdna.com/ibm/prod/logdna-agent-ds-us-south.yaml
   ```
   {: pre}

5. Verifique se o agente do LogDNA foi implementado com êxito. 

   ```
   kubectl get pods
   ```
   {: pre}
   

A implementação será bem-sucedida quando você vir um ou mais pods do LogDNA.
* **O número de pods de LogDNA é igual ao número de nós do trabalhador em seu cluster.** 
* Todos os pods devem estar em um estado `Executando`.
* O *Stdout* e o *stderr* são coletados e encaminhados automaticamente por meio de todos os contêineres. Os dados do log incluem logs do aplicativo e logs do trabalhador. 
* Por padrão, o pod do agente LogDNA que é executado em um trabalhador coleta logs de todos os namespaces nesse nó, incluindo os logs kube-system.



## Incluindo tags em um agente LogDNA em um cluster Kubernetes
{: #config_agent_kube_tags}

Conclua as etapas a seguir para incluir tags:

1. Configure o ambiente em cluster. Execute os comandos a seguir:

    Primeiro, obtenha o comando para configurar a variável de ambiente e faça download dos arquivos de configuração do Kubernetes.

    ```
    ibmcloud ks cluster-config <cluster_name_or_ID>
    ```
    {: codeblock}

    Quando o download dos arquivos de configuração estiver concluído, será exibido um comando que poderá ser usado para configurar o caminho para o seu arquivo de configuração local do Kubernetes como uma variável de ambiente.

    Em seguida, copie e cole o comando que é exibido em seu terminal para configurar a variável de ambiente KUBECONFIG.

2. Verifique a estratégia de atualização do DaemonSet. Em seguida, escolha usar o *kubectl apply* ou o *kubectl edit* para modificar o arquivo de configuração para o agente.

    Para verificar a estratégia de atualização, execute o comando a seguir:

    ```
    kubectl get ds/logdna-agent -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
    ```
    {: pre}

    Se a estratégia de atualização estiver configurada como *OnDelete* ou se você tiver o arquivo de configuração que é gerenciado por meio de um sistema de controle de versão, atualize o arquivo de configuração local e aplique as mudanças no agente LogDNA usando *kubectl apply*.

    Se a estratégia de atualização estiver configurada como *RollingUpdate*, será possível atualizar e aplicar as mudanças no agente LogDNA usando o *kubectl edit*.

3. Edite o arquivo  ` logdna-agent-configmap.yaml ` . 

    Atualize o arquivo de configuração modificando a cópia local. **Nota:** também é possível gerar o arquivo de configuração do agente, executando o comando a seguir:

    ```
    kubectl get configmap logdna-agent -o=yaml > prod-logdna-agent-configmap.yaml
    ```
    {: codeblock}

    Como alternativa, atualize o arquivo de configuração usando *kubectl edit*.

    ```
    kubectl edit configmap logdna-agent
    ```
    {: codeblock}

4. Faça mudanças. Inclua a seção  ** LOGDNA_TAGS **.

    ```
    - nome: LOGDNA_TAGS valor: tag1,tag2,tag3
    ```
    {: codeblock}

    Por exemplo, a seção a seguir mostra onde incluir tags no arquivo de configuração:

    ```
    apiVersion: extensions/v1beta1
    kind: DaemonSet
    metadata:
      name: logdna-agent
    spec:
      template:
        metadata:
          labels:
            app: logdna-agent
        spec:
          containers:
          - name: logdna-agent
            image: logdna/logdna-agent:latest
            imagePullPolicy: Always
            env:
            - name: LOGDNA_AGENT_KEY
              valueFrom:
                 secretKeyRef:
                  name: logdna-agent-key
                  key: logdna-agent-key
            - name: LDAPIHOST
              value: api.us-south.logging.cloud.ibm.com
            - name: LDLOGHOST
              value: logs.us-south.logging.cloud.ibm.com
            - name: LOGDNA_PLATFORM
              value: k8s
            - nome: LOGDNA_TAGS valor: tag1,tag2,tag3
    ```
    {: screen}

5. Aplique as mudanças de configuração se você editar o arquivo localmente. 

    ```
    kubectl apply -f logdna-agent-configmap.yaml
    ```
    {: codeblock}
    
    **Nota:** se você usar o *kubectl edit*, as mudanças serão aplicadas automaticamente quando você salvar suas modificações.


## Configurando um agente LogDNA no Linux Ubuntu ou Debian
{: #config_agent_linux}

Para configurar o seu servidor do Ubuntu para encaminhar logs para a sua instância do {{site.data.keyword.la_full_notm}}, deve-se instalar um `logdna-agent`. O agente do LogDNA lê arquivos de log por meio de */var/log* e encaminha os dados do log para a sua instância do LogDNA.

Para configurar o seu servidor do Ubuntu para encaminhar logs para a sua instância do LogDNA, conclua as etapas a seguir por meio de um terminal do Ubuntu:

1. Instale o agente LogDNA. Execute os comandos a seguir:

    ```
    echo "deb https://repo.logdna.com stable main" | sudo tee /etc/apt/sources.list.d/logdna.list 
    ```
    {: codeblock}

    ```
    wget -O- https://repo.logdna.com/logdna.gpg | sudo apt-key add - 
    ```
    {: codeblock}

    ```
    sudo apt-get update
    ```
    {: codeblock}

    ```
    sudo apt-get install logdna-agent < "/dev/null"
    ```
    {: codeblock}

2. Configure a chave de ingestão que o agente do LogDNA deve usar para encaminhar logs para a instância do {{site.data.keyword.la_full_notm}}.  

    ```
    sudo logdna-agent -k INGESTION_KEY
    ```
    {: codeblock}

    Em que INGESTION_KEY contém a chave de ingestão ativa para a instância do {{site.data.keyword.la_full_notm}} para a qual você está configurando o encaminhamento dos logs.

3. Configure o terminal de autenticação. O agente do LogDNA usa esse host para autenticar e obter o token para encaminhar logs.

    ```
    sudo logdna-agent -s LOGDNA_APIHOST=api.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

4. Configure o terminal de ingestão.

    ```
    sudo logdna-agent -s LOGDNA_LOGHOST=logs.us-south.logging.cloud.ibm.com
    ```
    {: codeblock}

5. Defina mais caminhos de log a serem monitorados. Execute o comando a seguir: 

    ```
    sudo logdna-agent -d /path/to/log/folders
    ```
    {: codeblock}

    Por padrão,  ** /var/log **  é monitorado.

6. Opcionalmente, configure o agente do LogDNA para identificar os seus hosts. 


## Incluindo tags em um agente LogDNA no Linux Ubuntu ou Debian
{: #config_agent-linux_tags}
 

Conclua as etapas a seguir para incluir mais tags no agente LogDNA:

1. Verifique se o agente LogDNA está em execução.

2. Inclua uma ou mais tags.

    ```
    sudo logdna-agent -t TAG1, TAG2 
    ```
    {: codeblock}


Também é possível editar o arquivo de configuração LogDNA e incluir tags. O arquivo de configuração está localizado em */etc/logdna.conf*.

1. Edite o arquivo.

    ```
    sudo update-rc.d logdna-agent defaults
    ```
    {: codeblock}

2. Incluir tags.

3. Reinicie o agente LogDNA.

    ``` 
    sudo /etc/init.d/logdna-agent start
    ```
    {: codeblock}














