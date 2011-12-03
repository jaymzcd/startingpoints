#!/bin/bash

mkdir $1/media;
mkdir $1/media/css;
mkdir $1/media/js;
mkdir $1/templates;
mkdir $1/assets;
mkdir $1/media/uploads;
mkdir $1/session_data;
touch $1/README.md

touch $1/media/css/styles.css;
touch $1/media/js/script.js;
touch $1/session_data/.gitignore;
touch $1/media/uploads/.gitignore;

cp cherrypy/app.py $1;
cp html/master.html $1/templates/master.html;
cp html/cherrypy_index.html $1/templates/index.html;

cd $1;
git init;
git add .;
git add -f $1/session_data/.gitignore;
git add -f $1/media/uploads/.gitignore;
git commit -am "initial commit";

echo "Go code!";
