variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "climatesyncai"
}
