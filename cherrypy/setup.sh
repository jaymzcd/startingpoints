#!/bin/bash

prefix=${2:-/var/www/}
mkdir $prefix$1;

mkdir $prefix$1/media;
mkdir $prefix$1/media/css;
mkdir $prefix$1/media/js;
mkdir $prefix$1/templates;
mkdir $prefix$1/assets;
mkdir $prefix$1/media/uploads;
mkdir $prefix$1/session_data;
touch $prefix$1/README.md

touch $prefix$1/media/css/styles.css;
touch $prefix$1/media/js/script.js;
touch $prefix$1/session_data/.gitignore;
touch $prefix$1/media/uploads/.gitignore;

cp cherrypy/app.py $prefix$1;
cp html/master.html $prefix$1/templates/master.html;
cp html/cherrypy_index.html $prefix$1/templates/index.html;

cd $prefix$1;
git init;
git add .;
git add -f $prefix$1/session_data/.gitignore;
git add -f $prefix$1/media/uploads/.gitignore;
git commit -am "initial commit";

echo "Go code!";
