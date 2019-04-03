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


# Enviando logs de fora do {{site.data.keyword.Bluemix_notm}}
{: #log_ingestion}

É possível enviar logs de fora do {{site.data.keyword.IBM_notm}} Cloud para o serviço {{site.data.keyword.loganalysisshort}} usando o Logstash Forwarder de diversos locatários. 
{:shortdesc}

Esse recurso está disponível somente para planos de serviços que permitem a ingestão de log. Para obter mais informações, veja [Planos de serviço](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_analysis_ov#plans).

Para enviar logs de fora do {{site.data.keyword.IBM_notm}} Cloud para o serviço {{site.data.keyword.loganalysisshort}}, você precisa dos recursos em Nuvem a seguir:

* Um {{site.data.keyword.IBM_notm}}id para efetuar login no {{site.data.keyword.Bluemix_notm}}. Esse ID do usuário deve ter permissões para trabalhar com o serviço {{site.data.keyword.loganalysisshort}} em um espaço no {{site.data.keyword.Bluemix_notm}}. O espaço é o domínio no {{site.data.keyword.Bluemix_notm}} em que você planeja enviar e analisar logs.
* Um token de criação de log que é gerado usando a CLI do {{site.data.keyword.loganalysisshort}} e é usado para autenticar seu ambiente local com o serviço {{site.data.keyword.loganalysisshort}}.  

Em seu ambiente local, deve-se configurar o mt-logstash-forwarder e especificar os arquivos de log que você deseja enviar para o serviço {{site.data.keyword.loganalysisshort}}.

Para obter mais informações sobre como configurar seu ambiente local para enviar logs para o serviço {{site.data.keyword.loganalysisshort}}, veja [Enviando dados no local para um espaço no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/how-to/send-data?topic=cloudloganalysis-send_data_mt#send_data_mt).



## URLs de ingestão
{: #log_ingestion_urls}

A tabela a seguir lista as URLs que se deve usar para enviar logs para o {{site.data.keyword.Bluemix_notm}}:

<table>
  <caption>URLs de ingestão</caption>
    <tr>
      <th>Region</th>
      <th>URL</th>
    </tr>
  <tr>
    <td>Alemanha</td>
	  <td>ingest-eu-fra.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Sydney</td>
	  <td>ingest-au-syd.logging.bluemix.net:9091</td>
  </tr>
  <tr>
    <td></td>
	  <td>ingest.logging.eu-gb.bluemix.net:9091</td>
  </tr>
  <tr>
    <td>Sul dos Estados Unidos</td>
	  <td>Ingest.logging.ng.bluemix.net:9091</td>
  </tr>
</table>


