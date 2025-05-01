# setup.py

from setuptools import setup, find_packages

setup(
    name="taskcli",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # if you use external packages later
    entry_points={
        "console_scripts": [
            "taskcli=taskcli.cli:main",
        ],
    },
)
