# Introduction
A theme for the static website generator [Pelican](http://getpelican.com/) heavily inspire by [Modernist](http://orderedlist.com/modernist/)

## Usage
### Dependencies to use Pelican
* Pelican

>$ sudo pip install pelican

* Pelican plugins

>$ git clone --recursive https://github.com/getpelican/pelican-plugins

Run the command above in project root
* Markdown

>$ sudo pip install markdown

* webassets

>$ sudo pip install webassets

* cssmin

>$ sudo pip install cssmin

* SASS

>$ gem install sass

Make sure gem bin directory is in your $PATH

### Theme dependencies
* CSS/SCSS
    * normalize
    * bourbon
* MathJax
* jQuery

### Update theme dependencies
* normalize
    * Download normalize from *http://necolas.github.io/normalize.css/* to *theme/O\(S\)/static/css/normalize*
* bourbon

>$ gem install bourbon

>$ bourbon install --path theme/O\(S\)/static/css/

* MathJax
    * Download complete MathJax package *https://github.com/mathjax/MathJax/archive/master.zip*
    * Copy extracted files under *theme/O\(S\)/static/js/MathJax*
    * Copy *Gruntfile.js* and *package.json* from *misc* to *theme/O\(S\)/static/js/MathJax*
    * Install grunt and dependencies

    >$ sudo npm install -g grunt-cli

    >$ npm install

    * Run gruntfile to reduce MathJax size

    >$ grunt

    * Remove *Gruntfile.js* and *node_modules* in *theme/O\(S\)/static/js/MathJax* 

## Run
### Generate blog
* To get your final blog run

>$ pelican content -o output -s publishconf.py

* To get an live preview on your local machine run the following in parallel

>$ pelican -r content -o output -s pelicanconf.py

>$ cd output && python -m pelican.server

Your blog can now be previewed on http://localhost:8000

## TODOs
### Important
* config lines for foooter button
* Markdown listing in list gets indetation and breaks
* fix footnote is indented by 40px by default (bad fix right now)
* fix huge margins between entries in footnote (bad fix right now)
* Menu for pages and option in config to hide/show menu

## Credits
Credits to Steve Smith for his [Modernist](http://orderedlist.com/modernist/) theme where most of the inspiration for this theme comes from.
Thanks to Atle Mo for his beautiful collection of [patterns](http://subtlepatterns.com) used for the background image.