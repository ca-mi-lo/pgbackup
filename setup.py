from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgpackup',
    version='0.1.0',
    author='Camilo Abboud',
    author_email='camilo.ab.sc@gmail.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='hhttps://github.com/ca-mi-lo/pgbackup',
    packages=find_packages('src')
)