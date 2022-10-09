output "sagemaker_role_arn" {
  value = aws_iam_role.sagemaker_admin.arn
}

output "lambda_role_arn" {
  value = aws_iam_role.lambda_sagemaker_access.arn
}
