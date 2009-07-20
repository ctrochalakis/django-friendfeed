from setuptools import setup

kwargs = {
    'name' : 'django_friendfeed',
    'version' : '0.1',
    'description' : 'Friendfeed utilities for Django',
    'author' : 'Christos Trochalakis',
    'author_email' : 'yatiohi@ideopolis.gr',
    'url' : 'http://github.com/ctrochalakis/django-friendfeed',
    'packages' : ['django_friendfeed',
                  'django_friendfeed.templatetags'],
    'classifiers' : ['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Framework :: Django',
                     'Topic :: Utilities'],
    'include_package_data' : False,
    'zip_safe' : False,
}

setup(**kwargs)
