from setuptools import setup, find_packages


setup(
    name="cryptography",
    version="0.1",
    packages=find_packages(),
    scripts=["scripts/caesar.py"]
)
