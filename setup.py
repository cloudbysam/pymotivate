from setuptools import setup, find_packages

setup(
    name="pymotivate",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Samuel Ajala",
    description="A CLI tool and Python package for fetching motivational quotes.",
)