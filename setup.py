# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='jira_task_manager',
    version='0.1.0',
    description='Track the loging hours in Jira',
    long_description=readme,
    author='Adrià Guixà',
    author_email='adriaguixa@gmail.com',
    url='https://github.com/adriaguixa/jira_task_manager',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)