resource "local_file" "sagemaker_role_arn" {
  content  = aws_iam_role.sagemaker_admin.arn
  filename = "sagemaker-role-arn.txt"
}

resource "local_file" "lambda_role_arn" {
  content  = aws_iam_role.lambda_sagemaker_access.arn
  filename = "lambda-role-arn.txt"
}
