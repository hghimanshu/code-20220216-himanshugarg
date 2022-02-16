from setuptools import setup, find_packages
from src.bmi_calculator import VERSION


PACKAGE_NAME = 'bmi-calculator'
AUTHOR = 'Himanshu Garg'

INSTALL_REQUIRES = []
PACKAGE_DIR = {"": "src"}

setup(name=PACKAGE_NAME,
      version=VERSION,
      author=AUTHOR,
      install_requires=INSTALL_REQUIRES,
      package_dir=PACKAGE_DIR,
      packages=find_packages(where="src")
      )