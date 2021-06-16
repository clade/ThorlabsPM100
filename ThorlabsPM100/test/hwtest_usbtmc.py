import unittest


from ..usbtmc import USBTMC
from .. import ThorlabsPM100


inst = USBTMC()
power_meter = ThorlabsPM100(inst, verbose=True)

class TestHW(unittest.TestCase):
    def test_wavelength(self):
        old_value = power_meter.sense.correction.wavelength
        power_meter.sense.correction.wavelength = 780
        self.assertEqual(power_meter.sense.correction.wavelength, 780)
        power_meter.sense.correction.wavelength = old_value

        with self.assertRaises(Exception) as context:
            power_meter.sense.correction.wavelength = 10

        self.assertIn('Wavelength is', str(context.exception))

    def test_configuration(self):
        power_meter.configure.scalar.power()
        self.assertEqual(power_meter.getconfigure, 'POW')
        power_meter.configure.scalar.current.dc()
        self.assertEqual(power_meter.getconfigure, 'CURR')

if __name__=='__main__':
    power_meter.configure.scalar.power()
    print(power_meter._inst.query('READ?'))
    power_meter.configure.scalar.current.dc()
    print(power_meter.getconfigure)
