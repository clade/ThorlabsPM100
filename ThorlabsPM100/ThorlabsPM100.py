# -*- coding: utf-8 -*-
from __future__ import print_function
from .VISA_wrapper_metaclass import (Group, IndexedGroup, InstrumentMetaclass,
Argument, GenericCommandClass, GenericGetCommandClass, GenericSetCommandClass,
GenericGetSetCommandClass, InstrumentCommand)

IndexedGroup.var = '<n>'

def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {})

class Generic(object):
    def __init__(self, inst, verbose=False):
        self._verbose = verbose
        self._inst = inst

    def _write(self, cmd):
        if self._verbose:
            print("Write command %s" % cmd)
        self._inst.write(cmd)

    def _ask(self, cmd):
        if self._verbose:
            print("Ask command %s ..." % cmd,)
        out = self._inst.ask(cmd)
        if self._verbose:
            print("recieve %s" % out)
        return out


class StatusQuestionable(Group, with_metaclass(InstrumentMetaclass)):

    class enable(GenericGetSetCommandClass):
        """Program the enable register"""
        cmd = 'Status:Questionable:ENABle'
        full_acces = 'status.questionable.enable'
        value = Argument(0, ["<value>"])

    class ntransition(GenericGetSetCommandClass):
        """Program the negative transition filter"""
        cmd = 'Status:Questionable:NTRansition'
        full_acces = 'status.questionable.ntransition'
        value = Argument(0, ["<value>"])

    class preset(GenericCommandClass):
        """Return status registers to default states."""
        cmd = 'Status:Questionable:PRESet'
        full_acces = 'status.questionable.preset'

    class ptransition(GenericGetSetCommandClass):
        """Program the positive transition filter"""
        cmd = 'Status:Questionable:PTRansition'
        full_acces = 'status.questionable.ptransition'
        value = Argument(0, ["<value>"])

    class event(GenericGetCommandClass):
        """Read the event register"""
        cmd = 'Status:Questionable:EVENt'
        full_acces = 'status.questionable.event'

    class condition(GenericGetCommandClass):
        """Read the condition register"""
        cmd = 'Status:Questionable:CONDition'
        full_acces = 'status.questionable.condition'


class StatusAuxillary(Group, with_metaclass(InstrumentMetaclass)):

    class ntransition(GenericGetSetCommandClass):
        """Program the negative transition filter"""
        cmd = 'Status:Auxillary:NTRansition'
        full_acces = 'status.auxillary.ntransition'
        value = Argument(0, ["<value>"])

    class ptransition(GenericGetSetCommandClass):
        """Program the positive transition filter"""
        cmd = 'Status:Auxillary:PTRansition'
        full_acces = 'status.auxillary.ptransition'
        value = Argument(0, ["<value>"])

    class enable(GenericGetSetCommandClass):
        """Program the enable register"""
        cmd = 'Status:Auxillary:ENABle'
        full_acces = 'status.auxillary.enable'
        value = Argument(0, ["<value>"])

    class event(GenericGetCommandClass):
        """Read the event register"""
        cmd = 'Status:Auxillary:EVENt'
        full_acces = 'status.auxillary.event'

    class condition(GenericGetCommandClass):
        """Read the condition register"""
        cmd = 'Status:Auxillary:CONDition'
        full_acces = 'status.auxillary.condition'


class StatusOperation(Group, with_metaclass(InstrumentMetaclass)):

    class ntransition(GenericGetSetCommandClass):
        """Program the negative transition filter"""
        cmd = 'Status:Operation:NTRansition'
        full_acces = 'status.operation.ntransition'
        value = Argument(0, ["<value>"])

    class ptransition(GenericGetSetCommandClass):
        """Program the positive transition filter"""
        cmd = 'Status:Operation:PTRansition'
        full_acces = 'status.operation.ptransition'
        value = Argument(0, ["<value>"])

    class enable(GenericGetSetCommandClass):
        """Program the enable register"""
        cmd = 'Status:Operation:ENABle'
        full_acces = 'status.operation.enable'
        value = Argument(0, ["<value>"])

    class event(GenericGetCommandClass):
        """Read the event register"""
        cmd = 'Status:Operation:EVENt'
        full_acces = 'status.operation.event'

    class condition(GenericGetCommandClass):
        """Read the condition register"""
        cmd = 'Status:Operation:CONDition'
        full_acces = 'status.operation.condition'


class StatusMeasurement(Group, with_metaclass(InstrumentMetaclass)):

    class ntransition(GenericGetSetCommandClass):
        """Program the negative transition filter"""
        cmd = 'Status:Measurement:NTRansition'
        full_acces = 'status.measurement.ntransition'
        value = Argument(0, ["<value>"])

    class ptransition(GenericGetSetCommandClass):
        """Program the positive transition filter"""
        cmd = 'Status:Measurement:PTRansition'
        full_acces = 'status.measurement.ptransition'
        value = Argument(0, ["<value>"])

    class enable(GenericGetSetCommandClass):
        """Program the enable register"""
        cmd = 'Status:Measurement:ENABle'
        full_acces = 'status.measurement.enable'
        value = Argument(0, ["<value>"])

    class event(GenericGetCommandClass):
        """Read the event register"""
        cmd = 'Status:Measurement:EVENt'
        full_acces = 'status.measurement.event'

    class condition(GenericGetCommandClass):
        """Read the condition register"""
        cmd = 'Status:Measurement:CONDition'
        full_acces = 'status.measurement.condition'


class Status(Group, with_metaclass(InstrumentMetaclass)):
    questionable = StatusQuestionable
    auxillary = StatusAuxillary
    operation = StatusOperation
    measurement = StatusMeasurement


class ConfigureScalarCurrent(Group, with_metaclass(InstrumentMetaclass)):

    class dc(GenericCommandClass):
        """Configure for current measurement"""
        cmd = 'Configure:Scalar:Current:DC'
        full_acces = 'configure.scalar.current.dc'


class ConfigureScalarVoltage(Group, with_metaclass(InstrumentMetaclass)):

    class dc(GenericCommandClass):
        """Configure for voltage measurement"""
        cmd = 'Configure:Scalar:Voltage:DC'
        full_acces = 'configure.scalar.voltage.dc'


class ConfigureScalar(Group, with_metaclass(InstrumentMetaclass)):
    current = ConfigureScalarCurrent
    voltage = ConfigureScalarVoltage

    class temperature(GenericCommandClass):
        """Configure for sensor temperature measurement"""
        cmd = 'Configure:Scalar:TEMPerature'
        full_acces = 'configure.scalar.temperature'

    class power(GenericCommandClass):
        """Configure for power measurement"""
        cmd = 'Configure:Scalar:POWer'
        full_acces = 'configure.scalar.power'

    class energy(GenericCommandClass):
        """Configure for energy measurement // PM100D only"""
        cmd = 'Configure:Scalar:ENERgy'
        full_acces = 'configure.scalar.energy'

    class resistance(GenericCommandClass):
        """Configure for sensor presence resistance measurement"""
        cmd = 'Configure:Scalar:RESistance'
        full_acces = 'configure.scalar.resistance'

    class frequency(GenericCommandClass):
        """Configure for frequency measurement // PM100D only"""
        cmd = 'Configure:Scalar:FREQuency'
        full_acces = 'configure.scalar.frequency'

    class pdensity(GenericCommandClass):
        """Configure for power density measurement"""
        cmd = 'Configure:Scalar:PDENsity'
        full_acces = 'configure.scalar.pdensity'

    class edensity(GenericCommandClass):
        """Configure for energy density measurement // PM100D only"""
        cmd = 'Configure:Scalar:EDENsity'
        full_acces = 'configure.scalar.edensity'


class Configure(Group, with_metaclass(InstrumentMetaclass)):
    scalar = ConfigureScalar


class Calibration(Group, with_metaclass(InstrumentMetaclass)):

    class string(GenericGetCommandClass):
        """Returns a human readable calibration string.
        This is a query only command.
        The response is formatted as string response data.
        """
        cmd = 'Calibration:STRing'
        full_acces = 'calibration.string'


class MeasureScalarCurrent(Group, with_metaclass(InstrumentMetaclass)):

    class dc(GenericCommandClass):
        """Performs a current measurement"""
        cmd = 'Measure:Scalar:Current:DC'
        full_acces = 'measure.scalar.current.dc'


class MeasureScalarVoltage(Group, with_metaclass(InstrumentMetaclass)):

    class dc(GenericCommandClass):
        """Performs a voltage measurement"""
        cmd = 'Measure:Scalar:Voltage:DC'
        full_acces = 'measure.scalar.voltage.dc'


class MeasureScalar(Group, with_metaclass(InstrumentMetaclass)):
    current = MeasureScalarCurrent
    voltage = MeasureScalarVoltage

    class temperature(GenericCommandClass):
        """Performs a sensor temperature measurement"""
        cmd = 'Measure:Scalar:TEMPerature'
        full_acces = 'measure.scalar.temperature'

    class power(GenericCommandClass):
        """Performs a power measurement"""
        cmd = 'Measure:Scalar:POWer'
        full_acces = 'measure.scalar.power'

    class energy(GenericCommandClass):
        """Performs a energy measurement // PM100D only"""
        cmd = 'Measure:Scalar:ENERgy'
        full_acces = 'measure.scalar.energy'

    class resistance(GenericCommandClass):
        """Performs a sensor presence resistance measurement"""
        cmd = 'Measure:Scalar:RESistance'
        full_acces = 'measure.scalar.resistance'

    class frequency(GenericCommandClass):
        """Performs a frequency measurement // PM100D only"""
        cmd = 'Measure:Scalar:FREQuency'
        full_acces = 'measure.scalar.frequency'

    class pdensity(GenericCommandClass):
        """Performs a power density measurement"""
        cmd = 'Measure:Scalar:PDENsity'
        full_acces = 'measure.scalar.pdensity'

    class edensity(GenericCommandClass):
        """Performs a energy density measurement // PM100D only"""
        cmd = 'Measure:Scalar:EDENsity'
        full_acces = 'measure.scalar.edensity'


class Measure(Group, with_metaclass(InstrumentMetaclass)):
    scalar = MeasureScalar


class SystemError(Group, with_metaclass(InstrumentMetaclass)):

    class next(GenericGetCommandClass):
        """Returns the latest <error code, “message”>. (SCPI Vol.2 §21.8.8)"""
        cmd = 'System:Error:NEXT'
        full_acces = 'system.error.next'


class SystemSensor(Group, with_metaclass(InstrumentMetaclass)):

    class idn(GenericGetCommandClass):
        """Query information about the connected sensor.
        This is a query only command.
        The response consists of the following fields:
        """
        cmd = 'System:Sensor:IDN'
        full_acces = 'system.sensor.idn'


class SystemBeeper(Group, with_metaclass(InstrumentMetaclass)):

    class state(GenericGetSetCommandClass):
        """Activate/deactivate the beeper. (SCPI Vol.2 §21.2.3)"""
        cmd = 'System:Beeper:STATe'
        full_acces = 'system.beeper.state'
        value = Argument(0, ["ON", "1", "OFF", "0"])

    class immediate(GenericCommandClass):
        """Issue an audible signal. (SCPI Vol.2 §21.2.2)"""
        cmd = 'System:Beeper:IMMediate'
        full_acces = 'system.beeper.immediate'


class System(Group, with_metaclass(InstrumentMetaclass)):
    error = SystemError
    sensor = SystemSensor
    beeper = SystemBeeper

    class time(GenericGetSetCommandClass):
        """Sets the instrument‟s clock. (SCPI Vol.2 §21.19) // PM100D only"""
        cmd = 'System:TIME'
        full_acces = 'system.time'
        value = Argument(0, ["<hour>,<min>,<sec>"])

    class lfrequency(GenericGetSetCommandClass):
        """Sets the instrument‟s line frequency setting to 50 or 60Hz.
        (SCPI Vol.2 §21.13)
        """
        cmd = 'System:LFRequency'
        full_acces = 'system.lfrequency'
        value = Argument(0, ["<numeric_value>"])

    class version(GenericGetCommandClass):
        """Query level of SCPI standard (1999.0) . (SCPI Vol.2 §21.21)"""
        cmd = 'System:VERSion'
        full_acces = 'system.version'

    class date(GenericGetSetCommandClass):
        """Sets the instrument‟s calendar. (SCPI Vol.2 §21.7) // PM100D only"""
        cmd = 'System:DATE'
        full_acces = 'system.date'
        value = Argument(0, ["<year>,<month>,<day>"])


class Initiate(Group, with_metaclass(InstrumentMetaclass)):

    class immediate(GenericCommandClass):
        """Start measurement"""
        cmd = 'Initiate:IMMediate'
        full_acces = 'initiate.immediate'


class SenseEnergyRange(Group, with_metaclass(InstrumentMetaclass)):

    class upper(GenericGetSetCommandClass):
        """Sets the energy range in J"""
        cmd = 'Sense:Energy:Range:UPPer'
        full_acces = 'sense.energy.range.upper'
        value = Argument(0, ["MINmum", "MAXimum", "<numeric_valuje>J"])

    class maximum_upper(GenericGetCommandClass):
        """Queries the maximum energy range"""
        cmd = 'Sense:Energy:Range:UPPer MAXimum'
        full_acces = 'sense.energy.range.maximum_upper'

    class minimum_upper(GenericGetCommandClass):
        """Queries the minimum energy range"""
        cmd = 'Sense:Energy:Range:UPPer MINimum'
        full_acces = 'sense.energy.range.minimum_upper'


class SenseEnergyReference(Group, with_metaclass(InstrumentMetaclass)):

    class state(GenericGetSetCommandClass):
        """Switches to delta mode"""
        cmd = 'Sense:Energy:Reference:STATe'
        full_acces = 'sense.energy.reference.state'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class value(GenericGetSetCommandClass):
        """Sets a delta reference value in J"""
        cmd = 'Sense:Energy:Reference:value'
        full_acces = 'sense.energy.reference.value'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>J"])


class SenseEnergy(Group, with_metaclass(InstrumentMetaclass)):
    range = SenseEnergyRange
    reference = SenseEnergyReference

    class default_reference(GenericGetCommandClass):
        """Queries the default delta reference value"""
        cmd = 'Sense:Energy:REFerence DEFault'
        full_acces = 'sense.energy.default_reference'

    class maximum_reference(GenericGetCommandClass):
        """Queries the maximum delta reference value"""
        cmd = 'Sense:Energy:REFerence MAXimum'
        full_acces = 'sense.energy.maximum_reference'

    class minimum_reference(GenericGetCommandClass):
        """Queries the minimum delta reference value"""
        cmd = 'Sense:Energy:REFerence MINimum'
        full_acces = 'sense.energy.minimum_reference'


class SensePowerDcReference(Group, with_metaclass(InstrumentMetaclass)):

    class state(GenericGetSetCommandClass):
        """Switches to delta mode"""
        cmd = 'Sense:Power:Dc:Reference:STATe'
        full_acces = 'sense.power.dc.reference.state'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class value(GenericGetSetCommandClass):
        """Sets a delta reference value in W"""
        cmd = 'Sense:Power:Dc:Reference:value'
        full_acces = 'sense.power.dc.reference.value'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>W"])


class SensePowerDcRange(Group, with_metaclass(InstrumentMetaclass)):

    class auto(GenericGetSetCommandClass):
        """Switches the auto-ranging function on and off"""
        cmd = 'Sense:Power:Dc:Range:AUTO'
        full_acces = 'sense.power.dc.range.auto'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class maximum_upper(GenericGetCommandClass):
        """Queries the maximum current range"""
        cmd = 'Sense:Power:Dc:Range:UPPer MAXimum'
        full_acces = 'sense.power.dc.range.maximum_upper'

    class minimum_upper(GenericGetCommandClass):
        """Queries the minimum current range"""
        cmd = 'Sense:Power:Dc:Range:UPPer MINimum'
        full_acces = 'sense.power.dc.range.minimum_upper'

    class upper(GenericGetSetCommandClass):
        """Sets the current range in W"""
        cmd = 'Sense:Power:Dc:Range:UPPer'
        full_acces = 'sense.power.dc.range.upper'
        value = Argument(0, ["MINmum", "MAXimum", "<numeric_valuje>W"])


class SensePowerDc(Group, with_metaclass(InstrumentMetaclass)):
    reference = SensePowerDcReference
    range = SensePowerDcRange

    class default_reference(GenericGetCommandClass):
        """Queries the default delta reference value"""
        cmd = 'Sense:Power:Dc:REFerence DEFault'
        full_acces = 'sense.power.dc.default_reference'

    class maximum_reference(GenericGetCommandClass):
        """Queries the maximum delta reference value"""
        cmd = 'Sense:Power:Dc:REFerence MAXimum'
        full_acces = 'sense.power.dc.maximum_reference'

    class minimum_reference(GenericGetCommandClass):
        """Queries the minimum delta reference value"""
        cmd = 'Sense:Power:Dc:REFerence MINimum'
        full_acces = 'sense.power.dc.minimum_reference'

    class unit(GenericGetSetCommandClass):
        """Sets the power unit W or dBm"""
        cmd = 'Sense:Power:Dc:UNIT'
        full_acces = 'sense.power.dc.unit'
        value = Argument(0, ["W", "DBM"])


class SensePower(Group, with_metaclass(InstrumentMetaclass)):
    dc = SensePowerDc


class SenseAverage(Group, with_metaclass(InstrumentMetaclass)):

    class count(GenericGetSetCommandClass):
        """Sets the averaging rate (1 sample takes approx. 3ms)"""
        cmd = 'Sense:Average:COUNt'
        full_acces = 'sense.average.count'
        value = Argument(0, ["<value>"])


class SenseCurrentDcRange(Group, with_metaclass(InstrumentMetaclass)):

    class auto(GenericGetSetCommandClass):
        """Switches the auto-ranging function on and off"""
        cmd = 'Sense:Current:Dc:Range:AUTO'
        full_acces = 'sense.current.dc.range.auto'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class maximum_upper(GenericGetCommandClass):
        """Queries the maximum current range"""
        cmd = 'Sense:Current:Dc:Range:UPPer MAXimum'
        full_acces = 'sense.current.dc.range.maximum_upper'

    class minimum_upper(GenericGetCommandClass):
        """Queries the minimum current range"""
        cmd = 'Sense:Current:Dc:Range:UPPer MINimum'
        full_acces = 'sense.current.dc.range.minimum_upper'

    class upper(GenericGetSetCommandClass):
        """Sets the current range in A"""
        cmd = 'Sense:Current:Dc:Range:UPPer'
        full_acces = 'sense.current.dc.range.upper'
        value = Argument(0, ["MINmum", "MAXimum", "<numeric_valuje>A"])


class SenseCurrentDcReference(Group, with_metaclass(InstrumentMetaclass)):

    class state(GenericGetSetCommandClass):
        """Switches to delta mode"""
        cmd = 'Sense:Current:Dc:Reference:STATe'
        full_acces = 'sense.current.dc.reference.state'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class value(GenericGetSetCommandClass):
        """Sets a delta reference value in A"""
        cmd = 'Sense:Current:Dc:Reference:value'
        full_acces = 'sense.current.dc.reference.value'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>A"])


class SenseCurrentDc(Group, with_metaclass(InstrumentMetaclass)):
    range = SenseCurrentDcRange
    reference = SenseCurrentDcReference

    class default_reference(GenericGetCommandClass):
        """Queries the default delta reference value"""
        cmd = 'Sense:Current:Dc:REFerence DEFault'
        full_acces = 'sense.current.dc.default_reference'

    class maximum_reference(GenericGetCommandClass):
        """Queries the maximum delta reference value"""
        cmd = 'Sense:Current:Dc:REFerence MAXimum'
        full_acces = 'sense.current.dc.maximum_reference'

    class minimum_reference(GenericGetCommandClass):
        """Queries the minimum delta reference value"""
        cmd = 'Sense:Current:Dc:REFerence MINimum'
        full_acces = 'sense.current.dc.minimum_reference'


class SenseCurrent(Group, with_metaclass(InstrumentMetaclass)):
    dc = SenseCurrentDc


class SenseFrequencyRange(Group, with_metaclass(InstrumentMetaclass)):

    class upper(GenericGetCommandClass):
        """Queries the frequency range // PM100D only"""
        cmd = 'Sense:Frequency:Range:UPPer'
        full_acces = 'sense.frequency.range.upper'

    class lower(GenericGetCommandClass):
        """Queries the frequency range // PM100D only"""
        cmd = 'Sense:Frequency:Range:LOWer'
        full_acces = 'sense.frequency.range.lower'


class SenseFrequency(Group, with_metaclass(InstrumentMetaclass)):
    range = SenseFrequencyRange


class SenseVoltageDcRange(Group, with_metaclass(InstrumentMetaclass)):

    class auto(GenericGetSetCommandClass):
        """Switches the auto-ranging function on and off"""
        cmd = 'Sense:Voltage:Dc:Range:AUTO'
        full_acces = 'sense.voltage.dc.range.auto'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class maximum_upper(GenericGetCommandClass):
        """Queries the maximum current range"""
        cmd = 'Sense:Voltage:Dc:Range:UPPer MAXimum'
        full_acces = 'sense.voltage.dc.range.maximum_upper'

    class minimum_upper(GenericGetCommandClass):
        """Queries the minimum current range"""
        cmd = 'Sense:Voltage:Dc:Range:UPPer MINimum'
        full_acces = 'sense.voltage.dc.range.minimum_upper'

    class upper(GenericGetSetCommandClass):
        """Sets the current range in V"""
        cmd = 'Sense:Voltage:Dc:Range:UPPer'
        full_acces = 'sense.voltage.dc.range.upper'
        value = Argument(0, ["MINmum", "MAXimum", "<numeric_valuje>V"])


class SenseVoltageDc(Group, with_metaclass(InstrumentMetaclass)):
    range = SenseVoltageDcRange

    class default_reference(GenericGetCommandClass):
        """Queries the delta default reference value"""
        cmd = 'Sense:Voltage:Dc:REFerence DEFault'
        full_acces = 'sense.voltage.dc.default_reference'

    class reference(GenericGetSetCommandClass):
        """Sets a delta reference value in V"""
        cmd = 'Sense:Voltage:Dc:REFerence'
        full_acces = 'sense.voltage.dc.reference'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>V"])

    class maximum_reference(GenericGetCommandClass):
        """Queries the delta maximum reference value"""
        cmd = 'Sense:Voltage:Dc:REFerence MAXimum'
        full_acces = 'sense.voltage.dc.maximum_reference'

    class state(GenericGetSetCommandClass):
        """Switches to delta mode"""
        cmd = 'Sense:Voltage:Dc:STATe'
        full_acces = 'sense.voltage.dc.state'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class minimum_reference(GenericGetCommandClass):
        """Queries the delta minimum reference value"""
        cmd = 'Sense:Voltage:Dc:REFerence MINimum'
        full_acces = 'sense.voltage.dc.minimum_reference'


class SenseVoltage(Group, with_metaclass(InstrumentMetaclass)):
    dc = SenseVoltageDc


class SenseCorrectionPowerPdiode(Group, with_metaclass(InstrumentMetaclass)):

    class maximum_response(GenericGetCommandClass):
        """Queries the photodiode maximum response value"""
        cmd = 'Sense:Correction:Power:Pdiode:RESPonse MAXimum'
        full_acces = 'sense.correction.power.pdiode.maximum_response'

    class default_response(GenericGetCommandClass):
        """Queries the photodiode default response value"""
        cmd = 'Sense:Correction:Power:Pdiode:RESPonse DEFault'
        full_acces = 'sense.correction.power.pdiode.default_response'

    class response(GenericGetSetCommandClass):
        """Sets the photodiode response value in A/W"""
        cmd = 'Sense:Correction:Power:Pdiode:RESPonse'
        full_acces = 'sense.correction.power.pdiode.response'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>A"])

    class minimum_response(GenericGetCommandClass):
        """Queries the photodiode minimum response value"""
        cmd = 'Sense:Correction:Power:Pdiode:RESPonse MINimum'
        full_acces = 'sense.correction.power.pdiode.minimum_response'


class SenseCorrectionPower(Group, with_metaclass(InstrumentMetaclass)):
    pdiode = SenseCorrectionPowerPdiode


class SenseCorrectionLossInput(Group, with_metaclass(InstrumentMetaclass)):

    class default_magnitude(GenericGetCommandClass):
        """Queries the user default attenuation factor"""
        cmd = 'Sense:Correction:Loss:Input:MAGNitude DEFault'
        full_acces = 'sense.correction.loss.input.default_magnitude'

    class minimum_magnitude(GenericGetCommandClass):
        """Queries the user minimum attenuation factor"""
        cmd = 'Sense:Correction:Loss:Input:MAGNitude MINimum'
        full_acces = 'sense.correction.loss.input.minimum_magnitude'

    class magnitude(GenericGetSetCommandClass):
        """Sets a user attenuation factor in dB"""
        cmd = 'Sense:Correction:Loss:Input:MAGNitude'
        full_acces = 'sense.correction.loss.input.magnitude'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>"])

    class maximum_magnitude(GenericGetCommandClass):
        """Queries the user maximum attenuation factor"""
        cmd = 'Sense:Correction:Loss:Input:MAGNitude MAXimum'
        full_acces = 'sense.correction.loss.input.maximum_magnitude'


class SenseCorrectionLoss(Group, with_metaclass(InstrumentMetaclass)):
    input = SenseCorrectionLossInput


class SenseCorrectionEnergyPyro(Group, with_metaclass(InstrumentMetaclass)):

    class maximum_response(GenericGetCommandClass):
        """Queries the pyro-detectro maximum response value"""
        cmd = 'Sense:Correction:Energy:Pyro:RESPonse MAXimum'
        full_acces = 'sense.correction.energy.pyro.maximum_response'

    class default_response(GenericGetCommandClass):
        """Queries the pyro-detectro default response value"""
        cmd = 'Sense:Correction:Energy:Pyro:RESPonse DEFault'
        full_acces = 'sense.correction.energy.pyro.default_response'

    class response(GenericGetSetCommandClass):
        """Sets the pyro-detector response value in V/J"""
        cmd = 'Sense:Correction:Energy:Pyro:RESPonse'
        full_acces = 'sense.correction.energy.pyro.response'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>V"])

    class minimum_response(GenericGetCommandClass):
        """Queries the pyro-detectro minimum response value"""
        cmd = 'Sense:Correction:Energy:Pyro:RESPonse MINimum'
        full_acces = 'sense.correction.energy.pyro.minimum_response'


class SenseCorrectionEnergy(Group, with_metaclass(InstrumentMetaclass)):
    pyro = SenseCorrectionEnergyPyro


class SenseCorrectionCollectZero(Group, with_metaclass(InstrumentMetaclass)):

    class initiate(GenericCommandClass):
        """Performs zero adjustment routine"""
        cmd = 'Sense:Correction:Collect:Zero:INITiate'
        full_acces = 'sense.correction.collect.zero.initiate'

    class state(GenericGetCommandClass):
        """Queries the zero adjustment routine state"""
        cmd = 'Sense:Correction:Collect:Zero:STATe'
        full_acces = 'sense.correction.collect.zero.state'

    class abort(GenericCommandClass):
        """Aborts zero adjustment routine"""
        cmd = 'Sense:Correction:Collect:Zero:ABORt'
        full_acces = 'sense.correction.collect.zero.abort'

    class magnitude(GenericGetCommandClass):
        """Queries the zero value"""
        cmd = 'Sense:Correction:Collect:Zero:MAGNitude'
        full_acces = 'sense.correction.collect.zero.magnitude'


class SenseCorrectionCollect(Group, with_metaclass(InstrumentMetaclass)):
    zero = SenseCorrectionCollectZero


class SenseCorrection(Group, with_metaclass(InstrumentMetaclass)):
    power = SenseCorrectionPower
    loss = SenseCorrectionLoss
    energy = SenseCorrectionEnergy
    collect = SenseCorrectionCollect

    class maximum_beamdiameter(GenericGetCommandClass):
        """Sets the maximum beam diameter in mm"""
        cmd = 'Sense:Correction:BEAMdiameter MAXimum'
        full_acces = 'sense.correction.maximum_beamdiameter'

    class minimum_beamdiameter(GenericGetCommandClass):
        """Sets the minimum beam diameter in mm"""
        cmd = 'Sense:Correction:BEAMdiameter MINimum'
        full_acces = 'sense.correction.minimum_beamdiameter'

    class beamdiameter(GenericGetSetCommandClass):
        """Sets the beam diameter in mm"""
        cmd = 'Sense:Correction:BEAMdiameter'
        full_acces = 'sense.correction.beamdiameter'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>mm"])

    class default_beamdiameter(GenericGetCommandClass):
        """Sets the default beam diameter in mm"""
        cmd = 'Sense:Correction:BEAMdiameter DEFault'
        full_acces = 'sense.correction.default_beamdiameter'

    class minimum_wavelength(GenericGetCommandClass):
        """Queries the minimum operation wavelength"""
        cmd = 'Sense:Correction:WAVelength MINimum'
        full_acces = 'sense.correction.minimum_wavelength'

    class maximum_wavelength(GenericGetCommandClass):
        """Queries the maximum operation wavelength"""
        cmd = 'Sense:Correction:WAVelength MAXimum'
        full_acces = 'sense.correction.maximum_wavelength'

    class wavelength(GenericGetSetCommandClass):
        """Sets the operation wavelength in nm"""
        cmd = 'Sense:Correction:WAVelength'
        full_acces = 'sense.correction.wavelength'
        value = Argument(0, ["MINimum", "MAXimum", "<numeric_value>nm"])


class SensePeakdetector(Group, with_metaclass(InstrumentMetaclass)):

    class threshold(GenericGetSetCommandClass):
        """Sets the trigger level in % for the energy mode
        """
        cmd = 'Sense:Peakdetector:THReshold'
        full_acces = 'sense.peakdetector.threshold'
        value = Argument(0, ["MINimum","MAXimum","DEFault","<numeric_value>nm"])

    class default_threshold(GenericGetCommandClass):
        """Queries the default trigger level setting"""
        cmd = 'Sense:Peakdetector:THReshold DEFault'
        full_acces = 'sense.peakdetector.default_threshold'

    class maximum_threshold(GenericGetCommandClass):
        """Queries the maximum trigger level setting"""
        cmd = 'Sense:Peakdetector:THReshold MAXimum'
        full_acces = 'sense.peakdetector.maximum_threshold'

    class minimum_threshold(GenericGetCommandClass):
        """Queries the minimum trigger level setting"""
        cmd = 'Sense:Peakdetector:THReshold MINimum'
        full_acces = 'sense.peakdetector.minimum_threshold'


class Sense(Group, with_metaclass(InstrumentMetaclass)):
    energy = SenseEnergy
    power = SensePower
    average = SenseAverage
    current = SenseCurrent
    frequency = SenseFrequency
    voltage = SenseVoltage
    correction = SenseCorrection
    peakdetector = SensePeakdetector


class InputAdapter(Group, with_metaclass(InstrumentMetaclass)):

    class type(GenericSetCommandClass):
        """Sets default sensor adapter type"""
        cmd = 'Input:Adapter:TYPE'
        full_acces = 'input.adapter.type'
        value = Argument(0, ["PHOTodiode", "THERmal", "PYRo"])


class InputThermopileAccelerator(Group, with_metaclass(InstrumentMetaclass)):

    class tau(GenericGetSetCommandClass):
        """Sets thermopile time constant tau(0-63%) in s"""
        cmd = 'Input:Thermopile:Accelerator:TAU'
        full_acces = 'input.thermopile.accelerator.tau'
        value = Argument(0, ["MINimum", "MAXimum", "DEFault",
                             "<numeric_value>s"])

    class state(GenericGetSetCommandClass):
        """Sets the thermopile accelerator state"""
        cmd = 'Input:Thermopile:Accelerator:STATe'
        full_acces = 'input.thermopile.accelerator.state'
        value = Argument(0, ["OFF", "0", "ON", "1"])

    class default_tau(GenericGetCommandClass):
        """Queries the default thermopile time constant tau(0-63%) in s"""
        cmd = 'Input:Thermopile:Accelerator:TAU DEFault'
        full_acces = 'input.thermopile.accelerator.default_tau'

    class minimum_tau(GenericGetCommandClass):
        """Queries the minimum thermopile time constant tau(0-63%) in s"""
        cmd = 'Input:Thermopile:Accelerator:TAU MINimum'
        full_acces = 'input.thermopile.accelerator.minimum_tau'

    class maximum_tau(GenericGetCommandClass):
        """Queries the maximum thermopile time constant tau(0-63%) in s"""
        cmd = 'Input:Thermopile:Accelerator:TAU MAXimum'
        full_acces = 'input.thermopile.accelerator.maximum_tau'


class InputThermopile(Group, with_metaclass(InstrumentMetaclass)):
    accelerator = InputThermopileAccelerator


class InputPdiodeFilterLpass(Group, with_metaclass(InstrumentMetaclass)):

    class state(GenericGetSetCommandClass):
        """Sets the bandwidth of the photodiode input stage"""
        cmd = 'Input:Pdiode:Filter:Lpass:STATe'
        full_acces = 'input.pdiode.filter.lpass.state'
        value = Argument(0, ["OFF", "0", "ON", "1"])


class InputPdiodeFilter(Group, with_metaclass(InstrumentMetaclass)):
    lpass = InputPdiodeFilterLpass


class InputPdiode(Group, with_metaclass(InstrumentMetaclass)):
    filter = InputPdiodeFilter


class Input(Group, with_metaclass(InstrumentMetaclass)):
    adapter = InputAdapter
    thermopile = InputThermopile
    pdiode = InputPdiode


class Display(Group, with_metaclass(InstrumentMetaclass)):

    class contrast(GenericGetSetCommandClass):
        """Set the display contrast. (SCPI Vol.2 §8.4) // PM100D only"""
        cmd = 'Display:CONTrast'
        full_acces = 'display.contrast'
        value = Argument(0, ["<value>"])

    class brightness(GenericGetSetCommandClass):
        """Set the display birghtness. (SCPI Vol.2 §8.2)"""
        cmd = 'Display:BRIGhtness'
        full_acces = 'display.brightness'
        value = Argument(0, ["<value>"])


class ThorlabsPM100(Generic, InstrumentCommand, with_metaclass(InstrumentMetaclass)):
    status = Status
    configure = Configure
    calibration = Calibration
    measure = Measure
    system = System
    initiate = Initiate
    sense = Sense
    input = Input
    display = Display

    class read(GenericGetCommandClass):
        """Start new measurement and read data (SCPI Vol.2 §3.3)"""
        cmd = 'READ'
        full_acces = 'read'

    class fetch(GenericGetCommandClass):
        """Read last measurement data (SCPI Vol.2 §3.2)"""
        cmd = 'FETCh'
        full_acces = 'fetch'

    class abort(GenericCommandClass):
        """Abort measurement"""
        cmd = 'ABORt'
        full_acces = 'abort'

    class getconfigure(GenericGetCommandClass):
        """Query the current measurement configuration."""
        cmd = 'CONFigure'
        full_acces = 'getconfigure'
