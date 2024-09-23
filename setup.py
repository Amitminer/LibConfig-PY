"""
Setup configuration for the LibConfig library.
"""

from setuptools import setup, find_packages

setup(
    name='libconfigv1',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['pyyaml'],
    author='amitminer',
    description='A library for working with YAML configuration files',
    url='https://github.com/Amitminer/LibConfig-PY',
)
