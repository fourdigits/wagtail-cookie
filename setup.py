import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-cookie',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPL License',
    description='A simple Wagtail app managing cookies consent and blocking third party cookies.',
    long_description=README,
    url='https://github.com/fourdigits/wagtail-cookie',
    author='Four Digits',
    author_email='support@fourdigits.nl',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)