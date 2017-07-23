import os
import argparse
import time

parser = argparse.ArgumentParser(description="A simple project manager for Python projects.")
parser.add_argument("project_name", type=str)
project_name = parser.parse_args().project_name()


os.mkdir(project_name)
print(time.strftime("[%H:%M:%S]"), "Created directory %s" % project_name)
os.chdir(project_name)
os.mkdir("src")
print(time.strftime("[%H:%M:%S]"), "Created source directory %s/src" % project_name)
os.mkdir("tests")
print(time.strftime("[%H:%M:%S]"), "Created tests directory %s/tests")
with open("LICENSE.txt", "xt") as l:
	print("""MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""", file=l)
print(time.strftime("[%H:%M:%S]"), "Created LICENSE file %s/LICENSE.txt" % project_name)
with open("README.md", "xt") as r:
	print("Sample description for your project", file=r)
print(time.strftime("[%H:%M:%S]"), "Created README file %s/README.md" % project_name)
with open("setup.py", "xt") as s:
	print("""try:
	from setuptools import setup
except:
	from distutils.core import setup

setup(
	name='%s',
	version='0.1dev',
	packages=['src'],
	tests=['tests']
	license='MIT License',
	description='sample description for your project',
)""" % project_name, file=s)
print(time.strftime("[%H:%M:%S]"), "Created setup file %s/setup.py" % project_name)
os.chdir("src")
with open("__init__.py", "xt") as i:
	print("from . import main", file=i)
print(time.strftime("[%H:%M:%S]"), "Created init file %s/src/__init__.py" % project_name)
with open("main.py", "xt") as m:
	print("", file=m)
print(time.strftime("[%H:%M:%S]"), "Created main file %s/src/main.py" % project_name)
os.chdir("..")
os.chdir("tests")
with open("test.py", "xt") as t:
	print("""import os
os.chdir("..")
os.chdir('src')
errors = 0
with open('__init__.py') as init:
	try:
		eval(str(init))
	except:
		errors += 1
print(str(errors), "errors raised while excecuting __init__.py")""", file=t)
print(time.strftime("[%H:%M:%S]"), "Created test file %s/tests/test.py" % project_name)
