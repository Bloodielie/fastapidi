import os
import re

import setuptools

requirements = [
    "fastapi",
    "pyjectt"
]


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


def get_long_description():
    """Return the README."""
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_packages(package):
    """Return root package and all sub-packages."""
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setuptools.setup(
    name="fastapidi",
    python_requires=">=3.7",
    version="0.1.4",
    packages=get_packages("fastapidi"),
    url="https://github.com/Bloodielie/fastapidi",
    license="MIT License",
    author="Bloodie_lie",
    author_email="riopro2812@gmail.com",
    description="Real dependency injection in fastapi",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    install_requires=requirements,
    classifiers=[
        "Environment :: Web Environment",
        "Topic :: Internet",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    zip_safe=False,
)
