#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# general settings
AUTHOR = 'YOUR_NAME'
SITENAME = 'YOUR_BLOG_TITLE'
SITESUBTITLE = 'YOUR_SUBTITLE'
SITEURL = 'YOUR_URL'

# look and feel
THEME = 'theme/O(S)'
DEFAULT_PAGINATION = 10
MATHJAX_SUPPORT = True
MD_EXTENSIONS = ['codehilite(css_class=codehilite)','extra']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets',]

# location settings
TIMEZONE = 'Europe/Berlin'
DATE_FORMATS = {'en': '%b %d %Y'}
DEFAULT_LANG = 'en'

# social, donation, affiliate links
# GITHUB_URL = 'https://github.com/YOUR_GITHUB_USER_NAME'
# BITBUCKET_URL = 'https://bitbucket.org/YOUR_BITBUCKET_USER_NAME'
# GOOGLE_PLUS_URL = 'https://plus.google.com/YOURE_GPLUS_ID/posts'
# TWITTER_USER = 'YOUR_TWITTER_USER_NAME'
# EMAIL = 'YOUR_MAIL_ADDRESS'
# FLATTR_USER = 'YOUR_FLATTR_USER_NAME'
# AMAZON_WISHLIST = 'http://www.amazon.de/registry/wishlist/YOUR_WISHLIST_ID'
# BITCOIN_ADDRESS = 'YOUR_BITCOIN_ADDRESS'

# feeds
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None

# blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# developer options
RELATIVE_URLS = True

### THESE  SETTINGS ARE NOT SUPPORTED YET ###
# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True