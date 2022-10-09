data "aws_iam_policy_document" "sagemaker_assumerole" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["sagemaker.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "sagemaker_admin" {
  name               = "sagemaker-admin"
  assume_role_policy = data.aws_iam_policy_document.sagemaker_assumerole.json
}

data "aws_iam_policy" "AmazonSageMakerFullAccess" {
  name = "AmazonSageMakerFullAccess"
}

resource "aws_iam_role_policy_attachment" "sagemaker" {
  role       = aws_iam_role.sagemaker_admin.name
  policy_arn = data.aws_iam_policy.AmazonSageMakerFullAccess.arn
}

data "aws_iam_policy_document" "lambda_assumerole" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy" "AWSLambdaBasicExecutionRole" {
  name = "AWSLambdaBasicExecutionRole"
}

data "aws_iam_policy_document" "lambda_access_sagemaker" {
  statement {
    actions   = ["sagemaker:InvokeEndpoint"]
    resources = ["*"]
    sid       = "AllowSagemakerInvokeEndpoint"
  }
}

resource "aws_iam_policy" "lambda_access_sagemaker" {
  name   = "lambda-access-sagemaker"
  policy = data.aws_iam_policy_document.lambda_access_sagemaker.json
}

resource "aws_iam_role" "lambda_sagemaker_access" {
  name               = "lambda-sagemaker-access"
  assume_role_policy = data.aws_iam_policy_document.lambda_assumerole.json
}

resource "aws_iam_role_policy_attachment" "lambda_default" {
  role       = aws_iam_role.lambda_sagemaker_access.name
  policy_arn = data.aws_iam_policy.AWSLambdaBasicExecutionRole.arn
}

resource "aws_iam_role_policy_attachment" "lambda_sagemaker_access" {
  role       = aws_iam_role.lambda_sagemaker_access.name
  policy_arn = aws_iam_policy.lambda_access_sagemaker.arn
}
