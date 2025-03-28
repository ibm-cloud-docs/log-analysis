---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords:

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# CIDR blocks
{: #cidr}

Classless Inter-Domain Routing (CIDR) blocks are ranges of addresses. {{site.data.keyword.la_full}} traffic will be sent from these addresses. This traffic includes webhooks, archiving to {{site.data.keyword.cos_full_notm}}, streaming to {{site.data.keyword.messagehub}} and so on. You can use these CIDR blocks in firewalls and other configurations to ensure that the data received by your code, or another {{site.data.keyword.IBM_notm}} service, originates only from {{site.data.keyword.la_full_notm}}.
{: shortdesc}


{{_include-segments/deprecation_notice.md}}

The CIDR blocks with a date next to them indicates the date they will be available. The CIDR blocks indicated as [Deprecated]{: tag-deprecated} are no longer supported and should be removed from any configured allowlists.
{: important}

## Public CIDR blocks
{: #cidr_public_gen2}

### Chennai
{: #cidr_public_gen2_8}

| Region   | CIDR block |
|----------|------------|
| Chennai  | 169.38.96.224/28  |
| Chennai  | 169.38.126.192/27 [9 March 2023]{: tag-cool-gray} |
{: caption="Chennai public CIDR blocks" caption-side="top"}

### Frankfurt
{: #cidr_public_gen2_3}

| Region   | CIDR block |
|----------|------------|
| Frankfurt | 161.156.114.96/28  |
| Frankfurt | 158.177.213.0/25  |
| Frankfurt | 158.177.168.32/28 [Deprecated]{: tag-deprecated} |
| Frankfurt | 149.81.103.80/28 [Deprecated]{: tag-deprecated} |
| Frankfurt | 158.177.37.192/26  |
| Frankfurt | 158.177.76.160/27  |
| Frankfurt | 149.81.189.192/26  |
| Frankfurt | 161.156.36.64/27  |
| Frankfurt | 161.156.36.128/26  |
| Frankfurt | 149.81.190.96/27  |
| Frankfurt | 161.156.41.0/25  |
| Frankfurt | 149.81.197.0/25  |
{: caption="Frankfurt public CIDR blocks" caption-side="top"}

### London
{: #cidr_public_gen2_5}

| Region   | CIDR block |
|----------|------------|
| London    | 158.176.89.32/27  |
| London    | 158.176.143.48/28 [Deprecated]{: tag-deprecated}  |
| London    | 141.125.139.160/27  |
| London    | 141.125.139.144/28  |
| London    | 158.175.167.48/28  |
| London    | 158.175.168.32/27  |
| London    | 158.176.67.64/26 [5 April 2023]{: tag-cool-gray} |
| London    | 161.156.205.0/26 [5 April 2023]{: tag-cool-gray} |
| London    | 141.125.144.192/26 [5 April 2023]{: tag-cool-gray} |
{: caption="London public CIDR blocks" caption-side="top"}

### Madrid
{: #cidr_public_madrid}

| Region   | CIDR block |
|----------|------------|
| Madrid    | 13.120.68.144/28 [26 September 2023]{: tag-cool-gray} |
| Madrid    | 13.122.68.112/28 [26 September 2023]{: tag-cool-gray} |
| Madrid    | 13.121.68.64/28 [26 September 2023]{: tag-cool-gray} |
{: caption="Madrid public CIDR blocks" caption-side="top"}

### Osaka
{: #cidr_public_gen2_9}

| Region   | CIDR block |
|----------|------------|
| Osaka	   | 163.73.65.176/28  |
| Osaka	   | 163.68.73.240/28  |
| Osaka	   | 163.69.68.48/28  |
| Osaka    | 163.69.72.96/27 [3 April 2023]{: tag-cool-gray} |
| Osaka    | 163.73.72.0/27 [3 April 2023]{: tag-cool-gray} |
| Osaka    | 163.68.68.160/27 [3 April 2023]{: tag-cool-gray} |
{: caption="Osaka public CIDR blocks" caption-side="top"}

### Sao Paulo
{: #cidr_public_gen2_11}

| Region   | CIDR block |
|----------|------------|
| Brazil	   | 169.57.222.224/28  |
| Brazil	   | 163.107.65.208/28  |
| Brazil	   | 163.109.67.224/28  |
| Brazil     | 169.57.178.32/27 [9 March 2023]{: tag-cool-gray} |
| Brazil     | 163.109.74.0/27 [9 March 2023]{: tag-cool-gray} |
| Brazil     | 163.107.74.32/27 [9 March 2023]{: tag-cool-gray} |
{: caption="Sao Paulo public CIDR blocks" caption-side="top"}

### Sydney
{: #cidr_public_gen2_6}

| Region   | CIDR block |
|----------|------------|
| Sydney    | 168.1.40.48/28 |
| Sydney    | 130.198.92.144/28 |
| Sydney    | 135.90.90.240/28  |
| Sydney    | 168.1.31.192/27 [3 April 2023]{: tag-cool-gray} |
| Sydney    | 130.198.83.0/27 [3 April 2023]{: tag-cool-gray} |
| Sydney    | 135.90.82.32/27 [3 April 2023]{: tag-cool-gray} |
{: caption="Sydney public CIDR blocks" caption-side="top"}

### Tokyo
{: #cidr_public_gen2_4}

| Region   | CIDR block |
|----------|------------|
| Tokyo	    | 161.202.78.80/28  |
| Tokyo	    | 161.202.78.192/27  |
| Tokyo	    | 128.168.83.96/27  |
| Tokyo	    | 165.192.97.208/28  |
| Tokyo	    | 128.168.95.64/28  |
| Tokyo	    | 165.192.107.32/27  |
{: caption="Tokyo public CIDR blocks" caption-side="top"}

### Toronto
{: #cidr_public_gen2_10}

| Region   | CIDR block |
|----------|------------|
| Toronto	   | 169.53.180.32/28  |
| Toronto | 169.55.136.192/27 [9 March 2023]{: tag-cool-gray} |
| Toronto	   | 163.74.69.208/28 [Deprecated]{: tag-deprecated} |
| Toronto	   | 163.75.69.160/28  |
| Toronto	   | 163.74.71.224/27 [9 March 2023]{: tag-cool-gray} |
| Toronto	   | 163.75.75.128/27 [9 March 2023]{: tag-cool-gray} |
{: caption="Toronto public CIDR blocks" caption-side="top"}

### US East
{: #cidr_public_gen2_2}

| Region   | CIDR block |
|----------|------------|
| US-East  | 169.60.83.144/28  |
| US-East  | 169.60.120.32/27  |
| US-East  | 52.117.81.128/26   |
| US-East  | 169.47.54.16/28  |
| US-East  | 52.117.100.16/28  |
| US-East  | 169.62.40.192/27  |
| US-East  | 169.47.188.0/27  |
| US-East  | 169.59.154.128/26  |
| US-East  | 150.239.98.0/26  |
{: caption="US-East public CIDR blocks" caption-side="top"}

### US South
{: #cidr_public_gen2_1}

| Region | CIDR block |
|--------|------------|
| US-South | 67.228.81.0/27  |
| US-South | 67.228.228.128/26  |
| US-South | 67.228.231.0/25  |
| US-South | 169.61.184.64/28  |
| US-South | 169.63.192.0/25  |
| US-South | 169.63.193.0/26  |
| US-South | 67.228.222.64/28  |
| US-South | 169.48.177.128/28  |
| US-South | 52.118.43.0/27  |
| US-South | 52.116.251.64/27  |
| US-South | 169.59.254.192/26  |
| US-South | 169.59.255.128/25  |
{: caption="US-South public CIDR blocks" caption-side="top"}

## Private CIDR blocks
{: #cidr_private_gen2}

### Chennai
{: #cidr_private_gen2_19}

| Region | CIDR block |
|--------|------------|
| Chennai	  | 10.162.140.0/26  |
{: caption="Chennai private CIDR blocks" caption-side="top"}

### Frankfurt
{: #cidr_private_gen2_14}

| Region | CIDR block |
|--------|------------|
| Frankfurt | 10.194.10.64/26  |
| Frankfurt | 10.240.29.64/26  |
| Frankfurt | 10.13.13.128/26  |
| Frankfurt | 10.240.239.0/24  |
| Frankfurt | 10.215.253.128/25  |
| Frankfurt | 10.21.3.0/25  |
| Frankfurt | 10.13.86.128/25  |
| Frankfurt | 10.20.6.0/24  |
| Frankfurt | 10.13.100.0/24  |
{: caption="Frankfurt private CIDR blocks" caption-side="top"}

### London
{: #cidr_private_gen2_16}

| Region | CIDR block |
|--------|------------|
| London    | 10.72.11.64/26  |
| London    | 10.196.113.0/25 [9 March 2023]{: tag-cool-gray} |
| London    | 10.196.134.64/26  |
| London    | 10.242.25.128/25 [9 March 2023]{: tag-cool-gray} |
| London    | 10.222.46.128/26  |
| London    | 10.222.86.128/25 [9 March 2023]{: tag-cool-gray} |
{: caption="London private CIDR blocks" caption-side="top"}

### Madrid
{: #cidr_private_madrid}

| Region   | CIDR block |
|----------|------------|
| Madrid    | 10.118.14.192/26 [26 September 2023]{: tag-cool-gray} |
| Madrid    | 10.118.76.192/26 [26 September 2023]{: tag-cool-gray} |
| Madrid    | 10.118.142.128/26 [26 September 2023]{: tag-cool-gray} |
{: caption="Madrid public CIDR blocks" caption-side="top"}

### Osaka
{: #cidr_private_gen2_20}

| Region | CIDR block |
|--------|------------|
| Osaka	  | 10.10.8.64/26  |
| Osaka	  | 10.9.15.128/26  |
| Osaka	  | 10.8.30.64/26  |
{: caption="Osaka private CIDR blocks" caption-side="top"}

### Sao Paulo
{: #cidr_private_gen2_22}

| Region   | CIDR block |
|----------|------------|
| Brazil	   | 10.150.186.192/26  |
| Brazil	   | 10.14.9.64/26  |
| Brazil	   | 10.15.20.192/26  |
{: caption="Sao Paulo private CIDR blocks" caption-side="top"}

### Sydney
{: #cidr_private_gen2_17}

| Region | CIDR block |
|--------|------------|
| Sydney	  | 10.139.31.0/26  |
| Sydney	  | 10.63.207.128/26  |
| Sydney	  | 10.195.95.64/26 |
{: caption="Sydney private CIDR blocks" caption-side="top"}

### Tokyo
{: #cidr_private_gen2_15}

| Region | CIDR block |
|--------|------------|
| Tokyo	    | 10.129.65.128/26  |
| Tokyo	    | 10.192.21.128/26  |
| Tokyo	    | 10.193.77.192/26  |
| Tokyo     | 10.193.30.0/25 [6 April 2023]{: tag-cool-gray} |
| Tokyo     | 10.133.200.128/25 [6 April 2023]{: tag-cool-gray} |
| Tokyo     | 10.192.170.128/25 [6 April 2023]{: tag-cool-gray} |
{: caption="Tokyo private CIDR blocks" caption-side="top"}

### Toronto
{: #cidr_private_gen2_21}

| Region | CIDR block |
|--------|------------|
| Toronto	  | 10.114.152.128/26  |
| Toronto	  | 10.11.16.64/26  |
| Toronto	  | 10.243.35.128/26  |
| Toronto | 10.115.99.128/25 [10 May 2023]{: tag-cool-gray} |
| Toronto | 10.11.18.128/25 [10 May 2023]{: tag-cool-gray} |
| Toronto | 10.243.52.128/25 [10 May 2023]{: tag-cool-gray} |
{: caption="Toronto private CIDR blocks" caption-side="top"}

### US South
{: #cidr_private_gen2_12}

| Region | CIDR block |
|--------|------------|
| US-South | 10.93.88.0/26  |
| US-South | 10.241.27.0/26  |
| US-South | 10.5.108.0/24  |
| US-South | 10.37.71.0/26  |
| US-South | 10.5.193.0/25  |
| US-South | 10.37.81.0/25  |
| US-South | 10.241.199.0/25  |
| US-South | 10.37.88.0/24   |
| US-South | 10.241.202.0/24  |
{: caption="US-South private CIDR blocks" caption-side="top"}

### US East
{: #cidr_private_gen2_13}

| Region | CIDR block |
|--------|------------|
| US-East  | 10.183.182.128/26  |
| US-East  | 10.190.43.128/25  |
| US-East  | 10.191.225.64/26  |
| US-East  | 10.188.240.192/26  |
| US-East  | 10.183.242.128/25  |
| US-East  | 10.189.123.128/25  |
{: caption="US-East private CIDR blocks" caption-side="top"}
