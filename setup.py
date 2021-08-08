from setuptools import setup, find_packages

VERSION = '0.2.0'
DESCRIPTION = 'Cloverly API Module for Python'
LONG_DESCRIPTION = """
The Cloverly Python Module is a wrapper around the python requests library.
It can be used to create, edit and delete cloverly resources, including, but not
limited to: Offsets, Estimates and Purchases.
"""

# Setting up
setup(
    name="cloverly-python-module",
    version=VERSION,
    author="Zain Lakhani",
    author_email="<zain@cloverly.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/cloverly/cloverly-python-module",
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
