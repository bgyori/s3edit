import sys
from .core import edit_file


if __name__ == '__main__':
    path = sys.argv[1]
    edit_file(path)
