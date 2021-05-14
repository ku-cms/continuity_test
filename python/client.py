# client.py
import serial

def read(port, baudrate, timeout, nbytes):
    with serial.Serial(port=port, baudrate=baudrate, timeout=timeout) as ser:
        x = ser.read(nbytes)
        s = x.decode("utf-8")
        return s

def write(port, baudrate, timeout, data):
    with serial.Serial(port=port, baudrate=baudrate, timeout=timeout) as ser:
        ser.write(data)

def beginTest(port, baudrate, timeout, data):
    # WARNING: include one space at end of string
    question = "Press enter to begin continuity test: "
    if data.endswith(question):
        print("Smashing enter!")
        x = "\n"
        x = x.encode("utf-8")
        write(port, baudrate, timeout, x)

def selectCable(port, baudrate, timeout, data, cable_type):
    # WARNING: include one space at end of string
    question = "Select which kind of cable is being tested (1-5): "
    if data.endswith(question):
        print("Selecting cable type ({0})".format(cable_type))
        x = str(cable_type) + "\n"
        x = x.encode("utf-8")
        write(port, baudrate, timeout, x)
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
    
    data = read(port, baudrate, timeout_read, nbytes)
    print(data)
    
    beginTest(port, baudrate, timeout_write, data)
    
    data = read(port, baudrate, timeout_read, nbytes)
    print(data)
    
    # select cable type (if not found automatically)
    selected = selectCable(port, baudrate, timeout_write, data, cable_type)
    
    # only read more data if selection was required
    if selected:
        data = read(port, baudrate, timeout_read, nbytes)
        print(data)

if __name__ == "__main__":
    main()

