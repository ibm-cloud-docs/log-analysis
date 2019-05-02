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

 
# Gerenciando o tráfego de
{: #network}

Quando você tiver um firewall adicional configurado ou tiver customizado as configurações de firewall em sua infraestrutura do {{site.data.keyword.cloud_notm}}, será necessário permitir o tráfego de rede de saída para o serviço {{site.data.keyword.la_full_notm}}. 
{:shortdesc}


## Tráfego de rede para configurações de firewall customizado na região Sul dos EUA
{: #ips_us-south}

Deve-se permitir o tráfego de saída na porta do TCP 443 e na porta do TCP 80 em seu firewall. Por exemplo, deve-se abrir a porta do TCP 443 e a porta do TCP 80 de cada trabalhador para o serviço do {{site.data.keyword.la_full_notm}}.

**Nota:** o terminal de API é necessário para a autenticação do agente do LogDNA. O agente do LogDNA obtém um token que pode ser usado para enviar logs para o terminal de Ingestão.

As tabelas a seguir listam os endereços IP por região que devem ser configurados em seu firewall para permitir o tráfego de saída:

| Região      | Terminal de ingestão                          | Endereços IP públicos               | Portas   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | logs.us-south.logging.cloud.ibm.com         | 169.48.237.107 </br>169.60.166.45 </br>169.47.224.77  | TCP 443 </br>TCP 80 | 
{: caption="Tabela 1. Endereços IP para enviar logs" caption-side="top"}


| Região      | Terminal de autenticação                     | Endereços IP públicos               | Portas   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `US South`    | api.us-south.logging.cloud.ibm.com          | 169.47.224.74  </br>169.60.166.44 </br>169.48.237.109  | TCP 443 </br>TCP 80 |
{: caption="Tabela 2. Endereços IP usados pelo agente LogDNA" caption-side="top"}



## Tráfego de rede para configurações de firewall customizadas na região DE da UE
{: #ips_eu-de}

Deve-se permitir o tráfego de saída na porta do TCP 443 e na porta do TCP 80 em seu firewall. Por exemplo, deve-se abrir a porta do TCP 443 e a porta do TCP 80 de cada trabalhador para o serviço do {{site.data.keyword.la_full_notm}}.

**Nota:** o terminal de API é necessário para a autenticação do agente do LogDNA. O agente do LogDNA obtém um token que pode ser usado para enviar logs para o terminal de Ingestão.

As tabelas a seguir listam os endereços IP por região que devem ser configurados em seu firewall para permitir o tráfego de saída:

| Região      | Terminal de ingestão                          | Endereços IP públicos               | Portas   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | logs.eu-de.logging.cloud.ibm.com         | 161.156.89.11 </br>149.81.86.68 </br>158.177.129.36  | TCP 443 </br>TCP 80 | 
{: caption="Tabela 3. Endereços IP para enviar logs" caption-side="top"}


| Região      | Terminal de autenticação                     | Endereços IP públicos               | Portas   |
|-------------|---------------------------------------------|-----------------------------------|---------|
| `EU DE`     | api.eu-de.logging.cloud.ibm.com          | 161.156.89.12  </br>149.81.86.66 </br>158.177.129.34    | TCP 443 </br>TCP 80 |
{: caption="Tabela 4. Endereços IP usados pelo agente LogDNA" caption-side="top"}


