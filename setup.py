#!/usr/bin/env python

import distribute_setup
# User may not have setuptools installed on their machines.
# This script will automatically install the right version from PyPI.
distribute_setup.use_setuptools()
import setuptools

setuptools.setup(
  name='gae-console',
  description=('Powerful Interactive Console for App Engine applications.'),
  version='0.1.0',
  packages=setuptools.find_packages(),
  author='Dmitry Sadovnychyi',
  author_email='gae-console@dmit.ro',
  keywords=['google app engine', 'gae', 'appengine', 'console', 'terminal'],
  url='https://github.com/sadovnychyi/gae-console',
  license='GNU General Public License v2.0',
  include_package_data=True,
  exclude_package_data={'': ['README.md']},
)
