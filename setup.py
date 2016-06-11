# setup.py
#
# Copyright 2015 Socos LLC
#

import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='emailsms',
    packages=['emailsms'],
    version='0.2',
    license='Apache License 2.0',
    description='Send text messages using email SMS gateways.',
    long_description=(read('README.rst')),
    author='Brandon Istenes',
    author_email='bistenes@socos.me',
    url='https://bitbucket.org/socos_me/emailsms',
    download_url='https://bitbucket.org/socos_me/emailsms/get/0.2.tar.gz',
    keywords=['sms', 'texting', 'phone', 'gateway', 'email'],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: Apache Software License']
)
