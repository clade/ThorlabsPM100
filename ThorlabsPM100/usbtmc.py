import os


class USBTMC(object):
    """Simple implementation of a USBTMC device driver, in the style of visa.h
    """

    def __init__(self, device="/dev/usbtmc0"):
        self.device = device
        self.FILE = os.open(device, os.O_RDWR)

    def write(self, command):
        os.write(self.FILE, command.encode('ascii'))

    def read(self, length=None):
        if length is None:
            length = 4000
        return os.read(self.FILE, length)

    def query(self, command, length=None):
        self.write(command)
        return self.read(length=length).decode('ascii')

    def ask_for_value(self, command):
        return eval(self.ask(command).strip())

    def getName(self):
        return self.ask("*IDN?")

    def sendReset(self):
        self.write("*RST")

if __name__ == "__main__":
    inst = USBTMC()
