#!/bin/bash

mkdir $1/media;
mkdir $1/media/css;
mkdir $1/media/js;
mkdir $1/templates;
mkdir $1/assets;
touch $1/README.md

touch $1/media/css/styles.css;
touch $1/media/js/script.js;

cp cherrypy/app.py $1;
cp html/master.html $1/templates/master.html;
cp html/cherrypy_index.html $1/templates/index.html;

cd $1;
echo "Go code!";