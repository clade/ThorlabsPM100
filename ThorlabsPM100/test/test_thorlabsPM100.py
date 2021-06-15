from __future__ import print_function
import unittest

from .. import ThorlabsPM100
from .fake_scpi import FakeSCPI


initial_value = {'READ':"1.23"}

class TestThorlabsPM100(unittest.TestCase):
    def setUp(self):
        inst = FakeSCPI()
        inst._record = initial_value.copy()
        self.inst = inst
        self.power_meter = ThorlabsPM100(inst)

    def test_read(self):
        self.assertEqual(self.power_meter.read, 1.23)

    def test_read_write(self):
        self.power_meter.sense.average.count = 10
        self.assertEqual(self.power_meter.sense.average.count, 10)

    def test_call(self):
        self.power_meter.system.beeper.immediate()
        self.assertTrue(self.inst._record['System:Beeper:IMMediate'])

    def test_some_function(self):
        self.power_meter.sense.power.dc.unit = 'DBM'
        self.assertEqual(self.inst._record['Sense:Power:Dc:UNIT'], 'DBM')

    def test_wavelength(self):
        self.power_meter.sense.correction.wavelength = 1550
        self.assertEqual(self.inst._record['Sense:Correction:WAVelength'], '1550nm')

