import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fpdecorator",
    version="0.0.1",
    author="One E. Field",
    author_email="one-element-field@protonmail.com",
    description="Your favorite combinator made decorator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/one-element-field/fixed-pint-decorators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
