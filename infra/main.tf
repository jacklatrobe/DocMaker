provider "digitalocean" {
  token = "<Your DigitalOcean API Token>"
}

data "digitalocean_kubernetes_versions" "main" {
  version_prefix = "1.22."
}

resource "digitalocean_kubernetes_cluster" "cluster" {
  name   = "DocMaker-cluster"
  region = "nyc1"

  version = data.digitalocean_kubernetes_versions.main.latest_version

  node_pool {
    name       = "default"
    size       = "s-2vcpu-2gb"
    node_count = 3
  }
}
