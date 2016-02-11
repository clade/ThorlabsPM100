from __future__ import print_function

from time import sleep
from numpy import array

from ThorlabsPM100 import ThorlabsPM100, USBTMC

inst = USBTMC()

power_meter = ThorlabsPM100(inst = inst)

power_meter.system.beeper.immediate()

print("Measurement type :", power_meter.getconfigure)
print("Current value    :", power_meter.read)
print("Wavelength       :", power_meter.sense.correction.wavelength)

print("Power range limit:", power_meter.sense.power.dc.range.upper)

print("Set range auto and wait 500ms    ...")
sleep(.5)
power_meter.sense.power.dc.range.auto = "ON"

print("Power range limit:", power_meter.sense.power.dc.range.upper)

print("Set bandwidth to High")
power_meter.input.pdiode.filter.lpass.state = 0

print("Average per mesure :", power_meter.sense.average.count) 
print("Set average to 1 ...")
power_meter.sense.average.count = 1

print("Perform 100 measurements ...")
mes = array([power_meter.read for _ in range(100)])
print("Average value      :", mes.mean())
print("std deviation      :", mes.std())

print("Set average to 10 ...")
power_meter.sense.average.count = 10

print("Perform 100 measurements ...")
mes = array([power_meter.read for _ in range(100)])
print("Average value      :", mes.mean())
print("std deviation      :", mes.std())

print("Set average to 100 ...")
power_meter.sense.average.count = 100

print("Perform 100 measurements ...")
mes = array([power_meter.read for _ in range(100)])
print("Average value      :", mes.mean())
print("std deviation      :", mes.std())

print("Set bandwidth to Low")
power_meter.input.pdiode.filter.lpass.state = 1

print("Set average to 1 ...")
power_meter.sense.average.count = 1

print("Perform 100 measurements ...")
mes = array([power_meter.read for _ in range(100)])
print("Average value      :", mes.mean())
print("std deviation      :", mes.std())

print("Set average to 10 ...")
power_meter.sense.average.count = 10

print("Perform 100 measurements ...")
mes = array([power_meter.read for _ in range(100)])
print("Average value      :", mes.mean())
print("std deviation      :", mes.std())

print("Set average to 100 ...")
power_meter.sense.average.count = 100

print("Perform 100 measurements ...")
mes = array([power_meter.read for _ in range(100)])
print("Average value      :", mes.mean())
print("std deviation      :", mes.std())

print("Set average to 1 ...")
power_meter.sense.average.count = 1

power_meter.system.beeper.immediate()

