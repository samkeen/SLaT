from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='slat',
    version='0.2.3',
    author="Sam Keen",
    author_email="sam.sjk@gmail.com",
    description="Simple Lambda Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samkeen/SLaT",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'structlog'
    ],
)
