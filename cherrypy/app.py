#!/usr/bin/env python2

import cherrypy
import json
import os
import re
import sqlite3
import sys
import urllib

from jinja2 import Environment, FileSystemLoader

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
DBPATH = os.path.join(PROJECT_PATH, 'entries.db')
SESSION_FILE_PATH = os.path.join(PROJECT_PATH, 'session_data/')
STATICDIR = PROJECT_PATH

sys.path.append(PROJECT_PATH)

try:
    from local_settings import *
except ImportError:
    pass

env = Environment(loader=FileSystemLoader(os.path.join(PROJECT_PATH, 'templates')))
env.globals['url'] = cherrypy.url


class Root(object):

    _cp_config = {'tools.sessions.on': True,
        'tools.sessions.timeout': 60 * 24,
        'tools.sessions.storage_type': "file",
        'tools.sessions.storage_path': SESSION_FILE_PATH,
    }

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        context = dict()
        tmpl = env.get_template('index.html')
        return tmpl.render(context)

conf = {
    '/': {
        'tools.encode.on': True,
        'tools.encode.encoding': 'utf-8',
        'tools.gzip.on': True,
    },
    '/media': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'media',
        'tools.staticdir.root': STATICDIR,
    },
}

# for mod_wsgi
application = cherrypy.Application(Root(), script_name=None, config=conf)

if __name__ == '__main__':

    wsgi_debug = bool(os.environ.get('WSGI_DEBUG', False))
    if wsgi_debug:
        # Profile this application by setting an environment variable "WSGI_DEBUG" to 1
        # See: http://docs.repoze.org/profile/ for the full docs and setup
        # Load profiling
        from repoze.profile.profiler import AccumulatingProfileMiddleware
        middleware = AccumulatingProfileMiddleware(
            application,
            log_filename='/tmp/app_profile.log',
            discard_first_request=True,
            flush_at_shutdown=True,
        )

        # There is a wsgi.pipeline conf that takes a WSGI application and applies
        # middleware to it. Not entirely sure exactly on how to hook this up to
        # the internal quickstart/cp server but wsgiref will do the same job
        # and works without much hassle (and is stdlib):

        # See (http://goo.gl/gTKKa) for example (although that's 2008, so guessing)
        # the pipeline way works as well, just sure how with quickstart

        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, middleware)
        print "Serving on 0.0.0.0:8080..."
        httpd.serve_forever()

    else:
        cherrypy.server.socket_host = '0.0.0.0'
        cherrypy.quickstart(Root(), config=conf)
