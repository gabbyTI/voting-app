import datetime
import os
from kubernetes import client, config
from kubernetes.client.rest import ApiException

def scale_hpa():
    config.load_incluster_config()  # Load in-cluster Kubernetes config
    api_instance = client.AutoscalingV1Api()

    today = datetime.datetime.now().weekday()  # Monday is 0, Sunday is 6
    namespace = "voting-app"
    hpa_name = "vote"

    if today in [0, 1, 2, 3, 4]:  # Weekdays (Monday to Friday)
        target_replicas = 5  
    else:
        target_replicas = 1  # Weekend scale down example

    # Update HPA object
    try:
        hpa = api_instance.read_namespaced_horizontal_pod_autoscaler(hpa_name, namespace)
        hpa.spec.min_replicas = target_replicas
        hpa.spec.max_replicas = target_replicas * 2  
        api_instance.replace_namespaced_horizontal_pod_autoscaler(hpa_name, namespace, hpa)
    except ApiException as e:
        print(f"Exception when calling AutoscalingV1Api: {e}\n")

if __name__ == "__main__":
    scale_hpa()
