#!/usr/bin/env python

import os

from setuptools import setup


root_dir = os.path.abspath(os.path.dirname(__file__))


PACKAGE = 'semantic_version'


setup(
    name=PACKAGE,
    version='0.1',
    author="Aleksei Slaikovskii",
    author_email="alexey@slaykovsky.com",
    description="A library that implements the basic semantic version scheme validation",
    license='BSD',
    keywords=['semantic version', 'versioning', 'version'],
    url='https://github.com/slaykovsky/python-version_checker',
    packages=['version_checker'],
    setup_requires=[
        'setuptools>=0.8',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests',
)
