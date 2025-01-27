# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="pydngconverter",
    version="0.2.0",
    description="Python Interface for the Adobe's DNG Converter",
    python_requires="==3.*,>=3.8.0",
    project_urls={
        "documentation": "https://bradenm.github.io/pydngconverter",
        "homepage": "https://github.com/BradenM/pydngconverter",
        "repository": "https://github.com/BradenM/pydngconverter",
    },
    author="Braden Mars",
    author_email="bradenmars@bradenmars.me",
    license="MIT",
    keywords="pydng dng dngconverter raw api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    packages=["pydngconverter"],
    package_dir={"": "."},
    package_data={},
    install_requires=["psutil==5.8.*,>=5.8.0", "rich==9.10.*,>=9.10.0", "wand==0.6.*,>=0.6.0"],
    extras_require={
        "dev": [
            "autoflake==1.*,>=1.4.0",
            "black==20.*,>=20.8.0.b1",
            "bump2version==1.*,>=1.0.1",
            "coveralls==3.*,>=3.0.0",
            "flake8==3.*,>=3.8.4",
            "isort==5.*,>=5.7.0",
            "mypy==0.*,>=0.800.0",
            "pytest==6.*,>=6.2.2",
            "pytest-asyncio==0.*,>=0.14.0",
            "pytest-cov==2.*,>=2.11.1",
            "pytest-coverage==0.*,>=0.0.0",
            "pytest-mock==3.*,>=3.5.1",
            "pytest-sugar==0.*,>=0.9.4",
            "recommonmark==0.*,>=0.7.1",
            "sphinx==3.*,>=3.4.3",
            "sphinx-autodoc-typehints==1.*,>=1.11.1",
            "sphinx-rtd-theme==0.*,>=0.5.1",
        ],
        "docs": [
            "recommonmark==0.*,>=0.7.1",
            "sphinx==3.*,>=3.4.3",
            "sphinx-autodoc-typehints==1.*,>=1.11.1",
            "sphinx-rtd-theme==0.*,>=0.5.1",
        ],
    },
)
