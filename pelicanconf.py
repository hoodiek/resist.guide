#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'resist.guide'
SITENAME = u'resist.guide'
SITEURL = 'https://resist.guide'
#THEME = 'theme/pure-single'
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
#    ('', ''),
#)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/resist-guide/resist.guide/'),
)

# Static path settings for GitHub Sites config
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Site Navigation Settings
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 13

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
