import os
from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    setup(
        name = "python_path",
        version = "0.1.3",
        author = "Cristian Garcia",
        author_email = "cgarcia.e88@gmail.com",
        description = "A clean way to import scripts on other folders via a context manager.",
        long_description = readme.read(),
        license = "MIT",
        keywords = [],
        url = "https://github.com/cgarciae/python_path",
        packages = find_packages(),
        package_data={},
        include_package_data = True,
        install_requires = []
    )
