# -*- coding: utf-8 -*-
"""This module convert VISA command to methods

For example, from a command like "BEGin:End VALue" the programm
will generate methods get_begin_end, set_begin_end and a property
begin_end using those methods.

There is a full example at the end of this file

"""
from __future__ import print_function
import re
import numbers


class TestValue(object):
    """Class use to test the paramters

    This class implement the test method the return
    either None (if the test failed) or a string to format the value.
    """
    def test(self, value):
        if self.condition(value):
            return self.to_string(value)
        else:
            return None

    def to_string(self, value):
        return str(value)

    def condition(self, value):
        return False

    def from_string(self, val):
        return _try_to_convert_to_number(val)


class TestValueFromEnum(TestValue):
    def __init__(self, values, replacement=None):
        if replacement is None:
            replacement = enum_value._keys
        self.replacement = replacement
        self.values = values

    def to_string(self, value):
        if isinstance(value, type(self.values[0])):
            i = self.values._values.index(value)
            return self.replacement[i]
        else:
            i = self.values._keys.index(value)
            return self.replacement[i]

    def condition(self, value):
        return (value in self.values._values) or (value in self.values._keys)

    def __repr__(self):
        return 'from enum %s' % self.values._keys.__str__()


class TestValueFromType(TestValue):
    """ Test if a value is from a given type """
    def __init__(self, tpe):
        self.type = tpe

    def condition(self, value):
        return isinstance(value, self.type)

    def __repr__(self):
        return 'of type %s' % self.type.__name__


class TestValueWithUnit(TestValue):
    """ Test if a value is from a given type """
    def __init__(self, tpe, unit):
        self.type = tpe
        self.unit = unit

    def condition(self, value):
        return isinstance(value, self.type)

    def to_string(self, value):
        return str(value)+self.unit

    def from_string(self, val):
        if not val.endswith(self.unit):
            return val
        val = val[:-len(self.unit)]
        return _try_to_convert_to_number(val)

class TestValueFromRE(TestValue):
    """ Test a value using a regular expression """
    def __init__(self, re):
        self.re = re

    def condition(self, value):
        return re.match(value)

    def __repr__(self):
        return 'match %s' % self.re


class TestValueBoundNumber(TestValue):
    """ Test if a value is a number within bounds """
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def condition(self, value):
        return isinstance(value, numbers.Number) and value>=self.minimum and value<=self.maximum 

    def __repr__(self):
        return 'in between %s and %s' % (self.minimum, self.maximum)


class TestValueFromValue(TestValue):
    """ Test if a value is equal to a given one """
    def __init__(self, val):
        self.val = val

    def condition(self, value):
        return value == self.val

    def __repr__(self):
        return 'equal to %s' % self.val


def _short_version(s):
    """Returns the short version of a string

    _short_version('COUPling')=='COUP'
    """
    sl = s.lower()
    return ''.join([c for i, c in enumerate(s) if s[i] != sl[i]])


class TestValueFromString(TestValue):
    """ Test a value by comparing to a string.
    If the string is CAPsmall then test for capsmall and cap.
    This test is not case sensitive
    """
    def __init__(self, val):
        self.initial_val = val
        self.val = val.lower()
        self.val_short = _short_version(val).lower()

    def condition(self, value):
        return str(value).lower()==self.val or str(value).lower()==self.val_short

    def __repr__(self):
        return 'equal to %s or equal to %s' % (self.initial_val,
                                               self.val_short)


def _convert_value_to_TestValue(val):
    if isinstance(val, TestValue):
        return val
    elif isinstance(val, type):
        return TestValueFromType(val)
    elif isinstance(val, type(re.compile('po'))):
        return TestValueFromRE(val)
    elif isinstance(val, str) or isinstance(val, unicode):
        return TestValueFromString(val)
    else:
        return TestValueFromValue(val)


def _convert_list_value_to_list_of_TestValue(lst):
    try:
        return map(_convert_value_to_TestValue, lst)
    except TypeError:
        return map(_convert_value_to_TestValue, [lst])


def _try_to_convert_to_number(value):
    """Try to convert a string to a number (int or float)"""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def _generic_command(cmd_name, doc=None):
    """ Create a method that will query the cmd_name

    for example: _generic_get_command('CH1:IMPedance') will create the
    method whose name is _get_ch1_impedance

    By default this function try also to convert the output of the request into
    an int or a float otherwise it uses the out_conversion function.
    """
    def command(self):
        cmd_nameb = self._get_cmd_name(cmd_name)
        value = self._write('%s' % cmd_nameb)
        return None
    command.__name__ = '_%s' % (cmd_name.replace(':', '_').lower())
    command.__doc__ = command.__name__ if doc is None else doc
    return command


def _generic_get_command(cmd_name, out_conversion=None, doc=None):
    """ Create a method that will query the cmd_name

    for example: _generic_get_command('CH1:IMPedance') will create the
    method whose name is _get_ch1_impedance

    By default this function try also to convert the output of the request into
    an int or a float otherwise it uses the out_conversion function.
    """
    if out_conversion is None:
        out_conversion = _try_to_convert_to_number

    def get_val(self):
        cmd_nameb = self._get_cmd_name(cmd_name)
        cmd_nameb = cmd_nameb.split(' ')
        cmd_nameb[0] = cmd_nameb[0]+'?'
        value = self._ask('%s' % ' '.join(cmd_nameb))
        return out_conversion(value)
    get_val.__name__ = '_get_%s' % (cmd_name.replace(':', '_').lower())
    get_val.__doc__ = get_val.__name__ if doc is None else doc
    return get_val


def _generic_set_command(cmd_name, in_test=None, doc=None):
    """ Create a method that will set the cmd_name

    for example: _generic_set_command('CH1:IMPedance') will create the method
    whose name is _set_ch1_impedance and takes one parameter

    Optional argument :
        in_test : function that converts arguments to string.
    """
    if in_test is None:
        def set_val(self, value):
            cmd_nameb = self._get_cmd_name(cmd_name)
            self._write('%s %s' % (cmd_nameb, value))
    else:
        def set_val(self, args):
            if isinstance(args, tuple):
                param = in_test(*args)
            else:
                param = in_test(args)
            cmd_nameb = self._get_cmd_name(cmd_name)
            self._write('%s %s' % (cmd_nameb, param))
    set_val.__name__ = '_set_%s' % (cmd_name.replace(':', '_').lower())
    set_val.__doc__ = set_val.__name__ if doc is None else doc
    return set_val


class GenericCommandClass(object):
    @classmethod
    def get_argument_list(cls):
        out = []
        for elm in cls.__dict__:
            if elm.startswith('__'):
                continue
            if not isinstance(cls.__dict__[elm], Argument):
                continue
            out.append(cls.__dict__[elm])
#        out = sorted(out, cmp=lambda x,y:cmp(x.ordre, y.ordre))
        out = sorted(out, key=lambda x: x.ordre)
        return out

    @classmethod
    def get_argument_list_name(cls):
        out = []
        for elm in cls.__dict__:
            if elm.startswith('__'):
                continue
            if not isinstance(cls.__dict__[elm], Argument):
                continue
            out.append((elm, cls.__dict__[elm]))
#        out = sorted(out, cmp=lambda x,y:cmp(x[1].ordre, y[1].ordre))
        out = sorted(out, key=lambda x: x[1].ordre)
        return [elm.split('__')[-1] for (elm, _) in out]

    @classmethod
    def out_conversion(cls, value_str):
        arg_list = cls.get_argument_list()
        split_value = value_str.split(',')
        if len(split_value) > len(arg_list):
            return _try_to_convert_to_number(value_str.strip())
        out = []
        for i, val in enumerate(split_value):
            out.append(arg_list[i].convert(val))
        if len(out) == 0:
            return None
        if len(out) == 1:
            return out[0]
        return tuple(out)

    @classmethod
    def in_test(cls, *args):
        arg_list = cls.get_argument_list()
        if len(args) > len(arg_list):
            raise Exception("Error in function : too much arguments")
        out = []
        for i, elm in enumerate(args):
            out.append(arg_list[i].check(elm))
        return ','.join(out)

    @classmethod
    def to_dict(cls, name):
        return {name: _generic_command(cls.cmd, doc=cls._get_the_doc())}
    full_acces = ""

    @classmethod
    def _get_the_doc(cls):
        title = cls.full_acces+'()'
        out = cls.__doc__ + '\n\n'
        return _make_doc(out, title, _type='method')


def _clean_doc(s):
    return s.replace('\n        ', '\n')


def _make_doc(txt, title, _type='attribute'):
    txt = _clean_doc(txt)
    fmt = "* **{title}**\n\n  {txt}\n\n".format(title=title, txt=txt.strip().replace('\n', '\n  '))
    fmt = ".. py:{_type}:: ThorlabsPM100.{title}\n\n   {txt}\n\n".format(title=title, txt=txt.strip().replace('\n', '\n   '), _type=_type)
    return fmt


def _underline(s, val='-'):
    s = s.strip()
    return s + '\n' + val*len(s)+'\n\n'


class GenericGetCommandClass(GenericCommandClass):
    @classmethod
    def to_dict(cls, name):
        get_cmd = _generic_get_command(cls.cmd, cls.out_conversion,
                                       doc=cls.__doc__)
        return {name: property(get_cmd, doc=cls._get_the_doc()),
                get_cmd.__name__: get_cmd}

    @classmethod
    def _get_the_doc(cls):
        title = cls.full_acces
        out = ""
        out = "Read-only property\n\n"
        out += cls.__doc__ + "\n\n"
        args = cls.get_argument_list_name()
        if set(args) != set(['value']) and not len(args) == 0:
            out += "**Property value (read-only) :** "+','.join(args)+"\n\n"
        out += "**Initial SCPI command :** {0}\n\n".format(cls.cmd)
        return _make_doc(out, title)


class GenericSetCommandClass(GenericCommandClass):
    @classmethod
    def to_dict(cls, name):
        set_cmd = _generic_set_command(cls.cmd, cls.in_test, doc=cls.__doc__)
        return {name: property(lambda self: None, set_cmd,
                               doc=cls._get_the_doc()),
                set_cmd.__name__: set_cmd}

    @classmethod
    def _get_the_doc(cls):
        title = cls.full_acces
        out = ""
        out = "Write-only property\n\n"
        out += cls.__doc__ + "\n\n"
        args = cls.get_argument_list()
#        if set(args)<>set(['value']) and not len(args)==0:
#            out += "**Property value (write-only) :** "+','.join(args)+"\n\n"
        out += "**Property value (write-only) :** "+','\
               .join(map(str, args[0].list_test_value))+"\n\n"
        out += "**Initial SCPI command :** {0}\n\n".format(cls.cmd)
        return _make_doc(out, title)


class GenericGetSetCommandClass(GenericCommandClass):
    @classmethod
    def to_dict(cls, name):
        get_cmd = _generic_get_command(cls.cmd, cls.out_conversion,
                                       doc=cls.__doc__)
        set_cmd = _generic_set_command(cls.cmd, cls.in_test, doc=cls.__doc__)
        return {name: property(get_cmd, set_cmd, doc=cls._get_the_doc()),
                get_cmd.__name__: get_cmd, set_cmd.__name__: set_cmd}

    @classmethod
    def _get_the_doc(cls):
        title = cls.full_acces
        out = ""
        out = "Write or read property\n\n"
        out += cls.__doc__ + "\n\n"
#        args = cls.get_argument_list_name()
#        if set(args)<>set(['value']) and not len(args)==0:
#            out += "**Property value :** "+','.join(args)+"\n\n"
        args = cls.get_argument_list()
        out += "**Property value :** "+','\
               .join(map(str, args[0].list_test_value))+"\n\n"
        out += "**Initial SCPI command :** {0}\n\n".format(cls.cmd)
        return _make_doc(out, title)


class Argument(object):
    def __init__(self, ordre, list_value, default=None):
        self.ordre = ordre
        self.list_value = list_value
        self.list_test_value = self.create_list_test_value()
        self.default = default

    def create_list_test_value(self):
        list_test_value = []
        for elm in self.list_value:
            if isinstance(elm, str) and elm.startswith('<'):
                assert '>' in elm
                if elm.endswith('>'):
                    list_test_value.append(numbers.Number)
                else:
                    unit = elm[elm.find('>')+1:]
                    list_test_value.append(TestValueWithUnit(numbers.Number, unit))
            else:
                list_test_value.append(elm)
        return list_test_value

    def convert(self, val):
        list_test_value = _convert_list_value_to_list_of_TestValue(self.list_test_value)
        for test in list_test_value:
            a = test.from_string(val)
            if not isinstance(a, str):
                return a
        return val

    def check(self, value):
        list_test_value = _convert_list_value_to_list_of_TestValue(self.list_test_value)
        if value is None:
            value = self.default
        for test in list_test_value:
            a = test.test(value)
            if a is not None:
                return a
        raise ValueError("Error: set value is %s while it should be %s"
                         % (value,  ' or '.join(map(str, list_test_value))))


class GroupProperty(object):
    def __init__(self, cls):
        self._cls = cls

    def __get__(self, instance, owner):
        if instance is None:
            return self._cls
        return self._cls(instance)


class InstrumentMetaclass(type):
    """ Meta class used to create property from GeneriCommand object

    For example :
    class Test():
        __metaclass__ = InstrumentMetaclass
        # Create a property attribute and the method get_attribute and set_attribute
        .....
    """
    def __new__(cls, class_name, bases, dct):
        attrs = dict((name, value) for name, value in dct.items() if type(value) == type and issubclass(value, GenericCommandClass))
        attrsbis = dict((name, value) for name, value in dct.items() if type(value) == InstrumentMetaclass and issubclass(value, Group))

#        out =  dict((name, value) for name, value in dct.items() if not name.startswith('__'))       
        out = dct
        for (name, value) in attrs.items():
            out.update(value.to_dict(name))

        for (name, value) in attrsbis.items():
            out.update({name: GroupProperty(value)})

        out['_subgroups'] = attrsbis.keys()
        out['_property_list'] = attrs.keys()

        final_object = type.__new__(cls, class_name, bases, out)
        return final_object


class InstrumentCommand(object):
    def _get_cmd_name(self, cmd_name):
        return cmd_name

    @classmethod
    def _get_the_doc(cls):
        out = ""
        out += _underline('Main commands', '=')
        for elm in cls._property_list:
            out += getattr(cls, elm).__doc__ + '\n\n'
        for elm in cls._subgroups:
            out += _underline('Group %s' % elm, '=')
            out += getattr(cls, elm)._get_the_doc()
        return out


class Group(object):
    """ This class is used to group command

    For example, if we want to use the command scope.Acquisition.StartTime,
    the object returned by scope.Acquisition is an instance of Group

    In order to add a group to an instrument:
    1) Define the class of the group that herits from Group
    2) Add an instance of the defined class in the __init__ of the instrument
    """
    def __init__(self, parent):
        self._parent = parent

    def _write(self, s):
        return self._parent._write(s)

    def _ask(self, s):
        return self._parent._ask(s)

    def _get_cmd_name(self, cmd_name):
        return self._parent._get_cmd_name(cmd_name)

    @classmethod
    def _get_the_doc(cls):
        out = ""
        for elm in cls._subgroups:
            out += getattr(cls, elm)._get_the_doc()
        for elm in cls._property_list:
            out += getattr(cls, elm).__doc__ + '\n\n'
        return out


class IndexedGroup(Group):
    """ This class is used to group command with a parameter

    For example, if we want to use the command scope.Channels[1].Offset,
    the object returned by scope.Channels is an instance of IndexedGroup

    In order to add a group to an instrument:
    1) Define the class of the group that herits from IndexedGroup
    2) Specify the attribute var that defines the string to replace with the
       item number in the command
    """
    def __init__(self, parent, item=0):
        Group.__init__(self, parent)
        self._item = item

    def __getitem__(self, i):
        out = self.__class__(self._parent, i)
        return out

    def _get_cmd_name(self, cmd_name):
        new_cmd = self._parent._get_cmd_name(cmd_name).replace(self.var,
                                                               str(self._item))
        return new_cmd


