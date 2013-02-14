#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name='sqlcanonclient',
    version='0.1',
    package_dir={'':'src'},
    packages=find_packages('src'),
    dependency_links=[
        'http://sourceforge.net/projects/pylibpcap/files/pylibpcap/0.6.4/'
    ],
    install_requires=['construct==2.06', 'pylibpcap==0.6.4'],
    entry_points={
        'console_scripts': [
            'sqlcanonclient = sqlcanonclient.sqlcanonclient',
        ]
    }
    #scripts=[
    #    'src/sqlcanonclient/sqlcanonclient.py',
    #],
)
