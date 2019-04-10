---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, IAM, security, logging, access groups

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

 
# IAM-Richtlinien und Zugriffsgruppen verwalten
{: #work_iam}

{{site.data.keyword.iamlong}} (IAM) ermöglicht Ihnen die sichere Authentifizierung von Benutzern und die einheitliche Steuerung des Zugriffs auf alle Cloudressourcen in {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

Weitere Informationen finden Sie in [Benutzerzugriff mit IAM verwalten](/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-iam#iam).


## Berechtigungen erteilen, mit denen ein Benutzer Administrator des Service im {{site.data.keyword.cloud_notm}}-Konto werden kann
{: #admin_account}

Als **Kontoeigner** oder **{{site.data.keyword.la_full_notm}}-Serviceadministrator** müssen Sie über Berechtigungen zum Ausführen der folgenden Aktionen verfügen: 

* Anderen Kontomitgliedern Zugriff für die Arbeit mit dem Service gewähren
* Serviceinstanz bereitstellen
* Serviceinstanz löschen
* Details einer Serviceinstanz anzeigen
* Service-ID erstellen

Daher muss der Benutzer über eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Plattformrolle **Administrator** verfügen, damit er einem Benutzer die Administratorrolle zur Verwaltung des Service im Konto zuweisen kann. Sie müssen diesem Benutzer Zugriff auf eine einzelne Ressource in dem Konto zuweisen. 

Führen Sie die folgenden Schritte aus, um einem Benutzer die Administratorrolle für den {{site.data.keyword.la_full_notm}}-Service im Konto zuzuweisen: 

1. Klicken Sie in der Menüleiste auf **Verwalten** &gt; **Zugriff (IAM)** und wählen Sie dann **Benutzer** aus.
2. Wählen Sie in der Zeile des Benutzers, dem Sie Zugriff gewähren wollen, das Menü **Aktionen** aus und klicken Sie dann auf **Zugriff zuweisen**.
3. Wählen Sie **Zugriff auf Ressourcen zuweisen** aus.
4. Wählen Sie **IBM Log Analysis with LogDNA** aus.
5. Wählen Sie **Alle aktuellen Regionen** aus.
6. Wählen Sie **Alle aktuellen Serviceinstanzen** aus.
7. Wählen Sie die Plattformrolle **Administrator** aus.
8. Klicken Sie auf 'Zuweisen'.


## Berechtigungen erteilen, mit denen ein Benutzer Administrator des Service in einer Ressourcengruppe werden kann
{: #admin_rg}

Als **{{site.data.keyword.la_full_notm}}-Serviceadministrator** müssen Sie über Berechtigungen zum Ausführen der folgenden Aktionen verfügen: 

* Anderen Kontomitgliedern Zugriff für die Arbeit mit dem Service gewähren
* Serviceinstanz bereitstellen
* Serviceinstanz löschen
* Details einer Serviceinstanz anzeigen
* Service-ID erstellen

Daher muss der Benutzer über eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Plattformrolle **Administrator** im Kontext einer Ressourcengruppe verfügen, damit er einem Benutzer die Administratorrolle zur Verwaltung von Instanzen in der Ressourcengruppe im Konto zuweisen kann. 

Führen Sie die folgenden Schritte aus, um einem Benutzer die Administratorrolle für den {{site.data.keyword.la_full_notm}}-Service im Kontext einer Ressourcengruppe zuzuweisen: 

1. Klicken Sie in der Menüleiste auf **Verwalten** &gt; **Zugriff (IAM)** und wählen Sie dann **Benutzer** aus.
2. Wählen Sie in der Zeile des Benutzers, dem Sie Zugriff gewähren wollen, das Menü **Aktionen** aus und klicken Sie dann auf **Zugriff zuweisen**.
3. Wählen Sie **Zugriff in einer Ressourcengruppe zuweisen** aus.
4. Wählen Sie eine Ressourcengruppe aus.
5. Wurde dem Benutzer noch keine Rolle für die ausgewählte Ressourcengruppe erteilt, wählen Sie eine Rolle für das Feld **Zugriff für eine Ressourcengruppe zuweisen** aus. 

    Je nachdem, welche Rolle Sie auswählen, kann der Benutzer die Ressourcengruppe in seinem Dashboard anzeigen, den Namen der Ressourcengruppe bearbeiten oder den Benutzerzugriff auf die Gruppe verwalten. 
    
    Sie können **Kein Zugriff** auswählen, wenn der Benutzer nur Zugriff auf den {{site.data.keyword.la_full_notm}}-Service in der Ressourcengruppe haben soll.

6. Wählen Sie **IBM Log Analysis with LogDNA** aus.
7. Wählen Sie die Plattformrolle **Administrator** aus.
8. Klicken Sie auf **Zuweisen**.


## DevOps-Benutzer Berechtigungen zur Verwaltung des Service im {{site.data.keyword.cloud_notm}}-Konto erteilen
{: #devops_account}

Als **DevOps-Benutzer** müssen Sie über Berechtigungen zum Ausführen der folgenden Aktionen verfügen: 

* Serviceinstanz bereitstellen
* Serviceinstanz löschen
* Details einer Serviceinstanz anzeigen
* Service-ID erstellen

Sie müssen daher über eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Plattformrolle **Bearbeiter** verfügen.

Führen Sie die folgenden Schritte aus, um einem Benutzer die Bearbeiterrolle für den {{site.data.keyword.la_full_notm}}-Service im Konto zuzuweisen: 

1. Klicken Sie in der Menüleiste auf **Verwalten** &gt; **Zugriff (IAM)** und wählen Sie dann **Benutzer** aus.
2. Wählen Sie in der Zeile des Benutzers, dem Sie Zugriff gewähren wollen, das Menü **Aktionen** aus und klicken Sie dann auf **Zugriff zuweisen**.
3. Wählen Sie **Zugriff auf Ressourcen zuweisen** aus.
4. Wählen Sie **IBM Log Analysis with LogDNA** aus.
5. Wählen Sie **Alle Serviceinstanzen** aus.
6. Wählen Sie die Plattformrolle **Bearbeiter** aus.
7. Klicken Sie auf 'Zuweisen'.

## DevOps-Benutzer Berechtigungen zur Verwaltung einer Instanz im {{site.data.keyword.cloud_notm}}-Konto erteilen
{: #devops_account_instance}

Führen Sie die folgenden Schritte aus, um einem Benutzer die Bearbeiterrolle für eine Instanz des {{site.data.keyword.la_full_notm}}-Service im Konto zuzuweisen: 

1. Klicken Sie in der Menüleiste auf **Verwalten** &gt; **Zugriff (IAM)** und wählen Sie dann **Benutzer** aus.
2. Wählen Sie in der Zeile des Benutzers, dem Sie Zugriff gewähren wollen, das Menü **Aktionen** aus und klicken Sie dann auf **Zugriff zuweisen**.
3. Wählen Sie **Zugriff auf Ressourcen zuweisen** aus.
4. Wählen Sie **IBM Log Analysis with LogDNA** aus.
5. Wählen Sie die Instanz aus.
6. Wählen Sie die Plattformrolle **Bearbeiter** aus.
7. Klicken Sie auf 'Zuweisen'.



## DevOps-Benutzer Berechtigungen zur Verwaltung des Service in einer Ressourcengruppe erteilen
{: #devops_rg}

Als **DevOps-Benutzer** müssen Sie über Berechtigungen zum Ausführen der folgenden Aktionen verfügen: 

* Serviceinstanz bereitstellen
* Serviceinstanz löschen
* Details einer Serviceinstanz anzeigen
* Service-ID erstellen

Sie müssen daher über eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Plattformrolle **Bearbeiter** verfügen.

Führen Sie die folgenden Schritte aus, um einem Benutzer die Bearbeiterrolle für den {{site.data.keyword.la_full_notm}}-Service im Kontext einer Ressourcengruppe zuzuweisen: 

1. Klicken Sie in der Menüleiste auf **Verwalten** &gt; **Zugriff (IAM)** und wählen Sie dann **Benutzer** aus.
2. Wählen Sie in der Zeile des Benutzers, dem Sie Zugriff gewähren wollen, das Menü **Aktionen** aus und klicken Sie dann auf **Zugriff zuweisen**.
3. Wählen Sie **Zugriff in einer Ressourcengruppe zuweisen** aus.
4. Wählen Sie eine Ressourcengruppe aus.
5. Wurde dem Benutzer noch keine Rolle für die ausgewählte Ressourcengruppe erteilt, wählen Sie eine Rolle für das Feld **Zugriff für eine Ressourcengruppe zuweisen** aus. 

    Je nachdem, welche Rolle Sie auswählen, kann der Benutzer die Ressourcengruppe in seinem Dashboard anzeigen, den Namen der Ressourcengruppe bearbeiten oder den Benutzerzugriff auf die Gruppe verwalten. 
    
    Sie können **Kein Zugriff** auswählen, wenn der Benutzer nur Zugriff auf den {{site.data.keyword.la_full_notm}}-Service in der Ressourcengruppe haben soll.

6. Wählen Sie **IBM Log Analysis with LogDNA** aus.
7. Wählen Sie die Plattformrolle **Bearbeiter** aus.
8. Klicken Sie auf **Zuweisen**.

## Berechtigungen zum Verwalten von Protokollen und zum Konfigurieren von Alerts in LogDNA erteilen
{: #admin_user_logdna}

Als **Benutzer mit Administratorberechtigung** in LogDNA müssen Sie über Berechtigungen zum Ausführen der folgenden Aktionen verfügen: 

* LogDNA-Protokollquellen hinzufügen
* Protokolle anzeigen
* Protokolle durchsuchen
* Protokolle filtern
* Alerts konfigurieren

Daher benötigen Sie die folgenden Richtlinien:

* Eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Plattformrolle **Bearbeiter**. Diese Richtlinie erteilt Berechtigungen zum Anzeigen der Serviceinstanzdetails über die Befehlszeile und im {{site.data.keyword.cloud_notm}}-Dashboard.
* Eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Servicerolle **Manager**. Diese Richtlinie erteilt Berechtigungen zum Überwachen, Filtern und Durchsuchen von Protokollen und zum Definieren von Alerts über die LogDNA-Webbenutzerschnittstelle.

**Anmerkung:** Wenn Sie als Administrator des Service einem Benutzer diese Richtlinien zuweisen, sollten Sie dies im Kontext einer Ressourcengruppe tun. Eine {{site.data.keyword.la_full_notm}}-Instanz wird im Kontext einer Ressourcengruppe bereitgestellt. Erteilen Sie daher Zugriffsberechtigungen im Kontext der Ressourcengruppe.


Führen Sie die folgenden Schritte aus, um einem Benutzer beide Richtlinien für den {{site.data.keyword.la_full_notm}}-Service im Kontext einer Ressourcengruppe zuzuweisen: 

1. Klicken Sie in der Menüleiste auf **Verwalten** &gt; **Zugriff (IAM)** und wählen Sie dann **Benutzer** aus.
2. Wählen Sie in der Zeile des Benutzers, dem Sie Zugriff gewähren wollen, das Menü **Aktionen** aus und klicken Sie dann auf **Zugriff zuweisen**.
3. Wählen Sie **Zugriff in einer Ressourcengruppe zuweisen** aus.
4. Wählen Sie eine Ressourcengruppe aus.
5. Wurde dem Benutzer noch keine Rolle für die ausgewählte Ressourcengruppe erteilt, wählen Sie eine Rolle für das Feld **Zugriff für eine Ressourcengruppe zuweisen** aus. 

    Je nachdem, welche Rolle Sie auswählen, kann der Benutzer die Ressourcengruppe in seinem Dashboard anzeigen, den Namen der Ressourcengruppe bearbeiten oder den Benutzerzugriff auf die Gruppe verwalten. 
    
    Sie können **Kein Zugriff** auswählen, wenn der Benutzer nur Zugriff auf den {{site.data.keyword.la_full_notm}}-Service in der Ressourcengruppe haben soll.

6. Wählen Sie **IBM Log Analysis with LogDNA** aus.
7. Wählen Sie die Plattformrolle **Bearbeiter** aus.
8. Wählen Sie die Servicerolle **Manager** aus.
8. Klicken Sie auf **Zuweisen**.

## Benutzer Berechtigungen zum Anzeigen von Protokollen in LogDNA erteilen
{: #user_logdna}

Als **Benutzer**, **Auditor** oder **Entwickler** benötigen Sie möglicherweise Berechtigungen, um die folgenden Aktionen ausführen zu können: 

* Protokolle anzeigen
* Protokolle durchsuchen
* Protokolle filtern

Daher benötigen Sie die folgenden Richtlinien:

* Eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Plattformrolle **Anzeigeberechtigter**. Diese Richtlinie erteilt Berechtigungen zum Anzeigen der Serviceinstanzdetails über die Befehlszeile und im {{site.data.keyword.cloud_notm}}-Dashboard.
* Eine IAM-Richtlinie für den {{site.data.keyword.la_full_notm}}-Service mit der Servicerolle **Leseberechtigter**. Diese Richtlinie erteilt Berechtigungen zum Anzeigen, Filtern und Durchsuchen von Protokollen über die LogDNA-Webbenutzerschnittstelle.

**Anmerkung:** Wenn Sie als Administrator des Service einem Benutzer diese Richtlinien zuweisen, sollten Sie dies im Kontext einer Ressourcengruppe tun. Eine {{site.data.keyword.la_full_notm}}-Instanz wird im Kontext einer Ressourcengruppe bereitgestellt. Erteilen Sie daher Benutzern Zugriffsberechtigungen im Kontext der Ressourcengruppe.

Führen Sie die folgenden Schritte aus, um einem Benutzer beide Richtlinien für den {{site.data.keyword.la_full_notm}}-Service im Kontext einer Ressourcengruppe zuzuweisen: 

1. Klicken Sie in der Menüleiste auf **Verwalten** &gt; **Zugriff (IAM)** und wählen Sie dann **Benutzer** aus.
2. Wählen Sie in der Zeile des Benutzers, dem Sie Zugriff gewähren wollen, das Menü **Aktionen** aus und klicken Sie dann auf **Zugriff zuweisen**.
3. Wählen Sie **Zugriff in einer Ressourcengruppe zuweisen** aus.
4. Wählen Sie eine Ressourcengruppe aus.
5. Wurde dem Benutzer noch keine Rolle für die ausgewählte Ressourcengruppe erteilt, wählen Sie eine Rolle für das Feld **Zugriff für eine Ressourcengruppe zuweisen** aus. 

    Je nachdem, welche Rolle Sie auswählen, kann der Benutzer die Ressourcengruppe in seinem Dashboard anzeigen, den Namen der Ressourcengruppe bearbeiten oder den Benutzerzugriff auf die Gruppe verwalten. 
    
    Sie können **Kein Zugriff** auswählen, wenn der Benutzer nur Zugriff auf den {{site.data.keyword.la_full_notm}}-Service in der Ressourcengruppe haben soll.

6. Wählen Sie **IBM Log Analysis with LogDNA** aus.
7. Wählen Sie die Plattformrolle **Anzeigeberechtigter** aus.
8. Wählen Sie die Servicerolle **Leseberechtigter** aus.
8. Klicken Sie auf **Zuweisen**.

