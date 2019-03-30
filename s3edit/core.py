import os
import boto3
import logging
import subprocess


logger = logging.getLogger(__name__)


def edit_file(path):
    editor = get_editor()
    logger.info(f'Editing with {editor}: {path}')
    subprocess.call([editor, path])


def get_editor():
    editor = os.environ.get('EDITOR')
    if not editor:
        editor = 'vi'
    return editor
