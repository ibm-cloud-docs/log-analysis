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

# Envío de datos locales a un espacio de IBM Cloud
{: #send_data_mt}

Para enviar datos de registro al servicio {{site.data.keyword.loganalysisshort}}, puede configurar un reenviador de Logstash multiarrendatario (mt-logstash-forwarder). 
{: shortdesc}

Siga los pasos siguientes para enviar datos de registro a un espacio de {{site.data.keyword.Bluemix_notm}}:

## Requisitos previos
{: #prereqs1}

* Un ID de {{site.data.keyword.Bluemix_notm}} para iniciar una sesión en {{site.data.keyword.Bluemix_notm}}.
* Un ID de usuario que tenga permisos para trabajar en un espacio con el servicio {{site.data.keyword.loganalysisshort}}. Para obtener más información, consulte [Seguridad](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#security_ov).
* La CLI de {{site.data.keyword.loganalysisshort}} instalada en el entorno local.
* El servicio {{site.data.keyword.loganalysisshort}} suministrado en un espacio de la cuenta con un plan que permita la ingestión de registros.


## Paso 1: Obtenga la señal de registro
{: #get_logging_auth_token}

Siga los pasos siguientes desde una sesión de terminal donde esté instalada la CLI de {{site.data.keyword.loganalysisshort}}:

1. Inicie la sesión en una región, organización y espacio en {{site.data.keyword.Bluemix_notm}}. 

    Para obtener más información, consulte [Cómo iniciar la sesión en {{site.data.keyword.Bluemix_notm}}](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Ejecute el mandato `ibmcloud logging token-get`. 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    El mandato devuelve la señal de registro.
    
    Por ejemplo,

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    donde *Tenant Id* es el GUID del espacio al que va a enviar los registros.


## Paso 2: Configure mt-logstash-forwarder
{: #configure_mt_logstash_forwarder}

Siga los pasos siguientes para configurar mt-logstash-forwarder en el entorno en el que tiene intención de enviar registros en el servicio {{site.data.keyword.loganalysisshort}}:

1.	Inicie sesión como usuario root. 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	Instale el paquete Network Time Protocol (NTP) para sincronizar la hora de los registros. 

    Por ejemplo, para un sistema Ubuntu, compruebe si `timedatectl status` muestra *Network time on: yes*. Si es así, significa que el sistema Ubuntu ya está configurado para utilizar ntp y puede saltarse este paso.
    
    ```
    # timedatectl status
    Local time: Mon 2017-06-12 03:01:22 PDT
    Universal time: Mon 2017-06-12 10:01:22 UTC
    RTC time: Mon 2017-06-12 10:01:22
    Time zone: America/Los_Angeles (PDT, -0700)
    Network time on: yes
    NTP synchronized: yes
    RTC in local TZ: no
    ```
    {: screen}
    
    Siga los siguientes pasos para instalar ntp en un sistema Ubuntu:

    1.	Ejecute el siguiente mandato para actualizar los paquetes. 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	Ejecute el siguiente mandato para instalar el paquete ntp. 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	Ejecute el siguiente mandato para instalar el paquete ntpdate. 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	Ejecute el siguiente mandato para detener el servicio 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	Ejecute el siguiente mandato para sincronizar el reloj del sistema. 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        El resultado confirma que se ha ajustado la hora, por ejemplo:
        
        ```
        4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	Ejecute el siguiente mandato para volver a iniciar ntpd. 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        El resultado confirma que el servicio se está iniciando.

    7.	Ejecute el siguiente mandato para habilitar el servicio ntpd para iniciarse automáticamente después de un bloqueo o rearranque. 
    
        ```
        service ntp enable
        ```
        {: codeblock}
        
        El resultado que se visualiza es una lista de mandatos que puede utilizarse para gestionar el servicio ntpd, por ejemplo:
        
        ```
        Uso: /etc/init.d/ntpd {start|stop|status|restart|try-restart|force-reload}
        ```
        {: screen}

3. Añada el repositorio correspondiente al servicio {{site.data.keyword.loganalysisshort}} al gestor de paquetes del sistema. Ejecute el mandato siguiente:

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. Instale y configura mt-logstash-forwarder para que envíe registros del entorno al componente de recopilación de registros. 

    1. Ejecute el siguiente mandato para instalar mt-logstash-forwarder:
    
        ```
        apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. Cree el archivo de configuración de mt-logstash-forwarder para su entorno. Este archivo incluye variables que se utilizan para configurar el reenviador de mt logstash de modo que apunte al servicio {{site.data.keyword.loganalysisshort}}.
    
       Edite el archivo `/etc/mt-logstash-forwarder/mt-lsf-config.sh`. Por ejemplo, puede utilizar el editor vi:
               
       ```
       vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       Para que el reenviador apunte al servicio {{site.data.keyword.loganalysisshort}}, añada las siguientes variables al archivo **mt-lsf-config.sh**: 
         
       <table>
          <caption>Tabla 1. Lista de las variables necesarias para que el reenviador de una VM apunte al servicio {{site.data.keyword.loganalysisshort}} </caption>
          <tr>
            <th>Nombre de variable</th>
            <th>Descripción</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>ID de VM, por ejemplo, *MyTestVM*. </td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>URL de destino. Para obtener la lista de los URL de ingestión, consulte [URL de ingestión](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls). Por ejemplo, establezca el valor en **ingest.logging.ng.bluemix.net:9091** para enviar los registros a la región EE.UU. sur. </td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>ID del espacio en el que el servicio {{site.data.keyword.loganalysisshort}} está listo para recopilar los registros que el usuario envía a {{site.data.keyword.Bluemix_notm}}. <br>Utilice el valor obtenido en el paso 1.</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>Señal de registro. <br>Utilice el valor obtenido en el paso 1.</td>
          </tr>
          <tr>
            <td>LSF_GROUP_ID</td>
            <td>Establezca este valor en una etiqueta personalizada que puede definir para agrupar los registros relacionados.</td>
          </tr>
       </table>
        
       Por ejemplo, observe el siguiente archivo de ejemplo correspondiente a un espacio con el ID *7d576e3b-170b-4fc2-a6c6-b7166fd57912* en la región Reino Unido:
        
       ```
       # more mt-lsf-config.sh
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. Inicie mt-logstash-forwarder. 
    
       ```
       service mt-logstash-forwarder start
       ```
       {: codeblock}
                
De forma predeterminada, el reenviador solo consulta syslog. Los registros están disponibles en Kibana para que se analicen.
        

## Paso 3: Especifique más archivos de registro
{: #add_logs}

De forma predeterminada, el reenviador solo supervisa el archivo /var/log/syslog. Puede añadir más archivos de configuración al siguiente directorio `/etc/mt-logstash-forwarder/conf.d/syslog.conf/` para que el reenviador también los supervise. 

Siga los pasos siguientes para añadir un archivo de configuración correspondiente a una app que se ejecuta en su entorno:

1.	Copie el archivo `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    **Consejo:** No edite el archivo syslog.conf para añadir archivos de registro.
    
    Por ejemplo, en un sistema Ubuntu, ejecute el siguiente mandato:
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	Con un editor de texto, edite el archivo *myapp.conf* y actualice el archivo para incluir los registros de aplicación que desea supervisar. Incluya el tipo de registro para cada registro de app. Suprima los ejemplos que no se utilicen.

3.	Reinicie mt-logstash-forwarder. 

     Reinicie servicio mt-logstash-forwarder. Ejecute el mandato siguiente:
    
    ```
    service mt-logstash-forwarder restart
    ```
    {: codeblock}

**Ejemplo**

Para incluir stdout o stderr de una app hello, redirija stdout o stderr a un archivo de registro. Cree un archivo de configuración del reenviador para la app. A continuación, reinicie mt-logstash-forwarder.

1.	Copie el archivo `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. Edite el archivo de configuración *myapp.conf*.

    Para poder buscar por un campo JSON en Kibana cuando ingiere un registro, habilite el análisis de JSON. Establezca `is_json` en true en el archivo de configuración para las vías de acceso a un archivo específico. Para archivos de registro que se han configurado de esta manera, las líneas del registro deben estar formateadas como bloques de JSON, separados por retornos de carro. El mt-logstash-forwarder consumirá todos estos campos JSON como campos individuales en los que se pueden realizar búsquedas de Kibana. Los nombres del campo JSON incluyen un sufijo que se basa en tipo.
    
    ```
    {
    "files": [
         # other file configurations omitted...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
