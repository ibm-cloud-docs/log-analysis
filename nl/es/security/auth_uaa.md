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


# Obtención de la señal de UAA
{: #auth_uaa}

Para gestionar los registros disponible mediante la API de {{site.data.keyword.loganalysisshort}}, debe utilizar una señal de autenticación.
{:shortdesc}

		
## Obtención de la señal de UAA
{: #uaa_cli}


Para obtener la señal de autorización, siga estos pasos:

1. Instale la CLI de {{site.data.keyword.Bluemix_notm}}.

   Para obtener más información, consulte [Descargar e instalar la CLI de {{site.data.keyword.Bluemix}}](/docs/cli?topic=cloud-cli-ibmcloud-cli#overview).
   
   Si la CLI está instalada, continúe en el paso siguiente.
    
2. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
	
3. Ejecute el mandato `ibmcloud iam oauth-token` para obtener la señal de UAA de {{site.data.keyword.Bluemix_notm}}.

    ```
	ibmcloud iam oauth-token
	```
	{: codeblock}
	
	La salida devuelve la señal de UAA que debe utilizar para autenticas su ID de usuario en dicho espacio y organización.
	

**Nota:** Cuando utilice la señal, elimine *Bearer* del valor de la señal que pasa en una llamada de API.
