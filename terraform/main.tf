resource "aws_s3_bucket" "state_bucket" {
  bucket = "${var.project_name}-state-bucket"
  force_destroy = true
}

resource "aws_dynamodb_table" "lock_table" {
  name           = "terraform-locks"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}

resource "aws_instance" "app_instance" {
  ami                    = "ami-0c55b159cbfafe1f0" # Replace with latest Amazon Linux AMI
  instance_type          = var.instance_type

  tags = {
    Name = "${var.project_name}-app"
  }
}
