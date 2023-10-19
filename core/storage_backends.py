from storages.backends.s3boto3 import S3Boto3Storage

class Static(S3Boto3Storage):
    location = 'static'
    default_acl = 'private'

class classname(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
