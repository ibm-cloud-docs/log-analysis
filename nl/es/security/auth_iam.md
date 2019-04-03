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


# Obtención de la señal de IAM
{: #auth_iam1}

Para gestionar los registros disponibles en el dominio de la cuenta mediante la API de {{site.data.keyword.loganalysisshort}}, debe utilizar una señal de autenticación. Utilice la CLI de {{site.data.keyword.cloud_notm}} para obtener la señal de IAM. La señal tiene un tiempo de caducidad. 
{:shortdesc}


## Obtención de la señal de IAM
{: #iam_token_cli}

Para obtener la señal de autorización mediante la CLI de {{site.data.keyword.cloud_notm}}, siga los pasos siguientes desde el terminal:

1. Instale la CLI de {{site.data.keyword.cloud_notm}}.

   Para obtener más información, consulte [Descargar e instalar la CLI de {{site.data.keyword.Bluemix}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Si la CLI está instalada, continúe en el paso siguiente.
    
2. Inicie una sesión en una región de {{site.data.keyword.cloud_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.cloud_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Ejecute el mandato `ibmcloud iam oauth-tokens` para obtener la señal de IAM.

    ```
	ibmcloud iam oauth-tokens
	```
	{: codeblock}
	
	La salida devuelve la señal de IAM que debe utilizar para autenticas su ID de usuario en dicho espacio y organización. Puede exportar la señal de IAM a una variable de shell como por ejemplo `$iam_token`.



**Nota:** Cuando utilice la señal, elimine *Bearer* del valor de la señal que pasa en una llamada de API.

