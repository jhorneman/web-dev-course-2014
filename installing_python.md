---
title: Installing Python (on Windows)
layout: default
---

# How to install Python on Windows

This assumes a clean system with no Python installed. If you do have Python installed, this guide assumes you know what you're doing and can skip any redundant steps.

## Install Python and core tools

We need Python 2.7, Setuptools, pip, and virtualenv because we're not animals.

(The following is based on [this guide](http://docs.python-guide.org/en/latest/starting/install/win/).)

Download the latest version of Python 2.7 for 64-bit Windows [here](https://www.python.org/downloads/release/python-278/). *Make sure it's the x86-64 version!*

Just install it to C:\Python27.

Add this to your PATH environment variable:

    C:\Python27\;C:\Python27\Scripts\

Download and run the latest version of Setuptools for Windows [here](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py). We only need it to install pip, a better package maanger. Don't ask.

Download and run the Python script [here](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) to install pip.

Install virtualenv using pip:

    pip install virtualenv

## Create a virtual environment

We want to separate the packages needed for the course from other Python stuff, so we use virtualenv.

Create a virtual environment using:

    virtualenv C:\python_venvs\webdev

It's good to have a place to put virtual environments. In this case we're assuming they're in C:\python_venvs\, but feel free to change that.

Now activate the virtual environment by running:

    C:\python_venvs\webdev\Scripts\activate.bat

The command line prompt should change to reflect the active virtual environment.

# Optional steps

Let's hope we don't need these!

## 64 bit binaries

We want to avoid having to build any C code for Python packages because it's tricky to set up. So we're going to download pre-built binaries for 64-bit Windows.

Open http://www.lfd.uci.edu/~gohlke/pythonlibs/ and download the latest installers (for amd64 and Python 2.7) for any packages you might need.

## Install PyWin32

Making sure the virtual environment is active, download PyWin32 from the download page above, then install it using:

    easy_install path/to/downloaded/installer.exe
