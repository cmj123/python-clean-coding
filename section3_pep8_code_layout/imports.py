# Import each library on a separate line
# Multiple packages within a module can be importef on the same line
# Import standard library first
# Import third party libraries second
# Import local packages third
# Imports should always be at the top of the file

import os
import sys
from subprocess import SubprocessError, PIPE

import flask
from django import get_version

from spacing_encoding import Person, alpha