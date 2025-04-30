# -*- coding: latin-1 -*-
from setuptools import setup

doc_url = "http://pythonhosted.org/ThorlabsPM100"

__version__ = "1.2.4" # PLEASE CHECK ALSO THE __init__.py

__long_description__ = u"""\
Overview
========

This package can be used to drive a PM100A/D power meter from Thorlabs.
It provides an object oriented interface
to the SCPI commands using Python properties.

Installation
============

To install the ThorlabsPM100 driver, download the package and run the command::

   python setup.py install

You can also directly move the ThorlabsPM100 to a location
that Python can import from (directory in which scripts
using ThorlabsPM100 are run, etc.)

Usage
=====

The best way to connect your instrument is with the pyvisa package
`<https://pyvisa.readthedocs.io/en/stable/>`_.
On linux, the instrument is automatically detected as a USBTMC device.
A simple interface is described in the file usbtmc.py

First you need to create your instrument. Using visa::

    import visa
    from ThorlabsPM100 import ThorlabsPM100
    rm = visa.ResourceManager()
    inst = rm.open_resource('USB0::0x0000::0x0000::xxxxxxxxx::INSTR',
                            term_chars='\\n', timeout=1)
    power_meter = ThorlabsPM100(inst=inst)

Or using usbtmc (you nedd to have read and write access to the
'/dev/usbtmc0')::

    from ThorlabsPM100 import ThorlabsPM100, USBTMC
    inst = USBTMC(device="/dev/usbtmc0")
    power_meter = ThorlabsPM100(inst=inst)


Commands that set or query a value are Python properties of ThorlabsPM100
class. Other command are methods of ThorlabsPM100 class ::

    print power_meter.read # Read-only property
    print power_meter.sense.average.count # read property
    power_meter.sense.average.count = 10 # write property
    power_meter.system.beeper.immediate() # method

Contact
=======

Please send bug reports or feedback to `Pierre Cladé`_.

Vesrion History
===============

* 1.2.1 : change 'ask' to 'query'
* 1.1.1 and 1.1.2 : small bug corrections
* 1.1 : support of Python 3 with 2to3
* 1.0 : initial release


.. _Pierre Cladé: mailto:pierre.clade@spectro.jussieu.fr
"""

long_description = __long_description__

long_description += r"""
Documentation
=============

**Detailed information** about the Thorlabs PM100 driver can be found on the 
`main web site <http://pythonhosted.org/ThorlabsPM100>`_

**Source code** available on `github <https://github.com/clade/ThorlabsPM100>`_.
"""

setup(name="ThorlabsPM100",
      version=__version__,
      author=u'Pierre Cladé',
      author_email="pierre.clade@spectro.jussieu.fr",
      maintainer=u'Pierre Cladé',
      maintainer_email="pierre.clade@spectro.jussieu.fr",
      license='''\
This software can be used under one of the following two licenses: \
(1) The BSD license. \
(2) Any other license, as long as it is obtained from the original \
author.''',

      description='Interface to the PM100A/D power meter from Thorlabs.',
      long_description=long_description,
      keywords=['Thorlabs', 'PM100', 'PM100A', 'PM100D'],
      url=doc_url,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'],
      packages=["ThorlabsPM100", ]
      )
