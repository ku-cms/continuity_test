# continuity_test

This repository has a python GUI and client to run the continuity tests on cables using a ZedBoard and L board.
The ZedBoard needs to be running the continuity test firmware to perform these tests.

The following python3 packages are required:
```
pip install tk
pip install pyserial
```

Use python3 to start the GUI:
```
python3 python/gui.py
```

The client class that communicates on a serial port is defined here:
```
python/client.py
```
If needed, you can also connect a terminal to the serial port using TeraTerm (in Windows) or picocom (in Linux).

Here are terminal commands for using picocom in Linux:

Search for the device in /dev:
```
ls -l /dev | grep ttyACM
```

Start picocom using device (e.g. ttyAMC0):
```
sudo picocom -b 115200 -r -l /dev/ttyACM0
```

To see help menu in picocom, use CTRL+A, CTRL+H.

To exist picocom, use CTRL+A, CTRL+X.

