---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, ingestion key

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

# Trabalhando com chaves de ingestão
{: #ingestion_key}

A chave de ingestão é uma chave de segurança que você deve usar para configurar os agentes LogDNA e encaminhar os logs com sucesso para a sua instância do {{site.data.keyword.la_full_notm}} no {{site.data.keyword.cloud_notm}}. Você obterá automaticamente a chave de ingestão ao fornecer uma instância. Como alternativa, também é possível obter a chave de ingestão criando um ID de serviço para a instância. 
{:shortdesc}

** Nota: ** 

* Para trabalhar com chaves de ingestão por meio da IU da web do {{site.data.keyword.la_full_notm}}, deve-se ter uma política do IAM com a função de plataforma **Visualizador** e a função de serviço **Gerenciador** para o serviço {{site.data.keyword.la_full_notm}}. 
* Para trabalhar com chaves de ingestão por meio da IU do {{site.data.keyword.cloud_notm}}, deve-se ter uma política do IAM com a função de plataforma **Editor** e a função de serviço **Gerenciador** para o serviço {{site.data.keyword.la_full_notm}}. 


## Obtenha a chave de ingestão por meio da IU do {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_ui}

Para obter a chave de ingestão para uma instância do {{site.data.keyword.la_full_notm}} usando a IU do {{site.data.keyword.cloud_notm}}, conclua as etapas a seguir:

1. Efetue login em sua conta do  {{site.data.keyword.cloud_notm}} .

    Clique em [ Painel do {{site.data.keyword.cloud_notm}}![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window} para ativar o painel do {{site.data.keyword.cloud_notm}}.

	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.cloud_notm}} é aberta.

2. No menu de navegação, selecione  ** Observabilidade **. 

3. Selecione  ** Criação de log **. O painel do  {{site.data.keyword.la_full_notm}}  é aberto. É possível ver a lista de instâncias de criação de log que estão disponíveis no {{site.data.keyword.cloud_notm}}.

3. Identifique a instância para a qual você deseja obter a chave de ingestão e clique em **Visualizar chave de ingestão**.

4. É aberta uma janela na qual é possível clicar em **Mostrar** para visualizar a chave de ingestão.


## Obtenha a chave de ingestão por meio da IU da web do {{site.data.keyword.la_full_notm}}
{: #logdna_ui}

Para obter a chave de ingestão para uma instância do {{site.data.keyword.la_full_notm}} usando a IU da web do {{site.data.keyword.la_full_notm}}, conclua as etapas a seguir:

1. Ative a IU da web do {{site.data.keyword.la_full_notm}}. Para obter mais informações, consulte [Ativando a IU da web do {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Selecione o ícone  ** Configuração ** . Em seguida, selecione  ** Organização **. 

3. Selecione  ** Chaves API **.

É possível ver as chaves de ingestão que foram criadas. 

**Nota:** apenas uma chave de ingestão está ativa por vez. 


## Obtenha a chave de ingestão por meio da CLI do {{site.data.keyword.cloud_notm}}
{: #ibm_cloud_cli}

Para obter a chave de ingestão para uma instância do {{site.data.keyword.la_full_notm}} por meio da linha de comandos, conclua as etapas a seguir:

1. [ Pré-requisito ] Instale a CLI do  {{site.data.keyword.cloud_notm}} .

   Para obter mais informações, consulte [Instalando a CLI do {{site.data.keyword.cloud_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-about#about).

   Se a CLI estiver instalada, continue com a próxima etapa.

2. Efetue login na região no {{site.data.keyword.cloud_notm}} no qual a instância está em execução. Execute o comando a seguir: [`ibmcloud login`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_login)

3. Configure o grupo de recursos no qual a instância do {{site.data.keyword.la_full_notm}} está em execução. Execute o comando a seguir: [`ibmcloud target`](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_cli#ibmcloud_target) com a opção `-g`.

    Por padrão, o grupo de recursos `default` é configurado.

4. Obtenha o nome da chave de API que está associada à instância do {{site.data.keyword.la_full_notm}}. Execute o comando  [ ` ibmcloud resource service-keys ` ](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_keys) :

    ```
    ibmcloud resource service-keys
    ```
    {: codeblock}

    Identifique a chave de serviço que está associada à sua instância.

5. Pegue a chave de ingestão. Execute o comando  [ ` ibmcloud resource service-key ` ](/docs/cli/reference/ibmcloud?topic=cloud-cli-ibmcloud_commands_resource#ibmcloud_resource_service_key) :

    ```
    ibmcloud resource service-key APIKEY_NAME
    ```
    {: codeblock}

    Em que APIKEY_NAME é o nome da chave de API
 
    A saída desse comando inclui o campo **ingestion_key** que contém a chave de ingestão para a instância.


## Reconfigurar a chave de ingestão 
{: #reset}

Se a chave de ingestão estiver comprometida ou você tiver uma política para renová-la após um número de dias, será possível gerar uma nova chave e excluir a antiga.

Para renovar a chave de ingestão para uma instância do {{site.data.keyword.la_full_notm}} usando a IU da web do {{site.data.keyword.la_full_notm}}, conclua as etapas a seguir:

1. Ative a IU da web do {{site.data.keyword.la_full_notm}}. Para obter mais informações, consulte [Ativando a IU da web do {{site.data.keyword.la_full_notm}}](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step2).

2. Selecione o ícone  ** Configuração ** . Em seguida, selecione  ** Organização **. 

3. Selecione  ** Chaves API **.

    É possível ver as chaves de ingestão que foram criadas. 

4. Selecione  ** Generate Ingestion Key **.

    Uma nova chave é incluída na lista.

5. Exclua a chave de ingestão antiga. Clique em  ** excluir **.

**Nota:** depois de reconfigurar a chave de ingestão, deve-se atualizá-la para quaisquer origens de log que você configurou para encaminhar os logs para esta instância do {{site.data.keyword.la_full_notm}}.



