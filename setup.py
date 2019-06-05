# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Abysser',
    version='0.0.1',
    description='A tool to parse Eve Online screenshots for Abyssal details',
    long_description=readme,
    author='Shadowcodex / Valindil89',
    author_email='shadow.codex01@gmail.com',
    url='https://github.com/shadowcodex/Abysser',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)