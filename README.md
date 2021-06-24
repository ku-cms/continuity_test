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

