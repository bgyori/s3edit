import sys
from .core import edit_from_s3


if __name__ == '__main__':
    path = sys.argv[1]
    edit_from_s3(path)
