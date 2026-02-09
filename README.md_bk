# 🚀 GitHub Actions CI/CD with Kubernetes Deployment

Automate your CI/CD pipeline using GitHub Actions and deploy your application seamlessly to a Kubernetes cluster.

## Introduction

This repository showcases a containerized full-stack application featuring an HTML/CSS frontend and a Laravel backend. It demonstrates a robust CI/CD pipeline built with GitHub Actions, which automates the Docker image building process, pushes them to Docker Hub, and executes seamless deployments to a Kubernetes cluster (via a self-hosted runner). This setup serves as a guide for automating multi-service deployments and maintaining application synchronization.

## Prerequisites

Before you begin, make sure you have the following installed and set up:

- **Git**: For cloning and managing repositories.
- **Docker**: To build and manage container images.
- **php-laravel**: For running the backend application.
- **kubectl**: Kubernetes command-line tool to interact with your cluster.
- **A Kubernetes Cluster**:A multi-node cluster consisting of one Master Node and one Worker Node (configured via Vagrant/Local environment).
- **GitHub Account**: To clone the repository and set up GitHub Actions.
- **Docker Hub Account**: To push Docker images.

## Getting Started

### 1. Clone the Repository

#### **Option A: clone the Repository**

1. Navigate to the [repository](https://github.com/AwaisUmarHayatOfficial/Mobile-Tracking-App.git).

#### **Option B: Clone the Repository**

```bash
git clone https://github.com/AwaisUmarHayatOfficial/Mobile-Tracking-App.git
```

Change directory into the project folder:

```bash
cd Mobile-Tracking-App
```

### 2. Project Structure

Here's the layout of the repository:

```
github-actions-kubernetes/
├── .github/
│   └── workflows/
│       └── ci-cd.yaml          # GitHub Actions workflow
├── .gitignore                  # Files and directories to ignore in Git
├── .git                        
├── README.md                   # Project documentation
├── frontend                    # Frontend application
│   └── html/                   # Project Code
│   └── Dockerfile              # Containerized Frontend application
├── backend                     # Backend application
│   └── app/                    # Project Code
│   └── src
│   └── Dockerfile              # Containerized backend application
├── Vagrantfile
├── frontend-deployment.yaml    # Kubernetes Frontend Deployment manifest
├── frontend-service.yaml       # Kubernetes Frontend Service manifest
├── backend-deployment.yaml     # Kubernetes Backend Deployment manifest
├── backend-service.yaml        # Kubernetes Backend Service manifest
├── redis-deployment.yaml       # Kubernetes Redis Deployment manifest
├── redis-service.yaml          # Kubernetes Redis Service manifest

```

### 3. Configure Docker and Kubernetes Secrets

#### **Docker Hub**

1. **Log In to Docker Hub:**

   ```bash
   docker login
   ```

2. **Create a Personal Access Token (Recommended):**

  - Go to Docker Hub > **Account Settings** > **Security**.
  - Click **New Access Token**, name it, and copy the token.

#### **Kubernetes Config**

1. **Get Your Kubeconfig File:**

  - Typically located at `$HOME/.kube/config`.

2. **Base64 Encode the Kubeconfig:**

   ```bash
   cat $HOME/.kube/config | base64 | pbcopy  # For macOS
   ```

   **Note:** On Windows, you can use:

   ```bash
   type %USERPROFILE%\.kube\config | base64 | clip
   ```

### 4. Set Up GitHub Actions Secrets

1. **Navigate to Your Forked Repository on GitHub.**

2. **Go to Settings > Secrets and variables > Actions.**

3. **Add the Following Secrets:**

  - **`DOCKERHUB_USERNAME`**: Your Docker Hub username.
  - **`DOCKERHUB_TOKEN`**: Your Docker Hub password or access token.
  - **`KUBE_CONFIG_DATA`**: The base64 encoded kubeconfig file.

## Usage

### 1. Build and Push Docker Image

**Note:** The GitHub Actions workflow will automate these steps, but you can also do them manually.

#### **Build the Docker Image:**

```bash
docker build -t awaisumarhayatofficial/frontend:latest .
docker build -t awaisumarhayatofficial/backend:latest .
```

#### **Push the Image to Docker Hub:**

```bash
docker push awaisumarhayatofficial/frontend:latest
docker push awaisumarhayatofficial/backend:latest
```

### 2. Deploy to Kubernetes

**Apply Kubernetes Manifests:**

```bash
kubectl apply -f frontend-deployment.yaml    
kubectl apply -f frontend-service.yaml   
kubectl apply -f backend-deployment.yaml 
kubectl apply -f backend-service.yaml    
kubectl apply -f redis-deployment.yaml   
kubectl apply -f redis-service.yaml
```
   

### 3. Test the Application

1. **Get the Service IP:**

   ```bash
   kubectl get services
   ```

2. **Access the Application:**

  - Navigate to the external IP in your browser.
  - http://192.168.56.10:30080
  - http://192.168.56.10:30001

## Step-by-Step Commands

Here's a consolidated list of commands to set up and run the project.

### **Clone the Repository**

```bash
git clone https://github.com/AwaisUmarHayatOfficial/Mobile-Tracking-App.git
cd Mobile-Tracking-App
```

### **Install Dependencies**

All dependencies are already configured inside the Docker containers.
No manual installation is required on local system.

### **Run the Application Locally**

Start the application using Dockerized the application:
```bash

docker compose up --build
OR
cd Mobile-Tracking-App
sudo docker compose up -d --build
```

### **Run the Docker Container Locally**

```bash

docker run -dit --name frontend -p 80:80 awaisumarhayatofficial/frontend:latest
docker run -dit --name backend -p 80:8000 awaisumarhayatofficial/backend:latest
```
#### Verify

Visit `http://localhost:8000` to test backend app.
Visit `http://localhost:80` to test frontend app.

### **Build the Docker Image**

```bash

docker build -t awaisumarhayatofficial/frontend:latest .

docker build -t awaisumarhayatofficial/backend:latest .

```

### **Push the Docker Image**

```bash
docker push awaisumarhayatofficial/frontend:latest
docker push awaisumarhayatofficial/backend:latest
```

### **Deploy to Kubernetes**

```bash
cd ~/Mobile-Tracking-App

kubectl apply -f frontend-deployment.yaml    
kubectl apply -f frontend-service.yaml   
kubectl apply -f backend-deployment.yaml 
kubectl apply -f backend-service.yaml    
kubectl apply -f redis-deployment.yaml   
kubectl apply -f redis-service.yaml

```

### **Check Deployment Status**

```bash
kubectl get deployments
kubectl get services
kubectl get pods
kubectl get svc
```

### **Set Up GitHub Actions Secrets**

1. **Access Repository Settings on GitHub.**

2. **Add Secrets:**

  - **DOCKERHUB_USERNAME**
  - **DOCKERHUB_TOKEN**
  - **KUBE_CONFIG_DATA**

### **Trigger GitHub Actions Workflow**

- **Push Changes to GitHub:**

  ```bash
  git add .
  git commit -m "Your commit message"
  git push origin main
  ```

- The GitHub Actions workflow will automatically run on pushes to the `main` branch.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

### **Steps to Contribute:**

1. **Fork the Repository.**

2. **Create a New Branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes and Commit:**

   ```bash
   git commit -m "Add your message"
   ```

4. **Push to Your Forked Repository:**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request on GitHub.**

---

**Note:** Replace `your-username` and `your-dockerhub-username` with your actual GitHub and Docker Hub usernames respectively.
---

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Docker Documentation](https://docs.docker.com/)

---
