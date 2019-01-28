# -*- coding: utf-8 -*-

"""
osu-API-Wrapper
~~~~~~~~
A hopefully good osu! API Wrapper.
"""

import logging
from collections import namedtuple
from osu.client import Client

__title__ = 'osu-API-Wrapper'
__author__ = 'Matthias K.'
__version__ = '0.0.1a'
__license__ = 'MIT'
__copyright__ = '(c) 2019 Matthias K.'
__url__ = 'https://github.com/byWambo/osu-API-Wrapper'

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel='alpha', serial=0)

fmt = '[%(levelname)s] %(asctime)s - %(name)s:%(lineno)d - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)
logging.getLogger(__name__).addHandler(logging.NullHandler())
