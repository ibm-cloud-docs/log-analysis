---

copyright:
  years:  2018, 2019
lastupdated: "2019-04-02"

keywords: LogDNA, IBM, Log Analysis, logging instance, enable, service logs

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

# {{site.data.keyword.cloud_notm}}-Serviceprotokolle konfigurieren
{: #config_svc_logs}

Es ist möglich, mehrere {{site.data.keyword.la_full_notm}}-Instanzen in einer Region zu haben. Es kann jedoch nur 1 Instanz in einer Region für den Empfang von Protokollen aus aktivierten Services in der {{site.data.keyword.cloud_notm}} konfiguriert werden.
{:shortdesc}



## Plattformserviceprotokolle über das Dashboard 'Beobachtbarkeit' konfigurieren
{: #config_svc_logs_ui}

Führen Sie die folgenden Schritte aus, um eine Instanz über das Dashboard 'Beobachtbarkeit' in {{site.data.keyword.cloud_notm}} zu konfigurieren:

1. [Melden Sie sich bei Ihrem {{site.data.keyword.cloud_notm}}-Konto an ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window}.

	Nach der Anmeldung mit Ihrer Benutzer-ID und Ihrem Kennwort wird die Benutzerschnittstelle von {{site.data.keyword.cloud_notm}} geöffnet.

2. Rufen Sie das Menüsymbol ![Menüsymbol](../../icons/icon_hamburger.svg) auf. Wählen Sie dann **Beobachtbarkeit** aus, um auf das Dashboard *Beobachtbarkeit* zuzugreifen.

3. Wählen Sie **Protokollierung** aus und klicken Sie dann auf **Plattformserviceprotokolle konfigurieren**. 

4. Wählen Sie aus, welche LogDNA-Instanz Protokolle aus den aktivierten Services der Cloudplattform empfangen soll.

5. Wählen Sie eine Region aus. 

6. Wählen Sie eine Instanz aus.

7. Klicken Sie auf **Speichern**. 

Es wird die Hauptseite für die *Beobachtbarkeit* geöffnet.

Die Instanz, die Sie für den Empfang von Serviceprotokollen auswählen, wird mit dem Flag **Plattformserviceprotokolle** angezeigt.

Weitere Informationen zu den Services, die für das Senden von Protokollen an {{site.data.keyword.la_full_notm}} aktiviert wurden, finden Sie unter [Cloud-Services](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-cloud_services).

