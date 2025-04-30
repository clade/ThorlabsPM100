# -*- coding: utf8 -*-
import sys

__version__ = '1.2.4' # PLEASE CHECK ALSO THE setup.py file


if "setuptools" not in sys.modules.keys():
    from .ThorlabsPM100 import ThorlabsPM100
    from .usbtmc import USBTMC
