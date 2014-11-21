import os
import sys

here = lambda *a: os.path.join(os.path.dirname(__file__), *a)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open(here('README.md')).read()
requirements = [x.strip() for x in open(here('requirements.txt')).readlines()]
setup(
    name='huepi',
    version='0.1.0',
    description='Application for the Raspberry Pi to control the Philips Hue lights.',
    long_description=readme,
    author='Tom Davidson',
    author_email='tom@davidson.me.uk',
    url='https://github.com/Tom-Davidson/huePi',
    packages=[
        'hue',
    ],
    package_dir={'hue': 'hue'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='huepi',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Home Automation',
    ],
    test_suite='tests',
    scripts=[
        'huepi.py'
        'prepHue.py'
    ],
)