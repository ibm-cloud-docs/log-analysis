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
{: #configuring_retention_policy}

Por padrão, a política de retenção é desativada e os logs são mantidos indefinidamente. Use o comando **ibmcloud logging option-update** para mudar a política de retenção.
{:shortdesc}

É possível usar o comando **ibmcloud logging option-show** para visualizar a política de retenção que define o número máximo de dias pelos quais os logs são mantidos na Coleção de logs. 

Ao configurar uma política de retenção, após a expiração do período de retenção, os logs são excluídos automaticamente.


## Desativando a política de retenção de log para uma conta
{: #disable_retention_policy_acc}

Quando você desativa a política de retenção, todos os logs são mantidos. 

Conclua as etapas a seguir para desativar uma política de retenção:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
2. Obtenha o ID da conta.

    Para obter mais informações, veja [Como obter o GUID de uma conta](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Configure o período de retenção como **-1** para desativar o período de retenção. Execute o comando:

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
	```
    {: codeblock}
	
	O RETENTION_VALUE é um numérico que define o número de dias.
    
**Exemplo**
    
Por exemplo, para desativar o período de retenção de uma conta com ID *12345677fgh436902a3*, execute o comando a seguir:

```
ibmcloud logging option-update -r account -i 12345677fgh436902a3 -e -1
```
{: codeblock}


## Desativando a política de retenção de log de um espaço
{: #disable_retention_policy_space}

Quando você desativa a política de retenção, todos os logs são mantidos.  

Conclua as etapas a seguir para desativar uma política de retenção:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Configure o período de retenção como **-1** para desativar o período de retenção. Execute o comando:

    ```
    ibmcloud logging option-show -e RETENTION_VALUE
	```
    {: codeblock}
	
	O RETENTION_VALUE é um numérico que define o número de dias.
    
**Exemplo**
    
Por exemplo, para desativar o período de retenção de um espaço com o ID *d35da1e3-b345-475f-8502-cfgh436902a3*, execute o comando a seguir:

```
Opção de criação de log ibmcloud-update -e -1
```
{: codeblock}


## Verificando a política de retenção de log de uma conta
{: #check_retention_policy_acc}

Para obter o período de retenção configurado para uma conta, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

2. Obtenha o ID da conta.

    Para obter mais informações, veja [Como obter o GUID de uma conta](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Obtenha o período de retenção. Execute o comando:

    ```
    ibmcloud logging option-show -r account -i AccountID
    ```
    {: codeblock}

    A saída é:

    ```
    ibmcloud logging option-show -r account -i kjskdsjfksjdflkjdsfbbd06461b066
    Showing log options of resource: kjskdsjfksjdflkjdsfbbd06461b066 ...

    Resource ID                              Retention   
    a:kjskdsjfksjdflkjdsfbbd06461b066       30   
	```
    {: screen}
	
## Verificando a política de retenção de log de um espaço
{: #check_retention_policy_space}

Para obter o período de retenção que é configurado para um espaço, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Obtenha o período de retenção. Execute o comando:

    ```
    ibmcloud logging option-show
    ```
    {: codeblock}

    A saída é:

    ```
    ibmcloud logging option-show
    Showing log options of resource: 12345678-1234-2edr-a9de-378620d6fab5 ...

    SpaceId                                Retention   
    12345678-1234-2edr-a9de-378620d6fab5   30   
	```
    {: screen}
    


## Configurando uma política de retenção de log no nível de conta
{: #set_retention_policy_acc}

Conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).

2. Obtenha o ID da conta.

    Para obter mais informações, veja [Como obter o GUID de uma conta](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#account_guid).
    
3. Configure o período de retenção. Execute o comando:

    ```
    ibmcloud logging option-update -r account -i AccountID -e RETENTION_VALUE
    ```
    {: codeblock}
    
    em que *RETENTION_VALUE* é um número inteiro que define o número de dias que você deseja manter os logs. 
    
    
**Exemplo**
    
Por exemplo, para manter qualquer tipo de log em sua conta por 15 dias apenas, execute o comando a seguir:

```
ibmcloud logging option-update -r account -i AccountID -e 15
```
{: codeblock}



## Configurando a política de retenção de log de um espaço
{: #set_retention_policy_space}

Para ver o período de retenção para um espaço, conclua as etapas a seguir:

1. Efetue login em uma região, uma organização e um espaço no {{site.data.keyword.Bluemix_notm}}. 

    Para obter mais informações, veja [Como efetuar login no {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Configure o período de retenção. Execute o comando:

    ```
    Opção de criação de log ibmcloud-update -e RETENTION_VALUE
    ```
    {: codeblock}
    
    em que *RETENTION_VALUE* é um número inteiro que define o número de dias que você deseja manter os logs.
    
    
**Exemplo**
    
Por exemplo, para manter os logs disponíveis em um espaço por um ano, execute o comando a seguir:

```
Opção de criação de log ibmcloud-update -e 365
```
{: codeblock}




