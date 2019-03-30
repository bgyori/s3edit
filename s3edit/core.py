import os
import boto3
import logging
import botocore
import tempfile
import subprocess


logger = logging.getLogger(__name__)
client = boto3.client('s3')


def get_editor():
    editor = os.environ.get('EDITOR')
    if not editor:
        editor = 'vi'
    return editor


def load_from_s3(bucket, key):
    try:
        obj = client.get_object(Bucket=bucket, Key=key)
        acl = client.get_object_acl(Bucket=bucket, Key=key)
        acl.pop('ResponseMetadata')
    except client.exceptions.NoSuchKey as e:
        msg = f'In bucket {bucket}, the key {key} doesn\'t exist.'
        raise S3editError(msg)
    except client.exceptions.NoSuchBucket as e:
        msg = f'The bucket {bucket} doesn\'t exist.'
        raise S3editError(msg)
    content = obj['Body'].read().decode('utf8')
    return content, acl


def save_to_s3(bucket, key, content, acl):
    obj = content.encode('utf-8')
    client.put_object(Body=obj, Bucket=bucket, Key=key)
    client.put_object_acl(Bucket=bucket, Key=key, AccessControlPolicy=acl)


def bucket_key_from_path(path):
    parts = path.split('/')
    bucket = parts[0]
    key = '/'.join(parts[1:])
    return bucket, key


def edit_from_s3(path):
    bucket, key = bucket_key_from_path(path)
    content, acl = load_from_s3(bucket, key)
    prefix, suffix = os.path.splitext(key)
    content = edit_content(content, suffix)
    save_to_s3(bucket, key, content, acl)


def edit_content(content, suffix):
    suffix = suffix if suffix else '.tmp'
    editor = get_editor()
    name = None
    with tempfile.NamedTemporaryFile(suffix=suffix, mode='w',
                                     delete=False) as tf:
        name = tf.name
        tf.write(content)
        tf.flush()
        subprocess.call([editor, name])
        tf.close()
    with open(name, 'r') as fh:
        content = fh.read()
    return content


class S3editError(Exception):
    pass
