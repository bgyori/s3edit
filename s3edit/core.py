import os
import boto3
import logging
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
    obj = client.get_object(Bucket=bucket, Key=key)
    content = obj['Body'].read().decode('utf8')
    return content


def save_to_s3(bucket, key, content):
    obj = content.encode('utf-8')
    client.put_object(Body=obj, Bucket=bucket, Key=key)


def bucket_key_from_path(path):
    parts = path.split('/')
    bucket = parts[0]
    key = '/'.join(parts[1:])
    return bucket, key


def edit_from_s3(path):
    bucket, key = bucket_key_from_path(path)
    content = load_from_s3(bucket, key)
    prefix, suffix = os.path.splitext(key)
    content = edit_content(content, suffix)
    save_to_s3(bucket, key, content)


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
