#!/usr/bin/env python2.7
from distutils.core import setup
from email_merger import PROG_VERSION_NUMERIC, PROG_NAME

setup(name='email_merger',
    version=PROG_VERSION_NUMERIC,
    author='Laurence Tratt',
    author_email='laurie@tratt.net',
    url='https://github.com/ltratt/email_merger',
    scripts=['email_merger.py'],
)
