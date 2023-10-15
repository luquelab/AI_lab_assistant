"""Install script for setuptools."""

from setuptools import find_packages
from setuptools import setup
long_description = open("README.md").read()
setup(
    name='Update name here',
    version='Update version number',
    description='Add a description',
    long_description =long_description,
    long_description_content_type='text/markdown',
    author='Add authors',
    author_email='author@gmail.com',
    license='MIT License',
    url='github link',
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires = 'Add the version number',
    install_requires=[
        "Add required libraries as a list"
    ],
    classifiers=[
        "Add required classifiers here, a list of classifiers can be found here: https://pypi.org/classifiers/"
    ],
)
