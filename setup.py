#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import io
from shutil import rmtree
from cx_Freeze import setup, Executable

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'whisperplayer'
DESCRIPTION = 'Randomized Sound Player for SEA-ENL Navarro 2018'
URL = 'https://github.com/thejohnd/whisper-player'
EMAIL = 'sparkoflife@gmail.com'
AUTHOR = 'John D (@psyenceguy)'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
    'pygame', 'tkinter', 'pathlib', 'random', 'datetime', 'os',
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier
# for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(
            '{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": [
    "pygame",
    "_tkinter",
    "mixer"
],
    "packages": [
    "tkinter",
    "os"
],
    "include_files": [
    r"C:\Python36-32\DLLs\tcl86t.dll",
    r"C:\Python36-32\DLLs\tk86t.dll",
],
    "path": sys.path + ['modules']
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r'C:\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\tcl\tk8.6'

setup(name=NAME,
      version=about['__version__'],
      description=DESCRIPTION,
      long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
        ],
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)