import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='slat',
    version='0.1.12',
    author="Sam Keen",
    author_email="sam.sjk@gmail.com",
    description="Simple Lambda Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samkeen/SLaT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'structlog'
    ],
)
