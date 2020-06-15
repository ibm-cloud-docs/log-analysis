

## Logs that are collected automatically
{: #kube_logs}

When a container running on Kubernetes writes its logs to stdout or stderr streams, the container engine streams them to the logging driver configured in Kubernetes. In most cases, these logs will end up in the /var/log/containers directory on your host.

STDOUT and STDERR logs are available through the `containerd.log` file.

The LogDNA agent collects the following log files from a worker (node):
* `syslog`: This file contain operating system (OS) events. 
* `auth.log`: This file includes information about the authentication requests that are made to the OS.


/var/log/kubelet.log - Kubelet, responsible for running containers on the node
/var/log/kube-proxy.log - Kube Proxy, responsible for service load balancing

IBM Cloud Kubernetes Service uses containerd as the container runtime to deploy containers from Docker container images into your cluster. 
 container logs for containerd are available under /var/log/pods.

The LogDNA agent collects the following log files from a container:
    container: Information that is logged by a running container.
    
    Paths: Anything that is written to STDOUT or STDERR.

    application: Information about events that occur at the application level. This could be a notification that an event took place such as a successful login, a warning about storage, or other operations that can be performed at the app level.
    
    Paths: You can set the paths that your logs are forwarded to. However, in order for logs to be sent, you must use an absolute path in your logging configuration or the logs cannot be read. If your path is mounted to your worker node, it might have created a symlink. Example: If the specified path is /usr/local/spark/work/app-0546/0/stderr but the logs actually go to /usr/local/spark-1.0-hadoop-1.2/work/app-0546/0/stderr, then the logs cannot be read.

    storage: Information about persistent storage that is set up in your cluster. Storage logs can help you set up problem determination dashboards and alerts as part of your DevOps pipeline and production releases. 
    
    Note: The paths /var/log/kubelet.log and /var/log/syslog also contain storage logs, but logs from these paths are collected by the kubernetes and worker log sources.
    Paths:
        /var/log/ibmc-s3fs.log
        /var/log/ibmc-block.log

   Pods: * portworx-*** * ibmcloud-block-storage-attacher-*** * ibmcloud-block-storage-driver-*** * ibmcloud-block-storage-plugin-*** * ibmcloud-object-storage-plugin-***

    kubernetes: Information from the kubelet, the kube-proxy, and other Kubernetes events that happen in the kube-system namespace of the worker node.
    Paths:
        /var/log/kubelet.log
        /var/log/kube-proxy.log
        /var/log/event-exporter/1..log

    kube-audit: Information about cluster-related actions that is sent to the Kubernetes API server, including the time, the user, and the affected resource.

    ingress: Information about the network traffic that comes into a cluster through the Ingress ALB.
    Paths:
        /var/log/alb/ids/*.log
        /var/log/alb/ids/*.err
        /var/log/alb/customerlogs/*.log
        /var/log/alb/customerlogs/*.err

Logging and monitoring Ingress   https://cloud.ibm.com/docs/containers?topic=containers-ingress_health


| Log source          | LogDNA App value         | File | 
|---------------------|--------------------------|-----------------------------------|
| `syslog`            | 
| `0.log`             |
| `containerd`        | `containerd.log`         | `/var/log/containerd.log`         |
| `kubelet`           | `kubelet.log`            | `/var/log/kubelet.log`            |
| `kube-proxy`        | `kube-proxy.log`         | `/var/log/kube-proxy.log`         |
| `event-exporter`    | `  `                     | `/var/log/event-exporter/1..log`   |
| `ingress-auth-<xxxx>` | 
| `nginx-ingress`     |    
| `Kubernetes-dashboard` | 
| `customerLogAccess_public<xxxx>` |
| `customerError_public<xxxx>`     |
| `   `                | `auth.log` |


Kern.log
History.log
Term.log
Dpkg.log
Vpn
Sysdig-agent
Olm-operator
Metrics-server-nanny
Metrics-server
Logdna-agent
Keepalived-watcher
Install-cni
Ibm-storage-watcher-container
Ibm-master-proxy-static
Ibm-file-plugin-container
Ibm-cloud-provider-ip
Dashboard-metrics-scraper
Catalog-operator
Calico-node. (high number of log entries) INFO/
Calico-kube-controllers. (info/warn/ERROR)
Calico-extension
Autoscaler


