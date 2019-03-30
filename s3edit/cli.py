import click
from .core import edit_from_s3


@click.command()
@click.argument('path')
def main(path):
    edit_from_s3(path)


if __name__ == '__main__':
    main()
