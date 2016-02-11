""" This module is used to list all the available VISA objects


"""

import visa
from pyvisa import vpp43

class VisaObjectList():
    """ Create a list of available VISA objects
    
    
    """
    def __init__(self):
        resource_names = []
        find_list, return_counter, instrument_description = \
                  vpp43.find_resources(visa.resource_manager.session, "?*")
        resource_names.append(instrument_description)
           
        for i in range(return_counter - 1):
            resource_names.append(vpp43.find_next(find_list))
       
    #    print "\nVisa resources found:"
    #    for a in range(len(resource_names)):
    #        print a, resource_names[a]
    #    print "Attempting to Identify Instruments. Please Wait..."
    
        resource_ids = []
        for a in range(len(resource_names)):
            interface_type, _ = \
            vpp43.parse_resource(visa.resource_manager.session, resource_names[a])
            if interface_type == visa.VI_INTF_ASRL:
                resource_ids.append("RS232 not Supported")
            else:
                try:
                    tempscope = visa.instrument(resource_names[a], timeout = 10)
                    scopename = tempscope.ask("*IDN?")
                    scopename = scopename.split(',')
                    resource_ids.append(scopename[0] + '-' + scopename[1] + \
                                        ' ' + scopename[2])
                except visa.VisaIOError:
                    resource_ids.append(" No Instrument Found ")
                except:
                    resource_ids.append(" Error Communicating with this device")
        self.resource_names = resource_names
        self.resource_ids = resource_ids
    def get_instrument(self, name, param_type=None):
        """Return an instrument instance
        
        name : the name of the instrument
            name can be 
                - a number (item in the list of detected instrument)
                - a string representing the visa resource name or id
            param_type : 'number', 'resource_name', 'resource_id'
                if None, try to automatically detect the param_type
                
        """
        if param_type is None:
            if type(name) is int:
                param_type = 'number'
            else:
                if name.find('::')>=0:
                    param_type = "resource_name"
                else:
                    param_type = "resource_id"
        if param_type=='number':
            return visa.instrument(self.resource_names[name])
        elif param_type=='resource_name':
            return visa.instrument(name)
        else:
            return visa.instrument(self.resource_names[self.resource_ids.index(name)])
    def __repr__(self):
        return '\n'.join(["%i : %s : %s"%(i, self.resource_names[i], 
                                          self.resource_ids[i])
                        for i in range(len(self.resource_names))])
   
