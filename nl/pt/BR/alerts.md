---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, alerts

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

 
# Trabalhando com alertas
{: #alerts}

É possível anexar um ou mais alertas a uma visualização. É possível definir múltiplos canais de notificação para um alerta. É possível silenciar alertas. É possível remover alertas de uma visualização.
{:shortdesc}

É possível configurar qualquer uma das condições a seguir para um alerta:

* *Frequência de tempo*: especifique com que frequência acionar um alerta. Os valores válidos são: 30 segundos, 1 minuto, 5 minutos, 15 minutos, 30 minutos, 1 hora, 6 horas, 12 horas, 24 horas
* *Contador de linhas de log*: especifique o número de linhas de log que correspondem aos critérios de filtragem e de procura da visualização. Quando o número de linhas de log é atingido, um alerta é acionado.

É possível decidir se as duas condições são verificadas ou apenas uma. Se ambas as condições forem configuradas, um alerta será acionado quando qualquer um dos limites for atingido. 

Por exemplo, é possível configurar um alerta que seja acionado após 30 segundos ou quando 100 linhas de log correspondentes aos critérios de filtragem e de procura da visualização forem coletadas.

É possível configurar diversos canais de notificação. Os canais válidos são: `email`, `Slack`, `PagerDuty`, `Webhook`, `OpsGenie`, `Datadog`, `AppOptics`, `VictorOps`

Também será possível definir uma **pré-configuração**. Uma pré-configuração é um modelo de alerta que pode ser anexado a qualquer número de visualizações. 

Para reutilizar uma configuração de alerta com diferentes visualizações, configure uma **pré-configuração de alerta**.
{: tip}

Um ícone de sino é exibido com a visualização para indicar que ela tem um alerta anexado.



## Configurar uma pré-configuração (modelo de alerta)
{: #config_preset}

Conclua as etapas a seguir para definir uma pré-configuração:

1. Selecione o ícone de **Configuração** ![Ícone de Configuração](images/admin.png "Ícone de Administrador").
2. Selecione  ** Alertas **.
3. Selecione  ** Incluir um alerta de pré-configuração **.
4. Escolha um canal de notificação. 
5. Defina as condições de limite.

    1. Selecione uma frequência de tempo. Por exemplo, 12 horas.

    2. Insira o número de linhas de log após as quais você deseja que o alerta seja acionado.

    3. Selecione se deseja que ambas as condições sejam verificadas ou apenas uma.

6. Inclua os detalhes para o canal de notificação que você escolheu.

    Por exemplo, para o canal de notificação por e-mail, inclua um ou mais destinatários e, opcionalmente, um fuso horário.

7. Clique em  ** Salvar alerta **.



## Configure um alerta usando uma pré-configuração
{: #config_alert_preset}

Conclua as etapas a seguir para anexar uma pré-configuração a uma visualização:

1. Clique no ícone  ** Visualizações **   ![Configuration icon](images/views.png).
2. Crie uma visualização. 

    Aplique um prazo, filtros e critérios de procura para filtrar as linhas de log que são exibidas por meio da visualização. 

    Para obter mais informações, consulte  [ Criando visualizações ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Clique no nome da visualização. Em seguida, selecione  ** Anexar um alerta **.

4. Escolha uma pré-configuração para reutilizar uma definição de alerta. 

5. Clique em  ** Salvar alerta **. 




## Configurar um alerta específico de visualização
{: #config_alert_view}

Conclua as etapas a seguir para anexar um alerta a uma visualização:

1. Clique no ícone  ** Visualizações **   ![Configuration icon](images/views.png).
2. Crie uma visualização. 

    Aplique um prazo, filtros e critérios de procura para filtrar as linhas de log que são exibidas por meio da visualização. 

    Para obter mais informações, consulte  [ Criando visualizações ](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-view_logs#view_logs_step7).

3. Clique no nome da visualização. Em seguida, selecione  ** Anexar um alerta **.

4. Escolha  ** Alerta Específico da Visualização **.

5. Escolha um canal de notificação. 

6. Defina as condições de limite.

    1. Selecione uma frequência de tempo. Por exemplo, 12 horas.

    2. Insira o número de linhas de log após as quais você deseja que o alerta seja acionado.

    3. Selecione se deseja que ambas as condições sejam verificadas ou apenas uma.

7. Inclua os detalhes para o canal de notificação que você escolheu.

    Por exemplo, para o canal de notificação por e-mail, inclua um ou mais destinatários e, opcionalmente, um fuso horário.

8. Clique em  ** Salvar alerta **.



## Excluir uma pré-configuração (modelo de alerta)
{: #delete_preset}

Conclua as etapas a seguir para excluir uma pré-configuração:

1. Selecione o ícone de **Configuração** ![Ícone de Configuração](images/admin.png "Ícone de Administrador").
2. Selecione  ** Alertas **.
3. Passe o mouse sobre o botão *editar* da pré-configuração que você deseja excluir. A opção  * delete *  é mostrada.
4. Selecione  ** Excluir **.
5. Confirme se você deseja excluir a pré-configuração. Clique em  ** Excluir **.

## Remova de uma visualização um alerta específico
{: #delete_alert}

Conclua as etapas a seguir para remover uma pré-configuração:

1. Selecione o ícone de **Configuração** ![Ícone de Configuração](images/admin.png "Ícone de Administrador").
2. Selecione  ** Alertas **.
3. Passe o mouse sobre o botão *editar* do alerta que você deseja excluir. A opção  * delete *  é mostrada.
4. Selecione  ** Desanexar **.
5. Confirme que deseja excluir o alerta. Clique em  ** Desanexar **.



## Canais de notificação
{: #channels}

A tabela a seguir lista os canais de notificação que podem ser configurados quando um alerta é acionado:

| Canal           | Detalhes da configuração | 
|-------------------|-----------------------|
| `email`             | É possível configurar um ou mais endereços de e-mail.  | 
| `Slack`             | É possível configurar um canal do Slack. |
| `Webhook`           | É possível configurar uma URL de gancho da web. |
| `PagerDuty`         | É possível configurar detalhes de conexão para o sistema PagerDuty e selecionar um serviço.|
| `OpsGenie`          | É possível configurar a chave de API para se conectar ao sistema OpsGenie. |
| `Datadog`           | É possível configurar a chave de API para se conectar ao sistema `Datadog`. |
| `AppOptics/Librato` | É possível configurar a chave de API para se conectar ao sistema AppOptics/Librato. |
| `VictorOps`         | É possível configurar a URL para que ela notifique quando um alerta é acionado, a chave de roteamento e um tipo de alerta. Os tipos de alerta válidos são: `info`, `warning` e `critical` |
{: caption="Canais de notificação" caption-side="top"} 


