---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-07"

keywords: LogDNA, IBM, Log Analysis, logging, network, IP addresses, port

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

 
# Gestión del tráfico de red
{: #network}

Cuando tiene configurado un cortafuegos adicional, o ha personalizado los valores del cortafuegos en la infraestructura de {{site.data.keyword.cloud_notm}}, debe permitir el tráfico de red de salida en el servicio {{site.data.keyword.la_full_notm}}. 
{:shortdesc}


## Tráfico de red para configuraciones de cortafuegos personalizadas en la región EE. UU. sur
{: #ips_us-south}

Debe permitir el tráfico de salida en el puerto TCP 443 y el puerto TCP 80 en el cortafuegos. Por ejemplo, debe abrir el puerto TCP 443 y el puerto TCP 80 de cada trabajador en el servicio {{site.data.keyword.la_full_notm}}.

**Nota:** el punto final de API es necesario para la autenticación del agente LogDNA. El agente LogDNA obtiene una señal que puede utilizar para enviar registros al punto final de ingestión.

En las tablas siguientes se muestran las direcciones IP por región que debe configurar en el cortafuegos para permitir el tráfico de salida:

| Región      | Punto final de ingestión                          | Direcciones IP públicas               | Puertos   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EE. UU. sur`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="Tabla 1. Direcciones IP para enviar registros" caption-side="top"}


| Región      | Punto final de autenticación                     | Direcciones IP públicas               | Puertos   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EE. UU. sur`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="Tabla 2. Direcciones IP utilizadas por el agente LogDNA" caption-side="top"}



## Tráfico de red para configuraciones de cortafuegos personalizadas en la región UE DE
{: #ips_eu-de}

Debe permitir el tráfico de salida en el puerto TCP 443 y el puerto TCP 80 en el cortafuegos. Por ejemplo, debe abrir el puerto TCP 443 y el puerto TCP 80 de cada trabajador en el servicio {{site.data.keyword.la_full_notm}}.

**Nota:** el punto final de API es necesario para la autenticación del agente LogDNA. El agente LogDNA obtiene una señal que puede utilizar para enviar registros al punto final de ingestión.

En las tablas siguientes se muestran las direcciones IP por región que debe configurar en el cortafuegos para permitir el tráfico de salida:

| Región      | Punto final de ingestión                          | Direcciones IP públicas               | Puertos   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `UE DE`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="Tabla 3. Direcciones IP para enviar registros" caption-side="top"}


| Región      | Punto final de autenticación                     | Direcciones IP públicas               | Puertos   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `UE DE`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="Tabla 4. Direcciones IP utilizadas por el agente LogDNA" caption-side="top"}


