#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Publish shortcut.
if sys.argv[-1] == "publish":
    os.system('python setup.py sdist upload')
    sys.exit()


required = [
    'zope.interface==3.7.0',
    'clint==0.2.4'
]


if sys.version_info[0:2] < (2, 6):
    required.append('simplejson')

setup(
    name='sshout',
    version='0.0.0',
    description='SSH it up.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/sshout',
    packages= ['sshout'],
    install_requires=required,
    license='ISC',
    classifiers=(
#       'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
    entry_points = {
        'console_scripts': [
            'sshout = sshout.cli:main',
            'tmpsshd = sshout.tmpsshd:main',
        ]
    }
)
