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
