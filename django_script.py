#!/usr/bin/env python2
import os
import sys

# Setup a working environment for our app
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH)

from django.core.management import setup_environ
import settings

setup_environ(settings)

# Imports from the django models can go below