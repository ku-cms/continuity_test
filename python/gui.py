# gui.py

from tkinter import *
from client import Client
import os
import platform
import datetime

class GUI():
    
    def __init__(self, root, client):
        self.root           = root
        self.client         = client
        self.cable_number   = -1
        self.cable_type     = ""
        self.testing_stage  = ""
        self.testing_stages = [
            "Stage 1",
            "Stage 2",
            "Stage 3"
        ]
        self.cable_types    = [
            "Type 1",
            "Type 2",
            "Type 3",
            "Type 4",
            "Type 5"
        ]
        # set colors
        self.setColors()
        # run GUI
        self.run()

    def setColors(self):
        self.color_label_fg  = "gray95"
        self.color_label_bg  = "gray45"
        self.color_button_fg = "gray10"

    def run(self):
        button_padx = 10
        button_pady = 10
        # Frames
        self.frame_top = Frame(
            self.root,
            bg=self.color_label_bg,
            height=100
        )
        self.frame_middle = Frame(
            self.root,
            bg=self.color_label_bg,
            height=100
        )
        self.frame_bottom = Frame(
            self.root,
            bg=self.color_label_bg,
            height=200
        )
        self.frame_top.pack(side=TOP,    fill=BOTH, expand=True)
        self.frame_middle.pack(side=TOP, fill=BOTH, expand=True)
        self.frame_bottom.pack(side=TOP, fill=BOTH, expand=True)
        # Widgets
        
        # testing stage menu
        self.entry_testing_stage = StringVar(self.root)
        self.entry_testing_stage.set(self.testing_stages[0])
        self.testing_stage_menu = OptionMenu(
            self.frame_middle,
            self.entry_testing_stage,
            *self.testing_stages
        )
        self.testing_stage_menu.config(font=("Arial", 20))
        
        # cable type menu
        self.entry_cable_type = StringVar(self.root)
        self.entry_cable_type.set(self.cable_types[0])
        self.cable_type_menu = OptionMenu(
            self.frame_middle,
            self.entry_cable_type,
            *self.cable_types
        )
        self.cable_type_menu.config(font=("Arial", 20))
        
        self.label_title = Label(
            self.frame_top,
            text="Cable Continuity Tester",
            font=("Arial", 30),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=40
        )
        self.label_cable_number = Label(
            self.frame_middle,
            text="Cable Number",
            font=("Arial", 20),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=20
        )
        self.label_testing_stage = Label(
            self.frame_middle,
            text="Testing Stage",
            font=("Arial", 20),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=20
        )
        self.label_output = Label(
            self.frame_bottom,
            text="Output",
            font=("Arial", 30),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=40
        )
        self.button_read = Button(
            self.frame_middle,
            text="Read",
            font=("Arial", 20),
            command=self.read,
            fg=self.color_button_fg,
            bg="gold"
        )
        self.button_log = Button(
            self.frame_middle,
            text="Log",
            font=("Arial", 20),
            command=self.log,
            fg=self.color_button_fg,
            bg="maroon1"
        )
        self.button_start = Button(
            self.frame_middle,
            text="Start",
            font=("Arial", 20),
            command=self.start,
            fg=self.color_button_fg,
            bg="SpringGreen3"
        )
        self.button_clear = Button(
            self.frame_middle,
            text="Clear",
            font=("Arial", 20),
            command=self.clear,
            fg=self.color_button_fg,
            bg="firebrick1"
        )
        self.button_select = Button(
            self.frame_middle,
            text="Select Cable",
            command=self.select,
            font=("Arial", 20),
            fg=self.color_button_fg,
            bg="deep sky blue"
        )
        self.entry_cable_number = Entry(
            self.frame_middle,
            font=("Arial", 20)
        )
        self.text_box = Text(
            self.frame_bottom,
            font=("Arial", 14),
            height=20,
            width=80
        )
        
        # Frame
        self.label_title.grid(           row=1, column=1)
        # center grid using surrounding empty rows/columns as padding to fill space
        self.frame_top.grid_rowconfigure(0,       weight=1)
        self.frame_top.grid_rowconfigure(2,       weight=1)
        self.frame_top.grid_columnconfigure(0,    weight=1)
        self.frame_top.grid_columnconfigure(2,    weight=1)
        # Frame
        self.label_cable_number.grid(    row=1, column=1, padx=button_padx, pady=button_pady)
        self.entry_cable_number.grid(    row=1, column=2, padx=button_padx, pady=button_pady)
        self.label_testing_stage.grid(   row=2, column=1, padx=button_padx, pady=button_pady)
        self.testing_stage_menu.grid(    row=2, column=2, padx=button_padx, pady=button_pady)
        self.button_read.grid(           row=3, column=1, padx=button_padx, pady=button_pady)
        self.button_log.grid(            row=3, column=2, padx=button_padx, pady=button_pady)
        self.button_start.grid(          row=4, column=1, padx=button_padx, pady=button_pady)
        self.button_clear.grid(          row=4, column=2, padx=button_padx, pady=button_pady)
        self.button_select.grid(         row=5, column=1, padx=button_padx, pady=button_pady)
        self.cable_type_menu.grid(       row=5, column=2, padx=button_padx, pady=button_pady)
        # center grid using surrounding empty rows/columns as padding to fill space
        self.frame_middle.grid_rowconfigure(0,       weight=1)
        self.frame_middle.grid_rowconfigure(6,       weight=1)
        self.frame_middle.grid_columnconfigure(0,    weight=1)
        self.frame_middle.grid_columnconfigure(3,    weight=1)
        # Frame
        self.label_output.grid(          row=1, column=1)
        self.text_box.grid(              row=2, column=1, padx=20, pady=20)
        # center grid using surrounding empty rows/columns as padding to fill space
        self.frame_bottom.grid_rowconfigure(0,       weight=1)
        self.frame_bottom.grid_rowconfigure(3,       weight=1)
        self.frame_bottom.grid_columnconfigure(0,    weight=1)
        self.frame_bottom.grid_columnconfigure(2,    weight=1)

    def checkCableNumber(self):
        # Require that cable number is a positive integer
        try:
            value = self.entry_cable_number.get()
            n = int(value)
            if n > 0:
                return True
            else:
                return False
        except ValueError:
            return False
    
    def getEntryCableNumber(self):
        return int(self.entry_cable_number.get())
    
    def getEntryCableType(self):
        return str(self.entry_cable_type.get())

    def getEntryTestingStage(self):
        return str(self.entry_testing_stage.get())

    def getCableNumber(self):
        return self.cable_number
    
    def getCableType(self):
        return self.cable_type
    
    def getTestingStage(self):
        return self.testing_stage
    
    def setCableNumber(self, value):
        self.cable_number = value
    
    def setCableType(self, value):
        self.cable_type = value
    
    def setTestingStage(self, value):
        self.testing_stage = value
    
    def makeDir(self, dir_name):
        # make directory if it does not exist
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    def getLogFileName(self, log_dir):
        # log file name has cable number, testing stage, and run number
        # get testing stage (number only)
        stage = self.getTestingStage().split(" ")[1]
        run = 1
        log_file = "{0}/cable{1}_stage{2}_run{3}.log".format(log_dir, self.getCableNumber(), stage, run)
        while(os.path.exists(log_file)):
            # get unique log file name by incremeting run number
            run += 1
            log_file = "{0}/cable{1}_stage{2}_run{3}.log".format(log_dir, self.getCableNumber(), stage, run)
        return log_file

    def write(self, data):
        print(data)
        self.text_box.insert(END, data + "\n")

    def read(self):
        self.write("READ")
        data = self.client.read(timeout=15, nbytes=100000)
        self.write(data)
        return

    def log(self):
        # first check if cable number is valid
        valid_number = self.checkCableNumber()
        if valid_number:
            # set values from entries
            self.setCableNumber(self.getEntryCableNumber())
            self.setTestingStage(self.getEntryTestingStage())
            self.write("LOG")
            log_dir = "logs"
            self.makeDir(log_dir)
            log_file = self.getLogFileName(log_dir)
            with open(log_file, "w") as f:
                f.write(self.text_box.get("1.0", END))
            return
        else:
            self.write("ERROR: Please enter a cable number (must be a positive integer).")
            return


    def start(self):
        # first check if cable number is valid
        valid_number = self.checkCableNumber()
        if valid_number:
            # set values from entries
            self.setCableNumber(self.getEntryCableNumber())
            self.setTestingStage(self.getEntryTestingStage())
            time = datetime.datetime.now()
            self.write("--------------------------------------------------------------")
            self.write("START")
            self.write("Date and time: {0}".format(time))
            self.write("Cable number: {0}".format(self.getCableNumber()))
            self.write("Testing stage: {0}".format(self.getTestingStage()))
            self.write("--------------------------------------------------------------")
            x = "y\n"
            self.client.write(timeout=1, data=x)
            self.read()
            return
        else:
            self.write("ERROR: Please enter a cable number (must be a positive integer).")
            return
    
    def clear(self):
        self.write("CLEAR")
        # delete cable number entry
        self.entry_cable_number.delete(0, END)
        # delete data in text box
        self.text_box.delete("1.0", END)
        return
    
    def select(self):
        # set values from entries
        self.setCableType(self.getEntryCableType())
        self.write("SELECT {0}".format(self.getCableType()))
        # get cable type (number only) to send via client
        n = self.getCableType().split(" ")[1]
        x = str(n) + "\n"
        self.client.write(timeout=1, data=x)
        self.read()
        return

def main():
    port        = ''
    baudrate    = 115200 

    # Set serial port based on operating system
    if platform.system() == 'Windows':  
        port = 'COM3'
    elif platform.system() == 'Linux':  
        port = '/dev/ttyACM0'
    else:
        print("WARNING: serial port not set for your operating system.")
    
    # Run GUI
    root        = Tk()
    client      = Client(port, baudrate)
    app         = GUI(root, client)
    root.mainloop()

if __name__ == "__main__":
    main()

