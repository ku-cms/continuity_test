# gui.py

from tkinter import *
from client import Client
import argparse
import os
import platform
import datetime

class GUI():
    
    def __init__(self, root, client, vertical_layout=False):
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
        # use vertical layout
        self.useVerticalLayout = vertical_layout
        # set colors
        self.setColors()
        # run GUI
        self.run()

    def setColors(self):
        self.color_label_fg  = "gray95"
        self.color_label_bg  = "gray45"
        self.color_button_fg = "gray10"

    def run(self):

        # There are vertical and horizontal layouts supported.

        # Vertical Layout
        # frame_1
        # frame_3
        # frame_4

        # Horizontal Layout
        # frame_1 --- frame_2
        # frame_3 --- frame_4
        
        # Frames
        self.frame_1 = Frame(
            self.root,
            bg=self.color_label_bg,
            height=100,
            width=100
        )
        self.frame_2 = Frame(
            self.root,
            bg=self.color_label_bg,
            height=100,
            width=100
        )
        self.frame_3 = Frame(
            self.root,
            bg=self.color_label_bg,
            height=200, 
            width=100
        )
        self.frame_4 = Frame(
            self.root,
            bg=self.color_label_bg,
            height=200,
            width=100
        )
        
        # Parameters
        button_padx = 10
        button_pady = 10
        if self.useVerticalLayout:
            title_width         = 40
            label_output_width  = 40
            text_box_height     = 20
            text_box_width      = 80
            label_output_frame  = self.frame_4
        else:
            title_width         = 20
            label_output_width  = 20
            text_box_height     = 20
            text_box_width      = 50
            label_output_frame  = self.frame_2
        
        # ----------------------- #
        # --- Vertical Layout --- #
        # ----------------------- #
        if self.useVerticalLayout:
            # use fill=BOTH, expand=True so that frames fill space!
            self.frame_1.pack(side=TOP, fill=BOTH, expand=True)
            self.frame_3.pack(side=TOP, fill=BOTH, expand=True)
            self.frame_4.pack(side=TOP, fill=BOTH, expand=True)
        
        # ------------------------- #
        # --- Horizontal Layout --- #
        # ------------------------- #
        else:
            # use sticky=E + W + N + S so that frames fill space!!
            self.frame_1.grid(row=0, column=0, sticky=E + W + N + S) 
            self.frame_2.grid(row=0, column=1, sticky=E + W + N + S) 
            self.frame_3.grid(row=1, column=0, sticky=E + W + N + S) 
            self.frame_4.grid(row=1, column=1, sticky=E + W + N + S) 
        
        # Widgets
        
        # testing stage menu
        self.entry_testing_stage = StringVar(self.root)
        self.entry_testing_stage.set(self.testing_stages[0])
        self.testing_stage_menu = OptionMenu(
            self.frame_3,
            self.entry_testing_stage,
            *self.testing_stages
        )
        self.testing_stage_menu.config(font=("Arial", 20))
        
        # cable type menu
        self.entry_cable_type = StringVar(self.root)
        self.entry_cable_type.set(self.cable_types[0])
        self.cable_type_menu = OptionMenu(
            self.frame_3,
            self.entry_cable_type,
            *self.cable_types
        )
        self.cable_type_menu.config(font=("Arial", 20))
        
        self.label_title = Label(
            self.frame_1,
            text="Cable Continuity Tester",
            font=("Arial", 30),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=title_width
        )
        self.label_cable_number = Label(
            self.frame_3,
            text="Cable Number",
            font=("Arial", 20),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=20
        )
        self.label_testing_stage = Label(
            self.frame_3,
            text="Testing Stage",
            font=("Arial", 20),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=20
        )
        self.label_output = Label(
            label_output_frame,
            text="Output",
            font=("Arial", 30),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=label_output_width
        )
        self.button_read = Button(
            self.frame_3,
            text="Read",
            font=("Arial", 20),
            command=self.read,
            fg=self.color_button_fg,
            bg="gold"
        )
        self.button_log = Button(
            self.frame_3,
            text="Log",
            font=("Arial", 20),
            command=self.log,
            fg=self.color_button_fg,
            bg="maroon1"
        )
        self.button_start = Button(
            self.frame_3,
            text="Start",
            font=("Arial", 20),
            command=self.start,
            fg=self.color_button_fg,
            bg="SpringGreen3"
        )
        self.button_clear = Button(
            self.frame_3,
            text="Clear",
            font=("Arial", 20),
            command=self.clear,
            fg=self.color_button_fg,
            bg="firebrick1"
        )
        self.button_select = Button(
            self.frame_3,
            text="Select Cable",
            command=self.select,
            font=("Arial", 20),
            fg=self.color_button_fg,
            bg="deep sky blue"
        )
        self.entry_cable_number = Entry(
            self.frame_3,
            font=("Arial", 20)
        )
        self.text_box = Text(
            self.frame_4,
            font=("Arial", 14),
            height=text_box_height,
            width=text_box_width
        )
        
        # Frame: title
        self.label_title.grid(           row=1, column=1)
        
        # center grid using surrounding empty rows/columns as padding to fill space
        self.frame_1.grid_rowconfigure(0,    weight=1)
        self.frame_1.grid_rowconfigure(2,    weight=1)
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(2, weight=1)
        
        # Frame: user input (buttons, text, etc)
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
        self.frame_3.grid_rowconfigure(0,    weight=1)
        self.frame_3.grid_rowconfigure(6,    weight=1)
        self.frame_3.grid_columnconfigure(0, weight=1)
        self.frame_3.grid_columnconfigure(3, weight=1)
        
        # ----------------------- #
        # --- Vertical Layout --- #
        # ----------------------- #
        if self.useVerticalLayout:
            # Frame: output
            self.label_output.grid( row=1, column=1)
            self.text_box.grid(     row=2, column=1, padx=20, pady=20)
        
            # center grid using surrounding empty rows/columns as padding to fill space
            self.frame_4.grid_rowconfigure(0,    weight=1)
            self.frame_4.grid_rowconfigure(3,    weight=1)
            self.frame_4.grid_columnconfigure(0, weight=1)
            self.frame_4.grid_columnconfigure(2, weight=1)
        
        # ------------------------- #
        # --- Horizontal Layout --- #
        # ------------------------- #
        else:
            # Frame: output label
            self.label_output.grid(row=1, column=1)
            
            # center grid using surrounding empty rows/columns as padding to fill space
            self.frame_2.grid_rowconfigure(0,    weight=1)
            self.frame_2.grid_rowconfigure(2,    weight=1)
            self.frame_2.grid_columnconfigure(0, weight=1)
            self.frame_2.grid_columnconfigure(2, weight=1)
            
            # Frame: output text box
            self.text_box.grid(row=1, column=1, padx=20, pady=20)
            
            # center grid using surrounding empty rows/columns as padding to fill space
            self.frame_4.grid_rowconfigure(0,    weight=1)
            self.frame_4.grid_rowconfigure(2,    weight=1)
            self.frame_4.grid_columnconfigure(0, weight=1)
            self.frame_4.grid_columnconfigure(2, weight=1)


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
        data = self.client.read(timeout=5, nbytes=100000)
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
            with open(log_file, "w", newline='') as f:
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
    # options
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--vertical_layout", "-v", default=False, action="store_true", help="use vertical layout (default is horizontal)")
    
    options         = parser.parse_args()
    vertical_layout = options.vertical_layout

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
    root   = Tk()
    client = Client(port, baudrate)
    app    = GUI(root, client, vertical_layout)
    root.mainloop()

if __name__ == "__main__":
    main()

