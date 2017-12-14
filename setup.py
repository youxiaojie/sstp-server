#!/usr/bin/env python3
from __future__ import print_function
import sys
from setuptools import setup, Extension

from sstpd import __version__ as version


if sys.version_info < (3, 4, 4):
    if sys.version_info < (3, ):
        print("""\nsstp-server v0.5+ does not support Python 2,
If you want use it with Python 2, please upgrade your pip to 9.0.1+ then retry,
or install sstp-server v4.x manually.""", file=sys.stderr)
    else:
        print("\nsstp-server requires Python 3.4.4 or above.", file=sys.stderr)
    sys.exit(1)

with open('README.rst') as readme:
    long_description = readme.read()

fcsmodule = Extension('sstpd.codec', sources=['sstpd/codecmodule.c'])

setup(
    name='sstp-server',
    version=version,
    description='Secure Socket Tunneling Protocol (SSTP) VPN server.',
    author='Shell Chen',
    author_email='me@sorz.org',
    url='https://github.com/sorz/sstp-server',
    packages=['sstpd'],
    ext_modules = [fcsmodule],
    entry_points="""
    [console_scripts]
    sstpd = sstpd:run
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet',
        'Topic :: Internet :: Proxy Servers',
        'License :: OSI Approved :: MIT License'
    ],
    long_description=long_description,
    python_requires='>=3.4.4',
    extras_require={
        'uvloop': ['uvloop>=0.8.0']
    },
)

