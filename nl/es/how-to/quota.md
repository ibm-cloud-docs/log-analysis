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


# Cálculo de la cuota de búsqueda y del uso diario
{: #quota}

Para obtener la cuota y el uso diario actual de un dominio de registros del servicio {{site.data.keyword.loganalysisshort}}, puede ejecutar un mandato cURL. 
{:shortdesc}

## Cálculo de la cuota de búsqueda y del uso diario mediante la CLI
{: #quota_cli}

Siga estos pasos:

1. Inicie sesión en {{site.data.keyword.Bluemix_notm}}.

    Por ejemplo, para iniciar sesión en la región EE.UU. sur, ejecute este mandato:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Ejecute el mandato de la cli `ibmcloud logging quota-usage-show`. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID]
    ```
    {: codeblock}

    donde 

    * Los valores válidos para RESOURCE_TYPE son los siguientes: space, account
    * RESOURCE_ID es el GUID de la cuenta o del espacio cuya cuota de uso desea obtener.


Por ejemplo, para mostrar el uso de la cuota de una cuenta, ejecute el mandato siguiente:

```
 ibmcloud logging quota-usage-show -r account -i 475693845023932019c6567c9c8de6dece
Showing quota usage for resource: 475693845023932019c6567c9c8de6dece ...
OK

Daily Allotmant   Current Usage
524288000         0   
```
{: screen}

Para mostrar la cuota de uso de un espacio, ejecute el siguiente mandato:

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Daily Allotmant   Current Usage
524288000         6774014   
```
{: screen}


## Obtención del historial de cuota de búsqueda mediante la CLI
{: #quota_history_cli}


Siga estos pasos:

1. Inicie sesión en {{site.data.keyword.Bluemix_notm}}.

    Por ejemplo, para iniciar sesión en la región EE.UU. sur, ejecute este mandato:

    ```
    ibmcloud login -a api.ng.bluemix.net
    ```
    {: codeblock}

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Ejecute el mandato de la cli `ibmcloud logging quota-usage-show` con el parámetro `-s`. 

    ```
    ibmcloud logging quota-usage-show [-r,--resource-type RESOURCE_TYPE][-i,--resource-id RESOURCE_ID] [-s,--history]
    ```
    {: codeblock}

    donde 

    * Los valores válidos para RESOURCE_TYPE son los siguientes: space, account
    * RESOURCE_ID es el GUID de la cuenta o del espacio cuya cuota de uso desea obtener.

Por ejemplo,

```
ibmcloud logging quota-usage-show -r space -i js7ydf98-8682-430d-bav4-36b712341744 -s
Showing quota usage for resource: js7ydf98-8682-430d-bav4-36b712341744 ...
OK

Date         Allotmant   Usage
2018.02.28   524288000   80405926
2018.03.06   524288000   18955540
2018.03.05   524288000   47262944
2018.03.08   524288000   18311338
2018.03.01   524288000   82416831
2018.03.03   524288000   75045462
2018.03.07   524288000   17386278
2018.03.02   524288000   104316444
2018.03.04   524288000   73125223   
```
{: screen}



## Cálculo de la cuota de búsqueda y del uso diario de una cuenta mediante la API
{: #account}

Siga estos pasos:

1. Inicie sesión en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Obtenga el ID de la cuenta. Ejecute el mandato siguiente:

    ```
	ibmcloud iam accounts
	```
    {: codeblock}	

	Una lista de cuentas en las que se visualiza los GUID.
	
	Exporte el ID de la cuenta a una variable de shell. Por ejemplo:
	
	```
	export AccountID="1234567891234567812341234123412"
	```
	{: screen}

3. Obtenga la señal de UAA. 

    Para obtener más información, consulte [Obtención de la señal de UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exporte la señal de UAA a una variable de shell. No incluya `Bearer`. Por ejemplo:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Obtenga la cuota del dominio y el uso actual. Ejecute el mandato siguiente:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	donde *ENDPOINT* varía según la región. Para obtener una lista de puntos finales por región, consulte [Puntos finales de registro](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).
	
	Por ejemplo, ejecute este mandato cURL para obtener la cuota correspondiente a la cuenta de la región EE.UU. sur:
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	El resultado incluye información sobre la cuota y el uso diario.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${AccountID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}

	
## Cálculo de la cuota de búsqueda y del uso diario de un espacio mediante la API
{: #space1}

Siga estos pasos:

1. Inicie sesión en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa/cli_qa.html#login).

2. Obtenga el ID del espacio.

    Para obtener más información, consulte [Cómo se obtiene el GUID de un espacio](/docs/services/CloudLogAnalysis/qa/cli_qa.html#space_guid)
	
	Exporte el ID del espacio a una variable de shell. Por ejemplo:
	
	```
	export SpaceID="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

3. Obtenga la señal de UAA. 

    Para obtener más información, consulte [Obtención de la señal de UAA](/docs/services/CloudLogAnalysis/security/auth_uaa.html#auth_uaa).

    Exporte la señal de UAA a una variable de shell. No incluya `Bearer`. Por ejemplo:
	
	```
	export TOKEN="xxxxxxxxxxxxxxxxxxxxx"
	```
	{: screen}

4. Obtenga la cuota del dominio y el uso actual. Ejecute el mandato siguiente:

    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET ENDPOINT/quota/usage
	```
	{: codeblock}
	
	donde *ENDPOINT* varía según la región. Para obtener una lista de puntos finales por región, consulte [Puntos finales de registro](/docs/services/CloudLogAnalysis/manage_logs.html#endpoints).

    Por ejemplo, ejecute el siguiente mandato cURL para obtener la cuota y el uso de un dominio de espacio de la región EE.UU. sur:
	
    ```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
	```
	{: codeblock}
	
	El resultado incluye información sobre la cuota y el uso diario.
	
	```
    curl -k -i --header "X-Auth-Token:${TOKEN}" --header "X-Auth-Project-Id: a-${SpaceID}" -XGET https://logging.ng.bluemix.net/quota/usage
    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Wed, 29 Nov 2017 13:18:20 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 52
    Connection: keep-alive

   {
      "usage": {
        "dailyallotment": 524288000,
        "current": 2115811531
       }
    }
    ```
    {: screen}



