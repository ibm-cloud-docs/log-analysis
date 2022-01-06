---

copyright:
  years: 2019, 2022
lastupdated: "2021-09-30"

keywords: IBM Cloud, Log Analysis, API, troubleshooting

subcollection: log-analysis

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Are you getting an Invalid JSON error when running a cURL command on Windows?
{: #troubleshoot-04}
{: troubleshoot}
{: support} 

If the API method requires data passed using `-d`, and you are running a cURL command from a Windows command prompt, the data passed must be passed in a file, not on the command.
{: shortdesc}

The API request fails and the response returns a JSON error.
{: tsSymptoms}

Windows requires data passed on a cURL command to be passed in a file, rather than on the command itself.
{: tsCauses}

For example, the following command cannot be run as shown from a Windows command prompt:

```text
curl --request POST https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream -H "content-type: application/json" -H "servicekey: 0000000aaaa000000bbb00000ccc" -d '{"brokers":["kafka-0.mh-svc1-0000.eu-de.containers.appdomain.cloud:9093","kafka-1.mh-sv2.eu-de.containers.appdomain.cloud:9093","kafka-2.mh-sv3.eu-de.containers.appdomain.cloud:9093"],"topic":"la-dallas-topic","user":"token","password":"0000000_aaaa00000_0bbb00000ccc"}'
```
{: pre}

Place the data to be passed on the `-d` parameter in a file and then pass the file to the command instead.
{: tsResolve}

In the previous example, create a file named `data.json` in the directory where you are running the cURL command with the following data:

```json
{"brokers":["kafka-0.mh-svc1-0000.eu-de.containers.appdomain.cloud:9093","kafka-1.mh-sv2.eu-de.containers.appdomain.cloud:9093","kafka-2.mh-sv3.eu-de.containers.appdomain.cloud:9093"],"topic":"la-dallas-topic","user":"token","password":"0000000_aaaa00000_0bbb00000ccc"}
```
{: codeblock}

Then pass the file on the cURL command as follows: 

```text
curl --request POST https://api.eu-gb.logging.cloud.ibm.com/v1/config/stream -H "content-type: application/json" -H "servicekey: 0000000aaaa000000bbb00000ccc" -d @data.json
```
{: pre} 


