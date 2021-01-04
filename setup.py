# This file makes a python package out of the project.
# This way you can access other modules in the project

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-LoSSeth",
    version="0.0.1",
    author="Jimmy Bierenbroodspot",
    author_email="aph095ba08@gmail.com",
    description="A casino game made for a challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LoSSeth/casino",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)