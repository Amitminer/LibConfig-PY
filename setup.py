from setuptools import setup, find_packages

setup(
    name='libconfig_py',
    version='1.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['pyyaml'],
    author='amitminer',
    author_email='amitxd4871@gmail.com',
    description='A library for working with YAML configuration files',
    url='https://github.com/Amitminer/LibConfig-PY',
)
