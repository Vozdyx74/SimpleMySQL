from .table import Table
from .column import Column
from .variables import *
from .errors import *
from .database import create_table, connect

import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__author__ = 'Vozdyx74, HaCsO'
__title__ = 'SimpleMySQL'
__license__ = 'MIT'
__version__ = '0.0.1'
