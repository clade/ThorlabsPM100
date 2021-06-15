import unittest
from ..VISA_wrapper_metaclass import *

from .fake_scpi import FakeSCPI

def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {})


class Generic(object):
    def __init__(self, intitial_values={}):
        self.inst = FakeSCPI()
        self.inst._record = intitial_values.copy()

    def _write(self, s):
        self.inst.write(s)

    def _ask(self, s):
        out = self.inst.query(s)
        if out : 
            return out
        raise Exception('No output for command {}'.format(s))

class ArgumentTypeTest(Group, with_metaclass(InstrumentMetaclass)):
    class number(GenericGetSetCommandClass):
        """ A simple number """
        cmd = "ArgTypTest:Number"
        value = Argument(0, ["<numeric_value>"])

    class min_max_number(GenericGetSetCommandClass):
        """Min Max Number"""
        cmd = "ArgTypTest:MMN"
        value = Argument(0, ["MINmum", "MAXimum", "<numeric_value>"])

    class with_unit(GenericGetSetCommandClass):
        """With unit"""
        cmd = "ArgTypTest:WU"
        value = Argument(0, ["<numeric_value>nm"])



class ChannelMachinGroup(Group, with_metaclass(InstrumentMetaclass)):

    class truc(GenericGetSetCommandClass):
        """ coucou """
        cmd = 'CH<X>:MACHIN:TRUC'
        value = Argument(0, [numbers.Number])

class ChannelGroup(IndexedGroup, with_metaclass(InstrumentMetaclass)):
    machin = ChannelMachinGroup
    var = '<X>'

    class testa(GenericGetSetCommandClass):
        """ coucou """
        cmd = 'CH<X>:TEST1'
        value = Argument(0, [TestValueBoundNumber(-1, 1)])

    class testb(GenericGetSetCommandClass):
        """ coucou """
        cmd = 'CH<X>:TEST'
        value = Argument(0, [TestValueBoundNumber(-1, 1)])
        freq = Argument(1, [numbers.Number])

class TestInstrument(Generic, InstrumentCommand, with_metaclass(InstrumentMetaclass)):

    class coucou_val(GenericGetCommandClass):
        """ This is a test method """
        cmd = 'COUCOU:VAL'
        value = Argument(0, ["PIErre", "MATHilde", numbers.Number],
                         default='Pierre')
        autre_valeur = Argument(1, [numbers.Number], default=3.14)

    channel = ChannelGroup
    arg_test = ArgumentTypeTest



class Test(unittest.TestCase):
    def test_many_arguments(self):
        scope = TestInstrument({'COUCOU:VAL':"10.4, 15.6"})
        self.assertEqual(scope.coucou_val, (10.4, 15.6))

    def test_min_max_number(self):
        scope = TestInstrument()
        scope.arg_test.min_max_number = "Min"
        self.assertEqual(scope.arg_test.min_max_number, 'Min')
        scope.arg_test.min_max_number = 3.14
        self.assertEqual(scope.arg_test.min_max_number, 3.14)
        
    def test_with_unit(self):
        scope = TestInstrument()
        scope.arg_test.with_unit = 1550
        self.assertEqual(scope.arg_test.with_unit, 1550)
        self.assertEqual(scope.inst._record["ArgTypTest:WU"], '1550nm')

    def test_channel(self):
        scope = TestInstrument({"CH2:MACHIN:TRUC":"123.4"})
        scope.channel[1].testb = 0.2, 4.5
        self.assertEqual(scope.channel[2].machin.truc, 123.4)

