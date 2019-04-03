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


# Mensagens de erro
{: #error_msgs}

Será possível ver estas mensagens de erro ao usar o serviço {{site.data.keyword.loganalysisshort}} no {{site.data.keyword.Bluemix}}:
{:shortdesc}

## BXNLG020001W
{: #BXNLG020001W}

**Descrição da mensagem**

Você atingiu a cota diária alocada para o espaço do Bluemix {GUID do espaço} para a instância do {{site.data.keyword.loganalysisfull}} {GUID da instância}. Sua dotação diária atual é 500 MB para armazenamento de Procura de log, que ficará retida no armazenamento de Procura de log por um período de 3 dias, durante o qual poderá ser procurada no Kibana. Para fazer upgrade de seu plano para que seja possível armazenar mais dados no armazenamento de Procura de log por dia e também reter todos os logs no armazenamento de Coleção de logs, faça upgrade do plano de serviço {{site.data.keyword.loganalysisshort}} para esse espaço. Para obter mais informações sobre planos de serviços e como fazer upgrade do plano, veja [Planos](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).


**Explicação da mensagem** 

Você poderá receber uma mensagem com o ID *BXNLG020001W* ao atingir a cota de armazenamento do Log de procura alocada para o plano de serviço Lite. O plano Lite é o plano de serviço complementar que é configurado por padrão quando você provisiona o serviço {{site.data.keyword.loganalysisshort}} em um espaço. Sua dotação diária atual é 500 MB para armazenamento de Procura de log, que ficará retida no armazenamento de Procura de log por um período de 3 dias, durante o qual poderá ser procurada no Kibana.

**Recuperação
**

Para fazer upgrade de seu plano para que seja possível armazenar mais dados no armazenamento de Procura de log por dia e também reter todos os logs no armazenamento de Coleção de logs, faça upgrade do plano de serviço {{site.data.keyword.loganalysisshort}} para esse espaço. Para obter mais informações sobre planos de serviços e como fazer upgrade do plano, veja [Planos](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).


## BXNLG020002W 
{: #BXNLG020002W}


**Descrição da mensagem**

Você atingiu a cota diária alocada para o espaço do Bluemix {GUID do espaço} para a instância do {{site.data.keyword.loganalysisfull}} {GUID da instância}.  Sua dotação diária atual é XXX para armazenamento de Procura de log, que ficará retida por um período de 3 dias, durante o qual poderá ser procurada no Kibana. Isso não afeta a política de retenção de log no armazenamento de Coleção de logs. Para fazer upgrade de seu plano para que seja possível armazenar mais dados no armazenamento de Procura de log por dia, faça upgrade do plano de serviço {{site.data.keyword.loganalysisshort}} para esse espaço. Para obter mais informações sobre planos de serviços e como fazer upgrade do plano, veja [Planos](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).

XXX representa o tamanho dos dados que podem ser procurados para seu plano atual.

**Explicação da mensagem** 

Você atingiu a cota diária alocada para o espaço {GUID do espaço} para a instância do {{site.data.keyword.loganalysisfull}} {GUID da instância}.  Sua dotação diária atual é 500 MB, 2 GB, 5 GB ou 10 GB para armazenamento de Procura de log, que ficará retida por um período de 3 dias, durante o qual poderá ser procurada no Kibana. Isso não afeta a política de retenção de log no armazenamento de Coleção de logs.

**Recuperação
**

Para fazer upgrade de seu plano para que seja possível armazenar mais dados no armazenamento de Procura de log por dia, faça upgrade do plano de serviço {{site.data.keyword.loganalysisshort}} para esse espaço. Para obter mais informações sobre planos de serviços e como fazer upgrade do plano, veja [Planos](/docs/services/CloudLogAnalysis/log_analysis_ov.html#plans).




