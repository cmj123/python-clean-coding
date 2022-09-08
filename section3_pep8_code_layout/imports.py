# Import each library on a separate line
# Multiple packages within a module can be importef on the same line
# Import standard library first
# Import third party libraries second
# Import local packages third
# Imports should always be at the top of the file
# Description of file comes before import
# After file description import future updates... 
# Future update should always appear after the file description
# dunder variables should be assigned after future imports


'''
    This file is a professional example to PEP8 imports
'''

from __future__ import unicode_literals

__all__ = ['a', 'b', 'c', 'd']
__version__ = '0.1'
__author__ = "Esuabom Dijemeni"


import os
import sys
from subprocess import SubprocessError, PIPE

import flask
from django import get_version

from spacing_encoding import Person, alpha

def a():
    pass

def b():
    pass

def c():
    pass