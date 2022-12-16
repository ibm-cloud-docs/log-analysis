---

copyright:
  years:  2018, 2022
lastupdated: "2022-12-13"

keywords: IBM, Log Analysis, logging, endpoints

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Service IP changes
{: #service-ip-changes}

Due to maintenance, {{site.data.keyword.la_full}} makes changes periodically to service IPs in some regions. You might need to take action to continue using the service.
{: shortdesc}

For the current list of endpoints that should be allowlisted in your environment, see [endpoints](/docs/log-analysis?topic=log-analysis-endpoints).

Endpoints and regions that are not listed are unchanged.
{: note}

## After 15 January 2023
{: #endpoint-changes-15Jan2022}

The following endpoints will be changing in after 15 January 2023. The new IPs are listed in [endpoints](/docs/log-analysis?topic=log-analysis-endpoints). The new IPs can be allowlisted in advance to avoid impacts when the change is made.

### Chennai (in-che)
{: #010123_inche}

* `api.private.in-che.logging.cloud.ibm.com`
* `logs.in-che.logging.cloud.ibm.com`
* `logs.private.in-che.logging.cloud.ibm.com`

### Dallas (us-south)
{: #010123_ussouth}

* `api.private.us-south.logging.cloud.ibm.com`
* `logs.us-south.logging.cloud.ibm.com`
* `logs.private.us-south.logging.cloud.ibm.com`

### Frankfurt (eu-de)
{: #010123_eude}

* `api.private.eu-de.logging.cloud.ibm.com`
* `logs.eu-de.logging.cloud.ibm.com`
* `logs.private.eu-de.logging.cloud.ibm.com`

### London (eu-gb)
{: #010123_eugb}

* `api.private.eu-gb.logging.cloud.ibm.com`
* `logs.eu-gb.logging.cloud.ibm.com`
* `logs.private.eu-gb.logging.cloud.ibm.com`

### Osaka (jp-osa)
{: #010123_jposa}

* `api.private.jp-osa.logging.cloud.ibm.com`
* `logs.jp-osa.logging.cloud.ibm.com`
* `logs.private.jp-osa.logging.cloud.ibm.com`

### Sao Paulo (br-sao)
{: #010123_brsao}

* `api.private.br-sao.logging.cloud.ibm.com`
* `logs.br-sao.logging.cloud.ibm.com`
* `logs.private.br-sao.logging.cloud.ibm.com`

### Sydney (au-syd)
{: #010123_ausyd}

* `api.private.au-syd.logging.cloud.ibm.com`
* `logs.au-syd.logging.cloud.ibm.com`
* `logs.private.au-syd.logging.cloud.ibm.com`

### Tokyo (jp-tok)
{: #010123_jptok}

* `api.private.jp-tok.logging.cloud.ibm.com`
* `logs.jp-tok.logging.cloud.ibm.com`
* `logs.private.jp-tok.logging.cloud.ibm.com`

### Toronto (ca-tor)
{: #010123_cator}

* `api.private.ca-tor.logging.cloud.ibm.com`
* `logs.ca-tor.logging.cloud.ibm.com`
* `logs.private.ca-tor.logging.cloud.ibm.com`

### Washington (us-east)
{: #010123_useast}

* `api.private.us-east.logging.cloud.ibm.com`
* `logs.us-east.logging.cloud.ibm.com`
* `logs.private.us-east.logging.cloud.ibm.com`

## 8 December 2022
{: #endpoint-changes-08Dec2022}

The following endpoints have changes effective 8 December 2022.

### Dallas (us-south)
{: #120822_ussouth}

* `logs.private.us-south.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.us-south.logging.cloud.ibm.com`

### Frankfurt (eu-de)
{: #120822_eude}

* `api.private.eu-de.logging.cloud.ibm.com`
* `logs.private.eu-de.logging.cloud.ibm.com`
* `syslog-a.private.eu-de.logging.cloud.ibm.com`
* `syslog://syslog-u.private.eu-de.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.private.eu-de.logging.cloud.ibm.com`

### Sao Paulo (br-sao)
{: #120822_brsao}

* `api.private.br-sao.logging.cloud.ibm.com`

### Seoul (kr-seo)
{: #120822_krseo}

All Seoul (kr-seo) endpoints are deprecated.
{: note}

* `api.kr-seo.logging.cloud.ibm.com`
* `api.private.kr-seo.logging.cloud.ibm.com`
* `logs.kr-seo.logging.cloud.ibm.com`
* `logs.private.kr-seo.logging.cloud.ibm.com`
* `syslog://syslog-a.kr-seo.logging.cloud.ibm.com`
* `syslog-a.private.kr-seo.logging.cloud.ibm.com`
* `syslog://syslog-u.kr-seo.logging.cloud.ibm.com`
* `syslog://syslog-u.private.kr-seo.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.kr-seo.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.private.kr-seo.logging.cloud.ibm.com`

### Sydney (au-syd)
{: #120822_ausyd}

* `api.private.au-syd.logging.cloud.ibm.com`
* `logs.private.au-syd.logging.cloud.ibm.com`
* `syslog-a.private.au-syd.logging.cloud.ibm.com`
* `syslog://syslog-u.private.au-syd.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.private.au-syd.logging.cloud.ibm.com`

### Tokyo (jp-tok)
{: #120822_jptok}

* `api.private.jp-tok.logging.cloud.ibm.com`
* `logs.private.jp-tok.logging.cloud.ibm.com`
* `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`
* `syslog-a.private.jp-tok.logging.cloud.ibm.com`
* `syslog://syslog-u.private.jp-tok.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.jp-tok.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.private.jp-tok.logging.cloud.ibm.com`

### Toronto (ca-tor)
{: #120822_cator}

* `api.private.ca-tor.logging.cloud.ibm.com`
* `logs.private.ca-tor.logging.cloud.ibm.com`

### Washington (us-east)
{: #120822_useast}

* `api.private.us-east.logging.cloud.ibm.com`
* `logs.private.us-east.logging.cloud.ibm.com`
* `syslog-a.private.us-east.logging.cloud.ibm.com`
* `syslog://syslog-u.private.us-east.logging.cloud.ibm.com`
* `syslog-tls://syslog-a.private.us-east.logging.cloud.ibm.com`


## 9 May 2022
{: #endpoint-changes-09May2022}

The following endpoints have changes effective 9 May 2022.

### Chenai (in-che)
{: #042122_inche}

* `api.in-che.logging.cloud.ibm.com`
* `syslog-a.private.in-che.logging.cloud.ibm.com`

### Dallas (us-south)
{: #042122_ussouth}

* `api.us-south.logging.cloud.ibm.com`
* `syslog-a.private.us-south.logging.cloud.ibm.com`

### Frankfurt (eu-de)
{: #042122_eude}

* `api.eu-de.logging.cloud.ibm.com`
* `syslog-a.private.eu-de.logging.cloud.ibm.com`

### London (eu-gb)
{: #042122_eugb}

* `api.eu-gb.logging.cloud.ibm.com`
* `syslog-a.private.eu-gb.logging.cloud.ibm.com`

### Osaka (jp-osa)
{: #042122_jposa}

* `api.jp-osa.logging.cloud.ibm.com`
* `syslog-a.private.jp-osa.logging.cloud.ibm.com`

### Sao Paulo (br-sao)
{: #042122_brsao}

* `api.br-sao.logging.cloud.ibm.com`
* `api.private.br-sao.logging.cloud.ibm.com`
* `syslog-a.private.br-sao.logging.cloud.ibm.com`

### Seoul (kr-seo)
{: #042122_krseo}

* `api.kr-seo.logging.cloud.ibm.com`
* `syslog-a.private.kr-seo.logging.cloud.ibm.com`

### Sydney (au-syd)
{: #042122_ausyd}

* `api.au-syd.logging.cloud.ibm.com`
* `syslog-a.private.au-syd.logging.cloud.ibm.com`

### Tokyo (jp-tok)
{: #042122_jptok}

* `api.jp-tok.logging.cloud.ibm.com`
* `api.private.jp-tok.logging.cloud.ibm.com`
* `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`
* `syslog-a.private.jp-tok.logging.cloud.ibm.com`

### Toronto (ca-tor)
{: #042122_cator}

* `api.ca-tor.logging.cloud.ibm.com`
* `api.private.ca-tor.logging.cloud.ibm.com`
* `syslog-a.private.ca-tor.logging.cloud.ibm.com`

### Washington (us-east)
{: #042122_useast}

* `api.us-east.logging.cloud.ibm.com`
* `api.private.us-east.logging.cloud.ibm.com`
* `syslog-a.private.us-east.logging.cloud.ibm.com`

## 3 February 2022
{: #service-ip-changes-03feb2022}

The following endpoint had changes effective 3 February 2022.

### Tokyo (jp-tok)
{: #syslog-ip-changes-tokyo}

* `syslog://syslog-a.jp-tok.logging.cloud.ibm.com`

## 28 May 2021
{: #service-ip-changes-28May2021}

The following endpoints have changes effective 28 May 2021.

### London (eu-gb)
{: #service-ip-changes-london}

* `logs.eu-gb.logging.cloud.ibm.com`
* `logs.private.eu-gb.logging.cloud.ibm.com`
* `syslog-a.eu-gb.logging.cloud.ibm.com`
* `api.eu-gb.logging.cloud.ibm.com`
* `api.private.eu-gb.logging.cloud.ibm.com`

### Dallas (us-south)
{: #service-ip-changes-dallas}

* `logs.us-south.logging.cloud.ibm.com`
* `logs.private.us-south.logging.cloud.ibm.com`
* `syslog-a.us-south.logging.cloud.ibm.com`
* `api.us-south.logging.cloud.ibm.com`
* `api.private.us-south.logging.cloud.ibm.com`

### Frankfurt (eu-de)
{: #service-ip-changes-frankfurt}

* `logs.eu-de.logging.cloud.ibm.com`
* `logs.private.eu-de.logging.cloud.ibm.com`
* `syslog-a.eu-de.logging.cloud.ibm.com`
* `api.eu-de.logging.cloud.ibm.com`
* `api.private.eu-de.logging.cloud.ibm.com`

## User-required tasks
{: #service-ip-changes-tasks}

If you are using public endpoints, you must complete the following tasks:

### Reconfigure your firewalls to the new IPs
{: #service-ip-changes-tasks-1}

If you have firewalls set up on the public or private network in your {{site.data.keyword.cloud_notm}} infrastructure account, you need to allow traffic to and from the {{site.data.keyword.la_full_notm}} service. You must allow traffic on TCP port 443 and TCP port 80 in your firewall for the API endpoints and the ingestion endpoints. Check that valid IPs are configured per region where you operate. For a list of valid IPs, see [IP changes by region](/docs/log-analysis?topic=log-analysis-service-ip-changes#service-ip-changes-ips).

### Reconfigure applications and services
{: #service-ip-changes-tasks-2}

If you have applications and services that restrict connectivity to specific IPs and communicate with the {{site.data.keyword.la_short}} service, make sure the new IPs are configured to avoid interruption of the logging service.
