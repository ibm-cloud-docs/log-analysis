---

copyright:
  years:  2018, 2019
lastupdated: "2019-05-01"

keywords: LogDNA, IBM, Log Analysis, logging, iam, manage user access

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

 
# Benutzerzugriff mit IAM verwalten
{: #iam}

{{site.data.keyword.iamlong}} (IAM) ermöglicht Ihnen die sichere Authentifizierung von Benutzern und die einheitliche Steuerung des Zugriffs auf alle Cloudressourcen in {{site.data.keyword.cloud_notm}}. 
{:shortdesc}

**Jedem Benutzer, der auf den {{site.data.keyword.la_full_notm}}-Service in Ihrem Konto zugreift, muss eine Zugriffsrichtlinie mit einer definierten IAM-Benutzerrolle zugeordnet werden. ** Die Richtlinie legt fest, welche Aktionen ein Benutzer im Kontext des ausgewählten Service bzw. der ausgewählten Instanz ausführen kann. Die zulässigen Aktionen werden angepasst und als Operationen definiert, deren Ausführung für den Service zulässig ist. Dann werden die Aktionen IAM-Benutzerrollen zugeordnet.

Durch *Richtlinien* ist es möglich, den Zugriff auf verschiedenen Ebenen zu gewähren. Zu den Optionen gehören unter anderem: 

* Zugriff auf alle IAM-fähigen Services in Ihrem Konto
* Zugriff auf alle Instanzen des Service in einer einzelnen Region in Ihrem Konto
* Zugriff auf eine einzelne Serviceinstanz in Ihrem Konto
* Zugriff auf alle Instanzen des Service im Kontext einer Ressourcengruppe
* Zugriff auf alle Instanzen des Service in einer einzelnen Region im Kontext einer Ressourcengruppe
* Zugriff auf alle IAM-fähigen Services im Kontext einer Ressourcengruppe

*Rollen* definieren die Aktionen, die ein Benutzer oder eine Service-ID ausführen kann. In {{site.data.keyword.cloud_notm}} gibt es verschiedene Rollentypen:

* Mit *Plattformmanagementrollen* können Benutzer Tasks für Serviceressourcen auf Plattformebene ausführen, z. B. Benutzerzugriff für den Service zuweisen, Service-IDs erstellen oder löschen, Instanzen erstellen, anderen Benutzern Richtlinien für Ihren Service zuordnen und Instanzen an Anwendungen binden.
* *Servicezugriffsrollen* ermöglichen es, dass Benutzern unterschiedliche Berechtigungsstufen für den Aufruf der Service-API zugewiesen werden.

**Verwenden Sie *Zugriffsgruppen*, um eine Gruppe von Benutzern und Service-IDs in einer einzelnen Entität zusammenzufassen, die Ihnen die Verwaltung von IAM-Berechtigungen erleichtert. ** Sie können der Gruppe eine einzige Richtlinie zuweisen, anstatt denselben Zugriff mehrmals für einzelne Benutzer oder einzelne Service-IDs zuzuweisen.
{: tip}


## Zugriff mit Zugriffsgruppen verwalten
{: #groups}

Sie müssen der Kontoeigner, Administrator oder Bearbeiter für alle Services mit aktiviertem Identity and Access Management im Konto oder der zugeordnete Administrator oder Bearbeiter für den IAM-Zugriffsgruppenservice sein, um mithilfe von Zugriffsgruppen den Benutzerzugriff verwalten oder Benutzern neue Zugriffsberechtigungen zuweisen zu können. 

Wählen Sie eine der folgenden Aktionen aus, um Zugriffsgruppen in {{site.data.keyword.cloud_notm}} zu verwalten:

* [Zugriffsgruppe erstellen](/docs/iam?topic=iam-groups#create_ag).
* [Zugriff auf eine Gruppe zuweisen](/docs/iam?topic=iam-groups#access_ag).


## Benutzerzugriff durch direkte Richtlinienzuordnung verwalten
{: #users}

Sie müssen der Kontoeigner, der Administrator für alle Services im Konto oder ein Administrator für den jeweiligen Service oder die jeweilige Serviceinstanz sein, um mithilfe von IAM-Richtlinien den Benutzerzugriff verwalten oder Benutzern neue Zugriffsberechtigungen zuweisen zu können. 

Wählen Sie eine der folgenden Aktionen aus, um IAM-Richtlinien in {{site.data.keyword.cloud_notm}} zu verwalten:

* Informationen zur Änderung der Berechtigungen eines Benutzers finden Sie in [Vorhandene Zugriffsberechtigungen bearbeiten](/docs/iam?topic=iam-iammanidaccser#edit_existing).
* Informationen zum Erteilen von Benutzerberechtigungen finden Sie in [Neue Zugriffsberechtigungen zuweisen](/docs/iam?topic=iam-iammanidaccser#assign_new_access).
* Informationen zum Widerrufen von Berechtigungen finden Sie in [Zugriffsberechtigungen entfernen](/docs/iam?topic=iam-iammanidaccser#removing_access).
* Informationen zum Überprüfen der Berechtigungen eines Benutzers finden Sie in [Zugewiesene Zugriffsberechtigungen überprüfen](/docs/iam?topic=iam-iammanidaccser#review_your_access).




## {{site.data.keyword.cloud_notm}}-Plattformrollen
{: #platform}

Mithilfe der folgenden Tabelle können Sie feststellen, welche Plattformrolle Sie einem Benutzer in {{site.data.keyword.cloud_notm}} zur Ausführung der folgenden Plattformaktionen zuweisen können:

| Plattformaktionen                                                         | {{site.data.keyword.cloud_notm}}-Plattformrollen    | 
|--------------------------------------------------------------------------|------------------------------------------------------|
| `Anderen Kontomitgliedern Zugriff für die Arbeit mit dem Service gewähren`            | Administrator                                        | 
| `Serviceinstanz bereitstellen`                                           | Bearbeiter                            | 
| `Serviceinstanz löschen`                                              | Administrator </br>Bearbeiter                            | 
| `Service-ID erstellen`                                                    | Administrator </br>Bearbeiter                            |
| `Details einer Serviceinstanz anzeigen`                                     | Administrator </br>Bearbeiter </br>Operator </br>Anzeigeberechtigter  | 
| `Serviceinstanzen im Dashboard Beobachtbarkeit - Protokollierung anzeigen`          | Administrator </br>Bearbeiter </br>Operator </br>Anzeigeberechtigter  | 
| `Aufnahmeschlüssel in {{site.data.keyword.cloud_notm}}-Konsole anzeigen` | Administrator                                        | 
{: caption="Tabelle 1. IAM-Benutzerrollen und -Aktionen" caption-side="top"}



## {{site.data.keyword.cloud_notm}}-Servicerollen
{: #service}

Mithilfe der folgenden Tabelle können Sie feststellen, welche Servicerollen Sie einem Benutzer zur Ausführung der folgenden Serviceaktionen zuweisen können:

| Aktionen                                                                 | {{site.data.keyword.cloud_notm}}-Servicerollen     | 
|-------------------------------------------------------------------------|------------------------------------------------------|
| `LogDNA-Protokollquellen hinzufügen`                                                | Manager                                              |
| `Aufnahmeschlüssel in der LogDNA-Webbenutzerschnittstelle verwalten`                       | Manager                                              |
| `Serviceschlüssel verwalten`                                                   | Manager                                              |
| `Protokolle archivieren`                                                          | Manager                                              |
| `Parsing verwalten`                                                        | Manager                                              |
| `Alerts konfigurieren`                                                      | Manager </br>Schreibberechtigter</br>Leseberechtigter                      | 
| `Protokolldaten filtern und durchsuchen`                                            | Manager </br>Schreibberechtigter</br>Leseberechtigter                      |
| `Ansichten erstellen`                                                          | Manager </br>Schreibberechtigter</br>Leseberechtigter                      |
| `Ansichten verwalten`                                                          | Manager </br>Schreibberechtigter</br>Leseberechtigter                      |
| `Protokolldaten exportieren`                                                       | Manager </br>Schreibberechtigter</br>Leseberechtigter                      |
| `Benutzervorgabe in der LogDNA-Webbenutzerschnittstelle konfigurieren`                       | Manager </br>Schreibberechtigter</br>Leseberechtigter                      |
| `Protokolle in der LogDNA-Webbenutzerschnittstelle anzeigen`                                   | Manager </br>Schreibberechtigter</br>Leseberechtigter                      | 
{: caption="Tabelle 2. IAM-Benutzerrollen und -Aktionen" caption-side="top"}


**Anmerkung:** Die Servicerolle **Manager** entspricht der LogDNA-Rolle **Administrator**.






