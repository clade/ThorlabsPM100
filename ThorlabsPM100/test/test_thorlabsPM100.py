from __future__ import print_function
import unittest

from .. import ThorlabsPM100

class FakeSCPI(object):
    _record = {}
    def write(self, val):
        if ' ' in val:
            cmd, vals = val.split(' ')
            self._record[cmd] = vals
        else:
#            print('WRITE', val)
            self._record[val] = True

    def ask(self, val):
        assert val[-1]=='?'
        out = self._record.get(val[:-1], '')
#        print('ASK', val,'...', out)
        return out


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
