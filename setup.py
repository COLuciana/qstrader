from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qstrader-reloaded",
    version="0.1.0",
    description="QSTrader backtesting simulation engine. Updated to work with newer Python and Pandas versions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/COLuciana/qstrader-reloaded",
    author="Luciana Torero",
    author_email="lucianatorero3@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "Click>=8.0.0",
        "matplotlib>=3.3.4",
        "numpy>=1.18.4",
        "pandas>=2.0",
        "seaborn>=0.10.1",
    ],
)
