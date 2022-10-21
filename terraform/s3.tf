
resource "aws_s3_bucket" "dkneipp_sagemaker" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_acl" "dkneipp_sagemaker" {
  bucket = aws_s3_bucket.dkneipp_sagemaker.id
  acl    = "private"
}
