#!/usr/bin/env python
from distutils.core import setup

setup(name='django-bricks-social',
      version='0.1',
      description='Django app with Bricks for social services like Instagram, Twitter and Facebook',
      author='AGoodId',
      author_email='teknik@agoodid.se',
      url='http://github.com/AGoodId/django-bricks-social/',
      packages=['bricks_social',],
      package_data = {
          'blinks': [
              'static/*',
              'templates/*.html',
              'templates/*/*.html',
          ],
      },
      license='BSD',
      include_package_data = False,
      zip_safe = False,
      classifiers = [
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Environment :: Web Environment',
          'Framework :: Django',
      ],
)
