from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: General",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Game"]

# Description should be a one-liner:
description = "mancala: Variations of the board game"
# Long description will go up on the pypi page
long_description = """

Mancala
========

Repository README_.

.. _README: https://github.com/samjcus/mancala/blob/master/README.md

License
=======
``mancala`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2016--, Sam Cusworth
"""

NAME = "mancala"
MAINTAINER = "Sam Cusworth"
MAINTAINER_EMAIL = "samjcus@googlemail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/samjcus/mancala"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Sam Cusworth"
AUTHOR_EMAIL = "samjcus@googlemail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGES = ['mancala',
            'mancala.tests']
PACKAGE_DATA = {'mancala': [pjoin('data', '*')]}
REQUIRES = ["numpy"]
