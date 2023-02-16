
resource "aws_s3_bucket" "bucket_sagemaker" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_acl" "bucket_sagemaker" {
  bucket = aws_s3_bucket.bucket_sagemaker.id
  acl    = "private"
}
