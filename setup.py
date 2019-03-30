from setuptools import setup


def main():
    setup(name='s3edit',
          version='0.0.1',
          description='Edit files from S3 directly with your default editor.',
          author='Benjamin M. Gyori',
          author_email='ben.gyori@gmail.com',
          url='https://github.com/bgyori/s3edit',
          packages=['s3edit'],
          install_requires=['boto3', 'click'],
          entry_points={'console_scripts': ['s3edit = s3edit.cli:main']}
          )


if __name__ == '__main__':
    main()
