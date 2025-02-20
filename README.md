# Rick and Morty API APP

## Prerequisites

- Kubernetes cluster (Minikube or Kind)
- kubectl configured
- Docker image for `rick-and-morty-api` built and available

## Setup

1. **Build the Docker image** for your Flask application:
    ```bash
    docker build -t rick-and-morty-api .
    ```

2. **Push the Docker image** to your container registry (if using a cloud registry):
    ```bash
    docker push rick-and-morty-api:latest
    ```

    Or, if you're using Minikube or Kind, make sure your image is loaded into the local Docker daemon.

3. **Create the `yamls` directory**:
    Create the folder `yamls` and add the following manifests:
    - `Deployment.yaml`
    - `Service.yaml`
    - `Ingress.yaml`

4. ## Deploy To Kubernetes
    Apply the manifests to your Kubernetes cluster:
    ```bash
    kubectl apply -f yamls/Deployment.yaml
    kubectl apply -f yamls/Service.yaml
    kubectl apply -f yamls/Ingress.yaml
    ```

5. **Access the application**:
    - If you're using **Minikube**, you can use the following command to access the Ingress:
      ```bash
      minikube tunnel
      ```

    - If you're using **Kind**, ensure you set up an Ingress controller and access the application through the service IP.

    After deploying and exposing your application, you should be able to access the following endpoints:
    - `/healthcheck`: Health check endpoint for checking if the app is running.
    - `/characters/human`: Returns characters of species "Human".
    - `/characters/alive`: Returns characters with status "Alive".
    - `/characters/earth`: Returns characters from "Earth".

6. **Test the application**:
    You can test the endpoints using `curl` or Postman.

    Example with `curl`:
    ```bash
    curl http://rick-and-morty.local/healthcheck
    curl http://rick-and-morty.local/characters/human
    curl http://rick-and-morty.local/characters/alive
    curl http://rick-and-morty.local/characters/earth
    ```
7.  Rick and Morty API Helm Chart

## Helm Chart Installation

To install the chart:

```bash
helm install rick-and-morty-api ./helm/rick-and-morty-api

---
## To uninstall the chart:

```bash
helm uninstall rick-and-morty-api

---

## Endpoints

- **GET `/healthcheck`**: Returns the status of the application.
- **GET `/characters/human`**: Returns a list of characters of species "Human".
- **GET `/characters/alive`**: Returns a list of characters with status "Alive".
- **GET `/characters/earth`**: Returns a list of characters from Earth.
```
---

8. ## GitHub Actions Workflow

This repository contains a GitHub Actions workflow to test and deploy the Rick and Morty API.

### Workflow Steps:

1. Spin up a local Minikube cluster.
2. Build the Docker image and load it into Minikube.
3. Deploy the application using Helm.
4. Run tests on the deployed application.

To trigger the workflow, push changes to the `main` branch.


