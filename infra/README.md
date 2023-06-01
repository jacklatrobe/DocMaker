# INFRA - README

## Notes
You will need to replace <Your DigitalOcean API Token> with your actual DigitalOcean API token.

This configuration assumes that you have the DigitalOcean provider configured and that you want to use the latest 1.22.x version of Kubernetes. The digitalocean_kubernetes_versions data source is used to fetch the latest version that starts with "1.22.".

The node_pool block defines the nodes that will be part of the cluster. In this case, it creates a pool named "default" with 3 nodes of size s-2vcpu-2gb.

Please note that this is a basic configuration. Depending on your requirements, you might need to add more settings, like enabling auto-upgrades, setting up a maintenance window, or adding tags.

For deploying your Docker container to the Kubernetes cluster, you would typically define a Kubernetes Deployment and Service. However, this would require your Docker image to be available in a registry that your cluster can pull from. If you're planning to use the DigitalOcean Container Registry, you might want to look into the digitalocean_container_registry resource.