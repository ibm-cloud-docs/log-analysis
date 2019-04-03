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

# Enviando dados no local para um espaço no IBM Cloud
{: #send_data_mt}

Para enviar dados de log para o serviço {{site.data.keyword.loganalysisshort}}, é possível configurar um Multi-Tenant Logstash Forwarder (mt-logstash-forwarder). 
{: shortdesc}

Conclua as etapas a seguir para enviar dados do log para um espaço no {{site.data.keyword.Bluemix_notm}}:

## Pré-requisitos
{: #prereqs1}

* Um {{site.data.keyword.Bluemix_notm}} ID para efetuar login no {{site.data.keyword.Bluemix_notm}}.
* Um ID do usuário que tenha permissões para trabalhar em um espaço com o serviço {{site.data.keyword.loganalysisshort}}. Para obter mais informações, veja [Segurança](/docs/services/CloudLogAnalysis/security_ov.html#security_ov).
* A CLI do {{site.data.keyword.loganalysisshort}} instalada em seu ambiente local.
* O serviço {{site.data.keyword.loganalysisshort}} provisionado em um espaço em sua conta com um plano que permite a ingestão de logs.


## Etapa 1: Obter o token de criação
{: #get_logging_auth_token}

Conclua as etapas a seguir de uma sessão de terminal na qual a CLI do {{site.data.keyword.loganalysisshort}} está instalada:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).
    
2. Execute o comando  ` ibmcloud logging token-get ` . 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    O comando retorna o token de criação de log.
    
    Por
exemplo,

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    em que *ID do locatário* é o GUID do espaço no qual você planeja enviar logs.


## Etapa 2: Configurar o mt-logstash-forwarder
{: #configure_mt_logstash_forwarder}

Conclua as etapas a seguir para configurar o mt-logstash-forwarder no ambiente do qual você planeja enviar logs para o serviço {{site.data.keyword.loganalysisshort}}:

1.	Efetue login como usuário raiz. 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	Instale o pacote do Network Time Protocol (NTP) para sincronizar o horário dos logs. 

    Por exemplo, para um sistema Ubunutu, verifique se `timedatectl status` mostra *Network time on: yes*. Em caso positivo, o sistema Ubuntu já está configurado para usar ntp e será possível ignorar esta etapa.
    
    ```
    # timedatectl status
    Local time: Mon 2017-06-12 03:01:22 PDT
    Universal time: Mon 2017-06-12 10:01:22 UTC
    RTC time: Mon 2017-06-12 10:01:22
    Time zone: America/Los_Angeles (PDT, -0700)
    Network time on: yes
    NTP synchronized: yes
    RTC in local TZ: no
    ```
    {: screen}
    
    Conclua as etapas a seguir para instalar ntp em um sistema Ubuntu:

    1.	Execute o comando a seguir para atualizar os pacotes. 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	Execute o comando a seguir para instalar o pacote ntp. 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	Execute o comando a seguir para instalar o pacote ntpdate. 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	Execute o comando a seguir para parar o serviço 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	Execute o comando a seguir para sincronizar o relógio do sistema. 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        O resultado confirma que o horário está ajustado, por exemplo:
        
        ```
        4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	Execute o comando a seguir para iniciar o ntpd novamente. 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        O resultado confirma que o serviço está sendo iniciado.

    7.	Execute o comando a seguir para ativar o serviço ntpd para iniciar automaticamente após um travamento ou uma reinicialização. 
    
        ```
        Service ntp permitem
        ```
        {: codeblock}
        
        O resultado exibido é uma lista de comandos que podem ser usados para gerenciar o serviço ntpd, por exemplo:
        
        ```
        Uso: /etc/init.d/ntpd {
        ```
        {: screen}

3. Inclua o repositório do serviço {{site.data.keyword.loganalysisshort}} no gerenciador de pacote do sistema. Execute o comando a seguir:

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. Instale e configure mt-logstash-forwarder para enviar logs de seu ambiente para a Coleção de logs. 

    1. Execute o comando a seguir para instalar mt-logstash-forwarder:
    
        ```
        Apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. Crie o arquivo de configuração mt-logstash-forwarder para seu ambiente. Esse arquivo inclui variáveis que são usadas para configurar o mt logstash forwarder para apontar o encaminhador para o serviço {{site.data.keyword.loganalysisshort}}.
    
       Edite o arquivo `/etc/mt-logstash-forwarder/mt-lsf-config.sh`. Por exemplo, é possível usar o editor de vi:
               
       ```
       Vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       Para apontar o encaminhador para o serviço {{site.data.keyword.loganalysisshort}}, inclua as variáveis a seguir no arquivo **mt-lsf-config.sh**: 
         
       <table>
          <caption>Tabela 1. Lista de variáveis necessárias para apontar o encaminhador em uma VM para o serviço {{site.data.keyword.loganalysisshort}} </caption>
          <tr>
            <th>Nome da Variável</th>
            <th>Descrição</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>ID para sua VM, por exemplo. *MyTestVM*. </td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>URL de Destino. Para obter as listas de URLs de ingestão, veja [URLs de ingestão](/docs/services/CloudLogAnalysis/log_ingestion.html#log_ingestion_urls). Por exemplo, configure o valor como **ingest.logging.ng.bluemix.net:9091** para enviar logs na região sul dos EUA. </td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>ID do espaço no qual o serviço {{site.data.keyword.loganalysisshort}} está pronto para coletar os logs que você envia para o {{site.data.keyword.Bluemix_notm}}. <br>Use o valor obtido na etapa 1.</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>Criação de token. <br>Use o valor obtido na etapa 1.</td>
          </tr>
          <tr>
            <td>Group_name</td>
            <td>Configure esse valor como uma tag customizada que possa ser definida para agrupar logs relacionados.</td>
          </tr>
       </table>
        
       Por exemplo, veja o arquivo de amostra a seguir de um espaço que tem o ID *7d576e3b-170b-4fc2-a6c6-b7166fd57912* na região do Reino Unido:
        
       ```
       # more mt-lsf-config.sh 
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. Inicie o mt-logstash-forwarder. 
    
       ```
       Serviço mt-logstash-forwarder start
       ```
       {: codeblock}
                
Por padrão, o encaminhador só observa o syslog. Seus logs ficam disponíveis no Kibana para análise.
        

## Etapa 3: Especifique mais arquivos de log
{: #add_logs}

Por padrão, apenas o arquivo /var/log/syslog é monitorado pelo encaminhador. É possível incluir mais arquivos de configuração no diretório a seguir `/etc/mt-logstash-forwarder/conf.d/syslog.conf/` para que o encaminhador também os monitore. 

Conclua as etapas a seguir para incluir um arquivo de configuração de um app executado em seu ambiente:

1.	Copie o `/etc/mt-logstash-forwarder/conf. d/syslog.conf` . 

    **Dica:** não edite o arquivo syslog.conf para incluir arquivos de log.
    
    Por exemplo, em um sistema Ubuntu, execute o comando a seguir:
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	Com um editor de texto, edite o arquivo *myapp.conf* e atualize o arquivo para incluir os logs do aplicativo que você deseja monitorar. Inclua o tipo de log para cada log do app. Exclua os exemplos não usados.

3.	Reinicie o mt-logstash-forwarder. 

     Reinicie o serviço mt-logstash-forwarder. Execute o comando a seguir:
    
    ```
    Serviço mt-logstash-forwarder restart
    ```
    {: codeblock}

**Exemplo**

Para incluir o stdout ou stderr por meio de um app hello, redirecione stdout ou stderr para um arquivo de log. Crie um arquivo de configuração de encaminhador para o app. Em seguida, reinicie o mt-logstash-forwarder.

1.	Copie o `/etc/mt-logstash-forwarder/conf. d/syslog.conf` . 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. Edite o arquivo de configuração *<filepath>myapp.conf*.

    Para ser possível procurar por um campo JSON no Kibana ao alimentar um log, ative a análise sintática de JSON. Configure `is_json` como true no arquivo de configuração para caminhos de arquivo específicos. Para arquivos de log configurados dessa maneira, as linhas do log devem ser formatadas como blocos JSON, separadas por retornos de linha. O mt-logstash-forwarder consumirá então todos esses campos JSON como campos individuais que podem ser procurados por Kibana. Os nomes dos campos JSON incluem um sufixo que se baseia no tipo.
    
    ```
    {
    "files":[
         # other file configurations omitted...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
