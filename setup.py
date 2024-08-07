# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

version = "0.0.12"
NAME = "elexonpy"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=version,
    description="Elexon Python Client",
    author="Richa Sharma",
    author_email="onlinericha19@gmail.com",
    url="https://github.com/openclimatefix/Elexonpy",
    keywords=["Swagger", "Elexon API", "Python Client"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is a Python client for the Elexon API, generated using Swagger Codegen.
    It provides an easy way to interact with the Elexon API in Python applications.
    """,
    long_description_content_type="text/markdown",
)
