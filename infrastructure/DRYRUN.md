```
Acquiring state lock. This may take a few moments...
data.aws_iam_policy_document.assume_role: Reading...
data.aws_iam_policy_document.assume_role: Read complete after 0s [id=3552664922]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_eks_cluster.primary will be created
  + resource "aws_eks_cluster" "primary" {
      + arn                   = (known after apply)
      + certificate_authority = (known after apply)
      + cluster_id            = (known after apply)
      + created_at            = (known after apply)
      + endpoint              = (known after apply)
      + id                    = (known after apply)
      + identity              = (known after apply)
      + name                  = "eks_project"
      + platform_version      = (known after apply)
      + role_arn              = (known after apply)
      + status                = (known after apply)
      + tags_all              = (known after apply)
      + version               = (known after apply)

      + vpc_config {
          + cluster_security_group_id = (known after apply)
          + endpoint_private_access   = false
          + endpoint_public_access    = true
          + public_access_cidrs       = (known after apply)
          + subnet_ids                = [
              + "subnet-07360426ae2f30194",
              + "subnet-0e1dc35d985bafee2",
            ]
          + vpc_id                    = (known after apply)
        }
    }

  # aws_eks_node_group.primary will be created
  + resource "aws_eks_node_group" "primary" {
      + ami_type               = (known after apply)
      + arn                    = (known after apply)
      + capacity_type          = (known after apply)
      + cluster_name           = "eks_project"
      + disk_size              = (known after apply)
      + id                     = (known after apply)
      + instance_types         = [
          + "m5.large",
        ]
      + node_group_name        = "eks-project-node-group"
      + node_group_name_prefix = (known after apply)
      + node_role_arn          = (known after apply)
      + release_version        = (known after apply)
      + resources              = (known after apply)
      + status                 = (known after apply)
      + subnet_ids             = [
          + "subnet-0e1dc35d985bafee2",
        ]
      + tags_all               = (known after apply)
      + version                = (known after apply)

      + scaling_config {
          + desired_size = 1
          + max_size     = 5
          + min_size     = 1
        }
    }

  # aws_iam_role.eks will be created
  + resource "aws_iam_role" "eks" {
      + arn                   = (known after apply)
      + assume_role_policy    = jsonencode(
            {
              + Statement = [
                  + {
                      + Action    = "sts:AssumeRole"
                      + Effect    = "Allow"
                      + Principal = {
                          + Service = "eks.amazonaws.com"
                        }
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
      + create_date           = (known after apply)
      + force_detach_policies = false
      + id                    = (known after apply)
      + managed_policy_arns   = (known after apply)
      + max_session_duration  = 3600
      + name                  = "eks-cluster-role"
      + name_prefix           = (known after apply)
      + path                  = "/"
      + tags_all              = (known after apply)
      + unique_id             = (known after apply)
    }

  # aws_iam_role.nodegroup will be created
  + resource "aws_iam_role" "nodegroup" {
      + arn                   = (known after apply)
      + assume_role_policy    = jsonencode(
            {
              + Statement = [
                  + {
                      + Action    = "sts:AssumeRole"
                      + Effect    = "Allow"
                      + Principal = {
                          + Service = "ec2.amazonaws.com"
                        }
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
      + create_date           = (known after apply)
      + force_detach_policies = false
      + id                    = (known after apply)
      + managed_policy_arns   = (known after apply)
      + max_session_duration  = 3600
      + name                  = "eks-nodegroup-role"
      + name_prefix           = (known after apply)
      + path                  = "/"
      + tags_all              = (known after apply)
      + unique_id             = (known after apply)
    }

  # aws_iam_role_policy_attachment.primary_AmazonEC2ContainerRegistryReadOnly will be created
  + resource "aws_iam_role_policy_attachment" "primary_AmazonEC2ContainerRegistryReadOnly" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
      + role       = "eks-nodegroup-role"
    }

  # aws_iam_role_policy_attachment.primary_AmazonEKSClusterPolicy will be created
  + resource "aws_iam_role_policy_attachment" "primary_AmazonEKSClusterPolicy" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
      + role       = "eks-cluster-role"
    }

  # aws_iam_role_policy_attachment.primary_AmazonEKSVPCResourceController will be created
  + resource "aws_iam_role_policy_attachment" "primary_AmazonEKSVPCResourceController" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
      + role       = "eks-cluster-role"
    }

  # aws_iam_role_policy_attachment.primary_AmazonEKSWorkerNodePolicy will be created
  + resource "aws_iam_role_policy_attachment" "primary_AmazonEKSWorkerNodePolicy" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
      + role       = "eks-nodegroup-role"
    }

  # aws_iam_role_policy_attachment.primary_AmazonEKS_CNI_Policy will be created
  + resource "aws_iam_role_policy_attachment" "primary_AmazonEKS_CNI_Policy" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
      + role       = "eks-nodegroup-role"
    }

Plan: 9 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + endpoint                              = (known after apply)
  + kubeconfig-certificate-authority-data = (known after apply)
```
