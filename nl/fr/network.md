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

 
# Gestion du trafic réseau
{: #network}

Lorsqu'un pare-feu supplémentaire est configuré, ou si vous avez personnalisé les paramètres de pare-feu, dans votre infrastructure {{site.data.keyword.cloud_notm}}, vous devez autoriser le trafic réseau sortant vers le service {{site.data.keyword.la_full_notm}}. 
{:shortdesc}


## Trafic réseau pour les configurations de pare-feu personnalisées dans la région US South
{: #ips_us-south}

Vous devez autoriser le trafic sortant sur le port TCP 443 et le port TCP 80 dans votre pare-feu. Par exemple, vous devez ouvrir les ports TCP 443 et 80 de chaque noeud worker vers le service {{site.data.keyword.la_full_notm}}.

**Remarque :** le noeud final d'API est nécessaire pour l'authentification de l'agent LogDNA. L'agent LogDNA obtient un jeton que vous pouvez utiliser pour envoyer des journaux au noeud final d'ingestion.

Les tableaux suivants répertorient les adresses IP par région que vous devez configurer dans votre pare-feu pour autoriser le trafic sortant :

| Région      | Noeud final d'ingestion                          | Adresses IP publiques               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="Tableau 1. Adresses IP pour l'envoi des journaux" caption-side="top"}


| Région      | Noeud final d'authentification                     | Adresses IP publiques               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="Tableau 2. Adresses IP utilisées par l'agent LogDNA" caption-side="top"}



## Trafic réseau pour les configurations de pare-feu personnalisées dans la région EU DE
{: #ips_eu-de}

Vous devez autoriser le trafic sortant sur le port TCP 443 et le port TCP 80 dans votre pare-feu. Par exemple, vous devez ouvrir les ports TCP 443 et 80 de chaque noeud worker vers le service {{site.data.keyword.la_full_notm}}.

**Remarque :** le noeud final d'API est nécessaire pour l'authentification de l'agent LogDNA. L'agent LogDNA obtient un jeton que vous pouvez utiliser pour envoyer des journaux au noeud final d'ingestion.

Les tableaux suivants répertorient les adresses IP par région que vous devez configurer dans votre pare-feu pour autoriser le trafic sortant :

| Région      | Noeud final d'ingestion                          | Adresses IP publiques               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="Tableau 3. Adresses IP pour l'envoi des journaux" caption-side="top"}


| Région      | Noeud final d'authentification                     | Adresses IP publiques               | Ports   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="Tableau 4. Adresses IP utilisées par l'agent LogDNA" caption-side="top"}


