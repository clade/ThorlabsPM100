Overview
========

This package can be used to drive a PM100A/D power meter from Thorlabs. It provides an object oriented interface to the SCPI commands using Python properties.

Installation
============

To install the ThorlabsPM100 driver, download the package and run the command:

    python setup.py install

You can also directly move the ThorlabsPM100 to a location that Python can import from (directory in which scripts using ThorlabsPM100 are run, etc.)

Usage
=====

The best way to connect your instrument is with the pyvisa package <https://pyvisa.readthedocs.io/en/stable/>. On linux, the instrument is automatically detected as a USBTMC device. A simple interface is described in the file usbtmc.py

First you need to create your instrument. Using visa:

    import pyvisa as visa
    from ThorlabsPM100 import ThorlabsPM100
    rm = visa.ResourceManager()
    inst = rm.open_resource('USB0::0x0000::0x0000::xxxxxxxxx::INSTR', term_chars='\\n', timeout=1)
    power_meter = ThorlabsPM100(inst=inst)

Or using usbtmc (you need to have read and write access to the ‘/dev/usbtmc0’):

    from ThorlabsPM100 import ThorlabsPM100, USBTMC
    inst = USBTMC(device="/dev/usbtmc0")
    power_meter = ThorlabsPM100(inst=inst)

Commands that set or query a value are Python properties of ThorlabsPM100 class. Other command are methods of ThorlabsPM100 class :

    print(power_meter.read) # Read-only property
    print(power_meter.sense.average.count) # read property
    power_meter.sense.average.count = 10 # write property
    power_meter.system.beeper.immediate() # method

Version history
===============

-   1.1 : support of Python 3 with 2to3
-   1.0 : initial release

