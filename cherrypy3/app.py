#!/usr/bin/env python2

from BeautifulSoup import BeautifulSoup as Soup
from jinja2 import Template
import urllib
import cherrypy
import re

from templates import PAGE_TEMPLATE

class CherryStart(object):

    def index(self):
        context = dict()
        return Template(PAGE_TEMPLATE).render(context)
    index.exposed = True

if __name__=='__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(CherryStart)

