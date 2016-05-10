"""
Copyright (C) 2013 Roman Mohr <roman@fenkhuber.at>
"""

"""setup - setuptools based setup for static

Copyright (C) 2006-2009 Luke Arno - http://lukearno.com/

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to:

The Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor,
Boston, MA  02110-1301, USA.

Luke Arno can be found at http://lukearno.com/

"""

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--cov', 'static', 'tests']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(name='static3',
      version='0.6.2',
      description=
      'A really simple WSGI way to serve static (or mixed) content.',
      long_description=open('README.rst', 'rb').read().decode('utf-8'),
      author='Roman Mohr',
      author_email='roman@fenkhuber.at',
      url='https://github.com/rmohr/static3',
      license="LGPL",
      py_modules=['static'],
      packages=[],
      cmdclass={'test': PyTest},
      tests_require=['pytest', 'webtest', 'pytest-cov'],
      extras_require={
          'KidMagic': 'kid',
          'GenshiMagic': 'Genshi',
      },
      entry_points="""
          [console_scripts]
              static=static:command
      """,
      keywords="wsgi web http static content webapps",
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Library or '
                   'Lesser General Public License (LGPL)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'])
