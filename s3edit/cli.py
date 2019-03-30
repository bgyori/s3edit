import sys
import click
import logging
from .core import edit_from_s3, S3editError


logger = logging.getLogger('s3edit')


@click.command()
@click.argument('path')
def main(path):
    try:
        edit_from_s3(path)
    except S3editError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
