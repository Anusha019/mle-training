import os.path as op
from distutils.core import setup

from setuptools import PEP420PackageFinder

ROOT = op.dirname(op.abspath(__file__))
SRC = op.join(ROOT, "src")

with open('README.md') as f:
    readme = f.read()


setup(
    name="housing_price",
    version="0.0.1",
    package_dir={"": "src"},
    description="Housing price prediction",
    long_description=readme,
    author="anusha polaki",
    author_email='anusha.polaki@tigeranalytics.com',
    packages=PEP420PackageFinder.find(where=str(SRC)),
)
