---

copyright:
  years:  2018
lastupdated: "2018-11-02"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:pre: .pre}
{:table: .aria-labeledby="caption"}
{:codeblock: .codeblock}
{:tip: .tip}
{:download: .download}

 
# Configuring network traffic in a Kubernetes cluster for custom firewall configurations in the {{site.data.keyword.Bluemix_notm}}
{: #network}

When you have an additional firewall set up, or you have customized the firewall settings in your {{site.data.keyword.Bluemix_notm}} infrastructure (SoftLayer), you need to allow outgoing network traffic from the worker node to the {{site.data.keyword.loganalysisshort}} service. 
{:shortdesc}





You must open TCP port 443 and TCP port 9091 from each worker to the {{site.data.keyword.loganalysisshort}} service for the following IP addresses in your customized firewall:

<table>
  <tr>
    <th>Region</th>
    <th>Ingestion URL</th>
	<th>Public IP addresses</th>
  </tr>
  <tr>
    <td>Germany</td>
	<td>ingest-eu-fra.logging.bluemix.net</td>
	<td>158.177.88.43 <br>159.122.87.107</td>
  </tr>
  <tr>
    <td>United Kingdom</td>
	<td>ingest.logging.eu-gb.bluemix.net</td>
	<td>169.50.115.113</td>
  </tr>
  <tr>
    <td>US South</td>
	<td>ingest.logging.ng.bluemix.net</td>
	<td>169.48.79.236 <br>169.46.186.113</td>
  </tr>
  <tr>
    <td>Sydney</td>
	<td>ingest-au-syd.logging.bluemix.net</td>
	<td>130.198.76.125 <br>168.1.209.20</td>
  </tr>
</table>