#!/usr/bin/env python
# flake8: noqa
import os

from setuptools import setup, find_packages


def read_file(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


readme = read_file('README.md')
changes = ''


install_requires = [
    'Django==3.2.11',
    'django-countries==7.2.1',
    'Pillow==9',
    'psycopg2-binary==2.9.3',
]

tests_requires = [

]
setup(
    name='been',
    version='0.1',
    license='MIT',

    packages=find_packages(exclude=('tests', 'tests.*')),
    install_requires=install_requires,
    extras_require={
        'test': tests_requires,
    },
    include_package_data=True,
    zip_safe=False,

    description='Where have you been all your life?',
    long_description='\n\n'.join([readme, changes]),
    author='Loek van Gent',
    author_email='info@loekvan.gent',
    platforms=['any'],
    url='https://github.com/ganentson/been',
    classifiers=[
        'Development Status :: 5 - Development/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ]
)
