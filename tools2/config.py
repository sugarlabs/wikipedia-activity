#!/usr/bin/env python
# -*- coding: utf-8 -*-
# These configuration params are used in the process to create 
# a new wikipedia activity

input_xml_file_name = './eswiki-20111112-pages-articles.xml'
favorites_file_name = 'favorites.txt'
blacklist_file_name = './blacklist.txt'

REDIRECT_TAGS = [u'#REDIRECT', u'#REDIRECCIÓN']

BLACKLISTED_NAMESPACES = ['Wikipedia:', 'MediaWiki:']

TEMPLATE_NAMESPACES = ['Plantilla:']

LINKS_NAMESPACES = [u'Categoría']

FILE_TAG = 'Archivo:'

MAX_IMAGE_SIZE = 300
