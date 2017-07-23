try:
	from setuptools import setup
except:
	from distutils.core import setup

setup(
	name='doman',
	version='0.1dev',
	packages=["src"],
	tests=["tests"]
	license="MIT License",
	description="A simple Python manager for your Python projects",
)