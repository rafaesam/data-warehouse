#!/usr/bin/env python
""" Setup the py-pip-install-test package """

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["pytest==7.1.1"]

test_requirements = [
    "docker",
    "airflow",
    "pandas",
    "matplotlib",
    "sql",
    "pytest"
]

setup(
    name="Data Warehouse",
    version="0.1.0",
    description ="Data Warehouse",
    install_requires=requirements,
    long_description=readme,
    author="Rafaa",
    email="rafaesam0@gmail.com",
    python_requires=">=3.6",
    include_package_data=True,
    keywords='dbt, data warehouse, traffic data',
    packages=['scripts'],
    url="https://github.com/rafaesam/AgriTech-USGS-LIDAR",
    zip_safe=False
)

package_dir={'':"src"},
packages=find_packages("src")
# test_suite="tests",
# tests_requires=test_requirements
