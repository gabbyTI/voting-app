# Terraform EKS Deployment

This repository contains Terraform scripts for deploying an Amazon EKS cluster with associated resources. The configuration creates an EKS cluster, node group, and necessary IAM roles and policies.

## Table of Contents

- [Terraform EKS Deployment](#terraform-eks-deployment)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Resources](#resources)
  - [Outputs](#outputs)
  - [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Terraform](https://www.terraform.io/downloads.html) (v0.12+)
- [AWS CLI](https://aws.amazon.com/cli/) (configured with appropriate permissions)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Usage

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Initialize the Terraform configuration**:

   ```sh
   terraform init
   ```

3. **Generate and review the execution plan**:

   ```sh
   terraform plan
   ```

   The `terraform plan` command will generate an execution plan showing the actions Terraform will take to reach the desired state defined in the configuration files.

4. **Apply the execution plan**:

   ```sh
   terraform apply
   ```

   This command will create the specified resources in your AWS account.

## Resources

The following resources will be created by the Terraform configuration:

- **EKS Cluster**:

  - `aws_eks_cluster.primary`
    - Name: `eks_project`
    - Subnet IDs: `subnet-07360426ae2f30194`, `subnet-0e1dc35d985bafee2`

- **EKS Node Group**:

  - `aws_eks_node_group.primary`
    - Cluster Name: `eks_project`
    - Instance Type: `m5.large`
    - Desired Size: 1
    - Max Size: 5
    - Min Size: 1

- **IAM Roles**:

  - `aws_iam_role.eks`
    - Name: `eks-cluster-role`
    - Assume Role Policy: Allows `eks.amazonaws.com`
  - `aws_iam_role.nodegroup`
    - Name: `eks-nodegroup-role`
    - Assume Role Policy: Allows `ec2.amazonaws.com`

- **IAM Role Policy Attachments**:
  - `aws_iam_role_policy_attachment.primary_AmazonEKSClusterPolicy`
    - Role: `eks-cluster-role`
    - Policy ARN: `arn:aws:iam::aws:policy/AmazonEKSClusterPolicy`
  - `aws_iam_role_policy_attachment.primary_AmazonEKSVPCResourceController`
    - Role: `eks-cluster-role`
    - Policy ARN: `arn:aws:iam::aws:policy/AmazonEKSVPCResourceController`
  - `aws_iam_role_policy_attachment.primary_AmazonEKSWorkerNodePolicy`
    - Role: `eks-nodegroup-role`
    - Policy ARN: `arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy`
  - `aws_iam_role_policy_attachment.primary_AmazonEKS_CNI_Policy`
    - Role: `eks-nodegroup-role`
    - Policy ARN: `arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy`
  - `aws_iam_role_policy_attachment.primary_AmazonEC2ContainerRegistryReadOnly`
    - Role: `eks-nodegroup-role`
    - Policy ARN: `arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly`

## Outputs

The following outputs will be available after applying the Terraform plan:

- `endpoint`: The endpoint for the EKS cluster.
- `kubeconfig-certificate-authority-data`: The certificate authority data for the EKS cluster.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
