# client.py

import serial

class Client():
    
    def __init__(self, port, baudrate):
        self.port       = port
        self.baudrate   = baudrate

    def read(self, timeout, nbytes):
        print("read(): port = {0}, baudrate = {1}".format(self.port, self.baudrate))
        # read data from serial port
        try:
            with serial.Serial(port=self.port, baudrate=self.baudrate, timeout=timeout) as ser:
                x = ser.read(nbytes)
                s = x.decode("utf-8")
                return s
        except:
            message = "ERROR: Cannot read from serial port. Check ZedBoard connection and power."
            print(message)
            return message
    
    def write(self, timeout, data):
        print("write(): port = {0}, baudrate = {1}".format(self.port, self.baudrate))
        # string needs to be encoded
        data_encoded = data.encode("utf-8")
        # write data to serial port
        try:
            with serial.Serial(port=self.port, baudrate=self.baudrate, timeout=timeout) as ser:
                ser.write(data_encoded)
        except:
            message = "ERROR: Cannot write to serial port. Check ZedBoard connection and power."
            print(message)
    
    def beginTest(self, timeout, data):
        # WARNING: include one space at end of string
        question = "Press enter to begin continuity test: "
        if data.endswith(question):
            print("Smashing enter!")
            x = "\n"
            self.write(timeout, x)
    
    def selectCable(self, timeout, data, cable_type):
        # WARNING: include one space at end of string
        question = "Select which kind of cable is being tested (1-5): "
        if data.endswith(question):
            print("Selecting cable type ({0})".format(cable_type))
            x = str(cable_type) + "\n"
            self.write(timeout, x)
            return True
        else:
            return False

def main():
    port            = '/dev/ttyACM0'
    baudrate        = 115200 
    timeout_read    = 15
    timeout_write   = 1
    nbytes          = 100000
    cable_type      = 1

    client = Client(port, baudrate)
    
    data = client.read(timeout_read, nbytes)
    print(data)
    
    client.beginTest(timeout_write, data)
    
    data = client.read(timeout_read, nbytes)
    print(data)
    
    # select cable type (if not found automatically)
    selected = client.selectCable(timeout_write, data, cable_type)
    
    # only read more data if selection was required
    if selected:
        data = client.read(timeout_read, nbytes)
        print(data)

if __name__ == "__main__":
    main()

