---

copyright:
  years:  2018, 2024
lastupdated: "2024-05-24"

keywords: IBM, Log Analysis, logging, agent update

subcollection: log-analysis

---

{{site.data.keyword.attribute-definition-list}}

# Configuring how logging agent updates are rolled
{: #log_analysis_agent_updates}

When you configure a logging agent, auto update of the logging agent is enabled. You might find this behavior acceptable for a proof of concept or for a development environment. However, for production environments, and for regulated, and highly available workloads, you might need to control when to update the logging agent.
{: shortdesc}


{{../_include-segments/deprecation_notice.md}}

For Linux log sources, you can configure the **autoupdate** parameter to configure how you want updates to the agent to be rolled.

For Kubernetes clusters, you can configure the YAML file to configure how you want updates to the agent to be rolled.


## Customize a Linux agent
{: #log_analysis_agent_updates_linux}



## Customize a standard Kubernetes cluster agent
{: #log_analysis_agent_updates_std_kube}

When you configure a logging agent by using the default standard Kubernetes cluster configuration YAML file, auto updates of the logging agent are enabled.

The default YAML configuration is set as follows:

```yaml
updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 100%
```
{: screen}


A Deployment’s rollout is triggered if and only if the Deployment’s Pod template (that is, .spec.template) is changed, for example if the labels or container images of the template are updated. Other updates, such as scaling the Deployment, do not trigger a rollout.

Rolling updates allow Deployments’ update to take place with zero downtime by incrementally updating Pods instances with new ones. The new Pods will be scheduled on Nodes with available resources.

Okay, now for the fix. The fix is pretty easy actually. This happens because kubernetes doesn’t know when your new pod is ready to start accepting requests, so as soon as your new pod gets created, the old pod is terminated without waiting to see if all the necessary services, processes have started in the new pod which would then enable it to receive requests.

To do this, Kubernetes provide a config option in deployment called Readiness Probe. Readiness Probe makes sure that the new pods created are ready to take on requests before terminating the old pods. To enable this, first you need to have a route in whatever the application you want to run which would return a 200 on an HTTP GET request. (Note: you can have other HTTP request methods as well, but for this post, I’m sticking with GET method)

## Customize an OpenShift Kubernetes cluster agent
{: #log_analysis_agent_updates_os_kube}


When you configure a logging agent by using the default OpenShift Kubernetes cluster configuration YAML file, auto updates of the logging agent are enabled.

The default YAML configuration is set as follows:

```yaml
updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 100%
```
{: screen}
