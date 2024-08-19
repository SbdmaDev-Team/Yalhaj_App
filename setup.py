from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in yalhaj_app/__init__.py
from yalhaj_app import __version__ as version

setup(
	name="yalhaj_app",
	version=version,
	description="Yalhaj",
	author="Yalhaj",
	author_email="'y@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
