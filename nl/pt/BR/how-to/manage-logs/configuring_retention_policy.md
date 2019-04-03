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

# Configurando a política de retenção de log
{: #configuring_retention_policy1}

Use o comando **cf logging option** para visualizar e configurar a política de retenção que define o número máximo de dias que os logs são mantidos na Coleção de logs. Por padrão, a política de retenção é desativada e os logs são mantidos indefinidamente. Após a expiração do período de retenção, os logs são excluídos automaticamente. 
{:shortdesc}

É possível ter políticas de retenção diferentes definidas na conta. É possível ter uma política de conta global e políticas de espaço individuais. A política de retenção configurada no nível de conta define o número máximo de dias durante os quais é possível manter os logs. Se você configurar uma política de retenção de espaço para um período de tempo superior ao período de nível de conta, a política aplicada será a última política configurada para esse espaço. 


## Desativando a política de retenção de log de um espaço
{: #disable_retention_policy_space1}

Conclua as etapas a seguir para desativar uma política de retenção:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Configure o período de retenção como **-1** para desativar o período de retenção. Execute o comando:

    ```
    ibmcloud cf logging option -r -1
    ```
    {: codeblock}
    
**Exemplo**
    
Por exemplo, para desativar o período de retenção de um espaço com o ID *d35da1e3-b345-475f-8502-cfgh436902a3*, execute o comando a seguir:

```
ibmcloud cf logging option -r -1
```
{: codeblock}

A saída é:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        -1 |
+--------------------------------------+-----------+
```
{: screen} 



## Verificando a política de retenção de log de um espaço
{: #check_retention_policy_space1}

Para obter o período de retenção que é configurado para um espaço, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Sai o período de retenção. Execute o comando:

    ```
    ibmcloud cf logging option
    ```
    {: codeblock}

    A saída é:

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## Verificando a política de retenção de log de todos os espaços em uma conta
{: #check_retention_policy_account}

Para obter o período de retenção que é configurado para cada espaço em uma conta, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Obtenha o período de retenção de cada espaço na conta. Execute o comando:

    ```
    ibmcloud cf logging option -a
    ```
    {: codeblock}

    A saída é:

    ```
    +--------------------------------------+-----------+
    |               SPACEID                | RETENTION |
    +--------------------------------------+-----------+
    | d35da1e3-b345-475f-8502-cfgh436902a3 |        30 |
    +--------------------------------------+-----------+
    | fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
    +--------------------------------------+-----------+
    ```
    {: screen}
    

## Configurando uma política de retenção de log no nível de conta
{: #set_retention_policy_space1}

Para ver o período de retenção para uma conta, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Configure o período de retenção. Execute o comando:

    ```
    ibmcloud cf logging option -r *Number_of_days* - a
    ```
    {: codeblock}
    
    em que *Number_of_days* é um número inteiro que define o número de dias que você deseja manter os logs. 
    
    
**Exemplo**
    
Por exemplo, para manter qualquer tipo de log em sua conta por 15 dias apenas, execute o comando a seguir:

```
ibmcloud cf logging option -r 15 -a
```
{: codeblock}

A saída lista uma entrada de cada espaço na conta, incluindo informações sobre o período de retenção:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |        15 |
+--------------------------------------+-----------+
| fdew45e3-b345-4365-8502-cfghrfthy5a3 |        30 |
+--------------------------------------+-----------+
```
{: screen}

## Configurando a política de retenção de log de um espaço
{: #set_retention_policy_account}

Para ver o período de retenção para um espaço, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Configure o período de retenção. Execute o comando:

    ```
    ibmcloud cf logging option -r *Number_of_days*
    ```
    {: codeblock}
    
    em que *Number_of_days* é um número inteiro que define o número de dias que você deseja manter os logs.
    
    
**Exemplo**
    
Por exemplo, para manter os logs disponíveis em um espaço por um ano, execute o comando a seguir:

```
ibmcloud cf logging option -r 365
```
{: codeblock}

A saída é:

```
+--------------------------------------+-----------+
|               SPACEID                | RETENTION |
+--------------------------------------+-----------+
| d35da1e3-b345-475f-8502-cfgh436902a3 |       365 |
+--------------------------------------+-----------+
```
{: screen}


