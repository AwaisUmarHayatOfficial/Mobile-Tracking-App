#  Kubernetes Installation Guide on Ubuntu 24.04

This document provides a complete step-by-step guide to install and configure a **Kubernetes cluster** on Ubuntu 24.04 using:

- kubeadm
- kubelet
- kubectl
- containerd
- Calico CNI

This setup is suitable for:

✅ DevOps labs  
✅ Vagrant environments  
✅ On-prem clusters  
✅ Learning Kubernetes  
✅ Production-like testing  

---

# Cluster Topology (Example)

| Role   | Hostname           | Example IP      |
|--------|-------------------|---------------|
| Master | k8s-master-node   | 192.168.56.10 |
| Worker | k8s-worker-node-1 | 192.168.56.11 |
| Worker | k8s-worker-node-2 | 192.168.56.12 |

---

# Step 1 — Configure Hostnames (All Nodes)

## Edit hosts file
```bash
sudo nano /etc/hosts
````

Add:

```bash
192.168.56.10 k8s-master-node
192.168.56.11 k8s-worker-node-1
192.168.56.12 k8s-worker-node-2
```

---

## Set hostname

### Master

```bash
sudo hostnamectl set-hostname k8s-master-node
```

### Worker 1

```bash
sudo hostnamectl set-hostname k8s-worker-node-1
```

### Worker 2

```bash
sudo hostnamectl set-hostname k8s-worker-node-2
```

Reload shell:

```bash
exec bash
```

Verify:

```bash
hostname
```

Test connectivity:

```bash
ping -c 3 k8s-worker-node-1
ping -c 3 k8s-worker-node-2
```

---

# Step 2 — Disable Swap (All Nodes)

Kubernetes requires swap to be disabled.

Temporarily disable:

```bash
sudo swapoff -a
```

Make permanent:

```bash
sudo nano /etc/fstab
```

Comment swap line:

```
# /swapfile none swap sw 0 0
```

Verify:

```bash
swapon --show
```

(No output means swap is disabled)

---

# Step 3 — Load Required Kernel Modules

```bash
sudo modprobe overlay
sudo modprobe br_netfilter
```

Persist after reboot:

```bash
sudo tee /etc/modules-load.d/k8s.conf <<EOF
overlay
br_netfilter
EOF
```

---

# Step 4 — Configure Networking

```bash
sudo nano /etc/sysctl.d/k8s.conf
```

Add:

```bash
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
```

Apply:

```bash
sudo sysctl --system
```

---

# Step 5 — Install Docker + Containerd

```bash
sudo apt update
sudo apt install docker.io -y
```

Enable services:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

---

## Configure containerd

Create config:

```bash
sudo mkdir /etc/containerd
sudo sh -c "containerd config default > /etc/containerd/config.toml"
```

Enable SystemdCgroup:

```bash
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
```

Restart:

```bash
sudo systemctl restart containerd
sudo systemctl status containerd
```

---

# Step 6 — Install Kubernetes Components

Install dependencies:

```bash
sudo apt-get install curl ca-certificates apt-transport-https -y
```

Add GPG key:

```bash
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key \
| sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

Add repository:

```bash
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /" \
| sudo tee /etc/apt/sources.list.d/kubernetes.list
```

Install Kubernetes tools:

```bash
sudo apt update
sudo apt install kubelet kubeadm kubectl -y
```

---

# Step 7 — Initialize the Master Node

```bash
sudo kubeadm init --pod-network-cidr=10.10.0.0/16
```

---

## Configure kubectl for current user

```bash
mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Test:

```bash
kubectl get nodes
```

---

# Step 8 — Install Calico CNI Plugin

Install operator:

```bash
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/tigera-operator.yaml
```

Download config:

```bash
curl https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/custom-resources.yaml -O
```

Update CIDR:

```bash
sed -i 's/cidr: 192\.168\.0\.0\/16/cidr: 10.10.0.0\/16/g' custom-resources.yaml
```

Apply:

```bash
kubectl create -f custom-resources.yaml
```

---

# Step 9 — Join Worker Nodes

Run the join command generated during `kubeadm init`:

```bash
kubeadm join <MASTER-IP>:6443 --token <TOKEN> \
--discovery-token-ca-cert-hash sha256:<HASH>
```

Verify:

```bash
kubectl get nodes
```

---

#  Step 10 — Test the Cluster

Create namespace:

```bash
kubectl create namespace demo-namespace
```

Deploy nginx:

```bash
kubectl create deployment my-app --image nginx --replicas 2 -n demo-namespace
```

Expose service:

```bash
kubectl expose deployment my-app -n demo-namespace --type NodePort --port 80
```

Check:

```bash
kubectl get svc -n demo-namespace
```

Test access:

```bash
curl http://<worker-ip>:<nodeport>
```

---

#  Useful Commands

```bash
kubectl get nodes
kubectl get pods -A
kubectl get svc
kubectl logs <pod>
kubectl describe pod <pod>
kubectl delete -f manifest.yaml
```

---


# Maintainer

GitHub: [https://github.com/awaisumarhayatofficial](https://github.com/awaisumarhayatofficial)

---

