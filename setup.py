# -*- coding: utf-8 -*-
"""
This module contains the tool of Products.PublicJobVacancy
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.2'

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('Products', 'PublicJobVacancy', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )

tests_require=['zope.testing']

setup(name='Products.PublicJobVacancy',
      version=version,
      description="Job Vacancy contenttype",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='contenttype Job vacancy OSHA',
      author='Syslab.com GmbH',
      author_email='mailto:info@syslab.com',
      url='https://svn.syslab.com/svn/OSHA/Products.PublicJobVacancy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'Products.PublicJobVacancy.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*- 
      """,
      paster_plugins = ["ZopeSkel"],
      )
