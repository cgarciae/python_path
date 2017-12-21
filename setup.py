import os
from setuptools import setup, find_packages


setup(
    name = "python_path",
    version = "0.0.1",
    author = "Cristian Garcia",
    author_email = "cgarcia.e88@gmail.com",
    description = ("A clean way to import scripts on other folders via a context manager."),
    license = "MIT",
    keywords = [],
    url = "https://github.com/cgarciae/python_path",
   	packages = find_packages(),
    package_data={},
    include_package_data = True,
    install_requires = []
)
