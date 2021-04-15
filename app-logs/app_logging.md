---

copyright:
  years:  2018, 2021
lastupdated: "2021-04-12"

keywords: IBM, Log Analysis, logging, applications

subcollection: log-analysis

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
{:external: target="_blank" .external}

# Logging with applications overview
{: #app_logging}

You can use the Ingestion REST API and libraries to send application logs to an {{site.data.keyword.la_full}} instance.
{:shortdesc}

In an application log, you can find information that you can use to troubleshoot and monitor your application.

In {{site.data.keyword.la_short}}, you can choose any of the following options to send application logs to an {{site.data.keyword.la_full_notm}} instance: 


## REST API
{: #app_logging_api}

You can send log data to an {{site.data.keyword.la_full_notm}} instance by using the Ingestion REST API. For more information, see [Sending logs by using the REST API](/docs/log-analysis?topic=log-analysis-ingest).


## Code library
{: #app_logging_code}


You can add code to an application to manage application logs through an {{site.data.keyword.la_full}} instance. 


The following table lists libraries that you can use to send application logs to an {{site.data.keyword.la_full_notm}} instance:

![Code libraries](/images/app_logging_img1.png "Code libraries")

| Library | Git Repo | More info |
|---------|----------|-----------|
| `Python` | [Python](https://github.com/logdna/python){: external} | [Sending logs by using Python](/docs/log-analysis?topic=log-analysis-ingest_python). |
| `Node`   | [Node](https://github.com/logdna/nodejs){: external} | You can send logs from your Node.js and JavaScript applications to an {{site.data.keyword.la_full_notm}} instance by using the Node.js library and adding a transport. </br></br>Valid transports are Winston and Bunyan. 
| `Ruby and Ruby on Rails` | [Ruby](https://github.com/logdna/ruby){: external} |  |
| `Go` | [Go](https://github.com/evalphobia/go-logdna){: external} | |
| `Java` | [Java](https://github.com/zileo-net/logback-logdna){: external} | |
| `PHP` | [PHP](https://github.com/nvanheuverzwijn/monolog-logdna){: external} | |
{: caption="Table 1. Code libraries" caption-side="top"}





