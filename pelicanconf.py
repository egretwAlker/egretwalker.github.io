from pickle import MARK


AUTHOR = 'egretwalker'
SITENAME = 'loghj'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'notmyidea_katex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('maquilaque.fr', 'https://maquilaque.fr/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = [ 'images',
                 'extra',]

EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},}

MARKDOWN = {
    'extension_configs': {
        # Needed for code syntax highlighting
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # This is for enabling the TOC generation
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
    },
    'output_format': 'html5',
}

READERS = {'html': None}
TEMPLATE_PAGES = {'pages/dfts.html': 'dfts.html'}

MARKDOWN = {
    'extensions': ['mdx_math'],
    'extension_configs': {
        'mdx_math': {
            'enable_dollar_delimiter': True
        }
    },
}
