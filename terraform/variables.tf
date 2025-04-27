variable "aws_region" {
  description = "Region where AWS resources will be created"
  type        = string
  default     = "eu-north-1"
}

variable "aws_access_key" {
  description = "AWS Access Key"
  type        = string
}

variable "aws_secret_key" {
  description = "AWS Secret Access Key"
  type        = string
  sensitive   = true
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnet_a_cidr" {
  description = "CIDR block for the first subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "subnet_b_cidr" {
  description = "CIDR block for the second subnet"
  type        = string
  default     = "10.0.2.0/24"
}

variable "availability_zone_a" {
  description = "Availability Zone for the first subnet"
  type        = string
  default     = "eu-north-1a"
}

variable "availability_zone_b" {
  description = "Availability Zone for the second subnet"
  type        = string
  default     = "eu-north-1b"
}

variable "cluster_name" {
  description = "Name of the EKS cluster"
  type        = string
  default     = "test-k8s-cluster"
}

variable "node_group_name" {
  description = "Name of the EKS Node Group"
  type        = string
  default     = "test-node-group"
}

variable "desired_size" {
  description = "Desired number of nodes in the Node Group"
  type        = number
  default     = 2
}

variable "max_size" {
  description = "Maximum number of nodes in the Node Group"
  type        = number
  default     = 3
}

variable "min_size" {
  description = "Minimum number of nodes in the Node Group"
  type        = number
  default     = 1
}

variable "namespace" {
  description = "Name of the Kubernetes namespace"
  type        = string
  default     = "test-app-namespace"
}
