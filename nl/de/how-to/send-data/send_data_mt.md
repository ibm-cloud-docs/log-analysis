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

# Lokale Daten an einen Bereich in IBM Cloud senden
{: #send_data_mt}

Zum Senden von Protokolldaten an den {{site.data.keyword.loganalysisshort}}-Service können Sie einen Multi-Tenant Logstash Forwarder (mt-logstash-forwarder) konfigurieren. 
{: shortdesc}

Führen Sie die folgenden Schritte aus, um Protokolldaten an einen Bereich in {{site.data.keyword.Bluemix_notm}} zu senden:

## Voraussetzungen
{: #prereqs1}

* Eine {{site.data.keyword.Bluemix_notm}} ID für die Anmeldung bei {{site.data.keyword.Bluemix_notm}}.
* Eine Benutzer-ID, die über Berechtigungen zum Arbeiten in einem Bereich mit dem {{site.data.keyword.loganalysisshort}}-Service verfügt. Weitere Informationen finden Sie unter [Sicherheit](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-security_ov#security_ov).
* Die in Ihrer lokalen Umgebung installierte {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle.
* Der {{site.data.keyword.loganalysisshort}}-Service, der in einem Bereich in Ihrem Konto mit einem Plan bereitgestellt wird, der die Protokollaufnahme ermöglicht.


## Schritt 1: Protokollierungstoken anfordern
{: #get_logging_auth_token}

Führen Sie in der Terminalsitzung, in der die {{site.data.keyword.loganalysisshort}}-Befehlszeilenschnittstelle installiert ist, die folgenden Schritte aus:

1. Melden Sie sich bei einer Region, Organisation und bei einem Bereich in {{site.data.keyword.Bluemix_notm}} an. 

    Weitere Informationen finden Sie in [Wie melde ich mich bei {{site.data.keyword.Bluemix_notm}} an?](/docs/services/CloudLogAnalysis/qa?topic=cloudloganalysis-cli_qa#login).
    
2. Führen Sie den Befehl `ibmcloud logging token-get` aus. 

    ```
    ibmcloud logging token-get
    ```
    {: codeblock}

    Der Befehl gibt das Protokollierungstoken zurück.
    
    Beispiel:

    ```
    ibmcloud logging token-get
    Getting log token of resource: 93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf ...
    OK

    Tenant Id                              Logging Token   
    93f54jh6-b5f5-46c9-9f0e-kfeutpldnbcf   oT98_abcdefz   
    ```
    {: screen}

    Dabei ist *Tenant Id* die GUID des Bereichs, zu dem Protokolle gesendet werden.


## Schritt 2: Multi-Tenant Logstash Forwarder konfigurieren
{: #configure_mt_logstash_forwarder}

Führen Sie die folgenden Schritte aus, um den Multi-Tenant Logstash Forwarder (mt-logstash-forwarder) in der Umgebung zu konfigurieren, von der aus Sie Protokolle an den {{site.data.keyword.loganalysisshort}}-Service senden wollen:

1.	Melden Sie sich als Rootbenutzer an. 

    ```
    sudo -s
    ```
    {: codeblock}
    
2.	Installieren Sie das NTP-Paket (NTP = Network Time Protocol), um die Protokolle zeitlich zu synchronisieren. 

    Beispiel: Prüfen Sie für ein Ubuntu-System, ob für `timedatectl status` Folgendes angezeigt wird: *Network time on: yes*. Ist dies der Fall, ist Ihr Ubuntu-System bereits so konfiguriert, dass 'ntp' verwendet wird, und Sie können diesen Schritt überspringen.
    
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
    
    Führen Sie die folgenden Schritte aus, um 'ntp' in einem Ubuntu-System zu installieren:

    1.	Führen Sie den folgenden Befehl aus, um die Pakete zu aktualisieren. 

        ```
        apt-get update
        ```
        {: codeblock}
        
    2.	Führen Sie den folgenden Befehl aus, um das ntp-Paket zu installieren. 

        ```
        apt-get install ntp
        ```
        {: codeblock}
        
    3.	Führen Sie den folgenden Befehl aus, um das ntpdate-Paket zu installieren. 
    
        ```
        apt-get install ntpdate
        ```
        {: codeblock}
        
    4.	Führen Sie den folgenden Befehl aus, um den Service zu stoppen. 
        
        ```
        service ntp stop
        ```
        {: codeblock}
        
    5.	Führen Sie den folgenden Befehl aus, um die Systemuhr zu synchronisieren. 
    
        ```
        ntpdate -u 0.ubuntu.pool.ntp.org
        ```
        {: codeblock}
        
        Das Ergebnis bestätigt, dass die Zeit angepasst wurde. Beispiel:
        
        ```
        4 May 19:02:17 ntpdate[5732]: adjust time server 50.116.55.65 offset 0.000685 sec
        ```
        {: screen}
        
    6.	Führen Sie den folgenden Befehl aus, um 'ntpd' erneut zu starten. 
    
        ```
        service ntp start
        ```
        {: codeblock}
    
        Das Ergebnis bestätigt, dass der Service gestartet wird.

    7.	Führen Sie den folgenden Befehl aus, um den ntpd-Service für den automatischen Start nach einem Ausfall oder Neustart zu aktivieren. 
    
        ```
        service ntp enable
        ```
        {: codeblock}
        
        Als Ergebnis wird eine Liste der Befehle angezeigt, die zur Verwaltung des ntpd-Service verwendet werden können. Beispiel:
        
        ```
        Usage: /etc/init.d/ntpd {start|stop|status|restart|try-restart|force-reload}
        ```
        {: screen}

3. Fügen Sie das Repository für den {{site.data.keyword.loganalysisshort}}-Service im Paketmanager des Systems hinzu. Führen Sie den folgenden Befehl aus:

    ```
    wget -O - https://downloads.opvis.bluemix.net/client/IBM_Logmet_repo_install.sh | bash
    ```
    {: codeblock}

4. Installieren und konfigurieren Sie den Multi-Tenant Logstash Forwarder (mt-logstash-forwarder), um Protokolle aus Ihrer Umgebung an die 'Log Collection' zu senden. 

    1. Führen Sie den folgenden Befehl aus, um den Multi-Tenant Logstash Forwarder (mt-logstash-forwarder) zu installieren:
    
        ```
        apt-get install mt-logstash-forwarder 
        ```
        {: codeblock}
        
    2. Erstellen Sie die mt-logstash-forwarder-Konfigurationsdatei für Ihre Umgebung. Diese Datei enthält Variablen, die verwendet werden, um Logstash Forwarder so zu konfigurieren, dass der Forwarder an den {{site.data.keyword.loganalysisshort}}-Service verwiesen wird.
    
       Bearbeiten Sie die Datei `/etc/mt-logstash-forwarder/mt-lsf-config.sh`. Sie können zum Beispiel den Editor vi verwenden:
               
       ```
       vi /etc/mt-logstash-forwarder/mt-lsf-config.sh
       ```
       {: codeblock}
        
       Um den Forwarder an den {{site.data.keyword.loganalysisshort}}-Service zu verweisen, fügen Sie die folgenden Variablen in die Datei **mt-lsf-config.sh** ein: 
         
       <table>
          <caption>Tabelle 1. Liste der Variablen, die erforderlich sind, um den Forwarder in einer VM an den {{site.data.keyword.loganalysisshort}}-Service zu verweisen </caption>
          <tr>
            <th>Variablenname</th>
            <th>Beschreibung</th>
          </tr>
          <tr>
            <td>LSF_INSTANCE_ID</td>
            <td>ID für Ihre VM. Beispiel: *MyTestVM*. </td>
          </tr>
          <tr>
            <td>LSF_TARGET</td>
            <td>Ziel-URL. Informationen zum Abrufen der Liste der URLs zum Einpflegen finden Sie unter [URLs für das Einpflegen](/docs/services/CloudLogAnalysis?topic=cloudloganalysis-log_ingestion#log_ingestion_urls). Legen Sie den Wert beispielsweise auf **ingest.logging.ng.bluemix.net:9091** fest, um Protokolle an die Region 'USA (Süden)' zu senden. </td>
          </tr>
          <tr>
            <td>LSF_TENANT_ID</td>
            <td>ID des Bereichs, für den der {{site.data.keyword.loganalysisshort}}-Service zur Erfassung der Protokolle bereit ist, die Sie an {{site.data.keyword.Bluemix_notm}} senden. <br>Verwenden Sie den Wert, den Sie in Schritt 1 erhalten haben.</td>
          </tr>
          <tr>
            <td>LSF_PASSWORD</td>
            <td>Protokollierungstoken. <br>Verwenden Sie den Wert, den Sie in Schritt 1 erhalten haben.</td>
          </tr>
          <tr>
            <td>LSF_GROUP_ID</td>
            <td>Geben Sie für diesen Wert einen angepassten Tag an, den Sie zum Gruppieren zusammengehöriger Protokolle definieren können.</td>
          </tr>
       </table>
        
       Beispiel: Suchen Sie in der folgenden Beispieldatei nach einem Bereich mit der ID *7d576e3b-170b-4fc2-a6c6-b7166fd57912* in der Region 'Vereinigtes Königreich':
        
       ```
       # more mt-lsf-config.sh 
       LSF_INSTANCE_ID="myhelloapp"
       LSF_TARGET="ingest.logging.ng.bluemix.net:9091"
       LSF_TENANT_ID="7d576e3b-170b-4fc2-a6c6-b7166fd57912"
       LSF_PASSWORD="oT98_abcdefz"
       LSF_GROUP_ID="Group1"
       ```
       {: screen}
        
    3. Starten Sie den Multi-Tenant Logstash Forwarder (mt-logstash-forwarder). 
    
       ```
       service mt-logstash-forwarder start
       ```
       {: codeblock}
                
Standardmäßig beobachtet der Forwarder nur das Syslog. Ihre Protokolle stehen in Kibana für die Analyse zur Verfügung.
        

## Schritt 3: Weitere Protokolldateien angeben
{: #add_logs}

Standardmäßig wird nur die Datei /var/log/syslog vom Forwarder überwacht. Sie können weitere Konfigurationsdateien zum Verzeichnis `/etc/mt-logstash-forwarder/conf.d/syslog.conf/` hinzufügen, damit der Forwarder auch diese überwachen kann. 

Führen Sie die folgenden Schritte aus, um eine Konfigurationsdatei für eine App hinzuzufügen, die in Ihrer Umgebung ausgeführt wird:

1.	Kopieren Sie die Datei `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    **Tipp:** Bearbeiten Sie die Datei syslog.conf nicht, um Protokolldateien hinzuzufügen.
    
    Beispiel: Führen Sie den folgenden Befehl in einem Ubuntu-System aus:
    
    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
        
2.	Bearbeiten Sie die Datei *myapp.conf* mit einem Texteditor und aktualisieren Sie die Datei, indem Sie die Anwendungsprotokolle einfügen, die Sie überwachen wollen. Geben Sie für jedes App-Protokoll den Protokolltyp an. Löschen Sie alle Beispiele, die nicht verwendet werden.

3.	Starten Sie den Multi-Tenant Logstash Forwarder (mt-logstash-forwarder) erneut. 

     Starten Sie den Service 'mt-logstash-forwarder' erneut. Führen Sie den folgenden Befehl aus:
    
    ```
    service mt-logstash-forwarder restart
    ```
    {: codeblock}

**Beispiel**

Wenn Sie Standardausgabe (stdout) oder Standardfehler (stderr) aus einer Hello-App einbeziehen möchten, leiten Sie 'stdout' oder 'stderr' in eine Protokolldatei um. Erstellen Sie eine Forwarder-Konfigurationsdatei für die App. Starten Sie 'mt-logstash-forwarder' anschließend neu.

1.	Kopieren Sie die Datei `/etc/mt-logstash-forwarder/conf.d/syslog.conf`. 

    ```
    cp /etc/mt-logstash-forwarder/conf.d/syslog.conf /etc/mt-logstash-forwarder/conf.d/myapp.conf
    ```
    {: codeblock}
    
2. Bearbeiten Sie die Konfigurationsdatei *myapp.conf*.

    Um beim Einpflegen eines Protokolls eine Suche anhand eines JSON-Feldes in Kibana durchführen zu können, aktivieren Sie das JSON-Parsing. Legen Sie `is_json` in der Konfigurationsdatei für bestimmte Dateipfade auf 'true' fest. Für Protokolldateien, die auf diese Weise konfiguriert werden, sollten die Protokollzeilen als mit Rücklauf voneinander getrennte JSON-Blöcke formatiert werden. Der Multi-Tenant Logstash Forwarder (mt-logstash-forwarder) verarbeitet alle diese JSON-Felder dann als einzelne, mit Kibana durchsuchbare Felder. JSON-Feldnamen enthalten ein Suffix, das auf dem entsprechenden Typ basiert.
    
    ```
    {
    "files": [
         # weitere Dateikonfigurationen ausgelassen...
            {
            "paths": [ "/var/log/myhelloapp.log" ],
            "fields": { "type": "helloapplog" },
            "is_json": true
            }
         ]
     }
     ```
     {: screen}
