#!/bin/bash

mkdir $1/media;
mkdir $1/media/css;
mkdir $1/media/js;
mkdir $1/templates;

cp cherrypy/app.py $1;
cp html/html5ish.html $1/templates/master.html;

cd $1;
echo "Go code!";