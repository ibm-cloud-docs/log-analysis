---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# Configurando os logs de serviço do {{site.data.keyword.cloud_notm}}
{: #config_svc_logs}

É possível ter múltiplas instâncias do {{site.data.keyword.la_full_notm}} em uma região. No entanto, apenas uma instância em uma região pode ser configurada para receber logs de serviços ativados no {{site.data.keyword.cloud_notm}}.
{:shortdesc}



## Configurando logs de serviços de plataforma por meio do painel Observabilidade
{: #config_svc_logs_ui}

Para configurar uma instância por meio do painel Observabilidade no {{site.data.keyword.cloud_notm}}, conclua as etapas a seguir:

1. [Efetue login em sua conta do {{site.data.keyword.cloud_notm}} ![Ícone de link externo](../../icons/launch-glyph.svg "Ícone de link externo")](https://cloud.ibm.com/login){:new_window}.

	Depois de efetuar login com seu ID de usuário e senha, a UI do {{site.data.keyword.cloud_notm}} é aberta.

2. Acesse o ícone de menu ![Ícone de menu](../../icons/icon_hamburger.svg). Em seguida, selecione **Observabilidade** para acessar o painel *Observabilidade*.

3. Selecione **Criação de log**e, em seguida, clique em **Configurar logs de serviços de plataforma**. 

4. Escolha qual instância do LogDNA receberá logs de serviços ativados na plataforma de nuvem.

5. Selecione uma região. 

6. Selecione uma instância.

7. Clique em  ** Salvar **. 

A página principal *Observabilidade* é aberta.

A instância que você escolher para receber os logs de serviço mostrará o sinalizador **Logs de serviços de plataforma**.

Para obter mais informações sobre os serviços que estão ativados para enviar logs para o {{site.data.keyword.la_full_notm}}, consulte [Serviços de nuvem](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services).

