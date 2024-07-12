# Voting App Helm Charts

- [Voting App Helm Charts](#voting-app-helm-charts)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Customizing Deployment](#customizing-deployment)
    - [Namespace and Release Name](#namespace-and-release-name)
    - [Applications](#applications)
  - [Uninstallation](#uninstallation)
  - [Additional Notes](#additional-notes)
    - [CronJob for Autoscaling](#cronjob-for-autoscaling)

This repository contains Helm charts for deploying the Voting Microservice App on Kubernetes clusters using Helm.

## Prerequisites

Before you begin, ensure you have the following installed:

- Kubernetes cluster (e.g., EKS, AKS, GKE or Minikube)
- Helm v3 or later installed
- Access to your Kubernetes cluster with appropriate permissions

## Installation

To install the Voting App using Helm, follow these steps:

1. **Clone the Repository**: Clone the GitHub repository containing the Helm charts.

   ```bash
   git clone https://github.com/your-username/voting-app.git
   cd voting-app/voting-app-helm-chart
   ```

2. **Install the Chart**: Use Helm to install the chart with your preferred configuration values. For example:

   ```bash
   helm install my-release ./ --namespace my-namespace -f values.yaml
   ```

   Replace `my-release` with the name you want to give to your deployment, `./` with the path to your Helm chart directory (assuming you are already inside `voting-app-helm-chart`), `my-namespace` with your Kubernetes namespace, and `values.yaml` with your customized configuration values file if needed.

3. **Verify Installation**: Check that the application has been deployed successfully:

   ```bash
   kubectl get pods -n my-namespace
   ```

   Replace `my-namespace` with your Kubernetes namespace.

4. **Accessesing the application**: Vistion the following url on you local machine

   ```txt
   http//:localhost:31000 // Vote webpage
   http//:localhost:31001 // Result webpage
   ```

## Customizing Deployment

You can customize the deployment by modifying the `values.yaml` file. Here are the components you can configure:

### Namespace and Release Name

```yaml
namespace: voting-app
name: voting-app-microservices
```

### Applications

The `apps` section defines various microservices for your Voting App. Each app can be customized with the following parameters:

- `name`: Name of the microservice.
- `replicas`: Number of replicas to run.
- `containerPort`: Port on which the container listens.
- `isAutoScalable`: Whether Horizontal Pod Autoscaler (HPA) is enabled.
- `image.name` and `image.tag`: Docker image repository and tag/version.
- `service.enabled`: Whether to expose the service.
- `service.port` and `service.type`: Service port and type (ClusterIP, NodePort, LoadBalancer).
- `service.nodePort`: Node port if `service.type` is NodePort.
- `volume.enabled` and `volume.mountPath`: Whether to enable volumes and mount path.
- `hasEnv`: Whether the microservice requires environment variables.
- `env`: List of environment variables if `hasEnv` is `true`.

Here's an example configuration for the apps:

```yaml
apps:
  - name: vote
    replicas: 1
    containerPort: 80
    isAutoScalable: true
    image:
      name: dockersamples/examplevotingapp_vote
      tag: latest
    service:
      enabled: true
      port: 5000
      type: NodePort
      nodePort: 31000
    volume:
      enabled: false
      mountPath:
    hasEnv: false

  - name: result
    replicas: 1
    containerPort: 80
    isAutoScalable: false
    image:
      name: dockersamples/examplevotingapp_result
      tag: latest
    service:
      enabled: true
      port: 5001
      type: NodePort
      nodePort: 31001
    volume:
      enabled: false
      mountPath:
    hasEnv: false

  # Include other apps similarly
```

## Uninstallation

To uninstall/delete the deployment:

```bash
helm uninstall my-release -n my-namespace
```

Replace `my-release` and `my-namespace` with your deployment and namespace names, respectively.

## Additional Notes

### CronJob for Autoscaling

The repository also includes a CronJob (scale-vote-hpa-weekdays) for automatically scaling the vote microservice based on weekdays. This CronJob modifies the Horizontal Pod Autoscaler (HPA) configuration dynamically.

```yaml
cronjobs:
  - name: scale-vote-hpa-weekdays
    schedule: '0 0 * * *' # Everyday at 12 AM
    timeZone: 'America/New_York' # Specify the timezone for the CronJob
    image:
      name: gabbyti/scale-vote-hpa
      tag: latest
    restartPolicy: OnFailure
```
