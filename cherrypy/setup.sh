#!/bin/bash

prefix=${2:-/var/www/}
mkdir $prefix$1;

mkdir $prefix$1/media;
mkdir $prefix$1/media/css;
mkdir $prefix$1/media/js;
mkdir $prefix$1/templates;
mkdir $prefix$1/templates/blocks;
mkdir $prefix$1/assets;
mkdir $prefix$1/media/uploads;
mkdir $prefix$1/session_data;
touch $prefix$1/README.md

touch $prefix$1/media/css/styles.less;
touch $prefix$1/media/js/script.js;
touch $prefix$1/session_data/.gitignore;
touch $prefix$1/media/uploads/.gitignore;
touch $prefix$1/templates/blocks/footer.html;
touch $prefix$1/templates/blocks/header.html;

cp cherrypy/app.py $prefix$1;
cp html/boostrap_cdn.html $prefix$1/templates/master.html;
cp html/cherrypy_index.html $prefix$1/templates/index.html;

cd $prefix$1;
git init;
git add .;
git add -f $prefix$1/session_data/.gitignore;
git add -f $prefix$1/media/uploads/.gitignore;
git commit -am "initial commit";

echo "Go code!";
