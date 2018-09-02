#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://naughty_string_validator_python.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='naughty_string_validator',
    version='0.1.0',
    description='A library that returns naughty strings from an offline database of Big List of Naughty Strings & emojis',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Shashi Kumar Raja',
    author_email='shashiraja92@gmail.com',
    url='https://github.com/shashikumarraja/naughty_string_validator_python',
    packages=[
        'naughty_string_validator',
    ],
    package_dir={'naughty_string_validator': 'naughty_string_validator'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='naughty_string_validator strings emoji',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
