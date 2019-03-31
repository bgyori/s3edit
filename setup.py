from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()


def main():
    setup(name='s3edit',
          version='0.0.1',
          description='Edit files from S3 directly with your default editor.',
          long_description=long_description,
          author='Benjamin M. Gyori',
          author_email='ben.gyori@gmail.com',
          url='https://github.com/bgyori/s3edit',
          packages=['s3edit'],
          classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3 :: Only',
            ],
          install_requires=['boto3', 'click'],
          entry_points={'console_scripts': ['s3edit = s3edit.cli:main']}
          )


if __name__ == '__main__':
    main()
