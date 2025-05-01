from setuptools import setup, find_packages

setup(
    name="taskcli",
    version="0.1.0",
    description="Simple task manager CLI tool",
    author="Your Name",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "taskcli=taskcli.cli:main",
        ],
    },
)
# This setup script uses setuptools to package the taskcli application.
