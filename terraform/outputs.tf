output "instance_id" {
  value = aws_instance.app_instance.id
}

output "public_ip" {
  value = aws_instance.app_instance.public_ip
}
