---

copyright:
  years:  2018, 2019
lastupdated: "2019-03-06"

keywords: LogDNA, IBM, Log Analysis, logging, detach config agent

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

# Zuordnung eines LogDNA-Agenten zu einer Instanz aufheben
{: #detach_agent}

Heben Sie die Zuordnung eines LogDNA-Agenten zu eine Protokollierungsinstanz auf, um das Erfassen von Protokollen zu stoppen.
{:shortdesc}

## Zuordnung eines LogDNA-Agenten zu einem Kubernetes-Cluster aufheben
{: #detach_agent_kube}

Wenn das Senden von Protokollen vom Kubernetes-Cluster an die {{site.data.keyword.la_full_notm}}-Instanz gestoppt werden soll, müssen Sie den LogDNA-Agenten vom Cluster entfernen. 

Führen Sie die folgenden Schritte über die Befehlszeile aus, um das Weiterleiten von Protokollen vom Kubernetes-Cluster zur LogDNA-Instanz zu stoppen:

1. Öffnen Sie ein Terminal. [Melden Sie sich dann bei {{site.data.keyword.cloud_notm}} ![Symbol für externen Link](../../icons/launch-glyph.svg "Symbol für externen Link")](https://cloud.ibm.com/login){:new_window} an und folgen Sie den Eingabeaufforderungen. 

    Wählen Sie das Konto aus, in dem Sie die {{site.data.keyword.la_full_notm}}-Instanz bereitgestellt haben.

2. Richten Sie die Clusterumgebung ein. Führen Sie die folgenden Befehle aus:

    Führen Sie zunächst den Befehl zur Angabe der Umgebungsvariablen und zum Herunterladen der Kubernetes-Konfigurationsdateien aus.

    ```
    ibmcloud ks cluster-config <Clustername_oder_-ID>
    ```
    {: codeblock}

    Sobald der Download der Konfigurationsdateien beendet ist, wird ein Befehl angezeigt, mit dem Sie den Pfad zur lokalen Kubernetes-Konfigurationsdatei als Umgebungsvariable festlegen können.

    Kopieren Sie dann den Befehl, der in Ihrem Terminal angezeigt wird, und fügen Sie ihn ein, um die Umgebungsvariable `KUBECONFIG` zu definieren.

3. Entfernen Sie den geheimen Schlüssel aus dem Kubernetes-Cluster. Der geheime Kubernetes-Schlüssel enthält den LogDNA-Aufnahmeschlüssel. Führen Sie den folgenden Befehl aus:

    ```
    kubectl delete secret logdna-agent-key
    ```
    {: codeblock}

4. Entfernen Sie den LogDNA-Agenten auf jedem Worker (Knoten) Ihres Kubernetes-Clusters. Der LogDNA-Agent ist für die Erfassung und Weiterleitung Ihrer Protokolle zuständig. Führen Sie den folgenden Befehl aus:

    ```
    kubectl delete daemonset logdna-agent
    ```
    {: codeblock}

5. Überprüfen Sie, ob der LogDNA-Agent erfolgreich gelöscht wurde. Führen Sie den folgenden Befehl aus:

    ```
    kubectl get pods
    ```
    {: codeblock}

    Es sollten keine LogDNA-Pods angezeigt werden.




