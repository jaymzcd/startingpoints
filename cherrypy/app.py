#!/usr/bin/env python2

import urllib
import cherrypy
import re
import sqlite3
import os
import json
import sys

from jinja2 import Template, Environment, FileSystemLoader

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH)
DBPATH = os.path.join(PROJECT_PATH, 'entries.db')

env = Environment(loader=FileSystemLoader(os.path.join(PROJECT_PATH, 'templates')))

class CherryStart(object):

    _cp_config = {'tools.sessions.on': True}

    def __init__(self):
        pass

    def index(self, lang=None, country=None, sku=None):
        tmpl = env.get_template('templates/index.html')
        return tmpl.render(context)
    index.exposed = True


STATICDIR = PROJECT_PATH

try:
    from local_settings import *
except ImportError:
    pass


conf = {
    '/': {
        'tools.encode.on': True,
        'tools.gzip.on': True,
    },
    '/media': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'media',
        'tools.staticdir.root': STATICDIR,
    },
}

if __name__=='__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(CherryStart(), config=conf)

application = cherrypy.Application(CherryStart(), script_name=None, config=conf)
