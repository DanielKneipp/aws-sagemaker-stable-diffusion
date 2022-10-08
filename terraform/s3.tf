
resource "aws_s3_bucket" "dkneipp_sagemaker" {
  bucket = "dkneipp-sagemaker"
}

resource "aws_s3_bucket_acl" "dkneipp_sagemaker" {
  bucket = aws_s3_bucket.dkneipp_sagemaker.id
  acl    = "private"
}
