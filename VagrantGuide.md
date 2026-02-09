#  Vagrant Kubernetes Lab Setup

This document describes a **Vagrant-based lab environment** for Kubernetes on Ubuntu 24.04.  

It includes:

- One **Master Node**
- One **Worker Node**
- Private networking
- Port forwarding for services
- Resource allocation (CPU & RAM)

---

#  Vagrantfile Overview

Vagrant is configured with **`bento/ubuntu-24.04`** box and VirtualBox provider.  

Each VM has:

- Static private IP
- Hostname
- Resource allocation
- Port forwarding for testing services

---

#  Master Node Configuration

```ruby
config.vm.define "MasterNode" do |master|
  master.vm.box = "bento/ubuntu-24.04"
  master.vm.hostname = "MasterNode"
  master.vm.network "private_network", ip: "192.168.56.10"

  # Port Forwarding (Guest → Host)
  master.vm.network "forwarded_port", guest: 80, host: 8080
  master.vm.network "forwarded_port", guest: 8080, host: 8081

  master.vm.provider "virtualbox" do |vb|
    vb.name = "Master Node"
    vb.memory = 4096
    vb.cpus = 2
  end
end
````

**Explanation:**

* `hostname`: Sets the VM's hostname.
* `private_network`: Assigns a static IP for communication with worker nodes.
* `forwarded_port`: Maps guest ports to host ports for accessing services.
* `provider`: Allocates **2 CPUs** and **4GB RAM** to ensure Kubernetes can run smoothly.

---

#  Worker Node Configuration

```ruby
config.vm.define "WorkerNode" do |worker|
  worker.vm.box = "bento/ubuntu-24.04"
  worker.vm.hostname = "WorkerNode"
  worker.vm.network "private_network", ip: "192.168.56.11"

  # Port Forwarding
  worker.vm.network "forwarded_port", guest: 8080, host: 8090
  worker.vm.network "forwarded_port", guest: 80, host: 8091

  worker.vm.provider "virtualbox" do |vb|
    vb.name = "Worker Node"
    vb.memory = 4096
    vb.cpus = 2
  end
end
```

**Explanation:**

* Uses the same Ubuntu box as Master node.
* Static private IP `192.168.56.11`.
* Port forwarding mapped to **different host ports** to avoid conflicts.
* Same resource allocation as Master.

---

#  Network Topology

```
Host Machine
 ├─ MasterNode (192.168.56.10)
 │    └─ Kubernetes Master
 └─ WorkerNode (192.168.56.11)
      └─ Kubernetes Worker
```

* **Private network** allows communication between Master & Worker.
* Port forwarding enables testing services from host browser or curl.

---

#  How to Bring Up the Vagrant Lab

1. Navigate to the directory with your `Vagrantfile`.
2. Run:

```bash
vagrant up
```

* This will start both Master and Worker nodes.

3. SSH into nodes:

```bash
vagrant ssh MasterNode
vagrant ssh WorkerNode
```

---

#  Recommended Resource Allocation

| Node   | CPU | RAM |
| ------ | --- | --- |
| Master | 2   | 4GB |
| Worker | 2   | 4GB |

* Enough for small Kubernetes labs.
* Can be increased for heavier workloads.

---

#  Notes

* This setup is ideal for **learning Kubernetes, testing deployments, and CI/CD experiments**.
* Both nodes are **persistent**, so cluster config remains after reboot.
* Port forwarding allows easy access to services from the host machine.

---

#  Maintainer

GitHub: [https://github.com/awaisumarhayatofficial](https://github.com/awaisumarhayatofficial)


---

