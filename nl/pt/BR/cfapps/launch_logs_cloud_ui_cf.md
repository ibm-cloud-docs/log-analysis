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

# Navegando para os logs de um app Cloud Foundry
{: #launch_logs_cloud_ui_cf}

Na UI do {{site.data.keyword.Bluemix}}, é possível visualizar, filtrar e analisar logs por meio da guia de log disponível para cada app Cloud Foundry ou por meio da UI de serviço do {{site.data.keyword.loganalysisshort}}.
{:shortdesc}

Para visualizar logs do app CF, considere as informações a seguir: 

<table>
  <caption>Informações sobre logs do app CF no {{site.data.keyword.Bluemix_notm}}</caption>
  <tr>
    <th>Opções de UI</th>
    <th>Informações</th>
  </tr>
  <tr>
    <td>Guia Log disponível por meio da UI do app CF </td>
    <td>Os logs disponíveis para análise incluem dados das últimas 24 horas.</td>
  </tr>
  <tr>
    <td>Painel do {{site.data.keyword.loganalysisshort}} (Kibana)</td>
    <td>Os logs disponíveis para análise incluem dados dos últimos 3 dias. Também é possível especificar um período customizado.</td>
  </tr>
</table>


## Navegando para os logs do app CF por meio do painel do app CF 
{: #cfapp_ui}

Para ver os logs de implementação ou de tempo de execução de um app Cloud Foundry, conclua as
etapas a seguir:

1. No painel Apps, clique no nome do seu app Cloud Foundry. 
    
2. Na página de detalhes do app, clique em **Logs**.
    
    Na guia **Logs**, é possível visualizar os logs recentes para seu app ou
acompanhar os logs em tempo real. Além disso, é possível filtrar logs por componente (tipo de log), por ID da instância do app e por erro.
    
Por padrão, os logs que estão disponíveis para análise no
console do {{site.data.keyword.Bluemix_notm}}
incluem dados das últimas 24 horas.


## Navegando para os logs do app CF por meio da UI do {{site.data.keyword.loganalysisshort}} 
{: #cfapp_la}

Para ver os logs de implementação ou de tempo de execução de um app Cloud Foundry, conclua as
etapas a seguir:

1. No painel Apps, clique no nome do seu app Cloud Foundry. 
    
2. Na página de detalhes do app, clique em **Logs**.
    
3. Clique em **Visualizar no Kibana**.

Por padrão, os logs disponíveis para análise incluem dados dos últimos 15 minutos.

**Dica:** para analisar dados para um período customizado, veja [Análise de log avançada com o Kibana](/docs/services/CloudLogAnalysis/kibana?topic=cloudloganalysis-analyzing_logs_Kibana#analyzing_logs_Kibana). 


